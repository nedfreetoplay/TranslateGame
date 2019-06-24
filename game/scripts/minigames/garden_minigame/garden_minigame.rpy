label job_done_dialogue(earnings):
    $ renpy.checkpoint()
    if M_diane.between_states(S_diane_bug_infested_garden, S_diane_clear_bug_infested_garden):
        scene garden_dead
    elif M_diane.finished_state(S_diane_barn_news):
        scene expression "backgrounds/location_barn_garden_day_blur.jpg"
    else:
        scene garden

    if M_diane.is_state(S_diane_clean_garden):
        scene garden_dead
        show player 14 with dissolve
        player_name "Пфу!"
        player_name "Ладно, думаю, я наконец-то все понял..."
        show player 31f with dissolve
        player_name "..."
        show player 32f
        player_name "Итак, куда {b}Диана{/b} улизнула?"
        player_name "Должно быть, она вошла внутрь..."
        hide player with dissolve
        $ M_diane.trigger(T_diane_cleaned_garden)

    elif M_diane.is_state(S_diane_drunken_garden_work):
        call expression game.dialog_select("dianes_garden_diane_drunk_like_a_sailor")
        $ M_diane.trigger(T_diane_drunken_massage)
        $ game.timer.tick(3)
        $ player.go_to(L_map)

    elif M_diane.is_state(S_diane_get_bug_spray, S_diane_clear_bug_infested_garden) and player.has_item("annihilator"):
        scene black with dissolve
        with Pause(0.5)
        show expression "backgrounds/location_diane_garden_cutscene03.jpg"
        show expression FilteredText("Я начал все опрыскивать зеленым напалмом...\n Опустошил всю банку спрея на противных жуков...\nПока ничего не осталось!") as cutscene at Position (xpos= 512, ypos = 700)
        with fade
        $ player.remove_item("annihilator")
        if player.has_item("exterminator"):
            $ player.remove_item("exterminator")

        if player.has_item("eradicator"):
            $ player.remove_item("eradicator")
        pause
        hide cutscene
        scene black
        with dissolve
        pause 0.5
        show unlock27 at truecenter with dissolve
        pause
        hide unlock27 with dissolve
        hide black
        $ M_diane.trigger(T_diane_use_bug_spray_on_garden)
        scene garden
        show player 13 at left
        show diane f_normal_talk a_dressed_blush
        with dissolve
        dia "Ну и ну, что за денек!"
        show diane f_normal a_dressed_shovel with dissolve
        show player 14
        player_name "Хех, я знаю... Я очень устал."
        player_name "Однако мы все закончили."
        show player 13
        show diane f_normal_talk
        dia "Конечно."
        show diane f_laugh
        dia "Это будет даже лучше, чем было раньше!"
        show diane a_dressed_finger with dissolve
        dia "Подожди и увидишь!"
        show diane f_normal a_dressed_shovel with dissolve
        show player 14
        player_name "Хе-хе, я надеюсь на это."
        show player 13
        show diane f_normal_talk
        dia "Спасибо за помощь сегодня, жеребец."
        show diane f_normal
        show player 17
        player_name "С удовольствием!"
        hide player
        show diane kiss
        with dissolve
        pause
        show player 13 at left
        show diane f_normal_talk
        dia "Передай привет {b}Дебби{/b} от меня."
        show diane f_normal
        show player 14
        player_name "Передам."
        hide player
        hide diane
        with dissolve
        $ game.timer.tick(2)
        $ M_diane.trigger(T_diane_inform_diane)

    elif M_diane.is_state(S_diane_work_on_garden):
        scene expression "backgrounds/location_diane_garden_closeup.jpg"
        show player 13 at right
        show diane f_normal_talk at flip
        with dissolve
        dia "Эй, это выглядит великолепно!"
        show diane f_normal
        show player 22
        player_name "!!!" with hpunch
        show player 29f with dissolve
        player_name "Привет, {b}Диана{/b}."
        show player 3f at Position (xoffset=-8)
        show diane f_normal_talk
        dia "Прости, что меня не было здесь, чтобы поприветствовать тебя..."
        show diane f_thinking
        dia "... были срочные дела."
        show diane f_cheese
        show player 10f
        player_name "... О, да?"
        show player 14f
        show diane f_normal
        player_name "Я имею в виду... Хех, не беспокойся!"
        show player 29f with dissolve
        player_name "Я здесь ... эмм ..."
        show player 3f at Position (xoffset=-8)
        pause
        show diane f_smirk_talk
        dia "... Работаешь?"
        show diane f_smirk
        show player 29f
        player_name "Да!"
        show player 3f at Position (xoffset=-8)
        show diane f_laugh
        dia "Хехе?"
        show diane f_normal_talk
        dia "С чего это ты вдруг такой косноязычный?"
        show diane f_normal
        show player 29f
        player_name "Ничего..."
        player_name "Я только... эмм..."
        show player 3f at Position (xoffset=-8)
        show diane f_normal_talk
        dia "Ну, сад действительно выглядит великолепно!"
        dia "Я думаю, это даже лучше, чем было до фиаско с уховерткой!"
        show diane grab_cucumber with dissolve
        show player 428f with dissolve
        dia "Только посмотрите на этих красавцев!"
        player_name "..."
        show diane a_dressed_cucumber_touch f_normal_talk with dissolve
        show player 11f
        dia "Какой монстр!"
        show diane a_dressed_cucumber_rub with dissolve
        dia "И он действительно ухабистый!"
        show diane f_cheese
        show player 78f with dissolve
        pause
        show player 81f
        player_name "!!!" with hpunch
        show diane f_normal_talk a_dressed_cucumber_touch with dissolve
        dia "С такими овощами мне, возможно, придется дать вам-"
        show diane f_surprised_down
        dia "Приииибааавку!"
        dia "!!!"
        show diane f_surprised
        player_name "..."
        dia "..."
        show player 79f with dissolve
        player_name "Я эээ..."
        show player 78f with dissolve
        show diane f_surprised_down
        dia "... Так?"
        show diane f_surprised
        show player 83f
        player_name "Я должен идти!!"
        show player 78f with dissolve
        show diane f_laugh
        dia "Подожди!"
        show player 81f
        player_name "Пока, {b}Диана{/b}!"
        hide player with dissolve
        pause
        show diane f_sad_talk
        dia "{b}[firstname]{/b}?!"
        show diane f_sad
        dia "..."
        hide diane with dissolve
        scene expression "backgrounds/location_diane_front_day_blur.jpg"
        show player 83 with dissolve
        player_name "О, боже..."
        player_name "Не могу поверить, что у меня стояк перед {b}Дианой{/b}!"
        player_name "Это было так неловко!"
        player_name "Я должен выбраться отсюда!"
        hide player with dissolve
        $ game.timer.tick(2)
        $ player.go_to(L_map)
        $ M_diane.trigger(T_diane_worked_on_garden)

    elif M_diane.get("garden first time"):
        if earnings > 0:
            scene black
            with Pause(0.5)
            call expression game.dialog_select("garden_firsttime_text")
            pause
            scene black with dissolve
            with Pause(0.5)
            scene expression player.location.background_blur with None
            show player 1 at left
            show diane f_normal_talk at lright
            with dissolve
            dia "О, вау! Мой сад выглядит абсолютно великолепно, {b}[firstname]{/b}!"
            show player 2
            show diane f_smirk
            player_name "Да... Мне пришлось избавиться от многих вещей..."
            show diane a_dressed_cucumber f_teasing_look with dissolve
            show player 11
            dia "Только посмотрите на этот большой, твердый огурец!"
            show diane f_smirk
            player_name "..."
            show player 10
            player_name "Почему вам нужны только овощи, которые длинные и твердые?"
            show player 5
            show diane f_shamed_talk_smile
            dia "Я эээ..."
            show diane f_shamed_talk_look
            dia "Ну, понимаешь, они... эээ..."
            show diane f_shamed
            show player 10
            player_name "Они продают лучше или что-то?"
            show player 5
            show diane f_laugh
            dia "Да!! Верно!"
            show diane f_teasing_look
            dia "Они продают лучше."
            show diane f_smirk
            show player 12
            player_name "Хмм, иетересно."
            show player 14
            player_name "Думаю, мне еще многое предстоит узнать об овощах..."
            show player 13
            show diane f_normal_talk a_dressed_shovel with dissolve
            dia "Ну, не волнуйся, {b}[firstname]{/b}."
            dia "Я могу научить тебя всему, что нужно знать о садоводстве."
            show diane f_normal
            show player 14
            player_name "Как ты вообще во все это ввязалась?"
            show player 13
            show diane f_normal_talk
            dia "О, у меня всегда было немного зеленого пальца. Даже когда я была ребенком."
            show diane f_normal
            show player 14
            player_name "Правда?"
            show player 13
            show diane f_laugh
            dia "Еще бы!"
            show diane f_normal_talk
            dia "Знаешь, я мечтала о собственной ферме..."
            show diane f_normal
            show player 14
            player_name "Как для настоящей фермы? С полями сельскохозяйственных культур и животных?"
            show player 13
            show diane f_normal_talk
            dia "Вот именно! Я хотела целых Девять ярдов!"
            show diane f_normal
            show player 14
            player_name "Ты должна это сделать, {b}Диана{/b}!"
            show player 17
            player_name "Я помогу тебе!"
            show player 13
            show diane f_laugh
            dia "Ха-ха, ну да, спасибо {b}[firstname]{/b}... Боюсь, это не так просто, как кажется."
            show diane f_normal
            show player 14
            player_name "Да, полагаю, ты права."
            show diane f_laugh
            show player 13
            dia "Спасибо за твою помощь сегодня!"
            show diane f_normal_talk
            dia "Почему бы тебе не вернуться завтра, и мы продолжим с того места, где остановились?"
            show diane f_normal
            show player 14
            player_name "Хорошо, тогда увидимся завтра."
            show player 13
            show diane f_smirk_talk
            dia "Пока, красавчик."
            hide player
            hide diane
            with dissolve
        else:
            call expression game.dialog_select("garden_firsttime_fail")
        $ M_diane.set("garden first time", False)
    $ game.timer.tick()
    if earnings < 0:
        $ earnings = 0
    $ after_minigame = True
    $ player.get_money(earnings)
    call screen money_popup(earnings, "garden")
    with dissolve
    if M_daisy.is_state(S_daisy_pizza_craving):
        call expression game.dialog_select("barn_front_daisy_pizza_craving")
        $ M_daisy.trigger(T_daisy_find_food)
        $ player.go_to(L_diane_barn_interior)
        $ game.main()
    $ game.main()

