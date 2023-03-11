
# Uriel Renteria
# 3/6/23

#project 1
#salary = float(input("Enter the gross salary: $"))

#while salary < 0:
#    salary = salary = float(input("Enter a positive gross salary: $"))

#percentage = salary * .10
#total = salary + percentage
#print(f"Total gross salary with 10% is: ${total: ,.2f}")

#project 2
#total = 0
#average = 0

#for index in range(5):
#    number = float(input("Enter a score: "))

#    while number < 0:
#        number = float(input("Enter a score greater than 0: "))

#    total += number

#average = total / 5

#print(f"The sum of the scores is: {total: .2f}\nThe average of the scores is: {average: .2f}")

#project 3
#firstName = input("Enter your first name: ")
#lastName = input("Enter your last name: ")
#age = int(input("Enter your age: "))

#while age < 0:
#    print("Error invalid age. Age needs to be greater than 0.")
#    age = int(input("Enter your age: "))

#print("The name enter and age is: " + firstName + " " + lastName + f", {age}")

#project 4
#again = 'y'

#while again == 'y':
#    sales = float(input("Enter the sales amount: $"))

#    if sales >= 50000 and sales < 70000:
#        commission = .1 * sales
        
#    elif sales >= 70000 and sales < 90000:
#        commission = .2 * sales
        
#    elif sales >= 90000 and sales < 100000:
#        commission = .3 * sales
        

#    print(f"Commission: ${commission: ,.2f}")

#    again = input("Enter y for yes to continue or any key to exit: ")

#    print()

#project 5
#again = 'y'

#while again == 'y':
#    sales = float(input("Enter the sales amount: $"))

#    if sales >= 50000 and sales < 70000:
#        salary = 70000.00
#        commission = .1 * salary
#        total = salary + commission
#    elif sales >= 70000 and sales < 90000:
#        salary = 80000.00
#        commission = .2 * salary
#        total = salary + commission
#    elif sales >= 90000 and sales < 100000:
#        salary = 90000.00
#        commission = .3 * salary
#        total = salary + commission

#    print(f"Commission: ${commission: ,.2f}")
#    print(f"Total: ${total:,.2f}")

#    again = input("Enter y for yes to continue or any key to exit: ")

#    print()

##project 6
scores = 0
total = 0.0
average = 0.0

print("Enter 4 grade scores.")
for index in range(4):
    scores = int(input("Enter a grade score: "))
    total += scores

average = total / 4

while average > 100:
    total = 0.0
    print("\nAverage scores are greater than 100. Re-enter 4 new grade scores.")
   
    for index in range(4):
        scores = int(input("Enter a grade score: "))
        total += scores

    average = total / 4

if average >= 90 and average <= 100:
    print(f"The average score is: {average: .2f}. The letter grade is A")
elif average >= 80 and average < 90:
    print(f"The average score is: {average: .2f}. TheThe letter grade is B")
elif average >= 70 and average < 80:
    print(f"The average score is: {average: .2f}. The letter grade is C")
elif average >= 60 and average < 70:
    print(f"The average score is: {average: .2f}. The letter grade is D")
else:
    print(f"The average score is: {average: .2f}. The letter grade is F")

#project 7
#total = 0
#for index in range(1,11):
#    total += index

#print(f"The sum of the number from 1 - 10: {total}")