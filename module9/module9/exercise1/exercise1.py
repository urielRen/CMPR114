# Uriel Renteria
# 4/25/23

class Students:
    def GetInformation(self):
        print('Student Last name is ' + self.Lastname)
        print('Student First name is ' + self.Firstname)
        print('Student Address is ' + self.Address)
        print('Student City is ' + self.City)
        print('Student State is ' + self.State)
        print('Student Zipcode is ' + self.Zipcode)

Student1 = Students()
Student1.Lastname = 'Doe'
Student1.Firstname = 'John'
Student1.Address = '111 St'
Student1.City = 'Santa Ana'
Student1.State = 'CA'
Student1.Zipcode = '12345\n'

Student2 = Students()
Student2.Lastname = 'Cantor'
Student2.Firstname = 'Mike'
Student2.Address = '222 St'
Student2.City = 'Garden Grove'
Student2.State = 'CA'
Student2.Zipcode = '67890\n'

Student3 = Students()
Student3.Lastname = input('Enter last name: ')
Student3.Firstname = input('Enter first name: ')
Student3.Address = input('Enter address: ')
Student3.City = input('Enter city: ')
Student3.State = input('Enter state: ')
Student3.Zipcode = input('Enter zipcode: ')


Student1.GetInformation()
Student2.GetInformation()
Student3.GetInformation()