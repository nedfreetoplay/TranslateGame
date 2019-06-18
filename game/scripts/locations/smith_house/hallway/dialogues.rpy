label smith_hallway_sneaking:
    scene expression "backgrounds/location_smith_hallway_night_blur.jpg"
    show player 10 with dissolve
    player_name "... Хорошо, я улавливаю супер жуткую атмосферу здесь."
    player_name "Хочется уйти прямо сейчас!"
    show player 12
    player_name "... Но я пообещал {b}Рокси, что найду эти тесты{/b}."
    show player 5
    pause
    show player 10
    player_name "{b}Она должна держать их в одной из этих комнат{/b}!"
    hide player with dissolve
    return

label smith_side_doors_locked_dialogue:

    scene expression "backgrounds/location_smith_hallway_day_blur.jpg"
    show player 10 with dissolve
    player_name "Черт! Эта дверь заперта..."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
