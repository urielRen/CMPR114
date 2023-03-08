
# Uriel Renteria
# 2/26/23

#sales = float(input("Enter the amount of sales: "))
#comm_rate =  float(input("Enter the commission rate: "))
#commission = sales * comm_rate
#print("The commission is $", format(commission, ',.2f'))

#sales = float(input("Enter the amount of sales: "))
#comm_rate =  float(input("Enter the commission rate: "))
#commission = sales * comm_rate
#print("The commission is $", format(commission, ',.2f'))

#sales = float(input("Enter the amount of sales: "))
#comm_rate =  float(input("Enter the commission rate: "))
#commission = sales * comm_rate
#print("The commission is $", format(commission, ',.2f'))

#keep_going = 'y'

#while keep_going == 'y':
#    sales = float(input("Enter the amount of sales: "))
#    comm_rate =  float(input("Enter the commission rate: "))
#    commission = sales * comm_rate
#    print("The commission is $", format(commission, ',.2f'))
#    keep_going = input('Do you want to calculate another commission (Enter y for yes): ')

#MAX_TEMP = 102.5
#temperature = float(input("Enter the temperature for today: "))

#while temperature > MAX_TEMP:
#    print("The temperature is too hogh.")
#    temperature = float(input("Enter the new Celsius temperature: "))

#    print("The temperature is acceptable.")


#CHALLENGE 1
#MAX_TEMPS = 102.5
#SETS = 4
#test1 = 0
#test2 = 0
#test3 = 0
#test4 = 0

#while SETS > 0:
#    temp = float(input("Enter a test number: "))

#    while MAX_TEMPS < temp:
#        temp = float(input("Enter a test number lower than 102.5: "))

#    if(SETS == 4):
#        test1 = temp

#    if SETS == 3:
#        test2 = temp

#    if SETS == 2:
#        test3 = temp

#    if SETS == 1:
#        test4 = temp

#    SETS -= 1

#the_Sum = test1 + test2 + test3 + test4
#the_Avg = the_Sum / 4

#print(f"The sum of all 4 test is {the_Sum: .2f}\n" + f"The average of all 4 test is {the_Avg: .2f}")

#keep_going = 'y'
#while keep_going == 'y':
#    sales = float(input("Enter the amount of sales: "))
#    comm_rate =  float(input("Enter the commission rate: "))
#    commission = sales * comm_rate
#    print(f"The commission is ${commission: ,.2f}")

#Challenge 2
#the_Sum = 0;
#SETS = 4

#while SETS > 0:
#    sales = float(input("Enter the amount of sales: "))
#    comm_rate =  float(input("Enter the commission rate: "))
#    commission = sales * comm_rate
#    print("The commission is $", format(commission, ',.2f'))

#    if SETS == 4:
#        comm1 = commission
#    elif SETS == 3:
#        comm2 = commission
#    elif SETS == 2:
#        comm3 = commission
#    else:
#        totalComm = comm1 + comm2 + comm3 + commission
#        print(f"The total sales and commission is ${totalComm: ,.2f}")

#    SETS -= 1

#print('I will display the numbers 1 through 5.')
#for num in [1,2,3,4,5]:
#    print(num)

#challenge 3
#print('I will display even numbers 1 through 10.')
#for num in [1,2,3,4,5,6,7,8,9,10]:
#    if num % 2 == 0:
#        print(num)

#print('I will display odd numbers 1 through 10.')
#for num in [1,2,3,4,5,6,7,8,9,10]:
#    if num % 2 == 1:
#        print(num)

#for name in ['Winken', 'Blinken', 'Nod']:
#    print(name)

#chalenge 4
#for lastName in ['Renteria']:
#    for firstName in ['Uriel']:
#        print('Your full name ' + lastName + ' ' + firstName)

#challenge 5
#for x in range(10):
#    print("Hello World")

#print('Number\tSquare')
#print('--------------')

#for number in range(1,11):
#    square = number**2
#    print(f'{number}\t{square}')

#print('This program displays a list of numbers')
#print('(Starting at 1) and their squares.')
#end = int(input('How high should I go?: '))

