label milking_game_pre:
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 13 at left
    show diane b_naked a_naked_sides f_normal_talk
    with dissolve
    dia "Вот он где."
    show diane f_smirk_talk
    dia "Ты готов попробовать эту новую установку доения?"
    show diane f_smirk
    show player 10
    menu:
        "Конечно!":
            player_name "П-прямо сейчас?"
            show player 13
            show diane f_laugh
            dia "Нет времени лучше настоящего."
            show diane f_smirk
            show player 14
            player_name "Хорошо."
            show player 13
            show diane f_smirk_talk
            dia "Слава Богу."
            dia "Эти малышки вот-вот лопнут!"
            show diane f_smirk
            $ M_diane.set("sex_pre_milking", False)
            call screen milking_minigame
        "Не сейчас.":

            player_name "Прости {b}Диана{/b}, Я не могу прямо сейчас."
            show diane f_sad
            show diane f_sad_talk with dissolve
            dia "Ооо... Очень плохо! "
            dia "Эти малышки вот-вот лопнут!"
            dia "Думаю, тогда я сама обо всем позабочусь..."
            show player 13
            show diane f_sad
            player_name "Я сделаю это в следующий раз!"
            player_name "Береги себя, {b}Диана{/b}!"
            $ game.timer.tick()
    $ game.main()

label milking_game_pre_after_sex:
    show diane f_smirk b_naked a_naked_sides
    show player 365
    player_name "Да?"
    show player 366
    show diane f_smirk
    dia "Мммммм!"
    show diane f_smirk_talk
    dia "Меня никогда так никто не трахал, {b}[firstname]{/b}!"
    dia "Хе-хе, мои ноги сейчас как желе..."
    show diane f_smirk
    show player 365
    player_name "Хехе."
    show player 366
    pause
    show diane f_smirk_talk
    dia "Фу, ты должен подоить меня, прежде чем мы пойдем домой."
    show diane f_smirk
    show player 365
    menu:
        "Конечно!":
            player_name "Да?"
            show player 366
            show diane f_smirk_talk
            dia "Определенно."
            dia "В книге сказано, что я буду производить больше молока сразу после сеанса размножения."
            show diane f_smirk
            show player 365
            player_name "Хорошо."
            show player 366
            show diane f_smirk_talk
            dia "Просто будь нежным, {b}[firstname]{/b}."
            hide player
            hide diane
            with dissolve
            $ M_diane.set("sex_pre_milking", True)
            call screen milking_minigame
        "Не сейчас.":

            show player 366
            player_name "Прости {b}Диана{/b}, У меня нет своббодного времени."
            show diane f_sad
            show diane f_sad_talk with dissolve
            dia "Ооо... Очень плохо! "
            dia "Эти малышки вот-вот лопнут!"
            dia "Думаю, тогда я сама обо всем позабочусь..."
            show player 365
            show diane f_sad
            player_name "Я сделаю это в следующий раз!"
            player_name "Береги себя, {b}Диана{/b}!"
            $ game.timer.tick()
    $ game.main()

label milking_minigame_done_daisy(earnings):
    scene expression player.location.background_blur with None
    show player 17 at left
    show daisy f_shy_down b_naked_shy a_naked_shy_front at Position (yoffset=10)
    with dissolve
    player_name "Все готово!"
    show player 1b
    show daisy f_shy_normal_talk at Position (yoffset=10)
    daisy "Ой, уже?"
    show daisy f_shy_normal at Position (yoffset=10)
    show player 14b
    player_name "Не думаю, что у тебя там что-то осталось..."
    show player 1b
    show daisy f_shy_normal_talk at Position (yoffset=10)
    daisy "Да, хорошо..."
    daisy "Можешь подоить меня позже, {b}[firstname]{/b}?"
    show daisy f_shy_normal at Position (yoffset=10)
    show player 14b
    player_name "Конечно, если хочешь."
    show player 1b
    show daisy f_laugh b_naked a_naked_up with dissolve
    daisy "Да, пожалуйста!"
    daisy "Так хорошо, когда ты это делаешь."
    show daisy f_normal a_naked_sides with dissolve
    pause
    hide player
    show daisy b_naked_hug f_empty a_empty
    with dissolve
    daisy "Спасибо, {b}[firstname]{/b}!"
    daisy "Ты самый лучший человек на свете!"
    show player 14b at left
    show daisy b_naked a_naked_sides f_normal
    with dissolve
    player_name "Пожалуйста."
    player_name "Мне, наверное, стоит начать другую работу."
    show player 1b
    show daisy f_normal_talk
    daisy "Хорошо, {b}[firstname]{/b}."
    show daisy f_normal
    show player 14b
    player_name "Увидимся позже, {b}Дейзи{/b}."
    show player 1b
    show daisy f_laugh
    daisy "Пооокааа!"
    hide player with dissolve
    pause
    show daisy f_normal

    pause
    hide daisy with dissolve
    $ player.get_money(earnings)
    $ game.timer.tick()
    $ M_daisy.trigger(T_daisy_milked)
    $ game.main()

