import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SPOTIFY_ID = os.environ['SPOTIFY_ID']
SPOTIFY_SECRET = os.environ['SPOTIFY_SECRET']

auth_manager = SpotifyClientCredentials(client_id= SPOTIFY_ID, client_secret= SPOTIFY_SECRET)



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
