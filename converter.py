
# Convert Spotify API jsons to CSV-lite
# Hope McIntyre

import sys, os
import json

# Read txt with converted files
try:
    with open('converted.txt','r') as f:
        old_files = f.read().splitlines()
        # print(old_files)
except FileNotFoundError:
    open('converted.txt','w').close()
    old_files = []

# Get list of files in folder
all_files = os.listdir('./history')
# print(all_files)

# Get list of new files
new_files = [file for file in all_files if file not in old_files]

# For each file
# Read file, extract song name, artist name, date time
for file in new_files:
    print(file)

    with open('history/'+file,'r') as j:
        data = json.load(j)

    histfile = open('simple_hist.tsv','a')
    for item in data['items']:
        # print(item['played_at'])
        track = item['track']
        # print(track['name'] + ' - ' + track['artists'][0]['name'])
        newline = track['name']+"\t"+track['artists'][0]['name']+"\t"+item['played_at']+"\n"
        histfile.write(newline)
    histfile.close()

    with open('converted.txt','a') as c:
        c.write(file+'\n')
