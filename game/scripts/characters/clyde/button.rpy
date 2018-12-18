label clyde_button_dialogue:
    scene expression player.location.background_blur
    if M_roxxy.is_state(S_roxxy_meeting_clyde) and game.timer.is_dark():
        call expression game.dialog_select("button_clyde_roxxy_meeting_buyer_dark")
        $ M_roxxy.trigger(T_roxxy_meet_buyer)
        $ game.sleep_lock = True
        $ player.go_to(L_park)
        $ game.main()

    elif M_roxxy.finished_state(S_roxxy_picnic_done) and not M_clyde.get("cletus"):
        $ M_clyde.set("cletus", True)
        call expression game.dialog_select("button_clyde_cletus_introduce")
        $ game.main()
    else:
        if not M_roxxy.finished_state(S_roxxy_missing_outfit_delay):
            call expression game.dialog_select("button_clyde_intro_0")
        elif M_roxxy.between_states(S_roxxy_missing_outfit_delay, S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_clyde_intro_1")
        else:
            call expression game.dialog_select("button_cletus_intro")
        menu clyde_dialogue_options:
            "Crystal in Prison." if M_roxxy.is_state(S_roxxy_get_evidence):
                call expression game.dialog_select("button_clyde_roxxy_get_evidence_intro")
                menu:
                    "What about {b}Roxxy{/b}?":
                        if player.has_required_chr(7):
                            call expression game.dialog_select("button_clyde_roxxy_get_evidence_about_roxxy_pass")
                            $ M_roxxy.trigger(T_roxxy_sell_meth)
                        else:
                            call expression game.dialog_select("button_clyde_roxxy_get_evidence_about_roxxy_fail")
                        $ game.main()
                    "Nevermind.":
                        call expression game.dialog_select("button_clyde_roxxy_get_evidence_nevermind")

            "Selling the Meth" if M_roxxy.is_state(S_roxxy_selling_meth_ask_roxxy):
                call expression game.dialog_select("button_clyde_roxxy_selling_meth_ask_roxxy")

            "Selling the Meth" if M_roxxy.is_state(S_roxxy_selling_meth):
                call expression game.dialog_select("button_clyde_roxxy_selling_meth")
                $ M_roxxy.trigger(T_roxxy_meet_clyde)

            "Selling the Meth" if M_roxxy.is_state(S_roxxy_meeting_clyde):
                call expression game.dialog_select("button_clyde_roxxy_meeting_buyer")

            "Wanna hit the range?" if M_roxxy.finished_state(S_roxxy_beat_clyde) and L_trailer_tractor.is_here(M_clyde):
                jump shooting_range_dialogue

            "Your dog." if M_clyde.get("doggo_quest") and not player.has_item("plush_11") and player.has_item("mysterious_statue_1"):
                call expression game.dialog_select("button_clyde_your_dog")
                jump clyde_dialogue_options

            "Pink Beaver." if M_clyde.get("doggo_quest") and player.has_item("plush_11") and player.has_item("mysterious_statue_1"):
                call expression game.dialog_select("button_clyde_pink_beaver")
                $ player.remove_item("plush_11")
                $ M_clyde.set("doggo_quest", False)
                $ player.get_item("mysterious_statue_2")
                jump clyde_dialogue_options

            "This statue." if player.has_item("mysterious_statue_1") and not player.has_item("mysterious_statue_2") and not player.has_item("mysterious_statue_3"):
                call expression game.dialog_select("button_clyde_mysterious_statue_1")
                jump clyde_dialogue_options

            "This statue." if player.has_item("mysterious_statue_1") and player.has_item("mysterious_statue_2") and not player.has_item("mysterious_statue_3"):
                call expression game.dialog_select("button_clyde_mysterious_statue_2")
                jump clyde_dialogue_options

            "Fine, how are you?" if not M_clyde.get("cletus"):
                call expression game.dialog_select("button_clyde_how_are_you")
                jump clyde_dialogue_options

            "Where are you from?" if not M_clyde.get("cletus"):
                call expression game.dialog_select("button_clyde_where_are_you_from")
                jump clyde_dialogue_options

            "This is ridiculous, I know you're {b}Clyde{/b}!" if M_clyde.get("cletus"):
                call expression game.dialog_select("button_clyde_know_youre_clyde")

            "What's going on in there?" if L_trailer_shack.is_here(M_clyde) and not L_trailer_shack_interior.locked:
                call expression game.dialog_select("button_clyde_whats_going_on")
                jump clyde_dialogue_options

            "Nice tractor" if L_trailer_tractor.is_here(M_clyde):
                call expression game.dialog_select("button_clyde_nice_tractor")
                jump clyde_dialogue_options

            "See ya, {b}Clyde{/b}" if not M_clyde.get("cletus"):
                call expression game.dialog_select("button_clyde_see_ya")
                $ game.main()

            "Nevermind." if M_clyde.get("cletus"):
                call expression game.dialog_select("button_clyde_nevermind")
                $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
