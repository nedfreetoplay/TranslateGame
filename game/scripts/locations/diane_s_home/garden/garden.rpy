label garden_dialogue:
    $ player.go_to(L_diane_garden)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if not game.timer.is_dark():
        if aunt_shed_scene and not aunt.known(aunt_drunken_splur):
            call expression game.dialog_select("dianes_garden_diane_drunken_splur_not_known")

            $ aunt.add_event(aunt_drunken_splur)

        elif quest09_3 and not aunt.known(aunt_mouse_attack):
            call expression game.dialog_select("dianes_garden_diane_mouse_attack_not_known")

            $ aunt.add_event(aunt_mouse_attack)

        elif aunt_count == 0 and not aunt_dialogue_advance:
            if in_garden:
                $ in_garden = False
                $ game.main()

            if quest20 not in quest_list:
                call expression game.dialog_select("dianes_garden_diane_need_shovel")
                $ quest_list.append(quest20)

                if not player.has_item("shovel"):
                    call expression game.dialog_select("dianes_garden_diane_need_shovel_no_shovel")
                else:

                    call expression game.dialog_select("dianes_garden_diane_need_shovel_have_shovel")
                    call expression game.dialog_select("dianes_garden_diane_have_shovel")
                    $ L_bank.unlock()
                    $ aunt_dialogue_advance = True
                    $ completed_quests.append(quest20)
                    $ game.main()

        elif aunt_count == 1 and quest21 not in completed_quests and garden_done >= 3:
            if in_garden:
                $ in_garden = False
                $ game.main()

            scene location_diane_garden_day_blur
            if quest21 in quest_list:
                call expression game.dialog_select("dianes_garden_diane_need_shovel_remove_waste_repeat")
            else:

                call expression game.dialog_select("dianes_garden_diane_need_shovel_remove_waste")
                $ quest_list.append(quest21)

            if player.stats.str() >= 2:
                call expression game.dialog_select("dianes_garden_diane_need_shovel_remove_waste_pass")
                $ completed_quests.append(quest21)
                $ aunt_dialogue_advance = True
            else:

                call expression game.dialog_select("dianes_garden_diane_need_shovel_remove_waste_fail")

        elif aunt_count == 2 and quest08 not in quest_list:
            if in_garden:
                $ in_garden = False
                $ game.main()
            call expression game.dialog_select("dianes_garden_diane_retrieve_pump")
            $ shed_unlocked = True
            $ quest_list.append(quest08)

        elif aunt_count == 3 and not aunt_dialogue_advance and quest09 not in quest_list:
            if not game.timer.is_weekend():
                if in_garden:
                    $ in_garden = False
                    $ game.main()
                call expression game.dialog_select("dianes_garden_diane_milk_delivery_week")
                $ quest_list.append(quest09)
                $ M_annie.place(place = L_school_cafeteria)
                $ M_annie.force(tod = [0,1])
            else:


                call expression game.dialog_select("dianes_garden_diane_milk_delivery_weekend")

        elif aunt_count == 4 and not aunt_dialogue_advance and quest10 not in quest_list:
            if quest10 in quest_list and not infestation_done:
                scene garden_dead with None
            else:

                scene garden with None
            call expression game.dialog_select("dianes_garden_diane_bug_infestation")
            $ quest_list.append(quest10)

        elif aunt_count == 5 and not aunt_dialogue_advance:
            if in_garden:
                $ in_garden = False
                $ game.main()
            call expression game.dialog_select("dianes_garden_diane_missing")


        elif aunt_count == 6 and not aunt_dialogue_advance:
            if in_garden:
                $ in_garden = False
                $ game.main()
            label dianes_garden_diane_sunbathing_replay:
                call expression game.dialog_select("dianes_garden_diane_sunbathing")
            menu:
                "Конечно!":
                    call expression game.dialog_select("dianes_garden_diane_sunbathing_okay")
                    $ renpy.end_replay()
                    $ persistent.cookie_jar["Diane"]["unlocked"] = True
                    $ persistent.cookie_jar["Diane"]["gallery"]["01_unlocked"] = True
                    $ drunk_dialogue = True
                    $ aunt_dialogue_advance = True
                    call expression game.dialog_select("map_dialogue")

                "Я бы предпочел этого не делать." if store._in_replay == None:
                    call expression game.dialog_select("dianes_garden_diane_sunbathing_leave")
                    $ game.main()

        elif aunt_count == 6 and aunt_dialogue_advance and drunk_dialogue:
            call expression game.dialog_select("dianes_garden_diane_do_not_disturb")
            call expression game.dialog_select("map_dialogue")

        elif aunt_count == 7 and not aunt_apology_seen:
            if in_garden:
                $ in_garden = False
                $ game.main()

            if drunk_dialogue:
                call expression game.dialog_select("dianes_garden_diane_drunk_apology")
                $ aunt_apology_seen = True
                $ game.main()
        else:

            if aunt_count < 8 and aunt_count != 5:
                if in_garden:
                    $ in_garden = False
                    $ game.main()

                if quest10 in quest_list and not infestation_done:
                    scene garden_dead
                else:
                    scene garden
                call expression game.dialog_select("dianes_garden_diane_gardening_help")
            $ game.main()
    else:

        if quest09 in completed_quests and not aunt_shed_scene and aunt_count < 8:
            if quest10 in quest_list and not infestation_done:
                scene garden_dead_night
            else:

                scene garden_night
            call expression game.dialog_select("dianes_garden_diane_shed_still_open")
        else:

            if aunt_count < 8:
                call expression game.dialog_select("night_closed_garden")
    $ game.main()

