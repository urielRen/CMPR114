# Uriel Renteria
# 3/12/23
# week 5


# PART 1
# Project 1
#def message1():
#    print('message 1')

#message1()

#def message2():
#    print('message 2')

#message2()

# Project 2
#def message1():
#    lastname = input('Enter the lastname: ')
#    firstname = input('Enter the firstname: ')
#    print('The lastname is ', lastname, ' the fristname is', firstname)

#message1()

# Project 3
#def main():
#    texas()
#    california()

#def texas():
#    birds = 5000
#    print(f'Texas has {birds} birds')

#def california():
#    birds = 8000
#    print(f'California has {birds} birds')

#main()

# Exercise 1
#def main():
#    texas()
#    california()

#def texas():
#    birds = int(input("Enter the number of birds in Texas: "))
#    print(f'Texas has {birds} birds')

#def california():
#    birds = int(input('Enter the number of birds in California: '))
#    print(f'California has {birds} birds')

#main()

# Project 4
#def main():
#    first_name = input('Enter your first name: ')
#    last_name = input('Enter your last name: ')
#    print('Your name reversed is ')
#    reverse_name(first_name, last_name)

#def reverse_name(first, last):
#    print(last,first)

#main()

# Exercise 2
#def main():
#    details()

#def details():
#    lastName = input('Enter your last name: ')
#    firstName = input('Enter your first name: ')
#    adress = input('Enter your adress: ')
#    city = input('Enter the city: ')
#    state = input('Enter the state: ')
#    zipcode = input('Enter your zip code: ')
#    print('\nName: ', firstName, lastName)
#    print('Adress: ', adress)
#    print('City: ', city)
#    print('State: ', state)
#    print('Zip code: ', zipcode)

#main()

# Project 5
#number = 0

#def main():
#    global number
#    number = int(input('Enter a number: '))
#    show_number()

#def show_number():
#    print(f'The number you entered is {number}.')

#def add(num1, num2):
#    global total
#    total = num1 + num2
#    return total

#add(3,4)
#print('Total: {total}')

#main()

# Exercise 3
#def add(num1, num2, num3):
#    global total
#    total = num1 + num2 + num3
#    return total

#add(3,4,9)
#print(f'Total: {total}')


# Exercise 4
#def main():
#    num1 = int(input('Enter a number: '))
#    num2 = int(input('Enter a number: '))
#    num3 = int(input('Enter a number: '))
#    the_total = add(num1, num2, num3)
#    the_average(the_total)
#    print(f'Sum: {the_total}')
#    print(f'Average: {average: .2f}')
    
#def add(num1, num2, num3):
#    global total
#    total = num1 + num2 + num3
#    return total

#def the_average(the_total):
#    global average
#    average = total / 3
#    return average

#main()

# Project 6
#CONTRIBUTION_RATE = 0.05

#def main():
#    gross_pay = float(input('Enter the gross pay: $'))
#    bonus = float(input('Enter the amount of bonuses: $'))
#    show_pay_contrib(gross_pay)
#    show_bonus_contrib(bonus)

#def show_pay_contrib(gross):
#    contrib = gross * CONTRIBUTION_RATE
#    print(f'Contribution for gross pay: ${contrib: ,.2f}')

#def show_bonus_contrib(bonus):
#    contrib = bonus * CONTRIBUTION_RATE
#    print(f'Contribution for bonuses: ${contrib: ,.2f}')

#main()


# Exercise 5
#HOUR = 40

#def main():
#    worked = int(input('Enter hours worked: '))
#    pay = float(input('Enter hourly pay: $'))
#    total(worked, pay)
#    print(f'Your pay is: ${hours: ,.2f}')

#def total(worked, pay):
#    global hours

#    if worked > HOUR:
#        hours = ((worked - HOUR) * 1.5 * pay) + (worked * pay)
#    else:
#        hours = worked * pay
#    return hours

#main()


# PART 2
# Project 1
#import random

#def main():
#    number = random.randint(1,10)
#    print(f'The number is {number}.')

#main()

#import random

#for num in range(20):
#    print(random.randint(1,10))

# Project 2
#import random

#HEADS = 1
#TAILS = 2
#TOSSES = 10

#def main():
#    for toss in range(TOSSES):
#        if random.randint(HEADS, TAILS) == HEADS:
#            print('Heads')
#        else:
#            print('Tails')

#main()

# Project 3
#import random 

#while True:
#    user = input("Enter a choice (rock, paper, scissor): ")
#    possible_actions = ["rock", "paper", "scissors"]
#    computer = random.choice(possible_actions)
#    print(f"\nYou chose {user}, computer chose {computer}.\n")

#    if user == computer:
#        print(f"Both players selected {user}. It's a tie!")
#    elif user == "rock":
#        if computer == "scissors":
#            print("Rock smashes scissors! You win!")
#        else:
#            print("Paper covers rock! You lose.")
#    elif user == "paper":
#        if computer == "rock":
#            print("Paper covers rock! You win!")
#        else:
#            print("Scissors cuts paper! You lose.")
#    elif user == "scissors":
#        if computer == "paper":
#            print("Scissors cuts paper!! You win!")
#        else:
#            print("Rock smashes scissors! You lose.")

#    play_again = input("Play again? (y/n): ")
#    if play_again.lower() != "y":
#        break

# Project 4
#import math
#def main():
#    number = float(input("Enter a number: "))
#    square_root = math.sqrt(number)
#    print(f"The square root of {number} is {square_root}.")

#main()

# Exercise 1
#CONVERTION_RATE = 0.6214

#def main():
#    distance = float(input('Enter distance in kilometers: '))
#    convertion(distance)
#    print(f"{distance: .2f} kilometers = {miles: .2f} miles")

#def convertion(temp):
#    global miles
#    miles = temp * CONVERTION_RATE
#    return miles

#main()

#Exercise 2
#MONTH = 12

#def main():
#    loan = float(input('Enter loan payment: $'))
#    insurance = float(input('Enter insurance payment: $'))
#    gas = float(input('Enter gas expenses: $'))
#    oil = float(input('Enter oil expenses: $'))
#    tires = float(input('Enter tire expenses: $'))
#    maintenance = float(input('Enter maintenance expenses: $'))
#    the_month = monthly_cost(loan, insurance, gas, oil, tires, maintenance)
#    annual_cost(the_month)

#def monthly_cost(loan, insurance, gas, oil, tires, maintenance):
#    global monthly
#    monthly = loan + insurance + gas + oil + tires + maintenance
#    return monthly

#def annual_cost(the_month):
#    annual = MONTH * the_month
#    print(f'\nMonthly costs for your automobile: ${the_month: ,.2f}')
#    print(f'Annual costs for your automobile: ${annual: ,.2f}')

#main()