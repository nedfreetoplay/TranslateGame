label ross_office_first_visit:
    scene school_office3_b with fade
    show player 11 with dissolve
    player_name "*Нюхает*"
    show player 12
    player_name "Что это за запах?"
    player_name "Как будто...благовония...и травы..."
    player_name "{b}Miss Ross{/b} наверняка проводит много времени здесь."
    hide player with dissolve
    return

label ross_hscene_start:
    $ M_ross.set ("sex speed", 0.15)
    if M_ross.is_state(S_ross_paint_with_body):
        call expression game.dialog_select("ross_office_hscene")
        call expression game.dialog_select("ross_hscene_first_time")
    else:
        $ persistent.cookie_jar["Ross"]["gallery"]["02_unlocked"] = True
        scene location_school_office3_closeup_sex
        show rosss 1 at right
        with dissolve
    jump ross_hscene_loop

label ross_office_hscene:
    scene expression game.timer.image("backgrounds/location_school_office3_closeup{}.jpg")
    show ross 13 at Position(xpos=0.35, ypos=1.0)
    show player 1f at Position(xpos=0.85, ypos=1.0)
    with dissolve
    ross "Вот мой маленький герой!"
    show ross 12
    show player 2f
    player_name "Вау,это пахнет очень хорошо здесь!"
    show ross 13
    show player 1f
    ross "Тебе это нравится? Это моя любимая благовония."
    ross "Это действительно повышает настроение не думаешь?"
    show ross 12
    show player 10f
    player_name "Эмм, Конечно. Я думаю..."
    player_name "А замем это гиганское полотно?"
    show player 11f
    show ross 13
    ross "Хехе, терпение, {b}[firstname]{/b}. Нельзя торопиться или искусство пострадает."
    show player 10f
    show ross 12
    player_name "... Ох, хорошо."
    show player 11f
    show ross 13
    ross "Почему бы тебе не пойти и не запереть дверь. Мы не хотим чтобы кто-то побеспокоил нас..."
    show player 2f
    show ross 12
    player_name "Хорошо."
    hide player with dissolve
    pause
    show ross 14 at Position(xpos=0.37, ypos=1.0) with dissolve
    pause
    show player 2f at Position(xpos=0.85, ypos=1.0)
    show ross 15 at Position(xpos=0.37, ypos=1.0)
    with dissolve
    player_name "... Хорошо, сейчас чт-"
    show ross 16 at Position(xpos=0.35, ypos=1.0)
    show player 11f
    with dissolve
    pause
    show player 10f
    show ross 17 at Position(xpos=0.34, ypos=1.0) with dissolve
    player_name "... Эм?"
    show ross 37 at Position(xpos=0.36, ypos=1.0) with dissolve
    player_name "Что вы делаете, {b}Miss Ross{/b}?"
    show player 11f
    show ross 36
    ross "Ох, тебе нужно будет так же раздеться..."
    ross "... Мы будем использовать наши тела для рисования, {b}[firstname]{/b}."
    show ross 37
    show player 10f
    player_name "... Наши тела?"
    hide ross
    show rossp 9 at Position(xpos=0.34, ypos=1.0)
    with dissolve
    show player 11f
    player_name "( !!! )" with hpunch
    show rossp 10
    ross "Точно!"
    ross "Не стесняйся..."
    ross "Избався от этих вещей!"
    show rossp 9
    show player 10f
    player_name "... Х-хорошо."
    show player 8f with dissolve
    pause
    show player 261 with dissolve
    pause
    show player 430f with dissolve
    show rossp 10
    ross "Замечательно!"
    ross "Ты такой одаренный молодой человек, {b}[firstname]{/b}..."
    show player 430bf
    show rossp 9
    player_name "Хех, спасибо."
    show player 430f
    ross "Ммммхммм."
    show rossp 10
    ross "Хорошо, для слудующего этапа..."
    ross "Нам понадобится добавить немного краски для выравнивания..."
    show rossp 9
    show player 430bf
    player_name "Я не уверен я..."
    hide ross
    show rossp 6 at Position(xpos=0.46, ypos=1.0)
    with dissolve
    show player 430f
    ross "Вот возьми это."
    show rossp 9 at Position(xpos=0.34, ypos=1.0)
    show player 613 at Position(xpos=0.83, ypos=1.0)
    with dissolve
    pause
    show player 614
    player_name "... Ч-что именно я рисую?"
    hide ross
    show rossp 1 at Position(xpos=0.41, ypos=1.0)
    with dissolve
    show player 613
    ross "Хехе, меня глупый!"
    ross "Не волнуйся,Я покажу тебе."
    show rossp 2
    pause
    hide rossp
    hide player
    with dissolve
    scene black with fade
    ross "Вот и все, {b}[firstname]{/b}..."
    ross "Просто сойти с уми с ними!"
    player_name "..."
    ross "Хехе, это щекочет!"
    scene expression game.timer.image("backgrounds/location_school_office3_closeup{}.jpg") with fade
    show ross 48 zorder 0 at Position(xpos=0.43, ypos=1.0)
    show rosso 1 zorder 1 at Position(xpos=0.43, ypos=0.99)
    show player 616 zorder 2 at Position(xpos=0.73, ypos=1.0)
    with dissolve


    pause
    show player 615 at Position(xpos=0.745, ypos=1.0) with dissolve
    show ross 47
    ross "Молодей, {b}[firstname]{/b}!"
    ross "Ох, Я действительно люблю эту технику!"
    hide rosso
    hide ross
    show rossp 3_4_5_4 at Position(xpos=0.43, ypos=1.0)
    with dissolve
    pause
    hide rossp
    show ross 47 zorder 0 at Position(xpos=0.43, ypos=1.0)
    show rosso 1 zorder 1 at Position(xpos=0.43, ypos=0.99)
    with dissolve
    ross "... Это кажется так удивительно!"
    hide ross
    hide rosso
    show rossp 3_4_5_4 at Position(xpos=0.43, ypos=1.0)
    show player 432f at Position(xpos=0.855, ypos=1.0)
    with dissolve
    player_name "Где вы этому научились так или иначе?"
    show rossp 10 zorder 0 at Position(xpos=0.4, ypos=1.0)
    show rosso 1 zorder 1 at Position(xpos=0.42, ypos=0.99)
    with dissolve
    show player 431f
    ross "Ох, Это то что я придумала давным давно."
    ross "Мой первый год фактического обучение."
    show rossp 9
    show player 432f
    player_name "Серьезно?"
    show player 431f
    ross "Ммммхммм..."
    show rossp 10
    ross "... но мы даже не дошли до самого лучшего."
    show rossp 9
    show player 432f
    player_name "... Чего самого лучшего?"
    show rossp 10
    show player 431f
    ross "Я хочу что бы мы занялись любовью, {b}[firstname]{/b}!"
    show player 430f
    player_name "( !!! )" with hpunch
    show player 430bf
    show rossp 9
    player_name "Чего?!"
    show player 430f
    show rossp 10
    ross "Займись со мной любовью! Прямр здесь на этом холсте!"
    ross "Используй моё телоя для рисования своего шедевра!"
    show player 430bf
    show rossp 9
    player_name "Вы в самом деле хотите... Со мной?"
    hide player
    hide rosso
    show rossp 11_12 at Position(xpos=0.785, ypos=1.0)
    with dissolve
    ross "Конечно Я хочу!"
    ross "Я хотела чтобы твой большой член был во мне с тех пор как я увидела того миленького маленького жирафика которого ты сделал из глины."
    player_name "... Ты хотела?"
    ross "Ох, да!"
    ross "Ничего не заводит меня более чем талантливый молодой художник!"
    player_name "... Это очень приятно."
    ross "Он вот вот будет чувствовать себя намного лучше!"
    ross "Подойди и ложись."
    return

