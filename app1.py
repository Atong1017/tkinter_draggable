# main.py
import tkinter as tk
from modules.ui_initializer import UIInitializer
from modules.ui_components_manager import UIComponentsManager
from modules.file_manager import FileManager
from code_generator.generator import CodeGenerator

class Application:
    def __init__(self, root):
        self.root = root

        self.ui_initializer = UIInitializer(root)
        self.ui_initializer.initialize_ui(self)

        self.components_manager = UIComponentsManager(root)
        self.file_manager = FileManager(self.components_manager, self.option_entry1)

    def add_combobox(self):
        component_type = self.option_combobox.get()
        current_value = self.option_entry.get()
        self.components_manager.add_combobox(component_type, current_value)

    def save_as_py(self):
        generator = CodeGenerator(self.components_manager.combobox_list, self.root)
        code = generator.generate_code()
        self.file_manager.save_as_py(code)

    def save_ui(self):
        self.file_manager.save_ui()

    def load_ui(self):
        self.file_manager.load_ui()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
