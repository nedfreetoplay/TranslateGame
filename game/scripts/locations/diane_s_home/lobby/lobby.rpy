label dianelobby_dialogue:
    $ player.go_to(L_diane_home)
    if aunt.started(aunt_mouse_attack):
        call expression game.dialog_select("dianes_lobby_diane_mouse_attack_started")
    $ game.main()

label dianelobby_locked:
    if player.location == L_diane_kitchen:
        scene dianekitchen
    elif player.location == L_diane_yard:
        scene location_diane_front_day_blur
    show diane 3 at right
    show player 11 at left
    with dissolve
    dia "Куда ты направляешься? Сад снаружи, а не там, красавчик."
    hide diane
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
