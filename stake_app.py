import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('667x500')
root.title('Generated Window')

entries = [
    ('entry20', '14, 15, 29, 34, 20', 180, 10, 100, 20),
    ('entry21', '2', 418, 40, 27, 19),
    ('entry22', '3', 418, 10, 24, 18),
    ('entry23', '20', 478, 10, 27, 24),
    ('entry24', '200', 72, 40, 41, 24),
    ('entry25', '7', 192, 40, 19, 21),
    ('entry26', '', 232, 40, 37, 20),
    ('entry27', '20', 478, 40, 25, 22),
    ('entry28', '', 72, 70, 72, 20),
    ('entry29', '0.1', 182, 70, 57, 25),
    ('entry30', '1', 462, 70, 21, 19),
    ('entry31', '100', 512, 70, 32, 22),
    ('entry32', '11', 10, 100, 31, 21),
    ('entry33', '3', 110, 100, 25, 23),
    ('entry34', '0', 235, 100, 23, 26),
    ('entry35', '50', 325, 100, 24, 21),
    ('entry36', '19', 390, 100, 21, 18),
    ('entry37', '24', 455, 100, 28, 19),
]
components = {}
for entry_name, entry_value, x_entry, y_entry, width, height in entries:
    components[entry_name] = tk.Entry(root)
    components[entry_name].insert(0, entry_value)
    components[entry_name].place(x=x_entry, y=y_entry, width=width, height=height)

comboboxes = [
    ('combobox1', ('歷史筆數', '自訂組數', 'Top', '號碼-+', '交集'), 10, 10, 80, 20, '歷史筆數'),
    ('combobox2', ('1', '2', '3', '4'), 341, 70, 50, 20, ''),
]
components.update({})
for combobox_name, values, x_combobox, y_combobox, width, height, current_value in comboboxes:
    components[combobox_name] = ttk.Combobox(root, values=values)
    components[combobox_name].place(x=x_combobox, y=y_combobox, width=width, height=height)
    components[combobox_name].set(current_value)

labels = [
    ('label3', '自訂組數:', 180, 10, 55, 20),
    ('label4', '連錯換單:', 358, 10, 53, 22),
    ('label5', '%', 508, 10, 22, 23),
    ('label6', '%', 508, 40, 20, 19),
    ('label7', '歷史筆數', 10, 40, 54, 21),
    ('label8', '下單組數(-+):', 110, 40, 75, 25),
    ('label9', '次後不再下注:', 268, 40, 81, 22),
    ('label10', '二次換單:', 358, 40, 55, 20),
    ('label11', '起始金額:', 10, 70, 56, 19),
    ('label12', '每單籌碼:', 123, 70, 59, 18),
    ('label13', '模擬器:', 278, 70, 46, 20),
    ('label14', '更新排名:', 400, 70, 54, 20),
    ('label15', '內無則扣除:', 40, 100, 65, 24),
    ('label16', '第二次無則扣除:', 140, 100, 89, 21),
    ('label17', '上升獲利:', 265, 100, 52, 20),
    ('label18', '往前:', 355, 100, 33, 20),
    ('label19', '往後:', 420, 100, 36, 20),
]
components.update({})
for label_name, text, x_label, y_label, width, height in labels:
    components[label_name] = tk.Label(root, text=text)
    components[label_name].place(x=x_label, y=y_label, width=width, height=height)

buttons = [
    ('button38', '新增任務', 548, 10, 56, 23),
    ('button39', '刪除任務', 548, 40, 55, 19),
    ('button40', '更新任務', 548, 70, 58, 21),
    ('button41', '關閉adb', 548, 100, 55, 20),
    ('button42', '測試', 618, 10, 33, 24),
    ('button43', '執行', 618, 100, 36, 23),
]
components.update({})
for button_name, text, x_button, y_button, width, height in buttons:
    components[button_name] = tk.Button(root, text=text)
    components[button_name].place(x=x_button, y=y_button)

root.mainloop()
