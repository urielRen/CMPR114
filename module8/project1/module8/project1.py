# Uriel Renteria
# 4/10/23

def main():
    while True:
        try:
            fat = float(input('Enter number of fat grams: '))
            break
        except ValueError:
            print('ERROR: invalid input.')

    fatC = calFat(fat)

    while True:
        try:
            carbo = float(input('Enter number of carbohydrates grams: '))
            break
        except ValueError:
            print('ERROR: Invalid input.')
    
    carboC = calCar(carbo)

    print(f'The number of calories for {fat: .2f} grams is {fatC: .2f}')
    print(f'The number of calories for {carbo: .2f} grams is {carboC: .2f}')

def calFat(value):
    calories = value * 9
    return calories

def calCar(value):
    calories = value * 4
    return calories

if __name__ == '__main__':
    main()