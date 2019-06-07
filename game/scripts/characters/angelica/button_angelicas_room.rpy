label angelicas_room_dialogue:
    if M_helen.is_set("helen route"):
        call expression game.dialog_select("angelicas_room_dialogue_helen_route_pre")
        menu angelicas_room_dialogue_helen_route_options:
            "Порка.":
                call expression game.dialog_select("angelicas_room_dialogue_helen_route_spanking")
                jump expression game.dialog_select("sacrament_complete")
            "Святое Семя.":

                call expression game.dialog_select("angelicas_room_dialogue_helen_route_holy_seed")
                jump expression game.dialog_select("helen_mc_churchsex")
            "Растопырить {b}Хелен{/b}.":

                call expression game.dialog_select("angelicas_room_dialogue_helen_route_spread_helen")
                jump expression game.dialog_select("sacrament_complete")
            "Согрешили ли вы?":

                show popup_unfinished at truecenter with dissolve
                pause
                hide popup_unfinished with dissolve
                jump expression game.dialog_select("angelicas_room_dialogue_helen_route_options")
            "Ничего.":

                call expression game.dialog_select("angelicas_room_dialogue_helen_route_leave")

    elif M_mia.is_set("mia route"):
        call expression game.dialog_select("angelicas_room_dialogue_mia_route")

    elif M_mia.is_state(S_mia_harolds_thoughts):
        call expression game.dialog_select("angelicas_room_dialogue_mia_harolds_thoughts")

    elif M_mia.is_state(S_mia_find_sinners):
        call expression game.dialog_select("angelicas_room_dialogue_mia_find_sinners_pre")
        menu:
            "Найти грешников..":
                call expression game.dialog_select("angelicas_room_dialogue_mia_find_sinners")

    elif M_mia.is_state(S_mia_angelicas_whip):
        call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_whip_pre")
        menu:
            "Кнут.":
                if player.has_item("whip"):
                    $ player.remove_item("whip")
                    jump expression game.dialog_select("helen_sacrement_training_part2")
                call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_whip")
            "Ничего.":

                call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_whip_leave")
    else:

        if M_mia.is_state([S_mia_harolds_thoughts, S_mia_angelicas_final_request]):
            call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_final_request_pre")
        else:
            call expression game.dialog_select("angelicas_room_dialogue_default_pre")
            $ player.go_to_previous()
            $ game.main()
        menu:
            "Страпон." if M_mia.is_state([S_mia_harolds_thoughts, S_mia_angelicas_final_request]) and not player.has_item("strapon"):
                call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_final_request_strap_on")

            "Ничего." if M_mia.is_state([S_mia_harolds_thoughts, S_mia_angelicas_final_request]):
                call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_final_request_leave")

            "Ничего." if not M_mia.is_state([S_mia_harolds_thoughts, S_mia_angelicas_final_request]):
                call expression game.dialog_select("angelicas_room_dialogue_default_leave")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
