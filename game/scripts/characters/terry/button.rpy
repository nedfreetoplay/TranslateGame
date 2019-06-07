label terry_button_dialogue:
    $ playMusic(audio.m_pier)
    scene expression game.timer.image("pier_closeup{}")
    if M_terry.is_state(S_terry_start):
        call expression game.dialog_select("terry_dialogue_terry_start")
        $ M_terry.trigger(T_terry_intro)

    elif M_terry.is_state(S_terry_nemesis):
        call expression game.dialog_select("terry_dialogue_terry_nemesis")
        $ M_terry.trigger(T_terry_tigger)

    elif M_terry.is_state(S_terry_retire) and player.has_item("tigger"):
        call expression game.dialog_select("terry_dialogue_terry_retire")
        $ M_terry.trigger(T_terry_overjoyed_swim)
        $ M_aqua.trigger(T_aqua_test_pass)
        $ player.remove_item("tigger")
        $ player.go_to(L_map)

    elif M_terry.is_state(S_terry_tigger_sign):
        call expression game.dialog_select("terry_dialogue_terry_tigger_sign")
        $ M_terry.trigger(T_terry_hang_tigger)
    else:

        call expression game.dialog_select("terry_dialogue_intro")
        menu:
            "Buy some fish ($100)":
                call expression game.dialog_select("terry_dialogue_buy_fish")
                menu:
                    "Seatrout":
                        $ fish = "Seatrout"
                        call expression game.dialog_select("terry_dialogue_buy_fish_buy")
                    "Snapper":

                        $ fish = "Snapper"
                        call expression game.dialog_select("terry_dialogue_buy_fish_buy")
                    "Mackerel":

                        $ fish = "Mackerel"
                        call expression game.dialog_select("terry_dialogue_buy_fish_buy")
                    "Nevermind":

                        call expression game.dialog_select("terry_dialogue_buy_fish_nevermind")

            "Sell some fish (80$)" if player.has_item("seatrout", "snapper", "mackerel"):
                call expression game.dialog_select("terry_dialogue_sell_fish")
                menu:
                    "Seatrout" if player.has_item("seatrout"):
                        $ fish = "Seatrout"
                        call expression game.dialog_select("terry_dialogue_sell_fish_sell")

                    "Snapper" if player.has_item("snapper"):
                        $ fish = "Snapper"
                        call expression game.dialog_select("terry_dialogue_sell_fish_sell")

                    "Mackerel" if player.has_item("mackerel"):
                        $ fish = "Mackerel"
                        call expression game.dialog_select("terry_dialogue_sell_fish_sell")
                    "Nevermind":

                        call expression game.dialog_select("terry_dialogue_sell_fish_nevermind")
            "Buy a drink (5$)":

                call expression game.dialog_select("terry_dialogue_buy_drink_pre")
                menu:
                    "Buy a shot.":
                        call expression game.dialog_select("terry_dialogue_buy_drink")
                    "I’ll pass.":

                        call expression game.dialog_select("terry_dialogue_buy_drink_pass")
            "Go fishing":

                call expression game.dialog_select("terry_dialogue_fishing")
                $ M_terry.set("bait talk", True)

            "Bait" if M_terry.is_set("bait talk"):
                call expression game.dialog_select("terry_dialogue_fishing_bait")

            "What's your secret?" if M_terry.is_state(S_terry_secret):
                call expression game.dialog_select("terry_dialogue_secret")
                $ M_terry.trigger(T_terry_secret_lure)
                $ M_aqua.trigger(T_aqua_special_lure)

            "About that lure..." if M_terry.is_state([S_terry_lure, S_terry_trade]) and not M_aqua.is_state(S_aqua_trade):
                call expression game.dialog_select("terry_dialogue_lure")

            "Golden Compass." if M_aqua.is_state(S_aqua_trade) and M_terry.is_state(S_terry_trade):
                call expression game.dialog_select("terry_dialogue_golden_compass")
                $ player.remove_item("golden_compass")
                $ player.get_item("special_lure")
                $ M_terry.trigger(T_terry_lure_trade)
                $ M_aqua.trigger(T_terry_lure_trade)

            "Retire." if M_terry.is_state([S_terry_bored, S_terry_retire]) and M_aqua.is_state(S_aqua_valor_test):
                call expression game.dialog_select("terry_dialogue_retire")
                $ M_terry.trigger(T_terry_retire)

            "Fake ID" if M_roxxy.get("talked to roxxy id") and M_roxxy.is_state(S_roxxy_get_fake_id, S_roxxy_fake_id_get_picture):
                if M_roxxy.is_state(S_roxxy_get_fake_id):
                    call expression game.dialog_select("terry_dialogue_fake_id")
                    $ M_roxxy.trigger(T_roxxy_ask_terry)

                elif M_roxxy.is_state(S_roxxy_fake_id_get_picture) and player.has_item("roxxy_picture"):
                    if M_roxxy.get("talked to terry"):
                        call expression game.dialog_select("terry_dialogue_fake_id_picture_repeat")
                    else:

                        call expression game.dialog_select("terry_dialogue_fake_id_picture_first")
                        $ M_roxxy.set("talked to terry", True)
                    menu:
                        "Yes" if player.has_money(400):
                            $ player.spend_money(400)
                            call expression game.dialog_select("terry_dialogue_fake_id_yes")
                            menu:
                                "Becca.":
                                    call expression game.dialog_select("terry_dialogue_fake_id_yes_becca")
                                "Missy.":

                                    call expression game.dialog_select("terry_dialogue_fake_id_yes_missy")
                            $ game.timer.tick(2)
                            $ M_player.set("jerk roxxy", True)
                            $ M_roxxy.trigger(T_roxxy_give_id)
                        "No":

                            call expression game.dialog_select("terry_dialogue_fake_id_no")

            "GoldSchwagger" if M_roxxy.is_state(S_roxxy_spin_bottle) and not player.has_item("goldschwagger"):
                call expression game.dialog_select("terry_dialogue_goldschwagger")
                $ player.get_item("goldschwagger")
            "Leave":

                $ pass

    $ playMusic()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
