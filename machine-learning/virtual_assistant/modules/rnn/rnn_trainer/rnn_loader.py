import torch
from torch import optim

from modules.rnn.rnn_tools.rnn_decoder import decoder, embedding
from modules.rnn.rnn_tools.rnn_encoder import RNNEncoder

from modules.handlers.data_handler.data_cleaner import (
    voc,
    pairs,
)

from modules.handlers.learning_handler import (
    device,
    voc_directory,
    hidden_size,
    dropout,
    batch_size,
    print_every,
    save_every,
    clip,
    data_directory,
    loadFilename,
    n_iteration,
    encoder_n_layers,
    decoder_n_layers,
    learning_rate,
    decoder_learning_ratio,
    model_name,
)


# Load model if a loadFilename is provided
from modules.rnn.rnn_trainer.rnn_trainer import train_iterations

if loadFilename:
    # If loading on same machine the model was trained on
    checkpoint = torch.load(loadFilename)
    # If loading a model trained on GPU to CPU
    # checkpoint = torch.load(loadFilename, map_location=torch.device('cpu'))
    encoder_sd = checkpoint["en"]
    decoder_sd = checkpoint["de"]
    encoder_optimizer_sd = checkpoint["en_opt"]
    decoder_optimizer_sd = checkpoint["de_opt"]
    embedding_sd = checkpoint["embedding"]
    voc.__dict__ = checkpoint["voc_dict"]

print("Building encoder and decoder ...")
# Initialize word embeddings
if loadFilename:
    embedding.load_state_dict(embedding_sd)
# Initialize encoder & decoder models
encoder = RNNEncoder(hidden_size, embedding, encoder_n_layers, dropout)
if loadFilename:
    encoder.load_state_dict(encoder_sd)
    decoder.load_state_dict(decoder_sd)

# Use appropriate device
encoder = encoder.to(device)
decoder = decoder.to(device)
print("Models built and ready to go!")

# Ensure dropout layers are in train mode
encoder.train()
decoder.train()

# Initialize optimizers
print("Building optimizers...")
encoder_optimizer = optim.Adam(encoder.parameters(), lr=learning_rate)
decoder_optimizer = optim.Adam(
    decoder.parameters(), lr=learning_rate * decoder_learning_ratio
)
if loadFilename:
    encoder_optimizer.load_state_dict(encoder_optimizer_sd)
    decoder_optimizer.load_state_dict(decoder_optimizer_sd)

# # If you have cuda, configure cuda to call
# for state in encoder_optimizer.state.values():
#     for k, v in state.items():
#         if isinstance(v, torch.Tensor):
#             state[k] = v.cuda()

# for state in decoder_optimizer.state.values():
#     for k, v in state.items():
#         if isinstance(v, torch.Tensor):
#             state[k] = v.cuda()

# Run training iterations
print("Starting Training!")
train_iterations(
    model_name,
    voc,
    pairs,
    encoder,
    decoder,
    encoder_optimizer,
    decoder_optimizer,
    embedding,
    encoder_n_layers,
    decoder_n_layers,
    voc_directory,
    n_iteration,
    batch_size,
    print_every,
    save_every,
    clip,
    data_directory,
    loadFilename,
)
