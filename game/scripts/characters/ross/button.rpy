label ross_button_dialogue:
    if M_ross.is_state(S_ross_grab_clay):
        call expression game.dialog_select("button_ross_grab_clay")

    elif M_ross.is_state(S_ross_find_partner):
        call expression game.dialog_select("button_ross_find_partner")
        $ M_ross.trigger(T_ross_find_partner)

    elif M_ross.is_state(S_ross_ask_mia_partner):
        call expression game.dialog_select("button_ross_ask_mia_partner")

    elif M_ross.is_state(S_ross_mia_is_partner):
        call expression game.dialog_select("button_ross_mia_is_partner")
        $ M_ross.trigger(T_ross_find_art_pad)

    elif M_ross.is_state([S_ross_find_art_pad, S_ross_find_eve_backpack, S_ross_get_eve_drawing]):
        if player.has_item("art_pad"):
            call expression game.dialog_select("button_ross_found_art_pad")
            $ M_ross.trigger(T_ross_mia_drawn)
            $ player.remove_item("art_pad")
            $ game.timer.tick()
        else:

            call expression game.dialog_select("button_ross_find_art_pad")

    elif M_ross.is_state(S_ross_collage):
        call expression game.dialog_select("button_ross_collage")
        $ M_ross.trigger(T_ross_find_magazines)
        $ player.remove_item("magazines")

    elif M_ross.is_state(S_ross_find_magazines):
        call expression game.dialog_select("button_ross_find_magazines")

    elif M_ross.is_state(S_ross_make_collage):
        call expression game.dialog_select("button_ross_make_collage")
        $ game.timer.tick()
        $ M_ross.trigger(T_ross_made_collage)

    elif M_ross.is_state(S_ross_need_easels):
        call expression game.dialog_select("button_ross_need_easels")
        $ M_ross.trigger(T_ross_find_easels)

    elif M_ross.is_state(S_ross_get_easels):
        if not player.has_item("easels"):
            call expression game.dialog_select("button_ross_get_easels")
        else:

            call expression game.dialog_select("button_ross_has_easels")
            $ M_ross.trigger(T_ross_has_easels)
            $ player.remove_item("easels")

    elif M_ross.is_state(S_ross_ask_model):
        call expression game.dialog_select("button_ross_ask_model")

    elif M_ross.is_state(S_ross_found_model):
        call expression game.dialog_select("button_ross_found_model")
        $ persistent.cookie_jar["Ross"]["unlocked"] = True
        $ persistent.cookie_jar["Ross"]["gallery"]["01_unlocked"] = True
        $ game.timer.tick()
        $ M_ross.trigger(T_ross_paint_for_smith)

    elif M_ross.is_state(S_ross_need_linens):
        call expression game.dialog_select("button_ross_need_linens")
        $ M_ross.trigger(T_ross_find_linens)

    elif M_ross.is_state(S_ross_get_linens):
        if player.has_item("linens"):
            call expression game.dialog_select("button_ross_has_linens")
            $ M_ross.trigger(T_ross_find_paint)
            $ player.remove_item("linens")
        else:

            call expression game.dialog_select("button_ross_get_linens")

    elif M_ross.is_state(S_ross_get_paint):
        call expression game.dialog_select("button_ross_get_paint_grace_reminder")

    elif M_ross.is_state(S_ross_get_paint_grace):
        if player.has_item("paint"):
            call expression game.dialog_select("button_ross_get_paint_grace")
            call screen art_minigame
        else:

            call expression game.dialog_select("button_ross_get_paint_grace_reminder")

    elif M_ross.is_state(S_ross_waiting_for_contest):
        call expression game.dialog_select("button_ross_waiting_for_contest")

    elif M_ross.is_state(S_ross_contest):
        call expression game.dialog_select("button_ross_contest")
        $ M_ross.trigger(T_ross_contest_over)

    elif M_ross.is_state(S_ross_paint_with_body):
        call expression game.dialog_select("button_ross_paint_with_body")

    elif M_ross.is_state(S_ross_end):
        call expression game.dialog_select("button_ross_end_intro")
        menu:
            "Да.":
                call expression game.dialog_select("button_ross_end_intro")
            "Нет.":

                call expression game.dialog_select("button_ross_end_intro")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
