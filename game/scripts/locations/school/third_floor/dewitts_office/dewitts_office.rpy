label mrs_dewitts_office_dialogue:
    $ player.go_to(L_school_dewittoffice)
    if L_school_dewittoffice.first_visit and not game.timer.is_dark():
        call expression game.dialog_select("dewitts_office_first_visit")
        $ L_school_dewittoffice.visited()

    if player.location.is_here(M_dewitt):
        if M_dewitt.is_state(S_dewitt_office_reward):
            call expression game.dialog_select("dewitts_office_dewitt_office_reward")
            $ persistent.cookie_jar["Dewitt"]["unlocked"] = True
            $ persistent.cookie_jar["Dewitt"]["gallery"]["01_unlocked"] = True

            $ game.timer.tick()
            $ M_dewitt.trigger(T_dewitt_twerk_n_derk)

        elif M_dewitt.is_state(S_dewitt_office_night_visit):
            jump expression game.dialog_select("dewitt_office_dewitt_night_visit")

    elif game.timer.is_dark():
        call expression game.dialog_select("dewitts_office_night_lock")
        $ player.go_to(L_school_floor3)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
