label spin_bottle_minigame_roxxy:
    if M_roxxy.get("roxxy locker sex"):
        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_roxxy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_missy")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_becca")
            call expression game.dialog_select("spin_bottle_minigame_final_spin")

        elif M_player.get("beach bottle spins") == 4:
            call expression game.dialog_select("spin_bottle_minigame_roxxy_solo_intro_pre")
            call expression game.dialog_select("spin_bottle_minigame_roxxy_solo_intro")
            $ anim_toggle = True
            $ M_roxxy.set("sex speed", .09)
            call expression game.dialog_select("spin_bottle_minigame_roxxy_solo_intro_after")
            jump expression game.dialog_select("spin_bottle_minigame_roxxy_solo_loop")
    else:

        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_roxxy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_missy")
            call expression game.dialog_select("spin_bottle_minigame_last_spin")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_becca")
            $ game.timer.tick()
            $ game.main()
    call screen spin_bottle_minigame

label beach_roxxy_solo_replay:
    $ M_player.set("beach bottle spins", 4)
    $ M_roxxy.set("roxxy locker sex", 1)
    jump expression game.dialog_select("spin_bottle_minigame_roxxy")

label spin_bottle_minigame_roxxy_solo_intro_pre:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 10 at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 7 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "Что?! НЕТ!!"
    show player_sitting 3b
    show missy sitting 8
    show roxxy sitting 5
    rox "Хе-хе, извините сучки."
    show roxxy sitting 3
    rox "Он весь мой сегодня."
    show roxxy sitting 2
    show player_sitting 3
    show becca sitting 10b
    becca "Аууу..."
    show becca sitting 10
    show missy sitting 7
    missy "А мы можем просто-"
    show missy sitting 6
    show roxxy sitting 6
    show player_sitting 3b
    rox "НЕТ!!!"
    show roxxy sitting 2
    show missy sitting 8
    missy "..."
    show missy sitting 7
    missy "Вот отстой!"
    hide roxxy
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show roxxy bikini 25 with dissolve
    rox "Сюда везунчик..."
    hide roxxy with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show roxxy bikini 22 at right
    with dissolve
    rox "Я так рада, что ты сегодня полностью в моем распоряжении."
    show roxxy bikini 21
    show player 14
    player_name "Хех, да. Я тоже."
    hide player
    show roxxy bikini 17 at left
    with dissolve
    pause
    show roxxy bikini 23 at center
    show player 13 at left
    with dissolve
    rox "Эти сучки, вероятно, через пару минут будут стоять у двери и наблюдать за нами."
    show roxxy bikini 21
    show player 14
    player_name "Ну, мы можем вернуться, если хочешь?"
    show player 13
    show roxxy bikini 1 with dissolve
    rox "..."
    show roxxy bikini 2
    rox "Нет, к черту все!"
    show roxxy bikini 5 with dissolve
    show player 426
    pause
    show roxxy bikini 6 with dissolve
    pause
    show roxxy bikini 7 with dissolve
    pause
    show roxxy bikini 8 with dissolve
    pause
    show roxxy bikini 9 with dissolve
    pause
    show roxxy bikini usa 5 with dissolve
    pause
    show roxxy 22 with dissolve
    pause
    show roxxy 23b with dissolve
    rox "Пусть смотрят."
    show roxxy 24
    show player 13
    rox "Я хочу тебя прямо сейчас!"
    show roxxy 23
    show player 14
    player_name "Хорошо."
    hide player
    hide roxxy
    with dissolve
    return

label spin_bottle_minigame_roxxy_solo_intro:
    scene expression "backgrounds/location_beach_cabin_sex_roxxy.jpg"
    show roxxys_solo 1
    with dissolve
    rox "Ммм, дай мне его {b}[firstname]{/b}..."
    show roxxys_solo 2 with dissolve
    pause
    show roxxys_solo 3 with dissolve
    rox "Аххххх..."
    return

label spin_bottle_minigame_roxxy_solo_intro_after:
    show expression AnimatedImage("roxxys_solo", [7,8,9,10,11,12,13,14,15,16], M_roxxy) as roxxys_solo
    with dissolve
    pause
    return

label spin_bottle_minigame_roxxy_solo_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("roxxys_solo", [7,8,9,10,11,12,13,14,15,16], M_roxxy) as roxxys_solo
            pause 5
            call expression game.dialog_select("spin_bottle_minigame_roxxy_solo_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [7,8,9,10,11,12,13,14,15,16]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "roxxys_solo {}".format(pose_list[pose_counter]) as roxxys_solo
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("spin_bottle_minigame_roxxy_solo_hscene_dialog")
        $ animcounter += 1
    call screen spin_bottle_minigame_solo_sex_options(M_roxxy)

label spin_bottle_minigame_roxxy_solo_hscene_dialog:
    if animcounter == 0:
        if randomizer() < 25:
            rox "Да!!{p=1}{nw}"

    elif animcounter == 1:
        if randomizer() < 25:
            rox "Охх, он так глубоко!{p=2}{nw}"

    elif animcounter == 2:
        if randomizer() < 25:
            rox "Ааааххххх!!{p=1}{nw}"
            rox "О бог мой!{p=1}{nw}"

    elif animcounter == 3:
        if randomizer() < 25:
            rox "{b}[firstname]{/b}!!!{p=1}{nw}"
            pause 1
            rox "О, трахни меня сильнее!{p=2}{nw}"
    return

label spin_bottle_minigame_roxxy_solo_cum:
    call expression game.dialog_select("spin_bottle_minigame_roxxy_solo_cum_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Roxxy"]["unlocked"] = True
    $ persistent.cookie_jar["Roxxy"]["gallery"]["07_unlocked"] = True
    $ M_roxxy.trigger(T_roxxy_beach_sex)
    $ game.timer.tick()
    $ game.main()

label spin_bottle_minigame_roxxy_solo_cum_dialogue:
    rox "Я кончаю!"
    player_name "Да, я тоже!"
    pause
    rox "Ааааа, БЛЯДЬ!!!"
    show roxxys_solo 3_4
    player_name "ХННГГГГ!" with flash
    pause
    show roxxys_solo 5 with dissolve
    player_name "Ааааааа... Ааааааа..."
    show roxxys_solo 6 with dissolve
    rox "Это было потрясающе!"
    player_name "О, да..."
    pause

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 366 at left
    show roxxy 108 at right
    with dissolve
    rox "Хехе, ну, я уверена, что это было неплохое шоу!"
    show roxxy 107
    rox "Я едва могу стоять на ногах..."
    show roxxy 106
    show player 365
    player_name "Думаешь, им понравилось?"
    show player 366
    rox "Хмм..."
    show roxxy 107
    rox "Что скажете, сучки? Вам понравилось?"
    show roxxy 106
    pause
    scene expression "backgrounds/location_beach_cutscene06.jpg" with fade
    missy "Да..."
    rox "Хахаха!"
    player_name "Хахаха!"
    hide player
    hide roxxy
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
