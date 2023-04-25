class AnimalType:
    def eats(self):
        print('This animal likes to eat ?')

class rabbits(AnimalType):
    def munch(self):
        print(" carrots ")

class birds(rabbits):
    def munch1(self):
        print(' seeds ')

RabbitObject = rabbits()
RabbitObject.eats()
RabbitObject.munch()

BirdObject = AnimalType()
BirdObject = birds()
BirdObject.eats()
BirdObject.munch1()
