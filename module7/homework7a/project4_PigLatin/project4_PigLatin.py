# Uriel Renteria
# 3/27/28

# Project 4
def main():
    sentence = input('Enter a sentence: ')

    pigLatin(sentence)

def pigLatin(str):
    tokens = str.split(' ')

    result = []

    if str.isupper():
        for word in tokens:
            word = word[: len(word)] + word[0] + 'AY'
            result.append(word[1:])
    else:
        for word in tokens:
            word = word[: len(word)] + word[0] + 'ay'
            result.append(word[1:])

    print('Pig Latin: ' + " ".join(result))

main()
