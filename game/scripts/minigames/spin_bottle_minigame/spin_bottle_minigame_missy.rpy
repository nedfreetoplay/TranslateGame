label spin_bottle_minigame_missy:
    if M_roxxy.get("roxxy locker sex"):
        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_missy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_missy")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_becca_missy")
            call expression game.dialog_select("spin_bottle_minigame_final_spin")

        elif M_player.get("beach bottle spins") == 4:
            if not M_missy.get("missy beach sex"):
                call expression game.dialog_select("spin_bottle_minigame_missy_solo_intro_pre_first")
            else:
                call expression game.dialog_select("spin_bottle_minigame_missy_solo_intro_pre_repeat")
            call expression game.dialog_select("spin_bottle_minigame_missy_solo_intro")
            $ anim_toggle = True
			$ animated = False
            $ M_missy.set("sex speed", .09)
            call expression game.dialog_select("spin_bottle_minigame_missy_solo_intro_after")
            jump expression game.dialog_select("spin_bottle_minigame_missy_solo_loop")
    else:

        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_missy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_missy")
            call expression game.dialog_select("spin_bottle_minigame_last_spin")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_becca_missy")
            $ game.timer.tick()
            $ game.main()
    call screen spin_bottle_minigame

label beach_missy_solo_replay:
    $ M_player.set("beach bottle spins", 4)
    $ M_roxxy.set("roxxy locker sex", 1)
    jump expression game.dialog_select("spin_bottle_minigame_missy")

label spin_bottle_minigame_missy_solo_intro_pre_first:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 6b at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 5 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "ДА!!!"
    show becca sitting 10
    becca "..."
    missy "Хаха, да, да, дааааа!!!"
    show roxxy sitting 6
    rox "{b}*вздох*{/b}"
    rox "Хорошо, победила {b}Мисси{/b}..."
    show roxxy sitting 2
    show missy sitting 3
    missy "Чертовски верно!"
    show missy sitting 2
    show player_sitting 3b
    show roxxy sitting 6
    rox "Просто помни правила!"
    show roxxy sitting 2
    show player_sitting 3
    player_name "..."
    show missy sitting 3
    missy "Я помню, Я помню! Пойдем {b}[firstname]{/b}!"
    show missy sitting 2
    show roxxy sitting 3
    rox "Ладно."
    rox "Давайте покончим с этим..."
    show roxxy sitting 2
    show missy sitting 5
    missy "Лучшая. Ночь. ИЗ ВСЕХ!"
    hide missy
    hide roxxy
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show roxxy bikini 27 with dissolve
    rox "Догоняй, {b}[firstname]{/b}..."
    hide roxxy with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show missy bikini 3
    show roxxy bikini 21f at right
    pause
    show roxxy bikini 22f
    rox "Хорошо сучка!"
    show roxxy bikini 21f
    show missy bikini 4 with dissolve
    pause .25
    show missy bikini 4b with dissolve
    pause .25
    show missy bikini 5 with dissolve
    pause .25
    show roxxy bikini 22 at Position (xoffset=-33) with dissolve
    rox "Я хочу, чтобы вы начали-"
    show player 428
    show roxxy bikini 24 at Position (xoffset=-33)
    show missy bikini 7b with dissolve
    rox "!!!"
    show missy naked 8 with dissolve
    missy "Я ОЧЕНЬ готова!"
    show missy naked 1 with dissolve
    show player 10
    player_name "Что мы будем делать?!"
    show player 5
    show roxxy bikini 19 with dissolve
    rox "... Но у меня нет-"
    show roxxy bikini 20
    show missy naked 3f with dissolve
    missy "Я буквально мечтала об этом члене с того момента, как увидела его, {b}[firstname]{/b}..."
    show player 11
    player_name "!!!"
    show missy naked 1f with dissolve
    show player 427
    player_name "Вы имеете в виду, что мы собираемся-"
    show player 11
    show roxxy bikini 19
    rox "Знаешь, ты действительно получаешь от этого удовольствие, {b}Мисси{/b}..."
    show roxxy bikini 20
    show missy naked 2f
    missy "Вот дерьмо. Извини, {b}Рокси{/b}."
    missy "Я забыла, что ты здесь..."
    show missy naked 9_10 at Position (xpos=300) with dissolve
    show player 428
    show roxxy bikini 24 at Position (xoffset=-33)
    rox "!!!" with hpunch
    pause
    show roxxy bikini 19 with dissolve
    rox "{b}[firstname]{/b}?"
    show roxxy bikini 20
    show player 427
    player_name "Д-Да?"
    show player 426
    show roxxy bikini 19
    rox "Уничтожь эту суку!"
    show roxxy bikini 20
    show missy naked 3f at center with dissolve
    show player 11
    missy "{b}*вздохнув*{/b} Да!!!"
    show missy naked 1f with dissolve
    show player 12
    player_name "Подожди, ты правда не против?"
    show player 11
    show roxxy bikini 19
    rox "Не против."
    rox "Я хочу, чтобы ты трахнул ее, пока она не устанет открывать свой глупый рот!"
    show roxxy bikini 20
    show missy naked 2f
    missy "Боже мой, это потрясающая идея!!!"
    show missy naked 1f
    show player 426
    player_name "..."
    show missy naked 2f
    missy "Ты слышал ее, {b}[firstname]{/b}!"
    show missy naked 3f with dissolve
    missy "Иди сюда и трахни меня, идиот!"
    show player 429
    player_name "... Хо-хорошо."
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    hide player
    show missy naked 6f
    with dissolve
    missy "Это наконец-то случится!!"
    show missy naked 7f
    missy "Ох, я так взволнована!!"
    hide player
    hide missy
    hide roxxy
    with dissolve
    return

