import config
from spotify import get_playlist_items
from spotify import parse_url
from menu import Menu_Item
from menu import activate_menu
access_token = ""
menu_items = []

def test_spotify():
    global access_token
    items = get_playlist_items("3AIdkgRsykCUVZeoMc7Pac",access_token)

def parse_test():
    print(parse_url("https://open.spotify.com/playlist/6464WxV1gWImrnYQfPnEqO?si=94efac4d66ab445f&pt=124c35ba0096c6f46a9105d2acde533c"))
    input()

def init(): #Wrap main in menu class
    global access_token
    if not config.validate_config():
        access_token = config.set_config()
    else:
        config_obj = config.load_config()
        access_token = config.request_token(config_obj["spotify_client_id"], config_obj["spotify_client_secret"])
    print("Your access token for this session is '{}'".format(access_token))
    input("Press ENTER to continue...")
    return access_token

Menu_Item("Main Menu",None, menu_items)
Menu_Item("Test spotify", test_spotify, menu_items)
Menu_Item("Exit", exit , menu_items)#Figure out a cleaner exit method.
Menu_Item("Test parse",parse_test, menu_items)
if __name__ == "__main__":
    access_token = init()
    activate_menu(menu_items)