label ross_hscene_first_time:
    scene location_school_office3_closeup_sex
    show rosss 1 at right
    with dissolve
    ross "Ох, Я не могу поверить неужели это наконец случилось!"
    ross "..."
    show rosss 2 with dissolve
    ross "Оооох, вау!"
    return

label ross_office_ross_sex:
    scene location_school_office3_closeup_sex
    show rosss 1 at right
    with dissolve
    ross "Ох, Я не могу поверить неужели это наконец случилось!"
    ross "..."
    show rosss 2 with dissolve
    ross "Оооох, вау!"
    $ M_ross.set ("sex speed", 0.2)
    show expression AnimatedImage("rosss", [2,3,4,5,6,7,8,9,10,11], M_ross) as rosss at right
    pause 3
    ross "Ох моя богиня! Это даже лучше чем я предстовляла!"
    pause 2
    player_name "Ах, {b}Miss Ross{/b}!"
    $ M_ross.set ("sex speed", 0.1)
    pause 5
    ross "Никогда еще не чувствовала себя так хорошо!"
    pause 5
    ross "Это невероятно!"
    pause 2
    player_name "Ахххх!"
    pause 2
    ross "Почему это так хорошо?!"
    $ M_ross.set ("sex speed", 0.06)
    pause 5
    ross "Ах, Выеби меня!"
    player_name "Я не могу-"
    player_name "Вы движетесь слишком быстро!"
    pause 5
    ross "Я люблю твой член, {b}[firstname]{/b}!"
    pause 2
    ross "Ах, Я люблю его так сильно!"
    return

