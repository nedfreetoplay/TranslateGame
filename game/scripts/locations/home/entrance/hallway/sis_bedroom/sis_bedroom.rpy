label sis_bedroom_dialogue:
    $ player.go_to(L_home_sisbedroom)




    scene expression game.timer.image("backgrounds/location_home_jennybedroom{}.jpg")
    if not game.timer.is_dark():
        if M_jenny.is_state(S_jenny_panty_steal):
            if L_home_sisbedroom.is_here(M_jenny):
                call expression game.dialog_select("sis_bedroom_sis_in_room")
                $ player.go_to(L_home_hallway)
            else:

                call expression game.dialog_select("sis_bedroom_sis_not_in_room")

        elif M_bissette.is_state(S_bissette_roxxy_jenny_spying):
            call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying")
            $ M_bissette.trigger(T_bissette_roxxy_jenny_spied)
            $ game.timer.tick()
            $ player.go_to(L_home_hallway)

        elif M_jenny.is_state(S_jenny_hallway_meetup_focus):
            call expression game.dialog_select("sis_bedroom_sis_hallway_2_started")
            $ player.go_to(L_home_hallway)

        elif M_jenny.is_state(S_jenny_panty_deal):
            call expression game.dialog_select("sis_bedroom_sis_caught_stealing_panties")
            if player.has_money(100):
                menu:
                    "Here's $100.":
                        $ player.spend_money(100)
                        $ player.get_item("panties")
                        call expression game.dialog_select("sis_bedroom_sis_caught_stealing_panties_buy_panties")
                        $ M_jenny.trigger(T_jenny_panty_bought)
                    "I don't need it.":

                        call expression game.dialog_select("sis_bedroom_sis_caught_stealing_panties_do_not_buy_panties")
            else:

                menu:
                    "I don't have enough.":
                        call expression game.dialog_select("sis_bedroom_sis_caught_stealing_panties_cant_buy_panties")
            $ player.go_to(L_home_hallway)

        elif M_jenny.is_state(S_jenny_hallway_noises):
            call expression game.dialog_select("sis_bedroom_sis_final_started")
            $ M_jenny.trigger(T_jenny_overhear_stream)
            $ player.go_to(L_home_hallway)

        elif M_bissette.is_state(S_bissette_roxxy_cheerleader_deal):
            call expression game.dialog_select("jennys_bedroom_bissette_roxxy_cheerleader_deal")
            $ M_bissette.trigger(T_bissette_jenny_deal)

    elif game.timer.is_dark() and not in_sis_room:
        call expression game.dialog_select("sis_bedroom_sis_sleeping")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
