label home_lock_check(destination_screen, destination_label):
    $ temp_bg = player.location.background_blur

    if M_mom.is_set("bedroom locked") and destination_screen == "Master Bedroom":
        scene expression temp_bg
        if not game.timer.is_dark():
            if not erik.over(erik_intro):
                show player 22 at left
                show debbie 2 at right
                with dissolve
                deb "{b}[firstname]{/b}? Что ты ищешь в моей комнате?"
                show player 21 at left
                show debbie 1 at right
                player_name "Я... ммм... Ищу свой телефон!"
                show player 18 at left
                player_name "Ааа, вот он, в кармане!"
                show debbie 3 at right
                show player 11 at left
                deb "Разве {b}Erik{/b} не ждет тебя?"
                show debbie 1 at right
                show player 17 at left
                player_name "Да, уже иду!"
            else:

                show player 10 with dissolve
                player_name "( Я не должен рыскать в спальне {b}[deb_name]{/b}. )"
            $ game.main()
        else:


            if M_mom.is_state(S_mom_debt_call):
                show player 10 with dissolve
                player_name "( Я должен убедится, что {b}[deb_name]{/b} в порядке. )"
            else:

                show player 10 with dissolve
                player_name "( Я действительно не должен беспокоить  {b}[deb_name]{/b} ,когда она спит. )"
            $ game.main()
        hide player
        hide debbie
        with dissolve

    elif (M_mom.is_state([S_mom_romance_movie, S_mom_romance_movie_two]) or (M_mom.is_set("movie night") and game.timer.is_dark())) and destination_screen == "Living Room TV":
        jump mom_movie_night

    elif sister.started(sis_breakfast) and destination_screen not in ["Dining Room", "Dining Room Table Sis"]:
        scene expression temp_bg
        show player 11 at left
        show debbie 2 at right
        with dissolve
        if destination_screen == "Mom":
            deb "Твой завтрак готов в {b}столовой{/b}, милый..."
            show player 14
            show debbie 1
            player_name "Спасибо, {b}[deb_name]{/b}! Пойду, поем."
        else:

            deb "Что ты делаешь? Твой завтрак готов в {b}столовой{/b}, милый..."
            show player 14
            show debbie 1
            player_name "Извени, {b}[deb_name]{/b}! Пойду, поем."
        hide player
        hide debbie
        with dissolve

    elif not game.timer.is_dark() and sister.started(sis_final) and destination_screen not in ["Hallway", "Upstairs Bedroom"]:
        scene expression temp_bg
        show player 11 with dissolve
        player_name "( Я действительно хочу знать, с кем разговаривает {b}[jen_name]{/b}. )"
        show player 4 at Position(xpos=518)
        player_name "( Может быть, я смогу подкрасться к ее двери и узнать... )"
        hide player with dissolve

    elif M_mia.is_state(S_mia_midnight_call, S_mia_urgent_message) and game.new_message and player.location == L_home_bedroom:
        scene expression temp_bg
        if not game.timer.is_dark():
            show player 12 with dissolve
        else:
            show player 101 with dissolve
        player_name "Я должен проверить свои сообщения."

    elif M_bissette.is_state(S_bissette_roxxy_jenny_spying) and destination_screen not in ["Hallway", "Upstairs Bedroom"]:
        scene expression temp_bg
        show player 10 with dissolve
        player_name "Я должен проверить {b}Roxxy{/b} и {b}[jen_name]{/b}..."
        hide player with dissolve

    elif M_mom.is_state(S_mom_note) and player.location == L_home_bedroom and destination_screen not in ["MC Computer"]:
        scene expression temp_bg
        show player 10 with dissolve
        player_name "( Я должен посмотреть, что на этой {b}записке{/b}. )"
        hide player with dissolve

    elif not sister.over(sis_couch01) and destination_screen == "Living Room TV":
        scene expression temp_bg
        show popup_tv_locked at truecenter with dissolve
        pause
        hide popup_tv_locked with dissolve

    elif sis_door_locked_count == 0 and destination_screen == "Upstairs Bedroom":
        scene expression temp_bg
        show player 12 with dissolve
        play audio sfxDoor(True)
        player_name "( Дверь закрыта... )"
        hide player with dissolve

    elif game.timer.is_night() and destination_screen == "Upstairs Bedroom":
        scene expression temp_bg
        show player 24 with dissolve
        player_name "( Я очень устал. Пойду лучше спать... )"
        hide player with dissolve
    else:

        if player.location == L_home and destination_screen in ["Home Entrance", "Garage"]:
            $ playSound()
            play audio sfxDoor()
        if player.location in [L_home_entrance, L_home_hallway]:
            $ playSound()
        if destination_screen in ["Master Bedroom", "Upstairs Bedroom", "Shower", "Bedroom"]:
            play audio sfxDoor()
        if player.location in [L_home_bedroom, L_home_sisbedroom, L_home_shower, L_home_mombedroom] and destination_screen in ["Hallway", "Living Room"]:
            play audio sfxDoor()
        jump expression destination_label

    hide jersey
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
