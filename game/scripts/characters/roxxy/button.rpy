label roxxy_classroom_dialogue:
    scene french_class_c
    if M_roxxy.is_state(S_roxxy_get_evidence):
        call expression game.dialog_select("button_roxxy_get_evidence")
        $ game.main()

    elif M_roxxy.is_state(S_roxxy_lolipop_for_lolipop, S_roxxy_lolipop_just_once):
        if player.has_item("roxxy_homework"):
            if M_roxxy.is_state(S_roxxy_lolipop_for_lolipop):
                call expression game.dialog_select("button_roxxy_lolipop_for_lolipop")
            elif M_roxxy.is_state(S_roxxy_lolipop_just_once):
                call expression game.dialog_select("button_roxxy_lolipop_just_once")
            call expression game.dialog_select("button_roxxy_lolipop_cutscene")
            $ player.remove_item("roxxy_homework")
            $ game.timer.tick()

            $ M_roxxy.trigger(T_roxxy_confrontation)
            $ player.go_to(L_school_hall)
            $ game.main()
        else:
            call expression game.dialog_select("button_roxxy_get_homework_locker")

    elif M_bissette.is_state(S_bissette_roxxy_exam_convince):
        if not M_roxxy.get("roxxy trailer sex"):
            call expression game.dialog_select("roxxy_dialogue_exam_convince")
        else:
            call expression game.dialog_select("roxxy_dialogue_exam_convince_roxxy_sex")
        $ M_bissette.trigger(T_bissette_roxxy_deal)

    elif M_bissette.is_state(S_bissette_roxxy_pom_poms):
        if not M_roxxy.get("roxxy trailer sex"):
            call expression game.dialog_select("roxxy_dialogue_pom_poms")
        else:
            call expression game.dialog_select("roxxy_dialogue_pom_poms_sex")

    elif M_bissette.is_state(S_bissette_roxxy_pom_poms_deal):
        if not M_roxxy.get("roxxy trailer sex"):
            call expression game.dialog_select("roxxy_dialogue_pom_poms_deal")
        else:
            call expression game.dialog_select("roxxy_dialogue_pom_poms_deal_sex")
        $ M_bissette.trigger(T_bissette_roxxy_deal)
        $ player.remove_item("pompoms")

    elif M_bissette.is_state([S_bissette_roxxy_cheerleader_deal, S_bissette_jenny_mentoring_payment]):
        if not M_roxxy.get("roxxy trailer sex"):
            call expression game.dialog_select("roxxy_dialogue_cheerleader_deal")
        else:
            call expression game.dialog_select("roxxy_dialogue_cheerleader_deal_sex")

    elif M_bissette.is_state(S_bissette_roxxy_deal_confirmation):
        if not M_roxxy.get("roxxy trailer sex"):
            call expression game.dialog_select("roxxy_dialogue_deal_confirmation")
        else:
            call expression game.dialog_select("roxxy_dialogue_deal_confirmation_sex")
        $ M_bissette.trigger(T_bissette_roxxy_meet_inform)

    elif M_roxxy.is_state(S_roxxy_get_fake_id):
        if M_roxxy.get("talked to roxxy id"):
            call expression game.dialog_select("button_roxxy_get_fake_id")
        else:
            call expression game.dialog_select("button_roxxy_get_fake_id_first")
            $ M_roxxy.set("talked to roxxy id", True)

    elif M_roxxy.is_state(S_roxxy_fake_id_ask_terry):
        call expression game.dialog_select("button_roxxy_fake_id_ask_terry")
        $ M_roxxy.set("take roxxy mall", True)
        $ player.go_to(L_map)
        $ game.main()

    elif M_roxxy.is_state(S_roxxy_fake_id_get_picture):
        call expression game.dialog_select("button_roxxy_fake_id_get_picture")
    else:

        if M_roxxy.get("roxxy relationship") == 0:
            call expression game.dialog_select("french_roxxy_dialogue_relationship_0")
            $ game.main()
        call expression game.dialog_select("french_roxxy_dialogue_relationship_{}".format(M_roxxy.get("roxxy relationship")))
        menu:
            "Модель." if M_ross.is_state(S_ross_ask_model):
                call expression game.dialog_select("roxxy_dialogue_ask_model")

            "Шоу талантов." if M_dewitt.is_set("talent ask roxxy"):
                if M_dewitt.is_set("talent helping kevin"):
                    call expression game.dialog_select("dewitt_talent_show_helping_kevin")

                elif M_dewitt.is_set("talent helping eve"):
                    call expression game.dialog_select("dewitt_talent_show_helping_eve")
                else:

                    call expression game.dialog_select("roxxy_dialogue_talent_show_help")
                    $ M_dewitt.set("talent ask roxxy", False)

            "Как у тебя дела?" if M_roxxy.is_state(S_roxxy_hows_it_going):
                call expression game.dialog_select("button_roxxy_hows_it_going")
                $ M_roxxy.trigger(T_roxxy_chat_with_becca_missy)

            "Как дела?" if not M_roxxy.is_state(S_roxxy_hows_it_going) and M_roxxy.get("roxxy relationship") in (1,2):
                call expression game.dialog_select("button_roxxy_hows_it_going_relationship_{}".format(M_roxxy.get("roxxy relationship")))

            "Экзамены." if M_roxxy.is_state(S_roxxy_sneak_into_smith):
                call expression game.dialog_select("button_roxxy_sneak_into_smith")

            "Выпивка." if M_roxxy.is_state(S_roxxy_need_booze):
                if M_roxxy.get("talked to roxxy booze"):
                    call expression game.dialog_select("button_roxxy_need_booze")
                else:
                    call expression game.dialog_select("button_roxxy_need_booze_first")
                    $ M_roxxy.set("talked to roxxy booze", True)

            "Есть новости от {b}Клайда{/b}?" if M_roxxy.get("roxxy relationship") not in (3,4) and M_roxxy.finished_state(S_roxxy_shut_down_lab):
                call expression game.dialog_select("button_roxxy_french_whats_up_clyde_relationship_2")

            "Что случилось с {b}Клайдом{/b}?" if M_roxxy.get("roxxy relationship") in (3,4):
                call expression game.dialog_select("button_roxxy_french_whats_up_clyde_relationship_{}".format(M_roxxy.get("roxxy relationship")))

            "Встретимся у моего шкафчика." if M_roxxy.get("roxxy locker sex") and not M_roxxy.is_set("meet for locker sex"):
                call expression game.dialog_select("button_roxxy_meet_me_at_my_locker")
                $ M_roxxy.set("meet for locker sex", True)

            "Увидимся сегодня ночью." if M_roxxy.get("roxxy relationship") == 4:
                call expression game.dialog_select("button_roxxy_ill_see_you_tonight")

            "Ничего." if M_roxxy.get("roxxy relationship")<=2:
                call expression game.dialog_select("french_roxxy_dialogue_leave_relationship_{}".format(M_roxxy.get("roxxy relationship")))

            "Я буду в порядке." if M_roxxy.get("roxxy relationship")==3:
                call expression game.dialog_select("french_roxxy_dialogue_leave_relationship_{}".format(M_roxxy.get("roxxy relationship")))

            "Мне нужно идти." if M_roxxy.get("roxxy relationship")==4:
                call expression game.dialog_select("french_roxxy_dialogue_leave_relationship_{}".format(M_roxxy.get("roxxy relationship")))
    hide roxxy
    hide player
    with dissolve
    $ game.main()

