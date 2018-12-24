label right_hall_eve_button:
    call expression game.dialog_select("button_eve_intro")
    menu:
        "Шоу талантов." if M_dewitt.is_state([S_dewitt_talent_show_ask, S_dewitt_talent_show_ask_eve]) or M_dewitt.is_set("talent helping kevin"):
            if M_dewitt.is_set("talent helping kevin"):
                call expression game.dialog_select("dewitt_talent_show_helping_kevin")
            else:

                call expression game.dialog_select("button_eve_talent_show_help")
                $ M_dewitt.trigger(T_dewitt_eves_agreement)

        "Блокнот." if M_ross.is_state(S_ross_find_art_pad):
            call expression game.dialog_select("button_eve_ross_find_art_pad")
            $ M_ross.trigger(T_ross_find_eve_backpack)

        "Рюкзак." if M_ross.is_state(S_ross_find_eve_backpack):
            if player.has_item("eve_backpack"):
                call expression game.dialog_select("button_eve_ross_find_eve_backpack_have_backpack")
                $ player.remove_item("eve_backpack")
                $ M_ross.trigger(T_ross_got_eve_backpack)
            else:

                call expression game.dialog_select("button_eve_ross_find_eve_backpack_no_backpack")

        "Рисование." if M_ross.is_state(S_ross_get_eve_drawing):
            call expression game.dialog_select("button_eve_ross_get_eve_drawing")

        "Модель." if M_ross.is_state(S_ross_ask_model):
            call expression game.dialog_select("button_eve_ask_model")

        "Краска." if M_ross.is_state(S_ross_get_paint):
            call expression game.dialog_select("button_eve_ross_get_paint")
            $ L_tattooparlor.unlock()
            $ M_ross.trigger(T_ross_talk_to_grace)

        "Краска." if M_ross.is_state(S_ross_get_paint_grace):
            call expression game.dialog_select("button_eve_ross_get_paint_grace")
        "Ничего.":

            $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
