label bedroom_dialogue:
    $ player.go_to(L_home_bedroom)
    scene expression game.timer.image("bedroom{}") with None
    if not M_player.is_set("just wokeup"):
        if M_mom.is_state(S_mom_mrsj_visit) and not game.timer.is_dark():
            jump expression game.dialog_select("home_front")

        elif M_mom.is_state(S_mom_car_fixed):
            jump expression game.dialog_select("home_front")

        elif M_mom.is_state(S_mom_bad_guys_revisit) and not game.timer.is_dark():
            jump expression game.dialog_select("home_front")

        elif M_mom.is_state(S_mom_diane_visit) and game.timer.is_evening():
            jump expression game.dialog_select("home_entrance")

    if game.timer.game_day() >= event_wait_till and not erik.known(erik_bullying):
        call expression game.dialog_select("bedroom_erik_bullying")
        $ erik.add_event(erik_bullying)
        $ M_erik.place(place = L_erikhouse_erikroom)
        $ M_erik.force()

    elif erik.completed(erik_bullying_2) and not erik.known(erik_bullying_3):
        jump expression game.dialog_select("erik_bullying_3")

    if M_mia.is_state(S_mia_tattoo_help) and M_mia.is_set('story delay'):
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

    if M_bissette.is_state(S_bissette_french_food_assignment):
        call expression game.dialog_select("bedroom_bissette_french_food_assignment")

    elif M_bissette.is_state(S_bissette_roxxy_jenny_mentoring) and game.timer.is_afternoon():
        call expression game.dialog_select("bedroom_bissette_roxxy_jenny_mentoring")

    if M_dewitt.is_state(S_dewitt_make_replacement_guitar) and player.has_item("paint") and player.has_item("wood_pile"):
        call expression game.dialog_select("bedroom_dewitt_make_replacement_guitar")

    if M_player.is_set("just wokeup"):
        call expression game.dialog_select("player_just_wokeup")

    elif game.timer.is_evening():
        if M_jenny.is_state(S_jenny_couch_naughty_time):
            call expression game.dialog_select("bedroom_sis_couch_1")

        elif M_jenny.is_state(S_jenny_couch_naughty_time_tier_3):
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
    if M_diane.is_state(S_diane_peeking_masturbate):
        jump diane_masturbatory_fantasy_d17
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

                "Рокси." if M_player.is_set("jerk roxxy"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_roxxy")
                    scene black with fade
                    $ game.timer.tick()

                "Диана." if M_player.is_set("jerk diane"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_diane")
                    scene black with fade
                    $ game.timer.tick()
                "Уйти.":

                    $ pass
        "Уйти.":

            $ pass
    $ game.main()

label diane_masturbatory_fantasy_d17:
    call expression game.dialog_select("bedroom_sleeping_jerk_off_diane")
    pause
    player_name "Ммм, {b}Диана{/b}!"
    scene expression "backgrounds/location_home_hallway_night_blur.jpg"
    show diane b_nightgown a_nightgown_sides f_scared
    with dissolve
    dia "( ... )"
    dia "( Ох, что я делаю? )"
    pause
    dia "( Я действительно обдумываю это?! )"
    pause
    player_name "Ммм, {b}Диана{/b}!"
    show diane f_surprised
    dia "( !!! )" with hpunch
    dia "( {b}[firstname]{/b}? )"
    scene expression "backgrounds/location_home_bedroom_cutscene11.jpg" with fade
    dia "( Он- )"
    pause
    dia "( !!! )"
    pause
    dia "( О, боже мой... )"
    pause
    dia "( Он такой большой! )"
    pause
    player_name "Ха, вот и оно!"
    scene expression "backgrounds/location_home_bedroom_cutscene11b.jpg" with fade
    pause
    player_name "ХННГГГГ!!!"
    dia "( !!! )" with hpunch
    pause
    dia "( Посмотри на всю эту сперму! )"
    pause
    player_name "Ааа, {b}Диана{/b}!"
    pause
    scene expression "backgrounds/location_home_bedroom_cutscene12.jpg" with fade
    dia "( Все это... Для меня? )"
    pause
    player_name "Аааа... Аааа..."
    scene black with fade
    dia "{b}[firstname]{/b}?"
    scene expression "backgrounds/location_home_bedroom_sex03.jpg"
    show player afterjerk 1
    show diane b_nightgown a_nightgown_sides f_smirk
    player_name "!!!" with hpunch
    player_name "{b}Диана{/b}?"
    player_name "Что ты-"
    show player afterjerk 2
    show diane f_reading_intrigued
    dia "Шшш."
    show diane b_nightgown_sit a_empty f_sit_bed_smirk_talk_fardown with dissolve
    dia "Я понятия не имела, что ты-"
    show diane f_jerk_bed_smirk_fardown b_nightgown_sit_stroke1
    pause
    show diane f_jerk_bed_smirk_talk_fardown b_nightgown_sit_stroke2
    dia "Так много всего..."
    show diane f_jerk_bed_smirk_fardown
    show player afterjerk 1
    player_name "Да."
    show diane f_empty b_nightgown_sit_kiss
    player_name "!!!" with hpunch
    show player afterjerk 3
    pause
    show player afterjerk 2
    show diane f_jerk_bed_smirk_talk_fardown b_nightgown_sit_stroke
    dia "Ммм, Я думаю, что хочу сделать это {b}[firstname]{/b}..."
    dia "Я хочу, чтобы ты осеменил меня."
    show diane f_jerk_bed_smirk_fardown
    show player afterjerk 1
    player_name "Ты хочешь?"
    show player afterjerk 2
    dia "Мммммм!"
    show player afterjerk 1
    player_name "Что о {b}[deb_name]{/b}?"
    show player afterjerk 2
    show diane f_jerk_bed_smirk_talk_fardown
    dia "Когда придет время, я поговорю с ней."
    dia "Мне остается только надеяться, что она простит меня..."
    show diane f_jerk_bed_smirk_fardown
    show player afterjerk 1
    player_name "Думаю, она поймет, {b}Диана{/b}."
    show player afterjerk 3
    show diane f_empty b_nightgown_sit_kiss
    with dissolve
    dia "Ммм."
    pause
    show player afterjerk 2
    show diane f_jerk_bed_smirk_talk_fardown b_nightgown_sit_stroke
    with dissolve
    dia "О, я так сильно хочу тебя внутри себя!"
    dia "... Но не сейчас!"
    show diane f_jerk_bed_smirk_fardown
    player_name "Хмм?"
    show diane f_jerk_bed_smirk_talk_fardown
    dia "Я хочу, чтобы наш первый раз был особенным."
    dia "Приходи ко мне завтра в амбар."
    show diane f_jerk_bed_smirk_fardown
    show player afterjerk 1
    player_name "Хорошо."
    show player afterjerk 3
    show diane f_empty b_nightgown_sit_kiss
    with dissolve
    pause
    show diane f_sit_bed_smirk_talk_fardown b_nightgown_sit
    show player afterjerk 2
    dia "Спокойной ночи, жеребец."
    show diane f_sit_bed_smirk_fardown
    show player afterjerk 1
    player_name "Спокойной ночи, {b}Диана{/b}..."
    hide diane with dissolve
    pause
    show player afterjerk 1
    player_name "( Да, как будто я действительно смогу спать после этого... )"
    hide player with dissolve
    $ M_diane.trigger(T_diane_learns_your_secret)
    $ game.timer.tick()
    $ game.unlock_ui()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
