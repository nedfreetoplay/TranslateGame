init -3 python:
    time_spent_playing_start = time()
    if persistent.time_spent_playing is None:
        persistent.time_spent_playing = 0

    if persistent.autosave_frequency is None:
        persistent.autosave_frequency = "200"

    if persistent.allow_internet_connections is None:
        persistent.allow_internet_connections = False

    if persistent.autosaving_enabled is None:
        persistent.autosaving_enabled = True

    if persistent.last_game_day is None:
        persistent.last_game_day = 0

    if persistent.display_android_text is None:
        persistent.display_android_text = True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
