label stairs_dialogue:
    $ player.go_to(L_school_floor2)
    call pa_announcement
    if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg") and not game.timer.is_dark():
        $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)

    if not L_school_floor2.is_visited:
        call expression game.dialog_select("second_floor_first_visit")
        $ L_school_floor2.visited()
        $ L_gym_front.unlock()

    elif M_okita.is_state(S_okita_dose_smith):
        call expression game.dialog_select("second_floor_okita_dose_smith")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
