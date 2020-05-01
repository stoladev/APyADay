alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

coded_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek ' \
                'qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx ' \
                'jxu iqcu evviuj!'

plain_message = 'your message has been decrypted, now let\'s see if you can ' \
                'decrypt this message!'

translated_message = ''


def decode(message, offset):
    global translated_message
    for char in message:
        if char in alphabet:
            translated_message += alphabet[alphabet.find(char) + offset]
        else:
            translated_message += char
    return translated_message


def encode(message, offset):
    global translated_message
    for char in message:
        if char in alphabet:
            translated_message += alphabet[alphabet.find(char) + 26 - offset]
        else:
            translated_message += char
    return translated_message


#print(encode(plain_message, 10))
#translated_message = ''
#print(decode(coded_message, 10))


print(decode('vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. '
             'px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk '
             'fxlltzxl ltyx.', 7))
