class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

class ProductionWorker(Employee):
    def __init__(self, name, number, shift, payrate):
        super().__init__(name, number)
        self.__shift = shift
        self.__payrate = payrate

    def set_shift(self, shift):
        self.__shift = shift

    def set_payrate(self, payrate):
        self.__payrate = payrate

    def get_shift(self):
        return self.__shift

    def get_payrate(self):
        return self.__payrate

def main():
    name = input('Enter the name of the employee: ')
    number = input('Enter the employee number: ')
    shift = int(input('Enter a 1 or 2 for shift: '))
    pay = float(input('Enter the hourly pay rate: $'))

    employee1 = ProductionWorker(name, number, shift, pay)

    print('Employee name:', employee1.get_name())
    print('Employee number:', employee1.get_number())

    if(employee1.get_shift() == 1):
        print('Employee shift time is Day')
    elif(employee1.get_shift() == 2):
        print('Employee shift time is Night')
    else:
        print('Invalid shift time')

    print('Employee hourly pay rate is $', employee1.get_payrate())

main()