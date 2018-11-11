label okita_button_dialogue:
    scene expression "backgrounds/location_school_science_closeup.jpg"
    if M_okita.is_state(S_okita_intro):
        call expression game.dialog_select("button_okita_intro")
        $ M_okita.trigger(T_okita_get_keycode)

    elif M_okita.is_state(S_okita_get_keycode):
        call expression game.dialog_select("button_okita_get_keycode")

    elif M_okita.is_state(S_okita_foam_misshap):
        call expression game.dialog_select("button_okita_foam_misshap")
        $ M_okita.trigger(T_okita_get_bifocal_lenses)

    elif M_okita.is_state(S_okita_get_bifocal_lenses):
        call expression game.dialog_select("button_okita_get_bifocal_lenses")

    elif M_okita.is_state(S_okita_picture_taken) and player.has_item("judith_glasses"):
        call expression game.dialog_select("science_classroom_okita_has_glasses")
        if M_okita.is_set("glasses assembly fail"):
            menu:
                "Попробовать ещё раз.":
                    call expression game.dialog_select("science_classroom_okita_has_glasses_try_again")
                "Ничего.":

                    $ game.main()

        if player.has_required_int(5):
            call expression game.dialog_select("science_classroom_okita_has_glasses_int_pass")
            $ M_okita.set("glasses assembly fail", False)
            $ player.remove_item("judith_glasses")

            $ M_okita.trigger(T_okita_xray_perved_classroom)
        else:

            call expression game.dialog_select("science_classroom_okita_has_glasses_int_fail")
            $ M_okita.set("glasses assembly fail", True)
            $ player.go_to(L_map)
            $ game.timer.tick(2)
            $ game.main()

    elif M_okita.is_state(S_okita_glasses_completed):
        call expression game.dialog_select("button_okita_get_faptic_engine")
        $ M_okita.trigger(T_okita_requested_faptic_engine)

    elif M_okita.is_state(S_okita_faptic_engine):
        call expression game.dialog_select("button_okita_get_faptic_engine_repeat")

    elif M_okita.is_state(S_okita_get_controller) and player.has_item("faptic_engine"):
        call expression game.dialog_select("science_classroom_okita_has_faptic")
        if M_okita.is_set("belt assembly fail"):
            menu:
                "Попробовать ещё раз.":
                    call expression game.dialog_select("science_classroom_okita_has_faptic_try_again")
                "Ничего.":

                    $ game.main()

        if player.has_required_int(8):
            scene expression "backgrounds/location_school_science_cutscene04.jpg"
            pause
            call expression game.dialog_select("science_classroom_okita_has_faptic_int_pass")
            $ M_okita.set("belt assembly fail", False)

            $ player.remove_item("faptic_engine")
            $ M_okita.trigger(T_okita_belt_assembled)
        else:

            scene expression "backgrounds/location_school_science_cutscene04b.jpg"
            pause
            call expression game.dialog_select("science_classroom_okita_has_faptic_int_fail")
            $ M_okita.set("belt assembly fail", True)
            $ player.go_to(L_map)
            $ game.timer.tick(2)
            $ game.main()

    elif M_okita.is_state(S_okita_tinkering_with_belt, S_okita_tinkering_with_belt_delay, S_okita_tinkering_with_belt_delay2):
        call expression game.dialog_select("button_okita_tinkering_belt")

    elif M_okita.is_state(S_okita_tinkering_with_belt_delay3):
        call expression game.dialog_select("button_okita_tinkered_belt")
        $ M_okita.trigger(T_okita_finished_tinkering_belt)
        $ game.timer.tick()
        $ player.go_to(L_school_floor3)
        $ game.main()

    elif M_okita.is_state(S_okita_tired_from_belt):
        call expression game.dialog_select("button_okita_tired_from_belt")
        $ M_okita.trigger(T_okita_get_ingredients)

    elif M_okita.is_state(S_okita_get_ingredients):
        if player.has_item("mushroom") and player.has_item("toad") and player.has_item("caveflower") and player.has_item("chicken_stock") and player.has_item("tissue"):
            call expression game.dialog_select("button_okita_got_all_ingredients")
            $ M_okita.trigger(T_okita_got_all_ingredients)
        else:

            scene location_school_science_closeup
            show player 11 at left
            show okita 2 at right
            player_name "Насчет тех предметов которые вам нужны..."
            menu okita_items:
                "Гриб." if not player.has_item("mushroom"):
                    call expression game.dialog_select("button_okita_ingredients_mushroom")

                "Похотливая Жаба." if not player.has_item("toad"):
                    call expression game.dialog_select("button_okita_ingredients_toad")

                "Цветок." if not player.has_item("caveflower"):
                    call expression game.dialog_select("button_okita_ingredients_flower")

                "Низкопробная Жидкость." if not player.has_item("chicken_stock"):
                    call expression game.dialog_select("button_okita_ingredients_stock")

                "ДНК Смит." if not player.has_item("tissue"):
                    call expression game.dialog_select("button_okita_ingredients_tissue")
                "Вот и всё.":

                    player_name "Тогда я вернусь за этими вещами."
                    $ game.main()
            jump expression game.dialog_select("okita_items")

    elif M_okita.is_state(S_okita_extract_cum):
        call expression game.dialog_select("button_okita_extract_cum")

    elif M_okita.is_state(S_okita_dose_smith):
        call expression game.dialog_select("button_okita_dose_smith")

    elif M_okita.is_state(S_okita_wait_for_smith_serum):
        call expression game.dialog_select("button_okita_wait_for_smith_serum")
        $ game.timer.tick(2)
        $ M_okita.trigger(T_okita_smith_effects_seen)

    elif M_okita.is_state(S_okita_wait_for_okita_serum, S_okita_wait_for_okita_serum_delay, S_okita_wait_for_okita_serum_delay2):
        call expression game.dialog_select("button_okita_wait_for_okita_serum")

    elif M_okita.is_state(S_okita_wait_for_okita_serum_delay3):
        call expression game.dialog_select("button_okita_serum_effects")
        $ M_okita.trigger(T_okita_serum_took_effect)

    elif M_okita.get("Q3 completed"):
        call expression game.dialog_select("button_okita_generic_after_q3")

    elif not M_okita.get("Q3 completed"):
        call expression game.dialog_select("button_okita_generic_before_q3")
    hide player
    hide okita
    hide principal
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
