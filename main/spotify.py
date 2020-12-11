import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id= 'd8fabd82cdc748578eca359605393bd9', client_secret= '8a3fd3de594d49e6a2a54ae3b6ca4a6a')



#create spotify objecvt
#spotify:user:1216336460

class User_Music():

    def __init__(self, user):

        self.sp = spotipy.Spotify(auth_manager=auth_manager)

        self.user = user

        self.pl_name = []
        self.pl_id = []
        self.pl_image = []
        self.pl_description = []


        self.playlists = self.sp.user_playlists(self.user, limit=30, offset=0) #'1216336460'

        for i, t in enumerate(self.playlists['items']):
            self.pl_name.append(t['name'])
            self.pl_id.append(t['id'])
            self.pl_image.append(t['images'][0]['url'])
            self.pl_description.append(t['description'])

    def print_playlist (self):

        for i, name in enumerate(self.pl_name):
            id = self.pl_id[i]
            image = self.pl_image[i]
            description = self.pl_description[i]
            print(f"{name}, {id}, {description}, image link {image}")



#test = User_Music('1216336460')

#test.print_playlist()



#print(json.dump(VAR, sort_key=True,indent=4))

#print(json.dumps(playlists, sort_keys=True, indent=4))
#print(insert_playlist())
