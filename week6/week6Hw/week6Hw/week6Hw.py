# Uriel Renteria
# 3/19/23

# Project 1
#def main():
#    writeFile()

#def writeFile():
#    try:
#        outFile = open('things.txt', 'a')
#    except FileNotFoundError:
#        print('ERROR: file was not found.')
#    else:
#        print('File has been open')
#        outFile.write('Animal: Zebra\n')
#        outFile.write('Fruit: Apples\n')
#        outFile.write('Country: Mexico\n')
#    finally:
#        outFile.close()
#        print('File has been closed.')

#if __name__ == '__main__':
#    main()

# Project 2
#def main():
#    readFile()

#def readFile():
#    try:
#        infile = open('things.txt', 'r')
#    except FileNotFoundError:
#        print('ERROR: file was not found.')
#    else:
#        print('File has been open.\n')
#        line = infile.readline()
#        while line != '':
#            print(line)
#            line = infile.readline()
#    finally:
#        infile.close()
#        print('File has been closed.')

#if __name__ == '__main__':
#    main()

# Project 3
#def main():
#    writeFile()

#def writeFile():
#    try:
#        outFile = open('number_list.txt', 'a')
#    except FileNotFoundError:
#        print('ERROR: file was not found.')
#    else:
#        print('File to generate 1 - 100.\n')
#        for count in range (1, 101):
#            outFile.write(f'{count: .0f}\n')
#    finally:
#        outFile.close()
#        print('File has been closed.')

#if __name__ == '__main__':
#    main()

## Project 4
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry("100x100")
win.title("Project 4")

def calculate():
    total = 0

    try:
        infile = open('numbers.txt', 'r')
    except FileNotFoundError:
        print('ERROR: file was not found.')
    else:
        line = infile.readline()

        while line != '':
            total += int(line)
            line = infile.readline()

    finally:
       infile.close()
       print('File has been closed.')

    messagebox.showinfo('Information', f"Total: {total: .0f}")

def quit():
    messagebox.showinfo('Information', 'Thank you...')
    win.destroy()

btnCalculate = tk.Button(win, text = "calculate", command = calculate).grid(column = 1, row = 50)
btnQuit = tk.Button(win, text = 'quit', command = quit).grid(column = 2, row = 50)

win.mainloop()