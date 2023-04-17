class Customer:
    def __init__(self, name, address, phone, city, zipcode, age):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__city = city
        self.__zipcode = zipcode
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def set_city(self, city):
        self.__city = city

    def set_zipcode(self, zipcode):
        self.__zipcode = zipcode

    def set_age(self, age):
        self.__age = age