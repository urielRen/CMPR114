class insects:
    def __init__(self, name, wings):
        self.__name = name
        self.__wings = wings

    def set_name(self, name):
        self.__name = name

    def set_wings(self, wings):
        self.__wings = wings

    def get_name(self):
        return self.__name

    def get_wings(self):
        return self.__wings

class Bumblebee(insects):
    def __init__(self, name, wings, color, ability):
        super().__init__(name, wings)
        self.__color = color 
        self.__ability = ability 

    def set_color(self, color):
        self.__color = color

    def set_ability(self, ability):
        self.__ability = ability

    def get_color(self):
        return self.__color

    def get_ability(self):
        return self.__ability

class Grasshopper(insects):
    def __init__(self, name, wings, food, unique):
        super().__init__(name, wings)
        self.__food = food
        self.__unique = unique

    def set_food(self, food):
        self.__food = food

    def set_unique(self,unique):
        self.__unique = unique

    def get_food(self):
        return self.__food

    def get_unique(self):
        return self.__unique

def main():
    bumblebee = Bumblebee('Bumblebee', 4, 'Yellow and Black', 'Sting')
    print('The name of the insect is', bumblebee.get_name())
    print(bumblebee.get_name(), 'has', bumblebee.get_wings(), 'wings')
    print(bumblebee.get_name(), 'colors are', bumblebee.get_color())
    print('The unique charactertic of the', bumblebee.get_name(), 'is having a', bumblebee.get_ability())
    print()

    grasshopper = Grasshopper('Grasshopper', 2, 'seeds', 'jumping')
    print('The name of the insect is', grasshopper.get_name())
    print(grasshopper.get_name(), 'has', grasshopper.get_wings(), 'pairs of wings')
    print(grasshopper.get_name(), 'eats', grasshopper.get_food())
    print('The unique charactertic of the', grasshopper.get_name(), 'is', grasshopper.get_unique(), 'really high')

main()