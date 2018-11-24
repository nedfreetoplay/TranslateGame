label second_floor_first_visit:
    scene stairs
    show player 4 with dissolve
    player_name "Hmmm..."
    player_name "( Not too many people going into the Cafeteria, yet. )"
    show player 12
    player_name "( It's not lunch time yet. )"
    hide player with dissolve
    return

label second_floor_okita_dose_smith:
    scene expression game.timer.image("backgrounds/location_school_second{}_blur.jpg")
    show player 35
    player_name "Hmm, I think {b}Principal Smith{/b} goes into the {b}Teacher's Lounge{/b} to {b}drink coffee{/b} in the afternoons."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
