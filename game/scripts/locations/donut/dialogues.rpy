label donut_buy_dialogue:
    show beth 2
    beth "Here ya go."
    show unlock51 at truecenter with dissolve
    pause
    hide unlock51 with dissolve
    show player 17
    show beth 1
    player_name "Thank you."
    show player 1
    show beth 2
    beth "Enjoy the sweet holes!"
    hide player
    hide xtra
    hide beth
    with dissolve
    $ game.main()

label donut_locked:
    scene expression game.timer.image("backgrounds/location_donut_day{}_blur.jpg")
    show player 10 with dissolve
    player_name "( I should come back during the day while they're open. )"
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
