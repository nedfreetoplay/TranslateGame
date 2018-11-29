label consumr:
    $ player.go_to(L_consumr)
    if M_okita.is_state(S_okita_get_ingredients) and not player.has_item("chicken_stock"):
        call expression game.dialog_select("consumr_okita_get_ingredients")

    elif M_diane.is_state(S_diane_go_to_consumr):
        call expression game.dialog_select("consumr_diane_get_bug_spray")
        $ M_diane.trigger(T_diane_entered_consumr)
        if player.has_item("annihilator"):
            jump expression game.dialog_select("consumr_diane_buy_bug_spray")
        $ player.get_money(100)

    elif M_diane.is_state(S_diane_get_milk_jug):
        call expression game.dialog_select("consumr_diane_get_milk_jug")
        $ M_diane.trigger(T_diane_research_milk_production)
        if player.has_item("milkjug"):
            jump expression game.dialog_select("consumr_diane_get_milk_jug_bought")
        $ player.get_money(300)
    $ game.main()

label diane_get_bug_spray_dialogue:
    if player.has_item("annihilator") and M_diane.is_state(S_diane_get_bug_spray):
        hide screen consumr
        jump consumr_diane_buy_bug_spray
    $ game.main()

label diane_get_milk_jug_dialogue:
    if player.has_item("milkjug") and M_diane.is_state(S_diane_buy_milk_jug):
        hide screen consumr
        jump consumr_diane_get_milk_jug_bought
    $ game.main()

label get_bike_dialogue:
    if player.has_item("bike"):
        $ player.upgrade_transport(1)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
