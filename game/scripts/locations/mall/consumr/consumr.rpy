label consumr:
    $ player.go_to(L_consumr)
    if M_okita.is_state(S_okita_get_ingredients) and not player.has_item("chicken_stock"):
        call expression game.dialog_select("consumr_okita_get_ingredients")

    elif M_diane.is_state(S_diane_go_to_consumr):
        call expression game.dialog_select("consumr_diane_get_bug_spray")
        $ M_diane.trigger(T_diane_entered_consumr)
        $ player.get_money(100)

    elif M_diane.is_state(S_diane_get_milk_jug):
        call expression game.dialog_select("consumr_diane_get_milk_jug")
        $ M_diane.trigger(T_diane_research_milk_production)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
