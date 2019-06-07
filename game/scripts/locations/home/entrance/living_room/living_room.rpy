label home_livingroom_dialogue:
    $ player.go_to(L_home_livingroom)
    if M_mom.is_state(S_mom_spy) and not game.timer.is_dark():
        call expression game.dialog_select("living_room_mom_spy")

    elif M_diane.is_state(S_diane_peeking) and game.timer.is_evening():
        call expression game.dialog_select("living_room_diane_peeking")
        $ M_diane.trigger(T_diane_gotta_jack_it)
        $ player.go_to(L_home_bedroom)
        $ game.lock_ui()
        $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
