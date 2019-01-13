label dianebedroom_dialogue:
    $ player.go_to(L_diane_bedroom)
    if M_diane.is_state(S_diane_get_cold_towel):
        call expression game.dialog_select("dianes_bedroom_diane_get_cold_towel")
        $ player.go_to(L_diane_home)
        $ game.main()
    $ game.main()

label diane_bedroom_diane_delivery_2_done:
    $ player.go_to(L_diane_bedroom)
    if M_diane.is_state(S_diane_delivery_2_done):
        scene expression "backgrounds/location_diane_bedroom_bed02.jpg"
        player_name "( Вау, она действительно устала! )"
        player_name "( Она даже не переоделась в пижаму... )"
        pause
        player_name "( ... )"
        player_name "( Я думаю, я просто оставлю деньги на тумбочке с запиской о дополнительном заказе. )"
        $ M_diane.trigger(T_diane_delivery_2_finished)
    else:
        scene expression "backgrounds/location_diane_bedroom_bed02.jpg"
        player_name "( Кажется, я всегда получаю больше, чем рассчитывал в доме {b}Дианы{/b}. )"
        pause
        player_name "( Я должен уйти до того, как у меня будет еще один инцидент... )"
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
