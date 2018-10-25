label dewitt_dialogue_office_dewitt_eve_meet_up:
    scene expression game.timer.image("dewitt_office_c{}")
    show player 10 with dissolve
    player_name "Я должен дать ей немного пространства на время."
    player_name "И мне также следует встретится с {b}Евой{/b} в {b}парке ночью{/b}."
    return

label dewitt_dialogue_office_dewitt_end_intro:
    scene expression game.timer.image("dewitt_office_c{}")
    show dewitt 18 at left
    show player 14f at right
    with dissolve
    player_name "Привет, {b}Мелоди{/b}!"
    show player 13f
    show dewitt 19
    dewitt "Ммм, привет {b}[firstname]{/b}!"
    dewitt "Я надеялась, что ты придешь ко мне ночью..."
    show dewitt 18
    show player 14f
    player_name "Хех, ты в настроении немного повеселиться?"
    show player 13f
    show dewitt 19
    dewitt "Я всегда в настроении для тебя, {b}[firstname]{/b}."
    dewitt "Ты хочешь получить право на это или я должна танцевать для тебя в первой?"
    show dewitt 18
    return

label dewitt_dialogue_office_dewitt_end_dance:
    show dewitt 19
    dewitt "Тогда присаживайся, сахарок."
    scene expression game.timer.image("dewitt_office_sex{}"):
    $ M_dewitt.set("sex speed", 0.125)
    show dewitts 1
    show dewitt cloths 1b
    show player dewitts 1 zorder 2 at left
    with dissolve
    pause
    hide dewitts
    hide dewitt
    show expression AnimatedImage("dewitt_twerk", [1,2,3,4,5,6,7,8,9,10], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve
    dewitt "Ммм..."
    dewitt "Тебе нравится, детка?"
    player_name "Ох, да!"
    show player dewitts 1b with hpunch
    show player dewitts 1 with dissolve
    dewitt "О!"
    dewitt "Мне нравится, когда ты так делаешь!"
    pause
    dewitt "Я думаю, что я должна снять часть одежды!"
    dewitt "Как ты думаешь, сахорок?"
    player_name "Д-да!"
    hide dewitts
    hide dewitt_twerk
    hide dewitt
    hide player
    with dissolve

    scene expression game.timer.image("dewitt_office_c{}")
    show dewitt 20 zorder 1 with dissolve
    pause
    show dewitt 31b with dissolve
    pause
    show dewitt 32b with dissolve
    pause
    show dewitt 29 with dissolve
    dewitt "Давай сменим музыку!"
    show dewitt 35b at Position (xoffset=354) with dissolve
    pause

    show player 626 zorder 0 at Position (xpos=550) with dissolve
    pause
    show dewitt 36 at Position (xoffset=354)
    dewitt "И что ты там делаешь?"
    dewitt "Разве ты не слышал, что нельзя трогать танцоров?"
    show dewitt 35 at Position (xoffset=354)

    show player 629
    show player_hand 629b_629c zorder 2 at Position (xpos=550)
    with dissolve
    player_name "Ууупс..."
    show player 628
    show dewitt 36 at Position (xoffset=354)
    dewitt "Непослушный мальч-"

    show player_hand 629d
    show dewitt 37 at Position (xoffset=290) with hpunch
    show player 626
    hide player_hand
    with dissolve
    dewitt "Эй...!"
    show dewitt 38 at Position (xoffset=290)
    show player 627
    with dissolve
    dewitt "Вернись на диван, шалун!"

    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_sex{}"):
    show dewitts 1
    show dewitt cloths 1c
    show player dewitts 1 zorder 2 at left
    with dissolve
    dewitt "Ммм, ну как я выгляжу сейчас?"
    hide dewitts
    hide dewitt
    show expression AnimatedImage("dewitt_twerk", ["1c","2c","3c","4c","5c","6c","7c","8c","9c","10c"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve
    player_name "Очень сексуально, {b}Мелоди{/b}!"
    dewitt "Хех, спасибо, сахарок!"
    pause
    show player dewitts 1b with hpunch
    show player dewitts 1 with dissolve
    dewitt "Ммм!"
    dewitt "Шалунишка!"
    dewitt "Ты делаешь меня такой мокрой!"
    pause
    dewitt "Ты готов к финалу?"
    player_name "Да, мэм!"
    dewitt "Хехе, следи внимательно..."
    scene black with fade
    pause 0.25
    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_sex{}"):
    show dewitts 1
    show player dewitts 1 zorder 2 at left
    with dissolve
    dewitt "Ммм, смотри как работает моя киска, малыш!"
    hide dewitts
    show expression AnimatedImage("dewitt_twerk", ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve
    pause
    show player dewitts 1b with hpunch
    show player dewitts 1 with dissolve
    dewitt "Трахни!"
    dewitt "Я не могу больше терпеть, сахорок!"
    dewitt "Мне нужен этот большой член!"
    pause
    return


label dewitt_dialogue_office_dewitt_end_bj:
    show player 14f
    player_name "Не могли бы вы снова дать мне BJ?"
    show player 13f
    show dewitt 19 with dissolve
    dewitt "С удовольствием!"
    dewitt "Ты же знаешь, я уже играла на нескольких флейтах."
    dewitt "Но твоя флейта - лучшее, что я имела удовольствие обхватить губами."
    dewitt "Но хватит разговоров, позволь мне дать тебе еще одно частное представление."
    scene black with fade

    $ M_dewitt.set("sex speed", 0.175)
    scene expression game.timer.image("dewitt_office_bj{}")
    show dewitt bj 1 at left
    with dissolve
    pause
    show dewitt bj 2
    pause
    show dewitt bj 3
    pause
    show dewitt bj 4
    pause
    hide dewitt
    show expression AnimatedImage("dewitts_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_dewitt) as dewitts_bj
    return

label dewitt_dialogue_office_dewitt_end_sex:
    show dewitt 19
    dewitt "Я надеялась, что ты захочешь прыгнуть прямо сюда!"
    dewitt "Давайте посмотрим, кто быстрее всех появится из одежды!"
    show dewitt 20 with dissolve
    show player 26f
    player_name "А обратный отсчет?"
    show dewitt 31f with dissolve
    show player 8f with dissolve
    dewitt "Нет!"
    show dewitt 32f with dissolve
    show player 261 with dissolve
    pause
    show dewitt 18b with dissolve

    show player 263 with dissolve
    pause
    show dewitt 19b
    dewitt "Похоже, что я выиграла!"
    dewitt "Теперь заставь меня кончить!"
    show player 262
    player_name "Да, мэм!"
    label dewitt_twerk_end:
        scene black with fade
        pause 0.25
        scene expression game.timer.image("dewitt_office_sex{}"):
        show dewitts 1
        show player dewitts 2 zorder 2 at left
        with dissolve
        dewitt "Дай мне, {b}[firstname]{/b}!"
        hide player
        show dewitts 3 at left
        with dissolve
        dewitt "Хватит играть там! Я не могу ждать!"
        show dewitts 4
        dewitt "Сейчас, сахарок..."
        show dewitts 5 with dissolve
        pause
        $ M_dewitt.set("sex speed", 0.125)
        show expression AnimatedImage("dewitts", [5,6,7,8,9,10,11,12,13,14], M_dewitt) as dewitts
        $ anim_toggle = True
    jump expression game.dialog_select("dewitt_sex_loop")

label dewitt_dialogue_office_intro:
    scene expression game.timer.image("dewitt_office_c{}"):
    show dewitt 1b at left
    show player 14f at right
    with dissolve
    player_name "Здравствуйте, {b}Мисс Девитт{/b}."
    show player 13f
    show dewitt 2b
    dewitt "Привет, {b}[firstname]{/b}!"
    dewitt "Тебе что-то нужно?"
    show dewitt 1b
    return

label dewitt_dialogue_office_flute_lessons:
    show player 26f
    player_name "Я надеялся, что вы сможете научить меня играть на флейте."
    show player 13f
    show dewitt 19 with dissolve
    dewitt "Я надеялась, что ты спросишь!"
    dewitt "Приходи сюда сегодня вечером и мы сможем поиграть вместе!"
    hide player
    show dewitt 6 at right
    with dissolve
    dewitt "И не опаздывай, а то мне придется играть одной."
    return

label dewitt_dialogue_office_leave:
    show player 14f
    player_name "Не сейчас."
    show player 13f
    show dewitt 2b
    dewitt " Что ж, хорошего дня!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
