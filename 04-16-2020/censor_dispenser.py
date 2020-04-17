# Email One Requirements (DONE)
#  -Write a function that can censor a specific word or phrase from a body of
#  text, and then return the text. Censor all instances of the phrase learning
#  algorithms from the first email, email_one.

# Email Two Requirements (DONE)
#  -Write a function that can censor not just a specific word or phrase from a
#  body of text, but a whole list of words and phrases, returning the text.

# Email Three Requirements (DONE)
#  -Write a function that can censor any occurance of a word from the “negative
#  words” list after any “negative” word has occurred twice, as well as
#  censoring everything from the list from the previous step as well and use it
#  to censor email_three.

# TODO: Email Four Requirements
#  -Write a function that censors not only all of the words from the
#  negative_words and proprietary_terms lists, but also censor any words in
#  email_four that come before AND after a term from those two lists.

# Extra Challenges
#  As a challenge, make sure they:
#  -Handle upper and lowercase letters. (DONE)
#  -Handle punctuation. (DONE)
#  -Censor words while preserving their length. (DONE)

# Imports
import re

# Emails
email_one = open('email_one.txt', 'r').read()
email_two = open('email_two.txt', 'r').read()
email_three = open('email_three.txt', 'r').read()
email_four = open('email_four.txt', 'r').read()

# Occurrences of negative words
word_uses = 0

# Automatically banned words
proprietary_terms = ['she', 'personality matrix', 'sense of self',
                     'self-preservation', 'learning algorithm', 'her',
                     'herself']

# First use of any of these words is allowed; those following are banned
negative_words = ['concerned', 'behind', 'danger', 'dangerous', 'alarming',
                  'alarmed', 'out of control', 'help', 'unhappy', 'bad',
                  'upset', 'awful', 'broken', 'damage', 'damaging', 'dismal',
                  'distressed', 'distressing', 'concerning', 'horrible',
                  'horribly', 'questionable']

# Pattern for censoring the word 'learning algorithm', singular and plural
p1 = f'\\blearning algorithms?\\b'

# Pattern for censoring all words in proprietary_terms
p2 = '|'.join(f'\\b{w}s?\\b' for w in proprietary_terms)

# Pattern for censoring all proprietary_terms and negative_words
proprietary_and_negative_words = proprietary_terms + negative_words
p3 = '|'.join(f'\\b{w}s?\\b' for w in proprietary_and_negative_words)

# Pattern for censoring all listed words, including words before and after them
p4 = '|'.join(f'\\S+\\s{w}\\s\\S+' for w in proprietary_and_negative_words)


# Bans proprietary_terms, scans negative_words and bans words following 2 uses
def censor(match):
    global word_uses
    word = match.group(0)
    word_is_negative = negative_words.count(word) > 0
    uses_allowed = 2
    censor_word = '*' * len(word)
    if uses_allowed == 0 or word.count('S+') > 0:
        return censor_word
    elif word_is_negative and word_uses <= uses_allowed:
        word_uses += 1
    elif word_is_negative and word_uses > uses_allowed:
        return censor_word
    else:
        return censor_word
    return word


email_one_scanned = re.sub(p1, censor, email_one, flags=re.IGNORECASE)

email_two_scanned = re.sub(p2, censor, email_two, flags=re.IGNORECASE)

email_three_scanned = re.sub(p3, censor, email_three, flags=re.IGNORECASE)

email_four_scanned = re.sub(p4, censor, email_four, flags=re.IGNORECASE)

print(email_one_scanned)
print(email_two_scanned)
print(email_three_scanned)
print(email_four_scanned)
