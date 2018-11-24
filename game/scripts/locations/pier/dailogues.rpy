label pier_first_visit:
    scene expression game.timer.image("backgrounds/location_pier{}.jpg")
    show player 2 at left with dissolve
    player_name "( It smells like the ocean around here. )"
    player_name "( People say it's the best spot for {b}fishing{/b}. )"
    return

label pier_board_first_visit:
    scene expression game.timer.image("pier{}")
    show player 4 at left with dissolve
    player_name "( These must be the {b}types of fish{/b} you can catch on the Pier and what {b}bait{/b} to use. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
