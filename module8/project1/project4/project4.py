# Uriel Renteria
# 4/10/23

def main():
    filename = 'expenses.txt'
    writeFile(filename)
    readFile(filename)

def writeFile(filename):
    while True:
        try:
            rent = float(input('Enter rent expenses for the month: $'))
            break
        except ValueError:
            print('ERROR: Invalid input.')

    while True:
        try:
            gas = float(input('Enter gas expenses for the month: $'))
            break
        except ValueError:
            print('ERROR: Invalid input.')

    while True:
        try:
            food = float(input('Enter food expenses for the month: $'))
            break
        except ValueError:
            print('ERROR: Invalid input.')

    while True:
        try:
            clothing = float(input('Enter clothing expenses for the month: $'))
            break
        except ValueError:
            print('ERROR: Invalid input.')

    while True:
        try:
            carPayment = float(input('Enter car payment expenses for the month: $'))
            break
        except ValueError:
            print('ERROR: Invalid input.')

    try:
        tempfile = open(filename, 'w')
    except FileNotFoundError:
        print('File not found.')

    tempfile.write('Rent expense: ' + f'${rent: .2f}\n')
    tempfile.write('Gas expense: ' + f'${gas: .2f}\n')
    tempfile.write('Food expense: ' + f'${food: .2f}\n')
    tempfile.write('Clothing expense: ' + f'${clothing: .2f}\n')
    tempfile.write('Car payment expense: ' + f'${carPayment: .2f}')
    print('Wrote to file.')
    tempfile.close()


def readFile(filename):
    try:
        temp_file = open(filename, 'r')
    except FileNotFoundError:
        print('ERROR: File ', filename, ' not found.')

    line = temp_file.read()
    print('The file reads with new content: ')
    print(line)

if __name__ == '__main__':
    main()