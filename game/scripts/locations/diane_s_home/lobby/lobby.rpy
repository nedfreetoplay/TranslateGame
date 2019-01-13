label dianelobby_dialogue:
    $ player.go_to(L_diane_home)
    if M_diane.is_state(S_diane_look_in_kitchen):
        call expression game.dialog_select("dianes_lobby_look_in_kitchen")
    $ game.main()

label dianelobby_locked:
    if player.location == L_diane_kitchen:
        scene dianekitchen
    elif player.location == L_diane_yard:
        scene location_diane_front_day_blur
    show player 10 with dissolve
    player_name "Кажется, я слышу кого-то на заднем дворе. Я должен проверить и посмотреть, может это {b}Диана{/b}."
    hide player with dissolve
    return

label dianekitchen_locked:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "Я не должен заходить туда без разрешения."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