#print('Number\tSquare')
#print('--------------')

#for number in range(1,end + 1):
#    square = number**2
#    print(f'{number}\t{square}')

#challenge 1
#MAX = 5
#total = 0.0
#average = 0.0
#print('This program calculates the sum of ')
#print(f'{MAX} number you will enter and the average of the numbers.')

#for counter in range(MAX):
#    number = int(input('Enter a number: '))
#    total += number

#average = total / MAX

#print(f'The total is {total} ' + f'The average is {average}')

#MARK_UP = 2.5
#another = 'y'

#while another == 'y' or another == "Y":
#    wholesale = float(input("Enter the item's wholesale cost: $"))

#    while wholesale < 0:
#        print('Cannot be a negative #, try again')
#        wholesale = float(input('Eter the correct wholesale cost: $'))

#    retail = wholesale * MARK_UP
#    print(f'Retail price ${retail:,.2f}')
#    another = input('Do you have another item? (Enter y for yes): ')

#TAX_FACTOR = 0.0065
#print('Enter the prpoerty lot number or enter 0 to end')
#lot = int(input('Lot number: '))

#while lot != 0:
#    value = float(input('Enter the property value: $'))
#    tax = value * TAX_FACTOR
#    print(f'Property tax: ${tax:,.2f}')
#    print('Enter the prpoerty lot number or enter 0 to end')
#    lot = int(input('Lot number: '))

#challenge 2
#product = 0

#while product < 100:
#    value = int(input('Enter a number: '))
#    product = value * 10
#    print(f'The product of the value you enter is {product}')

#print('The product of the number you enter multiplied by 10 is greater than 100.')

#challenge 3
#total = 0;

#for counter in range(5):
#    day = int(input('Enter the number of bugs cuaght today: '))
#    total += day

#print(f'The total number of bugs caught after 5 days is {total}')

#challenge 4
#BURN = 4.2
#minutes = 0
#total = 0.0

#print('The program will display the calories burn after 10 minutes.')
#while minutes < 31:
#    total += BURN
    
#    if minutes % 5 == 0 and minutes > 9:
#       print(f'The calories burned at {minutes}' + f' is {total: .1f}')
       
#    minutes += 1

#challenge 5
#slowest = 0
#fastest = 0.0
#total = 0.0
#average = 0.0
#lapTime = 0.0

#lapRun = int(input('Enter the number of laps run in a racetrack: '))

#for counter in range(1, lapRun + 1):
#    lapTime = float(input('Enter the lap time: '))
#    total += lapTime

#    if counter == 1:
#        slowest = lapTime
#        fastest = lapTime
#    else:
#        if slowest > lapTime:
#            slowest = lapTime

#        if fastest < lapTime:
#            fastest = lapTime

#average = total / lapRun

#print(f'The fastest lap time is {fastest: .2f}')
#print(f'The slowest lap time is {slowest: .2f}')
#print(f'The average lap time is {average: .2f}')

#evenNumbers = [2,4,6,8,10]
#print(evenNumbers)

#names = ["ian", "jason", "molly"]
#print(names)

#info = ["ally", 27, 1550.87]
#print(info)

#number = [5] * 5
#print(number)

#LoopNumbers = [1,2,3,4,5,6,7]
#for n in LoopNumbers:
#    print(n)

#index = 0
#while index < 4:
#    print(LoopNumbers[index])
#    index += 1

#size = len(LoopNumbers)
#print(size)

#evenNumbers = [2,4,6,8,10]
#print(evenNumbers[0])

#sum = 0
#evenNumbers = [2,4,6,8,10]
#for a in evenNumbers:
#    sum += a

#print(evenNumbers[0])
#print('Total sum ' + str(sum))

#def main1():
#    prodNums = ['V4T5', 'F987', 'Q143', 'R688']
#    search = input("Enter a product: ")
#    if search in prodNums:
#        print(search, ' was found on the list')
#    else:
#        print(search, ' was not found on the list')

#main1()

#def main2():
#    nameList = []
#    again = 'y'
    
