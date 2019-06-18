label trailer_lock_check(destination_screen):
    scene expression player.location.background_blur
    $ destination = destination_screen.lower()
    $ destination_label = destination + "_dialogue"
    if M_roxxy.is_state(S_roxxy_studying_at_roxxys) and not game.timer.is_dark() and destination == "trailer":
        show player 34 with dissolve
        player_name "( Я договорился с {b}Рокси{/b} встретиться здесь {b}вечером{/b}. Нужно подождать. )"
        hide player with dissolve

    elif M_roxxy.is_state(S_roxxy_studying_at_mcs) and destination not in ["trailer", "trailer_park"]:
        if destination == "trailer_interior" and not M_roxxy.get("heard clyde in trailer"):
            $ M_roxxy.set("heard clyde in trailer", True)
            scene trailer_interior_c
            show crystal 12 at right
            show clyde 17 at left
            with dissolve
            clyde "Боже, {b}Тётя{/b}! Придержи коней!"
            show clyde 16
            show crystal 13
            crys "За меня не парься!"
            crys "Я этим занимаюсь с того самого как ты родился."
            show crystal 12
            show clyde 17
            clyde "Я просто говорю, ты ж щас облажаешься со счётом!"
            show clyde 16
            show crystal 13
            crys "Сиди на жопе ровно и дай {b}тёте{/b} всё расшарить!"
            show crystal 12
            player_name "( Хмм, они... Ничего себе! Да здесь целая кипа денег! )"
            player_name "( Каким чёртом они их достали? )"
            player_name "( Лучше смываться, пока меня не заметили! )"
            scene black with fade
        else:
            scene expression player.location.background_blur
            show player 34 with dissolve
            player_name "( Хмм, нет... )"
            player_name "( Мне нужно догнать {b}Рокси{/b}! )"
            hide player with dissolve
        $ game.main()
    elif M_roxxy.is_state(S_roxxy_get_uniform_on_doggo):
        if not player.has_item("roxxy_uniform") and destination not in ["trailer_park", "trailer_shack", "shack_doghouse"]:
            if destination == "trailer_shack_interior":
                scene expression "backgrounds/location_trailer_shack_day_blur.jpg"
                player_name "( Хмм, эта {b}свинья{/b} должна быть где-то неподалёку... )"
                jump expression destination_label
            else:
                show player 12 with dissolve
                player_name "Мне нужно найти {b}свинью Клайда{/b}."
                show player 10
                player_name "В первую очередь нужно поискать рядом с его {b}лачугой{/b}."
                hide player with dissolve
        elif destination not in ["trailer_park", "trailer"] and player.has_item("roxxy_uniform"):
            show player 10 with dissolve
            player_name "Я должен следовать за {b}Рокси{/b} назад к {b}её трейлеру{/b}."
            hide player with dissolve
        else:
            if destination in ["trailer_interior", "trailer_bedroom", "trailer_shack_interior"]:
                $ playSound()
                play audio sfxDoor()
            jump expression destination_label
    elif M_roxxy.is_state(S_roxxy_beat_clyde) and destination not in ["trailer_park", "trailer_tractor"]:
        show player 10 with dissolve
        player_name "Хмм, я должен следовать за {b}Рокси{/b}..."
        player_name "Она говорила что-то о {b}тракторе{/b}?"
        hide player with dissolve
    elif M_roxxy.is_state(S_roxxy_wait_in_her_room) and destination not in ["trailer", "trailer_interior", "trailer_bedroom"]:
        if destination == "roxxy_trailer_button":
            show player 5 at left
            show roxxy 1 at right
            with dissolve
            player_name "..."
            show roxxy 3c
            rox "Серьёзно, прекрати пялиться и иди подожди в моей комнате!"
            show roxxy 1b
            rox "Я скоро подойду."
            show roxxy 1
            show player 10
            player_name "Да, хорошо."
            hide roxxy
            hide player
            with dissolve
        else:
            show player 14 with dissolve
            player_name "Мне нужно подождать {b}Рокси{/b} в её комнате."
            hide player with dissolve
    elif M_roxxy.is_state(S_roxxy_confront_clyde) and destination not in ("trailer_park", "trailer_tractor", "trailer_shack"):
        show player 10 with dissolve
        player_name "( {b}Рокси{/b} выбежала вслед за {b}Клайдом{/b}! )"
        player_name "( Я должен найти их, пока {b}она{/b} его не придушила! )"
        hide player with dissolve
    elif M_roxxy.is_state(S_roxxy_picnic_done) and destination != "trailer_bedroom":
        show player 13 at left
        show player_wet at left
        with dissolve
        player_name "( Я должен пойти просушиться с {b}Рокси{/b} в её комнате! )"
        hide player
        hide player_wet
        with dissolve
    else:
        if destination in ["trailer_interior", "trailer_bedroom", "trailer_shack_interior"]:
            $ playSound()
            play audio sfxDoor()
        jump expression destination_label
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
