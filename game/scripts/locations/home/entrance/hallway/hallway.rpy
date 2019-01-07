default attic_unlocked = False

label hallway_dialogue:
    $ player.go_to(L_home_hallway)
    if getPlayingSound("<loop 1>audio/ambience_shower_hallway.ogg") and game.in_shower is not None:
        $ playSound("<loop 1>audio/ambience_shower_hallway.ogg")

    if not game.timer.is_dark():
        if M_jenny.is_state(S_jenny_start):
            call expression game.dialog_select("hallway_jenny_start")
            call screen jen_name_input
            if jen_char_name.strip() == "":
                $ jen_char_name = "Джени"
            $ config.replay_scope["jen_char_name"] = jen_char_name
            $ persistent.jen_char_name = jen_char_name
            $ jen = Character("[jen_char_name]", color="#ff6df0")
            $ M_jenny.trigger(T_jenny_hallway)

        elif M_mom.is_state(S_mom_sis_boobs_afterthoughts):
            call expression game.dialog_select("hallway_mom_sis_boobs_afterthoughts")
            $ M_mom.trigger(T_mom_sis_nice_boobs)

        elif M_jenny.is_state(S_jenny_hallway_meetup):
            call expression game.dialog_select("hallway_sis_hallway_1_started")
            $ M_jenny.trigger(T_jenny_hallway_chat)

        elif M_jenny.is_state(S_jenny_hallway_meetup_focus):
            call expression game.dialog_select("hallway_sis_hallway_2_started")
            $ M_jenny.trigger(T_jenny_hallway_chat_focus)

        elif M_jenny.is_state(S_jenny_hallway_noises):
            call expression game.dialog_select("hallway_sis_final_started")

        elif M_jenny.is_state(S_jenny_overhear_caught):
            call expression game.dialog_select("hallway_sis_final_over")
            $ M_jenny.trigger(T_jenny_stream_idea)

        if L_home_shower.is_here(M_jenny) and (
                M_jenny.is_state(S_jenny_shower_peep_bed_cuddle) or
                M_jenny.is_state(S_jenny_shower_peep_bed_cuddle_tier_2) or
                M_jenny.is_state(S_jenny_shower_peep_bed_cuddle_tier_3) or
                M_jenny.is_state(S_jenny_shower_peep_bed_cuddle_tier_4) or
                M_jenny.is_state(S_jenny_shower_peep_bed_cuddle_tier_5)
        ):
            scene hallway
            show player 14 at left
            with dissolve
            player_name "( Кто-то принимает душ. )"
            show player 26
            player_name "( Думаю, они оставили дверь незапертой... )"
            hide player
            with dissolve

        elif M_mom.is_state([S_mom_shower_peek, S_mom_shower_walk_in]) and L_home_shower.is_here(M_mom):
            scene hallway
            show player 14 with dissolve
            player_name "( Кто-то принимает душ? )"
            player_name "( Интересно, если это {b}[deb_name]{/b}. )"
            show player 26
            player_name "( Может быть, я могу заглянуть немного... )"
            hide player with dissolve
    else:

        if M_mom.is_state(S_mom_sleepover_offer) and not game.timer.is_night():
            call expression game.dialog_select("hallway_mom_sleepover_offer")
            $ M_mom.trigger(T_mom_sleepover_accept)

        elif M_mom.is_state(S_mom_movie_night_two) and game.timer.is_evening():
            call expression game.dialog_select("hallway_mom_movie_night_two")
            $ M_mom.trigger(T_mom_movie_invite)

    $ game.main()

label attic_entry_dialogue:
    if attic_unlocked:
        jump expression game.dialog_select("attic_dialogue")

    elif player.has_picked_up_item("attic_key") and player.has_picked_up_item("stool"):
        scene expression game.timer.image("hallway{}")
        $ player.remove_item("attic_key")
        $ player.remove_item("stool")
        $ attic_unlocked = True
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
