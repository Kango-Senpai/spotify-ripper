import requests
def get_playlist_items(playlist_id, access_token):
    request_header = {"Authorization":f"Bearer {access_token}"}
    api_request = requests.get(f"https://api.spotify.com/v1/playlists/{playlist_id}",headers=request_header)
    if not api_request.ok:
        print(f"Failed to request playlist data. ({api_request.status_code}) Check your playlist id.")
        return None
    playlist_data = api_request.json()
    
    playlist_length = playlist_data["tracks"]["total"]
    playlist_name = playlist_data["name"]
    playlist_owner = playlist_data["owner"]["display_name"]

    print(f'Fetching data for {playlist_length} songs. "{playlist_name}" created by "{playlist_owner}".')
    # print(playlist_data["tracks"]["items"][1]["track"]["artists"][0]["name"])
    song_data = []
    for item in playlist_data["tracks"]["items"]:
        song_data.append((item["track"]["artists"][0]["name"],item["track"]["name"]))
    input("Done. Press ENTER to continue...")
    return song_data

