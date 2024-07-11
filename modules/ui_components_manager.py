# modules/ui_components_manager.py
from modules.ui_components import DraggableCombobox

class UIComponentsManager:
    def __init__(self, root):
        self.root = root
        self.combobox_list = []

    def add_combobox(self, component_type, current_value):
        initial_position = (50, 50 + 30 * len(self.combobox_list))
        new_combobox = DraggableCombobox(self.root, component_type, initial_position, current_value=current_value)
        self.combobox_list.append(new_combobox)

    def clear_components(self):
        for combobox in self.combobox_list:
            combobox.form.destroy()
        self.combobox_list.clear()

    def load_components(self, ui_config):
        for config in ui_config:
            new_combobox = DraggableCombobox(
                self.root,
                config['type'],
                config['position'],
                config['size'][0],
                config['size'][1],
                config['current_value']
            )
            self.combobox_list.append(new_combobox)
