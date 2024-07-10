import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x500')
root.title('Generated Window')

label = tk.Label(root, text='311313')
label.place(x=50, y=50, width=100, height=30)

root.mainloop()
