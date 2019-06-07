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
        player_name "( Wow, she really was tired! )"
        player_name "( She didn't even change into her pajamas... )"
        pause
        player_name "( ... )"
        player_name "( I guess I'll just leave the money on her nightstand with a note about the additional order. )"
        $ M_diane.trigger(T_diane_delivery_2_finished)
    else:
        scene expression "backgrounds/location_diane_bedroom_bed02.jpg"
        player_name "( I always seem to get more than I bargained for at {b}Diane's{/b} house. )"
        pause
        player_name "( I should leave before I have another incident... )"
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
