label bedroom_dialogue:
    $ player.go_to(L_home_bedroom)
    if not M_player.is_set("just wokeup"):
        if M_mom.is_state(S_mom_mrsj_visit) and not game.timer.is_dark():
            jump expression game.dialog_select("home_front")

        elif M_mom.is_state(S_mom_car_fixed):
            jump expression game.dialog_select("home_front")

        elif M_mom.is_state(S_mom_bad_guys_revisit) and not game.timer.is_dark():
            jump expression game.dialog_select("home_front")

        elif M_mom.is_state(S_mom_diane_visit) and game.timer.is_evening():
            jump expression game.dialog_select("home_entrance")

    if erik.completed(erik_bullying_2) and not erik.known(erik_bullying_3):
        jump expression game.dialog_select("erik_bullying_3")

    if M_player.is_state(S_player_start) and M_player.is_set("just wokeup"):
        call expression game.dialog_select("bedroom_mc_start_just_wokeup")

    elif game.timer.is_morning() and not game.timer.is_weekend() and M_player.is_set("just wokeup"):
        call expression game.dialog_select("bedroom_mc_weekday_just_wokeup")

    elif game.timer.is_morning() and game.timer.is_weekend() and M_player.is_set("just wokeup"):
        call expression game.dialog_select("bedroom_mc_weekend_just_wokeup")

    if game.timer.game_day() >= event_wait_till and not erik.known(erik_bullying):
        call expression game.dialog_select("bedroom_erik_bullying")

        $ erik.add_event(erik_bullying)
        $ M_erik.place(place = L_erikhouse_erikroom)
        $ M_erik.force()

    elif M_mia.is_state(S_mia_tattoo_help) and M_mia.is_set('story delay'):
        call expression game.dialog_select("bedroom_mia_tattoo_help")
        $ M_mia.trigger(T_mia_tattoo_start)

    elif M_mia.is_state(S_mia_strip_aftermath):
        call expression game.dialog_select("bedroom_mia_strip_aftermath_grounded")
        $ M_mia.trigger(T_mia_grounded)

    elif M_mia.is_state(S_mia_concerning_visit):
        call expression game.dialog_select("bedroom_mia_concerning_visit")

    elif M_mia.is_state(S_mia_urgent_message):
        call expression game.dialog_select("bedroom_mia_urgent_message")

        $ player.receive_message("mia02")

    elif M_mia.is_state(S_mia_angelicas_impatience):
        call expression game.dialog_select("bedroom_mia_angelicas_impatience")


    elif M_mia.is_state(S_mia_angelicas_home_visit):
        call expression game.dialog_select("bedroom_mia_angelicas_home_visit")


    elif M_mia.is_state(S_mia_angelicas_final_home_visit):
        call expression game.dialog_select("bedroom_mia_angelicas_final_home_visit")


    if M_mom.is_state(S_mom_overheard) and game.timer.is_dark():
        call expression game.dialog_select("bedroom_mom_overheard")
        $ M_mom.trigger(T_mom_check)


    elif M_mom.is_state(S_mom_doorbell):
        call expression game.dialog_select("bedroom_mom_doorbell")
        $ M_mom.trigger(T_mom_check_door)


    elif M_mom.is_state(S_mom_movie_afterthoughts):
        call expression game.dialog_select("bedroom_mom_movie_afterthoughts")
        $ M_mom.trigger(T_mom_movie_night_finish)

    elif M_mom.is_state(S_mom_movie_afterthoughts_two):
        call expression game.dialog_select("bedroom_mom_afterthoughts_two")
        $ M_mom.trigger(T_mom_movie_night_finish)

    elif M_mom.is_state(S_mom_note) and game.timer.is_dark():
        call expression game.dialog_select("bedroom_mom_note")

    elif M_mom.is_state(S_mom_note) and M_player.is_set("just wokeup"):
        call expression game.dialog_select("bedroom_mom_note_just_wokeup")
        $ M_player.set("just wokeup", False)


    if M_bissette.is_state(S_bissette_french_food_assignment):
        call expression game.dialog_select("bedroom_bissette_french_food_assignment")

    elif M_bissette.is_state(S_bissette_roxxy_jenny_mentoring) and game.timer.is_afternoon():
        call expression game.dialog_select("bedroom_bissette_roxxy_jenny_mentoring")

    if M_dewitt.is_state(S_dewitt_make_replacement_guitar) and player.has_item("paint") and player.has_item("wood_pile"):
        call expression game.dialog_select("bedroom_dewitt_make_replacement_guitar")

    if not game.timer.is_dark():
        if M_player.is_set("just wokeup"):
            call expression game.dialog_select("player_just_wokeup")

    elif game.timer.is_evening():
        if sister.started(sis_couch01):
            call expression game.dialog_select("bedroom_sis_couch_1")

        elif sister.started(sis_couch03):
            call expression game.dialog_select("bedroom_sis_couch_3")
    $ game.main()

