label home_entrance:
    $ player.go_to(L_home_entrance)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if erik.started(erik_bullying):
        call expression game.dialog_select("entrance_erik_bullying")
        $ erik_bullying.finish()


    if M_jenny.is_state(S_jenny_debbie_altercation) and game.timer.is_tick(1, 2):
        call expression game.dialog_select("entrance_jenny_debbie_altercation")
        $ M_jenny.trigger(T_jenny_altercation_with_debbie)

    elif M_jenny.is_state(S_jenny_catch_her_leaving):
        if not M_jenny.get("j10_caught_her_leaving"):
            $ M_jenny.set("j10_caught_her_leaving", True)
            call expression game.dialog_select("entrance_jenny_catch_her_leaving")
            if M_jenny.get("dominance") <= 0:
                call expression game.dialog_select("entrance_jenny_catch_her_leaving_sub_first")
            else:
                call expression game.dialog_select("entrance_jenny_catch_her_leaving_dom_first")
        else:
            call expression game.dialog_select("entrance_jenny_catch_her_leaving_repeat")
        if player.has_money(200):
            if M_jenny.get("dominance") <= 0:
                call expression game.dialog_select("entrance_jenny_catch_her_leaving_has_money_sub")
            else:
                call expression game.dialog_select("entrance_jenny_catch_her_leaving_has_money_dom")
            $ player.spend_money(200)
            $ M_jenny.trigger(T_jenny_leave_house)
        else:
            if M_jenny.get("dominance") <= 0:
                call expression game.dialog_select("entrance_jenny_catch_her_leaving_no_money_sub")
            else:
                if not M_jenny.get("j10_caught_her_leaving"):
                    call expression game.dialog_select("entrance_jenny_catch_her_leaving_no_money_dom_first")
                else:
                    call expression game.dialog_select("entrance_jenny_catch_her_leaving_no_money_dom")

    elif M_jenny.is_state(S_jenny_catch_her_jilling) and game.timer.is_evening():
        $ player.go_to(L_home_livingroom)
        call expression game.dialog_select("entrance_jenny_catch_her_jilling")
        jump jenny_couch_fj_loop

    elif M_jenny.is_state(S_jenny_want_some_breakfast) and game.timer.is_weekend() and game.timer.is_morning():
        call expression game.dialog_select("entrance_jenny_want_some_breakfast")
        $ player.go_to(L_home_kitchen)
        $ M_jenny.trigger(T_jenny_pool_talk)
        $ game.main()

    elif M_jenny.pregnancy.stage == 2 and M_jenny.pregnancy.first_baby and M_jenny.get("didnt_see_first_baby_dialogue"):
        call expression game.dialog_select("entrance_jenny_first_baby_stage_2_intro")
        if M_diane.finished_state(S_diane_check_barn_out):
            call expression game.dialog_select("entrance_jenny_first_baby_stage_2_diane")
        else:
            call expression game.dialog_select("entrance_jenny_first_baby_stage_2_no_diane")
        call expression game.dialog_select("entrance_jenny_first_baby_stage_2_end")
        $ M_jenny.set("didnt_see_first_baby_dialogue", False)
        $ player.go_to(L_home_livingroom)
        $ game.main()
    elif M_jenny.pregnancy.stage == 5 and M_jenny.pregnancy.first_baby and M_jenny.pregnancy.gave_birth and M_jenny.get("jenny_got_first_baby"):
        call expression game.dialog_select("entrance_jenny_pregnancy_first_baby_coming_home")
        $ M_jenny.set("jenny_got_first_baby", True)

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
            "Да.":
                call expression game.dialog_select("entrance_mom_hang_out_yes")
                $ M_mom.trigger(T_mom_hang_out_accept)
            "Нет.":


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
        "Позволь мне помочь.":
            call expression game.dialog_select("entrance_mom_vacuum_yes")
            $ game.timer.tick()
            $ M_mom.trigger(T_mom_vacuumed)
        "Это слишком громко.":
            call expression game.dialog_select("entrance_mom_vacuum_no")
    $ M_mom.set("chores", False)
    $ game.main()

label erik_bullying_3:
    $ player.go_to(L_home_entrance)
    call expression game.dialog_select("entrance_erik_bullying_3")
    $ erik.add_event(erik_bullying_3)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
