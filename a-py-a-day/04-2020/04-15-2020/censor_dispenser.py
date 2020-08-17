# TODO:
#  Write a function that can censor any occurrence of a word from the “negative words” list after any “negative”
#  word has occurred twice, as well as censoring everything from the list from the previous step as well and use it
#  to censor email_three.

# TODO:
#  Write a function that censors not only all of the words from the negative_words and proprietary_terms lists,
#  but also censor any words in email_four that come before AND after a term from those two lists.

# TODO:
#  As a challenge, make sure they:
#  Handle upper and lowercase letters.
#  Handle punctuation.
#  Censor words while preserving their length.

# Imports
import re

# Emails
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# Automatically banned words
proprietary_terms = ['she', 'personality matrix', 'sense of self', 'self-preservation', 'learning algorithm', 'her',
                     'herself']

# Pattern for proprietary_terms
pattern1 = '|'.join(f'\\b{w}s?\\b' for w in proprietary_terms)

# First use of any of these words is allowed; those following are banned
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]

# ToDo: Filter negative_words into overused_negative_words (first use of a word is fine - following are banned)
overused_negative_words = []
for w in negative_words:
    if email_three.count(f'\\b{w}s?\\b') >= 0:
        overused_negative_words.append(w)

# Combining both proprietary_terms and overused_negative_words for required pattern
proprietary_and_negative_words = proprietary_terms + overused_negative_words

# Pattern for both proprietary_terms and overused_negative_words
pattern2 = '|'.join(f'\\b{w}s?\\b' for w in proprietary_and_negative_words)


# Function for banned word replacement
def list_replace(email, pattern):
    return re.sub(pattern, 'REDACTED', email, flags=re.IGNORECASE)


# Printing the result, which completes all requirements without changing the original email
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(list_replace(email_two, pattern1))
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(list_replace(email_three, pattern2))
