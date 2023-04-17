# Uriel Renteria
# 4/16/23

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    name = ''
    animal_type = ''
    age = 0

    pet = Pet(name, animal_type, age)

    name = input('Enter pet name: ')
    animal_type = input('Enter animal type: ')
    age = int(input("Enter pet's age: "))

    pet.set_name(name)
    pet.set_animal_type(animal_type) 
    pet.set_age(age)

    print('Your pet name is ' + pet.get_name())
    print('The pet animal type is ' + pet.get_animal_type())
    print('The pet age is ' + str(pet.get_age()))

main()