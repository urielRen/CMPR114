# Uriel Renteria
# 3/19/23

# Project 1
## to write to a file
#def write():
#    outFile = open('myFile.txt', 'w')


#    outFile.write('Jason\n')
#    outFile.write('Jill\n')
#    outFile.write('Jake\n')

#    outFile1.write('Jason\n')
#    outFile1.write('Jill\n')
#    outFile1.write('Jake\n')

#    outFile.close()
#    outFile1.close()

#    print('The names haven been recorded')

#write()

## to read a file
#def read():
#    infile = open('myFile.txt', 'r')

#    fileContents = infile.read()
#    fileContents1 = infile1.read()

#    print(fileContents)
#    print(fileContents1)

#read()

## to write input and output into a file
#def WriteInput():
#    print("Enter the name of your friends: ")
#    writeMoreFriends = 'Y'

#    while writeMoreFriends == 'Y' or writeMoreFriends == 'y':
#        name1 = input('Friend #1: ')
#        name2 = input('Freind #2: ')
#        name3 = input('Friend #3: ')

#        FriendFile = open('friends.txt', 'a')

#        FriendFile.write(name1 + '\n')
#        FriendFile.write(name2 + '\n')
#        FriendFile.write(name3 + '\n')

#        FriendFile.close()

#        print('Friends recorded.')

#        writeMoreFriends = input('Do you want to write more friends? type Y or y: ')

#WriteInput()


## Exercise 1
#def main():
#    writeFile()
#    readFile()

#def writeFile():
#    firstName = input('Enter your first name: ')
#    lastName = input('Enter your last name: ')
#    age = int(input('Enter your age: '))

#    outFile = open('exercise1.txt', 'w')

#    outFile.write(firstName + '\n')
#    outFile.write(lastName + '\n')
#    outFile.write(str(age) + "\n")

#    outFile.close()

#    print("\nYour first name, last name and age have been written to a file.\n\n")

#def readFile():
#    inFile = open('exercise1.txt', 'r')

#    fileContents = inFile.read()
#    inFile.close()

#    print(fileContents)

#    print('The file has been read.')

#if __name__ == '__main__':
#    main()


# Project 2
#def WriteNumbers():
#    outfile = open('numbers.txt', 'a')

#    num1 = int(input('Enter #1: '))
#    num2 = int(input('Enter #2: '))
#    num3 = int(input('Enter #3: '))

#    add = num1 + num2 + num3
#    avg = add / 3

#    outfile.write('The 1st number is ' + str(num1) + '\n')
#    outfile.write('The 2nd number is ' + str(num2) + '\n')
#    outfile.write('The 3rd number is ' + str(num3) + '\n')
#    outfile.write('The avg number is ' + str(avg) + '\n')
#    outfile.write('The total number is ' + str(add) + '\n')

#    outfile.close()

#    print('Data recorded.')

#WriteNumbers()

# Excercise 2
#def WriteNumbers():
#    outfile = open('numbers.txt', 'a')

#    num1 = int(input('Enter #1: '))
#    num2 = int(input('Enter #2: '))
#    num3 = int(input('Enter #3: '))

#    add = num1 + num2 + num3
#    avg = add / 3

#    outfile.write('The 1st number is ' + str(num1) + '\n')
#    outfile.write('The 2nd number is ' + str(num2) + '\n')
#    outfile.write('The 3rd number is ' + str(num3) + '\n')
#    outfile.write('The avg number is ' + str(avg) + '\n')
#    outfile.write('The total number is ' + str(add) + '\n')

#    outfile.close()

#    print('Data recorded.')

#def main():
#    WriteNumbers()
#    ReadNumbers()

#def ReadNumbers():
#    infile = open('numbers.txt', 'r')

#    readCont = infile.read()

#    print('\nThis are numbers inside the file.\n')
#    print(readCont)

#    infile.close()

#    print('The file has been open.')

#if __name__ == '__main__':
#    main()

# Project 3
#def sales():
#    num_days = int(input('Enter the days of sales: '))
#    sales_file = open('sales.txt', 'a')

