label ronda_button_dialogue:
    call expression game.dialog_select("ronda_dialogue_intro")
    menu:
        "Шоу талантов." if M_dewitt.is_set("talent ask ronda"):
            if M_dewitt.is_set("talent helping kevin"):
                call expression game.dialog_select("dewitt_talent_show_helping_kevin")

            elif M_dewitt.is_set("talent helping eve"):
                call expression game.dialog_select("dewitt_talent_show_helping_eve")
            else:

                call expression game.dialog_select("ronda_dialogue_talent_show_help")
                $ M_dewitt.set("talent ask ronda", False)

        "Модель." if M_ross.is_state(S_ross_ask_model):
            call expression game.dialog_select("ronda_dialogue_model_help")
        "Оставить.":

            call expression game.dialog_select("ronda_dialogue_leave")
    hide player
    hide ronda
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
