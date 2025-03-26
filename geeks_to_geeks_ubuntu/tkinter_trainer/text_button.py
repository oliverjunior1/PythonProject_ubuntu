import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("500x500")

def change():
    label.config(text="Jesus love we, although we don't deserve... He loves we")

label = tk.Label(root, text="Jesus is the light of the world!")
label.pack()
button = tk.Button(root, text="clik here", command=change)
button.pack()

root.mainloop()