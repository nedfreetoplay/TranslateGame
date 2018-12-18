label mom_bedroom_screen:
    $ player.go_to(L_home_mombedroom)
    $ game.main()

label mom_bed:
    if M_mom.is_set("panties taken"):
        scene location_debbiebed01 with dissolve
        if M_mom.is_state(S_mom_panties_masturbation):
            call expression game.dialog_select("mom_bed_panties_masturbation_first")
            $ M_mom.trigger(T_mom_caught_masturbating)
            $ player.go_to(L_home_livingroom)

        elif M_mom.is_set("sex available"):
            call expression game.dialog_select("mom_bed_panties_masturbation_repeat")
        else:

            label replay_mom_panties:
                call expression game.dialog_select("mom_bed_panties_masturbation_pre")
            if store._in_replay == None and not M_mom.is_state(S_mom_panties_masturbation_again):
                jump expression game.dialog_select("mom_jerk_repeat")
            deb "You promised you wouldn't do this in my room!"
            if not store._in_replay == None:
                jump expression game.dialog_select("replay_mom_panties_2")
            menu:
                "I can't help it!":
                    label replay_mom_panties_2:
                        call expression game.dialog_select("mom_bed_panties_masturbation_cant_help_it")
                    if not store._in_replay == None:
                        jump expression game.dialog_select("mom_jerk_repeat")
                    menu:
                        "I'm trying.":
                            call expression game.dialog_select("mom_bed_panties_masturbation_im_trying")
                        "I like you.":

                            label mom_jerk_repeat:
                                $ M_mom.set("sex speed", .15)
                                $ M_mom.set("no panties", False)
                            if not store._in_replay == None or L_home_basement.is_here(M_mom):
                                if store._in_replay == None or not store._in_replay == None and renpy.random.random() > 0.5:
                                    $ M_mom.set("no panties", True)
                            call expression game.dialog_select("mom_bed_panties_masturbation_i_like_you")
                            $ renpy.end_replay()
                            $ persistent.cookie_jar["Debbie"]["unlocked"] = True
                            $ persistent.cookie_jar["Debbie"]["gallery"]["02_unlocked"] = True
                            $ M_mom.trigger(T_mom_caught_masturbating)
                        "Not really.":

                            call expression game.dialog_select("mom_bed_panties_masturbation_not_really")
                "Sorry.":

                    call expression game.dialog_select("mom_bed_panties_masturbation_sorry")
        $ M_mom.set("panties taken", False)

        $ game.timer.tick()
        hide debbie
        hide player
        with dissolve

    elif M_mom.is_state(S_mom_movie_afterthoughts_two):
        call expression game.dialog_select("mombedroom_mom_movie_afterthoughts_two")
        $ player.go_to(L_home_bedroom)
        $ game.main()

    elif M_mom.is_set("sleep together") and game.timer.is_dark():
        label mom_night_sex_replay:
            if not store._in_replay == None:
                $ M_mom.set("sex available", True)
        scene debbie_bedroom_closeup_sex
        if M_mom.is_set("sex available"):
            call expression game.dialog_select("mom_bed_sleep_together_pre_sex_available")
        else:

            call expression game.dialog_select("mom_bed_sleep_together_pre")
        $ game.timer.tick()
        menu mom_sleep_options:
            "Cuddle":
                if M_mom.is_set("sex available"):
                    call expression game.dialog_select("mom_bed_sleep_together_cuddle_sex_available")
                else:

                    call expression game.dialog_select("mom_bed_sleep_together_cuddle")
                menu mom_bed_sleep_together_cuddle_options:
                    "Keep going":
                        call expression game.dialog_select("mom_bed_sleep_together_cuddle_keep_going")
                        jump expression game.dialog_select("mom_bed_sleep_together_cuddle_options")
                    "Stop.":

                        call expression game.dialog_select("mom_bed_sleep_together_stop")
                        jump expression game.dialog_select("mom_sleep_options")
            "Ask for a kiss":

                if M_mom.is_set("sex available"):
                    call expression game.dialog_select("mom_bed_sleep_together_kiss_sex_available")
                else:

                    call expression game.dialog_select("mom_bed_sleep_together_kiss")
                menu mom_bed_sleep_together_kiss_options:
                    "Keep going":
                        call expression game.dialog_select("mom_bed_sleep_together_kiss_keep_going")
                        jump expression game.dialog_select("mom_bed_sleep_together_kiss_options")
                    "Stop.":

                        call expression game.dialog_select("mom_bed_sleep_together_stop")
                        jump expression game.dialog_select("mom_sleep_options")
            "Breastfeed":

                if M_mom.is_set("sex available"):
                    call expression game.dialog_select("mom_bed_sleep_together_breastfeed_sex_available")
                else:

                    call expression game.dialog_select("mom_bed_sleep_together_breastfeed")
                menu mom_bed_sleep_together_breastfeed_options:
                    "Keep going":
                        call expression game.dialog_select("mom_bed_sleep_together_breastfeed_keep_going")
                        jump expression game.dialog_select("mom_bed_sleep_together_breastfeed_options")
                    "Stop.":

                        call expression game.dialog_select("mom_bed_sleep_together_stop")
                        jump expression game.dialog_select("mom_sleep_options")
            "Rub":

                if M_mom.is_set("sex available"):
                    call expression game.dialog_select("mom_bed_sleep_together_rub_sex_available")
                else:

                    call expression game.dialog_select("mom_bed_sleep_together_rub")
                menu mom_bed_sleep_together_rub_options:
                    "Keep going":
                        call expression game.dialog_select("mom_bed_sleep_together_rub_keep_going")
                        jump expression game.dialog_select("mom_bed_sleep_together_rub_options")
                    "Stop.":

                        call expression game.dialog_select("mom_bed_sleep_together_stop")
                        jump expression game.dialog_select("mom_sleep_options")

            "Fuck" if M_mom.is_set("sex available"):
                $ anim_toggle = True
                $ animated = False
                $ xray = False
                call expression game.dialog_select("mom_bed_sleep_together_fuck")
                menu mom_bed_sleep_together_fuck_options:
                    "Keep going":
                        call expression game.dialog_select("mom_bed_sleep_together_fuck_keep_going")
                        jump expression game.dialog_select("mom_bed_sleep_together_fuck_options")
                    "Cum":

                        call expression game.dialog_select("mom_bed_sleep_together_fuck_cum")
                        $ renpy.end_replay()
                        $ persistent.cookie_jar["Debbie"]["unlocked"] = True
                        $ persistent.cookie_jar["Debbie"]["gallery"]["06_unlocked"] = True
                        menu:
                            "Stay.":
                                call expression game.dialog_select("mom_bed_sleep_together_fuck_cum_stay")
                                jump expression game.dialog_select("mom_sleeping")
                            "Leave.":

                                call expression game.dialog_select("mom_bed_sleep_together_fuck_cum_leave")
                                $ player.go_to(L_home_livingroom)

            "Sleep with {b}[deb_name]{/b}." if store._in_replay == None:
                call expression game.dialog_select("mom_bed_sleep_together_sleep")
                jump expression game.dialog_select("mom_sleeping")

    elif game.timer.is_dark():
        call expression game.dialog_select("mom_bed_night")
    else:

        call expression game.dialog_select("mom_bed_day")
    $ game.main()

