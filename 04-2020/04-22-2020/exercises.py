letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


# Write your unique_english_letters function here:


def unique_english_letters(word):
    unique_letter_count = 0
    unique_letters = ""
    for letter in word:
        if letter in letters and letter not in unique_letters:
            unique_letter_count += 1
            unique_letters += letter
        else:
            continue
    return unique_letter_count


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))


# should print 4

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Write your count_char_x function here:


def count_char_x(word, x):
    x_count = 0
    for letter in word:
        if letter == x:
            x_count += 1
        else:
            continue
    return x_count


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))


# should print 1

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Write your count_multi_char_x function here:


def count_multi_char_x(word, x):
    splits = -1
    for split in word.split(x):
        splits += 1
    return splits


# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))


# should print 1

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Write your substring_between_letters function here:


def substring_between_letters(word, start, end):
    word_split = word.split(start, 1)
    if end in word:
        word_split = word_split[1].split(end, 1)
    else:
        return word
    return word_split[0]


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))


# should print "apple"

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Write your x_length_words function here:


def x_length_words(sentence, x):
    sentence_split = sentence.split()
    for word in sentence_split:
        if len(word) < x:
            return False
        elif len(word) > x:
            continue
    return True


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))


# should print True

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Write your check_for_name function here:


def check_for_name(sentence, name):
    if name.lower() in sentence.lower():
        return True
    return False


# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))


# should print False

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Write your every_other_letter function here:


def every_other_letter(word):
    new_word = ''
    for i in range(len(word)):
        if i % 2 == 0:
            new_word += word[i]
        else:
            continue
    return new_word


# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))


# should print

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Write your reverse_string function here:


def reverse_string(word):
    reversed_str = ""
    for letter in word:
        reversed_str = letter + reversed_str
    return reversed_str


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Write your make_spoonerism function here:


def make_spoonerism(word1, word2):
    return word2[0] + word1[1:] + ' ' + word1[0] + word2[1:]


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Write your add_exclamation function here:


def add_exclamation(word):
    while len(word) < 20:
        word += '!'
    else:
        return word


# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn