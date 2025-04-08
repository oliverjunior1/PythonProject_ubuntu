from tkinter import *
from tkinter.ttk import *

master = Tk()

p1 = PhotoImage(file='bat.svg')
master.iconphoto(False, p1)
b = Button(master, text='Click me')
b.pack(side=TOP)
mainloop()