label angelica_dialogue:
    if M_ross.is_state(S_ross_get_linens) and not player.has_item("linens"):
        call expression game.dialog_select("angelica_dialogue_ross_get_linens_pre")
        menu:
            "Скатерти":
                call expression game.dialog_select("angelica_dialogue_ross_get_linens")
                $ player.get_item("linens")

    elif M_mia.is_set("helen dialogue change"):
        call expression game.dialog_select("angelica_dialogue_change_pre")
        menu:
            "Говорить.":
                call expression game.dialog_select("angelica_dialogue_change_talk")
            "Кладбище.":

                call expression game.dialog_select("angelica_dialogue_change_graveyard")
            "Неважно.":

                call expression game.dialog_select("angelica_dialogue_change_leave")
    else:

        call expression game.dialog_select("angelica_dialogue_pre")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
