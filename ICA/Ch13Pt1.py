# Week 15, ICA 1
import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='John Trujillo')
        self.label2 = tkinter.Label(self.bottom_frame, text='LBCC')
        self.label3 = tkinter.Label(self.bottom_frame, text='Engineering')

        self.label1.pack() # default top side
        self.label2.pack(side='left')
        self.label3.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

gui = GUI()