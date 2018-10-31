label teachers_lounge_first_visit:
    scene expression game.timer.image("backgrounds/location_school_lounge{}_blur.jpg") with fade
    show player 14 with dissolve
    player_name "Это должна быть учительская."
    player_name "Это маленькое места отдыха от моих одноклассников."
    hide player with dissolve
    return

label teachers_lounge_okita_dose_smith:
    scene location_school_lounge_day_blur
    show player 11
    player_name "( Вот и она! Пьет кофе как я и думал. )"
    player_name "( Мне просто нужно дозировать в горшок с кофе! )"
    return

label coffee_pot_dialogue_wrong_time:
    scene location_school_lounge_day_blur
    show player 11
    player_name "( Я не могу этого сделать пока она сидит там... )"
    return

label coffee_pot_dialogue_right_time:
    scene expression "backgrounds/location_school_lounge_cutscene01.jpg"
    with fade
    show text "Это похоже на наилучший план действий." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Я знал что {b}Директриса Смит{/b} пила кофе с этого горшка каждое утро." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "И так как это было синтезировано с помощью её ДНК, это не должно повлиять на кого то еще." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Во всяком случае, вот на что я надеялся." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    return

label coffee_pot_dialogue:
    if M_okita.is_state(S_okita_dose_smith):
        if game.timer.is_afternoon():
            call expression game.dialog_select("coffee_pot_dialogue_wrong_time")

        elif game.timer.is_morning():
            call expression game.dialog_select("coffee_pot_dialogue_right_time")
            $ M_okita.trigger(T_okita_dosed_smith)
    $ player.go_to(L_school_teacherslounge)
    $ game.main()

label smith_lounge_dialogue:
    scene expression game.timer.image("backgrounds/location_school_lounge_day{}_blur.jpg")
    show player 22 at left
    show principal 33 at right
    with dissolve
    player_name "( Вот дерьмо! Директриса Смит уже здесь! )"
    show player 11
    show principal 31 with dissolve
    player_name "( ... )"
    show principal 32
    smi "{b}[firstname]{/b}?"
    smi "С какой это радости ты находишся в учительской?!"
    show player 10
    show principal 31
    player_name "Я просто-"
    show player 11
    show principal 32
    smi "Ученикам разрешено быть зесь!"
    smi "Возвращайся в свой класс немедленно или я тебя исключу!"
    show player 10
    show principal 31
    player_name "Д-да,мэм!"
    $ player.go_to(L_school_floor2)
    $ game.main()

label microwave_dialogue:
    scene expression game.timer.image("backgrounds/location_school_lounge_microwave{}.jpg")
    player_name "Яблоко?!" with hpunch
    player_name "Зачем кому-то готовить яблоко в микроволновке..."
    $ A_apple.unlock()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
