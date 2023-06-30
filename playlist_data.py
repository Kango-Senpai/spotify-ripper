import credentials
import requests
import os

def get_name(playlist_id):
    api_endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    header = {
        "Authorization":f"Bearer {credentials.get_token()}"
    }
    r = requests.get(api_endpoint, headers=header)
    return r.json()["name"]

def get_total(playlist_id):
    api_endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    header = {
        "Authorization":f"Bearer {credentials.get_token()}",
    }
    r = requests.get(api_endpoint,headers=header)
    total = 51
    if r.ok:
        total = r.json()["total"]
    return total

def get_songs(playlist_id):
    if os.path.exists(f"{playlist_id}.txt"):
        os.remove(f"{playlist_id}.txt")
    total = get_total(playlist_id)
    print(f"Downloading data of {total} songs from playlist '{playlist_id}'.")
    song_list = {}
    for i in range(0,total,50):
        api_endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?limit=50" + f"&offset={i}" + "&fields=items.track.name,items.track.artists.name"
        header = {
            "Authorization":f"Bearer {credentials.get_token()}",
        }
        
        r = requests.get(api_endpoint,headers=header)
        
        if r.ok:
            songs = r.json()['items']
            
            for song in songs:
                track = song['track']
                artist_name = track['artists'][0]['name']
                track_name = track['name']
                with open(f"{playlist_id}.txt","a") as f:
                    search_query = f"{track_name} - {artist_name}"
                    f.write(search_query + "\n")
                    
                if artist_name not in song_list.keys():
                    song_list[artist_name] = [track_name]
                else:
                    song_list[artist_name].append(track_name)
        else:
            print(f"Error occurred while requesting data. \"{r.status_code}:{r.reason}\"")
    return song_list
