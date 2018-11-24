label pink_dialogue:
    $ player.go_to(L_pink)
    if game.timer.is_night():
        $ player.go_to(L_map)
        $ game.main()
    if L_pink.first_visit:
        call expression game.dialog_select("pink_first_visit")
        $ L_pink.visited()

    if M_mia.is_state(S_mia_helen_outfit_request) and not player.has_item("red_corset"):
        call expression game.dialog_select("pink_mia_helen_outfit_request")

    elif M_mia.is_state([S_mia_angelicas_order, S_mia_angelicas_whip]) and not player.has_item("whip"):
        call expression game.dialog_select("pink_mia_angelicas_whip")

    elif M_diane.is_state(S_diane_get_outfit_package):
        call expression game.dialog_select("pink_diane_get_outfit_package")
        $ M_diane.trigger(T_diane_got_outfit_package)
        $ player.get_item("package")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
