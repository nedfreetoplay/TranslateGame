label erik_dialogue_intro:
    scene location_school_computer_day_blur
    show player 2 at left
    show erik 1 at right
    with dissolve
    return

label erik_dialogue_okita_get_bifocal_lenses:
    show player 2
    player_name "I'm helping Okita out with a project."
    show player 1
    show erik 4
    eri "Really? Awesome!"
    eri "What kinda project is it?"
    show player 2
    show erik 1
    player_name "Uhh, I don't think I'm supposed to say..."
    show player 1
    show erik 4
    eri "Oh, top secret research?"
    eri "Cool, can I help?"
    show player 2
    show erik 1
    player_name "Actually Yes!"
    player_name "I need to find a couple of thick {b}lenses{/b}."
    player_name "You wouldn't happen to have a spare set of glasses, would you?"
    show player 1
    show erik 4
    eri "You kidding?"
    eri "Do you know how many times {b}Dexter{/b} has broken this pair?"
    eri "I always keep a spare set close."
    show player 2
    show erik 1
    player_name "Great!!"
    player_name "Would you let me have them?"
    show player 1
    show erik 4
    eri "Sure!"
    show player 2
    show erik 1
    player_name "Thanks, man!"
    show player 1
    show erik 4
    eri "No problem, {b}[firstname]{/b}! What are friends for?"
    show player 10
    show erik 1
    player_name "... Oh, wait!"
    show player 29 with dissolve
    player_name "I forgot, they need to be {b}Varifocal lenses{/b}..."
    show player 3
    show erik 5
    eri "Vari- What?"
    show player 10 with dissolve
    show erik 1
    player_name "Are you farsighted or nearsighted?"
    show player 11
    show erik 5
    eri "Nearsighted. Why?"
    show player 10
    show erik 1
    player_name "Crap! I need lenses from someone who is both."
    show player 11
    show erik 5
    eri "Oh."
    show player 24
    show erik 1
    player_name "*sigh*"
    show player 10
    player_name "I guess I'll have to keep looking."
    show player 11
    show erik 5
    eri "Sorry, {b}[firstname]{/b}."
    show player 2
    show erik 1
    player_name "It's alright, {b}Erik{/b}. Thanks anyways."
    show player 1
    show erik 4
    eri "Anytime, Man."
    return

label erik_dialogue_leave:
    show player 14
    player_name "Oh, nothing!"
    player_name "Just saying hi."
    show player 1
    show erik 4
    june "Oh, okay then..."
    show erik 1
    show player 29 at Position(xoffset=8)
    player_name "Err... I'll see you later!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
