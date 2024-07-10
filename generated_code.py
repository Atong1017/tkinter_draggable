import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x500')
root.title('Generated Window')

label = tk.Label(root, text='筆數:')
label.place(x=22, y=33, width=37, height=21)

entry2 = tk.Entry(root)
entry2.insert(0, '')
entry2.place(x=78, y=35, width=100, height=20)

label = tk.Label(root, text='種類:')
label.place(x=21, y=66, width=38, height=19)

combobox4 = ttk.Combobox(root, values=('Option 1', 'Option 2', 'Option 3'))
combobox4.place(x=78, y=66)
combobox4.set('Option 1')

button = tk.Button(root, text='計算')
button.place(x=354, y=335, width=100, height=20)

entry6 = tk.Entry(root)
entry6.insert(0, '')
entry6.place(x=20, y=95, width=458, height=228)

root.mainloop()
