# uriel renteria
# 5/1/23

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
    def __init__(self, name, number, shift, pay):
        super().__init__(name, number)
        self.__shift = shift
        self.__pay = pay

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay(self, pay):
        self.__pay = pay

    def get_shift(self):
        if self.__shift == 1:
            return 'Day shift'
        elif self.__shift == 2:
            return 'Night day'
        else:
            return 'Invalid shift number'

    def get_pay(self):
        return self.__pay

def main():
    name = input('Enter employee name: ')

    while True:
        try:
            number = int(input('Enter employee number: '))
            break
        except ValueError:
            print('ERROR: Invalid input. Try agian')

    while True:
        try:
            shift = int(input('Enter shift number 1 for Day or 2 for Night: '))
            break
        except ValueError:
            print('ERROR: Invalid input. Try agian')

    while True:
        try:
            pay = float(input('Enter employee pay: $'))
            break
        except ValueError:
            print('ERROR: Invalid input. Try agian')

    productionWorker = ProductionWorker(name, number, shift, pay)
    productionWorker2 = ProductionWorker('John Doe', 98719, 2, 17.23)
    productionWorker3 = ProductionWorker('Miguel Lopez', 92831, 1, 19.32)

    workerList = [productionWorker, productionWorker2, productionWorker3]

    for employee in workerList:
        print(f"Employee's name: {employee.get_name()}")
        print(f"Employee's number: {employee.get_number()}")
        print(f"Employee's shift: {employee.get_shift()}")
        print(f"Employee's pay: {employee.get_pay()}")
        print()

if __name__ == '__main__':
    main()