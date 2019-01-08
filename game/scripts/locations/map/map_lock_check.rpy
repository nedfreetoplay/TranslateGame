label map_lock_check(destination_screen, destination_label):
    $ jump_dest_screen = destination_screen
    $ jump_dest_label = destination_label
    scene expression L_map.background_blur
    if M_dewitt.is_state(S_dewitt_eve_karaoke) and destination_screen == "Erik":
        call map_lock_check_destination_jump (jump_dest_screen, jump_dest_label)

    elif M_mia.get_state() in [S_mia_midnight_help, S_mia_locked_room] and destination_screen == "Mia":
        call map_lock_check_destination_jump (jump_dest_screen, jump_dest_label)

    elif not M_mia.is_set("church night locked") and game.timer.is_evening() and destination_screen == "Church":
        call map_lock_check_destination_jump (jump_dest_screen, jump_dest_label)

    elif M_roxxy.is_state(S_roxxy_sneak_into_smith) and destination_screen != "Smith" and game.timer.is_dark():
        show player 10 with dissolve
        player_name "Я должен пойти в дом {b}Директрисы Смит{/b} сейчас."
        hide player with dissolve

    elif M_roxxy.is_state(S_roxxy_sneak_into_smith) and destination_screen == "Smith" and not game.timer.is_dark():
        show player 10 with dissolve
        player_name "Я не могу пойти туда прямо сейчас!"
        hide player with dissolve

    elif M_roxxy.is_state(S_roxxy_meeting_clyde) and destination_screen == "Trailer Park":
        call map_lock_check_destination_jump (jump_dest_screen, jump_dest_label)

    elif game.timer.is_evening() and ((not player.has_item("master_key") and destination_screen == "School") or destination_screen in ["Warehouse", "Mall", "Library"]):
        scene expression game.timer.image("townmap{}")
        if destination_screen == "School":
            call expression game.dialog_select("school_no_master_key_locked")
        else:

            call expression game.dialog_select("night_locked")

    elif game.timer.is_night() and ((not player.has_item("master_key") and destination_screen == "School") or destination_screen not in ["Home", "Beach House", "Smith"]):
        scene expression game.timer.image("townmap{}")
        if destination_screen == "School":
            call expression game.dialog_select("school_no_master_key_locked")
        else:

            call expression game.dialog_select("night_locked")
    else:

        call map_lock_check_destination_jump (jump_dest_screen, jump_dest_label)
    $ game.main()

label map_lock_check_destination_jump(destination_screen, destination_label):
    $ playMusic()
    if destination_screen == "School" and erik.started(erik_intro):
        pass
    elif destination_screen in ["School", "Diane", "Pool", "Mall", "Bank", "Pier", "Forest", "Police", "Beach", "Hospital"]:
        $ playSound()
    if destination_screen == "Home":
        $ in_sis_room = False
    if destination_screen == "Pool":
        $ wearing_swimsuit = False
        $ changing_count = 0
    jump expression destination_label

label night_locked:
    player_name "Я не могу пойти туда ночью!"
    return

label school_no_master_key_locked:
    player_name "Я не могу пойти в школу ночью!"
    player_name "Может если я {i}одолжу{/i} тот {b}Мастер-Ключ{/b} которым Энни открыла мой шкафчик..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
