label smith_hallway_sneaking:
    scene expression "backgrounds/location_smith_hallway_night_blur.jpg"
    show player 10 with dissolve
    player_name "... Okay, I'm picking up a super creepy vibe here."
    player_name "I'm ready to leave now!"
    show player 12
    player_name "... But I promised {b}Roxxy I'd find those exams{/b}."
    show player 5
    pause
    show player 10
    player_name "{b}She must keep them in one of these rooms{/b}!"
    hide player with dissolve
    return

label smith_side_doors_locked_dialogue:

    scene expression "backgrounds/location_smith_hallway_day_blur.jpg"
    show player 10 with dissolve
    player_name "Shoot! This door is locked..."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
