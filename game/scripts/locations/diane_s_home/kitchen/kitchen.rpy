label dianes_kitchen_dialogue:
    $ player.go_to(L_diane_kitchen)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if M_diane.is_state(S_diane_look_in_kitchen):
        call expression game.dialog_select("dianes_kitchen_diane_look_in_kitchen")
        $ M_diane.trigger(T_diane_search_kitchen)
        $ player.go_to(L_diane_home)

    elif M_diane.is_state(S_diane_clean_garden_report):
        call expression game.dialog_select("dianes_kitchen_diane_clean_garden_report")
        $ M_diane.trigger(T_diane_clean_garden_reported)
        $ player.go_to(L_map)
        $ game.main()
    $ game.main()

label kitchen_drink:
    scene expression "backgrounds/location_diane_kitchen_closeup.jpg"
    show player 133 with dissolve
    player_name "What drink should I make?"
    call screen drink_minigame(M_diane.get("random drink"))

label dianes_kitchen_get_water:
    scene expression "backgrounds/location_diane_kitchen_day_blur.jpg"
    show player 667b with dissolve
    pause
    show player 667 with dissolve
    player_name "Alright, one glass of water coming up..."
    hide player with dissolve

    $ M_diane.trigger(T_diane_found_cold_towel)
    $ game.main()

label dianes_kitchen_get_pump:
    scene expression "backgrounds/location_diane_kitchen_closeup.jpg"
    show player 103b with dissolve
    player_name "( Hmm? )"
    player_name "( This is one weird looking tool! )"
    player_name "( It looks like a spray bottle or something... )"
    player_name "( I'll have to ask {b}Diane{/b} about it. )"
    hide player with dissolve

    $ player.get_item("pump")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
