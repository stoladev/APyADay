from __future__ import print_function
import re
import os
import csv
import codecs

from utils import debug

# Utilizing test data from Cornell Movie Dialogue Corpus just to get things working.
# Will mutate this code later once everything is working as intended.

corpus_name = "training_data"
corpus = os.path.join(corpus_name)


def print_lines(file, n=10):
    with open(file, 'rb') as datafile:
        lines = datafile.readlines()
    for line in lines[:n]:
        print(line)


def convert_lines_to_dictionary(file_name, fields):
    lines = {}
    with open(file_name, "r", encoding="iso-8859-1") as f:
        for line in f:
            values = line.split(" +++$+++ ")
            line = {}
            for i, field in enumerate(fields):
                line[field] = values[i]
            lines[line["lineID"]] = line
    return lines


def group_lines_into_conversations(file_name, lines, fields):
    conversations = []
    with open(file_name, "r", encoding="iso-8859-1") as f:
        for line in f:
            values = line.split(" +++$+++ ")
            conversation = {}
            for i, field in enumerate(fields):
                conversation[field] = values[i]
            utterance_id_pattern = re.compile("L[0-9]+")
            line_ids = utterance_id_pattern.findall(conversation["utteranceIDs"])
            conversation["lines"] = []
            for line_id in line_ids:
                conversation["lines"].append(lines[line_id])
            conversations.append(conversation)
    return conversations


def extract_sentence_pairs(conversations):
    qa_pairs = []
    for conversation in conversations:
        for i in range(
            len(conversation["lines"]) - 1
        ):
            input_line = conversation["lines"][i]["text"].strip()
            target_line = conversation["lines"][i + 1]["text"].strip()
            if input_line and target_line:
                qa_pairs.append([input_line, target_line])
    return qa_pairs


def format_data():
    datafile = os.path.join(corpus, "formatted_movie_lines.txt")

    delimiter = "\t"
    delimiter = str(codecs.decode(delimiter, "unicode_escape"))

    # lines = {}
    # conversations = []
    movie_lines_fields = ["lineID", "characterID", "movieID", "character", "text"]
    movie_conversations_fields = [
        "character1ID",
        "character2ID",
        "movieID",
        "utteranceIDs",
    ]

    debug.log("\nProcessing data...")
    lines = convert_lines_to_dictionary(os.path.join(corpus, "movie_lines.txt"), movie_lines_fields)
    debug.log("\nLoading data...")
    conversations = group_lines_into_conversations(
        os.path.join(corpus, "movie_conversations.txt"),
        lines,
        movie_conversations_fields,
    )

    # Write new csv file
    debug.log("\nWriting new formatted file...")
    with open(datafile, "w", encoding="utf-8") as output_file:
        writer = csv.writer(output_file, delimiter=delimiter, lineterminator="\n")
        for pair in extract_sentence_pairs(conversations):
            writer.writerow(pair)

    print_lines(datafile)
