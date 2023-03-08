# Uriel Renteria
# 2/6/23

#my exercise #1
#print ("Uriel Renteria\n")
#print("2/6/23")

#salary = float(input("Enter salary amount: $"))
#bonus = float(input("Enter bonus amount: $"))

#total = salary + bonus

#print("your pay is " + str(total))

#this program displays a person name with address

#name = "Jason Sim";
#age = 25;
#address = "123 Street";

#print("Kate Austen")
#print('123 Full Circle Drive')
#print ('Asheville, NC 28899')

#print(name + "," + str(age) + "," + address)

#get the users firstname
#firstname = input('enter the first name: ')
##get the users lastname
#lastname = input('enter the last name: ')
##get tyhe output
#print('hello ' + firstname + "," + lastname)

#firstname = input("Enter first name: " + "\n")
#lastname = input("Enter last name: " + "\n")
#address = input("Enter address:  " + "\n")
#city = input("Enter city: " + "\n")
#state = input("Enter state and zip code: " + "\n")

#print("\n" + firstname + "\n" + lastname + "\n" + address + "\n" + city + "\n" + state + '\n')

#name1 = input("Enter employee 1 full name: ")
#hours1 = int(input("Enter employee 1 hours: "))
#pay1 = float(input("Enter employee 1 pay: $"))
#total1 = hours1 * pay1

#name2 = input("\nEnter employee 2 full name: ")
#hours2 = int(input("Enter employee 2 hours: "))
#pay2 = float(input("Enter employee 2 pay: $"))
#total2 = hours2 * pay2

#average = (total1 + total2) / 2

#print("\nEmployee 1 name is " + name1 + "\nHours worked: " + str(hours1) + "\nPay:  $" + str(pay1) + "\nTotal pay: $" + str(total1))

#print("\nEmployee 2 name is " + name2 + "\nHours worked: " + str(hours2) + "\nPay: $" + str(pay2) + "\nTotal pay: $" + str(total2))

#print("\nAverage of pay of " + name1 + " and " + name2 + " is $" + str(average))

#original = float(input("Enter original price: $"))
#discount = original * .2
#sale = original - discount

#print("\nOriginal price: $" + str(original) + "\nDiscount price: $" + str(discount) + "\nSale price: $" + str(sale))

#miles = int(input("Enter the miles driven: "))
#gas = float(input("Enter the gallons of gas used: "))

#mpg = miles / gas

#print("\nMiles driven: " + str(miles) + "\nGallons of gas used: " + str(gas) + "\nMPG = " + str(mpg))

#futureValue = float(input("Enter the desired future value: "))
#rate = float(input("Enter the annual interest rate: "))
#years = int(input("Enter the number of years the money will grow: "))
#presentValue = futureValue // (1.0 + rate) ** years

#print("\nYou will need to deposit this amount: $" + str(presentValue))

#total = float(input("Enter total sales: $"))
#percent = .23
#profit = total * percent

#print(f'\nThe profit is $ {profit : .2f}')

#preSale = float(input("Enter the food charge: $"))
#tip = .18 * preSale
#tax = .07 * preSale
#total = preSale + tip + tax

#print(f'\nPresale charge: ${preSale: .2f}' + f'\nTip: ${tip: .2f}' + f'\nTax: ${tax: .2f}' + f'\nTotal: ${total: .2f}')


#males = int(input("Enter number of male students in class: "))
#females = int(input("Enter number of female students in class: "))

#totalStudents = males + females
#malePercent = males / totalStudents * 100
#femalePercent = females / totalStudents * 100

#print("\nNumber of male students: " + str(males))
#print("Number of female students: " + str(females))
#print("Number of total students: " + str(totalStudents))
##print("\nMale Percentage: " + str(malePercent) + "%")
##print("Female Percentage: " + str(femalePercent) + "%")
#print(f"male percentage: {malePercent: .2f}%")
#print(f"female percentage: {femalePercent: .2f}%")

#buyShares = 2000
#buyPrice = 40.00
#totalBuy = buyShares * buyPrice
#firstBrokerFee =  totalBuy * .03

#soldShares = 2000
#soldPrice = 42.75
#totalSold = soldShares * soldPrice
#secondBrokerFee = totalSold * .03

#leftMoney = totalSold - firstBrokerFee - secondBrokerFee

#print(f"Amount Joe paid for stock: ${totalBuy: .2f}")
#print(f"Amount Joe paid broker fee: ${firstBrokerFee: .2f}")
#print(f"\nAmount Joe sold stock: ${totalSold: .2f}")
#print(f"Amount Joe paid broker fee 2nd round: ${secondBrokerFee: .2f}")

#if(leftMoney < 0) : print(f"\nMoney left over: ${leftMoney: .2f}" + "Joe lost money")
#else : print(f"\nMoney left over: ${leftMoney: .2f}" + "\nJoe made a profit")

#name = input("Enter your name: ")
#address = input("Enter your address: ")
#city = input("Enter your city: ")
#state = input("Enter your state: ")
#zipcode = input("Enter your zipcode: ")
#telephone = input("Enter your telephone number: ")
#major = input("Enter your college major: ")

#print("\nYour name: " + name)
#print("Adress: " + address + ", " + city + ", " + state + ", " + zipcode)
#print("Telephone number: " + telephone)
#print("College major: " + major)


#item1 = float(input("Enter price of first item: $"))
#item2 = float(input("Enter price of second item: $"))
#item3 = float(input("Enter price of third item: $"))
#item4 = float(input("Enter price of fourth item: $"))
#item5 = float(input("Enter price of fifth item: $"))
#subtotal = item1 + item2 + item3 + item4 + item5
#tax = subtotal * .07
#total = subtotal + tax
#print(f"\nSubtotal: ${subtotal: .2f}")
#print(f"Tax: ${tax: .2f}")
#print(f"Total: ${total: .2f}")

#meal = float(input("Enter the meal purchase price: $"))
#tip = meal * .18
#tax = meal * .07
#total = meal + tip + tax
#print(f"Meal price: ${meal: .2f}")
#print(f"Tip: ${tip: .2f}")
#print(f"Tax: ${tax: .2f}")
#print(f"Total: ${total: .2f}")


sugar = 1.5
butter = 1
flour = 2.75
cookies = 48
bake = int(input("Enter number of cookies you want to make: "))
cups = bake / cookies
sugarNew = sugar * cups
butterNew = butter * cups
flourNew = flour * cups
print("\nThe number of cookes you want to make is " + str(bake))
print(f"Number of cups of sugar: {sugarNew: .2f} cups")
print(f"Number of cups of butter: {butterNew: .2f} cups")
print(f"Number of cups of flour: {flourNew: .2f} cups")