"""This is my take on Codecademy's 'Censor Dispenser' project challenge.

# To see the requirements of the project (which will probably answer your
# questions regarding the censoring requirements of each email), visit the
# project page on https://www.codecademy.com/practice/projects/censor-dispenser

# This project utilizes:
# -Regular expressions (REGEX)
# -String substitution through match
# -Substitution without original file modification
# -Per-character replacement with *
"""

import re

# Emails
email_one = open('email_one.txt', 'r').read()
email_two = open('email_two.txt', 'r').read()
email_three = open('email_three.txt', 'r').read()
email_four = open('email_four.txt', 'r').read()

# Bannable terms and words
proprietary_terms = [
    'she', 'personality matrix', 'sense of self', 'self-preservation',
    'learning algorithm', 'her', 'herself'
]

negative_words = [
    'concerned', 'behind', 'danger', 'dangerous', 'alarming', 'alarmed',
    'out of control', 'help', 'unhappy', 'bad', 'upset', 'awful', 'broken',
    'damage', 'damaging', 'dismal', 'distressed', 'distressing', 'concerning',
    'horrible', 'horribly', 'questionable'
]

# Pattern for censoring all words in proprietary_terms
PT_PATTERN = '|'.join(f'\\b{w}s?\\b' for w in proprietary_terms)

proprietary_and_negative_words = proprietary_terms + negative_words

# Pattern for censoring all proprietary_terms and negative_words
PANW_PATTERN = '|'.join(f'\\b{w}s?\\b' for w in proprietary_and_negative_words)

# Pattern for censoring all listed words, including words before and after them
ALL_PATTERN = '|'.join(f'\\S+\\s{w}\\s?\\S+'
                       for w in proprietary_and_negative_words)


# Bans proprietary_terms, scans negative_words and bans words following 2 uses
def censor(match):
    """Bans proprietary terms, scanning for negative words. Bans words after
    two detected uses.

    Args:
        match: Matches from the pattern detection.
    """
    word = match.group(0)
    word_is_negative = negative_words.count(word) > 0
    word_uses = 0
    uses_allowed = 2
    censor_word = '*' * len(word)
    # Bans all words if no uses are allowed
    # if uses_allowed == 0:
    #     return censor_word
    # # Bans all words past second scanned email
    # elif EMAILS_CENSORED > 2:
    #     return censor_word
    # Scanning for uses_allowed, allowing or censoring the word
    if word_is_negative and word_uses <= uses_allowed:
        word_uses += 1
    else:
        return censor_word
    return word


# Amount of emails censored (fully censored after 3 emails)
EMAILS_CENSORED = 0

# re.sub (PATTERN, CENSOR WORD OR FUNCTION, WHAT TO CENSOR, FLAGS)
email_one_scanned = re.sub(PT_PATTERN, censor, email_one, flags=re.IGNORECASE)
EMAILS_CENSORED += 1

email_two_scanned = re.sub(PT_PATTERN, censor, email_two, flags=re.IGNORECASE)

EMAILS_CENSORED += 1

email_three_scanned = re.sub(PANW_PATTERN,
                             censor,
                             email_three,
                             flags=re.IGNORECASE)

EMAILS_CENSORED += 1

email_four_scanned = re.sub(ALL_PATTERN,
                            censor,
                            email_four,
                            flags=re.IGNORECASE)

print(email_one_scanned)
print(email_two_scanned)
print(email_three_scanned)
print(email_four_scanned)
