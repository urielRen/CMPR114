# Uriel Renteria
# 4/16/23

class Employee:
    def __init__(self, name, IDNumber, department, title):
        self.__name = name
        self.__IDNumber = IDNumber
        self.__department = department
        self.__title = title

    def set_name(self, name):
        self.__name = name

    def set_IDNumber(self, IDNumber):
        self.__IDNumber = IDNumber

    def set_department(self, department):
        self.__department = department

    def set_title(self, title):
        self.__title = title

    def get_name(self):
        return self.__name

    def get_IDNumber(self):
        return self.__IDNumber

    def get_department(self):
        return self.__department

    def get_title(self):
        return self.__title

def main():
    employee1 = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
    employee2 = Employee('Mark Jones', '39119', 'IT', 'Programmer')
    employee3 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

    print('Name\t\tID Number\tDepartment\tJob Title')
    print("-------------------------------------------------------------")
    print(employee1.get_name() + "\t" + employee1.get_IDNumber() + '\t\t' + employee1.get_department() + '\t' + employee1.get_title())
    print(employee2.get_name() + "\t" + employee2.get_IDNumber() + '\t\t' + employee2.get_department() + '\t\t' + employee2.get_title() )
    print(employee3.get_name() + "\t" + employee3.get_IDNumber() + '\t\t' + employee3.get_department() + '\t' + employee3.get_title() )


main()