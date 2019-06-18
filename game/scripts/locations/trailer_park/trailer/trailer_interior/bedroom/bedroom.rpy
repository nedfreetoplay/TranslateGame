label trailer_bedroom_dialogue:
    $ player.go_to(L_trailer_bedroom)
    if M_roxxy.is_state(S_roxxy_wait_in_her_room):
        call expression game.dialog_select("trailer_bedroom_roxxy_get_uniform_on_doggo_intro")
        if M_roxxy.get("lost shooting"):
            call expression game.dialog_select("trailer_bedroom_roxxy_wait_in_her_room_lost_shooting")
        else:

            call expression game.dialog_select("trailer_bedroom_roxxy_wait_in_her_room_won_shooting")
        $ M_roxxy.trigger(T_roxxy_has_uniform)

        $ player.go_to(L_map)

    elif M_roxxy.is_state(S_roxxy_picnic_done):
        call expression game.dialog_select("trailer_bedroom_roxxy_go_to_picnic")
        $ M_roxxy.trigger(T_roxxy_kissed)

        $ game.timer.tick()
        $ player.go_to(L_map)
    $ game.main()

label trailer_bedroom_roxxy_panties:
    scene expression player.location.background_blur with None
    show player 725 with dissolve
    player_name "( Это трусики {b}Рокси{/b}. )"
    player_name "( Как, черт возьми, она носит их? )"
    player_name "( Стринги выглядят так неудобно... )"
    pause
    player_name "( Держу пари {b}мастеру Сомраку{/b} они понравятся. )"

    hide player with dissolve
    $ player.get_item("roxxy_panties")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
