label gym_dialogue:
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ player.go_to(L_school_track)
    if M_roxxy.is_state(S_roxxy_intense_gymercise):
        call expression game.dialog_select("courtyard_roxxy_intense_gymercise")
        $ M_roxxy.trigger(T_roxxy_in_shower)

    elif M_bridget.is_state(S_bridget_intro):
        call expression game.dialog_select("courtyard_bridget_intro")
        $ shower_door_count = 1
        $ Machine.trigger(T_bridget_workout)

    elif player.location.is_here(M_bridget):
        call expression game.dialog_select("courtyard_bridget_training")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
