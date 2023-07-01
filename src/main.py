import config
from misc_utils import clear_screen

menu_items = []

class Menu_Item:
    def __init__(self, description, func_ptr):
        self.desc = description
        self.function = func_ptr
        menu_items.append(self)

def init(): #Wrap main in menu class
    access_token = ""
    if not config.validate_config():
        access_token = config.set_config()
    else:
        config_obj = config.load_config()
        access_token = config.request_token(config_obj["spotify_client_id"], config_obj["spotify_client_secret"])
    print("Your access token for this session is '{}'".format(access_token))
    input("Press ENTER to continue...")

def main():
    init()
    while True:
        clear_screen()
        for i in range(0,len(menu_items)):
            print(f"{i}. {menu_items[i].desc}")
        user_input = input("Selection: ")
        try:
            user_input = int(user_input)
        except:
            print("Selection must be a number!")
            input("Press ENTER to continue")
            continue
        try:
            menu_items[user_input].function()
        except:
            print("Invalid selection!")
            input("Press ENTER to continue")
            continue


Menu_Item("Main Menu",None)

if __name__ == "__main__":
    main()