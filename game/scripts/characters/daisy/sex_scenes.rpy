label first_time_dialogue_daisy_sex:
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show daisy_sex_breed pre_talk
    show daisy_sex_breed_mc
    with dissolve
    daisy "Я так рада, {b}[firstname]{/b}!"
    player_name "Да, могу себе представить."
    daisy "Я надеюсь, что ваша ласка подойдет, она действительно большая-"
    hide daisy_sex_breed_mc
    show daisy_sex_breed insert_and_pullout
    with dissolve
    pause
    show daisy_sex_breed creampie_pullout with dissolve
    pause 1
    show daisy_sex_breed creampie
    daisy "!!!" with hpunch
    daisy "Вау!"
    player_name "Ты в порядке?"
    daisy "Ага, твоя ласка просто очень большая!"
    player_name "Дай мне знать, если я сделаю тебе больно, хорошо?"
    daisy "Хорошо."
    $ M_daisy.set('sex speed', 0.09)
    show expression AnimatedImage("daisy_sex_back", [1,2,3,4,5,6,7,8,9,10], M_daisy) as daisy_sex_breed at Position(xalign = 0.0, yoffset = 0)
    $ animated = True
    pause
    player_name "Ух ты, действительно тесно, {b}Дейзи{/b}!"
    daisy "Это же хорошо?"
    player_name "Да, это очень хорошо."
    daisy "Хе-хе, хорошо!"
    pause
    daisy "Ааа!"
    daisy "Это намного лучше, чем с мастером!"
    pause
    daisy "Твоя ласка так глубоко внутри меня!"
    daisy "Я имею в виду твой пенис..."
    daisy "Твой пенис так глубокий, у меня во флугине!"
    player_name "Хех, ты очень симпатичная!"
    daisy "Спасибо!"
    jump daisy_sex_breed_start

label daisy_sex_breed_start:
    $ anim_toggle = True
    if not animated:
        $ M_daisy.set('sex speed', 0.09)
        show expression AnimatedImage("daisy_sex_back", [1,2,3,4,5,6,7,8,9,10], M_daisy) as daisy_sex_breed at Position(xalign = 0.0, yoffset = 0)
        $ animated = True

