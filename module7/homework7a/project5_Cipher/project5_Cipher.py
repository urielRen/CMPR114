# Uriel Renteria
# 3/27/23

# Project 5
def main():
    sentence = input('Enter a sentence: ')

    cipher(sentence)

def cipher(str):
    result = ''

    for ch in str:
        if (ch.isupper()):
            result += chr((ord(ch) + 13 - 65) % 26 + 65)
        elif (ch.isspace()):
            result += ' '
        else:
            result += chr((ord(ch) + 13 - 97) % 26 + 97)

    print("The Ceaser Cipher sentence: " + result)

main()