#    for count in range(1, num_days + 1):
#        sales = float(input(f'Enter the sales for day # {count: .0f}: $'))
#        sales_file.write(f'{sales: .0f}\n')

#    sales_file.close()
#    print('Sales recorded.')

#sales()

#def ReadSales():
#    sales_file = open('sales.txt', 'r')
#    line = sales_file.readline()

#    while line != '':
#        amount = float(line)
#        print(format(amount, '.2f'))
#        line = sales_file.readline()

#    sales_file.close()

#ReadSales()

# Exercise 3
#def sales():
#    salary = float(input('Enter the salary: $'))
#    num_days = int(input('Enter the days of sales: '))
#    sales_file = open('sales.txt', 'a')
#    salary_file = open('salary.txt', 'a')
#    total = 0

#    for count in range(1, num_days + 1):
#        sales = float(input(f'Enter the sales for day # {count: .0f}: $'))
#        total += sales
#        sales_file.write(f'{sales: .0f}\n')

#    if total > 1000:
#        newSalary = salary + (total * .1)
#        salary_file.write(f'Salary ${salary: ,.2f}\n')
#        salary_file.write(f'Total with commission ${newSalary: ,.2f}\n')

#    sales_file.close()
#    print('Sales recorded.')

#def ReadSales():
#    sales_file = open('sales.txt', 'r')
#    line = sales_file.readline()

#    while line != '':
#        amount = float(line)
#        print(format(amount, '.2f'))
#        line = sales_file.readline()

#    sales_file.close()

#def ReadSalary():
#    salary_file = open('salary.txt', 'r')
#    line = salary_file.read()

#    print(line)
#    salary_file.close()

#def main():
#    sales()
#    ReadSales()
#    ReadSalary()

#if __name__ == '__main__':
#    main()

# Project 4
#def main():
#    writeFile()
#    readFile()

#def writeFile():
#    num_emps = int(input('Enter a number of employee records: '))

#    emp_file = open('employees.txt', 'w')

#    for count in range(1, num_emps + 1):
#        print('Enter data for employee #', count)
#        name = input('Name: ')
#        id_num = input('ID NUMBER: ')
#        dept = input('DEPARTMENT: ')

#        emp_file.write(name + '\n')
#        emp_file.write(id_num + '\n')
#        emp_file.write(dept + '\n')

#        print()

#    emp_file.close()

#    print('Recorded')

#def readFile():
#    emp_file = open('employees.txt', 'r')
#    line = emp_file.read()
#    emp_file.close()

#    print(line)
#    print('Open the file and read the contents.')

#main()

# Project 5
#def main():
#    while True:
#        try:
#            hours = int(input('Hours worked: '))
#            pay = float(input('Hourly pay: $'))
#            gross = hours * pay
#            print('Gross pay $', format(gross, ',.2f'))
#            break

#            print('Recorded')
#        except ValueError:
#            print('ERROR: hours worked and pay must be valid numbers, try again')
#        except Exception as err:
#            print(err)

#main()

# Project 5
#from email import message
#import tkinter as tk
#from tkinter import messagebox

#win = tk.Tk()
#win.geometry("300x100")
#win.title("Customer Information")

#lblLastName = tk.Label(win, text = 'Enter the lastname').grid(column = 0, row = 0)
#lblFirstName = tk.Label(win, text = 'Enter the firstname').grid(column = 0, row = 1)


#def write():
#    text_file = open('Customers.txt', 'a')
#    content = text_file.write('\nConfirmation: ' + str(LN.get()) + ", " + str(FN.get()))
#    text_file.close()
#    messagebox.showinfo('information', 'Data Recorded')

#def quit():
#    messagebox.showinfo('information', 'Thank you...')
#    win.destroy()

#def submit():
#    messagebox.showinfo('information', 'entered: ' + LN.get() + ", " + FN.get())

