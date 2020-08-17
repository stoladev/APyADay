import csv


list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False},
        {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False},
        {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False},
        {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}]


with open('output.csv', 'w') as output_csv:
    fields = ['name', 'userid', 'is_admin']
    output_writer = csv.DictWriter(output_csv, fieldnames=fields)
    output_writer.writeheader()
    for item in list:
        output_writer.writerow(item)

# In the code above, we had a set of dictionaries with the same keys for each,
# a prime candidate for a CSV. We import the CSV library, and then open a new
# file in write-mode by passing the 'w' argument to the open() function.

# We then define the fields we're going to be using into a variable called
# fields. We then instantiate our CSV writer object and pass two arguments.
# The first is output_csv, the file handler object. The second is our list of
# fields 'fields' which we pass to the keyword parameter 'fieldnames'.

# After we've instantiated our CSV file writer, we can start adding lines to
# the file itself. First, we want the headers, so we call .writeheader() on the
# writer object. This writes all fields passed to fieldnames as the first row
# in our file. Then we iterate through our big_list ofdata. Each item in
# big_list is a dictionary with each field in fields as the keys. We call
# output_writer.writerow() with the item dictionaries which writes each line
# to the CSV file.
