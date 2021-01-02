import spotipy
from spotipy.oauth2 import SpotifyOAuth


def spotipy_auth():
    scope = 'user-library-read user-read-recently-played'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return sp
