import tkinter as tk

root = tk.Tk()

def change():
    label.config(text="Jesus gave his life for you!")

root.geometry('500x500')
label = tk.Label(root, text="Jesus is the light of the World!")
label.pack()
button = tk.Button(root, text="Click me", command=change)
button.pack()

root.mainloop()