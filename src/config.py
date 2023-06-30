import json
import requests

from misc_utils import clear_screen
def load_config():
    try:
        with open("config.json",'r') as config_file:
            config_obj = json.loads(config_file.read())
            return config_obj
    except:
        config_obj = {}
        return config_obj

def validate_config() -> bool:
    required_keys = ['spotify_client_id','spotify_client_secret']
    config_obj = load_config()
    for key in required_keys:
        if key not in config_obj.keys():
            print("Configuration file blank or invalid.")
            return False
    return True

def set_config() -> str:
    clear_screen()
    client_id = input("Please provide your spotify api client id:")
    clear_screen()
    client_secret = input("Please provide your spotify spi client secret:")
    clear_screen()
    print("Aquiring access token...")

    client_token = request_token(client_id, client_secret)
    if client_token == None:
        print("Token aquisition failed. Please check your configuration.")
        exit()
    
    config_obj = {"spotify_client_id":client_id,"spotify_client_secret":client_secret}
    with open("config.json", 'w') as config_file:
        config_file.writelines(json.dumps(config_obj))
    return client_token

def request_token(id, secret):
     
    api_request = requests.post("https://accounts.spotify.com/api/token",
                                    headers={"Content-Type":"application/x-www-form-urlencoded"},
                                    data={"grant_type":"client_credentials","client_id":id,"client_secret":secret}
                                    )
    if not api_request.ok:
        return None
    else:
        return api_request.json()['access_token']
    
