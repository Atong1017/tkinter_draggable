# modules/ui_initializer.py
import tkinter as tk
from tkinter import ttk

class UIInitializer:
    def __init__(self, root):
        self.root = root

    def initialize_ui(self, application):
        self.root.geometry("500x500")
        self.root.title("Draggable Combobox Example")

        tk.Label(self.root, text='表單:').place(x=10, y=400)
        application.option_combobox = ttk.Combobox(self.root, values=('Combobox', 'Entry', 'Label', 'Button'), width=10)
        application.option_combobox.current(1)
        application.option_combobox.place(x=45, y=401)

        tk.Label(self.root, text='內容:').place(x=10, y=430)
        application.option_entry = tk.Entry(self.root)
        application.option_entry.place(x=45, y=430, width=90)

        tk.Label(self.root, text='檔名:').place(x=10, y=460)
        application.option_entry1 = tk.Entry(self.root)
        application.option_entry1.insert(0, 'generated_code')
        application.option_entry1.place(x=45, y=460, width=90)

        tk.Button(self.root, text="新增", command=application.add_combobox).place(x=360, y=400)
        tk.Button(self.root, text="加載", command=application.load_ui).place(x=430, y=400)
        tk.Button(self.root, text="保存", command=application.save_as_py).place(x=360, y=450)
        tk.Button(self.root, text="預存", command=application.save_ui).place(x=430, y=450)