label garden_firsttime_text:
    show expression "backgrounds/location_diane_garden_cutscene01.jpg"
    show expression FilteredText("{b}Diane{/b} went to lie down as I began digging up her garden.\n It was so hot outside and there were so many weeds and bugs!\nI grit my teeth and set myself to the task...\n... I hope she's planning to pay me well for all this physical labor!") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with dissolve
    pause 0.5
    show expression "backgrounds/location_diane_garden_cutscene02.jpg"
    show expression FilteredText("Пока я работал, я заметил, что {b}Диана{/b} пристально наблюдает за мной...\nПолагаю, она просто хотела убедиться, что я хорошо поработал.\nМы перекинулись парой слов, но в основном просто болтали.\nЕе глаза, казалось, были устремлены на меня.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    scene black
    hide cutscene
    with dissolve
    return

label garden_firsttime_fail:
    scene expression player.location.background_blur with None
    show player 5 at left
    show diane f_sad_talk
    with dissolve
    dia "Хм... Есть место для улучшений."
    show diane f_sad
    show player 24 at left
    player_name "Да... У меня не очень хорошо получалось. Прости {b}Диана{/b}!"
    show diane f_shamed_talk_smile
    show player 13 at left
    dia "Все нормально... Ты в этом новичок..."
    show diane f_laugh
    dia "И я уверена, что у тебя получится лучше!"
    show diane f_normal_talk
    dia "Мне всегда нужны свежие овощи..."
    show diane f_normal
    show player 10 at left
    player_name "Думаю, да..."
    show player 5
    show diane f_smirk_talk a_dressed_finger with dissolve
    dia "Просто убедись, что остались {b}только{/b} {b}длинные{/b} и {b}твердые{/b} овощи!"
    show diane f_normal a_dressed_shovel with dissolve
    show player 10
    player_name "В следующий раз будет лучше..."
    show player 14
    player_name "Спасибо {b}Диана{/b}!"
    hide player
    hide diane
    with dissolve
    return

label garden_listing:
    call screen garden_minigame
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
