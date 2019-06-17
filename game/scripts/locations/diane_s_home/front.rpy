label dianes_front_yard_dialogue:
    $ player.go_to(L_diane_yard)
    if M_diane.is_state(S_diane_seen_cucumber):
        call expression game.dialog_select("dianes_front_seen_cucumber")
        $ M_diane.trigger(T_diane_cucumber_aftermath)
    $ game.main()

label dianes_front_yard_night_locked:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "{b}Диана{/b} уже наверное спит..."
    hide player with dissolve
    return

label dianes_front_seen_cucumber:
    scene expression "backgrounds/location_diane_front_day_blur.jpg"
    show player 83b with dissolve
    player_name "Вау!!!"
    player_name "Я понятия не имел, что {b}Диана{/b} была такой..."
    player_name "Я имею в виду... Она мастурбирует у себя на кухне!"
    player_name "... С огурцом!"
    show player 78 at Position (xoffset=50) with dissolve
    player_name "!!!"
    show player 79 with dissolve
    player_name "Я должен эээ... .. Наверное..."
    player_name "... Я не могу позволить {b}Диане{/b} увидеть меня в таком виде!"
    player_name "{b}Лучше всего начать с огорода.{/b} Это отвлечет меня от всяких мыслей."
    hide player with dissolve
    return

label locked_shed_dialogue:
    if M_diane.finished_state(S_diane_fetch_pump):
        scene garden
        show player 10 at left with dissolve
        player_name "{b}Диана{/b}?"
        show player 5
        dia "Секундочку!"
        player_name "..."
        show diane b_shirtless a_shirtless_sides f_normal
        show player 11
        player_name "!!!"
        show diane f_normal_talk
        dia "Что случилось, красавчик?"
        show diane f_normal
        show player 10
        player_name "Где твоя рубашка?"
        show player 5
        show diane f_surprised_front a_shirtless_shock with dissolve
        dia "Хмм?"
        show diane f_thinking_back a_shirtless_sides with dissolve
        dia "О, я сняла ее, потому что ... .. Ну..."
        dia "... Тут действительно жарко."
        show diane f_normal
        show player 14
        player_name "Да, верно!"
        show player 13
        show diane f_normal_talk
        dia "Тебе что-нибудь нужно?"
        show diane f_normal
        menu diane_shed_locked_menu:
            "Нужна какая-нибудь помощь?":
                show player 10 at left
                show diane f_normal
                with dissolve
                player_name "Тебе нужна помощь?"
                show player 13
                show diane f_laugh
                dia "Хехе, нет у меня все под контролем."
                show diane f_smirk_talk
                dia "TСпасибо за предложение, жеребец."
                show diane f_normal
                jump diane_shed_locked_menu
            "Ничего.":

                show player 14 at left
                show diane f_normal
                with dissolve
                player_name "Я просто проверял тебя."
                player_name "Здесь так тихо..."
                show player 13
                show diane f_laugh
                dia "Хех, да. Я просто сосредоточена."
                dia "Фу,там как в духовке!"
                show diane f_normal
                show player 14
                player_name "Знаешь, ты можешь оставить дверь открытой, если хочешь..."
                player_name "Это поможет справиться с жарой."
                show player 13
                show diane f_thinking_back
                dia "О, ммм..."
                dia "Нет, все в порядке."
                show diane f_laugh
                dia "Я лучше работаю в одиночестве."
                show diane f_normal
                show player 14
                player_name "Хмм, хорошо."
                player_name "Думаю, я покину тебя тоже."
                show player 13
                show diane f_normal_talk
                dia "Спасибо, {b}[firstname]{/b}."
                hide player
                hide diane
                with dissolve
                $ game.main()
    else:

        if M_diane.get("seen_shed_locked"):
            call expression game.dialog_select("dianes_shed_seen_shed_locked")
        else:

            call expression game.dialog_select("dianes_shed_not_seen_shed_locked")
            $ M_diane.set("seen_shed_locked", True)
    $ game.main()

label night_closed_garden:
    if M_diane.is_state(S_diane_get_bug_spray, S_diane_clear_bug_infested_garden):
        scene garden_dead_night
    else:
        scene garden_night
    show player 10 with dissolve
    if not M_diane.get("breed first time") and not game.timer.is_night():
        player_name "{b}Диана{/b} сказала, что она будет в {b}сарае{/b}."
    else:
        player_name "{b}Диана{/b}, наверное, спит... Не думаю, что смогу сейчас работать в саду."
    hide player 2 with dissolve
    return


