label diane_garden_check:
    if not M_diane.finished_state(S_diane_need_shovel):
        jump expression game.dialog_select("find_shovel")

    elif M_diane.is_state(S_diane_drunken_splur, S_diane_get_cold_towel, S_diane_bring_cold_towel, S_diane_drunken_splur_aftermath):
        jump expression game.dialog_select("garden_diane_drunken_splur_aftermath")

    elif M_diane.is_state(S_diane_clean_garden):
        jump expression game.dialog_select("garden_diane_clean_garden")

    elif M_diane.is_state(S_diane_check_up_on_garden, S_diane_look_in_kitchen):
        call expression game.dialog_select("garden_diane_check_up")

    elif M_diane.is_state(S_diane_gardening_help):
        call expression game.dialog_select("garden_diane_gardening_help")
        $ M_diane.trigger(T_diane_help_her)

    elif M_diane.is_state(S_diane_milking_help):
        call expression game.dialog_select("diane_milk_jug_pain")

    elif game.timer.is_dark():
        call expression game.dialog_select("night_closed_garden")
    else:

        jump expression game.dialog_select("garden_listing")
    $ game.main()

label garden_shed_transition:
    if M_diane.finished_state(S_diane_debbie_drop_off) or not L_diane_shed.is_here(M_diane):
        jump shed
    else:
        jump aunt_button_dialogue

label dianes_garden_dialogue:
    $ player.go_to(L_diane_garden)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if game.timer.is_day():
        if L_diane_garden.first_visit:
            call expression game.dialog_select("diane_garden_first_time")
            $ M_diane.trigger(T_diane_need_shovel)
            $ L_diane_garden.visited()

        elif M_diane.is_state(S_diane_need_shovel):
            if player.has_item("shovel"):
                call expression game.dialog_select("diane_garden_need_shovel_has_shovel")
                $ M_diane.trigger(T_diane_has_shovel)
            else:
                call expression game.dialog_select("diane_garden_need_shovel_no_shovel")

        elif M_diane.is_state(S_diane_delivery_1_task):
            call expression game.dialog_select("diane_garden_delivery_1_task")
            show screen popup("boxes/popup_item_milk.png")
            pause
            hide screen popup
            $ L_pizzeria_exterior.unlock()
            $ M_diane.trigger(T_diane_get_delivery_task)

        elif M_diane.is_state(S_diane_wheelbarrow, S_diane_wheelbarrow_retry):
            if M_diane.is_state(S_diane_wheelbarrow):
                call expression game.dialog_select("dianes_garden_diane_need_shovel_remove_waste")
            else:
                call expression game.dialog_select("dianes_garden_diane_need_shovel_remove_waste_repeat")

            if player.stats.str() < 2:
                call expression game.dialog_select("dianes_garden_diane_need_shovel_remove_waste_fail")
                $ M_diane.trigger(T_diane_wheelbarrow_strength_fail)
            else:
                call expression game.dialog_select("dianes_garden_diane_need_shovel_remove_waste_pass")
                $ M_diane.trigger(T_diane_wheelbarrow_strength_pass)
                $ game.timer.tick(2)

        elif M_diane.is_state(S_diane_drunken_splur):
            call expression game.dialog_select("dianes_garden_diane_drunken_splur")
            $ M_diane.trigger(T_diane_help_carry_to_bed)
            $ player.go_to(L_diane_home)

        elif M_diane.is_state(S_diane_bug_infested_garden):
            call expression game.dialog_select("dianes_garden_diane_bug_infestation")
            $ M_diane.trigger(T_diane_fix_infested_garden)

        elif M_diane.is_state(S_diane_clear_bug_infested_garden):
            call expression game.dialog_select("dianes_garden_diane_clear_bug_infested_garden")

        elif M_diane.is_state(S_diane_check_up_on_garden):
            call expression game.dialog_select("dianes_garden_diane_check_up_on_garden")
            $ M_diane.trigger(T_diane_check_on_garden)

        elif M_diane.is_state(S_diane_pump_request):
            call expression game.dialog_select("dianes_garden_diane_pump_request")
            $ M_diane.trigger(T_diane_find_pump)

        elif M_diane.is_state(S_diane_delivery_2_task):
            call expression game.dialog_select("dianes_garden_diane_delivery_2_task")
            $ M_diane.trigger(T_diane_get_delivery_2_task)

        elif M_diane.is_state(S_diane_d9_intro):
            call expression game.dialog_select("dianes_garden_diane_d9_intro")
            $ M_diane.trigger(T_diane_getting_sleep)
            $ game.main()

        elif M_diane.is_state(S_diane_ready_for_day_off):
            call expression game.dialog_select("dianes_garden_diane_ready_for_day_off")
            $ M_diane.trigger(T_diane_dump_pump)

        elif M_diane.is_state(S_diane_drunken_shenanigans_apology):
            call expression game.dialog_select("dianes_garden_diane_drunken_shenanigans_apology")
            $ M_diane.trigger(T_diane_apologizing)

        elif M_diane.is_state(S_diane_delivery_3_task) and not game.timer.is_weekend():
            call expression game.dialog_select("dianes_garden_diane_delivery_3_task_week")
            $ M_diane.trigger(T_diane_get_delivery_3_task)

        elif M_diane.is_state(S_diane_delivery_3_done):
            call expression game.dialog_select("dianes_garden_diane_delivery_3_done")
            $ M_diane.trigger(T_diane_delivery_3_report_back)

        elif M_diane.is_state(S_diane_find_carpenter):
            call expression game.dialog_select("dianes_garden_diane_find_carpenter")
            $ M_diane.trigger(T_diane_found_carpenter)
    else:

        if M_diane.is_state(S_diane_debbie_drop_off):
            call expression game.dialog_select("dianes_garden_shed_light_on")
            $ M_diane.trigger(T_diane_house_locked)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
