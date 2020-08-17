"""
Reading a file in Python

When reading a file, we might want to get the whole doc in a single string
just like .read() would return.

What if we wanted to store each line in a var?

We can use the .readlines() function to read a text file line by line instead
of the whole thing at once.
"""

with open('how_many_lines.txt') as lines_doc:
    for line in lines_doc.readlines():
        print(line)

"""
Reading a file per line in Python

Sometimes you don't want to go through a whole file.

.readline() reads a single line at a time.

If the entire doc is read line by line this way, subsequent calls to
.readline() will not throw an error but will start returning an empty string
("").
"""

with open('how_many_lines.txt') as first_line_doc:
    first_line = first_line_doc.readline()

print(first_line)

"""
Writing a file in Python

You must pass the argument 'w' in order to indicate to open the file in write
mode. The default arugment is 'r' and passing 'r' opensthe file in read-mode.

This creates a new file in the same directory and gives it the text you pass
through it.

If there is already a file named whatever you are naming it, it will completely
overwrite that file, erasing whatever its contents were before.
"""

with open('bad_bands.txt', 'w') as bad_bands_doc:
    bad_bands_doc.write('Mike\'s band')

"""
Appending to a file in Python

Instead of opening the file in 'w' for write mode, we open it with 'a' for
append mode. Text is appended on a new line.
"""

with open('cool_dogs.txt', 'a') as cool_dogs_file:
    cool_dogs_file.append('Air Buddy')
