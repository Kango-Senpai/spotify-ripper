import requests
def get_playlist_items(playlist_id, access_token):
    request_header = {"Authorization":f"Bearer {access_token}"}
    song_data = []
    total_items = 70
    batch_size = 50

    
    api_request = requests.get(f"https://api.spotify.com/v1/playlists/{playlist_id}",headers=request_header)
    if not api_request.ok:
        print(f"Failed to request playlist data. ({api_request.status_code}) Check your playlist id.")
        return None
    playlist_data = api_request.json()
    total_items = playlist_data["tracks"]["total"]
    
    print(f'Fetching data for {total_items} songs from "{playlist_data["name"]}" created by "{playlist_data["owner"]["display_name"]}".')
    
    # while index_offset <= total_items:
    for index_offset in range(0, total_items, batch_size):
        print(f"Total items: {total_items}")
        print(f"Index offset: {index_offset}")
        print(f"Batch size: {batch_size}")
        api_request = requests.get(f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?limit={batch_size}&offset={index_offset}",headers=request_header)
        if not api_request.ok:
            print(f"Failed to request playlist data. ({api_request.status_code}) Check your playlist id.")
            return None
        playlist_data = api_request.json()

        for item in playlist_data["items"]:
            song_data.append((item["track"]["artists"][0]["name"],item["track"]["name"])) #Ugly but can't find a way around that right now
        index_offset += batch_size
    input("Done. Press ENTER to continue...")
    return song_data

