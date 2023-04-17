# Uriel Renteria
# 4/15/23

import class7

def main():
    name = (input('Enter the name: '))
    address = (input('Enter the address: '))
    phone = (input('Enter the phone: '))
    city = (input('Enter the city: '))
    zipcode = (int(input('Enter the zipcode: ')))
    age = (int(input("Enter the age: ")))

    v1 = class7.Customer.set_name = name
    v2 = class7.Customer.set_address = address
    v3 = class7.Customer.set_phone = phone
    v4 = class7.Customer.set_city = city
    v5 = class7.Customer.set_zipcode = zipcode
    v6 = class7.Customer.set_age = age

    print('Hello ' + v1 + ' your address is ' + v2 + ' and your # is ' + v3 + 
          '\nyour city ' + v4 + ' your zip code is ' + str(v5) + ' your age is ' + str(v6))

main()
