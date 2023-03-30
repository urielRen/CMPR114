# Uriel Renteria
# 3/27/23

# Project 5
def main():
    food = ['Pizza', 'Burgers', 'Chips']

    print('Here are the food items in the list.')

    print(food)

    item = input('Which items in the list do you want to change? ')

    try:
        itemIndex = food.index(item)

        newItem = input('Enter the new food item: ')

        food[itemIndex] = newItem

        print('Here is the revisted list.')

        print(food)

    except ValueError:
        print('The item was not found in the list.')

main()
