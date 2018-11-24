label mom_button_dialogue:
    if M_mom.is_state(S_mom_relaxing):
        call expression game.dialog_select("debbie_dialogue_mom_relaxing")
        $ game.main()

    elif M_diane.is_state(S_diane_debbie_drop_off_request):
        call expression game.dialog_select("debbie_dialogue_diane_debbie_drop_off_request")
        $ M_diane.trigger(T_diane_debbie_request)
        $ game.main()

    elif M_mom.is_set("sleep together") and not M_mom.is_set("revealing") and player.location == L_home_kitchen:
        call expression game.dialog_select("debbie_dialogue_mom_not_revealing_kitchen")
        $ M_mom.set("revealing", True)
        $ M_mom.set("panties available", True)
        jump expression game.dialog_select("debbie_dialogue_options")

    scene expression player.location.background_blur

    if M_mom.is_set("fetch lotion") and not M_mom.is_set("retrieved lotion"):
        call expression game.dialog_select("debbie_dialogue_mom_fetch_lotion")

    elif M_mom.is_set("fetch lotion") and M_mom.is_set("retrieved lotion"):
        jump expression game.dialog_select("mom_lotion_fun")

    elif M_mom.is_state(S_mom_car_condition):
        call expression game.dialog_select("debbie_dialogue_mom_car_condition")
        $ M_mom.trigger(T_mom_deliver_car_news)
    else:

        if M_mom.is_set("revealing") and player.location == L_home_kitchen:
            call expression game.dialog_select("debbie_dialogue_mom_revealing_kitchen_pre")
            menu:
                "Взять за попку":
                    if M_mom.is_set("sex available"):
                        label mom_kitchen_replay:
                            call expression game.dialog_select("debbie_dialogue_mom_revealing_feel_ass_sex_pre")
                        $ M_mom.set("sex speed", .175)
                        call expression game.dialog_select("debbie_dialogue_mom_revealing_feel_ass_sex_after")
                        jump expression game.dialog_select("mom_kitchen_fuck_loop")
                    else:

                        call expression game.dialog_select("debbie_dialogue_mom_revealing_feel_ass_no_sex")
                        jump expression game.dialog_select("debbie_dialogue_options")
                "Поговорить":

                    call expression game.dialog_select("debbie_dialogue_mom_revealing_talk")
                    jump expression game.dialog_select("debbie_dialogue_options")

        if M_mom.is_set("revealing"):
            call expression game.dialog_select("debbie_dialogue_mom_revealing")
        else:

            call expression game.dialog_select("debbie_dialogue_mom_not_revealing")
        menu debbie_dialogue_options:
            "Спросить об {b}Отце{/b}." if M_mom.is_set("dad question"):
                $ M_mom.set("dad question", False)
                call expression game.dialog_select("debbie_dialogue_ask_about_dad")
                jump expression game.dialog_select("debbie_dialogue_options")

            "Спросить о денежных проблемах." if M_mom.is_set("money question"):
                $ M_mom.set("money question", False)
                call expression game.dialog_select("debbie_dialogue_ask_about_money_problems")
                jump expression game.dialog_select("debbie_dialogue_options")

            "Спросить о мужчинах в костюмах." if M_mom.is_set("bad guys question"):
                $ M_mom.set("bad guys question", False)
                call expression game.dialog_select("debbie_dialogue_ask_about_men_in_suits")
                jump expression game.dialog_select("debbie_dialogue_options")

            "Краска." if M_dewitt.is_state([S_dewitt_ask_deb_paint, S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint]):
                call expression game.dialog_select("debbie_dialogue_paint")
                $ M_dewitt.trigger(T_dewitt_diane_find_paint)
            "Помочь {b}[deb_name]{/b} по дому.":

                if M_mom.is_state([S_mom_fill_mower, S_mom_mow_lawn]):
                    call expression game.dialog_select("debbie_dialogue_help_mow_lawn")
                    $ game.main()

                elif M_mom.between_states(S_mom_sis_check, S_mom_fix_pipe):
                    call expression game.dialog_select("debbie_dialogue_help_fix_broken_pipe")

                elif M_mom.between_states(S_mom_vacuum_help, S_mom_laundry_help):
                    call expression game.dialog_select("debbie_dialogue_help_chores_pre")
                    if M_mom.is_state(S_mom_laundry_help) and M_mom.is_set("chores"):
                        call expression game.dialog_select("debbie_dialogue_help_chores_later")
                    else:
                        call expression game.dialog_select("debbie_dialogue_help_chores_tomorrow")
                    call expression game.dialog_select("debbie_dialogue_help_chores_after")

                elif M_mom.is_state(S_mom_check_car):
                    call expression game.dialog_select("debbie_dialogue_help_check_car")

                elif M_mom.is_state(S_mom_fix_car):
                    call expression game.dialog_select("debbie_dialogue_help_fix_car")
                else:

                    call expression game.dialog_select("debbie_dialogue_help_nothing")
                show player 1
                jump expression game.dialog_select("debbie_dialogue_options")

            "Нанести лосьон." if M_mom.is_set("lotion fun"):
                if M_mom.is_set("sex available") and player.location == L_home_kitchen:
                    call expression game.dialog_select("debbie_dialogue_lotion_fun_had_sex")
                else:

                    call expression game.dialog_select("debbie_dialogue_lotion_fun")
                call expression game.dialog_select("debbie_dialogue_lotion_fun_after")
                $ M_mom.set("fetch lotion", True)


            "За покупками" if M_mom.is_state(S_mom_hang_out_return) and player.location == L_home_kitchen:
                call expression game.dialog_select("debbie_dialogue_shopping")
                $ M_mom.trigger(T_mom_hang_out_accept)

            "Принять душ." if M_mom.is_set("sex available"):
                if player.location == L_home_basement:
                    call expression game.dialog_select("debbie_dialogue_shower_basement")

                elif player.location == L_home_kitchen:
                    call expression game.dialog_select("debbie_dialogue_shower_kitchen")
                jump expression game.dialog_select("mom_shower_question")

            "Заняться сексом в её комнате." if M_mom.is_set("sex available"):
                if player.location == L_home_basement:
                    call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_basement")

                elif player.location == L_home_kitchen:
                    call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_kitchen")
                call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_after")
                jump expression game.dialog_select("mom_sex")

            "Заняться сексом в своей комнате." if M_mom.is_set("sex available") and not M_mom.is_set("room sneak"):
                call expression game.dialog_select("debbie_dialogue_sex_in_my_room")
                $ M_mom.set("room sneak", True)

            "Затусить в машине." if M_mom.is_set("sex available"):
                call expression game.dialog_select("debbie_dialogue_sex_in_car")
                jump expression game.dialog_select("debbie_car_sex")

            "Посмотреть кино." if M_mom.is_set("sex available") and not M_mom.is_set("movie night"):
                call expression game.dialog_select("debbie_dialogue_watch_movie")
                $ M_mom.set("movie night", True)

            "Прачечная." if M_mom.is_set("basement sex"):
                if player.location == L_home_basement:
                    label mom_basement_replay:
                        if not store._in_replay == None:
                            if randomizer() < 50:
                                jump expression game.dialog_select("basement_mom_sex")
                    call expression game.dialog_select("debbie_dialogue_laundry_sex_basement")
                    if not M_mom.is_state(S_mom_give_laundry) and randomizer() <= 50:
                        $ mom_basement_rand = True
                        call expression game.dialog_select("debbie_dialogue_laundry_sex_basement_random_true")
                    else:

                        $ mom_basement_rand = False
                        call expression game.dialog_select("debbie_dialogue_laundry_sex_basement_random_false")
                    $ M_mom.set("sex speed", .4)
                    $ player.go_to(L_home_basement)
                    $ cum = False
                    $ anim_toggle = True
                    $ animated = False
                    $ xray = False
                    jump expression game.dialog_select("basement_mom_sex_loop")

                elif player.location == L_home_kitchen:
                    call expression game.dialog_select("debbie_dialogue_laundry_sex_kitchen")
                    jump expression game.dialog_select("basement_mom_sex")

            "Целоваться" if M_mom.is_state(S_mom_kissing_practice) and player.location == L_home_kitchen:
                call expression game.dialog_select("debbie_dialogue_kiss")
                menu:
                    "Ты можешь меня научить?":
                        call expression game.dialog_select("debbie_dialogue_kiss_teach")
                        if player.stats.chr() >= 5:
                            jump expression game.dialog_select("mom_kissing_practice")
                        else:

                            call expression game.dialog_select("debbie_dialogue_kiss_teach_stat_fail")
                    "Ничего":

                        call expression game.dialog_select("debbie_dialogue_kiss_leave")

            "Практиковать поцелуи" if M_mom.is_set("practice kissing") and player.location == L_home_kitchen:
                call expression game.dialog_select("debbie_dialogue_kiss_practice")
                $ game.timer.tick()
            "Неважно.":

                call expression game.dialog_select("debbie_dialogue_leave")
    hide player
    hide debbie
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
