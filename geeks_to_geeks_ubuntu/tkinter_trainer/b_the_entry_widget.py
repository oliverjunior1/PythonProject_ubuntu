import tkinter as tk
import tkinter as ttk

root = tk.Tk()

root.geometry('500x500')
label = ttk.Label(root, text='Jesus is the light of the World!')
label.pack()
entry = ttk.Entry(root)
entry.pack()
button = ttk.Button(root, text='Send')
button.pack()

root.mainloop()