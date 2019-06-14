label spin_bottle_minigame_mc:
    if M_roxxy.get("roxxy locker sex"):
        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_roxxy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_missy")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_becca")
            call expression game.dialog_select("spin_bottle_minigame_final_spin")

        elif M_player.get("beach bottle spins") == 4:
            if not M_player.get("mc beach sex"):
                call expression game.dialog_select("spin_bottle_minigame_mc_4some_intro_pre_first")
            else:
                call expression game.dialog_select("spin_bottle_minigame_mc_4some_intro_pre_repeat")
            $ anim_toggle = True
            $ animated = False
            $ M_roxxy.set("sex speed", .09)
            $ M_missy.set("sex speed", .09)
            $ M_becca.set("sex speed", .09)
            $ M_player.set("left of 4some", M_becca)
            call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_roxxy")
            call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=M_roxxy)
    else:

        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_roxxy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_missy")
            call expression game.dialog_select("spin_bottle_minigame_last_spin")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_becca")
            $ game.timer.tick()
            $ game.main()
    call screen spin_bottle_minigame

label beach_mc_4some_roxxy_replay:
    call expression game.dialog_select("beach_mc_4some_dialogue_replay")
    $ M_player.set("left of 4some", M_becca)
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_roxxy")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=M_roxxy)

label beach_mc_4some_missy_replay:
    call expression game.dialog_select("beach_mc_4some_dialogue_replay")
    $ M_player.set("left of 4some", M_roxxy)
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_missy")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=M_missy)

label beach_mc_4some_becca_replay:
    call expression game.dialog_select("beach_mc_4some_dialogue_replay")
    $ M_player.set("left of 4some", M_missy)
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_becca")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=M_becca)

label beach_mc_4some_dialogue_replay:
    call expression game.dialog_select("beach_mc_4some_dialogue_replay_intro")
    call expression game.dialog_select("button_roxxy_beach_spin_bottle")
    call expression game.dialog_select("button_roxxy_beach_spin_bottle_sex_repeat")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_intro_pre_repeat")
    $ anim_toggle = True
    $ animated = False
    $ M_roxxy.set("sex speed", .09)
    $ M_missy.set("sex speed", .09)
    $ M_becca.set("sex speed", .09)
    return

label beach_mc_4some_dialogue_replay_intro:
    scene expression game.timer.image("backgrounds/location_beach_water{}_blur.jpg")
    show player 13f at right
    show becca bikini 9 at Position (xpos=315)
    show missy bikini 2 at left
    show roxxy bikini 1f at Position (xpos=500)
    with dissolve
    return

