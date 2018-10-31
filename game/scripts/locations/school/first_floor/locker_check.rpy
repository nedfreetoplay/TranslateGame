label locker_check(direction, locker):
    if direction == "left":
        show expression game.timer.image("backgrounds/location_school_lefthall{}.jpg")
    else:
        show expression game.timer.image("backgrounds/location_school_right_hall{}.jpg")
    show player 1 at center
    if player.has_picked_up_item("master_key"):
        if not locker.is_visited:
            $ charname = locker.name.split("'")[0]
            player_name "Используя мастер-ключ, я смог открыть {b}[charname]{/b} шкафчик."
        $ player.location = locker
    else:
        call expression "locker_locked_{}".format(random.randint(1,2))
        $ game.main()
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
