# Uriel Renteria
# 4/24/23

class Person:
    def __init__(self, name, address, telephone):
        self.__name = name 
        self.__address = address 
        self.__telephone = telephone 

    def set_name(self, name):
        self.__name = name 

    def set_address(self, address):
        self.__address = address 

    def set_telephone(self, telephone):
        self.__telephone = telephone 

    def get_name(self):
        return self.__name 

    def get_address(self):
        return self.__address 

    def get_telephone(self):
        return self.__telephone 

class Customer(Person):
    def __init__(self, name, address, telephone, number, mailing):
        super().__init__(name, address, telephone)
        self.__number = number 
        self.__mailing = mailing 

    def set_number(self, number):
        self.__number = number 

    def get_number(self):
        return self.__number

    def maillingList(self):
        if self.__mailing:
            print(f'{self.get_name()} wants to be in the mailing list.')
        else:
            print(f"{self.get_name()} doesn't want to be in the mailing list.")

def main():
    name = input('Enter customer name: ')
    address = input('Enter customer address: ')
    telephone = input('Enter customer telephone: ')
    number = input('Enter customer number: ')
    wishes = input('Enter Y or N to be part of the mailing list: ')

    if wishes.lower() == 'y':
        mailing = True
    else:
        mailing = False 

    customer = Customer(name, address, telephone, number, mailing) 

    print('\n\nReceipt')
    print('--------------------------------------')
    print(f'Customer number: {customer.get_number()}')
    print(f'Customer name: {customer.get_name()}')
    print(f'Customer address: {customer.get_address()}')
    print(f'Customer telephone: {customer.get_telephone()}')
    customer.maillingList()

if __name__ == '__main__':
    main()