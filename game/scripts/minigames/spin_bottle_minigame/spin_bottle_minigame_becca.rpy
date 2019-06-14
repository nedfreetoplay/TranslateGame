label spin_bottle_minigame_becca:
    if M_roxxy.get("roxxy locker sex"):
        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_becca")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_becca_missy")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_becca")
            call expression game.dialog_select("spin_bottle_minigame_final_spin")

        elif M_player.get("beach bottle spins") == 4:
            if not M_becca.get("becca beach sex"):
                call expression game.dialog_select("spin_bottle_minigame_becca_solo_intro_pre_first")
            else:
                call expression game.dialog_select("spin_bottle_minigame_becca_solo_intro_pre_repeat")
            call expression game.dialog_select("spin_bottle_minigame_becca_solo_intro")
            $ anim_toggle = True
            $ animated = False
            $ M_becca.set("sex speed", .09)
            call expression game.dialog_select("spin_bottle_minigame_becca_solo_intro_after")
            jump expression game.dialog_select("spin_bottle_minigame_becca_solo_loop")
    else:

        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_becca")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_becca_missy")
            call expression game.dialog_select("spin_bottle_minigame_last_spin")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_becca")
            $ game.timer.tick()
            $ game.main()
    call screen spin_bottle_minigame

label beach_becca_solo_replay:
    $ M_player.set("beach bottle spins", 4)
    $ M_roxxy.set("roxxy locker sex", 1)
    jump expression game.dialog_select("spin_bottle_minigame_becca")

label spin_bottle_minigame_becca_solo_intro_pre_first:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 8b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 6 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "!!!"
    show player_sitting 3
    show becca sitting 8
    show missy sitting 7
    missy "Что?! НЕТ!!"
    show missy sitting 8
    show becca sitting 8b
    show roxxy sitting 5
    rox "Хе-хе, похоже, это счастливая ночь для {b}Бекки{/b}..."
    show roxxy sitting 2
    show becca sitting 8c
    becca "Я не-"
    show becca sitting 10b
    becca "Я имею в виду, ты-"
    show becca sitting 8b
    show roxxy sitting 3
    rox "Посмотри, какая она стеснительная..."
    show roxxy sitting 2
    show becca sitting 10b
    becca "Я нет!"
    show becca sitting 10
    show roxxy sitting 6
    rox "Разве она не прелестна?"
    show roxxy sitting 2
    show becca sitting 9
    becca "..."
    hide roxxy
    hide becca
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show roxxy bikini 26 with dissolve
    rox "Тебе это понравится..."
    hide roxxy with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show roxxy bikini 22 at right
    show becca bikini 1
    with dissolve
    rox "Я не могу дождаться, когда ты трахнешь ее очаровательные маленькие мозги!"
    show roxxy bikini 21
    show player 11
    player_name "!!!" with hpunch
    show becca bikini 13
    show player 10
    player_name "Ты серьезно?!"
    show becca bikini 1
    show player 11
    rox "Ммммммммм..."
    show roxxy bikini 22
    rox "Как ты думаешь, что за особая награда?!"
    show roxxy bikini 21
    show player 29 with dissolve
    player_name "Не знаю, больше поцелуев?!"
    show player 3
    show becca bikini 15
    show roxxy bikini 23
    rox "Хахаха!"
    show roxxy bikini 22
    rox "Давай, {b}Бекка{/b}..."
    rox "Снимай бикини!"
    show roxxy bikini 21
    show becca bikini 6
    becca "Я ээ..."
    show becca bikini 18
    becca "Хорошо."
    show becca bikini 3 with dissolve
    pause
    show becca bikini 4 with dissolve
    pause
    show becca bikini 5
    show player 428
    with dissolve
    pause
    show becca bikini 5b with dissolve
    pause
    show becca naked 1 with dissolve
    player_name "..."
    show roxxy bikini 22
    rox "Чёёёрт!"
    show player 426
    rox "Разве она не сексуальна, {b}[firstname]{/b}?"
    show roxxy bikini 21
    show player 429
    player_name "Д-Да..."
    show player 426
    show roxxy bikini 22
    rox "Разве ты не хочешь просто растерзать ее?!"
    show roxxy bikini 21
    show player 429
    player_name "Д-Да..."
    show player 426
    show roxxy bikini 22
    rox "Хехехе!"
    rox "А что насчет тебя, {b}Бекка{/b}?!"
    rox "Разве ты этого не хочешь?"
    show roxxy bikini 21
    show becca naked 2
    becca "... Да."
    show becca naked 1
    show roxxy bikini 23
    rox "Да ладно, ты можешь сделать лучше, чем это!"
    show roxxy bikini 22
    rox "Я хочу, чтобы ты умоляла об этом!"
    show roxxy bikini 21
    show player 11
    show becca naked 3
    becca "!!!"
    becca "..."
    show becca naked 2
    becca "Пожалуйста..."
    show becca naked 1
    show roxxy bikini 23
    rox "Пожалуйста что?"
    show roxxy bikini 21
    show becca naked 2
    becca "Пожалуйста, {b}Рокси{/b}..."
    becca "Я хочу чтобы {b}[firstname]{/b} трахнул меня!"
    show becca naked 1
    show roxxy bikini 22
    rox "Хахаха!"
    rox "Хорошо."
    rox "Иди туда и трахни ее, {b}[firstname]{/b}!"
    show roxxy bikini 21
    show player 429
    player_name "Хорошо..."
    hide player
    hide becca
    hide roxxy
    with dissolve
    return

