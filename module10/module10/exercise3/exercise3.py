import vehicles

def main():
    used_car = vehicles.Automobiles('Audi', 2022, 45000, 80000.0)

    print('Make: ', used_car.get_make())
    print('Model: ', used_car.get_model())
    print('Mileage: ', used_car.get_mileage())
    print('Price: ', used_car.get_price())
    print()
    used_car2 = vehicles.Automobiles('Honda', 2022, 45000, 80000.0)

    print('Make: ', used_car2.get_make())
    print('Model: ', used_car2.get_model())
    print('Mileage: ', used_car2.get_mileage())
    print('Price: ', used_car2.get_price())

main()
