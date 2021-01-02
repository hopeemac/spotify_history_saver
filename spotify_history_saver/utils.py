import os
import datetime
import pandas as pd


def get_last_save_time():
    if not os.path.exists('cursor.txt'):
        return None
    with open('cursor.txt', 'r') as f:
        dt_str = f.read()
    return datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S.%f')


def write_last_save_time(current_runtime):
    with open('cursor.txt', 'w') as f:
        f.write(f'{current_runtime}')


def write_to_log(current_runtime, message):
    with open('log.txt', 'a') as f:
        f.write(f'{current_runtime:%Y-%m-%dT%H%M%S}\t{message}\n')


def save_results(results, runtime):
    if len(results['items']) > 0:
        to_save = [(item['played_at'], item['track']['name'], item['track']['artists'][0]['name'])
                   for item in results['items']]
        to_save = pd.DataFrame(to_save, columns=['played_at', 'track', 'artist'])
        # make folder if does not exist
        to_save.to_csv(f'./history/{runtime:%Y-%m-%dT%H%M%S}.tsv', sep='\t')


def datetime_to_spotify_timestamp_format(start):
    if start is None:
        return None
    else:
        return round(start.timestamp() * 1000)  # convert to millisec unix timestamp per API req, no decimal
