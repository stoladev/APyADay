# In python, you can use the csv library's DictReader object.

# import csv

# list_of_email_addresses = []
#
# with open('users.csv', newline='') as users_csv:
#     user_reader = csv.DictReader(users_csv)
#     for row in user_reader:
#         list_of_email_addresses.append(row['Email'])

# In the above code we've opened the users.csv file with the temporary variable
# users_csv. We pass the additional keyword argument newline='' to the file
# opening open() function so that we don't accidentally mistake a line break in
# one of our data fields as a new row in our CSV.

# After opening our new CSV file, we use csv.DictReader(users_csv) which
# converts the lines of our CSV file to Python dictionaries which we can use
# access methods for.

import csv

with open('cool_csv.csv') as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file)
    for row in cool_csv_dict:
        print(row['Cool Fact'])
