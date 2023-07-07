import config
import os
from menu import Menu_Item
from menu import activate_menu
from youtube import song_prompt
from spotify import spotify_main
import spotify
menu_items = []



def init() -> None: #Wrap main in menu class
    spotify.access_token
    if not config.validate_config():
        spotify.access_token = config.set_config()
    else:
        config_obj = config.load_config()
        spotify.access_token = config.request_token(config_obj["spotify_client_id"], config_obj["spotify_client_secret"])
    print("Your spotify access token for this session is '{}'".format(spotify.access_token))
    input("Press ENTER to continue...")

Menu_Item("Main Menu", None, menu_items)
Menu_Item("Download from YouTube individually", song_prompt, menu_items)
Menu_Item("Download full spotify playlist", spotify_main, menu_items)
Menu_Item("Exit", exit , menu_items)#Figure out a cleaner exit method.

if __name__ == "__main__":
    init()
    activate_menu(menu_items)