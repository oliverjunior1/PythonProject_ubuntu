# text changed
import tkinter as tk
import tkinter as ttk

root = tk.Tk()

def change():
    label.config(text="Jesus give his own live for love us, sinner's men!")

root.geometry('500x500')
label = tk.Label(root, text='Jesus is the light of the world!')
label.pack()
button = ttk.Button(root, text='Click Here', command=change)
button.pack()
root.mainloop()
