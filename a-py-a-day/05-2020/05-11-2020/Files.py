#!/usr/bin/env python3

# Instead of using the `w` argument for write-mode, you can open the file with
# `a` for append mode.
#
# Example:
with open('generated_file.txt', 'a') as gen_file:
    gen_file.write("... and it still is")

# In the code above we open a file object in the temporary variable gen_file.
# This variable points tohef ile generated_file.txt and, since it's open in
# append mode, adds the line `...and it still is` as a new line to the file.

with open('cool_dogs.txt', 'a') as cool_dogs_file:
    cool_dogs_file.write("Air Buddy")

# The with keyword invokes something called a context manager for the file
# that we’re calling open() on. This context manager takes care of opening
# the file when we call open() and then closing the file after we leave the
# indented block.

# Why is closing the file so complicated? Well, most other aspects of our
# code deal with things that Python itself controls. All the variables you
# create: integers, lists, dictionaries — these are all Python objects, and
# Python knows how to clean them up when it’s done with them. Since your
# files exist outside your Python script, we need to tell Python when we’re
# done with them so that it can close the connection to that file. Leaving a
# file connection open unnecessarily can affect performance or impact other
# programs on your computer that might be trying to access that file.

# The with syntax replaces older ways to access files where you need to call
# .close() on the file object manually. We can still open up a file and append
# to it with the old syntax, as long as we remember to close the file
# connection afterwards.

fun_cities_file = open('fun_cities.txt', 'a')

# We can now append a line to "fun_cities".
fun_cities_file.write("Montréal")

# But we need to remember to close the file
fun_cities_file.close()

# In the above script we added “Montréal” as a new line in our file
# fun_cities.txt. However, since we used the older-style syntax, we had to
# remember to close the file afterwards. Since this is necessarily more verbose
# (requires at least one more line of code) without being any more expressive,
# using with is preferred.

with open('fun_file.txt') as fun_file:
    setup = fun_file.readline()
    punchline = fun_file.readline()
    print(setup)

# Tomorrow's lesson: CSV file reading with Python
