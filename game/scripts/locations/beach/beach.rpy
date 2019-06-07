label beach_dialogue:
    $ player.go_to(L_beach)
    if getPlayingSound("<loop 2>audio/ambience_beach.ogg"):
        $ playSound("<loop 2>audio/ambience_beach.ogg")
    if M_roxxy.is_state(S_roxxy_spin_bottle) and game.timer == Date("afternoon", "saturday"):
        if player.has_item("goldschwagger"):
            call expression game.dialog_select("beach_roxxy_spin_bottle_goldschwagger")
            $ game.timer.tick()
            $ player.remove_item("goldschwagger")
            $ M_roxxy.trigger(T_roxxy_spun_bottle)
        else:
            call expression game.dialog_select("beach_roxxy_spin_bottle_no_goldschwagger")
            $ player.go_to(L_map)

    elif M_roxxy.is_state(S_roxxy_spin_bottle) and game.timer == Date("evening", "saturday"):
        call expression game.dialog_select("beach_roxxy_spin_bottle_wrong_time")
        $ player.go_to(L_map)
    $ game.main()

label sara_bikini_picked_up:
    scene expression "backgrounds/location_beach_water_contest_closeup.jpg"
    if M_roxxy.is_state(S_roxxy_get_new_bikini):
        show player 655 with dissolve
        player_name "Hmm..."
        show player 655b
        player_name "It's a little small for {b}Roxxy{/b} but it might do the trick."
        show player 655
        player_name "..."
        show player 655b
        player_name "I can't believe {b}Miss Sara{/b} was wearing this tiny thing!"
        player_name "Hmm, I doubt she'd mind if I borrow it for awhile."
        player_name "I should take it to {b}Roxxy{/b} and see what she thinks..."
        hide player with dissolve
        $ player.get_item("sara_bikini")
    else:
        show player 655 with dissolve
        player_name "( Hmm... )"
        show player 655b
        player_name "( It's miss sara's bikini... )"
        show player 655
        player_name "( I should pick it up to return it to her )"
        show player 655b
        $ player.get_item("sara_bikini")
    $ game.main()

label beach_island_dialogue:
    $ player.go_to(L_beach_island)
    if M_aqua.is_state(S_aqua_treasure_search):
        call expression game.dialog_select("beach_island_aqua_treasure_search")
    $ game.main()

label beach_water_dialogue:
    $ player.go_to(L_beach_water)
    if M_roxxy.is_state(S_roxxy_invite_to_bikini_contest) and game.timer == Date("afternoon", "saturday"):
        call expression game.dialog_select("beach_roxxy_invite_to_bikini_contest")
        $ M_roxxy.trigger(T_roxxy_go_see_contest)

    elif M_roxxy.get("roxxy locker sex") >= 1 and not (M_roxxy.get("roxxy beach sex") or M_becca.get("becca beach sex") or M_missy.get("missy beach sex") or M_player.get("mc beach sex")) and player.location.is_here(M_roxxy):
        call expression game.dialog_select("beach_roxxy_spin_bottle_sex_intro")
        $ M_player.set("beach bottle spins", 0)
        call screen spin_bottle_minigame
    $ game.main()

label beach_tower_dialogue:
    $ player.go_to(L_beach_tower)
    if M_roxxy.is_state(S_roxxy_get_oil) and not player.has_item("massage_oil"):
        call expression game.dialog_select("beach_tower_roxxy_get_oil")
    $ game.main()

label beach_cabin_dialogue:
    $ player.go_to(L_beach_cabin)
    if M_roxxy.is_state(S_roxxy_in_cabin):
        call expression game.dialog_select("beach_cabin_roxxy_in_cabin")
        $ M_roxxy.trigger(T_roxxy_bikini_failure)
        $ player.go_to(L_beach_water)

    elif M_roxxy.is_state(S_roxxy_get_new_bikini):
        if player.has_item("sara_bikini"):
            call expression game.dialog_select("beach_cabin_roxxy_has_bikini")
            $ M_roxxy.trigger(T_roxxy_get_oil)
            $ player.remove_item("sara_bikini")
            $ player.go_to(L_beach_water)
        else:

            call expression game.dialog_select("beach_cabin_roxxy_get_new_bikini")
            $ player.go_to(L_beach_water)

    elif M_roxxy.is_state(S_roxxy_get_oil):
        if player.has_item("massage_oil"):
            call expression game.dialog_select("beach_cabin_roxxy_has_oil")
            $ M_roxxy.trigger(T_roxxy_contest_over)
            $ game.timer.tick()
            $ player.go_to(L_beach_water)
        else:

            call expression game.dialog_select("beach_cabin_roxxy_get_oil")
            $ player.go_to(L_beach_water)

    elif M_roxxy.get("massage"):
        label roxxy_massage_hscene_replay:
            call expression game.dialog_select("beach_cabin_roxxy_massage")
        $ renpy.end_replay()
        $ persistent.cookie_jar["Roxxy"]["unlocked"] = True
        $ persistent.cookie_jar["Roxxy"]["gallery"]["04_unlocked"] = True
        $ M_roxxy.set("massage", False)
        $ game.timer.tick()
        $ player.go_to(L_beach_water)
    $ game.main()

label beach_showers_dialogue:
    $ player.go_to(L_beach_showers)
    $ game.main()

label beach_tower_oil_pickup:
    scene expression "backgrounds/location_beach_tower_day_blur.jpg"
    show player 657b with fastdissolve
    player_name "This is it!"
    player_name "Yessssssss!!!"
    hide player with fastdissolve
    $ player.get_item("massage_oil")
    $ game.main()

label beach_statue:
    if not player.has_item("shovel"):
        call expression game.dialog_select("beach_statue_no_shovel")
        $ game.main()

    if M_aqua.is_state(S_aqua_treasure_search):
        call expression game.dialog_select("beach_statue_aqua_treasure_search")
        $ M_aqua.trigger(T_aqua_treasure_found)

    if not M_aqua.is_state([S_aqua_treasure_search, S_aqua_treasure_unlock]):
        jump expression game.dialog_select("treasure_unlocked")

    call expression game.dialog_select("treasure_lock_intro")
    call screen treasure_lock

label treasure_open:
    if not player.has_item("treasure_key"):
        call expression game.dialog_select("treasure_open_no_key")
    else:

        $ player.remove_item("treasure_key")
        jump expression game.dialog_select("treasure_unlocked")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
