# Uriel Renteria
# 4/15/23

class PI:
    def GetInformation(self, LN, FN, Age, AD, CI, ZC):
        return LN + ' , ' + FN + ' , ' + str(Age) + ' , ' + AD + ' , ' + CI + ' , ' + str(ZC)

PersonalInformation = PI()
PersonalInformation.Lastname = input('Enter the lastname: ')
PersonalInformation.Firstname = input('Enter the firstname: ')
PersonalInformation.Age = int(input('Enter the age: '))
PersonalInformation.Address = input('Enter the address: ')
PersonalInformation.City = input('Enter the city: ')
PersonalInformation.Zipcode = int(input('Enter the zipcode: '))

print(PersonalInformation.GetInformation(PersonalInformation.Lastname, PersonalInformation.Firstname, PersonalInformation.Age, 
                                         PersonalInformation.Address, PersonalInformation.City, PersonalInformation.Zipcode))
