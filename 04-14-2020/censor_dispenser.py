# These are the emails you will be censoring. The open() function is opening the text file that the emails are
# contained in and the .read() method is allowing us to save their contexts to the following variables:

# IMPORTS
import re

# EMAILS
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# LISTS
proprietary_terms = ['she', 'personality matrix', 'sense of self', 'self-preservation', 'learning algorithm', 'her',
                     'herself']  # AUTO BANNED

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]  # CAN USE ONCE ONLY, OR BANNED


# PATTERNS FOR REDACTION METHODS
pattern1 = '|'.join(f'\\b{w}s?\\b' for w in proprietary_terms)  # Automatically banned words


def list_replace(email, pattern):
    return re.sub(pattern, 'REDACTED', email, flags=re.IGNORECASE)


overused_negative_words = []  # List of banned words because of multiple case use of negative words
for w in negative_words:
    if email_three.count(f'\\b{w}s?\\b') >= 1:
        overused_negative_words.append(w)


proprietary_and_negative_words = proprietary_terms + overused_negative_words  # Final list for pattern2
pattern2 = '|'.join(f'\\b{w}s?\\b' for w in proprietary_and_negative_words)  # Automatically and overused banned words


def list_replace_v2(email, pattern):
    return re.sub(pattern, 'REDACTED', email, flags=re.IGNORECASE)


print(list_replace_v2(email_three, pattern2))


# negative_word_use(email_three, pattern2)
# print(list_replace(email_two, pattern1))
# print(negative_word_use(email_three, pattern2))