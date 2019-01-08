label pizza_exterior_first_visit:
    scene expression game.timer.image("backgrounds/location_pizza_outside_day{}.jpg")
    show player 14 with dissolve
    player_name "( {b}Пицца Тони{/b}. Он известен тем, что делает лучшую пиццу в городе. )"
    hide player with dissolve
    return

label pizza_closed:
    scene expression "backgrounds/location_pizza_outside_night.jpg"
    show player 14 with dissolve
    player_name "Я не могу пойти туда ночью!"
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
