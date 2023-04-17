# Uriel Renteria
# 4/16/23

class RetailItem:
    #def __init__(self, description, units, price):
    #    self.__description = description
    #    self.__units = units
    #    self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price

def main():
    item1 = RetailItem()
    item2 = RetailItem()
    item3 = RetailItem()
    #item1 = RetailItem('Jacket', 12, 59.95)
    #item2 = RetailItem('Designer Jeans', 40, 34.95)
    #item3 = RetailItem('Shirt', 20, 24.95)

    item1.set_description('Jacket')
    item1.set_units(12)
    item1.set_price(59.95)

    item2.set_description('Designer Jeans')
    item2.set_units(40)
    item2.set_price(34.95)

    item3.set_description('Shirt')
    item3.set_units(20)
    item3.set_price(24.95)

    print('\t\tDescription\t\tUnits in Inventory\t\tPrice')
    print("-----------------------------------------------------------------------------------")
    print('Item #1\t\t' + item1.get_description() + '\t\t\t\t' + str(item1.get_units()) + '\t\t\t$' + str(item1.get_price()))
    print('Item #2\t\t' + item2.get_description() + '\t\t\t' + str(item2.get_units()) + '\t\t\t$' + str(item2.get_price()))
    print('Item #3\t\t' + item3.get_description() + '\t\t\t\t' + str(item3.get_units()) + '\t\t\t$' + str(item3.get_price()))

main()