label spin_bottle_minigame_mc_4some_intro_pre_first:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 8b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 6b at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "Эй, подожди секундочку..."
    missy "Что происходит сейчас?"
    show missy sitting 6
    show becca sitting 8c
    becca "Да, я никогда даже не думала о том, чтобы приземлиться на {b}[firstname]{/b}..."
    show becca sitting 8b
    show player_sitting 3b
    show roxxy sitting 3
    rox "Ну, это значит, что {b}[firstname]{/b} победил."
    show roxxy sitting 2
    show becca sitting 7
    becca "Ааа?"
    show becca sitting 8
    show player_sitting 3
    show missy sitting 3
    missy "И так, он идет в раздевалку за особой наградой?"
    show missy sitting 2
    show becca sitting 5
    show roxxy sitting 5
    rox "Хахаха, нет."
    show roxxy sitting 3
    show player_sitting 3b
    rox "Это означает, что мы все идем!"
    show roxxy sitting 2
    show player_sitting 5
    show becca sitting 8b
    becca "!!!"
    show missy sitting 6b
    missy "Серьезно?!"
    show missy sitting 6
    show roxxy sitting 3
    rox "Ага!"
    show roxxy sitting 2
    show becca sitting 9
    becca "..."
    show missy sitting 5
    missy "ПОТРЯСАЮЩЕ!"
    player_name "..."
    show player_sitting 3b
    show roxxy sitting 3
    rox "Вам это понравится, {b}[firstname]{/b}."
    show roxxy sitting 2
    show player_sitting 3
    show becca sitting 8
    show missy sitting 3
    missy "Посмотри, как нервничает {b}Бекка{/b}!!"
    show missy sitting 5
    show becca sitting 8b
    missy "Хахаха!"
    show becca sitting 8
    show roxxy sitting 5
    rox "Хахаха!"
    show becca sitting 7b
    becca "Заткнитесь, стервы!"
    hide becca
    hide missy
    hide roxxy
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show becca bikini 20 at right
    show roxxy bikini 27 at Position (xpos=400)
    with dissolve
    rox "Ты готов, {b}[firstname]{/b}?"
    hide roxxy
    hide becca
    with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 10 at left
    show roxxy bikini 5 at right
    show becca bikini 1 at Position (xpos=575)
    show missy bikini 1 at Position (xpos=375)
    with dissolve
    player_name "Итак, мы собираемся-"
    show roxxy bikini 6 with dissolve
    show player 428
    player_name "!!!"
    show roxxy bikini 7 with dissolve
    pause .15
    show roxxy bikini 8 with dissolve
    pause .15
    show player 426
    show roxxy bikini 9 with dissolve
    pause .15
    show roxxy bikini usa 5 with dissolve
    pause .15
    show roxxy 22 with dissolve
    pause .15
    show roxxy 24 with dissolve
    rox "Давайте, девочки, время идет впустую!"
    show roxxy 23
    show becca bikini 13
    show missy bikini 3 with dissolve
    pause .25
    show becca bikini 16
    show missy bikini 4 with dissolve
    pause .25
    show becca bikini 3
    show missy bikini 4b
    with dissolve
    pause .2
    show becca bikini 4
    show missy bikini 5
    with dissolve
    pause .15
    show becca bikini 5
    show missy bikini 7b
    with dissolve
    pause .15
    show becca bikini 5b
    show missy naked 1
    with dissolve
    pause .15
    show becca naked 1 with dissolve
    show player 427
    player_name "Ладно, я не жалуюсь..."
    show player 12
    player_name "... Но что именно происходит?!"
    show player 5
    show roxxy 24
    rox "Сегодня мы будем делить тебя."
    show roxxy 23
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "{b}*глоток*{/b} Т-ты имеете в виду-"
    show player 5
    show roxxy 24
    rox "Ага!"
    rox "Давай раздевайся, {b}[firstname]{/b}."
    show roxxy 23
    player_name "..."
    show player 10
    player_name "Хорошо..."
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player 430 with dissolve
    pause
    hide player
    hide becca
    hide missy
    show roxxy 109 at center
    with dissolve
    rox "Я начну..."
    pause
    show roxxy 109c
    rox "Хочу убедиться, что вы все помните, кто здесь {b}Альфа Сучка{/b}!"
    hide roxxy with dissolve
    return

