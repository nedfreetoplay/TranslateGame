label pool_dialogue:
    $ player.go_to(L_pool)
    $ used_changing_girls = []
    if M_cassie.is_state(S_cassie_ban_from_pool):
        if not game.timer.is_dark():
            call expression game.dialog_select("pool_banned_from_pool_day")
        else:

            call expression game.dialog_select("pool_banned_from_pool_night")
            call expression game.dialog_select("pool_banned_from_pool_night_swim")
            $ M_cassie.trigger(T_cassie_lift_ban)
        $ player.go_to(L_map)

    elif not game.timer.is_dark():
        if M_cassie.is_state(S_cassie_medic_room):
            call expression game.dialog_select("pool_cassie_after_fun")
            $ M_cassie.trigger(T_cassie_end)
    else:

        call expression game.dialog_select("pool_closed_night")
    $ game.main()

label medic_room_dialogue:
    scene changeroom02
    if M_cassie.is_state(S_cassie_medic_room) and not M_cassie.get("had sex"):
        label medic_room_cassie_replay:
            if not store._in_replay is None:
                scene changeroom02
            call expression game.dialog_select("medic_room_dialogue_count_0")
        menu:
            "Ok, let's try it.":
                call expression game.dialog_select("medic_room_dialogue_count_0_lets_try")
                $ M_cassie.set("had sex", True)
                jump expression game.dialog_select("gloryhole_medic")

            "I don't feel like it." if store._in_replay is None:
                call expression game.dialog_select("medic_room_dialogue_count_0_do_not_feel_like_it")

    elif M_cassie.is_state(S_cassie_medic_room) and M_cassie.get("had sex"):
        call expression game.dialog_select("medic_room_dialogue_count_1")
        $ renpy.end_replay()
        $ persistent.cookie_jar["Cassie"]["unlocked"] = True
        $ persistent.cookie_jar["Cassie"]["gallery"]["01_unlocked"] = True
        show unlock19 at truecenter with dissolve
        pause
        hide unlock19 with dissolve

    elif M_cassie.is_state(S_cassie_end) and not M_cassie.get("had sex"):
        call expression game.dialog_select("medic_room_dialogue_count_2")
        menu:
            "I'd love to.":
                call expression game.dialog_select("medic_room_dialogue_count_2_love_to")
                $ M_cassie.set("had sex", True)
                jump expression game.dialog_select("gloryhole_medic")
            "Just changing.":

                call expression game.dialog_select("medic_room_dialogue_count_2_just_changing")
                if wearing_swimsuit:
                    $ wearing_swimsuit = False
                    $ changing_count = 0
                else:

                    $ wearing_swimsuit = True
                $ used_changing_girls = []
    else:

        call expression game.dialog_select("medic_room_dialogue_count_finished")
        $ M_cassie.set("had sex", False)
    jump expression game.dialog_select("pool_dialogue")

label poolrules_dialogue:
    scene pool
    if M_cassie.is_state(S_cassie_start):
        if not player.has_item("swimsuit"):
            call expression game.dialog_select("poolrules01_dialogue_pre")
            call expression game.dialog_select("poolrules01_dialogue_after")
            $ game.main()
        else:
            call expression game.dialog_select("poolrules02_dialogue")

    elif M_cassie.is_state(S_cassie_caught_skinny_dipping):
        call expression game.dialog_select("pool_cutscene01_dialogue")
        call expression game.dialog_select("pool_rescued_dialogue")
        $ M_cassie.trigger(T_cassie_drowning)
        $ M_player.set("first swim", False)
        jump expression game.dialog_select("medic_room_dialogue")
    else:

        if M_player.get("first swim"):
            call expression game.dialog_select("pool_cutscene01")
            call expression game.dialog_select("pool_rescued_dialogue")
            $ M_cassie.trigger(T_cassie_drowning)
            jump expression game.dialog_select("medic_room_dialogue")
        else:

            call expression game.dialog_select("pool_cutscene02")
            $ changing_count = 0
            if not ronda_after_swimming:
                call expression game.dialog_select("ronda_after_swimming")
                $ ronda_after_swimming = True
            else:

                jump expression game.dialog_select("pool_dialogue")

    hide player
    hide cassie
    with dissolve
    $ game.main()

label changing_dialogue:
    $ rand_girl = renpy.random.choice(changing_girls)
    scene changeroom01
    if wearing_swimsuit:
        call expression game.dialog_select("changing_dialogue_wearing_swimsuit")

    elif changing_count == 0:
        call expression game.dialog_select("changing_dialogue_occupied_pre")
        $ used_changing_girls.append(rand_girl)
        call expression game.dialog_select("changing_dialogue_occupied_after")
        $ changing_count = 1

    elif changing_count == 1:
        call expression game.dialog_select("changing_dialogue_occupied_pre")
        $ used_changing_girls.append(rand_girl)
        call expression game.dialog_select("changing_dialogue_occupied_after")
        $ changing_count = 2
        if M_cassie.is_state(S_cassie_start):
            $ M_cassie.trigger(T_cassie_ban_mc)
            call expression game.dialog_select("changing_caught")
            $ player.go_to(L_map)
            $ used_changing_girls = []
            $ game.main()

    elif changing_count == 2:
        call expression game.dialog_select("changing_dialogue_change")
        $ wearing_swimsuit = True
        $ changing_count = 3
        $ used_changing_girls = []
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
