# Uriel Renteria
# 3/27/23

# Project 3
def main():
    sentence = input('Enter a sentence with all the words together and have some upper case letter: ')
    
    seperate(sentence)

def seperate(str):
    index = 0
    result = ""
    
    for token in str:
        if token.isupper() and index > 0:
            result += " "
            result += token.lower()
        else:
            result += token

        index += 1

    print(result)
            
main()