label spin_bottle_minigame_mc_4some_intro_pre_repeat:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 5 zorder 1 at right
    show becca sitting 8b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 6 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    rox "{b}[firstname]{/b} победил!"
    show player_sitting 3
    show roxxy sitting 2
    show missy sitting 2
    show becca sitting 3
    becca "Это значит, что мы все идем, верно?"
    show becca sitting 2
    show roxxy sitting 3
    rox "Верно."
    show roxxy sitting 2
    show becca sitting 9
    show missy sitting 5
    missy "Да!!!"
    player_name "..."
    show missy sitting 2
    show roxxy sitting 3
    show player_sitting 3b
    rox "Тебе это понравится, {b}[firstname]{/b}."
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 3
    missy "Смотри как нервничает {b}Бекка{/b}!!"
    show missy sitting 5
    show becca sitting 8b
    missy "Хахаха!"
    show becca sitting 8
    show roxxy sitting 5
    rox "Хахаха!"
    show becca sitting 7b
    becca "Заткнитесь, стервы!"
    hide roxxy
    hide missy
    hide becca
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show becca bikini 20 at right
    show roxxy bikini 27 at Position (xpos=400)
    with dissolve
    rox "Ты готов, {b}[firstname]{/b}?"
    hide roxxy
    hide becca
    with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show roxxy bikini 5 at right
    show becca bikini 1 at Position (xpos=575)
    show missy bikini 1 at Position (xpos=375)
    with dissolve
    pause .15
    show roxxy bikini 6 with dissolve
    show player 426
    pause .15
    show roxxy bikini 7 with dissolve
    pause .15
    show roxxy bikini 8 with dissolve
    pause .15
    show roxxy bikini 9 with dissolve
    pause .15
    show roxxy bikini usa 5 with dissolve
    pause .15
    show roxxy 22 with dissolve
    pause .15
    show roxxy 24 with dissolve
    rox "Давайте, девочки, мы тратим время впустую!"
    show roxxy 23
    show becca bikini 13
    show missy bikini 3 with dissolve
    pause .25
    show becca bikini 16
    show missy bikini 4 with dissolve
    pause .25
    show becca bikini 3
    show missy bikini 4b
    with dissolve
    pause .2
    show becca bikini 4
    show missy bikini 5
    with dissolve
    pause .15
    show becca bikini 5
    show missy bikini 7b
    with dissolve
    pause .15
    show becca bikini 5b
    show missy naked 1
    with dissolve
    pause .15
    show becca naked 1 with dissolve
    show missy naked 2
    missy "Ммм, могу я пойти первой на этот раз?!"
    show missy naked 1
    show becca naked 2
    becca "Нет, {b}Рокси{/b} пойдет первой. Ты знаешь правила!"
    show roxxy 24
    rox "Точно!"
    rox "Раздевайся, {b}[firstname]{/b}."
    show roxxy 23
    show player 429
    player_name "Хорошо."
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player 430 with dissolve
    pause
    hide player
    hide becca
    hide missy
    show roxxy 109c at center
    with dissolve
    rox "Я начну..."
    pause
    rox "Хочу убедиться, что вы все помните, кто здесь {b}Альфа Сучка{/b}!"
    hide roxxy with dissolve
    return

label spin_bottle_minigame_mc_4some_loop_pre(current_character_machine, next_character_machine):
    $ anim_toggle = True
    $ animated = False
    $ M_roxxy.set("sex speed", .09)
    $ M_missy.set("sex speed", .09)
    $ M_becca.set("sex speed", .09)
    if current_character_machine == M_roxxy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_from_roxxy")

    elif current_character_machine == M_missy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_from_missy")

    elif current_character_machine == M_becca:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_from_becca")

    if next_character_machine == M_roxxy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_to_roxxy")
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_roxxy")

    elif next_character_machine == M_missy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_to_missy")
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_missy")

    elif next_character_machine == M_becca:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_to_becca")
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_becca")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=next_character_machine)

label spin_bottle_minigame_mc_4some_loop_pre_change_from_roxxy:
    show roxxys_beach 13 at Position (xalign = 0.5) with dissolve
    pause .4
    show roxxys_beach 11 with dissolve
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_from_missy:
    show missys_beach 13 at Position (xalign = 0.5) with dissolve
    pause .4
    show missys_beach 11 with dissolve
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_from_becca:
    show beccas_beach 13 at Position (xalign = 0.7) with dissolve
    pause .4
    show beccas_beach 11 with dissolve
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_to_roxxy:
    player_name "Хорошо, {b}Рокси{/b}. Готова к следующему раунду?"
    rox "О, я всегда готова для тебя, {b}[firstname]{/b}."
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_to_missy:
    player_name "Хорошо {b}Мисси{/b}, твой черед."
    missy "Да, наконец!"
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_to_becca:
    player_name "{b}Бекка{/b}, хочешь развернуться?"
    becca "Д-Да... Хорошо."
    return

