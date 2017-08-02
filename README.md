# Spotify User Music History Saver
Use the Spotify API and Spotipy package to save your personal Spotify listening history

## Design
- Regularly requests and saves recent music history (API limit = 50 songs)
- Uses cursor to capture previously uncollected music history
- Designed to be run daily as a Cron job

## Requirements
- Python: 3.5
- Packages: Spotipy
- Spotify Development Authentication Token
