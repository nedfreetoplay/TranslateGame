label dexter_court_dialogue:
    scene expression player.location.background_blur
    if M_roxxy.get("roxxy relationship") == 0:
        call expression game.dialog_select("button_dexter_intro_beginning")
        $ game.main()
    else:
        if M_roxxy.get("roxxy relationship") == 5:
            call expression game.dialog_select("button_dexter_intro_final")
        else:
            call expression game.dialog_select("button_dexter_intro")
        menu:
            "Шоу талантов." if M_dewitt.is_set("talent ask dexter"):
                if M_dewitt.is_set("talent helping kevin"):
                    call expression game.dialog_select("dewitt_talent_show_helping_kevin")

                elif M_dewitt.is_set("talent helping eve"):
                    call expression game.dialog_select("dewitt_talent_show_helping_eve")
                else:

                    call expression game.dialog_select("button_dexter_talent_show")
                    $ M_dewitt.set("talent ask dexter", False)

            "Бросить вызов." if player.location == L_basketball_court:
                call expression game.dialog_select("button_dexter_challenge")
                $ M_dexter.trigger(T_dex_challenge)

            "Отжимания." if M_roxxy.is_state(S_roxxy_do_pushups_intro, S_roxxy_do_pushups):
                if M_roxxy.is_state(S_roxxy_do_pushups):
                    call expression game.dialog_select("dexter_button_pushups")
                    call screen pushups_minigame
                else:
                    call expression game.dialog_select("dexter_button_pushups_rematch")
                    call screen pushups_minigame

            "Библиотечная книга." if M_bissette.between_states(S_bissette_jane_return_books, [S_bissette_got_eriks_martinez_books, S_bissette_got_martinez_eriks_books]) and not M_bissette.is_set("dexters book search"):
                call expression game.dialog_select("button_dexter_library_book")
            "По-прежнему играть в баскетбол":

                if M_roxxy.get("roxxy relationship") == 5:
                    call expression game.dialog_select("button_dexter_basketball_final")
                else:
                    call expression game.dialog_select("button_dexter_basketball")
            "Хорошо себя ведешь?" if M_roxxy.get("roxxy relationship")==5:
                call expression game.dialog_select("button_dexter_behaving_yourself")

            "Беги сейчас же." if M_roxxy.get("roxxy relationship")==5:
                call expression game.dialog_select("button_dexter_run_along")

            "Неважно." if M_roxxy.get("roxxy relationship") < 5:
                call expression game.dialog_select("button_dexter_whatever")
    hide dexter
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
