# Uriel Renteria
# 4/15/23

class PI:
    def GetInformation(self, LN, FN, Age):
        return LN + ' , ' + FN + ' , ' + str(Age)

PersonalInformation = PI()
PersonalInformation.Lastname = input('Enter the lastname: ')
PersonalInformation.Firstname = input('Enter the firstname: ')
PersonalInformation.Age = int(input('Enter the age: '))

print(PersonalInformation.GetInformation(PersonalInformation.Lastname, PersonalInformation.Firstname, PersonalInformation.Age))