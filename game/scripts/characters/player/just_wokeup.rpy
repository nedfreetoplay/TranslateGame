label player_just_wokeup(woke_with=None):
    scene expression player.location.background_blur
    if M_player.is_state(S_player_start):
        call expression game.dialog_select("bedroom_mc_start_just_wokeup")

    elif woke_with is M_diane and player.location is L_home_mombedroom:
        if M_diane.is_set("3way first time"):
            call expression game.dialog_select("diane_debbie_sleepover_wakeup_first")
            $ M_diane.set("3way first time", False)
        else:
            call expression game.dialog_select("diane_debbie_sleepover_wakeup_repeat")

    elif player.location is L_home_mombedroom:
        if M_mom.is_set("sex available"):
            if randomizer() <= 50:
                call expression game.dialog_select("mom_sleeping_sex_available_random")
            else:
                call expression game.dialog_select("mom_sleeping_sex_available")

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

    if player.location is L_home_bedroom:
        if game.timer.is_morning() and L_home_sisbedroom.is_here(M_jenny) and (M_jenny.is_state(S_jenny_watch_stream) or
            M_jenny.is_state(S_jenny_watch_stream_tier_2) or
            M_jenny.is_state(S_jenny_watch_stream_tier_3) or
            (M_jenny.finished_state(S_jenny_prepare_stream_tier_4) and not sis_lastwebcam_show_seen)):
            call expression game.dialog_select("bedroom_sis_webcam_show")

        elif M_jenny.is_state(S_jenny_telescope_spying) and (not L_home_shower.is_here(M_jenny) and game.timer.is_morning()):
            call expression game.dialog_select("bedroom_sis_telescope_1")

        elif M_jenny.is_state(S_jenny_telescope_spying_tier_2) and (not L_home_shower.is_here(M_jenny) and game.timer.is_morning()):
            call expression game.dialog_select("bedroom_sis_telescope_2")

        elif M_jenny.is_state(S_jenny_telescope_spying_tier_3) and (not L_home_shower.is_here(M_jenny) and game.timer.is_morning()):
            call expression game.dialog_select("bedroom_sis_telescope_3")

        elif (training_count == 1 and training_tier == 2 and M_jenny.is_state(S_jenny_somrak_more_panty)) or (training_count == 2 and training_tier == 3 and M_jenny.is_state(S_jenny_somrak_more_panty_tier_2)) or (training_count == 3 and training_tier == 4 and M_jenny.is_state(S_jenny_somrak_more_panty_tier_3)):
            call expression game.dialog_select("bedroom_master_somrak_training")

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
    $ M_player.set("just wokeup", False)
    call check_pregnancies
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
