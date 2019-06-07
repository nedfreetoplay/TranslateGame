label player_just_wokeup(woke_with=None):
    scene expression player.location.background_blur
    if M_jenny.is_state(S_jenny_bedroom_intrusion) and player.location == L_home_bedroom:
        call expression game.dialog_select("bedroom_jenny_bedroom_intrusion_1")
    if M_player.is_state(S_player_start):
        call expression game.dialog_select("bedroom_mc_start_just_wokeup")

    elif woke_with is M_diane and player.location == L_home_mombedroom:
        if M_diane.is_set("3way first time"):
            call expression game.dialog_select("diane_debbie_sleepover_wakeup_first")
            $ M_diane.set("3way first time", False)
        else:
            call expression game.dialog_select("diane_debbie_sleepover_wakeup_repeat")

    elif woke_with is M_jenny and player.location == L_home_sisbedroom:
        call expression game.dialog_select("player_jenny_sleepover_sisbedroom")
        $ player.go_to(L_home_hallway)
        $ game.main()

    elif woke_with is M_jenny and player.location == L_home_bedroom:
        call expression game.dialog_select("player_jenny_sleepover_mcbedroom")

    elif player.location == L_home_mombedroom:
        if M_mom.is_set("sex available"):
            if randomizer() <= 50:
                call expression game.dialog_select("mom_sleeping_sex_available_random")
            else:
                call expression game.dialog_select("mom_sleeping_sex_available")

    elif M_jenny.is_state(S_jenny_get_a_toy) and player.location == L_home_bedroom:
        call expression game.dialog_select("bedroom_jenny_get_a_toy")

    elif game.timer.is_weekend():
        if player.location in L_beachhouse_front.get_all_children():
            call expression game.dialog_select("beachhouse_weekend_just_wokeup")
        else:
            call expression game.dialog_select("bedroom_mc_weekend_just_wokeup")
    else:

        if player.location in L_beachhouse_front.get_all_children():
            call expression game.dialog_select("beachhouse_weekday_just_wokeup")
        else:
            call expression game.dialog_select("bedroom_mc_weekday_just_wokeup")

    if player.location == L_home_bedroom:
        if M_mom.is_set("chores"):
            call expression game.dialog_select("bedroom_mom_chores")

        elif M_mom.is_state(S_mom_search_panties):
            call expression game.dialog_select("bedroom_mom_search_panties")

        elif M_mom.is_state(S_mom_kissing_practice):
            call expression game.dialog_select("bedroom_mom_kissing_practice")

        elif M_mom.is_state(S_mom_note):
            call expression game.dialog_select("bedroom_mom_note_just_wokeup")

        if M_diane.is_state(S_diane_get_augmentation):
            call expression game.dialog_select("bedroom_diane_get_augmentation")
            $ M_diane.trigger(T_diane_chat_at_home)

        elif M_diane.is_state(S_diane_debbie_dinner):
            call expression game.dialog_select("bedroom_diane_debbie_dinner")
            $ M_diane.trigger(T_diane_dinner_task_acquired)

        elif M_diane.is_state(S_diane_barn_news):
            call expression game.dialog_select("bedroom_diane_barn_news")

        elif M_diane.is_state(S_diane_breeding_candidate):
            call expression game.dialog_select("bedroom_diane_breeding_candidate")

        if M_roxxy.is_state(S_roxxy_spin_bottle) and game.timer == Date(dow="saturday"):
            call expression game.dialog_select("bedroom_roxxy_spin_bottle")
            if not player.has_item("goldschwagger"):
                call expression game.dialog_select("bedroom_roxxy_spin_bottle_no_goldschwagger")
            hide player with dissolve

        if M_jenny.pregnancy.stage == 4 and not M_jenny.get("seen_in_shower_pregnant"):
            call expression game.dialog_select("bedroom_jenny_pregnant_and_peeing")
            $ M_jenny.set("seen_in_shower_pregnant", True)
            $ game._in_shower = None
            $ player.go_to(L_home_hallway)
            $ game.main()

        if M_jenny.is_state(S_jenny_breakfast_notice):
            call expression game.dialog_select("bedroom_jenny_breakfast_notice")
            $ M_jenny.trigger(T_jenny_breakfast_notice)
        elif M_jenny.is_state(S_jenny_pics_afterthought):
            call expression game.dialog_select("bedroom_jenny_pics_afterthought")
            $ M_jenny.trigger(T_jenny_snoop_in_her_room)
        elif M_jenny.is_state(S_jenny_breakfast_notice_2):
            call expression game.dialog_select("bedroom_jenny_breakfast_notice")
            $ M_jenny.trigger(T_jenny_breakfast_notice_2)
        elif M_jenny.is_state(S_jenny_snooping_laptop_notice):
            call expression game.dialog_select("bedroom_jenny_snoopin_laptop_notice")
        elif M_jenny.is_state(S_jenny_new_video_notice):
            call expression game.dialog_select("bedroom_jenny_new_video_notice")
        elif M_jenny.is_state(S_jenny_buy_bad_monster):
            call expression game.dialog_select("bedroom_jenny_buy_bad_monster")
        elif M_jenny.is_state(S_jenny_spy_on_mia_telescope):
            call expression game.dialog_select("bedroom_jenny_spy_on_mia_telescope")
        elif M_jenny.is_state(S_jenny_pissed_at_handjob, S_jenny_pissed_at_blowjob):
            call expression game.dialog_select("bedroom_jenny_pissed_at_handjob")
        elif M_jenny.is_state(S_jenny_morning_visit):
            call expression game.dialog_select("bedroom_jenny_morning_visit")
            $ M_jenny.trigger(T_jenny_start_camshow_blowjob)
        elif M_jenny.is_state(S_jenny_perv_on_tammy):
            call expression game.dialog_select("bedroom_jenny_perv_on_tammy_notice")
        elif M_jenny.is_state(S_jenny_bedroom_intrusion):
            call expression game.dialog_select("bedroom_jenny_bedroom_intrusion_2")
            $ M_jenny.trigger(T_jenny_go_breakfast)
        elif M_jenny.is_state(S_jenny_weird_relationship):
            call expression game.dialog_select("bedroom_jenny_weird_relationship")
            $ M_jenny.trigger(T_jenny_final_breakfast)
    $ M_player.set("just wokeup", False)
    call check_pregnancies
    $ Machine.trigger(T_player_woke_up)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
