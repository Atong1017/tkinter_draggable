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

        # self.delete_button = tk.Button(root, text="X", command=DraggableCombobox.delete_selected)
        # self.delete_button.place(x=150, y=0)

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
        root_width = root.winfo_width()
        root_height = root.winfo_height()
        code += f"root.geometry('{root_width}x{root_height}')\n"
        code += "root.title('Generated Window')\n\n"

        # 生成Combobox初始化的程式碼
        for idx, cb in enumerate(self.combobox_list):
            pos = cb.get_position()
            current_value = cb.get_current_value()
            values = cb.get_values()
            widget_width = cb.form.winfo_width()
            widget_height = cb.form.winfo_height()

            if 'entry' in str(cb.form):
                code += f"entry{idx+1} = tk.Entry(root)\n"
                code += f"entry{idx + 1}.insert(0, '{current_value}')\n"
                code += f"entry{idx+1}.place(x={pos[0]}, y={pos[1]}, width={widget_width}, height={widget_height})\n\n"

            elif 'combobox' in str(cb.form):
                if current_value not in values:
                    values += (current_value, )
                code += f"combobox{idx+1} = ttk.Combobox(root, values={values})\n"
                code += f"combobox{idx+1}.place(x={pos[0]}, y={pos[1]})\n"
                code += f"combobox{idx+1}.set('{current_value}')\n\n"

            elif 'label' in str(cb.form):
                code += f"label = tk.Label(root, text='{current_value}')\n"
                code += f"label.place(x={pos[0]}, y={pos[1]}, width={widget_width}, height={widget_height})\n\n"

            elif 'button' in str(cb.form):
                code += f"button = tk.Button(root, text='{current_value}')\n"
                code += f"button.place(x={pos[0]}, y={pos[1]}, width={widget_width}, height={widget_height})\n\n"

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
            print(e)
            # messagebox.showerror("加載失敗", f"加載 UI 配置時發生錯誤：{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
