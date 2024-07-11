import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('666x500')
root.title('Generated Window')

comboboxes = [
    ('combobox1', ('Option 1', 'Option 2', 'Option 3', ''), 15, 19, 100, 20, ''),
    ('combobox2', ('Option 1', 'Option 2', 'Option 3', ''), 313, 130, 100, 20, ''),
]
components.update({})
for combobox_name, values, x_combobox, y_combobox, width, height, current_value in comboboxes:
    components[combobox_name] = ttk.Combobox(root, values=values)
    components[combobox_name].place(x=x_combobox, y=y_combobox, width=width, height=height)
    components[combobox_name].set(current_value)

labels = [
    ('label3', '自訂組數:', 50, 110, 100, 20),
    ('label4', '連錯換單:', 50, 140, 100, 20),
    ('label5', '%', 50, 170, 100, 20),
    ('label6', '%', 50, 200, 100, 20),
    ('label7', '歷史筆數', 50, 230, 100, 20),
    ('label8', '下單組數(-+):', 50, 260, 100, 20),
    ('label9', '次後不再下注:', 50, 290, 100, 20),
]
components.update({})
for label_name, text, x_label, y_label, width, height in labels:
    components[label_name] = tk.Label(root, text=text)
    components[label_name].place(x=x_label, y=y_label, width=width, height=height)

root.mainloop()
