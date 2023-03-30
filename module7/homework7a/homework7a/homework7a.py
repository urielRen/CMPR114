# Uriel Renteria
# 3/27/23

# Project 1 Vowels and Consonants
def main():
    sentence = input('Enter a sentence: ')

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    Vowels(sentence, vowels)
    consonants(sentence, vowels)

def Vowels(str, vowels):
    count = 0

    for ch in str:
        if ch in vowels:
            count += 1

    print('The sentence has ', count, ' vowels.')

def consonants(str, vowels):
    index = 0
    count = 0
    space = 0
    
    while index < len(str):
        if str[index].isspace() == True:
            space += 1
        else:
            if str[index] not in vowels:
                count += 1

        index += 1

    print('The sentence has ', count, ' consonants.')

main()