label home_livingroom_dialogue:
    python:
        sis_caught_spying = False
    $ player.go_to(L_home_livingroom)
    if M_jenny.is_state(S_jenny_couch_naughty_time) and game.timer.is_evening() and not M_mom.is_state(S_mom_sleepover):
        call expression game.dialog_select("living_room_sis_couch_1_progress")

    elif M_jenny.is_state(S_jenny_couch_naughty_time_tier_3) and game.timer.is_evening() and (not M_mom.is_state(S_mom_sleepover) or not player.location.is_here(M_mom)):
        call expression game.dialog_select("living_room_sis_couch_3_started")
        jump expression game.dialog_select("home_livingroom_tv")

    elif M_mom.is_state(S_mom_spy) and not game.timer.is_dark():
        call expression game.dialog_select("living_room_mom_spy")

    elif M_diane.is_state(S_diane_peeking) and game.timer.is_evening():
        call expression game.dialog_select("living_room_diane_peeking")
        $ M_diane.trigger(T_diane_gotta_jack_it)
        $ player.go_to(L_home_bedroom)
        $ game.lock_ui()
        $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
