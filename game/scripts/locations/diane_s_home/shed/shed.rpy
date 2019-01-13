label shed:
    $ player.go_to(L_diane_shed)
    if M_diane.is_state(S_diane_fetch_pump) and not M_dewitt.is_state([S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint, S_dewitt_make_replacement_guitar]):
        scene expression game.timer.image("shed{}")
        show pump_object at Position(xpos = 118, ypos = 437)
        call expression game.dialog_select("dianes_shed_diane_fetch_pump")

    elif M_diane.is_state(S_diane_delivery_2_fetch_goods):
        call expression game.dialog_select("dianes_shed_diane_delivery_2_fetch_goods")
        $ L_annie_front.unlock()

    elif L_diane_shed.is_here(M_diane):
        if M_diane.is_state(S_diane_debbie_drop_off, S_diane_check_shed_light):
            call expression game.dialog_select("dianes_shed_diane_check_shed_light")
            $ M_diane.trigger(T_diane_house_locked)
            $ M_diane.trigger(T_diane_caught_milking)
            $ game.timer.tick(3)
            $ player.go_to(L_map)
            $ game.main()

        elif M_diane.is_state(S_diane_milking_help):
            call expression game.dialog_select("dianes_shed_milking_help")
            $ M_diane.trigger(T_diane_milking_malfunction_help)
            $ game.timer.tick(2)
            $ player.go_to(L_map)
            $ game.main()

    $ game.main()

label dianes_shed_got_milk_delivery_3:
    show expression "backgrounds/location_diane_shed01_day_blur.jpg"
    show player 168b with dissolve
    player_name "!!!"
    show player 168c
    player_name "Срань господня! Это намного тяжелее предыдущего!"
    show player 167
    pause
    show player 168
    player_name "{b}Диана{/b} действительно должна инвестировать в ручную тележку."
    player_name "Будет тяжело тащить это всю дорогу до школы самостоятельно."
    hide player with dissolve
    show popup_item_milk at truecenter with dissolve
    $ player.get_item("milk_carton")
    hide popup_item_milk with dissolve
    $ M_diane.trigger(T_diane_found_delivery_3_goods)
    $ game.main()

label dianes_shed_pick_up_milk_delivery_02:
    scene shed
    show player 163c with dissolve
    player_name "Блин, это намного тяжелее, чем в прошлый раз!"
    player_name "Я думаю, это хорошо, хотя ..."
    player_name "... Бизнес {b}Дианы{/b} быстро растет!"

    player_name "Хорошо, я должен {b}доставить это в детский сад по соседству.{/b}"
    hide player with dissolve
    $ game.main()

label dianes_shed_get_milk_to_dump:
    scene expression "backgrounds/location_diane_shed01_day_blur.jpg"
    show player 680 with dissolve
    player_name "О, оно все еще теплое."
    player_name "Хорошо, {b}мне просто нужно вылить это в один из бидонов.{/b}"
    player_name "Проще простого."
    hide player with dissolve

    $ M_diane.set("acquired milk", True)
    $ game.main()

label dianes_shed_dump_milk:
    if M_diane.get("acquired milk"):
        scene expression "backgrounds/location_diane_shed01_day_blur.jpg"
        show player 680 with dissolve
        player_name "Хорошо, я просто наливаю это вот так..."
        show player 681 with dissolve
        player_name "... Ииииии готово!"
        show player 17 with dissolve
        player_name "Теперь, я должен пойти проверить {b}Диану{/b}."
        hide player with dissolve
        $ M_diane.trigger(T_diane_make_drink)
    else:
        scene expression "backgrounds/location_diane_shed01_day_blur.jpg"
        show player 681b with dissolve
        player_name "Это должно быть бидон!"
        player_name "Он холодный на ощупь!"
        player_name "{b}Мне просто нужно найти насос, а затем слить его сюда.{/b}"
        hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
