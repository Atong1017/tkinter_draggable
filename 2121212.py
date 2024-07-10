import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x500')
root.title('Generated Window')

entry1 = tk.Entry(root)
entry1.insert(0, '')
entry1.place(x=50, y=50, width=299, height=118)

combobox2 = ttk.Combobox(root, values=('Option 1', 'Option 2', 'Option 3', ''))
combobox2.place(x=106, y=208)
combobox2.set('')

label = tk.Label(root, text='這是一個標籤')
label.place(x=49, y=306, width=100, height=30)

button = tk.Button(root, text='按鈕')
button.place(x=252, y=298, width=100, height=30)

root.mainloop()
