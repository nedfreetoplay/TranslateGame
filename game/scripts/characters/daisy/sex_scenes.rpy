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
    daisy "Oh my, oh my!"
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show daisy_sex_breed after
    show daisy_sex_breed_mc cumshot 2
    player_name "HNNGGG!!!" with flash
    daisy "NGGHHH!!!"
    show daisy_sex_breed_mc cumshot 1
    show daisy_sex_flying_cum 1
    with dissolve
    pause 1
    show daisy_sex_flying_cum 2
    with dissolve
    pause
    player_name "Haah... Haah..."
    player_name "That was amazing!"
    daisy "Hehe, you squirted your milk all over me!"
    pause
    hide daisy_sex_flying_cum
    hide daisy_sex_breed_mc
    hide daisy_sex_breed
    with dissolve
    jump daisy_sex_post_pregnancy_minigame

label daisy_sex_breed_cum_in:
    daisy "Oh my, oh my!"
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    $ M_daisy.set("sex speed",0.4)
    show daisy_sex_breed creampie zorder 0
    show xray_diane_back zorder 1 at Position (xpos=440,ypos=680)
    player_name "HNNGGG!!!" with flash
    hide xray_diane_back
    show daisy_sex_breed creampie_pullout
    with dissolve
    daisy "NGGHHH!!!"
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
    player_name "Haah... Haah..."
    player_name "That was amazing!"
    daisy "Hehe, I can feel your milk inside me..."
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
        player_name "You okay?"
        show player 366
        show daisy f_shy_talk
        daisy "My legs feel funny..."
        show daisy f_shy
        show player 365
        player_name "Heh."
        show player 366
        show daisy f_shy_talk
        daisy "What was that?"
        show daisy f_shy
        show player 365
        player_name "Uhh, an orgasm I think."
        show player 366
        show daisy f_shy_talk
        daisy "Orgasm?"
        show daisy f_shy
        show player 365
        player_name "Yeah, it felt good didn't it?"
        show player 366
        show daisy f_laugh a_naked_up with dissolve
        daisy "It felt REALLY good!"
        show daisy f_normal a_naked_sides with dissolve
        pause
        show daisy f_normal_talk
        daisy "Is that supposed to happen everytime?"
        show daisy f_normal
        show player 365
        player_name "Well, hopefully..."
        show player 366
        show daisy f_shy_talk
        daisy "It never happened with Master."
        show daisy f_shy
        pause
        show daisy f_laugh
        daisy "Can we do it again?!"
        show daisy f_normal
        show player 365
        player_name "Heh, maybe in a little while... I need to rest first."
        show player 366
        show daisy f_sad_talk
        daisy "Oh, okay."
        show daisy f_sad
        pause
        show daisy f_normal_talk at flip
        show daisy at Position (xpos=750)
        daisy "{b}Diane{/b}!!!"
        show daisy f_normal
        show player 367
        player_name "Whoa, what are yo-"
        show player 368
        show daisy f_normal_talk
        daisy "{b}Diane{/b}!!!"
        show daisy f_normal
        show diane b_naked a_naked_sides f_sad_talk at Position (xpos=600)
        dia "{b}Daisy{/b}?!"
        dia "What's the matter with-"
        show diane f_surprised
        pause
        show diane f_smirk_talk
        dia "You two just had sex, didn't you."
        show diane f_smirk
        show player 367
        player_name "Uhh..."
        show player 368
        show daisy f_normal_talk
        show diane f_smirk_fardown
        daisy "Yup, and guess what?!"
        show daisy f_normal
        show diane f_smirk_talk_fardown
        dia "What?"
        show diane f_smirk_fardown
        show daisy f_laugh a_naked_up with dissolve
        daisy "I had an orgasm!"
        show daisy f_normal a_naked_sides with dissolve
        show diane f_smirk_talk_fardown
        dia "{b}*Gasp*{/b} You did?"
        show diane f_smirk_fardown
        show daisy f_normal_talk
        daisy "Uh huh!"
        daisy "My insides felt all tingly and my legs went silly and, and..."
        show daisy f_normal
        show diane f_laugh
        dia "Haha!"
        dia "Okay, okay, I get it."
        show diane f_smirk_talk_fardown
        dia "He's pretty good, isn't he?"
        show diane f_smirk_fardown
        show daisy f_normal_talk
        daisy "You mean at sex?"
        show daisy f_normal
        show diane f_smirk_talk_fardown
        dia "Yes, at sex."
        show diane f_smirk_fardown
        show daisy f_laugh
        daisy "Oh, yes!"
        show daisy f_normal_talk
        daisy "I can't wait to do it again."
        show daisy f_normal
        show diane f_laugh
        dia "Hehe!"
        show diane f_smirk
        show player 367
        player_name "Uhh, I'm gonna get a drink..."
        show player 368
        show daisy f_normal_talk at unflip
        show daisy at Position (xpos=300)
        daisy "I'll do it!"
        show daisy f_normal
        show player 367
        player_name "No, I can-"
        show player 368
        show daisy f_normal_talk
        daisy "You just stay and rest!"
        hide daisy with dissolve
        pause
        show diane f_smirk_talk
        dia "So you went through with it, huh?"
        show diane f_smirk
        show player 365
        player_name "Heh, yeah..."
        show player 366
        show diane f_laugh
        dia "I'm happy for you two!"
        show diane f_smirk
        show player 365
        player_name "T-thanks."
        show player 366
        pause
        show diane f_smirk_talk
        dia "Just don't forget to throw me a bone once in awhile too."
        dia "I have a business to run, you know?"
        show diane f_smirk
        show player 365
        player_name "Of course."
        show player 366
        show diane f_smirk_talk
        dia "Hehe."
        hide player
        show diane kiss_both_naked at Position (xoffset=-217)
        with dissolve
        pause
        show player 366 at left
        show diane b_naked a_naked_sides f_smirk_talk
        with dissolve
        dia "Don't wear yourself out, stud."
        show diane f_smirk
        show player 365
        player_name "Yeah, I won't."
        $ M_daisy.set("daisy_breed_first_time", False)
    else:
        show daisy f_laugh
        daisy "That was fun!"
        show daisy f_normal
        show player 365
        player_name "Heh, yeah it was..."
        show player 366
        show daisy f_normal_talk
        daisy "Let's do it again!"
        show daisy f_normal
        show player 365
        player_name "Uhh, maybe later... I need to rest first."
        show player 366
        show daisy f_normal_talk
        daisy "Oh, right."
        daisy "I always forget about that..."
        show daisy f_normal
        show player 365
        player_name "Hehe."
        show player 366
        show daisy f_laugh
        daisy "Let me get you a glass of water!"
        hide daisy with dissolve
        show player 367
        player_name "No, you don't hav-"
        show player 368
        pause
        show player 367
        player_name "{b}*Sigh*{/b} Have to do that."
        player_name "She's gone."
        show player 368
        pause
        show player 365
        player_name "Heh, crazy cow girl."
    hide player
    hide diane
    with dissolve
    $ persistent.cookie_jar["Daisy"]["unlocked"] = True
    $ persistent.cookie_jar["Daisy"]["gallery"]["01_unlocked"] = True
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