label sleeping:
    if M_mom.is_state([S_mom_movie_night, S_mom_movie_night_two]):
        call expression game.dialog_select("bedroom_sleeping_debbie_movie_night")
        $ game.timer.tick(2)

        $ game.main()

    elif M_mom.is_state(S_mom_sleepover):
        call expression game.dialog_select("bedroom_sleeping_debbie_sleepover")
        $ game.main()

    elif M_mom.is_set("room sneak"):
        jump expression game.dialog_select("bedroom_debbie_sleepover")

    if erik.over(erik_breastfeeding_2) and not erik.over(erik_thief):
        if erik.in_progress(erik_thief):
            $ erik_thief.unfinish()


        elif randomizer() > 66:
            if not erik.known(erik_thief):
                $ erik.add_event(erik_thief)
            call expression game.dialog_select("bedroom_sleeping_erik_thief_pre")
            menu:
                "Использовать телескоп.":
                    call expression game.dialog_select("bedroom_sleeping_erik_thief_use_telescope")
                    $ game.timer.tick(3)
                    $ erik_thief.finish()

                    scene black with fade
                    jump expression game.dialog_select("erik_house_dialogue")
                "Вернуться ко сну.":

                    call expression game.dialog_select("bedroom_sleeping_erik_thief_sleep")

    elif erik.started(erik_bullying_3):
        call expression game.dialog_select("bedroom_sleeping_erik_bullying_3_started")
        $ erik_bullying_3.finish()
        $ M_erik.place(place = L_erikhouse_basement)
        $ M_erik.force()

    elif M_dewitt.is_state(S_dewitt_eve_karaoke):
        call expression game.dialog_select("bedroom_sleeping_dewitt_eve_karaoke")
        $ game.main()

    elif M_dewitt.is_state(S_dewitt_school_sneak_mission):
        call expression game.dialog_select("bedroom_sleeping_dewitt_school_sneak_mission")
        $ game.main()

    elif M_mia.is_state(S_mia_midnight_call):
        call expression game.dialog_select("bedroom_sleeping_mia_midnight_call")

        $ game.timer.tick(3)
        $ player.receive_message("mia01")
        $ game.main()

    elif M_mom.is_state(S_mom_solo_dream):
        call expression game.dialog_select("bedroom_sleeping_debbie_solo_dream")
        $ M_mom.trigger(T_mom_dream)

    elif M_mom.is_state(S_mom_night_visit):
        call expression game.dialog_select("bedroom_sleeping_debbie_night_visit")
        $ M_mom.trigger(T_mom_midnight_fun)

    elif M_mom.is_state(S_mom_night_visit_two):
        call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_two")
        $ persistent.cookie_jar["Debbie"]["unlocked"] = True
        $ persistent.cookie_jar["Debbie"]["gallery"]["03_unlocked"] = True
        $ M_mom.trigger(T_mom_midnight_fun)

    elif M_mom.is_state(S_mom_midnight_noises):
        call expression game.dialog_select("bedroom_sleeping_debbie_midnight_noises")
        $ M_mom.trigger(T_mom_midnight_wakeup)
        $ game.timer.tick(3)

        $ game.main()

    elif M_mom.is_state(S_mom_night_visit_three):
        label mom_mc_sexvisit:
            call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three")
        $ keep_going = 0
        $ M_mom.set("change angle", False)
        call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_loop")
    else:

        show expression game.timer.image("bedroom{}")

    if M_player.is_set("pet cat"):
        scene location_home_bedroom_sleeping3 with fade
    else:
        scene location_home_bedroom_sleeping with fade
    show unlock11 at truecenter with dissolve
    $ renpy.pause()
    $ Sleep()
    hide unlock11
    hide bedroom
    hide bedroom_broken
    hide bedroom_night
    hide bedroom_broken_night
    scene black with fade
    hide sleeping with fade

    if M_mom.is_state(S_mom_smith_dream):
        call expression game.dialog_select("bedroom_sleeping_debbie_smith_dream")
        $ M_mom.trigger(T_mom_dream)
    jump expression game.dialog_select("bedroom_dialogue")

label jerking_off_dialogue:
    scene expression game.timer.image("bedroom{}")
    menu:
        "Дрочить.":
            $ A_solo_pleasure.unlock()
            menu:
                "{b}[deb_name]{/b}." if M_player.is_set("jerk mom"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_debbie")
                    scene black with fade
                    $ game.timer.tick()

                "Мия." if M_player.is_set("jerk mia"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_mia")
                    scene black with fade
                    $ game.timer.tick()

                "Рокси" if M_player.is_set("jerk roxxy"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_roxxy")
                    scene black with fade
                    $ game.timer.tick()
                "Оставить.":

                    $ pass
        "Оставить.":

            $ pass
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
