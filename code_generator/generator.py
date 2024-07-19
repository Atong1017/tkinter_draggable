# code_generator/generator.py
class CodeGenerator:
    def __init__(self, combobox_list, root):
        self.combobox_list = combobox_list
        self.root = root

    def generate_code(self):
        code = "import tkinter as tk\n"
        code += "from tkinter import ttk\n\n"

        # 設置視窗大小
        root_size = self.root.geometry().split("+")[0]
        code += f"root = tk.Tk()\n"
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()
        code += f"root.geometry('{root_width}x{root_height - 98}')\n"
        code += "root.title('Generated Window')\n\n"

        entries = []
        comboboxes = []
        labels = []
        buttons = []
        checkbuttons = []

        # 收集所有组件的信息
        for idx, cb in enumerate(self.combobox_list):
            pos = cb.get_position()
            current_value = cb.get_current_value()
            widget_width, widget_height = cb.get_size()
            component_type = cb.selected_option
            values = cb.get_values()

            if component_type == 'Entry':
                entries.append((f"entry{idx + 1}", current_value, pos[0], pos[1], widget_width, widget_height))
            elif component_type == 'Combobox':
                comboboxes.append((f"combobox{idx + 1}", current_value, pos[0], pos[1], widget_width, widget_height))
            elif component_type == 'Label':
                labels.append((f"label{idx + 1}", current_value, pos[0], pos[1], widget_width, widget_height))
            elif component_type == 'Button':
                buttons.append((f"button{idx + 1}", current_value, pos[0], pos[1], widget_width, widget_height))
            elif component_type == 'Checkbutton':
                checkbuttons.append((f"checkbutton{idx + 1}", current_value, pos[0], pos[1], widget_width, widget_height))

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
            code += "for combobox_name, current_value, x_combobox, y_combobox, width, height in comboboxes:\n"
            code += "    components[combobox_name] = ttk.Combobox(root, values=['Option 1', 'Option 2', 'Option 3'])\n"
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

        if checkbuttons:
            code += "checkbuttons = [\n"
            for checkbutton in checkbuttons:
                code += f"    {checkbutton},\n"
            code += "]\n"
            code += "components.update({})\n"
            code += "for checkbutton_name, text, x_checkbutton, y_checkbutton, width, height in checkbuttons:\n"
            code += "    components[checkbutton_name] = tk.Checkbutton(root, text=text, onvalue=1, offvalue=0)\n"
            code += "    components[checkbutton_name].place(x=x_checkbutton, y=y_checkbutton, width=width, height=height)\n"
            code += "    # 預設值參數代入方式\n"
            code += "    # var = tk.IntVar()\n"
            code += "    # components[checkbutton_name] = tk.Checkbutton(root, text=text, variable=var, onvalue=1, offvalue=0)\n"
            code += "    # var.set(1)  1:勾選\n\n"

        code += "root.mainloop()\n"

        return code