label roxxy_third_floor_dialogue:
    if M_roxxy.is_state(S_roxxy_teachers_event):
        call expression game.dialog_select("button_roxxy_intro")
        $ M_roxxy.trigger(T_roxxy_locker_room)
    $ game.main()

label roxxy_trailer_button_dialogue:
    scene expression player.location.background_blur
    if M_roxxy.get("roxxy relationship") == 0:
        call expression game.dialog_select("home_roxxy_dialogue_relationship_0")
        $ game.main()
    call expression game.dialog_select("home_roxxy_dialogue_relationship_{}".format(M_roxxy.get("roxxy relationship")))
    menu:
        "Хочешь потусоваться?" if M_roxxy.get("roxxy relationship") == 1:
            call expression game.dialog_select("button_roxxy_home_hang_out")

        "Что-нибудь слышно от {b}Клайда{/b}?" if M_roxxy.get("roxxy relationship") == 2:
            call expression game.dialog_select("button_roxxy_french_whats_up_clyde_relationship_{}".format(M_roxxy.get("roxxy relationship")))

        "Как поживаешь?" if M_roxxy.get("roxxy relationship") == 2:
            call expression game.dialog_select("button_roxxy_home_hows_it_going")

        "Что случилось с {b}Клайдом{/b}?" if M_roxxy.get("roxxy relationship") in (3,4):
            call expression game.dialog_select("button_roxxy_french_whats_up_clyde_relationship_{}".format(M_roxxy.get("roxxy relationship")))

        "Тусоваться." if M_roxxy.is_state(S_roxxy_end) and game.timer.is_dark():
            if not M_roxxy.get("roxxy trailer sex"):
                call expression game.dialog_select("button_roxxy_trailer_bed_sex_first")
            else:
                label roxxy_bedroom_fuck_hscene_replay:
                    call expression game.dialog_select("button_roxxy_trailer_bed_sex_repeat")
            $ anim_toggle = True
            $ animated = False
            $ M_roxxy.set("sex speed", .09)
            call expression game.dialog_select("button_roxxy_trailer_bed_sex_loop_pre")
            jump expression game.dialog_select("button_roxxy_trailer_bed_sex_loop")

        "Ничего." if M_roxxy.get("roxxy relationship") <= 3:
            call expression game.dialog_select("home_roxxy_dialogue_leave_relationship_{}".format(M_roxxy.get("roxxy relationship")))

        "Мне пора идти." if M_roxxy.get("roxxy relationship") == 4:
            call expression game.dialog_select("home_roxxy_dialogue_leave_relationship_{}".format(M_roxxy.get("roxxy relationship")))
    $ game.main()

