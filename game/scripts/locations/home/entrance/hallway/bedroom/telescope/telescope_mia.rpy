label mia_bedroom:
    if sister.started(sis_telescope02):
        call expression game.dialog_select("telescope_mia_sister_spying")
        $ persistent.cookie_jar["Mia"]["unlocked"] = True
        $ persistent.cookie_jar["Mia"]["gallery"]["02_unlocked"] = True
        $ sis_telescope02.finish()
        $ sister.add_event(sis_hallway02)
        jump expression game.dialog_select("bedroom_dialogue")
    else:
        call expression game.dialog_select(game.telescope.mia)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_mia_sister_spying:
    scene
    show windowmiaday 3
    player_name "( О бог... )"
    player_name "( Что {b}Mia{/b} делает? )"
    player_name "( Надеюсь, ее не поймают за этим... )"
    hide windowmiaday
    hide screen telescope
    show telescope_caught 1
    with dissolve

    jen "( Хм... Интересно, что он задумал. )"
    show telescope_caught 3 with dissolve
    pause
    show telescope_caught 5
    jen "( Опять?! )"
    scene location_home_bedroom_telescope_window
    show player 357 at Position(xpos=456,ypos=758)
    with dissolve
    pause
    show jenny 137 at right with fastdissolve
    pause
    show jenny 138
    jen "Кажется, тебе это нравится."
    show jenny 137
    show player 358 at Position(xpos=448)
    player_name "!!!" with vpunch
    show player 360 at Position(ypos=768)
    player_name "Ты можешь перестать подкрадываться ко мне?!"
    show jenny 138
    show player 361
    jen "Я просто хотела одолжить карандаш."
    jen "Я не ожидала, что снова увижу, как ты пялишься на наших соседей..."
    show player 360
    show jenny 137
    player_name "Я не пялился!"
    show player 361
    show jenny 138
    jen "Да ну?"
    jen "Позволь я посмотрю."
    show player 360
    show jenny 137
    player_name "Чего?"
    show player 361
    show jenny 138
    jen "Подвинься."
    show player 361 at left
    show jenny 142 at Position(xpos=806,ypos=768)
    with fastdissolve
    jen "Так, посмотрим..."
    show jenny 140
    pause
    show windowmiaday 3 with dissolve
    pause
    scene location_home_bedroom_telescope_window
    show player 361 at left
    show jenny 140 at Position(xpos=545,ypos=768)
    with dissolve
    jen "... Это девчонка из твоего класса?"
    show jenny 142
    jen "Тебе нравится смотреть как девушки мастурбируют?"
    show jenny 141
    show player 360
    player_name "Это не так! Я..."
    player_name "Это случайность, я не знал что она там!"
    show jenny 142
    show player 361
    jen "Ага, щас."
    jen "Бьюсь об заклад, ты любишь смотреть, как она делает это в своей комнате..."
    jen "Ты дрочишь, наблюдая за ней?"
    show jenny 141
    show player 360
    player_name "Нет..."
    show jenny 142
    show player 361
    jen "Хаха! Так я и поверила..."
    show jenny 138 at right with fastdissolve
    jen "Забудь про карандаш..."
    jen "Я просто позволю тебе закончить то, что ты начал..."
    hide jenny with fastdissolve
    show player 359
    pause
    $ renpy.end_replay()
    return

label telescope_mia_morning_1:
    scene windowmiamorning01
    if game.timer.dayOfWeek() == "Sun":
        player_name "( Она собирается в церковь.. )"
    elif game.timer.is_weekend():
        player_name "( Интересно, что она сегодня делает? )"
    else:
        player_name "( Она готовится к школе. )"
    return

label telescope_mia_morning_2:
    scene windowmiamorning02
    player_name "( Слишком поздно... Я всегда пропускаю самое интересное! )"
    return

label telescope_mia_afternoon_1:
    scene windowmiaday 1
    player_name "( Ее жалюзи закрыты. Ее, наверное, нет дома. )"
    return

label telescope_mia_afternoon_2:
    scene windowmiaday 2
    player_name "( Ее нет дома. )"
    return

label telescope_mia_night_1:
    scene windowmianight01
    player_name "( Она все время читает или учится... )"
    return

label telescope_mia_night_2:
    if not M_mia.get("telescope teddy seen"):
        $ persistent.cookie_jar["Mia"]["unlocked"] = True
        $ persistent.cookie_jar["Mia"]["gallery"]["01_unlocked"] = True
        $ M_mia.set("telescope teddy seen", True)
        scene windowmianight03a_b
        player_name "( Что она делает? )"
        player_name "..."
        player_name "( Она... )"
        player_name "( ...Трахает своего {b}Teddy Bear{/b}? )"
        player_name "( Вау... )"
        player_name "( Это реально круто- )"
        scene windowmianight03c with hpunch
        player_name "!!!"
        scene windowmianight03d
        player_name "( Вот дерьмо! )"
        player_name "( Думаю, ее только что поймали.... )"
        player_name "( Ее {b}мама{/b} должно быть в ярости... Она всегда так строга с ней...)"
        $ renpy.end_replay()
    else:
        call telescope_mia_night_3
    return

label telescope_mia_night_3:
    scene windowmianight02
    player_name "( Она должно быть уже спит. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
