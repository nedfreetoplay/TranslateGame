label kevin_button_dialogue:
    scene cafeteria_b
    if M_ross.is_state(S_ross_find_magazines) and not M_ross.get("magazine kevin"):
        call expression game.dialog_select("kevin_dialogue_ross_find_magazines")
        call expression "player_ross_magazines_{}_left".format(M_ross.get("magazines remaining"))
        $ M_ross.set("magazine kevin", True)

    elif M_ross.is_state(S_ross_ask_model):
        call expression game.dialog_select("kevin_dialogue_ross_ask_model")
    else:

        if not erik.completed(erik_favor_2):
            call expression game.dialog_select("button_kevin_intro_pre_favor")
        else:
            call expression game.dialog_select("kevin_dialogue_intro")
            call expression game.dialog_select("kevin_dialogue_erik_favor_2_completed")
        menu kevin_menu_dialogue:
            "Дежурство в столовой." if not erik.completed(erik_favor_2):
                if not M_kevin.get("asked_shift_cover"):
                    call expression game.dialog_select("button_kevin_cafeteria_duty_first")
                    $ M_kevin.set("asked_shift_cover", True)
                else:
                    call expression game.dialog_select("button_kevin_cafeteria_duty_repeat")

            "Кто-то, чтобы прикрыть тебя." if M_kevin.get("asked_shift_cover") and not erik.over(erik_favor_2):
                if not erik.completed(erik_favor_2):
                    call expression game.dialog_select("button_kevin_shift_cover_no_favor")
                else:
                    call expression game.dialog_select("button_kevin_shift_cover_has_favor")

            "Гитара." if M_dewitt.is_state(S_dewitt_kevin_give_guitar):
                call expression game.dialog_select("kevin_dialogue_dewitt_kevin_give_guitar")
                $ player.remove_item("guitar")
                if M_dewitt.is_set("talent ask eve"):
                    $ M_dewitt.trigger(T_dewitt_find_last_talent)
                else:
                    $ M_dewitt.trigger(T_dewitt_give_fender_guitar)

            "Шоу талантов." if M_dewitt.between_states(S_dewitt_talent_show_ask, S_dewitt_replace_guitar) or M_dewitt.is_set("talent helping eve"):
                if M_dewitt.is_set("talent helping eve"):
                    call expression game.dialog_select("dewitt_talent_show_helping_eve")

                elif M_dewitt.is_state([S_dewitt_talent_show_ask, S_dewitt_talent_show_ask_kevin]):
                    call expression game.dialog_select("kevin_dialogue_talent_show_help")
                    $ M_dewitt.trigger(T_dewitt_kevins_agreement)

                elif M_dewitt.is_state(S_dewitt_replace_guitar):
                    call expression game.dialog_select("kevin_dialogue_talent_show_replace_guitar")
                else:

                    call expression game.dialog_select("kevin_dialogue_talent_show")

            "Использованные Трусики." if M_somrak.finished_state(S_somrak_start):
                if M_somrak.get("asked kevin panties"):
                    call expression game.dialog_select("button_kevin_used_panties_repeat")
                else:
                    call expression game.dialog_select("button_kevin_used_panties_first")
                    $ M_somrak.set("asked kevin panties", True)
                jump kevin_menu_dialogue

            "Клей." if M_dewitt.is_state(S_dewitt_science_adhesive):
                call expression game.dialog_select("kevin_dialogue_dewitt_science_adhesive")
            "Ничего.":

                call expression game.dialog_select("kevin_dialogue_leave")

    hide kevin
    hide player
    with dissolve
    $ game.main()

label kevin_button_dialogue_gym:
    if game.timer.is_day():
        call expression game.dialog_select("kevin_gym_intro")
    else:
        call expression game.dialog_select("tired_training_dialogue")
        $ game.main()
    menu:
        "Давай просто поднимемся.":
            call expression game.dialog_select("kevin_gym_lets_lift")
            jump weightlifting
        "Успокойтесь.":
            call expression game.dialog_select("kevin_gym_take_it_easy")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
