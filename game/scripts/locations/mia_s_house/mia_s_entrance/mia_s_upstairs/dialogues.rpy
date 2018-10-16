label mias_upstairs_mia_parent_unblock:
    scene mia_house_upstairs_night_b
    show player 1 at left
    show helen 2 at right
    with dissolve
    helen "Что ты здесь делаешь?"
    show helen 1
    show player 22
    player_name "!!!" with vpunch
    show helen 1
    show player 10
    player_name "Я, эээ-"
    show player 5
    show helen 2
    helen "Ты пытаешься подсмотреть за {b}Мией{/b}?"
    show player 10
    show helen 1
    player_name "Но, я могу объясни-"
    show player 5
    show helen 2
    helen "Тебя здесь не должно быть, юноша."
    show helen 3
    helen "Держись подальше от моей дочери. Ясно?"
    show player 10
    show helen 1
    player_name "Да, мэм..."
    return

label mias_upstairs_mia_midnight_help:
    scene mia_house_upstairs_night_b
    show player 11 with dissolve
    "*приглушенные звуки*"
    show player 30
    player_name "А?"
    player_name "( Звуки доносятся из {b}комнаты слева{/b}... )"
    hide player with dissolve
    return

label mias_upstairs_mia_unexpected_visit:
    label helen_baton_replay:
        scene mia_house_upstairs_b
    show player 30 with dissolve
    player_name "А?"
    show player 10
    player_name "( Звуки доносятся из спальни {b}Хелен{/b}... )"
    player_name "( ...{b}Мия{/b} должно быть там вместе с мамой. )"
    hide player with dissolve
    if not store._in_replay == None:
        jump helen_baton_replay_1
    return

label mias_upstairs_helen_aftersex_mia_suspicious:
    scene mia_house_upstairs_night_b
    show mia 44f at right
    show player 22 at left
    with dissolve
    player_name "!!!" with hpunch
    show mia 43f
    mia "{b}[firstname]{/b}?"
    show mia 44f
    show player 29 with dissolve
    player_name "Ой... Ёй... Привет!"
    show player 3
    show mia 43f
    mia "Я и не знала что ты здесь."
    show mia 44f
    show player 12 with dissolve
    player_name "Ох..."
    show player 11
    show mia 43f
    mia "А что ты делал в маминой спальне?"
    show mia 44f
    show player 10
    player_name "Эммм... Да вот... Она..."
    player_name "...Она просто хотела поговорить со мной о...ээээм...библейских текстах."
    show player 5
    show mia 43f
    mia "Серьёзно? А с чего это ты всем этим заинтересовался?"
    show mia 44f
    show player 29 with dissolve
    player_name "Эмм... Ну... Вот так. Я только вот недавно в это всё втянулся."
    player_name "Эй! Хочешь потусоваться вместе? Я вот только закончил...говорить...с твоей мамой."
    show player 3
    show mia 46f
    mia "Мне не особо хочется."
    mia "Мне сейчас хочется просто посидеть в своей комнате."
    show mia 45f
    show player 29
    player_name "Окей..."
    player_name "Я тогда домой пойду."
    show player 3
    show mia 46f
    mia "Да, давай."
    hide mia
    show player 24
    with dissolve
    player_name "...Пока..."
    hide player with dissolve
    return

label helens_locked_room_block:
    scene expression game.timer.image("mia_house_upstairs{}_b")
    player_name "( Дверь заперта. )"
    if M_mia.is_state(S_mia_midnight_help):
        player_name "( Мне нужно найти {b}ключ{/b}... )"
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
