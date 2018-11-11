label chad_button_dialogue:
    if M_ross.is_state(S_ross_get_eve_drawing) and not player.has_item("art_pad"):
        if not M_ross.get("talked with chad"):
            call expression game.dialog_select("button_chad_get_eve_drawing_first")
            $ M_ross.set("talked with chad", True)

        elif not player.has_item("eve_drawing"):
            call expression game.dialog_select("button_chad_get_eve_drawing")

        elif player.has_item("eve_drawing"):
            call expression game.dialog_select("button_chad_get_eve_drawing_completed")
            $ player.remove_item("eve_drawing")
            $ player.get_item("art_pad")
    else:
        call expression game.dialog_select("button_chad_generic")
        menu:
            "Уйти.":
                call expression game.dialog_select("button_chad_nothing")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
