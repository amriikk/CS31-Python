##################################################### 
# CS 31, Prof. Muldrow
# Name: Jhon Trujillo
# Assignment: Ch13_HW - Ex.6
# Due Date: 05.23.21
# ####################################################

import tkinter

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.total_Frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text="Joe's Automotive")
        self.label2 = tkinter.Label(self.top_frame, text="Service\t\t\t")
        self.label3 = tkinter.Label(self.top_frame, text="Price")

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        self.cb1 = tkinter.Checkbutton(self.middle_frame, text='Oil Change' + '\t\t\t$30.00', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.middle_frame, text='Lube job' + '\t\t\t\t$20.00', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.middle_frame, text='Radiator flush' + '\t\t\t$40.00', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.middle_frame, text='Transmission flush ' + '\t\t$100.00', variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.middle_frame, text='Inspection' + '\t\t\t$35.00', variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.middle_frame, text='Muffler replacement' + '\t\t$200.00', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.middle_frame, text='Tire rotation' + '\t\t\t$20.00', variable=self.cb_var7)
        self.label4 = tkinter.Label(self.total_Frame, text='Total:')
        self.total_val = tkinter.StringVar()
        self.label5 = tkinter.Label(self.total_Frame, textvariable=self.total_val)

        self.button1 = tkinter.Button(self.bottom_frame, text='Total', command=self.total)
        self.button2 = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.label4.pack(side='left')
        self.label5.pack(side='left')

        self.label1.pack()
        self.label2.pack(side='left', anchor='w')
        self.label3.pack(side='left', anchor='e')

        self.cb1.pack(anchor='w')
        self.cb2.pack(anchor='w')
        self.cb3.pack(anchor='w')
        self.cb4.pack(anchor='w')
        self.cb5.pack(anchor='w')
        self.cb6.pack(anchor='w')
        self.cb7.pack(anchor='w')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.total_Frame.pack()
        self.bottom_frame.pack()

        self.button1.pack(side='left')
        self.button2.pack(side='left')

        tkinter.mainloop()

    def total(self):
        self.t = 0.00
        if self.cb_var1.get() == 1:
            self.t += 30.00
        if self.cb_var2.get() == 1:
            self.t += 20.00
        if self.cb_var3.get() == 1:
            self.t += 40.00
        if self.cb_var4.get() == 1:
            self.t += 100.00
        if self.cb_var5.get() == 1:
            self.t += 35.00
        if self.cb_var6.get() == 1:
            self.t += 200.00
        if self.cb_var7.get() == 1:
            self.t += 20.00
        self.total_val.set(self.t)

gui = GUI()