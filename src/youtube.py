import os
from yt_dlp import YoutubeDL
banned_title_phrases = ["official music video", "music video", "official video", "directed"]

def individual_download(song:tuple) -> None:
    song_str = f"{song[0]}-{song[1]}" if type(song) == type(()) else song
    print(f"Searching YouTube for '{song_str}'...")
    opts = {
        "format":"bestaudio",
        "noplaylist":True,
        "sleep_interval":0,
        "max_sleep_interval":1,
        "call_home":False,
        "restrictfilenames":"False",
        "quiet":True,
        "nooverwrites":True,
        "no_warnings":True,
        "outtmpl": song_str,
        "postprocessors": [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality':'192'
        }]
    }
    class Banned(Exception):pass
    with YoutubeDL(opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch4:{song_str}",download=False)
        for video in search_results['entries']:
            try:
                for phrase in banned_title_phrases:
                    if phrase in video["fulltitle"].lower():
                        raise Banned
            except Banned:
                continue
            ydl.download(video["webpage_url"])
            print("Download complete.")
            return

def song_prompt() -> None:
    user_query = input("Search for audio: ")
    individual_download((user_query))

def playlist_download(playlist_name, queries:list) -> None:
    if not os.path.exists(playlist_name):
        os.mkdir(playlist_name)
    for query in queries:
        individual_download(query)
    os.system(f"mv *.mp3 {playlist_name}/")
    print("Playlist downloaded to ./{}/".format(playlist_name))