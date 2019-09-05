label kevin_gym_take_it_easy:
    show player 14
    player_name "Я собираюсь выбраться отсюда, чувак."
    show player 13
    show kevin 11b with dissolve
    kev "Уже, братан?"
    show kevin 11c
    show player 14
    player_name "Да, у меня есть некоторые другие вещи которые мне нужно делать."
    show player 13
    show kevin 9 with dissolve
    kev "А, хорошо."
    show kevin 8
    show player 14
    player_name "Увидимся позже, {b}Кевин{/b}."
    hide kevin
    hide player
    with dissolve
    return

label kevin_gym_lets_lift:
    show player 14
    player_name "Давай просто поднимем."
    show player 13
    show kevin 9
    kev "О, ты готов покачать немного железа?"
    show kevin 10 with dissolve
    kev "Отлично, братан."
    kev "Давайте сделаем это!"
    hide kevin
    hide player
    with dissolve
    return

label kevin_gym_intro:
    scene expression player.location.background_blur with None
    show player 13 at left
    show kevin 9 at right
    with dissolve
    kev "Эй, братан!"
    show kevin 8
    show player 14
    player_name "Как дела, {b}Кевин{/b}?"
    show player 13
    show kevin 9
    kev "Я работал над своими ягодицами все утро!"
    show kevin 13b with dissolve
    kev "Почувствуй, какие тугие эти мальчики!"
    show player 10b with dissolve
    player_name "Нет, спасибо..."
    show player 5b
    kev "Ты уверен, братан?"
    kev "Ты не знаешь что теряешь!"
    show kevin 8 with dissolve
    show player 29 with dissolve
    player_name "Хех."
    show player 5 with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
