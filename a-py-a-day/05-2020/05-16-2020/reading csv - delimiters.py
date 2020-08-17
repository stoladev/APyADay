# We can call all files with a list of different values a CSV file, and then
# use different delimiters (like a coma or tab) to inducate where the different
# values start and stop.

# The delimiter parameter, which is the string that's used to delineate
# separate fields in the CSV, can be called to help iterate through the CSV and
# print out specific items (as an example).

import csv

isbn_list = []

with open('books.csv', newline='') as books_csv:
    books_reader = csv.DictReader(books_csv, delimiter='@')
    for row in books_reader:
        isbn_list.append(row['ISBN'])

print(isbn_list)
