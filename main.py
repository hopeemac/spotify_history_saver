# # save_my_music
# By: Hope McIntyre

from spotify_history_saver import saver


if __name__ == '__main__':
    saver.run_saver()


# Next steps - pagnation, and storing of data
# -- Write to new file? Append to old (risky if issue, though not deleting...)
# Automate requests every 20 min. (0.5*50 = 25 minutes is min amount of data that could turn over)
# Figure out data storage plan (text for now)
