# Uriel Renteria
# 4/10/23

def main():
    readFile('Coffee.txt')

def readFile(filename):
    try:
        temp_file = open(filename, 'r')
    except FileNotFoundError:
        print('ERROR: File ', filename, ' not found.')

    print('File has been open.')

    line = temp_file.read()
    print('The file reads: ')
    print(line)

    temp_file.close()
    print('File close.')

if __name__ == '__main__':
    main()