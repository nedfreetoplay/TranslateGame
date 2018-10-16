label mia_button_dialogue:
    if M_helen.is_set("helen route"):
        call expression game.dialog_select("mia_dialogue_helen_route")

    elif M_mia.is_state(S_mia_helen_change_news):
        call expression game.dialog_select("mia_dialogue_helen_change_news")
        $ M_mia.trigger(T_mia_thanks)
        $ game.main()

    if player.location == L_miahouse_miaroom:
        if M_mia.is_state(S_mia_end):
            call expression game.dialog_select("mia_dialogue_mia_bedroom_mia_end_intro")
            menu:
                "Study":
                    call expression game.dialog_select("mia_dialogue_mia_bedroom_mia_end_study")
                    $ M_mia.set("sex speed", .175)
                    jump expression game.dialog_select("mia_strip_repeat")
                "I have to go.":

                    call expression game.dialog_select("mia_dialogue_mia_bedroom_mia_end_leave")
                    $ game.main()

        elif M_mia.is_state(S_mia_night_visit):
            jump expression game.dialog_select("mia_strip_show")

        elif M_mia.is_state(S_mia_tattoo_help):
            call expression game.dialog_select("mia_dialogue_mia_bedroom_mia_tattoo_help")
            $ game.timer.tick()
            $ M_mia.trigger(T_mia_delay)
            $ player.go_to(L_miahouse)
            $ game.main()

        elif M_mia.is_state(S_mia_church_plan):
            call expression game.dialog_select("mia_dialogue_mia_bedroom_mia_church_plan")
        else:

            call expression game.dialog_select("mia_dialogue_mia_bedroom_intro")

    elif player.location == L_school_scienceclassroom:
        show mial 1f zorder 2 at right
        if M_mia.is_state(S_mia_strip_aftermath):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_strip_aftermath")
            $ game.main()

        elif M_mia.is_state(S_mia_consult):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_consult")
            $ M_mia.trigger(T_mia_plan)

        elif M_mia.is_state(S_mia_parent_unblock):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_parent_unblock")
            $ M_mia.trigger(T_mia_results)
            $ game.main()

        elif M_mia.is_state(S_mia_favor):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_favor")
            $ M_mia.trigger(T_mia_dinner_plan)
            $ game.main()

        elif M_mia.is_state(S_mia_need_space):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_need_space")
            $ game.main()

        elif M_mia.is_state(S_mia_church_plan):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_church_plan")

        elif M_mia.is_state(S_mia_urgent_help):
            call expression game.dialog_select("mia_dialogue_science_classroom_mia_urgent_help")
        else:

            call expression game.dialog_select("mia_dialogue_science_classroom_intro")

    elif player.location == L_miahouse_entrance:
        if M_mia.is_state(S_mia_favor):
            call expression game.dialog_select("mia_dialogue_mias_house_entrance_mia_favor")
            $ M_mia.trigger(T_mia_dinner_plan)
            $ game.main()

        elif M_mia.is_state(S_mia_helen_talk):
            call expression game.dialog_select("mia_dialogue_mias_house_entrance_mia_helen_talk")
            $ game.main()

        elif M_mia.is_state([S_mia_church_plan, S_mia_clues]):
            call expression game.dialog_select("mia_dialogue_mias_house_entrance_mia_church_plan")
        else:

            call expression game.dialog_select("mia_dialogue_mias_house_entrance_intro")
    menu mia_dialogue:
        "Chat" if player.location == L_miahouse_miaroom:
            call expression game.dialog_select("mia_dialogue_chat")
            jump expression game.dialog_select("mia_dialogue")

        "Talent Show." if M_dewitt.is_set("talent ask mia"):
            if M_dewitt.is_set("talent helping kevin"):
                call expression game.dialog_select("dewitt_talent_show_helping_kevin")

            elif M_dewitt.is_set("talent helping eve"):
                call expression game.dialog_select("dewitt_talent_show_helping_eve")
            else:

                call expression game.dialog_select("mia_dialogue_talent_show_help")
                $ M_dewitt.set("talent ask mia", False)

        "Parents." if player.location == L_school_scienceclassroom and M_mia.between_states(S_mia_start, S_mia_helen_refusal):
            call expression game.dialog_select("mia_dialogue_parents")
            jump expression game.dialog_select("mia_dialogue")

        "{b}Harold{/b}." if M_mia.is_state(S_mia_clues):
            call expression game.dialog_select("mia_dialogue_mia_clues")

        "{b}Harold{/b}." if M_mia.is_state(S_mia_convince_harold):
            call expression game.dialog_select("mia_dialogue_mia_convince_harold")

        "Glasses." if M_mia.is_state(S_mia_harold_gift):
            call expression game.dialog_select("mia_dialogue_glasses")

        "Donuts." if M_mia.is_state(S_mia_impress_harold):
            call expression game.dialog_select("mia_dialogue_donuts")
            jump expression game.dialog_select("mia_dialogue")

        "Tattoo." if M_mia.is_state([S_mia_find_easel, S_mia_draw_tattoo]):
            call expression game.dialog_select("mia_dialogue_mia_draw_tattoo")

        "Tattoo." if list(set(["tattoo_dolphin", "tattoo_stars", "tattoo_flowers", "tattoo_skull", "tattoo_cookie"]) & set(player.inventory.items)):
            call expression game.dialog_select("mia_dialogue_mia_show_tattoo_fail")
            $ player.remove_item(drawn_tattoo)
            $ M_mia.trigger(T_mia_wrong_tattoo)

        "Tattoo." if player.has_item("tattoo_butterfly"):
            call expression game.dialog_select("mia_dialogue_mia_show_tattoo_pass")
            $ player.remove_item(drawn_tattoo)
            $ M_mia.trigger(T_mia_right_tattoo)

        "Sugar Tats" if M_mia.is_state([S_mia_get_tattoo, S_mia_buy_tattoo]):
            call expression game.dialog_select("mia_dialogue_mia_get_tattoo")

        "Church." if M_mia.is_state(S_mia_church_plan):
            call expression game.dialog_select("mia_dialogue_church")

        "Art Sessions." if player.location == L_school_scienceclassroom and M_ross.is_state(S_ross_ask_mia_partner):
            call expression game.dialog_select("mia_dialogue_art_sessions_intro")
            if player.has_required_chr(3):
                call expression game.dialog_select("mia_dialogue_art_sessions_stat_pass")
                $ M_ross.trigger(T_ross_convinced_mia)
            else:

                call expression game.dialog_select("mia_dialogue_art_sessions_stat_fail")

        "Homework." if player.location == L_school_scienceclassroom and not M_helen.is_set("helen route"):
            if not M_mia.between_states(S_mia_start, S_mia_helen_refusal) and not M_mia.is_state([S_mia_study_sex, S_mia_end]):
                call expression game.dialog_select("mia_dialogue_homework_want_parents_back")
            else:

                call expression game.dialog_select("mia_dialogue_homework_intro")
                if M_mia.is_state(S_mia_do_homework):
                    call expression game.dialog_select("mia_dialogue_homework_still_busy")
                    $ game.main()
                else:

                    call expression game.dialog_select("mia_dialogue_homework_study")
                jump expression game.dialog_select("mia_dialogue")

        "Study" if player.location == L_miahouse_miaroom and not M_helen.is_set('helen route'):
            if M_mia.is_set("study"):
                call expression game.dialog_select("mia_dialogue_study_repeat")
                $ game.timer.tick()
                $ player.go_to(L_miahouse)
                $ game.main()
            else:

                if M_mia.between_states(S_mia_start, S_mia_helen_refusal):
                    call expression game.dialog_select("mia_dialogue_study_first")
                    jump expression game.dialog_select("mia_study")
                else:

                    call expression game.dialog_select("mia_dialogue_study_want_parents_back")
                    jump expression game.dialog_select("mia_dialogue")

        "I have to go." if player.location == L_miahouse_miaroom:
            call expression game.dialog_select("mia_dialogue_mias_bedroom_leave")

        "Nothing." if player.location == L_school_scienceclassroom:
            call expression game.dialog_select("mia_dialogue_science_classroom_leave")

        "I have to go." if player.location == L_miahouse_entrance:
            call expression game.dialog_select("mia_dialogue_mias_house_entrance_leave")
    hide player
    hide mia
    hide mial
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
