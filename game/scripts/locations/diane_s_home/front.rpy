label diane_front_yard:
    $ player.go_to(L_diane_yard)
    $ game.main()

label diane_front_yard_night_locked:
    show expression game.timer.image("backgrounds/location_diane_front_day{}_blur.jpg")
    show player 10 with dissolve
    player_name "{b}Тётя Диана{/b} уже наверное спит..."
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
