label home_garage:
    $ player.go_to(L_home_garage)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if M_dewitt.is_state([S_dewitt_garage_find_paint, S_dewitt_ask_deb_paint]):
        call expression game.dialog_select("garage_dewitt_find_paint")
        $ M_dewitt.trigger(T_dewitt_no_paint)
    $ game.main()

label garage_use_workbench:
    if game.timer.is_dark():
        call expression game.dialog_select("garage_use_workbench_night")
        $ game.main()
    if M_dewitt.is_state(S_dewitt_make_new_flute) and player.has_item("drill") and player.has_item("stick"):
        call expression game.dialog_select("garage_dewitt_make_new_flute")
        $ player.remove_item("broken_flute")
        $ player.remove_item("drill")
        $ player.remove_item("stick")
        $ player.get_item("flute")
        $ game.timer.tick()
        $ M_dewitt.trigger(T_dewitt_fix_flute)

    elif M_dewitt.is_state(S_dewitt_make_replacement_guitar) and player.has_item("paint") and player.has_item("wood_pile"):
        call expression game.dialog_select("garage_dewitt_make_replacement_guitar")
        $ player.remove_item("wood_pile")
        $ player.remove_item("paint")
        $ player.get_item("fake_guitar")
        $ game.timer.tick()
        $ M_dewitt.trigger(T_dewitt_made_replacement_guitar)

    elif M_ross.is_state(S_ross_get_easels) and player.has_item("wood_pile"):
        call expression game.dialog_select("garage_build_easels")
        $ player.remove_item("wood_pile")
        $ player.get_item("easels")
        $ game.timer.tick()
    else:

        call expression game.dialog_select("garage_workbench_not_needed")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