label daisy_sex_breed_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_daisy.get("change angle"):
                    scene expression "backgrounds/location_barn_sex_front_day.jpg"
                    show expression AnimatedImage("daisy_sex_front", [1,2,3,4,5,6,7,8,9,10], M_daisy) as daisy_sex_breed at Position(xalign = 0.0, yoffset = 0)
                    with dissolve
                else:
                    scene expression "backgrounds/location_barn_sex_back_day.jpg"
                    show expression AnimatedImage("daisy_sex_back", [1,2,3,4,5,6,7,8,9,10], M_daisy) as daisy_sex_breed at Position(xalign = 0.0, yoffset = 0)
                    with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("daisy_sex_breed_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                if M_daisy.get("change angle"):
                    scene expression "backgrounds/location_barn_sex_front_day.jpg"
                    show expression "daisy_sex_front {}".format(pose_list[pose_counter]) as daisy_sex_breed at Position(xalign = 0.0, yoffset = 0)
                else:
                    scene expression "backgrounds/location_barn_sex_back_day.jpg"
                    show expression "daisy_sex_back {}".format(pose_list[pose_counter]) as daisy_sex_breed at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("daisy_sex_breed_hscene_dialog")
        $ animcounter += 1
    call screen daisy_sex_breed_options

label daisy_sex_breed_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        daisy "Ааа!{p=1}{nw}"
    if animcounter == 0 and randomizer() < 10:
        daisy "Мне нравится твоя ласка!{p=1}{nw}"
        daisy "Он лучший ласка когда-либо!{p=2}{nw}"
        pause 1
        player_name "Уверен, моя ласка тоже тебя любит!{p=2}{nw}"
        daisy "Он любит мою потайную дырочку, не так ли?!{p=2}{nw}"
        player_name "Ух хах!{p=1}{nw}"
    if animcounter == 0 and randomizer() < 25:
        daisy "Дай мне молочко ласки!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 25:
        daisy "{b}*задыхаясь*{/b} Вау!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 25:
        daisy "Сильнее, {b}[firstname]{/b}, сильнее!{p=1}{nw}"
        daisy "Аааааа!!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 25:
        daisy "Аааааа!!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        daisy "Муууу!!!{p=1}{nw}"
        daisy "Муууууууууууууу!!!{p=1}{nw}"
        player_name "Ты-?{p=1}{nw}"
        daisy "МММММУУУУУУУУУУУУУУ!!!{p=1}{nw}"
        player_name "Вау!{p=1}{nw}"
    if animcounter == 4 and randomizer() < 25:
        daisy "О боже, я очень чувствительная сегод-{p=2}{nw}"
        daisy "МууУУУУУУУ!!!{p=1}{nw}"
        player_name "Ты в порядке?{p=1}{nw}"
        daisy "Не останавливайся!!{p=1}{nw}"
    if animcounter == 4:
        if randomizer() < 25:
            daisy "Я собираюсь кончить, {b}[firstname]{/b}!{p=1}{nw}"
            player_name "Хаааа, я тоже!{p=1}{nw}"
        elif randomizer() < 10:
            daisy "О, ооо!{p=1}{nw}"
            daisy "{b}[firstname]{/b} что-то происходит!{p=1}{nw}"
            player_name "Я знаю, я тоже приближаюсь!{p=1}{nw}"
            pause 1
            daisy "Аааа, не останавливайся!{p=1}{nw}"
            daisy "Не останавливайся!!!{p=1}{nw}"
    return

label daisy_sex_breed_cum_out:
    daisy "Боже мой, Боже мой!"
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show daisy_sex_breed after
    show daisy_sex_breed_mc cumshot 2
    player_name "ХННГГГГ!!!" with flash
    daisy "НГГХХХХ!!!"
    show daisy_sex_breed_mc cumshot 1
    show daisy_sex_flying_cum 1
    with dissolve
    pause 1
    show daisy_sex_flying_cum 2
    with dissolve
    pause
    player_name "Аааа... Аааа..."
    player_name "Это было потрясающе!"
    daisy "Хе-хе, ты забрызгал меня своим молоком!"
    pause
    hide daisy_sex_flying_cum
    hide daisy_sex_breed_mc
    hide daisy_sex_breed
    with dissolve
    jump daisy_sex_post_pregnancy_minigame

label daisy_sex_breed_cum_in:
    daisy "Боже мой, Боже мой!"
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    $ M_daisy.set("sex speed",0.4)
    show daisy_sex_breed creampie zorder 0
    show xray_diane_back zorder 1 at Position (xpos=440,ypos=680)
    player_name "ХННГГГГ!!!" with flash
    hide xray_diane_back
    show daisy_sex_breed creampie_pullout
    with dissolve
    daisy "НГГХХХХ!!!"
    show daisy_sex_breed insert_and_pullout
    show daisy_sex_dick_cum 2 zorder 3
    with dissolve
    pause
    show daisy_sex_breed after
    show daisy_sex_cum zorder 1
    show daisy_sex_breed_mc zorder 2
    show daisy_sex_dick_cum 1
    with dissolve
    pause
    show daisy_sex_breed after_spread
    show daisy_sex_cum spread
    with dissolve
    player_name "Аааа... Аааа..."
    player_name "Это было потрясающе!"
    daisy "Хе-хе, я чувствую твое молоко внутри себя..."
    pause
    if store._in_replay is not None:
        jump daisy_sex_post_pregnancy_minigame
    call screen pregnancy_minigame("daisy_sex_post_pregnancy_minigame", M_daisy)

label daisy_sex_post_pregnancy_minigame:
    hide daisy_sex_cum
    hide daisy_sex_breed
    hide daisy_sex_dick_cum
    hide daisy_sex_breed_mc
    with dissolve
    $ renpy.end_replay()
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 365 at left
    show daisy b_naked a_naked_sides f_shy at Position (xpos=300)
    with dissolve

    if M_daisy.get("daisy_breed_first_time"):
        player_name "Ты в порядке?"
        show player 366
        show daisy f_shy_talk
        daisy "Мои ноги чувствуют себя странно..."
        show daisy f_shy
        show player 365
        player_name "Хе."
        show player 366
        show daisy f_shy_talk
        daisy "Что это было?"
        show daisy f_shy
        show player 365
        player_name "Ух, я думаю оргазм."
        show player 366
        show daisy f_shy_talk
        daisy "Оргазм?"
        show daisy f_shy
        show player 365
        player_name "Да, это было приятно, не так ли?"
        show player 366
        show daisy f_laugh a_naked_up with dissolve
        daisy "Это было КРУТО!"
        show daisy f_normal a_naked_sides with dissolve
        pause
        show daisy f_normal_talk
        daisy "Так должно происходить каждый раз?"
        show daisy f_normal
        show player 365
        player_name "Ну, надеюсь..."
        show player 366
        show daisy f_shy_talk
        daisy "С Мастером такого никогда не было."
        show daisy f_shy
        pause
        show daisy f_laugh
        daisy "Мы можем сделать это снова?!"
        show daisy f_normal
        show player 365
        player_name "Хех, может быть через некоторое время... Сначала мне нужно отдохнуть."
        show player 366
        show daisy f_sad_talk
        daisy "О, хорошо."
        show daisy f_sad
        pause
        show daisy f_normal_talk at flip
        show daisy at Position (xpos=750)
        daisy "{b}Диана{/b}!!!"
        show daisy f_normal
        show player 367
        player_name "Эй, что ты-"
        show player 368
        show daisy f_normal_talk
        daisy "{b}Диана{/b}!!!"
        show daisy f_normal
        show diane b_naked a_naked_sides f_sad_talk at Position (xpos=600)
        dia "{b}Дэйзи{/b}?!"
        dia "Что случилось с-"
        show diane f_surprised
        pause
        show diane f_smirk_talk
        dia "Вы только что занимались сексом, не так ли?"
        show diane f_smirk
        show player 367
        player_name "Эээ..."
        show player 368
        show daisy f_normal_talk
        show diane f_smirk_fardown
        daisy "Ага, и знаешь что?!"
        show daisy f_normal
        show diane f_smirk_talk_fardown
        dia "Что?"
        show diane f_smirk_fardown
        show daisy f_laugh a_naked_up with dissolve
        daisy "У меня был оргазм!"
        show daisy f_normal a_naked_sides with dissolve
        show diane f_smirk_talk_fardown
        dia "{b}*вздыхая*{/b} У тебя был...?"
        show diane f_smirk_fardown
        show daisy f_normal_talk
        daisy "Ну..!"
        daisy "Мои внутренности покалывало, и ноги стали непослушными и ..."
        show daisy f_normal
        show diane f_laugh
        dia "Хаха!"
        dia "Хорошо, хорошо, я поняла."
        show diane f_smirk_talk_fardown
        dia "Он довольно хорош, не так ли?"
        show diane f_smirk_fardown
        show daisy f_normal_talk
        daisy "Ты имеешь в виду секс?"
        show daisy f_normal
        show diane f_smirk_talk_fardown
        dia "Да, в сексе."
        show diane f_smirk_fardown
        show daisy f_laugh
        daisy "О, да!"
        show daisy f_normal_talk
        daisy "Не могу дождаться, чтобы сделать это снова."
        show daisy f_normal
        show diane f_laugh
        dia "Хехе!"
        show diane f_smirk
        show player 367
        player_name "Ух, надо чего-нибудь выпить..."
        show player 368
        show daisy f_normal_talk at unflip
        show daisy at Position (xpos=300)
        daisy "Я сделаю!"
        show daisy f_normal
        show player 367
        player_name "Нет, Я могу-"
        show player 368
        show daisy f_normal_talk
        daisy "Ты просто останься и отдохни!"
        hide daisy with dissolve
        pause
        show diane f_smirk_talk
        dia "Так ты прошел через это, а?"
        show diane f_smirk
        show player 365
        player_name "Ну, да..."
        show player 366
        show diane f_laugh
        dia "Я рада за вас двоих!"
        show diane f_smirk
        show player 365
        player_name "С-спасибо."
        show player 366
        pause
        show diane f_smirk_talk
        dia "Только не забывай иногда бросать мне пару палок."
        dia "У меня есть бизнес, которым нужно управлять, понимаешь?"
        show diane f_smirk
        show player 365
        player_name "Конечно."
        show player 366
        show diane f_smirk_talk
        dia "Хехе."
        hide player
        show diane kiss_both_naked at Position (xoffset=-217)
        with dissolve
        pause
        show player 366 at left
        show diane b_naked a_naked_sides f_smirk_talk
        with dissolve
        dia "Не утомляйся, жеребец."
        show diane f_smirk
        show player 365
        player_name "Да, не буду."
        $ M_daisy.set("daisy_breed_first_time", False)
    else:
        show daisy f_laugh
        daisy "Это было весело!"
        show daisy f_normal
        show player 365
        player_name "Хех, да, так и было..."
        show player 366
        show daisy f_normal_talk
        daisy "Давайте сделаем это снова!"
        show daisy f_normal
        show player 365
        player_name "Может быть, попозже... Сначала мне нужно отдохнуть."
        show player 366
        show daisy f_normal_talk
        daisy "О, хорошо."
        daisy "Я всегда забываю об этом..."
        show daisy f_normal
        show player 365
        player_name "Хехе."
        show player 366
        show daisy f_laugh
        daisy "Давай я принесу тебе стакан воды!"
        hide daisy with dissolve
        show player 367
        player_name "Нет, ты не должна-"
        show player 368
        pause
        show player 367
        player_name "{b}*Вздыхая*{/b} Придется это сделать."
        player_name "Она пропала."
        show player 368
        pause
        show player 365
        player_name "Хех, сумасшедшая девочка-корова."
    hide player
    hide diane
    with dissolve
    $ persistent.cookie_jar["Daisy"]["unlocked"] = True
    $ persistent.cookie_jar["Daisy"]["gallery"]["01_unlocked"] = True
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
