import requests

def spotify_main(access_token):
    playlist_ids = []
    print("Enter a spotify playlist or url to download.")
    print("Type '#' when you're done.")
    while True:
        user_input = input("Playlist id or url: ")
        if user_input.strip() == '#':
            break
        if user_input.strip() == '':
            continue
        print(user_input)
        print("https" in user_input)
        if "https" in user_input:
            user_input = parse_url(user_input)
        playlist_ids.append(user_input)
    for playlist_id in playlist_ids:
        print(get_playlist_items(playlist_id, access_token))
    input()
    


def parse_url(playlist_url):
    if "https" not in playlist_url:
        return playlist_url
    #https://open.spotify.com/playlist/6464WxV1gWImrnYQfPnEqO?si=94efac4d66ab445f&pt=124c35ba0096c6f46a9105d2acde533c
    playlist_id = ""
    landmark = "/playlist/"
    index = playlist_url.index(landmark)
    index += len(landmark)
    
    while index < len(playlist_url) and playlist_url[index] != '?':
        playlist_id += playlist_url[index]
        index += 1
    return playlist_id

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
        # print(f"Total items: {total_items}")
        # print(f"Index offset: {index_offset}")
        # print(f"Batch size: {batch_size}")
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
