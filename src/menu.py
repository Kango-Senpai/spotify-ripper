class Menu_Item:
    def __init__(self, description, func_ptr, target_array):
        self.desc = description
        self.function = func_ptr
        target_array.append(self)