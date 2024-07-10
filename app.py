import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from modules.ui_components import DraggableCombobox
import json


class Application:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Draggable Combobox Example")
        self.resizing = False  # 用於判斷是否處於調整大小狀態

        combobox_name = tk.Label(root, text='表單:')
        combobox_name.place(x=10, y=400)

        self.option_combobox = ttk.Combobox(root, values=('Combobox', 'Entry', 'Label', 'Button'), width=10, height=5)
        self.option_combobox.current(1)
        self.option_combobox.place(x=45, y=401)

        entry_name = tk.Label(root, text='內容:')
        entry_name.place(x=10, y=430)

        self.option_entry = tk.Entry(root)
        self.option_entry.place(x=45, y=430, width=90)

        entry1_name = tk.Label(root, text='檔名:')
        entry1_name.place(x=10, y=460)

        self.option_entry1 = tk.Entry(root)
        self.option_entry1.insert(0, 'generated_code')
        self.option_entry1.place(x=45, y=460, width=90)

        self.add_button = tk.Button(root, text="新增", command=self.add_combobox)
        self.add_button.place(x=360, y=400)

        self.load_button = tk.Button(root, text="加載", command=self.load_ui)
        self.load_button.place(x=430, y=400)

        self.confirm_button = tk.Button(root, text="保存", command=self.save_as_py)
        self.confirm_button.place(x=360, y=450)

        self.save_button = tk.Button(root, text="預存", command=self.save_ui)
        self.save_button.place(x=430, y=450)

        self.combobox_list = []

    def add_combobox(self):
        initial_position = (50, 50 + 30 * len(self.combobox_list))
        oc_get = self.option_combobox.get()
        new_combobox = DraggableCombobox(self.root, oc_get, initial_position, current_value=self.option_entry.get())
        new_combobox.parent = self  # 設置父應用程序以便刪除
        self.combobox_list.append(new_combobox)

    def generate_code(self):
        code = "import tkinter as tk\n"
        code += "from tkinter import ttk\n\n"

        # 設置視窗大小
        root_size = self.root.geometry().split("+")[0]
        code += f"root = tk.Tk()\n"
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()
        code += f"root.geometry('{root_width}x{root_height}')\n"
        code += "root.title('Generated Window')\n\n"

        entries = []
        comboboxes = []
        labels = []
        buttons = []

        # 收集所有组件的信息
        for idx, cb in enumerate(self.combobox_list):
            pos = cb.get_position()
            current_value = cb.get_current_value()
            widget_width, widget_height = cb.get_size()
            component_type = cb.selected_option

            if component_type == 'Entry':
                entries.append((f"entry{idx + 1}", current_value, pos[0], pos[1], widget_width, widget_height))
            elif component_type == 'Combobox':
                values = cb.get_values()
                if current_value not in values:
                    values += (current_value,)
                comboboxes.append(
                    (f"combobox{idx + 1}", values, pos[0], pos[1], widget_width, widget_height, current_value))
            elif component_type == 'Label':
                labels.append((f"label{idx + 1}", current_value, pos[0], pos[1], widget_width, widget_height))
            elif component_type == 'Button':
                buttons.append((f"button{idx + 1}", current_value, pos[0], pos[1], widget_width, widget_height))

        # 生成Entry初始化的程式碼
        if entries:
            code += "entries = [\n"
            for entry in entries:
                code += f"    {entry},\n"
            code += "]\n"
            code += "components = {}\n"
            code += "for entry_name, entry_value, x_entry, y_entry, width, height in entries:\n"
            code += "    components[entry_name] = tk.Entry(root)\n"
            code += "    components[entry_name].insert(0, entry_value)\n"
            code += "    components[entry_name].place(x=x_entry, y=y_entry, width=width, height=height)\n\n"

        # 生成Combobox初始化的程式碼
        if comboboxes:
            code += "comboboxes = [\n"
            for combobox in comboboxes:
                code += f"    {combobox},\n"
            code += "]\n"
            code += "components.update({})\n"
            code += "for combobox_name, values, x_combobox, y_combobox, width, height, current_value in comboboxes:\n"
            code += "    components[combobox_name] = ttk.Combobox(root, values=values)\n"
            code += "    components[combobox_name].place(x=x_combobox, y=y_combobox, width=width, height=height)\n"
            code += "    components[combobox_name].set(current_value)\n\n"

        # 生成Label初始化的程式碼
        if labels:
            code += "labels = [\n"
            for label in labels:
                code += f"    {label},\n"
            code += "]\n"
            code += "components.update({})\n"
            code += "for label_name, text, x_label, y_label, width, height in labels:\n"
            code += "    components[label_name] = tk.Label(root, text=text)\n"
            code += "    components[label_name].place(x=x_label, y=y_label, width=width, height=height)\n\n"

        # 生成Button初始化的程式碼
        if buttons:
            code += "buttons = [\n"
            for button in buttons:
                code += f"    {button},\n"
            code += "]\n"
            code += "components.update({})\n"
            code += "for button_name, text, x_button, y_button, width, height in buttons:\n"
            code += "    components[button_name] = tk.Button(root, text=text)\n"
            code += "    components[button_name].place(x=x_button, y=y_button, width=width, height=height)\n\n"

        code += "root.mainloop()\n"

        return code

    def save_as_py(self):
        code = self.generate_code()
        try:
            with open(f"{self.option_entry1.get()}.py", "w", encoding="utf-8") as f:
                f.write(code)
            messagebox.showinfo("保存成功", f"程式碼已保存為 {self.option_entry1.get()}.py")
        except Exception as e:
            messagebox.showerror("保存失敗", f"保存程式碼時發生錯誤：{str(e)}")

    def save_ui(self):
        ui_config = [cb.get_config() for cb in self.combobox_list]
        try:
            with open(f"{self.option_entry1.get()}.json", "w", encoding="utf-8") as f:
                json.dump(ui_config, f, ensure_ascii=False, indent=4)
            messagebox.showinfo("保存成功", f"UI 配置已保存為 {self.option_entry1.get()}.json")
        except Exception as e:
            messagebox.showerror("保存失敗", f"保存 UI 配置時發生錯誤：{str(e)}")

    def load_ui(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            title="選擇 UI 配置文件"
        )

        if not file_path:
            return  # 如果用戶取消了選擇，則直接返回

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                ui_config = json.load(f)

            # 清空当前控件
            for combobox in self.combobox_list:
                combobox.form.destroy()
                combobox.delete_button.destroy()
            self.combobox_list.clear()

            # 加載新控件
            for config in ui_config:
                new_combobox = DraggableCombobox(
                    self.root,
                    config['type'],
                    config['position'],
                    config['size'][0],
                    config['size'][1],
                    config['current_value']
                )
                new_combobox.parent = self  # 設置父應用程序以便刪除
                self.combobox_list.append(new_combobox)
            messagebox.showinfo("加載成功", "UI 配置已加載")
        except Exception as e:
            messagebox.showerror("加載失敗", f"加載 UI 配置時發生錯誤：{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