label roxxy_beach_button_dialogue:
    scene expression game.timer.image("backgrounds/location_beach_water{}_blur.jpg")
    if M_roxxy.get("roxxy relationship") == 0:
        call expression game.dialog_select("beach_roxxy_dialogue_relationship_0")
        $ game.main()
    if M_roxxy.finished_state(S_roxxy_spin_bottle):
        call expression game.dialog_select("button_roxxy_beach_intro")
    else:
        call expression game.dialog_select("beach_roxxy_dialogue_relationship_{}".format(M_roxxy.get("roxxy relationship")))
    menu:
        "Я поиграю." if M_roxxy.finished_state(S_roxxy_spin_bottle):
            call expression game.dialog_select("button_roxxy_beach_spin_bottle")
            if M_roxxy.get("roxxy beach sex") or M_becca.get("becca beach sex") or M_missy.get("missy beach sex") or M_player.get("mc beach sex"):
                call expression game.dialog_select("button_roxxy_beach_spin_bottle_sex_repeat")
            $ M_player.set("beach bottle spins", 0)
            call screen spin_bottle_minigame

        "Что насчет массажа?" if M_roxxy.finished_state(S_roxxy_get_oil):
            call expression game.dialog_select("roxxy_beach_button_massage")
            $ M_roxxy.set("massage", True)

        "Не-а, не этой ночью." if M_roxxy.finished_state(S_roxxy_spin_bottle):
            call expression game.dialog_select("button_roxxy_beach_leave")

        "Ничего." if not M_roxxy.finished_state(S_roxxy_spin_bottle):
            call expression game.dialog_select("button_roxxy_beach_leave_before_spin_bottle")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
