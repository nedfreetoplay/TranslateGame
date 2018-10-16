label dewitts_office_first_visit:
    scene school_office2_b with fade
    show player 14 with dissolve
    player_name "Вау... {b}Miss Dewitt's{/b} кабинет емеет сладкую обстановку!"
    player_name "Похоже она собирается сдесь со сдудентами для частных записей..."
    player_name "...И у нее есть диван чтобы потусить!!"
    hide player with dissolve
    return

label dewitts_office_dewitt_office_reward:
    scene expression game.timer.image("dewitt_office_c{}"):
    show player 55f at right
    show tyrone 6f at Position (xpos=500)
    show eve 5f at Position (xpos=400)
    show dewitt 28 at left
    with dissolve
    player_name "*Кашель*"
    show player 10f with dissolve
    player_name "Боже, что здесь происходит?!"
    show player 11f
    show eve 6f
    eve "Горячая коробка!"
    show eve 5f
    show tyrone 7f
    tyrone "Закрой дверь, белый!Ты позволяешь всему дыму выходить!"
    show tyrone 8f at Position (xoffset=16) with dissolve
    show dewitt 30
    dewitt "Хэй, будь вежлив с {b}[firstname]{/b}!Он мой маленький сахарок!"
    show dewitt 28
    show tyrone 7f with dissolve
    tyrone "Пфффф, хахаха!"
    show tyrone 6f
    show player 10f
    player_name "{b}Miss Dewitt{/b}?"
    player_name "Что случилось с ваше одеждой?!"
    show player 11f
    pause
    show dewitt 29
    dewitt "Хмм?"
    dewitt "Ох! Да, Я не знаю.Они где-то здесь."
    show dewitt 28
    show tyrone 8f at Position (xoffset=16) with dissolve
    show player 212f
    player_name "..."
    show dewitt 30
    dewitt "Иди потанцуй со мной!"
    show dewitt 28
    show tyrone 6f with dissolve
    show player 29f with dissolve
    player_name "Хех,Я не очень хороший танцор."
    show player 3f at Position (xoffset=-8)
    show dewitt 29
    dewitt "Ну все в порядке,сахарок."
    show dewitt 30
    dewitt "Просто приясдь и я станцую для тебя!"
    show dewitt 28
    show player 29f
    player_name "Х-хорошо..."
    hide player
    hide dewitt
    hide eve
    hide tyrone
    with dissolve

    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_twerk{}")
    show dewitts 1
    show dewitt cloths 1c
    show player dewitts 1 zorder 2 at left
    dewitt "Посмотри на это!"
    hide dewitts
    hide dewitt
    show expression AnimatedImage("dewitt_twerk", ["1c","2c","3c","4c","5c","6c","7c","8c","9c","10c"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve

    tyrone "Черт! Ты действительно знаешь как встяхнуть этой штукрй, {b}Miss Dewitt{/b}."
    eve "Ни хера!Ты думаешь что можешь учить меня как это делать?"
    tyrone "Ох пожалуйста, у тебя должны быть причендалы в твоем багажнике чтобы осуществлять такие движения!"
    eve "Хэй Хуй! Не неси дерьми или я надеру твою задницу!"
    tyrone "Тебе нужно поймать меня первой,Чудохлебушек!"
    eve "...Ублюдок!"
    scene expression game.timer.image("dewitt_office_sex{}")
    show expression AnimatedImage("dewitt_twerk", ["1c","2c","3c","4c","5c","6c","7c","8c","9c","10c"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    show player dewitts 1 zorder 2 at left
    with fastdissolve
    pause
    hide dewitt_twerk
    show dewitts 1
    show dewitt cloths 1c zorder 1
    with dissolve
    dewitt "Слава богу они ушли."
    dewitt "Так что ты скажешь, {b}[firstname]{/b}? Тебе понравились мои танцы?"
    show dewitts 2
    player_name "Д-да!"
    player_name "У вас хорошая попка"
    show dewitts 1
    dewitt "Хех,тебе лучше поверить в это."
    dewitt "Все нормально, сахарок. Ты можешь потрогать если хочешь."
    show dewitts 2
    player_name "Серьезно?"
    hide player
    show dewitts 3b at left
    with dissolve
    pause
    show dewitts 4b
    dewitt "Ммммхмммм."
    show dewitts 3b
    pause
    show dewitts 4b
    pause
    show player dewitts 1 zorder 2 at left
    hide dewitts
    show dewitts 1
    with dissolve
    dewitt "Тебе нравиться эта сочная попка?"
    show dewitts 2
    player_name "..."
    show player dewitts 1b with hpunch
    show dewitts 2b
    dewitt "Ага!{p=1}{nw}"
    show player dewitts 1 with dissolve
    show dewitts 1
    dewitt "О боже мой,ты проказник!"
    show dewitts 2
    show player dewitts 1b with hpunch
    pause 1
    show player dewitts 1 with dissolve
    show dewitts 1
    dewitt "Мммм."
    hide player
    show dewitts 3b at left
    with dissolve
    pause
    show dewitts 4b
    dewitt "..."
    show dewitts 3b
    pause
    show dewitts 4b
    pause
    show player dewitts 1 zorder 2 at left
    hide dewitts
    show dewitts 1
    with dissolve
    dewitt "Хорошо, нам лучше остановиться. Ты начинаешь меня заводить!"
    show dewitts 2
    player_name "Ох Да. Хорошо."
    player_name "Я думаю уже становится поздно."
    show dewitts 1
    dewitt "Время летит когда веселишься!"
    dewitt "Спасибо еще раз за сегодня, {b}[firstname]{/b}.Это был действительно невероятный сюрприз!"
    show dewitts 2
    player_name "Мне очень приятно, {b}Miss Dewitt{/b}."
    player_name "Увидимся, завтра."
    show dewitts 1
    dewitt "Спокойной ночи,сахарок."
    hide dewitts
    hide dewitt cloths
    hide player
    with dissolve
    return

label dewitt_office_dewitt_night_visit:
    scene expression game.timer.image("dewitt_office_c{}")
    show dewitt 18 at left
    show player 14f at right
    with dissolve
    player_name "Хэй {b}Miss Dewitt{/b}."
    player_name "Что вы делаете?"
    show player 13f
    show dewitt 19
    dewitt "Зови меня{b}Melody{/b}, сахарок."
    dewitt "Я просто хотела послушать этот новый трек сдесь."
    dewitt "Что ты об этом думаешь?"
    show dewitt 18
    show player 17f
    player_name "Хмм, Это круто! мне нравится этот бит!"
    show player 14f
    player_name "Кто это?"
    show player 13f
    show dewitt 19
    dewitt "Хех, Это одна из моих!"
    show dewitt 18
    show player 14f
    player_name "Реально?!"
    player_name "Я не знал что вы пишите свою собственную музыку!"
    show player 13f
    show dewitt 19
    dewitt "Ну я пыталась..."
    dewitt "Я сделала это для кого-то особенного."
    show dewitt 18
    show player 14f
    player_name "Ох да?"
    player_name "Кто не будь кого я знаю?"
    show player 13f
    show dewitt 19
    dewitt "Мммм да. Я думаю ты мог слышать о нем..."
    dewitt "Он действительно помог мне выйти из одной передряги недавно."
    show dewitt 18
    show player 14f
    player_name "Хороший наверной парень..."
    show player 13f
    show dewitt 19
    dewitt "Хех, ох сахарок. Он очень хороший парень."
    dewitt "... И он должен присесть прямо здесь..."
    show dewitt 1
    show player 10f
    player_name "Что происходит, {b}Melody{/b}?"
    show player 5f
    show dewitt 19
    dewitt "Что ж, ты сделал отличное шоу для меня..."
    dewitt "Это будет справедливо чтобы я вернула должок."
    show dewitt 20 with dissolve
    show player 26f
    pause
    show dewitt 31f with dissolve
    pause
    show dewitt 32f with dissolve
    pause
    show dewitt 18b with dissolve
    pause
    show player 435f
    player_name "... Вау!"
    player_name "Вы выглядите... Прекрасно, {b}Miss Dewitt{/b}!"
    show dewitt 19b
    dewitt "Хехе, У меня есть изгибы по всех нужных местах,сахарок!"
    dewitt "... Но я знаю чего ты хочешь."

    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_sex{}"):
    show dewitts 1
    show player dewitts 1 zorder 2 at left
    with dissolve
    dewitt "Что ты думаешь об этой заднице, {b}[firstname]{/b}?"
    player_name "{b}*Gulp*{/b}"
    player_name "Это..."
    player_name "Это Прекрасно"
    player_name "Я люблю когда она дрожит!"
    dewitt "Ммм, тогда вам это понравится, сахарок!"
    hide dewitts
    show expression AnimatedImage("dewitt_twerk", ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"], M_dewitt) as dewitt_twerk at top
    with dissolve
    player_name "!!!"
    pause
    player_name "Это так сексуально, {b}Miss Dewitt{/b}!"
    dewitt "{b}Melody{/b}, {b}[firstname]{/b}..."
    player_name "Извините.Это так сексуально, {b}Melody{/b}!"
    dewitt "Хех, чтож Я рада что тебе нравится..."
    dewitt "Почему бы тебе не достать свой этот большой член?"
    player_name "Серьезно?"
    dewitt "Ммммхмммм..."
    scene black with fade
    pause 0.25
    scene expression game.timer.image("dewitt_office_sex{}"):
    show dewitts 1
    show player dewitts 2 zorder 2 at left
    with dissolve
    dewitt "Черт, это один из хороших!"
    dewitt "Интересно как он будет себя чувствать на вкус ?"
    show dewitts 2
    player_name "Вы имеете в виду Я могу-"
    player_name "... В-вы хотите меня тоже..."
    hide player
    show dewitts 3 at left
    with dissolve
    dewitt "Ммм, Я хочу что бы ты дал его мне, {b}[firstname]{/b}!"
    show dewitts 4
    dewitt "Прямо здесь, сахарок..."
    show dewitts 5 with dissolve
    pause
    show expression AnimatedImage("dewitts", [5,6,7,8,9,10,11,12,13,14], M_dewitt) as dewitts
    jump expression game.dialog_select("dewitt_sex_loop")

label dewitt_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("dewitts", [5,6,7,8,9,10,11,12,13,14], M_dewitt) as dewitts
            pause 1
            call expression game.dialog_select("dewitt_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [5,6,7,8,9,10,11,12,13,14]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "dewitts {}".format(pose_list[pose_counter]) as dewitts
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("dewitt_hscene_dialog")
        $ animcounter += 1
    call screen dewitt_sex_options

label dewitt_bj_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("dewitts_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_dewitt) as dewitts_bj
            pause 1
            call expression game.dialog_select("dewitt_bj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "dewitts_bj {}".format(pose_list[pose_counter]) as dewitts_bj
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("dewitt_bj_hscene_dialog")
        $ animcounter += 1
    call screen dewitt_office_bj_options

label dewitt_twerk_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("dewitt_twerk", ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
            pause 1
            call expression game.dialog_select("dewitt_twerk_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "dewitt_twerk {}".format(pose_list[pose_counter]) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("dewitt_twerk_hscene_dialog")
        $ animcounter += 1
    call screen dewitt_twerk_options

label dewitt_hscene_dialog:
    if animcounter == 0:
        if randomizer() <= 50:
            dewitt "Ох ебать,конечно!{p=2}{nw}"
            dewitt "Это большой мальчик!{p=2}{nw}"
            dewitt "Мммм...{p=1}{nw}"

        elif not M_dewitt.is_state(S_dewitt_office_night_visit):
            dewitt "Ох да, малыш!{p=2}{nw}"
            dewitt "Это именно то что мне было нужно!{p=2}{nw}"
        else:

            player_name "Ох, Вау!{p=1}{nw}"
            player_name "{b}Melody{/b}! Это круто!{p=2}{nw}"
            dewitt "Mмммхммм...{p=1}{nw}"

    elif animcounter == 2:
        if randomizer() <= 50:
            dewitt "Загони в эту киску, сладенький!{p=2}{nw}"
            dewitt "Дай его мне, {b}[firstname]{/b}!{p=2}{nw}"
            dewitt "Аххх!{p=1}{nw}"

        elif not M_dewitt.is_state(S_dewitt_office_night_visit):
            dewitt "Блять,этот член настолько хорош!{p=2}{nw}"
            player_name "Я люблю смотреть как ты катаешся на нем {b}Miss Dewitt{/b}...{p=3}{nw}"
            dewitt "Хех, Ммм...{p=1}{nw}"

    elif animcounter == 3:
        if randomizer() <= 50:
            dewitt "Ебать, это так глубоко!!{p=2}{nw}"
            dewitt "Вот так детка! Я собираюсь кончить на весь твой большой член!{p=3}{nw}"
            dewitt "Mmmm!!{p=1}{nw}"

        elif not M_dewitt.is_state(S_dewitt_office_night_visit):
            dewitt "Ахххх!{p=1}{nw}"
            dewitt "Дай его мне сильнее, малыш!{p=2}{nw}"
            dewitt "Ебаааааа!!!{p=1}{nw}"
    return

label dewitt_bj_hscene_dialog:
    if animcounter == 1:
        if randomizer() <= 50:
            player_name "Охх...{p=1}{nw}"
        else:

            player_name "Ухх!{p=1}{nw}"

    elif animcounter == 3 and randomizer() <= 50:
        dewitt "Мммммм!{p=1}{nw}"
    return

label dewitt_twerk_hscene_dialog:
    if animcounter == 0:
        if randomizer() <= 50:
            player_name "Охх...{p=1}{nw}"
        else:
            player_name "Уххх!{p=1}{nw}"

    elif animcounter == 2 and randomizer() <= 50:
        dewitt "Мммм!!!{p=1}{nw}"

    elif animcounter == 3 and randomizer() <= 50:
        show player dewitts 1b with hpunch
        show player dewitts 1 with dissolve
        dewitt "Nnnggh!{p=1}{nw}"
        dewitt "Ты  хочешьз заставить меня  чтобы я тебя умоляла об этом, {b}[firstname]{/b}?{p=2}{nw}"
    return

label dewitt_sex_cum_first:
    player_name "{b}Melody{/b}, Я собираюсь..."
    player_name "Я собираюсь!!"
    dewitt "Сделай это, мылыш!"
    dewitt "Я готова!"
    $ M_dewitt.set("sex speed", 0.4)
    show dewitts 15_16 at left with flash
    player_name "HNNGGG!!!"
    dewitt "АХ, ЕБАТЬ ДАААААААА!!"
    player_name "{b}Miss Dewitt{/b}!!"
    dewitt "NNGGHH!!!"
    player_name "Хааах... Хааах..."
    show dewitts 17 with dissolve
    dewitt "{b}*Фух*{/b}."
    show dewitts 18 with dissolve
    dewitt "Черт, это было здорово!"
    dewitt "Ты получил что то особенное тут, сладенький!"
    player_name "Д-дааа! Ты тоже, {b}Melody{/b}..."
    hide dewitts with dissolve

    scene expression game.timer.image("dewitt_office_c{}")
    show player 13f at right
    show dewitt 19b at left
    with dissolve
    dewitt "Ты должен вернуться и сделать это снова!"
    show dewitt 18b
    show player 14f
    player_name "Серьезно?!"
    show player 13f
    show dewitt 19b
    dewitt "Абсолюьгл!"
    dewitt "Я не позволю тебе уйти!"
    dewitt "Я хочу этот член регулярно!"
    show dewitt 18b
    show player 17f
    player_name "Хех, Я этому рад."
    show player 13f
    show dewitt 19b
    dewitt "Хорошо! Приходи ко мне в любое время,сахарок!"
    dewitt "Мои двери всегда открыты."
    show dewitt 18b
    show player 14f
    player_name "Спасибо, {b}Melody{/b}."
    show player 434f
    pause
    hide player
    hide dewitt
    with dissolve
    $ renpy.end_replay()
    return

label dewitt_sex_cum_repeat:
    player_name "ОХ!Вот оно пришло!"
    dewitt "НАПОЛНИ  меня, сахарок!"
    dewitt "Ммм!"
    dewitt "Я собираюсь кончить надо твоим шарикам!"
    $ M_dewitt.set("sex speed", 0.4)
    show dewitts 15_16 at left with flash
    player_name "HNNGGG!!!"
    dewitt "NNGGHH!!!"
    dewitt "Ебать!"
    player_name "Хаах... Хаах..."
    show dewitts 17 with dissolve
    dewitt "{b}*Фух*{/b}."
    show dewitts 18 with dissolve
    dewitt "Ммм..."
    dewitt "Хороший мальчик."
    hide dewitts with dissolve

    scene expression game.timer.image("dewitt_office_c{}")
    show player 13f at right
    show dewitt 19b at left
    with dissolve
    dewitt "Спасибо за хорошое время, сахарок."
    dewitt "Увидемся еще раз, скоро?"
    show dewitt 18b
    show player 14f
    player_name "Конечно!"
    show player 434f
    pause
    show dewitt 19b
    dewitt "Хех, Сладких снов, малыш!"
    show dewitt 18b
    show player 14f
    player_name "Спокойно ночи, {b}Melody{/b}!"
    hide player
    hide dewitt
    with dissolve
    $ renpy.end_replay()
    return

label dewitt_sex_cum:
    if M_dewitt.is_state(S_dewitt_office_night_visit):
        call expression game.dialog_select("dewitt_sex_cum_first")
        $ persistent.cookie_jar["Dewitt"]["gallery"]["03_unlocked"] = True
        $ M_dewitt.trigger(T_dewitt_sex_it_up)
        $ M_dewitt.set_default_locations([[L_school_musicclassroom, L_school_dewittoffice, L_school_dewittoffice, L_NULL],
                                          [L_NULL, L_NULL, L_NULL, L_NULL]])
    else:

        call expression game.dialog_select("dewitt_sex_cum_repeat")
    $ player.go_to(L_school_floor3)
    $ game.timer.tick()
    $ game.main()

label dewitt_bj_cum:
    hide dewitts_bj
    show dewitt bj 5 at left
    with flash
    player_name "ОХХХ!!!"
    show dewitt bj 6
    player_name "{b}Miss Dewitt{/b}!"
    show dewitt bj 7
    dewitt "Мммммм..."
    scene black with fade

    scene expression game.timer.image("dewitt_office_c{}")
    show player 13f at right
    show dewitt 19 at left
    with dissolve
    dewitt "Я надеялась услышать другую воодушевляющие слова!"
    dewitt "Или это было так хорошо что это оставило тебя без дара речи?"
    show dewitt 18
    show player 14f
    player_name "Хехе. Это было круто."
    show player 13f
    show dewitt 19
    dewitt "Возаращайся за большим! Я буду дуть в эту флейту в любой день!"
    hide player
    hide dewitt
    with dissolve
    $ player.go_to(L_school_floor3)
    $ game.timer.tick()
    $ game.main()

label dewitts_office_night_lock:
    scene expression game.timer.image("school_hall_third_floor{}_b"):
    show player 55 at Position (xoffset=12) with dissolve
    pause
    show player 56 with dissolve
    player_name "Мне нужно идти домой и немного отдохнуть."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
