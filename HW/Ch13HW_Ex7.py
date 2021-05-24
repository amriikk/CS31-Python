##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch13_HW - Ex.7
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

        self.label1 = tkinter.Label(self.top_frame, text="Rates for telephone calls")
        self.label2 = tkinter.Label(self.top_frame, text="Rate category\t\t\t")
        self.label3 = tkinter.Label(self.top_frame, text="Rate per Minute")

        self.label1.pack()
        self.label2.pack(side='left', anchor='w')
        self.label3.pack(side='left', anchor='e')

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.middle_frame, text='Daytime(6:00am-5:59pm)\t\t\t$0.07', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.middle_frame, text='Evening(6:00pm-11:59pm)\t\t\t$0.12', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.middle_frame, text='Off-Peak(12:00am-5:59am)\t\t\t$0.05', variable=self.radio_var, value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.label4 = tkinter.Label(self.middle_frame, text='Enter Minutes:')
        self.entry1 = tkinter.Entry(self.middle_frame, width=10)

        self.label4.pack(side='left')
        self.entry1.pack(side='left')

        self.button1 = tkinter.Button(self.bottom_frame, text='Total', command=self.total)
        self.button2 = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.button1.pack(side='left')
        self.button2.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def total(self):
        t = int(self.entry1.get())
        if self.radio_var.get() == 1:
            total = t * 0.07
        elif self.radio_var.get() == 2:
            total = t * 0.12
        else:
            total = t * 0.05
        tkinter.messagebox.showinfo('Rate', f'Total: ${total:.2f}')

gui = GUI()