label aunt_button_dialogue:
    if aunt_drink_made:
        $ aunt_drink_made = False
        $ aunt_drink_offered = False
        label dianes_dialogue_drink_replay:
            call expression game.dialog_select("dianes_dialogue_drink")
        if not store._in_replay == None or aunt_extra_shot:
            call expression game.dialog_select("dianes_dialogue_drink_extra_shot")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Diane"]["unlocked"] = True
            $ persistent.cookie_jar["Diane"]["gallery"]["02_unlocked"] = True

            $ in_garden = True
            $ aunt_extra_shot = False
            $ aunt_drink_active = False
            $ aunt_dialogue_advance = True
            call expression game.dialog_select("garden_dialogue")
        else:
            $ game.main()

    elif aunt_count < 8:
        call expression game.dialog_select("dianes_dialogue_pre_fun_intro")
        menu dia_default_dialogue_options:
            "Говорить.":
                call expression game.dialog_select("dianes_dialogue_pre_fun_talk")
                call expression game.dialog_select("dia_default_dialogue_options")

            "Краска." if M_dewitt.is_state([S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint]):
                call expression game.dialog_select("dianes_dialogue_pre_fun_paint")
                $ M_dewitt.trigger(T_dewitt_shed_paint)

            "Я нашёл лопату." if quest20 in quest_list and quest20 not in completed_quests and player.has_item("shovel"):
                call expression game.dialog_select("dianes_dialogue_pre_fun_found_shovel")
                call expression game.dialog_select("dianes_garden_diane_have_shovel")
                $ L_bank.unlock()
                $ aunt_dialogue_advance = True
                $ completed_quests.append(quest20)
                $ game.main()

            "Сад." if quest20 in completed_quests:
                call expression game.dialog_select("dianes_dialogue_pre_fun_remove_waste")
                call expression game.dialog_select("dia_default_dialogue_options")

            "Насос." if quest08 in quest_list and quest08 not in completed_quests:
                call expression game.dialog_select("dianes_dialogue_pre_fun_pump_intro")
                menu:
                    "Где он находится?":
                        call expression game.dialog_select("dianes_dialogue_pre_fun_pump_location")
                        call expression game.dialog_select("dia_default_dialogue_options")
                    "Ещё.":

                        call expression game.dialog_select("dianes_dialogue_pre_fun_pump_not_yet")
                        call expression game.dialog_select("dia_default_dialogue_options")

                    "Я нашел его!" if player.has_item("pump"):
                        call expression game.dialog_select("dianes_dialogue_pre_fun_pump_found")
                        $ player.remove_item("pump")
                        $ quest_complete(quest08)
                        $ aunt_dialogue_advance = True

            "Доставка молока." if quest09 in quest_list and quest09 not in completed_quests:
                call expression game.dialog_select("dianes_dialogue_pre_fun_milk_delivery_intro")
                menu:
                    "А где в школе?":
                        call expression game.dialog_select("dianes_dialogue_pre_fun_milk_delivery_location")
                        call expression game.dialog_select("dia_default_dialogue_options")
                    "Ещё.":

                        call expression game.dialog_select("dianes_dialogue_pre_fun_milk_delivery_not_yet")
                        call expression game.dialog_select("dia_default_dialogue_options")

                    "Я доставил их!" if quest09_3:
                        call expression game.dialog_select("dianes_dialogue_pre_fun_milk_delivery_delivered")
                        menu:
                            "Конечно!":
                                call expression game.dialog_select("dianes_dialogue_pre_fun_milk_delivery_try_milk")
                                $ M_player.set("drank milk", True)
                            "Мне не нравится молоко.":

                                call expression game.dialog_select("dianes_dialogue_pre_fun_milk_delivery_do_not_try_milk")
                        $ drink_milk_offer = True
                        $ game.timer.tick()
                        $ completed_quests.append(quest09)
                        $ M_annie.unforce()
                        $ aunt_dialogue_advance = True
                        $ quest09_3 = False

            "Клопов." if quest10 in quest_list and not infestation_done:
                call expression game.dialog_select("dianes_dialogue_pre_fun_bug_infestation_intro")
                menu:
                    "Что мне следует делать?":
                        call expression game.dialog_select("dianes_dialogue_pre_fun_bug_infestation_task")
                        call expression game.dialog_select("dia_default_dialogue_options")
                    "Ещё.":

                        call expression game.dialog_select("dianes_dialogue_pre_fun_bug_infestation_not_done")
                        call expression game.dialog_select("dia_default_dialogue_options")

                    "Я от них избавился!" if infestation_done:
                        call expression game.dialog_select("dianes_dialogue_pre_fun_bug_infestation_done")
                        $ aunt_dialogue_advance = True
                        $ completed_quests.append(quest10)

            "Сделать напиток." if aunt_count == 6 and not aunt_dialogue_advance or aunt_count == 7 and not aunt_dialogue_advance:
                if player.stats.chr() >= 5:
                    call expression game.dialog_select("dianes_dialogue_pre_fun_make_drink_pass")
                    $ aunt_drink_offered = True
                    $ aunt_drink_active = True
                else:

                    call expression game.dialog_select("dianes_dialogue_pre_fun_make_drink_fail")
            "Мне нужно работать.":

                call expression game.dialog_select("dianes_dialogue_pre_fun_leave")
        $ game.main()

    elif aunt_count >= 8:
        call expression game.dialog_select("dianes_dialogue_after_fun_intro")
        menu dia_default_dialogue_options_kitchen:
            "Говорить.":
                call expression game.dialog_select("dianes_dialogue_after_fun_talk")
                call expression game.dialog_select("dia_default_dialogue_options_kitchen")
            "О чем говорить {b}[deb_name]{/b}.":

                call expression game.dialog_select("dianes_dialogue_after_fun_talk_about_debbie_intro")
                menu:
                    "Да.":
                        call expression game.dialog_select("dianes_dialogue_after_fun_talk_about_debbie_confess")
                        call expression game.dialog_select("dia_default_dialogue_options_kitchen")
                    "Нет.":

                        call expression game.dialog_select("dianes_dialogue_after_fun_talk_about_debbie_do_not_confess")
                        call expression game.dialog_select("dia_default_dialogue_options_kitchen")

            "Краска." if M_dewitt.is_state([S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint]):
                call expression game.dialog_select("dianes_dialogue_pre_fun_paint")
                $ M_dewitt.trigger(T_dewitt_shed_paint)

            "Производство молока." if not aunt.known(aunt_breeding_guide):
                call expression game.dialog_select("dianes_dialogue_after_fun_diane_breeding_guide_not_known")
                $ quest_list.append(quest12)
                $ aunt.add_event(aunt_breeding_guide)

            "Молочный кувшин." if quest12 in quest_list and quest12 not in completed_quests and not player.has_item("milkjug"):
                call expression game.dialog_select("dianes_dialogue_after_fun_do_not_have_milkjug")

            "Молочный кувшин." if quest12 in quest_list and quest12 not in completed_quests and player.has_item("milkjug"):
                call expression game.dialog_select("dianes_dialogue_after_fun_have_milkjug")
                $ player.remove_item("milkjug")
                $ completed_quests.append(quest12)

            "Книга по производству молока." if aunt.known(aunt_breeding_guide) and player.has_item("breeding_guide") and not aunt.known(aunt_breeding_bull):
                call expression game.dialog_select("dianes_dialogue_after_fun_have_breeding_guide")
                $ aunt.add_event(aunt_breeding_bull)
                $ player.remove_item("breeding_guide")
                call expression game.dialog_select("garden_dialogue")

            "Разведение." if aunt.over(aunt_breeding_bull) and not aunt.known(aunt_breeding_help):
                call expression game.dialog_select("dianes_dialogue_after_fun_diane_breeding_help_not_known_intro")
                menu:
                    "Тебя!" if player.stats.chr() < 7:
                        call expression game.dialog_select("dianes_dialogue_after_fun_diane_breeding_help_not_known_fail")
                        call expression game.dialog_select("dia_default_dialogue_options_kitchen")

                    "Тебя!" if player.stats.chr() >= 7:
                        call expression game.dialog_select("dianes_dialogue_after_fun_diane_breeding_help_not_known_pass")
                        $ aunt.add_event(aunt_breeding_help)
                    "Ещё.":

                        call expression game.dialog_select("dianes_dialogue_after_fun_diane_breeding_help_not_known_leave")
            "Повеселиться.":

                label dianes_dialogue_after_fun_have_fun_replay:
                    call expression game.dialog_select("dianes_dialogue_after_fun_have_fun")
                if store._in_replay == None and not aunt_had_sex:
                    call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_first_time")
                    menu:
                        "Да.":
                            call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_first_time_yes")
                            menu dia_sex_options:
                                "Я хочу тебя." if player.stats.chr() < 7:
                                    call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_first_time_want_fail")
                                    call expression game.dialog_select("dia_sex_options")

                                "Я хочу тебя." if player.stats.chr() >= 7:
                                    call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_first_time_want_pass")
                                    $ M_aunt.set("sex speed", .4)
                                    call expression game.dialog_select("aunt_sex_loop")
                                "Сделать больше.":

                                    call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_first_time_more")
                else:

                    call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_repeat")
                    $ anim_toggle = False
                    $ xray_toggle = False
                    $ M_aunt.set("sex speed", .4)
                    menu dia_sex_options_2:
                        "Поиграй с клитором.":
                            call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_repeat_clit_play")
                            call expression game.dialog_select("dia_sex_options_2")
                        "Играть с овощами.":

                            call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_repeat_vegetable_play")
                            call expression game.dialog_select("dia_sex_options_2")
                        "Ебать без Презерватива.":

                            call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_repeat_raw_sex")
                            $ condom_on = False
                            call expression game.dialog_select("aunt_sex_loop")
                        "Ебать с Презервативом.":

                            call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_repeat_safe_sex")
                            $ condom_on = True
                            call expression game.dialog_select("aunt_sex_loop")
            "Мне пора идти.":

                call expression game.dialog_select("dianes_dialogue_after_fun_have_fun_repeat_leave")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
