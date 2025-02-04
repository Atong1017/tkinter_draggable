import tkinter as tk
from tkinter import ttk


class DraggableCombobox:
    def __init__(self, parent, selected_option, initial_position=(50, 50), width=100, height=20, current_value=''):
        self.parent = parent
        self.selected_option = selected_option  # 要新增的選單
        self.resizing = False  # 用於判斷是否處於調整大小狀態
        self.start_x = 0
        self.start_y = 0
        self.selected_entry = None  # 選中的選單

        # 建立預設選單
        if self.selected_option == 'Combobox':
            self.form = ttk.Combobox(parent, values=["Option 1", "Option 2", "Option 3"])
            self.form.set(current_value)
        elif self.selected_option == 'Entry':
            self.form = tk.Entry(parent)
            self.form.insert(0, current_value)
        elif self.selected_option == 'Label':
            if current_value == "":
                current_value = 'Label'
            self.form = tk.Label(parent, text=current_value, bg='LightGray')
        elif self.selected_option == 'Button':
            if current_value == "":
                current_value = 'Button'
            self.form = tk.Button(parent, text=current_value)
        elif self.selected_option == 'Checkbutton':
            if current_value == "":
                current_value = 'Check'
            self.check_var = tk.IntVar()
            self.form = tk.Checkbutton(parent, text=current_value, variable=self.check_var, onvalue=1, offvalue=0, bg='LightGray')
            self.check_var.set(1)

        # 選單位置、大小
        self.form.place(x=initial_position[0], y=initial_position[1], width=width, height=height)

        # 建立選單刪除鈕
        self.delete_button = tk.Button(parent, text="X", command=self.delete_selected)
        self.delete_button.place(x=initial_position[0] + width, y=initial_position[1])

        # 選單促發內容
        self.form.bind("<ButtonPress-1>", self.on_press)
        self.form.bind("<B1-Motion>", self.on_motion)
        self.form.bind("<Enter>", self.on_enter)
        self.form.bind("<Leave>", self.on_leave)
        self.form.bind("<Motion>", self.on_resize_motion)

    # 選中的選單
    def select_entry(self, entry):
        self.selected_entry = entry

    # 刪除選中的選單
    def delete_selected(self):
        if self.form:
            self.form.destroy()
            self.delete_button.destroy()
            self.parent.options_list.remove(self)

    def on_press(self, event):
        self.select_entry(self.form)  # 选择控件
        self.start_x = event.x_root
        self.start_y = event.y_root

    def on_motion(self, event):
        if self.resizing:
            self.resize(event)
        else:
            self.drag(event)

    def drag(self, event):
        new_x = self.form.winfo_x() + (event.x_root - self.start_x)
        new_y = self.form.winfo_y() + (event.y_root - self.start_y)
        self.form.place(x=new_x, y=new_y)
        self.delete_button.place(x=new_x + self.form.winfo_width(), y=new_y)
        self.start_x = event.x_root
        self.start_y = event.y_root

    def resize(self, event):
        new_width = self.form.winfo_width() + (event.x_root - self.start_x)
        new_height = self.form.winfo_height() + (event.y_root - self.start_y)
        self.form.place(width=new_width, height=new_height)
        self.start_x = event.x_root
        self.start_y = event.y_root
        self.delete_button.place(x=self.form.winfo_x() + new_width, y=self.form.winfo_y())

    def on_enter(self, event):
        self.form.config(cursor="arrow")

    def on_leave(self, event):
        self.form.config(cursor="")

    def on_resize_motion(self, event):
        widget_width = self.form.winfo_width()
        widget_height = self.form.winfo_height()
        border_width = 3  # 鼠標靠近邊緣時啟用調整大小模式的邊緣寬度

        if (widget_width - border_width <= event.x <= widget_width and
            widget_height - border_width <= event.y <= widget_height):
            self.form.config(cursor="bottom_right_corner")
            self.resizing = True
        else:
            self.form.config(cursor="arrow")
            self.resizing = False

    def get_position(self):
        return self.form.winfo_x(), self.form.winfo_y()

    def get_values(self):
        if self.selected_option == 'Combobox':
            return self.form['values']
        return None

    def get_current_value(self):
        if self.selected_option == 'Combobox':
            return self.form.get()
        elif self.selected_option == 'Entry':
            return self.form.get()
        elif self.selected_option == 'Label':
            return self.form.cget("text")
        elif self.selected_option == 'Button':
            return self.form.cget("text")
        elif self.selected_option == 'Checkbutton':
            return self.form.cget("text")
        return None

    def get_size(self):
        return self.form.winfo_width(), self.form.winfo_height()

    def get_config(self):
        return {
            'type': self.selected_option,
            'position': self.get_position(),
            'size': self.get_size(),
            'current_value': self.get_current_value()
        }
