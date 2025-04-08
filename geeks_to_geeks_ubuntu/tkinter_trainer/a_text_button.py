import tkinter as tk
import tkinter as ttk

root = tk.Tk()
def text():
    label.config(text='Jesus is the light of the World!')

root.geometry('800x800')

label = tk.Label(root, text="Jesus walk on the water, teach us how to have faith!")
label.pack()
button = ttk.Button(root, text="click here", command=text)
button.pack()

root.mainloop()