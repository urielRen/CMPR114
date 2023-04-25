# Uriel Renteria
# 4/24/23
class AnimalType:
    def eats(self):
        print('This animal likes to eat ?')

class rabbits(AnimalType):
    def munch(self):
        print(" carrots ")

class birds(rabbits):
    def munch1(self):
        print(' seeds ')

class fish(AnimalType):
    def munch2(self):
        print(' worms ')

RabbitObject = rabbits()
RabbitObject.eats()
RabbitObject.munch()

BirdObject = AnimalType()
BirdObject = birds()
BirdObject.eats()
BirdObject.munch1()

FishObject = fish()
FishObject.eats()
FishObject.munch2()