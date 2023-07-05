from misc_utils import clear_screen
class Menu_Item:
    def __init__(self, description, func_ptr, target_array):
        self.desc = description
        self.function = func_ptr
        target_array.append(self)

def activate_menu(menu_array):
    while True:
        clear_screen()
        for i in range(0,len(menu_array)):
            print(f"{i}. {menu_array[i].desc}")
        user_input = input("Selection: ")
        try:
            user_input = int(user_input)
        except:
            print("Selection must be a number!")
            input("Press ENTER to continue")
            continue
        if user_input >= 1 and user_input <= len(menu_array):
            menu_array[user_input].function()
        else:
            print("Invalid selection!")
            input("Press ENTER to continue")
            continue