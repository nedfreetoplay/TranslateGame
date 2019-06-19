label hallway_dialogue:
    $ player.go_to(L_home_hallway)
    if getPlayingSound("<loop 1>audio/ambience_shower_hallway.ogg") and game.in_shower is not None:
        $ playSound("<loop 1>audio/ambience_shower_hallway.ogg")

    if M_jenny.is_state(S_jenny_start) and not game.timer.is_dark():
        call expression game.dialog_select("hallway_jenny_start")
        call screen jen_name_input
        if jen_char_name.strip() == "":
            $ jen_char_name = "Jenny"
        $ config.replay_scope["jen_char_name"] = jen_char_name
        $ persistent.jen_char_name = jen_char_name
        $ jen = Character("[jen_char_name]", color="#ff6df0")
        $ M_jenny.trigger(T_jenny_hallway)

    elif M_jenny.is_state(S_jenny_hallway_eavesdropping) and game.timer.is_dark():
        call expression game.dialog_select("hallway_jenny_hallway_eavesdropping")
        $ M_jenny.trigger(T_jenny_eavesdropped)
        $ player.spend_money(100)

    elif M_jenny.is_state(S_jenny_confront_her_hallway):
        call expression game.dialog_select("hallway_jenny_confront_her_hallway")
        $ M_jenny.trigger(T_jenny_wait_a_day)

    elif M_jenny.is_state(S_jenny_caught_talking_to_camslut) and game.timer.is_tick(2, 3):
        call expression game.dialog_select("hallway_jenny_caught_talking_to_camslut")
        $ game.timer.tick()
        $ player.go_to(L_home_bedroom)
        $ M_jenny.trigger(T_jenny_beaten_up_with_dildo)
        $ game.main()

    elif M_jenny.is_state(S_jenny_hallway_talk) and game.timer.is_morning():
        call expression game.dialog_select("hallway_jenny_hallway_talk")
        $ M_jenny.trigger(T_jenny_diary_clue)
        $ game.timer.tick()
        $ game.main()

    if L_home_shower.is_here(M_jenny) and not game.timer.is_dark() and not M_jenny.get("seen_in_shower"):
        call expression game.dialog_select("hallway_jenny_in_shower")
        $ M_jenny.set("seen_in_shower", True)

    if M_mom.is_state(S_mom_sis_boobs_afterthoughts) and not game.timer.is_dark():
        call expression game.dialog_select("hallway_mom_sis_boobs_afterthoughts")
        $ M_mom.trigger(T_mom_sis_nice_boobs)

    elif M_mom.is_state([S_mom_shower_peek, S_mom_shower_walk_in]) and L_home_shower.is_here(M_mom) and not game.timer.is_dark():
        scene hallway
        show player 14 with dissolve
        player_name "( Кто-то принимает душ? )"
        player_name "( Интересно, если это {b}[deb_name]{/b}. )"
        show player 26
        player_name "(  Может быть, я могу заглянуть немного... )"
        hide player with dissolve

    elif M_mom.is_state(S_mom_sleepover_offer) and game.timer.is_evening():
        call expression game.dialog_select("hallway_mom_sleepover_offer")
        $ M_mom.trigger(T_mom_sleepover_accept)

    elif M_mom.is_state(S_mom_movie_night_two) and game.timer.is_evening():
        call expression game.dialog_select("hallway_mom_movie_night_two")
        $ M_mom.trigger(T_mom_movie_invite)


    if M_jenny.finished_state(S_jenny_cheerleader_sex) and M_mom.get('sex available') and game.timer.is_morning() and not M_jenny.get("jenny_debbie_acknowlegement"):
        call expression game.dialog_select("hallway_jenny_acknowleges_debbie_sex")
        $ M_jenny.set("jenny_debbie_acknowlegement", M_jenny.get("diary_index") + 1)

    $ game.main()

label attic_entry_dialogue:
    if not L_home_attic.locked:
        jump expression game.dialog_select("attic_dialogue")

    elif player.has_picked_up_item("attic_key") and player.has_picked_up_item("stool"):
        scene expression game.timer.image("hallway{}")
        $ player.remove_item("attic_key")
        $ player.remove_item("stool")
        $ L_home_attic.unlock()
        show expression "boxes/popup_attic.png" at truecenter with dissolve
        pause
        hide expression "boxes/popup_attic.png" with dissolve
        jump expression game.dialog_select("attic_entry_dialogue")
    else:

        scene expression game.timer.image("hallway{}")
        show player 34 with dissolve
        player_name "Хмм..."
        show player 35
        if not player.has_picked_up_item("stool"):
            player_name "( Мне нужно {b}стоять{/b} на чём то для открытия... )"
        else:
            player_name "( Этот маленький люк {b}заперт{/b}. )"
        jump expression game.dialog_select("hallway_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