label mom_bedroom:
    $ player.go_to(L_home_mombedroom)
    if game.timer.is_dark() and M_mom.is_state(S_mom_end) and M_diane.is_state(S_diane_risky_frisky_kinky) and not M_diane.pregnancy and not M_mom.pregnancy:
        call expression game.dialog_select("mom_bedroom_diane_risky_frisky_kinky")
        $ player.go_to(L_home_bedroom)
        $ M_diane.trigger(T_diane_debbie_caught)
        $ game.main()

    if M_diane.is_state(S_diane_end) and M_diane.get("refused 3way"):
        call expression game.dialog_select("mom_bedroom_diane_refused_3way")
        $ player.go_to(L_home_livingroom)
        $ game.main()

    if M_mom.is_state(S_mom_spy) and not game.timer.is_dark():
        call expression game.dialog_select("mom_spy")
        $ M_mom.trigger(T_mom_caught_spying)
        $ persistent.cookie_jar["Debbie"]["unlocked"] = True
        $ persistent.cookie_jar["Debbie"]["gallery"]["01_unlocked"] = True
        $ game.timer.tick()

    elif M_mom.is_state(S_mom_panties_masturbation_again):
        call expression game.dialog_select("moms_bedroom_mom_panties_masturbation_again")

    elif M_mom.is_state(S_mom_sleepover_wakeup):
        call expression game.dialog_select("moms_bedroom_mom_sleepover_makeup")
        $ M_mom.trigger(T_mom_sleepover_morning)
        $ player.go_to(L_home_livingroom)

    elif M_diane.is_state(S_diane_debbie_dinner_outfit):
        call expression game.dialog_select("moms_bedroom_mom_dinner_outfit")
        menu:
            "Ask {b}[deb_name]{/b}.":
                call expression game.dialog_select("moms_bedroom_mom_dinner_outfit_ask")
            "Just leave.":

                $ pass
        $ M_diane.trigger(T_diane_debbie_gave_dinner_outfit_advice)
        jump expression game.dialog_select("home_livingroom_dialogue")

    elif M_mom.is_state(S_mom_midnight_swim_after):
        $ player.go_to(L_home_livingroom)
        call expression game.dialog_select("moms_bedroom_mom_midnight_swim_after")

    elif game.timer.is_dark() and not L_home_mombedroom.is_here(M_diane) and L_home_mombedroom.is_here(M_mom):
        call expression game.dialog_select("moms_bedroom_night")

    elif not M_mom.is_set("fetch lotion") and not M_mom.is_set("sleep together"):
        call expression game.dialog_select("moms_bedroom_mom_is_set_lotion")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