label spin_bottle_minigame_missy_solo_intro_pre_repeat:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 6b at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 5 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "ДА!!!"
    show becca sitting 10
    becca "..."
    missy "Хаха, да, да, даааа!!!"
    show roxxy sitting 6
    rox "{b}*вздох*{/b}"
    show player_sitting 3b
    rox "Хорошо, победила {b}Мисси{/b}..."
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 3
    missy "Чертовски верно!"
    show missy sitting 2
    show roxxy sitting 6
    rox "Просто помни правила!"
    show roxxy sitting 2
    player_name "..."
    show missy sitting 3
    missy "Я помню, Я помню! Пойдем {b}[firstname]{/b}!"
    show missy sitting 2
    show roxxy sitting 3
    rox "Ладно."
    rox "Давайте покончим с этим..."
    show roxxy sitting 2
    show missy sitting 5
    missy "Лучшая. Ночь. ИЗ ВСЕХ!"
    hide missy
    hide roxxy
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show roxxy bikini 27 with dissolve
    rox "Догоняй, {b}[firstname]{/b}..."
    hide roxxy with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show roxxy bikini 19 at right
    show missy bikini 1b
    with dissolve
    rox "На этот раз ты сделаешь то, что я тебе скажу?!"
    show roxxy bikini 20
    show missy bikini 2b
    missy "Да, {b}Рокси{/b}..."
    show missy bikini 1b
    show roxxy bikini 22 with dissolve
    rox "Снимай свою одежду."
    show roxxy bikini 21
    show missy bikini 3 with dissolve
    pause .25
    show missy bikini 4 with dissolve
    show player 426
    pause .25
    show missy bikini 4b with dissolve
    pause .25
    show missy bikini 5 with dissolve
    show roxxy bikini 22
    rox "Она хорошая маленькая сучка..."
    show missy bikini 7b with dissolve
    rox "Разве она не хорошая маленькая сучка, {b}[firstname]{/b}?"
    show missy naked 1 with dissolve
    show roxxy bikini 21
    show player 429
    player_name "Да."
    show player 426
    show roxxy bikini 23
    rox "Хахаха!"
    show roxxy bikini 22
    rox "А теперь иди сюда и проси чтобы {b}[firstname]{/b} трахнул тебя..."
    show roxxy bikini 21
    show missy naked 2f at Position (xpos=450) with dissolve
    show player 13
    missy "Пожалуйста, трахни меня {b}[firstname]{/b}."
    show player 426
    show missy naked 3f
    missy "Пожалуйста..."
    show missy naked 9_10 at Position (xpos=300) with dissolve
    show player 426
    missy "Я так сильно этого хочу..."
    show roxxy bikini 22
    rox "Хм, это было довольно хорошо."
    rox "Что скажешь, {b}[firstname]{/b}?"
    show roxxy bikini 23
    rox "Она заслужила эту награду?"
    show roxxy bikini 21
    show player 429
    player_name "Определенно!"
    show missy naked 8 at center with dissolve
    show player 426
    show roxxy bikini 22
    rox "Хахаха!"
    rox "Тогда ладно."
    rox "Иди."
    hide player
    hide missy
    hide roxxy
    with dissolve
    return

