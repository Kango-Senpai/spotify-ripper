import requests
client_id = "82b4d6095dd84d3ba9d6402a72e5c896"
client_secret = "ac3cf13fd3ec42cd8c3478450b7e85c3"

header = {"Content-Type":"application/x-www-form-urlencoded"}

payload = {
    "grant_type":"client_credentials",
    "client_id":client_id,
    "client_secret":client_secret
}
token_endpoint_url = "https://accounts.spotify.com/api/token"

def request_token():
    r = requests.post(token_endpoint_url,headers=header,data=payload)
    if r.ok:
        return r.json()['access_token']
    else:
        print(f"{r.status_code}:{r.reason}")
        return None
        
def spit_token():
    token_file = open("token","w")
    token_file.writelines(request_token())
    token_file.close()

def get_token():
    token = None
    try:
        token_file = open("token","r")
        token = token_file.readlines()[0]
        token_file.close()
    except:
        token = request_token()
        with open("token",'w') as f:
            f.write(token)
    return token

def verify_access():
    api_endpoint = "https://api.spotify.com/v1/playlists"

    r = requests.get(api_endpoint, headers={"client_id":client_id,"client_secret":client_secret})

    if r.status_code == 401:
        print("Expired access token. Renewing...")
        spit_token()