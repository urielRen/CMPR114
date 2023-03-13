# Uriel Renteria
# 2/13/23
#
#
# 


#Project 1 Quarter of the Year
the_months = int(input('Enter a month from 1 - 12: '))
if the_months >= 1 and the_months <= 3:
    print('The month is in the first quarter')
elif the_months >= 4 and the_months <= 6:
    print('The month is in the second quarter')
elif the_months >= 7 and the_months <= 9:
    print('The month is in the second quarter')
elif the_months >= 10 and the_months <= 12:
    print('The month is in the second quarter')
else:
    print('The number you input was invalid')



#Project 2 Hot Dog Cookout Calculator
packages = 10
buns = 8
people = int(input('Enter number of people for the cookout: '))
eaten = int(input('Enter number of hot dogs each person will eat: '))
total = people * eaten

min_Packages = total // packages
total_min_packages = total - (packages * (min_Packages))

if total_min_packages > 0 and total_min_packages < 9:
    min_Packages += 1
else:
    min_Packages = min_Packages

min_Buns  = total // buns
total_min_buns = total - (buns * (min_Buns))

if total_min_buns > 0 and total_min_buns < 9:
    min_Buns += 1
else:
    min_Buns = min_Buns

leftover_Packages = (packages * (min_Packages)) - total
leftover_Buns = (buns * (min_Buns)) - total
print('\nTotal number of hot dogs: ' + str(total))
print("\nMinimum packages of hot dogs is: " + str(min_Packages))
print("Minimum packages of hot dogs buns is: " + str(min_Buns))
print("Number of hot dogs left over is: " + str(leftover_Packages))
print("Number of hot dogs buns left over is: " + str(leftover_Buns))


#Project 3 Software Sales
retail = 99
software = int(input('Enter number of packages purchased: '))
preDiscount = retail * software

if software >= 10 and software <= 19:
    discount = preDiscount * .1
elif software >= 20 and software <= 49:
    discount = preDiscount * .2
elif software >= 50 and software <= 99:
    discount = preDiscount * .3
elif software >= 100:
    discount = preDiscount * .4
else:
    discount = 0

total = preDiscount - discount
print(f"The amount of discount (if any): ${discount: .2f}")
print(f"The total amount of purchase after discount: ${total: .2f}")



#In class exercises
#high_score = 95
#test1 = int(input("Enter test score 1: "))
#test2 = int(input("Enter test score 2: "))
#test3 = int(input("Enter test score 3: "))
#average = (test1 + test2  +test3)/3
#print('The average score is ' + str(average))
#if average >= high_score:
#    print('Congrats')
#else:
#    print('Try harder next time')

#test1 = int(input("Enter test score 1: "))
#test2 = int(input("Enter test score 2: "))
#test3 = int(input("Enter test score 3: "))
#average = (test1 + test2  +test3)/3
#print('The average score is ' + str(average))

#if average > 100:
#    print("the average cannot be over 100, try again")
#elif average >= 90 and average <= 100:
#    print('Letter grade A', round(average))
#elif average >= 80 and average <= 89:
#    print('Letter grade B', round(average))
#elif average >= 70 and average <= 79:
#    print('Letter grade C', round(average))
#elif average >= 60 and average <= 69:
#    print('Letter grade D', round(average))
#else:
#    print('Letter grade F', round(average))

#f = open("C:\\Users\\uriel\\OneDrive\\Documents\\CMPR 114\\week2\\week2\\Grades.txt", "a")
#f.write('\nthe average score is ' + str(round(average)))
#f.close()
#f = open("Grades.txt", "r")
#print(f.read())

#temp = float(input("Enter the current tempeature: "))
#if temp < 40:
#    print("A little cold, isn't it?")
#else:
#    print("Nice weather we're having.")


#sales = float(input("Enter sales amount: $"))
#if sales > 50000:
#    bonus = 500.0
#    commision_rate = 0.12
#    total = sales * commision_rate + bonus
#    print("You met your sales quota! \n$" + str(total))
#else:
#    print("You didn't meet your sales quota!")

#rate = float(input("Enter the pay rate: $"))
#hours = int(input("Enter the # of hours worked: "))
#full = 40
#if hours <= full:
#    sal = hours * rate
#    print("The salary is $" + str(sal))
#else:
#    sal = (full * rate) + (hours - full) * rate * 1.5
#    print("The salary is $" + str(sal))

#print("Days of the week program")
#enter = int(input("Enter the day of the week, from 1-7 : "))
#if enter == 1:
#    print("Today is Monday")
#elif enter == 2:
#    print("Today is Tuesday")
#elif enter == 3:
#    print("Today is Wednesday")
#elif enter == 4:
#    print("Today is Thursday")
#elif enter == 5:
#    print("Today is Friday")
#elif enter == 6:
#    print("Today is Saturday")
#elif enter == 7:
#    print("Today is Sunday")
#else:
#    print("Invalid entry, try again")

