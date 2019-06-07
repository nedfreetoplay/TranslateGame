label home_front:
    $ player.go_to(L_home)
    if erik.completed(erik_bullying_2) and not erik.known(erik_bullying_3):
        jump erik_bullying_3

    if game.timer.is_dark():
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    else:

        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)

    if M_roxxy.is_state(S_roxxy_studying_at_mcs):
        call expression game.dialog_select("home_roxxy_studying_at_mcs")
        $ M_roxxy.trigger(T_roxxy_get_cheerleader)
        $ player.go_to(L_home_bedroom)
        $ game.main()

    elif M_roxxy.is_state(S_roxxy_cookies_and_milk):
        call expression game.dialog_select("home_front_roxxy_cookies_and_milk")
        $ game.timer.tick(1)
        $ M_roxxy.trigger(T_roxxy_go_to_police)
        $ player.go_to(L_map)
        $ game.main()

    elif M_mom.is_state(S_mom_mrsj_visit) and not game.timer.is_dark():
        call expression game.dialog_select("home_front_mom_mrsj_visit")
        $ M_mom.trigger(T_mom_mrsj_condolences)

    elif M_mom.is_state(S_mom_mow_lawn):
        call expression game.dialog_select("home_front_mom_mow_lawn")
        $ M_mom.trigger(T_mom_mowed_lawn)


    elif M_mom.is_state(S_mom_car_fixed):
        call expression game.dialog_select("home_front_mom_car_fixed")

        $ player.go_to(L_home_garage)
        call expression game.dialog_select("home_front_mom_car_fixed_check_car")
        $ M_mom.set("jerk count", 0)
        $ M_mom.set("sex speed", .3)
        $ animated = False
        menu:
            "A little longer.":
                call expression game.dialog_select("home_front_mom_car_fixed_check_car_little_longer")
                jump expression game.dialog_select("mom_car_jerk_loop")
            "Leave the car.":

                call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished")

    elif M_mom.get_state() == S_mom_bad_guys_driveby and not game.timer.is_dark():
        jump expression game.dialog_select("bad_guys_driveby")

    elif M_mom.is_state(S_mom_bad_guys_revisit) and not game.timer.is_dark():
        call expression game.dialog_select("home_front_mom_bad_guys_revisit")
        $ M_mom.trigger(T_mom_bad_guys_beatup)
        $ game.timer.tick()
        jump expression game.dialog_select("hallway_dialogue")

    elif M_diane.is_state(S_diane_checkup_results):
        call expression game.dialog_select("home_diane_checkup_results")
        $ M_diane.trigger(T_diane_package_block)
        $ player.go_to(L_home_entrance)
        if not game.timer.is_dark():
            $ game.timer.tick(3)
        $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
