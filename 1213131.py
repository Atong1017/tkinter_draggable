import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x500')
root.title('Generated Window')

entry1 = tk.Entry(root)
entry1.insert(0, '')
entry1.place(x=65, y=67, width=144, height=19)

combobox2 = ttk.Combobox(root, values=('Option 1', 'Option 2', 'Option 3', ''))
combobox2.place(x=81, y=279)
combobox2.set('')

root.mainloop()
