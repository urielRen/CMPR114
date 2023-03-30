# Uriel Renteria
# 3/28/23

# Project 2
import pickle

filename = 'vegetables.dat'

def main():
    dbfile = open(filename, 'rb')

    try:
        vegetables = pickle.load(dbfile)
    except EOFError:
        vegetables = {}
    
    dbfile.close()

    choice = 0

    while choice != 5:
        choice = get_menu_choice()

        if choice == 1:
            display(vegetables)
        elif choice == 2:
            addNew(vegetables)
        elif choice == 3:
            change(vegetables)
        elif choice == 4:
            delete(vegetables)

    quit(vegetables, filename)

def get_menu_choice():
    print()
    print('Vegetables')
    print('---------------------------')
    print('1. List of all vegetables')
    print('2. Add a new vegetables')
    print('3. Change existing vegetables')
    print('4. Delete an existing vegetable')
    print('5. Quit the program')
    print()

    choice = int(input('Enter your choice: '))

    while choice < 1 or choice > 5:
        choice = int(input('Enter a valid choice: '))

    return choice

def display(the_list):
    if len(the_list) == 0:
        print('Dictionary is empty.')
    else:
        for veg in the_list:
            print("{}\t\t${}".format(veg,the_list[veg]))

def addNew(the_list):
    vegetable = input('Enter the name of the vegetable: ')

    check = True

    while check == True:
        try:
            price = float(input('Enter the price of vegetable: $'))
            check = False
        except:
            print('Invalid input.')
            check = True      

    if vegetable not in the_list:
        the_list[vegetable] = price
    else:
        print(vegetable, 'is already exist in the dictionary.')

def change(the_list):
    vegetable = input('Enter the name of the vegetable to change the price: ')

    check = True

    if vegetable in the_list:

        while check == True:
            try:
                price = float(input('Enter the new price: $'))
                check = False
            except:
                print('Invalid input.')
                check = True 

        the_list[vegetable] = price
    else:
        print(vegetable, 'is not in the dictionary.')

def delete(the_list):
    vegetable = input('Enter the name of the vegetable to delete: ')

    if vegetable in the_list:
        del the_list[vegetable]
        print(vegetable, 'has been deleted from the dictionary.')
    else:
        print(vegetable, 'is not in the dictionary.')

def quit(the_list, file):
    dbfile = open(filename, 'wb')
    pickle.dump(the_list, dbfile)
    dbfile.close()
    print('Wrote to the ', file)

main()