label spin_bottle_minigame_becca_solo_intro_pre_repeat:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 8b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 6 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "!!!"
    show player_sitting 3
    show missy sitting 7
    missy "Что?! НЕТ!!"
    show missy sitting 8
    show roxxy sitting 3
    show player_sitting 3b
    rox "Хе-хе, похоже, это счастливая ночь для {b}Бекки{/b}..."
    show player_sitting 3
    show roxxy sitting 2
    show becca sitting 8c
    becca "Я не-"
    show becca sitting 10b
    becca "Я имею в виду, ты-"
    show becca sitting 8b
    show roxxy sitting 3
    rox "Посмотри, какая она стеснительная..."
    show roxxy sitting 2
    show becca sitting 8c
    becca "Я не такая!"
    show becca sitting 9
    show roxxy sitting 6
    rox "Разве она не прелестна?"
    show roxxy sitting 2
    becca "..."
    hide becca
    hide roxxy
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show roxxy bikini 26 with dissolve
    rox "Тебе это понравится..."
    hide roxxy with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show roxxy bikini 22 at right
    show becca bikini 1
    with dissolve
    rox "Давай, {b}Бекка{/b}..."
    rox "Сними это бикини!"
    show roxxy bikini 21
    show becca bikini 6
    becca "Я ээ..."
    show becca bikini 18
    becca "Хорошо."
    show becca bikini 3 with dissolve
    pause
    show becca bikini 4 with dissolve
    pause
    show becca bikini 5
    show player 428
    with dissolve
    pause
    show becca bikini 5b with dissolve
    pause
    show becca naked 1 with dissolve
    player_name "..."
    show roxxy bikini 22
    rox "Чёёрт!"
    show player 426
    rox "Разве она не сексуальна, {b}[firstname]{/b}?"
    show roxxy bikini 21
    show player 429
    player_name "Д-Да..."
    show player 426
    show roxxy bikini 22
    rox "Разве ты не хочешь просто растерзать ее?!"
    show roxxy bikini 21
    show player 429
    player_name "Д-Да..."
    show player 426
    show roxxy bikini 22
    rox "Хехехе!"
    rox "А что насчет тебя, {b}Бекка{/b}?!"
    rox "Разве ты этого не хочешь?"
    show roxxy bikini 21
    show becca naked 2
    becca "... Да."
    show becca naked 1
    show roxxy bikini 23
    rox "Да ладно, ты можешь сделать лучше, чем это!"
    show roxxy bikini 22
    rox "Я хочу, чтобы ты умоляла об этом!"
    show roxxy bikini 21
    show player 11
    show becca naked 3
    becca "!!!"
    becca "..."
    show becca naked 2
    becca "Пожалуйста..."
    show becca naked 1
    show roxxy bikini 23
    rox "Пожалуйста что?"
    show roxxy bikini 21
    show becca naked 2
    becca "Пожалуйста, {b}Рокси{/b}..."
    becca "Я хочу чтобы {b}[firstname]{/b} трахнул меня!"
    show becca naked 1
    show roxxy bikini 22
    rox "Хахаха!"
    rox "Хорошо."
    rox "Иди туда и трахни ее, {b}[firstname]{/b}!"
    show roxxy bikini 21
    show player 429
    player_name "Хорошо..."
    hide player
    hide becca
    hide roxxy
    with dissolve
    return

label spin_bottle_minigame_becca_solo_intro:
    scene expression "backgrounds/location_beach_cabin_sex_becca.jpg"
    show beccas_solo 1
    with dissolve
    pause
    show beccas_solo 2 with dissolve
    pause
    show beccas_solo 3
    becca "!!!" with hpunch
    becca "Срань господня!"
    rox "Хахаха!"
    rox "Я знаю, верно?!"
    becca "Он очень большой!"
    rox "Давай, {b}[firstname]{/b}. Она готова!"
    show beccas_solo 4 with dissolve
    becca "АААхххххх!!"
    return

