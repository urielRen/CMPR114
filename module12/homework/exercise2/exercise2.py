# Uriel Renteria
# 5/8/23

import tkinter

class TestAVG:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.test4_frame = tkinter.Frame(self.main_window)
        self.test5_frame = tkinter.Frame(self.main_window)
        
        self.sum_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.test1_label = tkinter.Label(self.test1_frame,
                                         text='Enter the score for test 1:')
        self.test1_entry = tkinter.Entry(self.test1_frame,width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        self.test2_label = tkinter.Label(self.test2_frame,
                                         text='Enter the score for test 2:')
        self.test2_entry = tkinter.Entry(self.test2_frame,
                                         width=10)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')

        self.test3_label = tkinter.Label(self.test3_frame, 
                                         text='Enter the score for test 3:')
        self.test3_entry = tkinter.Entry(self.test3_frame,
                                         width=10)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        self.test4_label = tkinter.Label(self.test4_frame, 
                                         text='Enter the score for test 4:')
        self.test4_entry = tkinter.Entry(self.test4_frame,
                                         width=10)
        self.test4_label.pack(side='left')
        self.test4_entry.pack(side='left')

        self.test5_label = tkinter.Label(self.test5_frame, 
                                         text='Enter the score for test 5:')
        self.test5_entry = tkinter.Entry(self.test5_frame,
                                         width=10)
        self.test5_label.pack(side='left')
        self.test5_entry.pack(side='left')

        self.result1_label = tkinter.Label(self.sum_frame, text='Sum:')
        self.sum = tkinter.StringVar()
        self.sum_label = tkinter.Label(self.sum_frame, textvariable= self.sum)
        self.result1_label.pack(side='left')
        self.sum_label.pack(side='left')

        self.result2_label = tkinter.Label(self.avg_frame,text='Average:')
        self.avg = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.avg_frame,textvariable=self.avg)
        self.result2_label.pack(side='left')
        self.avg_label.pack(side='left')

        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Calculate',
                                          command=self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.test4_frame.pack()
        self.test5_frame.pack()
        self.sum_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def calc_avg(self):
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())
        self.test4 = float(self.test4_entry.get())
        self.test5 = float(self.test5_entry.get())

        self.add = self.test1 + self.test2 + self.test3 + self.test4 + self.test5

        self.sum.set(self.add)

        self.average = self.add / 5.0

        self.avg.set(self.average)

if __name__ == '__main__':
    test_avg = TestAVG()
