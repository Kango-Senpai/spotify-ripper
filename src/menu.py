class Menu_Item:
    def __init__(self, description, func_ptr):
        self.desc = description
        self.function = func_ptr
        menu_items.append(self)