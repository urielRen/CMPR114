# Uriel Renteria
# 4/10/23

def main():
    filename = 'Coffee.txt' 
    writeFile(filename)
    readFile(filename)

def readFile(filename):
    try:
        temp_file = open(filename, 'r')
    except FileNotFoundError:
        print('ERROR: File ', filename, ' not found.')

    print('\n\nFile has been open.')

    line = temp_file.read()
    print('The file reads with new content: ')
    print(line)

    temp_file.close()
    print('File close.')

def writeFile(filename):
    coffee = input('Enter your favorite coffee brand: ')
    prod = input('Enter the product number 99-8888: ')
    price = input('Enter the price of $9.88: $ ')

    try:
        tempFile = open(filename, 'a')
    except FileNotFoundError:
        print('ERROR: File ', filename, ' not found.')

    tempFile.write('\n'+ coffee + ',')
    tempFile.write(prod + ',')
    tempFile.write(price)
    tempFile.close()
    print('Wrote to file.')

if __name__ == '__main__':
    main()