label spin_bottle_minigame_missy_solo_intro:
    scene expression "backgrounds/location_beach_cabin_sex_missy.jpg"
    show missys_solo 1 at left
    with dissolve
    missy "Да, да, ДА!!!"
    show missys_solo 2 with dissolve
    pause
    show missys_solo 3
    missy "{b}*вздох*{/b}!!!" with hpunch
    player_name "Ничего себе, действительно туго!"
    missy "..."
    player_name "{b}Мисси{/b}?"
    missy "..."
    player_name "Она в порядке?"
    rox "... Ха."
    rox "Это действительно заставило ее замолчать..."
    missy "..."
    rox "Хахаха!"
    return

label spin_bottle_minigame_missy_solo_intro_after:
    show expression AnimatedImage("missys_solo", [7,8,9,10,11,12,13,14,15,16,17,18], M_missy) as missys_solo at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    pause
    return

label spin_bottle_minigame_missy_solo_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("missys_solo", [7,8,9,10,11,12,13,14,15,16,17,18], M_missy) as missys_solo at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("spin_bottle_minigame_missy_solo_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [7,8,9,10,11,12,13,14,15,16,17,18]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "missys_solo {}".format(pose_list[pose_counter]) as missys_solo at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("spin_bottle_minigame_missy_solo_hscene_dialog")
        $ animcounter += 1
    call screen spin_bottle_minigame_solo_sex_options(M_missy)

label spin_bottle_minigame_missy_solo_hscene_dialog:
    if animcounter == 1:
        if randomizer() < 25:
            missy "БЛЯЯЯЯЯЯЯЯДЬ!!!{p=1}{nw}"
            player_name "А вот и она!{p=2}{nw}"
            player_name "Я думал, мы потеряли тебя на секунду...{p=2}{nw}"
            missy "...{p=1}{nw}"
            player_name "{b}Мисси{/b}?!{p=1}{nw}"
            missy "...{p=1}{nw}"
            rox "Давай, {b}[firstname]{/b}. Трахни ее сильнее!{p=3}{nw}"
            if M_missy.get("sex speed") > .031:
                $ M_missy.set("sex speed", M_missy.get("sex speed") - 0.03)
            missy "ААААААААААА!!!{p=1}{nw}"
            pause 1
            missy "Божемой, божемой, О. МОЙ. БОГ!!!{p=2}{nw}"

    elif animcounter == 2:
        if randomizer() < 25:
            missy "Ох как глубоко!{p=2}{nw}"
            rox "Хахаха!{p=1}{nw}"

    elif animcounter == 3:
        if randomizer() < 25:
            player_name "Она такая тугая!{p=2}{nw}"
            rox "Правда?{p=1}{nw}"
            rox "Я думаю, что ты не шлюха в конце концов, {b}Мисси{/b}.{p=2}{nw}"
            missy "Я буду такой, какой ты захочешь...{p=2}{nw}"
            missy "Просто не останавливайся!{p=2}{nw}"
    return

label spin_bottle_minigame_missy_solo_cum:
    call expression game.dialog_select("spin_bottle_minigame_missy_solo_cum_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Becca & Missy"]["unlocked"] = True
    $ persistent.cookie_jar["Becca & Missy"]["gallery"]["01_unlocked"] = True
    $ M_missy.machine_trigger(T_missy_beach_sex)
    $ game.timer.tick()
    $ game.main()

label spin_bottle_minigame_missy_solo_cum_dialogue:
    player_name "Я близко."
    missy "Я хочу, чтобы он кончил во внутрь меня."
    missy "Пожалуйста, {b}Рокси{/b}!"
    missy "Пожалуйста, пожалуйста, пожалуйста!"
    rox "Ха-ха, ну раз ты так вежливо попросила..."
    rox "Давай, {b}[firstname]{/b}..."
    pause
    player_name "Вот и все..."
    pause
    show missys_solo 3_4
    player_name "ХННГГГГ!!!" with flash
    missy "ДААААААА!!!"
    pause
    show missys_solo 5 with dissolve
    missy "О, боже."
    show missys_solo 6 with dissolve
    missy "Вот это загрузка..."
    rox "Хахаха!"

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 366 at left
    show missy naked 5
    show roxxy 1g at right
    with dissolve
    missy "Это было настолько потрясающе!"
    show missy naked 4
    show roxxy 1h
    rox "Это было довольно круто..."
    show roxxy 1g
    show player 365
    player_name "Да, это было действительно здорово!"
    show player 366
    show missy naked 5
    missy "Мы обязательно должны повторить это когда-нибудь!"
    show missy naked 4
    show roxxy 2
    rox "Боже, ты такая ненасытная сука, {b}Мисси{/b}!"
    show roxxy 1g
    show missy naked 5
    missy "Давай, пожалуйста {b}Рокси{/b}!!"
    show missy naked 4
    show roxxy 1
    rox "{b}*вздыхая*{/b}"
    show roxxy 2
    rox "Может в следующую {b}Субботу{/b}..."
    show roxxy 1g
    show missy naked 5
    missy "дааааа!!!"
    missy "Спасибо, спасибо, СПАСИБО!!!"
    show missy naked 4
    show roxxy 2
    rox "Ухх, серьезно?"
    show roxxy 1g
    show missy naked 5
    missy "У твоего парня самый лучший член на свете!"
    show missy naked 4
    show roxxy 1h
    rox "Ух, это да. Расскажи мне то, чего я не знаю!"
    show roxxy 1g
    show missy naked 5f with dissolve
    missy "Серьезно, {b}[firstname]{/b}."
    missy "ЛУЧШИЙ!"
    missy "Не могу дождаться, чтобы рассказать об этом {b}моей сестре{/b}!"
    show missy naked 4f
    show roxxy 3c
    rox "Чего?!"
    rox "Ни за что!"
    rox "Не говори этой шлюхе ничего об этом!"
    show roxxy 3b
    show missy naked 5 with dissolve
    missy "Ааа, но-"
    show missy naked 4
    show roxxy 3
    rox "Ни слова, {b}Мисси{/b}!"
    show roxxy 3b
    missy "..."
    show missy naked 5
    missy "Хорошо, я не буду говорить ей, блин..."
    show missy naked 4
    show roxxy 2
    rox "Хорошо. А теперь надевай свою чертову одежду и иди посиди у костра с {b}Беккой{/b}!"
    show roxxy 1g
    show missy naked 5
    missy "{b}*вздыхая*{/b} Ладно."
    hide missy
    hide player
    hide roxxy
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
