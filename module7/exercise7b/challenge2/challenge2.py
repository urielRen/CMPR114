# Uriel Renteria
# 3/27/23

# Challenge 2
from tkinter import *

top = Tk()

listbox = Listbox(top, height=10, 
                  width=15, bg = 'gray',
                  activestyle = 'dotbox',
                  font = 'Helvita',
                  fg = 'yellow',
                  selectmode=MULTIPLE)

top.geometry('300x250')

label = Label(top, text = 'FOOD ITEMS')

listbox.insert(1, 'Sandwhich')
listbox.insert(2, 'Burger')
listbox.insert(3, 'Pizza')
listbox.insert(4, 'French Fries')
listbox.insert(5, 'Hot Dogs')
listbox.insert(6, 'CheeseBurger')

def selected_item():
    for i in listbox.curselection():
        print(listbox.get(i))

btn = Button(top, text='Print Selected', command=selected_item)

btn.pack(side='bottom')

label.pack()
listbox.pack()

top.mainloop()
