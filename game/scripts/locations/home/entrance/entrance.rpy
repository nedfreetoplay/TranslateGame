label home_entrance:
    $ player.go_to(L_home_entrance)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if erik.started(erik_bullying):
        call expression game.dialog_select("entrance_erik_bullying")
        $ erik_bullying.finish()


    if M_mia.is_state(S_mia_angelicas_impatience):
        call expression game.dialog_select("entrance_mia_angelicas_impatience")
        $ M_mia.trigger(T_angelica_house_visit)


    elif M_mia.is_state(S_mia_angelicas_home_visit):
        call expression game.dialog_select("entrance_mia_angelicas_home_visit")
        $ M_mia.trigger(T_angelica_requires_whip)


    elif M_mia.is_state(S_mia_angelicas_final_home_visit):
        call expression game.dialog_select("entrance_mia_angelicas_final_home_visit")
        $ M_mia.trigger(T_angelica_strapon_request)


    if M_mom.is_state(S_mom_overheard):
        call expression game.dialog_select("entrance_mom_overheard")
        $ M_mom.trigger(T_mom_check)


    elif M_mom.is_state(S_mom_lawn_help) and not game.timer.is_dark():
        call expression game.dialog_select("entrance_mom_lawn_help")
        $ M_mom.trigger(T_mom_help_mow)

    elif M_mom.is_state(S_mom_clothes_dirty):
        call expression game.dialog_select("entrance_mom_clothes_dirty")
        $ M_mom.trigger(T_mom_sis_bitch)

    elif M_mom.is_state(S_mom_debt_collectors):
        $ playMusic("<loop 73.5>audio/music_villain.ogg", 1.0)
        call expression game.dialog_select("entrance_mom_debt_collectors")
        $ M_mom.trigger(T_mom_bad_guys)


    elif M_mom.is_state(S_mom_pipe_help) and game.timer.is_morning():
        call expression game.dialog_select("entrance_mom_pipe_help")
        $ M_mom.trigger(T_mom_broken_pipe)


    elif M_mom.is_state(S_mom_movie_night) and game.timer.is_evening():
        call expression game.dialog_select("entrance_mom_movie_night")
        $ M_mom.trigger(T_mom_movie_invite)


    elif M_mom.is_state(S_mom_hang_out) and not game.timer.is_dark():
        call expression game.dialog_select("entrance_mom_hang_out")
        menu:
            "Yes.":
                call expression game.dialog_select("entrance_mom_hang_out_yes")
                $ M_mom.trigger(T_mom_hang_out_accept)
            "No.":


                call expression game.dialog_select("entrance_mom_hang_out_no")
                $ M_mom.trigger(T_mom_hang_out_refuse)
        hide debbie
        hide player
        with dissolve

    elif M_mom.is_state(S_mom_spy) and not game.timer.is_dark():
        call expression game.dialog_select("entrance_mom_spy")

    elif M_mom.is_state(S_mom_kissing_practice) and not game.timer.is_dark():
        call expression game.dialog_select("entrance_mom_kissing_practice")

    elif M_mom.is_state(S_mom_car_broken) and game.timer.is_morning():
        call expression game.dialog_select("entrance_mom_car_broken")
        $ M_mom.trigger(T_mom_car_help)

    elif M_mom.is_state(S_mom_panties_masturbation_again) and not game.timer.is_dark():
        if L_home_basement.is_here(M_mom):
            $ temp = "Basement"
        else:
            $ temp = "Kitchen"
        call expression game.dialog_select("entrance_mom_panties_masturbation_again")

    elif M_mom.is_state(S_mom_diane_visit) and game.timer.is_evening():
        call expression game.dialog_select("entrance_mom_diane_visit")

    elif M_mom.is_state(S_mom_midnight_search):
        jump mom_midnight_swim

    if M_jenny.is_state(S_jenny_couch_naughty_time) and game.timer.is_evening():
        call expression game.dialog_select("entrance_sis_couch_1")

    elif M_jenny.is_state(S_jenny_couch_naughty_time_tier_2) and game.timer.is_evening():
        call expression game.dialog_select("entrance_sis_couch_2")

    elif M_jenny.is_state(S_jenny_couch_naughty_time_tier_3) and game.timer.is_evening() and (not M_mom.is_state(S_mom_sleepover) or not L_home_livingroom.is_here(M_mom)):
        call expression game.dialog_select("entrance_sis_couch_3")
        jump home_livingroom_dialogue

    if M_bissette.is_state(S_bissette_roxxy_jenny_mentoring) and game.timer.is_afternoon():
        if not M_roxxy.get("roxxy trailer sex"):
            call expression game.dialog_select("entrance_bissette_roxxy_jenny_mentoring")
        else:

            call expression game.dialog_select("entrance_bissette_roxxy_jenny_mentoring_sex")
        $ M_bissette.trigger(T_bissette_roxxy_jenny_hangout)

    if M_diane.is_state(S_diane_debbie_evening_visit) and game.timer.is_evening():
        call expression game.dialog_select("entrance_diane_debbie_evening_visit_overhear")

    elif M_diane.is_state(S_diane_debbie_drop_off_request) and game.timer.is_dark():
        call expression game.dialog_select("entrance_diane_debbie_drop_off_request")
        $ M_diane.trigger(T_diane_debbie_request)

    elif M_diane.is_state(S_diane_couch_crashing):
        call expression game.dialog_select("entrance_diane_couch_crashing")
        $ M_diane.trigger(T_diane_moved_in)
        $ game.timer.tick(3)
        $ game.main()

    elif M_diane.is_state(S_diane_peeking) and game.timer.is_evening():
        call expression game.dialog_select("entrance_diane_peeking")

    if game.timer.is_evening() and M_diane.pregnancy.gave_birth and not M_diane.pregnancy.gave_birth_dialogue_seen:
        call expression game.dialog_select("entrance_diane_gave_birth_dialogue_seen")
        $ M_diane.pregnancy.gave_birth_dialogue_seen = True

    $ game.main()

label vacuum_dialogue:
    call expression game.dialog_select("entrance_mom_vacuum")
    menu:
        "Let me help.":
            call expression game.dialog_select("entrance_mom_vacuum_yes")
            $ game.timer.tick()
            $ M_mom.trigger(T_mom_vacuumed)
        "It's too loud.":
            call expression game.dialog_select("entrance_mom_vacuum_no")
    $ M_mom.set("chores", False)
    $ game.main()

label erik_bullying_3:
    $ player.go_to(L_home_entrance)
    call expression game.dialog_select("entrance_erik_bullying_3")
    $ erik.add_event(erik_bullying_3)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
