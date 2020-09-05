from modules.handlers.data_handler.data_cleaner import normalize_string, MAX_LENGTH, indexes_from_sentence, voc
from modules.handlers.learning_handler import device, datafile
import torch

from modules.rnn.rnn_tools.rnn_decoder import SearchDecoder
from modules.rnn.rnn_trainer.rnn_loader import encoder, decoder


def evaluate(searcher, voc_item, sentence, max_length=MAX_LENGTH):
    # words -> indexes
    indexes_batch = [indexes_from_sentence(voc_item, sentence)]

    # Create lengths tensor
    lengths = torch.tensor([len(indexes) for indexes in indexes_batch])

    # Transpose dimensions of batch to match models' expectations
    input_batch = torch.LongTensor(indexes_batch).transpose(0, 1)

    # Use appropriate device
    input_batch = input_batch.to(device)
    lengths = lengths.to(device)

    # Decode sentence with searcher
    tokens, scores = searcher(input_batch, lengths, max_length)

    # indexes -> words
    decoded_words = [voc_item.index2word[token.item()] for token in tokens]
    return decoded_words


def evaluate_input(searcher, voc_item):
    input_sentence = ""
    while 1:
        try:
            # Get input sentence
            input_sentence = input("> ")
            # Check if it is quit case
            if input_sentence == "q" or input_sentence == "quit":
                break
            # Normalize sentence
            input_sentence = normalize_string(input_sentence)
            # Evaluate sentence
            output_words = evaluate(searcher, voc_item, input_sentence)
            # Format and print response sentence
            output_words[:] = [
                x for x in output_words if not (x == "EOS" or x == "PAD")
            ]
            print("Bot:", " ".join(output_words))

        except KeyError:
            question = input_sentence
            answer = input("Learnable Q:A detected. How would you answer your own question?\n> ")
            output_file = open(datafile, "a", encoding="utf-8")
            output_file.write(question + "\t" + answer + "\n")
            output_file.close()


def converse():
    # Set dropout layers to eval mode
    encoder.eval()
    decoder.eval()

    # Initialize search module
    searcher = SearchDecoder(encoder, decoder)

    # Begin chatting (uncomment and run the following line to begin)
    evaluate_input(searcher, voc)
