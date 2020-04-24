# Vigenère Cipher

# Example:
"""
message:                     b  a  r  r  y    i  s   t  h  e   s  p  y

keyword phrase:              d  o  g  d  o    g  d   o  g  d   o  g  d

resulting place value:       4  14 15 12 16   24 11  21 25 22  22 17 5
"""


# Variables
alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
plain_message = 'barry is the spy!'
encrypted_message = ''
decrypted_message = ''
main_keyword = 'dog'

second_encrypted_message = ' dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv ' \
                           'jipreneo uhllj kpi rahjib eg fjdkwkedhmp!'
second_keyword = 'friends'


# Functions
def encode(message, keyword):
    global encrypted_message
    # creates a psuedo-loop within the for loop, going through kw length
    kw_place = 0
    for char in message:
        # finds index of the current char within the alphabet
        char_num = alphabet.find(char)
        # finds index of current kw within the alphabet
        kw_num = alphabet.find(keyword[kw_place])
        if char in alphabet:
            # starts at first index, 0, of kw. adds 1 to kw_place
            if kw_place < len(keyword) - 1:
                encrypted_message += alphabet[char_num + kw_num]
                kw_place += 1
            # once it reaches end of kw, resets kw_place to beginning, 0
            elif kw_place == len(keyword) - 1:
                encrypted_message += alphabet[char_num + kw_num]
                kw_place = 0
        # this allows all chars not found in the alphabet to pass through
        else:
            encrypted_message += char
    return encrypted_message


def decode(message, keyword):
    global decrypted_message
    kw_place = 0
    for char in message:
        kw_num = alphabet.find(keyword[kw_place])
        char_num = alphabet.find(char)
        if char in alphabet:
            if kw_place < len(keyword) -1:
                # adds 26 to index to allow subtracting kw_num
                decrypted_message += alphabet[char_num + 26 - kw_num]
                kw_place += 1
            elif kw_place >= len(keyword) -1:
                decrypted_message += alphabet[char_num + 26 - kw_num]
                kw_place = 0
        else:
            decrypted_message += char
    return decrypted_message


# Print statements
print('Encrypted: ' + encode(plain_message, main_keyword))
print('Decrypted: ' + decode(encrypted_message, main_keyword))
print()
print('Second message decrypted: '
      + decode(second_encrypted_message, second_keyword))