label diane_house_lock_check(location):
    if location.locked:
        if game.timer.is_dark():
            if location is L_diane_home:
                call expression game.dialog_select("dianes_front_yard_night_locked")
            else:
                call expression game.dialog_select("night_closed_garden")
        else:

            if location is L_diane_kitchen:
                call expression game.dialog_select("dianekitchen_locked")

            elif location is L_diane_home:
                call expression game.dialog_select("dianelobby_locked")

            elif location is L_diane_shed:
                if M_dewitt.is_state(S_dewitt_shed_get_paint):
                    $ game.main(location = location)
                else:
                    jump locked_shed_dialogue

    elif M_diane.is_state(S_diane_check_up_on_garden) and location is L_diane_home:
        call expression game.dialog_select("diane_check_up_on_garden")

    elif M_diane.is_state(S_diane_look_in_kitchen) and player.location is L_diane_garden and location is L_diane_kitchen:
        call expression game.dialog_select("dianes_kitchen_locked")

    elif M_diane.is_state(S_diane_seen_cucumber) and location is L_diane_kitchen:
        call expression game.dialog_select("dianes_kitchen_busy_masturbating")

    elif M_diane.is_state(S_diane_work_on_garden) and (location is L_diane_home or location is L_diane_kitchen):
        call expression game.dialog_select("diane_attend_to_garden")

    elif M_diane.is_state(S_diane_delivery_2_task, S_diane_delivery_2_fetch_goods, S_diane_delivery_2) and (location is L_diane_home or location is L_diane_kitchen):
        call expression game.dialog_select("diane_tired_from_delivery_upkeep")

    elif M_diane.is_state(S_diane_debbie_drop_off) and location is L_diane_home and game.timer.is_dark():
        call expression game.dialog_select("diane_debbie_drop_off")

    elif M_diane.is_state(S_diane_check_shed_light) and not location is L_diane_shed:
        call expression game.dialog_select("diane_shed_light_on")

    elif M_diane.is_state(S_diane_drunken_garden_work):
        call expression game.dialog_select("diane_day_off_gardening")

    elif M_diane.is_state(S_diane_milking_help) and not (location is L_diane_garden or location is L_diane_shed):
        call expression game.dialog_select("diane_milk_jug_pain")

    elif game.timer.is_dark() and (location is L_diane_home or location is L_diane_kitchen):
        if location is L_diane_home:
            call expression game.dialog_select("dianes_front_yard_night_locked")
        else:
            call expression game.dialog_select("night_closed_garden")
    else:

        if location is L_diane_shed:
            play audio "audio/sfx_door_heavy.ogg"

        elif (not ((player.location is L_diane_kitchen and location is L_diane_home) or
              (player.location is L_diane_home and location is L_diane_kitchen) or
              (player.location is L_diane_yard and location is L_diane_garden) or
              (player.location is L_diane_garden and location is L_diane_yard))):
            play audio sfxDoor()
        $ location.call()
    $ game.main()

label dianes_kitchen_locked:
    scene expression player.location.background_blur
    show player 30 with dissolve
    player_name "Хмм?"
    player_name "Закрыто."
    player_name "{b}Диана{/b} никогда не запирает эту дверь днем..."
    show player 34
    player_name "..."
    show player 35
    player_name "Я должен пойти попробовать через {b}входную дверь{/b}."
    hide player with dissolve
    return

label dianes_kitchen_busy_masturbating:
    $ M_diane.set("sex speed",0.4)
    show diane_masturbate 1_2
    dia "Нггхххх..."
    dia "Не останавливайся, жеребец!"
    pause
    player_name "( Я должен убраться отсюда, пока она меня не увидела. )"
    pause
    return

label diane_check_up_on_garden:
    scene expression player.location.background_blur
    show player 30 with dissolve
    player_name "Я должен {b}проверить огород.{/b}"
    hide player with dissolve
    return

label diane_attend_to_garden:
    scene expression player.location.background_blur
    show player 79 with dissolve
    player_name "Я должен {b}начать работать в саду.{/b}"
    hide player with dissolve
    return

label diane_tired_from_delivery_upkeep:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "Я должен дать ей отдохнуть..."
    show player 17
    player_name "... Кроме того, мне нужно сделать доставку молока!"
    show player 14
    player_name "Я должен взять пакет из {b}сарае Дианы{/b} и {b}доставить его по соседству.{/b}"
    hide player with dissolve
    return

label diane_debbie_drop_off:
    scene expression player.location.background_blur
    show player 13 with dissolve
    player_name "( ... )"
    pause
    show player 5
    player_name "( Почему она не открывает дверь? )"
    player_name "( Конечно, она больше не работает... )"
    player_name "( ... )"
    player_name "( {b}Я лучше пойду проверю сарай.{/b} )"
    hide player with dissolve
    return

label diane_shed_light_on:
    scene expression player.location.background_blur
    show player 12 with dissolve
    player_name "Мне нужно найти {b}Диану{/b}."
    hide player with dissolve
    return

label diane_day_off_gardening:
    scene expression player.location.background_blur
    show player 14 with dissolve
    player_name "{b}Я должен начать работать в саду.{/b}"
    hide player with dissolve
    return

label diane_milk_jug_pain:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "Что-то не так с {b}Дианой{/b}!"
    player_name "{b}Я должен немедленно проверить ее в сарае!{b}"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
