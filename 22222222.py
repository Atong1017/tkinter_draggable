import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x500')
root.title('Generated Window')

entry1 = tk.Entry(root)
entry1.insert(0, '')
entry1.place(x=50, y=50, width=277, height=141)

root.mainloop()
