# modules/file_manager.py
import json
from tkinter import filedialog, messagebox


class FileManager:
    def __init__(self, components_manager, filename_entry):
        self.components_manager = components_manager
        self.filename_entry = filename_entry

    def save_as_py(self, code):
        try:
            with open(f"{self.filename_entry.get()}.py", "w", encoding="utf-8") as f:
                f.write(code)
            messagebox.showinfo("保存成功", f"程式碼已保存為 {self.filename_entry.get()}.py")
        except Exception as e:
            messagebox.showerror("保存失敗", f"保存程式碼時發生錯誤：{str(e)}")

    def save_ui(self):
        ui_config = [cb.get_config() for cb in self.components_manager.combobox_list]
        try:
            with open(f"{self.filename_entry.get()}.json", "w", encoding="utf-8") as f:
                json.dump(ui_config, f, ensure_ascii=False, indent=4)
            messagebox.showinfo("保存成功", f"UI 配置已保存為 {self.filename_entry.get()}.json")
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

            self.components_manager.clear_components()
            self.components_manager.load_components(ui_config)
            messagebox.showinfo("加載成功", "UI 配置已加載")
        except Exception as e:
            messagebox.showerror("加載失敗", f"加載 UI 配置時發生錯誤：{str(e)}")