label ross_hscene_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("rosss", [2,3,4,5,6,7,8,9,10,11], M_ross) as rosss at right
            pause 1
            if animcounter in [1,3]:
                call expression game.dialog_select("ross_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [2,3,4,5,6,7,8,9,10,11]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "rosss {}".format(pose_list[pose_counter]) as rosss at right
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("ross_hscene_dialog")
        $ animcounter += 1
    call screen ross_sex_options

label ross_hscene_dialog:
    if M_ross.is_state(S_ross_paint_with_body):
        $ temp = choice_randomizer([(1, 1), (2, 2), (3, 1)])
    else:
        $ temp = choice_randomizer([(1, 1), (2, 2), (3, 2), (4, 1)])

    if temp == 1:
        if M_ross.is_state(S_ross_paint_with_body):
            ross "Ох моя богиня! Это даже лучше чем я предстовляла!"
            player_name "Ах, {b}Miss Ross{/b}!"
        else:

            ross "Ох, Я рада что ты пришел сегодня!"
            ross "Мне это действительно было необходимо!"
            player_name "Ох,Как приятно!"
            ross "Мммм, Я так сильно люблю этот член!"
            ross "Дай его мне, {b}[firstname]{/b}!"
            ross "Вот и все!"
            ross "АААХХХ!"

    elif temp == 2:
        if M_ross.is_state(S_ross_paint_with_body):
            ross "Никогда еще не чувствовала себя так хорошо!"
            ross "Это невероятно!"
            player_name "Ahhh!"
            ross "Почему это так хорошо!"
        else:

            ross "Вот и все, {b}[firstname]{/b}!"
            ross "Ох, Это так красиво!"
            ross "Я хочу чтобы ты приходил ко мне много раз!"
            player_name "Ах, вау!"
            player_name "Ахххх!"
            ross "Вот и все!"
            ross "Нарисуй белый шедевр на моем яичническом холсте!"

    elif temp == 3:
        if M_ross.is_state(S_ross_paint_with_body):
            ross "Ах, Еби меня!"
            player_name "Я не могу-"
            player_name "Вы движетесь слишком быстро!"
            ross "Я люблю твой член, {b}[firstname]{/b}!"
            ross "Ах, Я люблю его так сильно!"
        else:

            ross "Ох, мне все еще немного больно от нашей прошлой сессии..."
            player_name "Может остановимся?"
            ross "Не смей останавливаться!"
            ross "Ах, дв!"
            ross "Да! Да! Выеби меня!"
            ross "Это так хорошо, {b}[firstname]{/b}!"
            player_name "Oh, {b}Miss Ross{/b}!!!"

    elif temp == 4:
        ross "Я думала об этом весь день!"
        player_name "Ты думала?"
        ross "Да..."
        ross "... Целый день..."
        ross "... Просто думала об твоем счастливом маленьком члене..."
        ross "... И сколько и сколько мне нужно его внутри чтобы осчастливить мою маленькую пизду!"
        player_name "..."
        ross "Ах, Я скоро кончу!"
        ross "АХ БЛЯТЬ!"
        ross "ААААХХХ!!!"
    return

label ross_office_ross_sex_cum_dialogue:
    player_name "я немогу сдержаться!"
    ross "Ох,Я люблю это!Я люблю это!Я люблю это!"
    pause
    ross "ААААХХ!!"
    pause
    show rosss 12_13 at right with flash
    player_name "HNNGGG!!!"
    ross "{b}*Задахаясь*{/b}!"
    ross "Mmmph!"
    pause
    show rosss 14 with dissolve
    ross "Хааах... Хааах..."
    ross "Вау!"
    ross "... {b}[firstname]{/b}."
    ross "Это было..."
    show rosss 15 with dissolve
    pause
    show rosss 16 with dissolve

    ross "... Я имею в виду у меня было много секс в моей жизни..."
    ross "... Много хорошего секса!"
    ross "... Но это было что-то другое, совершено!"
    player_name "... Y-yeah."
    scene expression game.timer.image("backgrounds/location_school_office3_closeup{}.jpg")
    show rossp 10 zorder 0 at Position(xpos=0.2, ypos=1.0)
    show rosso 1 zorder 1 at Position(xpos=0.22, ypos=1.0)
    show player 8f at right
    with dissolve
    ross "Нам нужно это сделать снова!"
    show player 1f with dissolve
    ross "Я никогда еще не канчала так без передышки прежде!"
    show rossp 9
    player_name "..."
    show rossp 10
    ross "Ты не возражаешь сделать это снова как-нибудь, пожалуйста {b}[firstname]{/b}?"
    show rossp 9
    show player 2f
    player_name "Конечно нет!"
    player_name "Я сделаю это в любое время когда вы захотите!"
    show rossp 10
    show player 1f
    ross "Хехе, что ж Я думаю что на сегодня достаточно..."
    ross "Я измотана..."
    show player 2f
    show rossp 9
    player_name "Да, я тоже."
    show player 1f
    show rossp 10
    ross "Приходи и найди меня в {b}моем кабинете{/b} всякий раз когда тебе будет нужен еще один \"частный урок.\" Хорошо?"
    show player 2f
    show rossp 9
    player_name "Хех, да Мэм!"
    return

label ross_office_ross_sex_cum:
    call expression game.dialog_select("ross_office_ross_sex_cum_dialogue")
    $ renpy.end_replay()
    $ game.timer.tick()
    $ M_ross.trigger(T_ross_sexual_body_painting)
    $ M_ross.set_default_locations([[L_school_artclassroom, L_school_rossoffice, L_school_rossoffice, L_NULL],
                                    [L_NULL, L_NULL, L_NULL, L_NULL]])
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
