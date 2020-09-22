import torch
from playsound import playsound

from modules.handlers import thread_handler
from modules.handlers.data_handler.data_cleaner import normalize_string, MAX_LENGTH, indexes_from_sentence
from modules.handlers.learning_handler import device, datafile
from modules.handlers.response_handler import respond


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


def check_input(searcher, voc_item, input_sentence):
    try:
        # Check if it is quit case
        if input_sentence == "q" or input_sentence == "quit":
            thread_handler.stop_threads()
        # Normalize sentence
        input_sentence = normalize_string(input_sentence)
        # Evaluate sentence
        output_words = evaluate(searcher, voc_item, input_sentence)
        # Format and print response sentence
        output_words[:] = [
            x for x in output_words if not (x == "EOS" or x == "PAD")
        ]
        response = " ".join(output_words)
        respond(response)

    except KeyError:
        playsound("audio/cmnd_not_recognized_audio.mp3")
        learn_correct_response(input_sentence)


def learn_correct_response(input_sentence):
    question = input_sentence
    answer = input("Learnable Q:A detected. How would you answer your own question?\n> ")
    output_file = open(datafile, "a", encoding="utf-8")
    output_file.write(question + "\t" + answer + "\n")
    output_file.close()
