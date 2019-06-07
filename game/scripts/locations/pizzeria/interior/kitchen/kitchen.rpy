label pizzeria_kitchen_dialogue:
    $ player.go_to(L_pizzeria_kitchen)
    if M_diane.is_state(S_diane_delivery_1_place_goods):
        call expression game.dialog_select("pizzeria_storage_diane_delivery_1_place_goods")
        if player.transport_level > 0:
            call expression game.dialog_select("pizzeria_storage_diane_delivery_1_place_goods_bike")
        else:
            call expression game.dialog_select("pizzeria_storage_diane_delivery_1_place_goods_no_bike")
        $ M_diane.trigger(T_diane_place_delivery_goods)
        $ player.get_money(100)
        $ player.go_to(L_map)
        $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
