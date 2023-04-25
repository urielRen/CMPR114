import vehicles

def main():
    used_car = vehicles.Automobiles('Audi', 2022, 45000, 80000.0)
    used_car2 = vehicles.Automobiles('Honda', 2022, 45000, 80000.0)

    print('Make: ', used_car.get_make())
    print('Model: ', used_car.get_model())
    print('Mileage: ', used_car.get_mileage())
    print('Price: ', used_car.get_price())
    print()
    print('Make: ', used_car2.get_make())
    print('Model: ', used_car2.get_model())
    print('Mileage: ', used_car2.get_mileage())
    print('Price: ', used_car2.get_price())
    print()

    truck = vehicles.Truck('Toyota', 'Tacoma', 40000, 12000.0)
    suv = vehicles.SUV('Volvo', 'SE', 30000, 18500.0)
    eletric = vehicles.Electric('Tesla', 'Model S', 12890, 45980.0)

    print('the following truck is in inventory')
    print('Make: ', truck.get_make())
    print('Model: ', truck.get_model())
    print('Mileage: ', truck.get_mileage())
    print('Price: ', truck.get_price())
    print()
    print('the following suv is in inventory')
    print('Make: ', suv.get_make())
    print('Model: ', suv.get_model())
    print('Mileage: ', suv.get_mileage())
    print('Price: ', suv.get_price())
    print()
    print('the following electric is in inventory')
    print('Make: ', eletric.get_make())
    print('Model: ', eletric.get_model())
    print('Mileage: ', eletric.get_mileage())
    print('Price: ', eletric.get_price())


main()

