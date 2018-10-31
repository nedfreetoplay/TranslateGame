label coach_locker_dialogue:
    if player.has_picked_up_item("master_key"):
        if M_bissette.is_state(S_bissette_roxxy_pom_poms):
            if player.has_item("pompoms"):
                jump expression game.dialog_select("coachs_office_locker_peeking")
            else:

                call expression game.dialog_select("coachs_locker_bissette_roxxy_pom_poms")
        python:
            for image in renpy.get_showing_tags():
                renpy.hide(image)
        call screen coachs_locker
    else:

        if M_bissette.is_state(S_bissette_roxxy_pom_poms):
            call expression game.dialog_select("coachs_locker_locked_bissette_roxxy_pom_poms")
        else:

            call expression game.dialog_select("coachs_locker_locked")
    $ game.main()

label coachs_locker_bissette_roxxy_pom_poms:
    show coach_locker
    player_name "Вот они!"
    return

label coachs_locker_locked_bissette_roxxy_pom_poms:
    show expression game.timer.image("coach_office{}_b")
    show player 12 with dissolve
    player_name "Держу пари что они в этом шкафу."
    player_name "Похоже мне нужен ключ чтобы туда войти."
    hide player with dissolve
    return

label coachs_locker_locked:
    show expression game.timer.image("coach_office{}_b")
    show player 1 with dissolve
    player_name "Шкафчик Тренера Бриджит закрыт. Я не могу его открыть так как у меня нет ключа."
    hide player with dissolve
    return

label coachs_office_roxxy_pom_poms_right_time:
    show player 30 with dissolve
    player_name "Хорошо,её здесь нет."
    show player 14
    player_name "Это мой шанс найти эти {b}Помпоны{/b}!"
    show player 3f with dissolve
    player_name "..."
    show player 38 at Position (xoffset=41) with dissolve
    player_name "Сейчас где же они могут быть?"
    hide coach
    hide player
    with dissolve
    return

label coachs_office_roxxy_pom_poms_wrong_time:
    show coach 8 at right
    show player 23 at left
    with dissolve
    player_name "Вот дерьмо! Она здесь!"
    show player 22
    show coach 10
    bri "Я могу тебе помочь?"
    show coach 8
    show player 10
    player_name "Эээ, эммм..."
    show player 11
    show coach 10
    bri "Да?"
    show coach 8
    show player 21
    player_name "Нет,Я просто..."
    show player 27
    show coach 9
    bri "..."
    show coach 8
    show player 29
    show xtra 21 at left
    with dissolve
    player_name "Извините меня,мне нужно в туалет!"
    hide player
    hide xtra
    with dissolve
    show coach 10
    bri "Что за чудак..."
    hide coach
    hide player
    with dissolve
    return

label coachs_office_roxxy_pom_poms:
    scene expression game.timer.image("coach_office{}_b")
    if game.timer.is_morning():
        call expression game.dialog_select("coachs_office_roxxy_pom_poms_right_time")
    else:

        call expression game.dialog_select("coachs_office_roxxy_pom_poms_wrong_time")
        $ player.go_to(L_school_righthallway)
    return

label coach_locker_pom_poms:
    show coach_locker
    player_name "Круто!"
    call expression game.dialog_select("coach_locker_pom_poms_dialogue")
    $ player.get_item("pompoms")

    $ player.location.call_screen(False)

label coach_locker_pom_poms_dialogue:
    show expression "boxes/popup_item_pompom1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_pompom1.png" with dissolve

    scene expression game.timer.image("coach_office{}_b")
    show player 14 with dissolve
    player_name "Сейчас мне только нужно отнести их назад к {b}Рокси{/b}-"
    show player 11
    bri "ДА, да! Просто направляйся по трассе и Я там тебя встречу."
    bri "Сначала Я должна переодеться ."
    show player 22
    player_name "!!!" with hpunch
    show player 23
    player_name "Вот дерьмо! Она придет!"
    player_name "Я умру от страха! Что мне делать!?"
    player_name "Я должен спрятаться где-нибудь!"
    hide player with dissolve
    return

label coachs_office_locker_hide_fail:
    call expression game.dialog_select("coachs_office_locker_hide_fail_dialogue")

    $ M_bissette.trigger(T_bissette_bridget_pompoms_steal)
    $ player.go_to(L_school_righthallway)
    $ game.main()

label coachs_office_locker_hide_fail_dialogue:
    scene expression game.timer.image("coach_office{}_b")
    show coach 3 at Position (xpos=850)
    show player 22 at left
    with dissolve
    bri "Что ты здесь делаешь?"
    show coach 7
    show player 23
    player_name "Я... эм..."
    show player 29 with dissolve
    player_name "Это... не уборная?"
    show player 22 with dissolve
    show coach 4
    bri "Уберай свою тощую задницу отсюда!"
    show coach 7
    show player 23
    player_name "Уже В пути!"
    hide player with dissolve
    show coach 10 at right with dissolve
    bri "Чудила."
    hide coach with dissolve
    return

label coachs_office_locker_peeking:
    call expression game.dialog_select("coachs_office_locker_peeking_dialogue")

    $ M_bissette.trigger(T_bissette_bridget_pompoms_steal)
    $ game.main()

label coachs_office_locker_peeking_dialogue:
    scene expression game.timer.image("coach_office{}_b")
    show player 10 with dissolve
    player_name "Это единственное место где можно спрятаться!"
    player_name "Мне просто нужно надеятся что она не заглянет сюда."
    hide player with dissolve

    scene coach_locker_cs1
    with fade
    show text "Здесь довольно тесно но я смог попать в шкафчик и закрыть дверь.\nКак раз вовремя,когда {b}Тренер Бриджит{/b} почти поймала меня!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve

    scene coach_locker_cs2
    with fade
    show text "Все что ядолжен сейчас сделать это сидеть тихо и надеяться что она не найдем меня." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve

    scene coach_locker_peek
    show coach 1
    show coach_locker_peek_overlay
    with dissolve
    player_name "( Вот она! )"
    player_name "( Пожалуйста не смотри сюда... )"
    pause
    show coach 2
    bri "Мэн, уверена что то там готовят снаружи."
    bri "Я вспотела как шлюха в церкви!"
    show coach 11 with dissolve
    player_name "( Она раздевается! )"
    player_name "( Я труп если она найдет меня! )"
    show coach 12 with dissolve
    pause
    show coach 13 at Position (xoffset=37) with dissolve
    bri "Мммм, Я думаю что ты обращал внимания!"
    player_name "( Она знает?! )"
    pause
    show coach 14 at Position (xoffset=51) with dissolve
    bri "Я бы хотела что бы ты пропустил оружейную выстовку!"
    player_name "( ... )"
    pause
    bri "Проклятая девченка!"
    bri "Лучше убрать это прежде чем они ранят кого-нибудь."
    show coach 12 with dissolve
    player_name "( Что за извращенка... )"
    show coach 11 with dissolve
    pause
    show coach 9 with dissolve
    pause
    show coach 10
    bri "Хмм. Кажется я что то слышала."
    bri "Наверно это мое воображение..."
    hide coach with dissolve
    pause
    pause
    player_name "( Думаю что она ушла. )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