#LN = tk.StringVar()
#txtLastname = tk.Entry(win, width = 12, textvariable= LN).grid(column = 1, row = 0)
#FN = tk.StringVar()
#textFirstname = tk.Entry(win, width = 12, textvariable= FN).grid(column = 1, row = 1)

#btnSubmit = tk.Button(win, text = "submit", command = submit).grid(column = 0, row = 4)
#btnQuit = tk.Button(win, text = 'quit', command = quit).grid(column = 1, row = 4)
#btnWrite = tk.Button(win, text = 'transfer', command = write).grid(column = 2, row = 4)

#win.mainloop()
#submit()

#Exercise 5
#import tkinter as tk
#from tkinter import messagebox

#win = tk.Tk()
#win.geometry("300x100")
#win.title("Customer Information")

#lblLastName = tk.Label(win, text = 'Enter the lastname').grid(column = 0, row = 0)
#lblFirstName = tk.Label(win, text = 'Enter the firstname').grid(column = 0, row = 1)
#lblAdress = tk.Label(win, text = 'Enter adress').grid(column = 0, row = 2)
#lblCity = tk.Label(win, text = 'Enter a city').grid(column = 0, row = 3)
#lblState = tk.Label(win, text = 'Enter a state').grid(column = 0, row = 4)
#lblZipcode = tk.Label(win, text = 'Enter zip code').grid(column = 0, row = 5)

#def write():
#    text_file = open('Customers.txt', 'a')
#    content = text_file.write('\nConfirmation: ' + str(LN.get()) + ", " + str(FN.get()) + "\n" + str(AD.get()) + '\n' + str(CI.get()) + ", " + str(ST.get()) + " " + str(ZC.get()))
#    text_file.close()
#    messagebox.showinfo('information', 'Data Recorded')

#def quit():
#    messagebox.showinfo('information', 'Thank you...')
#    win.destroy()

#def submit():
#    messagebox.showinfo('information', 'Entered: ' + LN.get() + ", " + FN.get() + "\n" + AD.get() + "\n" + CI.get() + ", " + ST.get() + " " + ZC.get())

#LN = tk.StringVar()
#txtLastname = tk.Entry(win, width = 12, textvariable= LN).grid(column = 1, row = 0)
#FN = tk.StringVar()
#textFirstname = tk.Entry(win, width = 12, textvariable= FN).grid(column = 1, row = 1)
#AD = tk.StringVar()
#txtAdress = tk.Entry(win, width = 12, textvariable= AD).grid(column = 1, row = 2)
#CI = tk.StringVar()
#txtAdress = tk.Entry(win, width = 12, textvariable= CI).grid(column = 1, row = 3)
#ST = tk.StringVar()
#txtAdress = tk.Entry(win, width = 12, textvariable= ST).grid(column = 1, row = 4)
#ZC = tk.StringVar()
#txtAdress = tk.Entry(win, width = 12, textvariable= ZC).grid(column = 1, row = 5)

#btnSubmit = tk.Button(win, text = "submit", command = submit).grid(column = 0, row = 7)
#btnQuit = tk.Button(win, text = 'quit', command = quit).grid(column = 1, row = 7)
#btnWrite = tk.Button(win, text = 'transfer', command = write).grid(column = 2, row = 7)

#win.mainloop()
#submit()

## Exercise 6
#import tkinter as tk
#from tkinter import messagebox

#win = tk.Tk()
#win.geometry("300x100")
#win.title("Exercise 6")

#lblNumber1 = tk.Label(win, text = 'Enter a number').grid(column = 0, row = 0)
#lblNumber2 = tk.Label(win, text = 'Enter a number').grid(column = 0, row = 1)
#lblNumber3 = tk.Label(win, text = 'Enter a number').grid(column = 0, row = 2)

#def write():
#    num1 = int(N1.get())
#    num2 = int(N2.get())
#    num3 = int(N3.get())
#    SU = num1 + num2 + num3
#    AV = SU / 3
#    text_file = open('NumbersPart6.txt', 'a')
#    content = text_file.write('\nNumber 1: ' + str(N1.get()) + "\nNumber 2: " + str(N2.get()) + "\nNumber 3: " + str(N3.get()) + '\nTotal: ' + str(SU) + f"\nAverage: {AV: .0f}")
#    text_file.close()
#    messagebox.showinfo('Information', 'Data Recorded')

