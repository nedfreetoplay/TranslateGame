label pizza_exterior_first_visit:
    scene expression game.timer.image("backgrounds/location_pizza_outside_day{}.jpg")
    show player 14 with dissolve
    player_name "( {b}Tony’s Pizza{/b}. He’s known to make the best pizza in town. )"
    hide player with dissolve
    return

label pizza_closed:
    scene expression "backgrounds/location_pizza_outside_night.jpg"
    show player 14 with dissolve
    player_name "I can't go there at night!"
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
