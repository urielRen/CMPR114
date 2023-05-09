import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.lastName = tkinter.Label(self.main_window, text = 'Renteria')
        self.firstName = tkinter.Label(self.main_window, text = 'Uriel')
        self.age = tkinter.Label(self.main_window, text = '28')

        self.lastName.pack()
        self.firstName.pack()
        self.age.pack()

        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()

