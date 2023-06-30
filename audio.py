from yt_dlp import YoutubeDL
from requests import get

def audio_download(query:str,directory:str) -> None:
    filename = f"{directory}/{query}.mp3"
    print("Downloading {}".format(filename))
    opts = {
        "format":"bestaudio",
         "noplaylist":True,
        "sleep_interval":0,
        "max_sleep_interval":1,
        "call_home":True,
        "restrictfilenames":"False",
        # "matchtitle":"Official",
        # "rejecttitle":"Live|Music Video",
        # "nooverwrites":True
        #"verbose":"True"
    }
    with YoutubeDL(opts) as ydl:
        if "https://" not in query:
            ydl.extract_info(f"ytsearch5:{query}",download=False)
        else:
            ydl.extract_info(query,download=True)

def futz(artist:str, song:str):
    print("'{} - {}'".format(artist,song))
    opts = {
        "format":"bestaudio",
        "noplaylist":True,
        "sleep_interval":0,
        "max_sleep_interval":1,
        "call_home":True,
        "restrictfilenames":"False",
        "quiet":True,
        "nooverwrites":True,
        "no_warnings":True,
        "outtmpl": f"{artist}-{song}",
        "postprocessors": [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality':'192'
        }]
    }
    with YoutubeDL(opts) as ydl:
        videos = ydl.extract_info(f"ytsearch3:{artist}-{song}",download=False)
        for video in videos['entries']:
            fulltitle = video["fulltitle"]
            if "Official Music Video" not in fulltitle and "Official Video" not in fulltitle and "Directed" not in fulltitle:
                ydl.download(video['webpage_url'])
                return
    print("Match not found for {} - {}".format(artist,song))

