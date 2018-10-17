default attic_unlocked = False

label hallway_dialogue:
    $ player.go_to(L_home_hallway)
    if getPlayingSound("<loop 1>audio/ambience_shower_hallway.ogg") and game.in_shower is not None:
        $ playSound("<loop 1>audio/ambience_shower_hallway.ogg")

    if not game.timer.is_dark():
        if hallway_count == 0:
            label jenny_intro:
            call expression game.dialog_select("hallway_sis_start")
            call screen jen_name_input
            if jen_char_name.strip() == "":
                $ jen_char_name = "Джени"
            $ config.replay_scope["jen_char_name"] = jen_char_name
            $ persistent.jen_char_name = jen_char_name
            $ jen = Character("[jen_char_name]", color="#ff6df0")
            $ hallway_count = 1

        elif M_mom.is_state(S_mom_sis_boobs_afterthoughts):
            call expression game.dialog_select("hallway_mom_sis_boobs_afterthoughts")
            $ M_mom.trigger(T_mom_sis_nice_boobs)

        elif sister.started(sis_hallway01) and sister.over(sis_shower_cuddle02):
            call expression game.dialog_select("hallway_sis_hallway_1_started")
            $ sis_hallway01.finish()
            $ sister.add_event(sis_couch01)

        elif sister.started(sis_hallway02) and sister.over(sis_telescope02) and M_mom.is_set("jerk available"):
            call expression game.dialog_select("hallway_sis_hallway_2_started")
            $ sis_hallway02.finish()
            $ sister.add_event(sis_shower_cuddle03)

        elif sister.started(sis_final) and sister.completed(sis_shower_cuddle04):
            call expression game.dialog_select("hallway_sis_final_started")


        elif sister.over(sis_final) and not sister.known(sis_final2):
            call expression game.dialog_select("hallway_sis_final_over")
            $ sister.add_event(sis_final2)

        if L_home_shower.is_here(M_jenny) and (
                sister.started(sis_shower_cuddle01) or
                sister.started(sis_shower_cuddle02) or
                sister.started(sis_shower_cuddle03) or
                sister.started(sis_shower_cuddle04) or
                sister.started(sis_shower_cuddle05)
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
            player_name "( Мне нужно {b}стоят{/b} на чём либо до открытия... )"
        else:
            player_name "( Эта маленькая люк {b}заперт{/b}. )"
        jump expression game.dialog_select("hallway_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
