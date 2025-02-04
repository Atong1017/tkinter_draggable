import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from modules.ui_components import DraggableCombobox
from code_generator.generator import CodeGenerator
import re


class Application:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Draggable Combobox Example")
        self.resizing = False  # 用於判斷是否處於調整大小狀態

        options_name = tk.Label(root, text='表單:')
        options_name.place(x=10, y=400)

        self.option_combobox = ttk.Combobox(root, values=('Combobox', 'Entry', 'Label', 'Button', 'Checkbutton'), width=10, height=5)
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

        self.add_button = tk.Button(root, text="新增", command=self.add_options)
        self.add_button.place(x=350, y=450)

        self.edit_button = tk.Button(root, text="編輯", command=self.edit_py)
        self.edit_button.place(x=400, y=450)

        self.save_button = tk.Button(root, text="保存", command=self.save_as_py)
        self.save_button.place(x=450, y=450)

        self.options_list = []

    def add_options(self):
        list_count = len(self.options_list) // 10  # 每10個後換行
        list_mode = len(self.options_list) % 10  # 10個內往下新增列
        add_x = 10 + 120 * list_count
        add_y = 10 + 30 * list_mode

        initial_position = (add_x, add_y)
        oc_get = self.option_combobox.get()
        new_options = DraggableCombobox(self.root, oc_get, initial_position, current_value=self.option_entry.get())
        new_options.parent = self  # 設置父應用程式以便刪除
        self.options_list.append(new_options)

    #
    def py_to_dict(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            a = f.read()

        all_info = []

        # 使用規則運算式匹配 entries 列表
        for es in ['entries', 'comboboxes', 'labels', 'buttons', 'checkbuttons']:
            entries_pattern = re.compile(fr"{es}\s*=\s*\[([^\]]+)\]", re.DOTALL)
            matches = entries_pattern.search(a)

            if matches:
                entries_string = matches.group(1).strip()
                # 解析 entries 字串為 Python 物件
                entries = eval(f"[{entries_string}]")

                for e in entries:
                    if es == 'entries':
                        type = "Entry"
                    elif es == 'comboboxes':
                        type = 'Combobox'
                    elif es == 'labels':
                        type = 'Label'
                    elif es == 'buttons':
                        type = 'Button'
                    elif es == 'checkbuttons':
                        type = 'Checkbutton'

                    a_dict = {
                        "type": type,
                        "position": [e[2], e[3]],
                        "size": [e[4], e[5]],
                        "current_value": e[1]
                    }

                    all_info.append(a_dict)
            else:
                print("No entries found")

        return all_info

    def save_as_py(self):
        generator = CodeGenerator(self.options_list, self.root)
        code = generator.generate_code()
        try:
            with open(f"{self.option_entry1.get()}.py", "w", encoding="utf-8") as f:
                f.write(code)
            messagebox.showinfo("保存成功", f"程式碼已保存為 {self.option_entry1.get()}.py")
        except Exception as e:
            messagebox.showerror("保存失敗", f"保存程式碼時發生錯誤：{str(e)}")

    def edit_py(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.py"), ("All files", "*.*")],
            title="選擇 UI 設定檔"
        )

        if not file_path:
            return  # 如果用戶取消了選擇，則直接返回

        try:
            ui_config = self.py_to_dict(file_path)

            # 清空當前控制項
            for option in self.options_list:
                option.form.destroy()
                option.delete_button.destroy()
            self.options_list.clear()

            # 加載新控制項
            for config in ui_config:
                new_option = DraggableCombobox(
                    self.root,
                    config['type'],
                    config['position'],
                    config['size'][0],
                    config['size'][1],
                    config['current_value']
                )
                new_option.parent = self  # 設置父應用程式以便刪除
                self.options_list.append(new_option)
            messagebox.showinfo("加載成功", "UI 配置已加載")
        except Exception as e:
            messagebox.showerror("加載失敗", f"加載 UI 配置時發生錯誤：{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
