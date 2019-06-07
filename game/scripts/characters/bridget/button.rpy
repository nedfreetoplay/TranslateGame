label coach_button_dialogue:
    if player.location == L_school_bridgetoffice:
        call expression game.dialog_select("coach_bridget_dialogue_office_intro")

    elif player.location == L_school_track:
        call expression game.dialog_select("coach_bridget_dialogue_courtyard_intro")
    menu:
        "Where do I train?":
            call expression game.dialog_select("coach_bridget_dialogue_training_advice")
        "Nothing.":

            call expression game.dialog_select("coach_bridget_dialogue_leave")
    hide bridget
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
