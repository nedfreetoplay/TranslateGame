label dewitt_office_button_dialogue:
    if M_dewitt.is_state([S_dewitt_eve_meet_up, S_dewitt_erik_get_beer, S_dewitt_clean_graffiti]):
        call expression game.dialog_select("dewitt_dialogue_office_dewitt_eve_meet_up")

    elif M_dewitt.is_state(S_dewitt_end) and game.timer.is_dark():
        call expression game.dialog_select("dewitt_dialogue_office_dewitt_end_intro")
        menu:
            "Танцевать.":
                call expression game.dialog_select("dewitt_dialogue_office_dewitt_end_dance")
                jump expression game.dialog_select("dewitt_twerk_loop")
            "Би Джей.":

                call expression game.dialog_select("dewitt_dialogue_office_dewitt_end_bj")
                jump expression game.dialog_select("dewitt_bj_loop")
            "Прямо к делу.":

                jump expression game.dialog_select("dewitt_dialogue_office_dewitt_end_sex")
    else:

        call expression game.dialog_select("dewitt_dialogue_office_intro")
        menu:
            "Частные уроки флейты." if M_dewitt.is_state(S_dewitt_end):
                call expression game.dialog_select("dewitt_dialogue_office_flute_lessons")
            "Ничего.":

                call expression game.dialog_select("dewitt_dialogue_office_leave")
    hide player
    hide dewitt
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
