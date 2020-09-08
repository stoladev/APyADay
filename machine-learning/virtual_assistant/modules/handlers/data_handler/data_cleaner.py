import unicodedata
import itertools
import torch
import re

from modules.handlers.learning_handler import (
    data,
    datafile,
    PAD_token,
    SOS_token,
    EOS_token,
    MAX_LENGTH,
)


class Voc:
    def __init__(self, name):
        self.name = name
        self.trimmed = False
        self.word2index = {}
        self.word2count = {}
        self.index2word = {PAD_token: "PAD", SOS_token: "SOS", EOS_token: "EOS"}
        self.num_words = 3  # Count SOS, EOS, PAD

    def add_sentence(self, sentence):
        for word in sentence.split(" "):
            self.add_word(word)

    def add_word(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.num_words
            self.word2count[word] = 1
            self.index2word[self.num_words] = word
            self.num_words += 1
        else:
            self.word2count[word] += 1


# Turn a Unicode string to plain ASCII, thanks to
# https://stackoverflow.com/a/518232/2809427
def unicode_to_ascii(s):
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


# Lowercase, trim, and remove non-letter characters
def normalize_string(s):
    s = unicode_to_ascii(s.lower().strip())
    # s = re.sub(r"([.!?])", r" \1", s)
    s = re.sub(r"[^a-zA-Z0-9.!?@#$%^&*()\[\]\-_+=\\/\';:\"]+", r" ", s)
    s = re.sub(r"\s+", r" ", s).strip()
    return s


# Read query/response pairs and return a voc object
def read_vocs(file, corpus_name):
    print("Reading lines...")
    # Read the file and split into lines
    lines = open(file, encoding="utf-8").read().strip().split("\n")
    # Split every line into pairs and normalize
    sentence_pairs = [[normalize_string(s) for s in lines.split("\t")] for lines in lines]
    voc_item = Voc(corpus_name)
    return voc_item, sentence_pairs


# Returns True iff both sentences in a pair 'p' are under the MAX_LENGTH threshold
def filter_pair(p):
    # Input sequences need to preserve the last word for EOS token
    return len(p[0].split(" ")) < MAX_LENGTH and len(p[1].split(" ")) < MAX_LENGTH


# Filter pairs using filterPair condition
def filer_pairs(sentence_pairs):
    return [pair for pair in sentence_pairs if filter_pair(pair)]


# Using the functions defined above, return a populated voc object and pairs list
def load_prepared_data(corpus_name, data_item):
    print("Start preparing training data ...")
    voc_item, sentence_pairs = read_vocs(data_item, corpus_name)
    print("Read {!s} sentence pairs".format(len(sentence_pairs)))
    sentence_pairs = filer_pairs(sentence_pairs)
    print("Trimmed to {!s} sentence pairs".format(len(sentence_pairs)))
    print("Counting words...")
    for pair in sentence_pairs:
        voc_item.add_sentence(pair[0])
        voc_item.add_sentence(pair[1])
    print("Counted words:", voc_item.num_words)
    return voc_item, sentence_pairs


def indexes_from_sentence(voc_item, sentence):
    return [voc_item.word2index[word] for word in sentence.split(" ")] + [EOS_token]


def zero_padding(line, fill_value=PAD_token):
    return list(itertools.zip_longest(*line, fillvalue=fill_value))


def binary_matrix(line):
    m = []
    for i, seq in enumerate(line):
        m.append([])
        for token in seq:
            if token == PAD_token:
                m[i].append(0)
            else:
                m[i].append(1)
    return m


# Returns padded input sequence tensor and lengths
def input_var(line, voc_item):
    indexes_batch = [indexes_from_sentence(voc_item, sentence) for sentence in line]
    lengths = torch.tensor([len(indexes) for indexes in indexes_batch])
    pad_list = zero_padding(indexes_batch)
    pad_var = torch.LongTensor(pad_list)
    return pad_var, lengths


# Returns padded target sequence tensor, padding mask, and max target length
def output_var(line, voc_item):
    indexes_batch = [indexes_from_sentence(voc_item, sentence) for sentence in line]
    max_target_len = max([len(indexes) for indexes in indexes_batch])
    pad_list = zero_padding(indexes_batch)
    mask = binary_matrix(pad_list)
    mask = torch.BoolTensor(mask)
    pad_var = torch.LongTensor(pad_list)
    return pad_var, mask, max_target_len


# Returns all items for a given batch of pairs
def convert_batch_to_training_data(voc_item, pair_batch):
    pair_batch.sort(key=lambda x: len(x[0].split(" ")), reverse=True)
    input_batch, output_batch = [], []
    for pair in pair_batch:
        input_batch.append(pair[0])
        output_batch.append(pair[1])
    inp, lengths = input_var(input_batch, voc_item)
    output, mask, max_target_len = output_var(output_batch, voc_item)
    return inp, lengths, output, mask, max_target_len


voc, pairs = load_prepared_data(data, datafile)
