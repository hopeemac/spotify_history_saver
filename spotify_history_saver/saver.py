import time
import datetime

from spotify_history_saver import auth, utils


def run_saver():
    sp = auth.spotipy_auth()

    # Loop runs until 11:35pm of the day the script was started
    stop_time = datetime.datetime.now().replace(hour=23, minute=35)

    while datetime.datetime.now() < stop_time:
        current_runtime = datetime.datetime.now()
        last_runtime = utils.get_last_save_time()

        try:
            results = sp.current_user_recently_played(limit=49, after=utils.datetime_to_spotify_timestamp_format(last_runtime))
            utils.save_results(results, current_runtime)
            log_message = f"{len(results['items'])} results"
            utils.write_last_save_time(current_runtime)
        except ConnectionError:
            log_message = 'Caught ConnectionError'

        utils.write_to_log(current_runtime, log_message)
        time.sleep(60 * 20)
