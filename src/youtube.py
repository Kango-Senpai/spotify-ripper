from yt_dlp import YoutubeDL
banned_title_phrases = ["official music video", "music video", "official video", "directed"]

def individual_download(song:tuple) -> None:
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
        "outtmpl": f"{song[0]}-{song[1]}",
        "postprocessors": [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality':'192'
        }]
    }
    class Banned(Exception):pass
    with YoutubeDL(opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch5:{song[0]}-{song[1]}",download=False)
        for video in search_results['entries']:
            try:
                for phrase in banned_title_phrases:
                    if phrase in video["fulltitle"].lower():
                        raise Banned
            except Banned:
                continue
            ydl.download(video["webpage_url"])
            return
            