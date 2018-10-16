label beachhouse_not_bought:
    scene expression player.location.background_blur
    show player 3 at left
    player_name "Эх...ключа то нету..."
    show player 4 at left
    player_name "Хмм... Этот домик продаётся..."
    show player 1 at left with dissolve
    player_name "Можно попытаться накопить их тех денег, которые {b}Тётя Диана{/b} мне платит..."
    with dissolve
    return

label beach_house_first_time:
    scene expression player.location.background_blur
    show player 14
    with dissolve
    player_name "Ух ты! Прекрасный домик!"
    player_name "И так много места!"
    show player 1
    pause
    show player 14
    player_name "Не верю что сейчас он мой!"
    show player 1
    pause
    show player 14
    player_name "Наверное надо начать поиски {b}мебели{/b}."
    player_name "... Тогда тут будет идеально!"
    return

label beachhouse_weekday_just_wokeup:
    scene expression L_beachhouse_bedroom.background_blur
    show player 7 with dissolve
    player_name "{b}*Зевает*{/b}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( Надо готовиться идти в школу... )"
    hide player with dissolve
    return

label beachhouse_weekend_just_wokeup:
    scene expression L_beachhouse_bedroom.background_blur
    show player 7 with dissolve
    player_name "{b}*Зевает*{/b}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( Надо за выходные что нибудь сделать... )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
