import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x500')
root.title('Generated Window')

entries = [
    ('entry1', '', 10, 10, 100, 20),
    ('entry2', '', 10, 40, 100, 20),
]
components = {}
for entry_name, entry_value, x_entry, y_entry, width, height in entries:
    components[entry_name] = tk.Entry(root)
    components[entry_name].insert(0, entry_value)
    components[entry_name].place(x=x_entry, y=y_entry, width=width, height=height)

checkbuttons = [
    ('checkbutton3', 'Check', 10, 70, 100, 20),
    ('checkbutton4', 'Check', 10, 100, 100, 20),
    ('checkbutton5', 'Check', 10, 130, 100, 20),
    ('checkbutton6', '113', 10, 160, 100, 20),
]
components.update({})
for checkbutton_name, text, x_checkbutton, y_checkbutton, width, height in checkbuttons:
    components[checkbutton_name] = tk.Checkbutton(root, text=text, onvalue=1, offvalue=0)
    components[checkbutton_name].place(x=x_checkbutton, y=y_checkbutton, width=width, height=height)

root.mainloop()
