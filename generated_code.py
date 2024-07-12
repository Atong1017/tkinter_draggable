import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x500')
root.title('Generated Window')

entries = [
    ('entry3', '', 69, 10, 100, 20),
    ('entry5', '', 10, 76, 458, 236),
]
components = {}
for entry_name, entry_value, x_entry, y_entry, width, height in entries:
    components[entry_name] = tk.Entry(root)
    components[entry_name].insert(0, entry_value)
    components[entry_name].place(x=x_entry, y=y_entry, width=width, height=height)

comboboxes = [
    ('combobox4', 'Option 1', 130, 40, 100, 20),
]
components.update({})
for combobox_name, current_value, x_combobox, y_combobox, width, height in comboboxes:
    components[combobox_name] = ttk.Combobox(root, values=['Option 1', 'Option 2', 'Option 3'])
    components[combobox_name].place(x=x_combobox, y=y_combobox, width=width, height=height)
    components[combobox_name].set(current_value)

labels = [
    ('label1', '筆數:', 10, 10, 40, 20),
    ('label2', '種類:', 10, 40, 100, 20),
]
components.update({})
for label_name, text, x_label, y_label, width, height in labels:
    components[label_name] = tk.Label(root, text=text)
    components[label_name].place(x=x_label, y=y_label, width=width, height=height)

buttons = [
    ('button6', '計算', 413, 337, 43, 28),
]
components.update({})
for button_name, text, x_button, y_button, width, height in buttons:
    components[button_name] = tk.Button(root, text=text)
    components[button_name].place(x=x_button, y=y_button, width=width, height=height)

root.mainloop()