label spin_bottle_minigame_mc_4some_loop_pre_roxxy:
    scene expression "backgrounds/location_beach_cabin_sex_foursome.jpg"
    if M_player.get("left of 4some") == M_becca:
        show beccas_beach_side at Position (xpos = 50)
        show missys_beach_side at Position (xpos = 925)
    else:

        show missys_beach_sidef at Position (xpos = 150)
        show beccas_beach_sidef at Position (xpos = 975)
    show roxxys_beach 12 at Position (xalign = 0.5)
    with dissolve
    rox "Теперь девушки обратите пристальное внимание..."
    rox "Я покажу вам, как это делается!"
    show roxxys_beach 11
    missy "Ты правда сможешь принять его весь?"
    show roxxys_beach 13 with dissolve
    rox "Ха, да. Это проще прос-"
    show roxxys_beach 14
    rox "-ТОГООООО!" with hpunch
    show expression AnimatedImage("roxxys_beach", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_beach at Position (xalign = 0.5)
    pause
    return

label spin_bottle_minigame_mc_4some_loop_pre_missy:
    scene expression "backgrounds/location_beach_cabin_sex_foursome.jpg"
    if M_player.get("left of 4some") == M_becca:
        show beccas_beach_side at Position (xpos = 50)
        show roxxys_beach_side at Position (xpos = 950)
    else:

        show roxxys_beach_sidef at Position (xpos = 50)
        show beccas_beach_sidef at Position (xpos = 975)
    show missys_beach 12 at Position (xalign = 0.5)
    with dissolve
    missy "Я собираюсь взорвать твой мозг, {b}[firstname]{/b}!"
    show missys_beach 11
    becca "Хахаха, да!"
    becca "Как будто у тебя есть подсказка, что делать..."
    show missys_beach 13 with dissolve
    missy "Эй, заткнись, я точно знаю, что я-"
    show missys_beach 14
    missy "{b}*вздох*{/b}" with hpunch
    pause
    player_name "О, она действительна узкая!"
    show expression AnimatedImage("missys_beach", [1,2,3,4,5,6,7,8,9,10], M_missy) as missys_beach at Position (xalign = 0.5)
    pause
    return

label spin_bottle_minigame_mc_4some_loop_pre_becca:
    scene expression "backgrounds/location_beach_cabin_sex_foursome.jpg"
    if M_player.get("left of 4some") == M_roxxy:
        show roxxys_beach_sidef at Position (xpos = 50)
        show missys_beach_side at Position (xpos = 925)
    else:

        show missys_beach_sidef at Position (xpos = 150)
        show roxxys_beach_side at Position (xpos = 950)
    show beccas_beach 11 at Position (xalign = 0.7)
    with dissolve
    becca "Просто будь осторожен, я не привыкла к чему-то настолько большому..."
    show beccas_beach 12
    rox "Ой пожалуйста! Ее киска такая мокрая!"
    show beccas_beach 13 with dissolve
    rox "Он будет скользить."
    show beccas_beach 14
    becca "Аааааххх!" with hpunch
    rox "Видишь..."
    becca "Это так чертовски глубоко!"
    show expression AnimatedImage("beccas_beach", [1,2,3,4,5,6,7,8,9,10], M_becca) as beccas_beach at Position (xalign = 0.7)
    pause
    return

label spin_bottle_minigame_mc_4some_loop(character_machine):
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if character_machine == M_roxxy:
                    show expression AnimatedImage("roxxys_beach", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_beach at Position (xalign = 0.5)

                elif character_machine == M_missy:
                    show expression AnimatedImage("missys_beach", [1,2,3,4,5,6,7,8,9,10], M_missy) as missys_beach at Position (xalign = 0.5)

                elif character_machine == M_becca:
                    show expression AnimatedImage("beccas_beach", [1,2,3,4,5,6,7,8,9,10], M_becca) as beccas_beach at Position (xalign = 0.7)
                $ animated = True
            pause 5
            call expression game.dialog_select("spin_bottle_minigame_mc_4some_hscene_dialog") pass (character_machine=character_machine)
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                if character_machine == M_roxxy:
                    show expression "roxxys_beach {}".format(pose_list[pose_counter]) as roxxys_beach at Position (xalign = 0.5)

                elif character_machine == M_missy:
                    show expression "missys_beach {}".format(pose_list[pose_counter]) as missys_beach at Position (xalign = 0.5)

                elif character_machine == M_becca:
                    show expression "beccas_beach {}".format(pose_list[pose_counter]) as beccas_beach at Position (xalign = 0.3)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("spin_bottle_minigame_mc_4some_hscene_dialog") pass (character_machine=character_machine)
        $ animcounter += 1
    call screen spin_bottle_minigame_mc_4some_options(character_machine)

label spin_bottle_minigame_mc_4some_hscene_dialog(character_machine):
    if animcounter == 0:
        if randomizer() < 25:
            if character_machine == M_roxxy:
                rox "ААХХХХ! Блядь!{p=1}{nw}"
                missy "Хахаха!{p=1}{nw}"

            elif character_machine == M_missy:
                player_name "Нггххх, вот дерьмо!{p=2}{nw}"
                missy "Обожемой, Обожемой, Обожемой!!!{p=1}{nw}"

            elif character_machine == M_becca:
                becca "Аххххх!{p=1}{nw}"
                missy "Вау, {b}Бекка{/b} выглядит так мило, когда ее трахает этот большой член...{p=3}{nw}"
                rox "Верно?!{p=2}{nw}"
        else:

            if character_machine == M_missy:
                missy "Он такой охуенно толстый!!{p=2}{nw}"

    elif animcounter == 1:
        if randomizer() < 25:
            if character_machine == M_roxxy:
                becca "Ммм, Я люблю смотреть, как ее сиськи прыгают...{p=2}{nw}"
                missy "Да, это гипнотизирует.{p=2}{nw}"
                pause 1
                missy "Бонги, бонги, бонги!{p=1}{nw}"
                becca "Хахаха!{p=1}{nw}"
                rox "Боже мой, заткнись!{p=2}{nw}"
                rox "Я пытаюсь наслаждаться эт-{p=2}{nw}"
                if M_roxxy.get("sex speed") > .031:
                    $ M_roxxy.set("sex speed", M_roxxy.get("sex speed") - 0.03)
                rox "-иИИИИИММММММ!!!{p=1}{nw}"

            elif character_machine == M_missy:
                rox "Сильнее, {b}[firstname]{/b}!{p=1}{nw}"
                rox "Трахай эту тупую сучку!{p=2}{nw}"
                if M_missy.get("sex speed") > .031:
                    $ M_missy.set("sex speed", M_missy.get("sex speed") - 0.03)
                missy "О, БОГ!!{p=1}{nw}"
                becca "Ничего себе, он действительно дает ей это!{p=2}{nw}"
                rox "Я знаю.{p=1}{nw}"
                rox "Мой парень - монстр в постели!{p=2}{nw}"

            elif character_machine == M_becca:
                becca "Боже мой, это так здорово!{p=2}{nw}"
                rox "Давай {b}[firstname]{/b}, сделай это сильнее!{p=2}{nw}"
                missy "Да, съеби эти тупые веснушки с ее лица!{p=2}{nw}"
                becca "Заткнись, {b}Мисси{/b}!{p=2}{nw}"
                if M_becca.get("sex speed") > .031:
                    $ M_becca.set("sex speed", M_becca.get("sex speed") - 0.03)
                becca "ААААХХХХХ!!!{p=1}{nw}"
                pause 1
                rox "Да, так лучше!{p=2}{nw}"

    elif animcounter == 2:
        if randomizer() < 25:
            if character_machine == M_roxxy:
                rox "Вот дерьмо!{p=1}{nw}"

            elif character_machine == M_missy:
                missy "Я-{p=1}{nw}"
                missy "АААХХХХ!!{p=1}{nw}"
                becca "Ммм, Не могу поверить, как это меня заводит...{p=2}{nw}"
                rox "Я знаю!{p=1}{nw}"

            elif character_machine == M_becca:
                becca "Ааааа! БЛЯДЬ!!{p=1}{nw}"
                missy "О, она приближается!{p=2}{nw}"

    elif animcounter == 3:
        if randomizer() < 25:
            if character_machine == M_roxxy:
                rox "Я щас кончу!{p=1}{nw}"
                rox "О боже мой!{p=1}{nw}"
                rox "Я кончаю-{p=1}{nw}"
                pause 1
                rox "ГГХХХХХХ!!!{p=1}{nw}"

            elif character_machine == M_missy:
                missy "Нггггхх!!{p=1}{nw}"
                missy "ААААААААААААХХХХ!!!{p=1}{nw}"

            elif character_machine == M_becca:
                becca "ААААХХХ!!{p=1}{nw}"
                becca "{b}*скулит*{/b}{p=1}{nw}"
                pause 1
                rox "Боже, она так чертовски восхитительна, когда кончает!{p=2}{nw}"
    return

label spin_bottle_minigame_mc_4some_cum(character_machine):
    if character_machine == M_roxxy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_roxxy_cum_dialogue")

    elif character_machine == M_missy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_missy_cum_dialogue")

    elif character_machine == M_becca:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_becca_cum_dialogue")

    call expression game.dialog_select("spin_bottle_minigame_mc_4some_after_cum_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Roxxy"]["unlocked"] = True
    $ persistent.cookie_jar["Roxxy"]["gallery"]["08_unlocked"] = True
    $ persistent.cookie_jar["Becca & Missy"]["unlocked"] = True
    $ persistent.cookie_jar["Becca & Missy"]["gallery"]["03_unlocked"] = True
    $ persistent.cookie_jar["Becca & Missy"]["gallery"]["04_unlocked"] = True
    $ M_player.machine_trigger(T_mc_beach_sex)
    $ game.timer.tick()
    $ game.main()

label spin_bottle_minigame_mc_4some_roxxy_cum_dialogue:
    player_name "{b}Рокси{/b}, Я уже близко!"
    rox "Не останавливайся, {b}[firstname]{/b}!"
    rox "Я хочу, чтобы все это было внутри меня!"
    pause
    show roxxys_beach 14_15 at Position (xalign = 0.5)
    player_name "ННХХХХХХ!!!" with flash
    rox "ААААХХХХХ!!!"
    show roxxys_beach 15
    show xray_roxxy_3some_beach at Position (align=(0,0))
    missy "Потрясающе!"
    pause
    hide xray_roxxy_3some_beach
    show roxxys_beach 16
    with dissolve
    rox "Боже мой, как же мне хорошо!"
    show roxxys_beach 17 with dissolve
    pause
    becca "Срань господня, посмотри на этот огромный груз!"
    missy "У меня сейчас там такой кисель..."
    return

label spin_bottle_minigame_mc_4some_missy_cum_dialogue:
    player_name "Я щас взорвусь!"
    rox "Не останавливайся, {b}[firstname]{/b}."
    rox "Наполни эту тупую сучку!"
    missy "Ооо даааа!!!"
    missy "Спасибо, спасибо, СПАСИБО!!"
    pause
    show missys_beach 14_15 at Position (xalign = 0.5)
    player_name "ННГГГ!!!" with flash
    missy "{b}*задыхаясь*{/b}"
    show missys_beach 15
    show xray_missy_3some_beach at Position (align=(0,0))
    pause
    hide xray_missy_3some_beach
    show missys_beach 16
    with dissolve
    missy "Ааааа... Ааааа..."
    show missys_beach 17
    missy "Это было эпично!"
    show missys_beach 18
    becca "Да, он полностью разрушил тебя!"
    rox "Это было действительно сексуально..."
    return

label spin_bottle_minigame_mc_4some_becca_cum_dialogue:
    player_name "Я не могу больше терпеть..."
    becca "О, Можно мне {b}Рокси{/b}?!"
    becca "Пожалуйста!"
    rox "{b}*вздыхая*{/b} Ладно..."
    missy "Ох, но я этого хотела!"
    rox "Заткнись, {b}Мисси{/b}!"
    pause
    player_name "Я На подходе....!"
    show beccas_beach 14_15 at Position (xalign = 0.7)
    player_name "ННГГГГ!!!" with flash
    becca "{b}*стонет*{/b}"
    show beccas_beach 15
    show xray_becca_3some_beach at Position (align=(0,0))
    pause
    hide xray_becca_3some_beach
    show beccas_beach 16
    with dissolve
    pause
    show beccas_beach 17 with dissolve
    becca "Боже мой, это было потрясающе..."
    show beccas_beach 18
    missy "Вау, так много спермы!"
    rox "Ты мне должна, {b}Бекка{/b}!"
    return

label spin_bottle_minigame_mc_4some_after_cum_dialogue:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 366f at right
    show becca naked 4 at Position (xpos=315)
    show roxxy 106 at Position (xpos=600)
    show missy naked 5 at left
    with dissolve
    missy "Это была самая крутая вещь, которую мы когда-либо делали!"
    show missy naked 4
    show becca naked 5
    becca "Ты такая дура, {b}Мисси{/b}..."
    show becca naked 4
    show missy naked 5
    missy "Что?!"
    missy "Я серьезно!"
    missy "Мы обязательно должны повторить это на следующей неделе!"
    show missy naked 4
    becca "..."
    show roxxy 107
    rox "{b}*вздох*{/b}"
    rox "Посмотрим..."
    show roxxy 106
    show missy naked 5
    missy "Йоуууу!!!"
    show missy naked 4
    show becca naked 5
    becca "Пошли, дура..."
    becca "Давай оставим этих голубков наедине."
    show becca naked 4
    missy "Хмм?"
    show missy naked 5
    missy "Оуу..."
    missy "Хорошо."
    missy "Спасибо что трахнул нас, {b}[firstname]{/b}!!!"
    show missy naked 4
    becca "!!!" with hpunch
    show missy naked 5
    missy "Это было по НАСТОЯЩЕМУ круто!"
    missy "Пока!!"
    hide missy with dissolve
    show becca naked 5
    becca "Я..."
    becca "Она не должна была..."
    show becca naked 4
    becca "..."
    show becca naked 5
    becca "Хехе, ух..."
    becca "Пока {b}[firstname]{/b}."
    hide becca with dissolve
    show roxxy 108
    rox "Что ж, все прошло гладко..."
    show roxxy 106
    show player 365f
    player_name "Я думаю, они очаровательны."
    show player 366f
    show roxxy 107f at Position (xpos=500) with dissolve
    rox "Да, но не дай им об этом узнать."
    rox "Надеюсь, тебе понравилось?"
    show roxxy 106f
    show player 365f
    player_name "Да!"
    show player 367f
    player_name "Ты уверена, что не против всего этого?"
    show player 368f
    show roxxy 107f
    rox "Пока это происходит в моем присутствии."
    show roxxy 108f
    rox "... Да!"
    show player 366f
    show roxxy 107f
    rox "Я действительно думаю, что это очень сексуально."
    rox "Смотреть, как ты их трахаешь."
    show roxxy 106f
    show player 365f
    player_name "Ух, ты лучшая девушка в мире, {b}Рокси{/b}!"
    show player 366f
    show roxxy 107f
    rox "Я знаю!"
    rox "Давай пойдем!"
    show roxxy 108f
    rox "Я хочу искупаться нагишом!"
    hide roxxy with dissolve
    show player 365f
    player_name "Хех, подожди!"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