#PersonAge = int(input("Enter your age: "))
#if PersonAge < 0:
#    print('Invalid')
#elif PersonAge <= 1:
#    print('infant')
#elif PersonAge > 1 and PersonAge < 13:
#    print('child')
#elif PersonAge >= 13 and PersonAge < 20:
#    print('teen')
#elif PersonAge >= 20:
#    print('Adult')

#roman = int(input("Enter a number from 1-10: "))
#if roman == 1:
#    print("Roman Numeral is I")
#elif roman == 2:
#    print("Roma Numeral is II")
#elif roman == 3:
#    print("Roma Numeral is III")
#elif roman == 4:
#    print("Roma Numeral is IV")
#elif roman == 5:
#    print("Roma Numeral is V")
#elif roman == 6:
#    print("Roma Numeral is VI")
#elif roman == 7:
#    print("Roma Numeral is VII")
#elif roman == 8:
#    print("Roma Numeral is VII")
#elif roman == 9:
#    print("Roma Numeral is IX")
#elif roman == 10:
#    print("Roma Numeral is X")
#else:
#    print("Number is out of range from 1 - 10, try again")


#test1 = input("Enter test score 1: ")
#test2 = input("Enter test score 2: ")
#mainExam = input("Enter main exam: ")

#if int(test1) < 0 and int(test1) > 25:
#    print("Test score 1 is out of range from 0 - 25")
#elif int(test2) < 0 and int(test2) > 25:
#    print("Test score 2 is out of range from 0 - 25")
#elif int(mainExam) < 0 and int(mainExam) > 50:
#    print("Main Exam is out of range from 0 - 50")
#else:
#    total = int(test1) + int(test2) + int(mainExam)
#    if int(mainExam) < 25:
#        print("Total point is " + str(total) + " grade: Fail")
#    elif total > 80:
#        print("Total point is " + str(total) + " grade: Distinction")
#    elif total > 60 and total < 80:
#        print ("Total point is " + str(total) + " grade: Credit")
#    elif total < 60 and total > 50:
#        print ("Total point is " + str(total) + " grade: Pass")
#    else:
#        print("Total point is " + str(total) + " grade: Fail")

#name1 = 'Mary'
#name2 = 'Mark'
#if name1 == name2:
#    print("The names are the same.")
#else:
#    print('The name are Not the same.')

#password = input("Enter the password: ")
#if password == 'sac123':
#    print("Password accepted.")
#else:
#    print("Sorry, that is the wrong password")


#name1 = input('Enter a name (last name first): ')
#name2 = input('Enter a another name (last name first): ')
#print('Here are the names, listed alphabetically')
#if name1 < name2:
#    print(name1)
#    print(name2)
#else:
#    print(name2)
#    print(name1)

#min_Salary = 30000.0
#min_Years = 2
#salary = float(input('Enter your annual salary: $'))
#years = int(input('Enter the number of years employed: '))
#if salary >= min_Salary:
#    if years >= min_Years:
#        print('You qualify for a loan')
#    else:
#        print(f'You must have been employed 'f' for at least {min_Years} 'f' years to qualify')
#else:
#    print(f'You must earn at least $ 'f'{min_Salary: ,.2f} 'f' per year to qualify.')


#pocket = int(input('Enter a pocket number from 0 - 36: '))

#if pocket == 0:
#    print('Pocket is green')
#elif pocket >= 1 and pocket <= 10:
#    if pocket % 2:
#        print('Pocket is red')
#    else:
#        print('Pocket is black')
#elif pocket >= 11 and pocket <= 18:
#    if pocket % 2:
#        print('Pocket is black')
#    else:
#        print('Pocket is red')
#elif pocket >= 19 and pocket <= 28:
#    if pocket % 2:
#        print('Pocket is red')
#    else:
#        print('Pocket is black')
#elif pocket >= 29 and pocket <= 36:
#    if pocket % 2:
#        print('Pocket is black')
#    else:
#        print('Pocket is red')
#else:
#    print('Pocket number is out of range from 0 - 36')

#pounds = int(input('Enter weight of package: '))
#if pounds < 2 and pounds >= 0:
#    print('Shipping charge for ' + str(pounds) + ' pounds is  $1.50')
#elif pounds > 2 and pounds < 6:
#    print('Shipping charge for ' + str(pounds) + ' pounds is  $3.00')
#elif pounds > 6 and pounds < 10:
#    print('Shipping charge for ' + str(pounds) + ' pounds is  $4.00')
#else:
#    print('Shipping charge for ' + str(pounds) + ' pounds is  $4.75')