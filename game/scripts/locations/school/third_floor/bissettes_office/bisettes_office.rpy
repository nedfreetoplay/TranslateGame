label mrs_bissettes_office_dialogue:
    $ player.go_to(L_school_bissetteoffice)
    if M_bissette.is_set("office first visit") and not game.timer.is_dark():
        call expression game.dialog_select("bissettes_office_first_visit")
        $ M_bissette.set("office first visit", False)

    if player.location.is_here(M_bissette):
        if M_bissette.is_state(S_bissette_office_meetup) and player.location.is_here(M_bissette):
            call expression game.dialog_select("bissettes_office_afternoon_visit")
            $ M_bissette.trigger(T_bissette_roxxy_convince)

    elif game.timer.is_dark():
        call expression game.dialog_select("bissette_office_night_lock")
        $ player.go_to(L_school_floor3)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
