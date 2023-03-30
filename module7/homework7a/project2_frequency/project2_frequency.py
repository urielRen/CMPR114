# Uriel Renteria
# 3/27/23

# Project 2 
def main():
    sentence = input('Enter a sentence: ')

    frequency(sentence)

def frequency(str):
    ch = ''
    count = 1
    current = 0
    index = 0
    back = len(str) - 1

    while index < len(str):

        while back > index:
            if str[index].isspace() == True:
                break

            if str[index] == str[back]:
                count += 1
                if current < count:
                    ch = str[index]

            back -= 1

        if current < count:
            current = count
            count = 1
        else:
            count = 1

        index += 1
        back = len(str) - 1

    print('The character that appear the most was ', ch, ' with ', current, ' times')

main()
