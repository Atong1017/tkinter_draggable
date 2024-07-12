import tkinter as tk
import tkinter.ttk as ttk
from modules import task, json_utils
import os
from src import player


def create_ui_components(parent):

    parent.em_data = json_utils.read_json(os.path.join(parent.data_path, "data"))  # 模擬器相關數據
    eo = parent.em_data["Emulator_options_cn"]  # 選擇語言

    root = parent.window

    components = {}

    comboboxes = [
        ('combobox1', ('歷史筆數', '自訂組數', 'Top', '號碼-+', '交集'), 10, 10, 80, 20, '歷史筆數'),
        ('combobox2', ('1', '2', '3', '4'), 341, 70, 50, 20, ''),
    ]
    components.update({})
    for combobox_name, values, x_combobox, y_combobox, width, height, current_value in comboboxes:
        components[combobox_name] = ttk.Combobox(root, values=values)
        components[combobox_name].place(x=x_combobox, y=y_combobox, width=width, height=height)
        components[combobox_name].set(current_value)


    return components, parent.em_data