#def quit():
#    messagebox.showinfo('Information', 'Thank you...')
#    win.destroy()

#def submit():
#    num1 = int(N1.get())
#    num2 = int(N2.get())
#    num3 = int(N3.get())
#    SU = num1 + num2 + num3
#    AV = SU / 3
#    messagebox.showinfo('information', 'Entered:\nNumber 1: ' + str(N1.get()) + "\nNumber 2: " + str(N2.get()) + "\nNumber 3: " + str(N3.get()) + "\nTotal: " + str(SU) + f"\nAverage: {AV: .0f}")

#N1 = tk.StringVar()
#txtNum1 = tk.Entry(win, width = 12, textvariable= N1).grid(column = 1, row = 0)
#N2 = tk.StringVar()
#textNum2 = tk.Entry(win, width = 12, textvariable= N2).grid(column = 1, row = 1)
#N3 = tk.StringVar()
#txtNum3 = tk.Entry(win, width = 12, textvariable= N3).grid(column = 1, row = 2)

#btnSubmit = tk.Button(win, text = "submit", command = submit).grid(column = 0, row = 6)
#btnQuit = tk.Button(win, text = 'quit', command = quit).grid(column = 1, row = 6)
#btnWrite = tk.Button(win, text = 'transfer', command = write).grid(column = 2, row = 6)

#win.mainloop()
#submit()

## Exercise 7
#def main():
#    getGrades()
#    readFile()

#def getGrades():
#    fullName = input('Enter your full name: ')

#    try:
#        midterm = int(input('Enter midterm score: '))
#        final = int(input('Enter final score: '))

#        if midterm < 0 or midterm > 100:
#            raise Exception('Midterm needs to be between 0 or 100')
#        if final < 0 or final > 100:
#            raise Exception('Final needs to be between 0 or 100')

#    except ValueError:
#        print('ERROR: midterm and final need to be integer numbers. Try again')
#    else: 
#        total = midterm + final
#        average = total / 2

#        if average > 90 or average < 100:
#            letter = 'A'
#        elif average > 80 or average < 90:
#            letter = 'B'
#        elif average > 70 or average < 80:
#            letter = 'C'
#        elif average > 60 or average < 70:
#            letter = 'D'
#        else:
#            letter = 'F'

#        text_file = open('exercise7.txt', 'a')

#        text_file.write('\nRead from file:\n')
#        text_file.write('Full name: ' + fullName + '\n')
#        text_file.write(f'Midterm: {midterm: .0f}\n')
#        text_file.write(f'Final: {final: .0f}\n')
#        text_file.write(f'Total score: {total: .0f}\n')
#        text_file.write(f'Average score: {average: .2f}\tLetter grade: ' + letter + '\n')
#        text_file.close()
    
#def readFile():
#    try:
#        infile = open('exercise7.txt', 'r')

#    except FileNotFoundError:
#        print('The file was not found.')
#    else:
#        line = infile.readline()

#        while line != '':
#            print(line)
#            line = infile.readline()
#    finally:
#        print('File has been read.')
#        infile.close()

#main()

# Exercise 8
import random

def main():
    writeFile()
    readFile()

def writeFile():
    endpoint = int(input('Enter how many numbers to generate: '))
    write_file = open('exercise8.txt', 'a')

    write_file.write('Number Generator\n')

    for count in range(0, endpoint):
        num = random.randint(1, 10)
        write_file.write(f'{num: .0f}\n')

    write_file.close()

def readFile():
    try:
        infile = open('exercise8.txt', 'r')

    except FileNotFoundError:
        print('The file was not found.')
    else:
        line = infile.readline()

        while line != '':
            print(line)
            line = infile.readline()
    finally:
        print('File has been read.')
        infile.close()

main()