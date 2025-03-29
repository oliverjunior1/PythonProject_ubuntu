import tkinter as tk
import tkinter as ttk

root = tk.Tk()
root.geometry('600x400')

name_var = tk.StringVar()
passw_var = tk.StringVar()

def submit():
    name = name_var.get()
    password=passw_var.get()

    print('The name is:'+ name)
    print('The password is: '+ password)

name_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))
