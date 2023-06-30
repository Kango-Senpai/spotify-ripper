import audio
import os
import playlist_data
#playlists = ['7xwDZxQWIXrknfhiYygsrF','4aCSLFIoWWEdm87HZgEMK5']
#playlists = ['3x78HXhAE19G9E12v8oOjN']
#playlists = ['2KINChKf6hSSaf3dVv4wVA'] #Test
#playlists = ['1OdkzyfKopPrdfhYVN6C7I']
playlists = [str('0cCh79ssqOaKJoqYCgjDFZ')]



def test():
    # songs = ["Styx - Renegade","Imagine Dragons - Demons","Queen - Brighton Rock","Cardi B - WAP"]
    songs = {"Styx":["Renegade","Mr. Roboto"],"Cardi B":["WAP","Up"],"Rage Against the Machine":["Know your enemy","Guerilla radio"]}
    for artist in songs.keys():
        for song in songs[artist]:
            audio.futz(artist,song)
    os.system("mv *.webm test/")

def main():
    for playlist_id in playlists:
        try:
            if not os.path.isdir("./playlist_id/"):
                os.mkdir(playlist_id)
        except:
            print("Directory exists...")
        songs = playlist_data.get_songs(playlist_id)
        for artist in songs.keys():
            for song in songs[artist]:
                audio.futz(artist,song)
        os.system("mv *.mp3 {}/".format(playlist_id))
        
        #Tech debt
        os.system(f"mv {playlist_id} \'{playlist_data.get_name(playlist_id)}\'")
    
#audio.futz("Eminem","Godzilla")
# audio.futz("Rage against the machine","Know your enemy")
main()
