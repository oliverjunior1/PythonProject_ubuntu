import tkinter as tk
import tkinter as ttk

root = tk.Tk()

def change():
    label.config(text='Jesus is the light of the World!')

root.geometry("500x500")
label = tk.Label(root, text="Jesus loves you too much!")
label.pack()
button = ttk.Button(root, text="Click here", command=change)
button.pack()

root.mainloop()