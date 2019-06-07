label annie_dialogue_music_classroom_intro:
    show player 2
    player_name "Hey, {b}Annie{/b}."
    show player 1
    show annie 3
    ann "I'm trying to concentrate."
    show annie 1
    show player 3
    player_name "..."
    show player 29 with dissolve
    player_name "Sorr-"
    show player 3 with dissolve
    show annie 7
    ann "I'M CONCENTRATING!"
    show annie 6
    show player 2f
    player_name "And I'm leaving!"
    player_name "Geez..."
    hide player
    hide annie
    with dissolve
    return

label annie_dialogue_ross_ask_model:
    show player 2 at left
    show annie 1 at right
    player_name "I'm working on a project for {b}Miss Ross{/b} and it requires a live model."
    player_name "Would you be interested?"
    show player 1
    show annie 3
    ann "Can't do it. I have rounds!"
    show player 10
    show annie 1
    player_name "Huh?"
    show player 11
    show annie 4
    ann "I've gotta patrol for miscreants!"
    ann "Get outta my way!"
    hide annie
    hide player
    show player 12f
    with dissolve

    player_name "Alright, sheesh!"
    player_name "Weirdo..."
    return

label annie_dialogue_leave:
    show player 14
    player_name "Hey {b}Annie{/b}!"
    show annie 5
    show player 1
    ann "Make it quick!"
    show annie 6
    show player 17
    player_name "Oh, nothing... I was just saying hi!"
    show annie 4
    show player 18
    ann "I'm on hall monitoring duty... And you're wasting my time."
    show annie 6
    show player 11
    player_name "..."
    show player 12
    player_name "All right. Sorry to bother you. Sheesh!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