#    while  again == 'y':
#        name = input('Enter a name: ')
#        nameList.append(name)
#        print('Do you want to add another name? ')
#        again = input('y = yes, hit any other key for NO: ')
#        print()

#    print('Here are the names you entered: ')
#    for name in nameList:
#        print(name)

#    outfile = open('names.txt', 'w')
#    outfile.write(str(nameList))
#    outfile.close()
#    print('Recorded the names in the list')

#main2()

#def main():
#    names = ['Howard', 'Jamie', 'Jill']
#    print('The list before the insert or remove')
#    print(names)
#    NameRemove = input('Enter the name to remove: ')
#    names.insert(0, 'Joe')
#    names.remove(NameRemove)
#    print('The list after the insert')
#    print(names)

#main()

#def total():
#    numbers = [1,2,3,4,5,6,7,8,9,10]
#    sum = 0
#    for value in numbers:
#        sum += value
#    average = sum / len(numbers)
#    print('The total is ', sum, ' the average is ', average)
#    outfile = open('numbers.txt', 'w')
#    outfile.write(str(numbers))
#    outfile.close()
#    print('Recorded the names in the list')


#total()

#challenge 4
#def main():
#    daysInTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#    weekSales = []
#    print('Enter the sales for the week.\n')
#    index = 0
#    for i in daysInTheWeek:
#        sale = float(input(f"Enter the sales for {i}: "))
#        weekSales.insert(index,sale)
#        index += 1
#    totalSales = total(weekSales)
#    print(f'The total sales of the week is ${totalSales:,.2f}')
#    write('weekSales.txt', weekSales, totalSales)

#def total(numbers):
#    sum = 0
#    for value in numbers:
#        sum += int(value or 0)
#    return sum

#def write(name, sales, total):
#    output = open(name, 'w')
#    for money in sales:
#        output.writelines(str(money) + '\n')
#    output.writelines(f'Total sales: ${total:,.2f}')

#main()

#def main():
#    monthOfTheYear = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#    monthlyRain = []
#    print('Enter the rain fall for each month.\n')
#    index = 0
#    for i in monthOfTheYear:
#        rain = float(input(f'Enter the amount of rain for {i}: '))
#        monthlyRain.insert(index,rain)
#        index += 1

#    totalRain = total(monthlyRain)
#    averageRain = totalRain / len(monthlyRain)
#    lessRain = min(monthlyRain)
#    lessRainIndex = monthlyRain.index(lessRain)
#    mostRain = max(monthlyRain)
#    mostRainIndex = monthlyRain.index(mostRain)
#    print(f'The total rain in the year was: {totalRain}')
#    print(f'The average rain in each month is: {averageRain: .2f}')
#    print(f'The month with lowest rain was {monthOfTheYear[lessRainIndex]} with {lessRain} inches of rain.')
#    print(f'The month with highest rain was {monthOfTheYear[mostRainIndex]} with {mostRain} inches of rain.')

#    write('yearlyRain.text', monthlyRain, totalRain, monthOfTheYear)

#def total(numbers):
#    sum = 0
#    for value in numbers:
#        sum += int(value or 0)
#    return sum

#def write(name, monthlyRain, total, monthOfTheYear):
#    index = 0
#    output = open(name,'w')
#    for rain in monthlyRain:
#        output.writelines(f'{monthOfTheYear[index]}: {rain} inches\n')
#        index += 1
#    output.writelines(f'Total rain: {total: .2f} inches')
#    output.writelines(f'The average rain on this year was {total / len(monthOfTheYear)} inches')
#    lessRain = min(monthlyRain)
#    lessRainIndex = monthlyRain.index(lessRain)
#    mostRain = max(monthlyRain)
#    mostRainIndex = monthlyRain.index(mostRain)
#    output.writelines(f'The month with lowest rain was {monthOfTheYear[lessRainIndex]} with {lessRain} inches of rain.')
#    output.writelines(f'The month with highest rain was {monthOfTheYear[mostRainIndex]} with {mostRain} inches of rain.')

#main()
