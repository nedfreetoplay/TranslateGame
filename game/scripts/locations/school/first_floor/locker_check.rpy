label locker_check(direction, locker):
    if direction == "left":
        show expression game.timer.image("backgrounds/location_school_lefthall{}.jpg")
    else:
        show expression game.timer.image("backgrounds/location_school_right_hall{}.jpg")
    show player 1 at center
    if game.timer.is_day():
        if player.has_picked_up_item("master_key"):
            if not locker.is_visited:
                $ charname = locker.name.split("'")[0]
                player_name "Используя мастер-ключ, я смогу открыть {b}[charname]{/b} шкафчик."
            $ player.location = locker
        else:
            call expression game.dialog_select("locker_locked_{}".format(random.randint(1,2)))
            $ game.main()
    else:
        if not player.has_picked_up_item("master_key"):
            call expression game.dialog_select("locker_locked_night")
            $ game.main()
        else:
            if not locker.is_visited:
                $ charname = locker.name.split("'")[0]
                player_name "Используя мастер-ключ, я смогу открыть {b}[charname]{/b} шкафчик."
            $ player.location = locker
    scene expression locker.background
    return

label locker_locked_1:
    show player 10 with dissolve
    player_name "Это не мой шкафчик... Мне нужен ключ, чтобы открыть его."
    return

label locker_locked_2:
    player_name "Заперто и у меня нет ключа."
    player_name "Наверное, у {b}Директрисы Смит{/b} есть ключ ко всему."
    hide player with dissolve
    return

label locker_locked_night:
    scene expression player.location.background_blur
    show player 5 with dissolve
    player_name "Сейчас не лучшее время слоняться по коридорам. Я должен попробовать еще раз в течение дня."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
