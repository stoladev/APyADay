from abc import ABC

import torch
import torch.nn as nn
import torch.nn.functional as functional

from modules.handlers.data_handler.data_cleaner import voc
from modules.handlers.learning_handler import device, SOS_token, attn_model, hidden_size, decoder_n_layers, dropout
from utils import debug


def dot_score(hidden, encoder_output):
    return torch.sum(hidden * encoder_output, dim=2)


class Attn(nn.Module, ABC):
    def __init__(self, method, hidden_size):
        super(Attn, self).__init__()
        self.method = method
        if self.method not in ["dot", "general", "concat"]:
            raise ValueError(self.method, "is not an appropriate attention method.")
        self.hidden_size = hidden_size
        if self.method == "general":
            self.attn = nn.Linear(self.hidden_size, hidden_size)
        elif self.method == "concat":
            self.attn = nn.Linear(self.hidden_size * 2, hidden_size)
            self.v = nn.Parameter(torch.FloatTensor(hidden_size))

    def general_score(self, hidden, encoder_output):
        energy = self.attn(encoder_output)
        return torch.sum(hidden * energy, dim=2)

    def concat_score(self, hidden, encoder_output):
        energy = self.attn(
            torch.cat(
                (hidden.expand(encoder_output.size(0), -1, -1), encoder_output), 2
            )
        ).tanh()
        return torch.sum(self.v * energy, dim=2)

    def forward(self, hidden, encoder_outputs):
        # Calculate the attention weights (energies) based on the given method
        if self.method == "general":
            attn_energies = self.general_score(hidden, encoder_outputs)
        elif self.method == "concat":
            attn_energies = self.concat_score(hidden, encoder_outputs)
        elif self.method == "dot":
            attn_energies = dot_score(hidden, encoder_outputs)
        else:
            debug.log("No attn energies.")
            return

        # Transpose max_length and batch_size dimensions
        attn_energies = attn_energies.t()

        # Return the softmax normalized probability scores (with added dimension)
        return functional.softmax(attn_energies, dim=1).unsqueeze(1)


class AttnRNNDecoder(nn.Module, ABC):
    def __init__(
            self, attn_model_used, embedding_used, hidden_size_used, output_size_used, dropout_used=0.1, n_layers=1
    ):
        super(AttnRNNDecoder, self).__init__()

        # Keep for reference
        self.attn_model = attn_model_used
        self.hidden_size = hidden_size_used
        self.output_size = output_size_used
        self.n_layers = n_layers
        self.dropout = dropout_used

        # Define layers
        self.embedding = embedding_used
        self.embedding_dropout = nn.Dropout(dropout_used)
        self.gru = nn.GRU(
            hidden_size_used,
            hidden_size_used,
            n_layers,
            dropout=(0 if n_layers == 1 else dropout_used),
        )
        self.concat = nn.Linear(hidden_size_used * 2, hidden_size_used)
        self.out = nn.Linear(hidden_size_used, output_size_used)

        self.attn = Attn(attn_model_used, hidden_size_used)

    def forward(self, input_step, last_hidden, encoder_outputs):
        # Note: we run this one step (word) at a time
        # Get embedding of current input word
        embedded = self.embedding(input_step)
        embedded = self.embedding_dropout(embedded)
        # Forward through unidirectional GRU
        rnn_output, hidden = self.gru(embedded, last_hidden)
        # Calculate attention weights from the current GRU output
        attn_weights = self.attn(rnn_output, encoder_outputs)
        # Multiply attention weights to encoder outputs to get new "weighted sum" context vector
        context = attn_weights.bmm(encoder_outputs.transpose(0, 1))
        # Concatenate weighted context vector and GRU output using Luong eq. 5
        rnn_output = rnn_output.squeeze(0)
        context = context.squeeze(1)
        concat_input = torch.cat((rnn_output, context), 1)
        concat_output = torch.tanh(self.concat(concat_input))
        # Predict next word using Luong eq. 6
        output = self.out(concat_output)
        output = functional.softmax(output, dim=1)
        # Return output and final hidden state
        return output, hidden


class SearchDecoder(nn.Module, ABC):
    def __init__(self, encoder_used, decoder_used):
        super(SearchDecoder, self).__init__()
        self.encoder = encoder_used
        self.decoder = decoder_used

    def forward(self, input_seq, input_length, max_length):
        # Forward input through encoder model
        encoder_outputs, encoder_hidden = self.encoder(input_seq, input_length)
        # Prepare encoder's final hidden layer to be first hidden input to the decoder
        decoder_hidden = encoder_hidden[: decoder.n_layers]
        # Initialize decoder input with SOS_token
        decoder_input = torch.ones(1, 1, device=device, dtype=torch.long) * SOS_token
        # Initialize tensors to append decoded words to
        all_tokens = torch.zeros([0], device=device, dtype=torch.long)
        all_scores = torch.zeros([0], device=device)
        # Iteratively decode one word token at a time
        for _ in range(max_length):
            # Forward pass through decoder
            decoder_output, decoder_hidden = self.decoder(
                decoder_input, decoder_hidden, encoder_outputs
            )
            # Obtain most likely word token and its softmax score
            decoder_scores, decoder_input = torch.max(decoder_output, dim=1)
            # Record token and score
            all_tokens = torch.cat((all_tokens, decoder_input), dim=0)
            all_scores = torch.cat((all_scores, decoder_scores), dim=0)
            # Prepare current token to be next decoder input (add a dimension)
            decoder_input = torch.unsqueeze(decoder_input, 0)
        # Return collections of word tokens and scores
        return all_tokens, all_scores


embedding = nn.Embedding(voc.num_words, hidden_size)

decoder = AttnRNNDecoder(attn_model, embedding, hidden_size, voc.num_words, dropout, decoder_n_layers)
