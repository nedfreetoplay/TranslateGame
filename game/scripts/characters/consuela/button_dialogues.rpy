label button_consuela_intro:
    show player 10 at left
    show consuela
    with dissolve
    player_name "Привет, {b}Консуэла{/b}."
    show player 5
    show consuela f_unsure
    consuela "Привет, мистер {b}[firstname]{/b}."
    show consuela f_normal
    show player 12
    player_name "Ты можешь звать меня просто {b}[firstname]{/b}..."
    show player 5
    show consuela f_unsure
    consuela "¿Qué? (Что?)"
    consuela "No hablo inglés. (Я не говорю по-английски.)"
    show consuela f_normal
    show player 10
    player_name "О, эээ..."
    show player 5
    pause
    consuela "..."
    show player 3 with dissolve
    player_name "..."
    show consuela f_unsure
    consuela "Эхх... Теперь я убираюсь."
    consuela "¿Sí? (Да?)"
    show consuela f_normal
    show player 10 with dissolve
    player_name "Ну, да."
    player_name "Эээ, Я говорю... Sí!"
    show player 14
    player_name "Спасибо, {b}Консуэла{/b}."
    show player 13
    show consuela f_normal_talk
    consuela "Пожалуйста, мистер {b}[firstname]{/b}."
    hide player
    hide consuela
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
