label annies_house_front_dialogue:
    $ player.go_to(L_annie_front)
    if M_diane.is_state(S_diane_delivery_2) and game.timer.is_day():
        call expression game.dialog_select("annies_house_livingroom_diane_delivery_2")
        $ M_diane.trigger(T_diane_make_delivery_2)
        $ player.remove_item("milk_carton")
        $ player.go_to(L_annie_daycare)

    elif M_diane.is_state(S_diane_ask_help_annie) and game.timer.is_day():
        call expression game.dialog_select("annie_front_diane_ask_help_annie")
        $ M_diane.trigger(T_diane_asked_annie_help)

    elif M_diane.is_state(S_diane_build_toys) and game.timer.is_day():
        call expression game.dialog_select("annie_front_diane_build_toys")
        $ M_diane.trigger(T_diane_helped_annie)
        $ player.remove_item("hammer")
        $ player.remove_item("handsaw")
    $ game.main()

label annies_house_livingroom_dialogue:
    $ player.go_to(L_annie_livingroom)
    if M_diane.is_state(S_diane_help_annie) and game.timer.is_day():
        call expression game.dialog_select("annies_house_diane_help_annie")
    $ game.main()

label annies_house_daycare_dialogue:
    $ player.go_to(L_annie_daycare)
    $ game.main()

label annies_house_get_hammer:
    scene expression L_annie_livingroom.background_blur
    show player 687 with dissolve
    player_name "Да, этого вполне достаточно."
    hide player with dissolve

    $ player.get_item("hammer")
    if player.has_item("handsaw"):
        show player 14
        player_name "Хорошо, теперь мне нужно выйти наружу и собрать игрушки для {b}Люси{/b}."
        hide player with dissolve
        $ M_diane.trigger(T_diane_find_tools)
    $ game.main()

label annies_house_get_saw:
    scene expression L_annie_livingroom.background_blur
    show player 686 with dissolve
    player_name "О, это прекрасно и остро!"
    hide player with dissolve

    $ player.get_item("handsaw")
    if player.has_item("hammer"):
        show player 14
        player_name "Хорошо, теперь мне нужно выйти наружу и собрать игрушки для {b}Люси{/b}."
        hide player with dissolve
        $ M_diane.trigger(T_diane_find_tools)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc