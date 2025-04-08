from tkinter import *
from tkinter.ttk import *

root =Tk()
p1 = PhotoImage(file='Untitled.jpeg')
root.iconphoto(False, p1)
b = Button(root, text='Click me!')
b.pack(side=TOP)
mainloop()