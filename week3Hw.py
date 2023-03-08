# Uriel Renteria
# 2/27/23

#homework 3

#challenge 1 - display the time and distance
#distance = 0.0
#speed = 0.0
#time = 0

#speed = int(input("What is the speed of the vehicle in mph? "))
#time = int(input("How many hours has it traveled? "))

#print('Hours\t\tDistance Traveled')
#print('---------------------------------')
#for counter in range(1, time + 1):
#    distance = speed * counter
#    print(f' {counter}\t\t\t{distance}')


#challenge 2 - rainfall 
#years = int(input('Enter the number of years: '))
#total = 0.0

#for outer in range(1, years + 1):
#    print(f'Enter the rainfall for year {outer}: ')
#    for inner in range(1,13):
#        rain = float(input(f'Enter the amount of rainfall for month {inner}: '))
#        total += rain

#months = years * 12
#average = total / months

#print(f"The total amount of months is {months}")
#print(f'The total inches of rainfall is {total: .2f} inches')
#print(f"The average rainfall per month is {average: .2f} inches")


#challenge 3 - get only positive number and exit with negative numbers
#theSum = 0.0

#print('Enter a positive number to enter a loop or a negative to end program.')
#positive = float(input('Enter a number: '))

#while positive > 0:
#    theSum += positive
#    print('Enter a positive number to continue or a negative to exit to get the sum.')
#    positive = float(input('Enter a number: '))

#print(f'The sum of the positive number is {theSum: .2f}')




#homework 3.7

#project 1 - getting total from a list of numbers
#def main():
#    scores = getScores()
#    total = getTotal(scores)
#    print(f'The total test scores are: {total: .2f}')
#    write('totalScores.txt', scores, total)

#def getScores():
#    testScores = []
#    again = 'y'

#    while again == 'y' or again == 'Y':
#        value = float(input('Enter a test score: '))
#        testScores.append(value)

#        print('Do you want to add another score?')
#        again = input('y = yes, or any other key = no: ')
#        print()

#    return testScores

#def write(name, scores, total):
#    index = 0
#    output = open(name, 'w')

#    for s in scores:
#        output.writelines(f'Test score {index + 1}: {s}\n')
#        index += 1

#    print(f'A file named {name} has been created and total test scores has been added.')
#    output.writelines(f'The total test scores are: {total: .2f}')

#def getTotal(valueList):
#    total = 0.0

#    for num in valueList:
#        total += num

#    return total

#if __name__ == '__main__':
#    main()

#project 2 - 20 numbers in a list
from asyncio.windows_events import NULL


def main():
    numbers = getNumbers()
    display(numbers)

def getNumbers():
    store = []

    for index in range(0,20):

        number = int(input("Enter a number: "))

        store.append(number)
        
    return store

def display(valueList):
    lowest = NULL
    highest = NULL
    total = NULL
    average = NULL
    index = 0

    for num in valueList:
        
        if index == 0:
            lowest = num
            highest = num
            total += num
        else:
            if lowest > num:
                lowest = num
            if highest < num:
                highest = num
            total += num

        index += 1

    average = total / 20
    aTuple = tuple(valueList)
    print(aTuple)
    print(f'The lowest number in the list is: {lowest}')
    print(f'The hightest number in the list is: {highest}')
    print(f'The total of the numbers in the list is: {total}')
    print(f'The average of the numbers in the list is: {average: .2f}')

if __name__ == '__main__':
    main()