label spin_bottle_minigame_becca_solo_intro_after:
    show expression AnimatedImage("beccas_solo", [7,8,9,10,11,12,13,14,15,16], M_becca) as beccas_solo
    with dissolve
    pause
    return

label spin_bottle_minigame_becca_solo_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("beccas_solo", [7,8,9,10,11,12,13,14,15,16], M_becca) as beccas_solo
                $ animated = True
            pause 5
            call expression game.dialog_select("spin_bottle_minigame_becca_solo_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [7,8,9,10,11,12,13,14,15,16]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "beccas_solo {}".format(pose_list[pose_counter]) as beccas_solo
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("spin_bottle_minigame_becca_solo_hscene_dialog")
        $ animcounter += 1
    call screen spin_bottle_minigame_solo_sex_options(M_becca)

label spin_bottle_minigame_becca_solo_hscene_dialog:
    if animcounter == 0:
        if randomizer() < 25:
            becca "О боже мой!{p=2}{nw}"
            becca "О БОЖЕ МОЙ!!{p=2}{nw}"
            rox "Hahaha!{p=1}{nw}"

    elif animcounter == 1:
        if randomizer() < 25:
            rox "Вот так, {b}[firstname]{/b}!{p=2}{nw}"
            rox "Трахни ее мозги!{p=2}{nw}"

    elif animcounter == 2:
        if randomizer() < 25:
            becca "АААХХХ!!{p=1}{nw}"
            becca "Я кончаю!{p=1}{nw}"
            becca "{b}*стонет*{/b}{p=1}{nw}"
            pause
            rox "Хахаха, это было быстро!{p=2}{nw}"
            rox "Она делает самые очаровательные гримасы!{p=2}{nw}"
            rox "Продолжай, {b}[firstname]{/b}!{p=2}{nw}"

    elif animcounter == 3:
        if randomizer() < 25:
            becca "Ггрррр!!{p=1}{nw}"
            pause 1
        else:

            becca "{b}*стонет*{/b}{p=1}{nw}"
    return

label spin_bottle_minigame_becca_solo_cum:
    call expression game.dialog_select("spin_bottle_minigame_becca_solo_cum_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Becca & Missy"]["unlocked"] = True
    $ persistent.cookie_jar["Becca & Missy"]["gallery"]["02_unlocked"] = True
    $ M_becca.machine_trigger(T_becca_beach_sex)
    $ game.timer.tick()
    $ game.main()

label spin_bottle_minigame_becca_solo_cum_dialogue:
    player_name "Я скоро кончу!"
    becca "Кончай во внутрь меня!"
    rox "Извени, что?!"
    becca "..."
    rox "Это не похоже на мольбу..."
    becca "{b}*стонет*{/b}"
    pause
    becca "Ггрррр!!!"
    becca "Пожалуйста, {b}Рокси{/b}!!!"
    becca "ААхххх!!! Пожалуйста, пожалуйста пожалуйста!"
    rox "Хахаха!"
    rox "Хорошо, {b}[firstname]{/b}..."
    rox "Дай ей!"
    pause
    becca "О БОЖЕ МОЙ!!!"
    show beccas_solo 3_4
    player_name "ГГРРРРРР!!!" with flash
    show beccas_solo 4
    show xray_becca_1o1_beach at Position (align=(0,0))
    pause
    hide xray_becca_1o1_beach
    show beccas_solo 5
    with dissolve
    player_name "Хааааааа... Хаааааа..."
    becca "{b}*стонет*{/b}"
    show beccas_solo 6 with dissolve
    rox "Ха-ха, ничего себе, ты действительно сделал номер на ее..."
    rox "Это было так чертовски круто!"

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 365 at left
    show becca naked 4
    show roxxy 1g at right
    with dissolve
    player_name "Ты в порядке, {b}Бекка{/b}?"
    show player 366
    show becca naked 5
    becca "Мммхмм, Я просто не могу... Именно... Чувствовать свои ноги..."
    show becca naked 4
    show roxxy 1h
    rox "Хе-хе, я думаю, ты измотал ее."
    show roxxy 1g
    pause
    show player 365
    player_name "Мне немного жаль {b}Мисси{/b}."
    player_name "Она там совсем одна..."
    show player 366
    show roxxy 1h
    rox "Пффф, к черту эту жадную сучку."
    rox "Кроме того, она почти все время наблюдала из-за двери..."
    rox "Не так ли, {b}Мисси{/b}?!"
    show roxxy 1g
    pause
    missy "... Нет."
    show roxxy 4
    show player 365
    rox "Хахаха!"
    player_name "Хахаха!"
    hide player
    hide roxxy
    hide becca
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
