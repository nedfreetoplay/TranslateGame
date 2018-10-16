label erik_button_dialogue:
    if M_bissette.get_state() in [S_bissette_jane_return_books, S_bissette_got_dexters_book,
                                  S_bissette_got_dexters_martinez_books, S_bissette_got_martinez_book,
                                  S_bissette_got_martinez_dexters_books
                                 ] and not M_bissette.is_set("eriks book search"):
        if player.location == L_erikhouse_basement:
            scene location_erik_basement01_closeup

        elif player.location == L_erikhouse_erikroom:
            scene expression game.timer.image("eriks_room{}_c")

        elif player.location == L_school_cafeteria:
            scene expression game.timer.image("backgrounds/location_school_cafeteria{}_blur.jpg")

        elif player.location == L_school_scienceclassroom:
            scene expression game.timer.image("backgrounds/location_school_science{}_blur.jpg")
        call erik_book_return
        $ M_bissette.set("eriks book search", True)
        $ game.main()

    if not erik.known(erik_card_hunt) and player.location == L_erikhouse_basement:
        call expression game.dialog_select("erik_card_hunt")
        $ erik.add_event(erik_card_hunt)
        $ M_erik.unforce()
        $ game.main()

    if erik.over(erik_crown_card) and not erik.known(erik_orcette) and player.location == L_erikhouse_basement:
        jump erik_orcette

    if player.location.is_here(M_june):
        scene expression "backgrounds/location_erik_house_bedroom_bed_june_day.jpg" with hpunch
        player_name "!!!"
        $ player.go_to(L_erikhouse_entrance)
        $ erik_funky = True
        jump erik_funky_block

    if player.location == L_erikhouse_basement:
        scene location_erik_basement01_closeup

    elif player.location == L_erikhouse_erikroom:
        if erik.started(erik_gf):
            scene expression game.timer.image("erik_house_bedroom{}_b")
            show player 14
            with dissolve
            player_name "Он выглядит таким счастливым сейчас."
            show player 17
            player_name "Я должен пойти и сказать {b}Миссис Джонсон{/b} о хорошей новости!"
            hide player with dissolve
            $ game.main()

        elif erik.in_progress(erik_gf_stolen):
            scene expression game.timer.image("erik_house_bedroom{}_b")
            show player 10
            with dissolve
            player_name "Наверное, он сейчас не в лучшем настроении..."
            player_name "Я поговорю с ним завтра."
            hide player with dissolve
            $ game.main()
        scene expression game.timer.image("eriks_room{}_c")

    elif player.location == L_school_scienceclassroom:
        scene school_science_c02

    elif player.location == L_school_cafeteria:
        scene expression game.timer.image("backgrounds/location_school_cafeteria{}_blur.jpg")

    show erik 1 at right
    if player.location == L_school_scienceclassroom:
        show erikl 1f at right
    show player 2 at left
    with dissolve
    player_name "Привет {b}Эрик{/b}!"
    show player 1 at left
    show erik 5 at right
    eri "Привет {b}[firstname]{/b}! Что случилось?"
    label erik_talk:
        menu:
            "Мастер Бластер." if M_okita.is_state(S_okita_get_controller_info):
                call expression game.dialog_select("button_erik_master_blaster")
                $ M_okita.trigger(T_okita_got_master_blaster_info)

            "Мастер Бластер." if M_okita.is_state(S_okita_get_controller):
                call expression game.dialog_select("button_erik_master_blaster_again")

            "Флейта." if M_dewitt.is_state(S_dewitt_make_new_flute):
                call expression game.dialog_select("button_erik_make_flute")

            "Шоу талантов." if M_dewitt.is_set("talent ask erik"):
                if M_dewitt.is_set("talent helping kevin"):
                    call expression game.dialog_select("dewitt_talent_show_helping_kevin")

                elif M_dewitt.is_set("talent helping eve"):
                    call expression game.dialog_select("dewitt_talent_show_helping_eve")
                else:

                    call expression game.dialog_select("button_erik_talent_show")
                    $ M_dewitt.set("talent ask erik", False)

            "Гитара." if M_dewitt.is_state([S_dewitt_erik_borrow_guitar, S_dewitt_garage_find_paint, S_dewitt_ask_deb_paint, S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint, S_dewitt_make_replacement_guitar]):
                if M_dewitt.is_state(S_dewitt_erik_borrow_guitar):
                    call expression game.dialog_select("button_erik_borrow_guitar")
                    if shed_unlocked:
                        $ M_dewitt.trigger(T_dewitt_eriks_agreement_shed)
                    else:
                        $ M_dewitt.trigger(T_dewitt_eriks_agreement_no_shed)
                else:

                    call expression game.dialog_select("button_erik_make_guitar")
                    if shed_unlocked:
                        $ M_dewitt.trigger(T_dewitt_eriks_agreement_shed)
                    else:
                        $ M_dewitt.trigger(T_dewitt_eriks_agreement_no_shed)

            "Пиво." if M_dewitt.is_state([S_dewitt_erik_get_beer, S_dewitt_clean_graffiti]):
                call expression game.dialog_select("button_erik_ask_beer")
                $ M_dewitt.trigger(T_dewitt_erik_deal)

            "Напитки для {b}Рокси{/b}" if M_roxxy.get("talked to roxxy booze"):
                call expression game.dialog_select("button_erik_talked_to_roxxy_booze")
                $ M_roxxy.trigger(T_roxxy_get_beer)

            "Нужна твоя помощь." if M_dewitt.is_state(S_dewitt_school_sneak_mission_help):
                call expression game.dialog_select("button_erik_school_sneak_mission_help")
                $ M_dewitt.trigger(T_dewitt_erik_deal)

            "Модель." if M_ross.is_state(S_ross_ask_model):
                call expression game.dialog_select("button_erik_ask_model")

            "Карты." if erik.started(erik_card_hunt):
                call expression game.dialog_select("erik_cards")

            "Петух с шиповоной короной ." if erik.started(erik_crown_card):
                jump erik_crown_card

            "Пакет." if erik.started(erik_orcette) or erik.started(erik_orcette_2):
                jump erik_package

            "Гарнитура VR." if erik.started(erik_vr):
                jump erik_vr_game

            "Книга из библиотеки." if M_bissette.is_set("eriks book search"):
                call erik_book_return

            "Половое воспитание." if mrsj.started(mrsj_sex_ed):
                call expression game.dialog_select("button_erik_sex_ed")

            "Подруга." if June.completed(june_erik_help) and not erik.known(erik_gf):
                call expression game.dialog_select("button_erik_girlfriend")
                $ erik.add_event(erik_gf)

            "Подруга." if June.completed(june_mc_help) and not erik.known(erik_gf_stolen):
                call expression game.dialog_select("button_erik_girlfriend_stolen")
                $ erik.add_event(erik_gf_stolen)
                $ erik_gf_stolen.finish()

            "Подруга." if June.completed(june_intro) and not June.known(june_intro_2):
                call expression game.dialog_select("button_erik_girlfriend_intro")
                $ June.add_event(june_intro_2)
                jump erik_talk

            "Сообщение от {b}Миссис Джонсон{/b}." if erik.started(erik_father_forgive):
                call expression game.dialog_select("button_erik_message_from_dad")
                $ erik_father_forgive.finish()

            "{b}Миссис Джонсон{/b}." if erik.over(erik_breastfeeding_2) and not erik.completed(erik_path_split):
                if mrsj.completed(mrsj_poker_night_2) and not erik.known(erik_path_split):
                    call expression game.dialog_select("button_erik_mrsj_poker_lost")
                    $ erik.add_event(erik_path_split)
                    jump erik_talk

                elif erik.started(erik_path_split):
                    call expression game.dialog_select("button_erik_path_split")
                    jump erik_talk
                else:

                    call expression game.dialog_select("button_erik_breastfeeding_in_person")

            "У меня есть игра!" if erik.completed(erik_favor) and player.has_item("game") and not erik.known(erik_favor_2):
                call expression game.dialog_select("button_erik_favor_completed")
                $ player.remove_item("game")
                $ erik.add_event(erik_favor_2)
                jump erik_talk

            "Мне нужна помощь." if erik.started(erik_favor):
                call expression game.dialog_select("button_erik_ask_favor")
                $ erik_favor.finish()
                jump erik_talk
            "Где {b}Миссис Джонсон{/b}?":

                call expression game.dialog_select("button_erik_where_is_mrsj")
            "Не многое.": #

                call expression game.dialog_select("button_erik_not_much")

            "Мне нужна помощь." if False:
                call expression game.dialog_select("button_erik_webcam_help")
                $ M_erik.set("webcam help", True)
    hide erikl
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
