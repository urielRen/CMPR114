# Uriel Renteria
# 4/24/23

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

class ShiftSupervisor(Employee):
    def __init__(self, name, number, bonus, salary):
        super().__init__(name, number)
        self.__bonus = bonus
        self.__salary = salary 

    def set_bonus(self, bonus):
        self.__bonus = bonus 

    def set_salary(self, salary):
        self.__salary = salary 

    def get_bonus(self):
        return self.__bonus

    def get_salary(self):
        return self.__salary 

def main():
    name = input('Enter the name of the employee: ')
    number = input('Enter the employee number: ')
    salary = float(input('Enter the employee salary: $'))

    production = float(input('Enter the production of the shift: '))
    if(production >= 12000):
        bonus = float(input('Enter the yearly bonus: $'))
    else:
        bonus = 0

    shiftSupervisor = ShiftSupervisor(name, number, bonus, salary)

    print('Supervisor name:', shiftSupervisor.get_name())
    print('Supervisor number:', shiftSupervisor.get_number())
    print(f'Supervisor salary: ${shiftSupervisor.get_salary(): ,.2f}')
    if(production >= 12000):
        print(f'Supervisor bonus: ${shiftSupervisor.get_bonus(): ,.2f}')
        print(f'Total: ${shiftSupervisor.get_salary() + shiftSupervisor.get_bonus(): ,.2f}')
    else:
        print("Shift did't meet the production goals. Supervisor didn't earn a bonus.")

if __name__ == '__main__':
    main()
