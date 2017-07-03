
# # save_my_music
# By: Hope McIntyre

import spotipy
import spotipy.util as util
from spotipy import oauth2
import os
import sys
import json
import datetime
import time

# Replace Spotify Class with Class that includes Recent History
from spotipy_mod import Spotify_mod
spotipy.Spotify = Spotify_mod

# Import and store Spotify App Credentials from txt file
key = {}
f = open('auth.txt','r')
for line in f.readlines():
    l = line.split()
    key[l[0]+l[1][:-1]] = l[2]

# Create environment var for app credentials
os.environ["SPOTIPY_CLIENT_ID"] = key['ClientID']
os.environ["SPOTIPY_CLIENT_SECRET"]=key['ClientSecret']
os.environ["SPOTIPY_REDIRECT_URI"]='http://localhost/'

# Execute Authentication Request and Retrieve Users Recently Played Music
scope = 'user-library-read user-read-recently-played'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    # print("Usage: %s username" % (sys.argv[0],))
    print("Provide username as sys.argv")
    sys.exit()

token = util.prompt_for_user_token(username, scope)
sp_oauth = oauth2.SpotifyOAuth(key['ClientID'], key['ClientSecret'], 'http://localhost/', \
scope=scope, cache_path=".cache-" + username )

# Loop runs until 11:35pm of the day the script was started
start_time = datetime.datetime.now()
stop_time = start_time.replace(hours=23,minutes=35)
while datetime.datetime.now() < stop_time:

    if token:

        # print(token)
        token_info = sp_oauth.get_cached_token()
        token = token_info['access_token']
        # print(token_info['access_token'])

        sp = spotipy.Spotify(auth=token)

        # Read the last endtime from tracker
        try:
            with open('cursor.txt','r') as f:
                start = f.read()
            # Warning: Submitting 50+ will NOT return a 'cursors' object
            try:
                results = sp.current_user_recently_played(limit=49, after=start)
            except ConnectionError as e:
                print('Caught ConnectionError')
                time.sleep(2*60)
        except FileNotFoundError:
            start = 0
            try:
                results = sp.current_user_recently_played(limit=49)
            except ConnectionError as e:
                print('Caught ConnectionError')
                time.sleep(2*60)

        # print(start)



        # Catch for no new songs in timewindow
        if len(results['items']) == 0:
            print('no new songs')
        else:
            # Write next start time to tracker
            # print(results['cursors']['after'])
            with open('cursor.txt','w') as f:
                f.write(results['cursors']['after'])

            # Store History in Txt File
            filename = './history/HM_spotify_'+str(start)
            print(filename)
            with open(filename,'w') as f:
                json.dump(results, f)

            print(str(len(results['items']))+' new songs saved')

            # Print History
            # for item in results['items']:
            #     print(item['played_at'])
            #     track = item['track']
            #     print(track['name'] + ' - ' + track['artists'][0]['name'])

            # print(results['cursors'])
    else:
        print("Can't get token for", username)

    # Write time/date details to log file
    with open('log.txt','a') as f:
        f.write(str(datetime.datetime.now())+"\t"+str(len(results['items']))+"\n")

    print(str(t*20)+'minutes running')
    time.sleep(20*60)



# Next steps - pagnation, and storing of data
# -- Write to new file? Append to old (risky if issue, though not deleting...)
# Automate requests every 20 min. (0.5*50 = 25 minutes is min amount of data that could turn over)
# Figure out data storage plan (text for now)
