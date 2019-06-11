label donut_buy_dialogue:
    show beth 2
    beth "Вот тебе."
    show unlock51 at truecenter with dissolve
    pause
    hide unlock51 with dissolve
    show player 17
    show beth 1
    player_name "Спасибо."
    show player 1
    show beth 2
    beth "Наслаждайся сладкими дырочками!"
    hide player
    hide xtra
    hide beth
    with dissolve
    $ game.main()

label donut_locked:
    scene expression game.timer.image("backgrounds/location_donut_day{}_blur.jpg")
    show player 10 with dissolve
    player_name "( Я должен вернуться к ним в течении дня когда они будут открыты. )"
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
