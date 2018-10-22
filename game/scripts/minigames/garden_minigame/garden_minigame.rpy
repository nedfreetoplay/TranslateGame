label job_done_dialogue(earnings):
    $ renpy.checkpoint()
    if quest10 in quest_list and not infestation_done and player.has_item("annihilator"):
        scene black with dissolve
        with Pause(0.5)
        show expression Cutscene("garden_event01", "Я начал опрыскивать всю партию зеленым напалмом...\nОпустошил всю банку на мерзких педиков...\nПока ничего не осталось!") as cutscene with dissolve
        $ player.remove_item("annihilator")
        if player.has_item("exterminator"):
            $ player.remove_item("exterminator")

        if player.has_item("eradicator"):
            $ player.remove_item("eradicator")
        pause
        hide cutscene with dissolve

        scene black with dissolve
        with Pause(0.5)
        scene black
        with Dissolve(0.5)
        show unlock27 at truecenter with dissolve
        pause
        $ infestation_done = True
        $ aunt_dialogue_advance = True
        hide unlock27 with dissolve
        hide black
        $ game.main()

    if not garden_firsttime:
        scene black
        with Pause(0.5)
        call expression game.dialog_select("garden_firsttime_text")
        pause
        scene black with dissolve
        with Pause(0.5)
        $ garden_firsttime = True
    if quest10 in quest_list and not infestation_done:
        scene garden_dead
    else:

        scene garden
    if earnings > 0:
        show player 1 at left with dissolve
        show diane 2 at right with dissolve
        dia "О, Вау! Мой сад выглядит просто великолепно, {b}[firstname]{/b}!"
        show player 1 at left
        show diane 9 at right
        player_name "Да... Мне пришлось избавиться от многих вещей..."
        show diane 15 at right
        show player 11 at left
        dia "Только посмотрите на этот большой, твердый огурец!"
        show diane 16 at right
        player_name "..."
        show diane 5 at right
        show player 13 at left
        dia "Спасибо, Красавчик! И возвращайся поскорее!"
        hide player 13 at left with dissolve
        hide diane 5 at right with dissolve
    else:

        call expression game.dialog_select("garden_firsttime_fail")
    $ game.timer.tick()
    if earnings < 0:
        $ earnings = 0
    $ player.get_money(earnings)
    $ after_minigame = True
    $ garden_done += 1
    show unlock7 at truecenter
    show text "{size=30}{b}[earnings]{/b}{/size}" at Position(xpos = 485,ypos = 413)
    with dissolve
    play audio coins1
    $ renpy.pause()
    hide text "{b}[earnings]{/b}"
    hide unlock7
    with dissolve
    $ in_garden = True
    call expression game.dialog_select("garden_dialogue")

label garden_firsttime_text:
    show expression Cutscene("garden_firsttime_01", "{b}Диана{/b} пошла прилечь, когда я начал копать её сад.\n Было так жарко снаружи, и было так много сорняков и Жуков!\nЯ стиснул зубы и поставил перед собой задачу...\n... Надеюсь, она хорошо заплатит мне за весь этот физический труд!") as cutscene with dissolve
    pause
    hide cutscene with dissolve
    scene black with dissolve
    with Pause(0.5)
    show expression Cutscene("garden_firsttime_02", "Когда я работал, я заметил, что {b}Диана{/b} пристально наблюдает за мной...\nПолагаю, она просто пыталась убедиться, что я хорошо работаю.\nМы обменялись парой слов здесь и там, но в основном просто болтали.\nЕе глаза были устремлены на мое промокшее от пота тело.") as cutscene with dissolve
    pause
    hide cutscene with dissolve
    return

label garden_firsttime_fail:
    show player 5 at left with dissolve
    show diane 23 at right with dissolve
    dia "Хм... Есть место для улучшений."
    show diane 24 at right
    show player 24 at left
    player_name "Да... У меня не очень хорошо получалось. Прости {b}Диана{/b}!"
    show diane 3 at right
    show player 13 at left
    dia "Все нормально... Ты в этом деле новенький..."
    show diane 2 at right
    dia "И я уверен, что у тебя получится лучше!"
    dia "Мне всегда нужны свежие овощи..."
    show diane 1 at right
    show player 10 at left
    player_name "Думаю, да..."
    show diane 14 at right
    show player 11 at left
    dia "Просто убедитесь, что ты взял {b}только{/b} {b}длинные{/b} и {b}твердые{/b} овощи!"
    show diane 1 at right
    show player 13 at left
    player_name "В следующий раз получится лучше..."
    player_name "Спасибо {b}Диана{/b}!"
    hide player 13 at left with dissolve
    hide diane 1 at right with dissolve
    return

label garden_listing:
    call screen garden_minigame
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
