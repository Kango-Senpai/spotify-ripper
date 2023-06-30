import eyed3
from string import ascii_lowercase as alphabet
import os
from os.path import exists

def repair_files():
    dir_scan = os.scandir(os.getcwd())
    for entry in dir_scan:
        old_name = entry.name
        new_name = old_name.replace('_'," ")
        if entry.name != new_name and not exists(new_name):
            os.rename(entry.name,new_name)

def get_metadata(file_name):
    metadata = file_name
    metadata = metadata.replace(".mp3","")
    if len(metadata.split('-')) == 2:
        metadata = metadata.split('-')
    elif len(metadata.split('.')) == 2:
        metadata = metadata.split('.')
    else:
        metadata = metadata.split('-')
        metadata.append(metadata[0])
        metadata[0] = "Unknown"
    #cleanse
    metadata[0] = metadata[0].replace('_'," ")
    metadata[1] = metadata[1].replace('_'," ")
    metadata[0] = metadata[0].strip()
    metadata[1] = metadata[1].strip()

    return metadata

def write_metadata(file_name,artist,title):
    try:
        song_file = eyed3.load(file_name)
        if not song_file.tag:
            song_file.initTag()
        song_file.tag.artist = artist
        song_file.tag.title = title
        song_file.tag.save()
        #print(f"Metadata for '{file_name}': \"{title}\" by \"{artist}\".\n")
        return 1
    except Exception as ex:
        print(f"\033[31mBad mp3 \"{file_name}\".\033[37m")
        #print(ex)
        return 0