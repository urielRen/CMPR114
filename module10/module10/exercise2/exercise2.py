# Uriel Renteria
# 4/24/23

class person:
    def __init__(self, name, age, address, city, state, zipcode):
        self.name = name
        self.age = age
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

class Student(person):
    def __init__(self, name, age, address, city, state, zipcode, studentID, GPA):
        name = input('Enter the name: ')
        age = input('Enter the age: ')
        address = input('Enter address: ')
        city = input('Enter the city name: ')
        state = input('Enter state name: ')
        zipcode = input('Enter zipcode: ')
        studentID = input('Enter the Stdent ID: ')
        GPA = input('Enter the GPA: ')

        super().__init__(name, age, address, city, state, zipcode)
        self.studentID = studentID
        self.GPA = GPA

class Teacher(person):
    def __init__(self, name, age, address, city, state, zipcode, TeacherID, ClassTeaching):
        name = input('Enter the name: ')
        age = input('Enter the age: ')
        address = input('Enter address: ')
        city = input('Enter the city name: ')
        state = input('Enter state name: ')
        zipcode = input('Enter zipcode: ')
        TeacherID = input('Enter the Teacher ID: ')
        ClassTeaching = input('Enter the name of the course teaching: ')

        super().__init__(name, age, address, city, state, zipcode)

        self.TeacherID = TeacherID
        self.ClassTeaching = ClassTeaching

student = Student('','','','','','','','')
print('Student Name: ', student.name)
print('Student Age: ', student.age)
print('Student Address: ', student.address)
print('Student City: ', student.city)
print('Student State: ', student.state)
print('Student Zip code: ', student.zipcode)
print('Student ID: ', student.studentID)
print('Student GPA: ', student.GPA)
print('\n')

teacher = Teacher('','','','','','','','')
print('Teacher Name: ', teacher.name)
print('Teacher Age: ', teacher.age)
print('Teacher Address: ', teacher.address)
print('Teacher City: ', teacher.city)
print('Teacher State: ', teacher.state)
print('Teacher Zip code: ', teacher.zipcode)
print('Teacher ID: ', teacher.TeacherID)
print('Teacher Course: ', teacher.ClassTeaching)
