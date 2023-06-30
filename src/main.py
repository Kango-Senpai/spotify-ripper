import config
def main():
    access_token = ""
    if not config.validate_config():
        access_token = config.set_config()
    else:
        config_obj = config.load_config()
        access_token = config.request_token(config_obj["spotify_client_id"], config_obj["spotify_client_secret"])
    print("Your access token for this session is '{}'".format(access_token))

    
if __name__ == "__main__":
    main()

