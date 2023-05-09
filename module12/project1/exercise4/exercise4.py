
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.button1 = tkinter.Button(self.main_window, text='Quote 1',command=self.quote1)
        self.button2 = tkinter.Button(self.main_window,text='Quote 2',command=self.quote2)
        self.button3 = tkinter.Button(self.main_window,text='Quote 3',command=self.quote3)
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

        tkinter.mainloop()

    def quote1(self):
        tkinter.messagebox.showinfo('Quote 1', 
                                    'Your day will be great.')
    def quote2(self):
        tkinter.messagebox.showinfo('Quote 2', 
                                    'You will have a great lunch today.')
    def quote3(self):
        tkinter.messagebox.showinfo('Quote 3', 
                                    'You will finish your work on time today.')

if __name__ == '__main__':
    my_gui = MyGUI()