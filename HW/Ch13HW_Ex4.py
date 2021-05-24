##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch13_HW
# Due Date: 05.23.21
# ####################################################

import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='Fahrenheit Conversion')

        self.label2 = tkinter.Label(self.middle_frame, text='Enter value in Celsius:')
        self.entry1 = tkinter.Entry(self.middle_frame, width=10)

        self.button1 = tkinter.Button(self.bottom_frame, text='Convert', command=self.display)
        self.button2 = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.label1.pack()

        self.label2.pack(side='left')
        self.entry1.pack(side='left')

        self.button1.pack(side='left')
        self.button2.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def display(self):
        conv = float(self.entry1.get())
        f = (9/5) * conv + 32
        tkinter.messagebox.showinfo('Result', str(conv) + ' degrees Celsius is equal to ' + str(f) + ' degrees Fahrenheit ')


gui = GUI()