label milking_minigame_fail_daisy:
    scene expression player.location.background_blur with None
    show player 24 at left
    show daisy f_sad_talk
    with dissolve
    daisy "Ты в порядке, {b}[firstname]{/b}?"
    show daisy f_sad
    player_name "Да."
    show player 10b
    player_name "Думаю, я просто немного не в своей тарелке сегодня..."
    show player 5b
    show daisy f_normal_talk
    daisy "Хе-хе, все в порядке."
    show daisy f_normal
    show player 10b
    player_name "Ты должна пойти и попросить {b}Диану{/b} закончить с тобой."
    show player 5b
    show daisy f_sad_talk
    daisy "Я должна?"
    show daisy f_sad
    show player 10b
    player_name "Да, мне не очень-то везет..."
    show player 5b
    pause
    show player 10b
    player_name "Прости, {b}Дейзи{/b}."
    show player 5b
    show daisy f_normal_talk
    daisy "Ааа... Все хорошо."
    daisy "Пооокааа {b}[firstname]{/b}!"
    hide daisy
    hide player
    with dissolve
    $ game.timer.tick()
    $ game.main()

label milking_minigame_done(earnings):
    scene expression "backgrounds/location_barn_day_blur.jpg"
    if M_diane.between_states(S_diane_return_production_book, S_diane_return_outfit_package):
        scene expression "backgrounds/location_barn_day_blur.jpg"
        show player 13 at left
        show diane f_laugh b_shirtless a_shirtless_sides
        with dissolve
        dia "Фу!"
        dia "Так намного лучше!"
        show diane f_cheese
        pause
        show diane f_normal_talk
        dia "Спасибо, {b}[firstname]{/b}."
        show diane f_normal
        show player 17
        player_name "Пожалуйста."
        show player 13
        show diane f_normal_talk
        dia "Я не знаю, ты ли это или это новое оборудование, но это был самый гладкий сеанс доения, который у меня когда-либо был."
        dia "Только посмотри на все это молоко!"
        show diane f_normal
        show player 14
        player_name "Да, у тебя там было его много."
        show player 13
        show diane f_laugh
        dia "Хехе!"
        show diane f_normal_talk
        dia "Продолжайте в том же духе, и мы выполним Мои заказы без проблем!"
        show diane f_normal
        pause
        show diane f_normal_talk
        dia "Я собираюсь пойти дальше и дать тебе твою долю сейчас."
        show diane f_normal
        show player 5
        player_name "Хмм?"
        show diane f_normal_talk a_shirtless_money with dissolve
        dia "Вот."
        show diane f_normal b_shirtless a_shirtless_sides
        show player 640e
        with dissolve
        player_name "Ты заплатишь мне за это?"
        show player 13 with dissolve
        show diane f_normal_talk
        dia "Ну, конечно."
        dia "Это же работа."
        show diane f_normal
        show player 14
        player_name "Да, но-"
        show player 13
        show diane f_smirk_talk
        dia "Поверь мне, твои волшебные руки стоят каждого пенни."
        show diane f_smirk
        show player 14
        player_name "Ты уверена?"
        show player 13
        show diane f_smirk_talk
        dia "Ага."
        show diane f_normal_talk
        dia "Просто помни, что у тебя также есть сад, и о нем надо заботиться."
        show diane f_normal
        show player 14
        player_name "Я помню."
        show player 13
        show diane f_normal_talk
        dia "Ну, тогда тебе лучше заняться им."
        show diane f_normal
        show player 14
        player_name "Спасибо, {b}Диана{/b}."
        show player 13
        show diane f_normal_talk
        dia "Пожалуйста, красавчик."
        hide player
        hide diane
        with dissolve

        $ game.timer.tick()
    else:

        if M_diane.is_set("breed first time"):
            if M_diane.get("sex_pre_milking"):
                show player 365 at left
            else:
                show player 14 at left
            show diane b_naked a_naked_sides f_smirk
            with dissolve
            player_name "Так много молока!"
            if M_diane.get("sex_pre_milking"):
                show player 366
            else:
                show player 13
            show diane f_smirk_talk
            dia "Да, много."
            dia "Ты сделал все правильно, {b}[firstname]{/b}!"
            show diane f_smirk
            if M_diane.get("sex_pre_milking"):
                show player 365
            else:
                show player 14
            player_name "Спасибо!"
            hide player
            if M_diane.get("sex_pre_milking") or M_diane.outfit == "cow":
                show diane kiss_both_naked at Position (xoffset=-217)
            else:
                show diane kiss_shirtless
            with dissolve
            dia "Ммм."
            pause
            if M_diane.get("sex_pre_milking"):
                show player 366 at left
            else:
                show player 13 at left
            show diane b_naked a_naked_sides f_smirk_talk
            with dissolve
            dia "Мне нужно привести себя в порядок."
            show diane f_smirk
            if M_diane.get("sex_pre_milking"):
                show player 365
            else:
                show player 14
            player_name "Да, хорошо."
            if M_diane.get("sex_pre_milking"):
                show player 366
            else:
                show player 13
            show diane f_smirk_talk
            dia "Мы будем делать это часто, {b}[firstname]{/b}..."
            show diane f_laugh
            dia "... И я имею в виду, МНОГО!"
            show diane f_smirk
            if M_diane.get("sex_pre_milking"):
                show player 365
            else:
                show player 14
            player_name "Хе, хорошо."
            player_name "Увидимся дома?"
            if M_diane.get("sex_pre_milking"):
                show player 366
            else:
                show player 13
            show diane f_smirk_talk
            dia "Еще бы."
            hide player
            hide diane
            with dissolve
            $ M_diane.set("breed first time", False)
            $ player.go_to(L_map)
            $ game.timer.tick(2)
        else:

            if M_diane.get("sex_pre_milking"):
                show player 366 at left
            else:
                show player 13 at left
            show diane b_naked a_naked_sides f_smirk_talk
            with dissolve
            dia "Отличная работа, красавчик."
            show diane f_smirk
            if M_diane.get("sex_pre_milking"):
                show player 365
            else:
                show player 14
            player_name "Спасибо!"
            hide player
            if M_diane.get("sex_pre_milking") or M_diane.outfit == "cow":
                show diane kiss_both_naked at Position (xoffset=-217)
            else:
                show diane kiss_shirtless
            with dissolve
            pause
            if M_diane.get("sex_pre_milking"):
                show player 365 at left
            else:
                show player 14 at left
            show diane b_naked a_naked_sides f_smirk
            with dissolve
            player_name "Увидимся вечером дома?"
            if M_diane.get("sex_pre_milking"):
                show player 366
            else:
                show player 13
            show diane f_smirk_talk
            dia "Еще бы!"
            hide player
            hide diane
            with dissolve
            $ game.timer.tick()
    $ player.get_money(earnings)
    show expression "boxes/popup_minigame_07.png" as popup_milking at truecenter
    show text "{size=30}{b}[earnings]{/b}{/size}" at Position(xpos = 485,ypos = 413)
    with dissolve
    play audio coins1
    $ renpy.pause()
    hide text "{b}[earnings]{/b}"
    hide popup_milking
    with dissolve
    $ game.main()

label milking_minigame_fail:
    scene expression "backgrounds/location_barn_day_blur.jpg"
    if M_diane.get("sex_pre_milking"):
        show player 368 at left
    else:
        show player 5 at left
    if M_diane.between_states(S_diane_barn_news, S_diane_return_outfit_package):
        $ M_diane.outfit = "shirtless"
    show diane f_sad_talk b_naked a_naked_sides
    with dissolve
    dia "Что ж, это было разочаровывающе..."
    show diane f_sad
    if M_diane.get("sex_pre_milking"):
        show player 367
    else:
        show player 10
    player_name "Прости, {b}Диана{/b}."
    player_name "Я не знаю, что случилось."
    if M_diane.get("sex_pre_milking"):
        show player 368
    else:
        show player 5
    show diane f_shamed_talk_smile
    dia "Все в порядке, красавчик."
    dia "Наверное, у меня просто выходной."
    show diane f_shamed
    pause
    show diane f_shamed_talk_smile
    dia "Мы можем попробовать позже, хорошо?"
    show diane f_shamed
    if M_diane.get("sex_pre_milking"):
        show player 367
    else:
        show player 10
    player_name "Да, хорошо."
    hide player
    hide diane
    with dissolve
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
