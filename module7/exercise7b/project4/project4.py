# Uriel Renteria
# 3/27/23

# Project 4
import pickle

def main():
    again = 'y' # To control loop repetition
    output_file = open('info.dat', 'wb')

    while again.lower() == 'y':
        save_data(output_file)
        again = input('Enter more data? (y/n): ')

    output_file.close()

def save_data(file):
    person = {}
    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = float(input('Weight: '))

    pickle.dump(person, file)

if __name__ == '__main__':
    main()
