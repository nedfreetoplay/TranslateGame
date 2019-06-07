label dewitt_dialogue_lounge_intro:
    scene location_school_lounge_couch
    show player 10 at left
    show dewittl 5 at right
    with dissolve
    pause
    show dewittl 1 with dissolve
    player_name "Oh, hi there, {b}Miss DeWitt.{/b}"
    show player 11
    show dewittl 3 with dissolve
    dewitt "{b}[firstname]{/b}? You're not supposed to be in here..."
    show player 10
    show dewittl 2
    player_name "Yeah, sorry."
    show player 2
    player_name "{b}Miss Ross{/b} has me looking for old magazines."
    player_name "We're making a collage!"
    show player 1
    show dewittl 3
    dewitt "Collage, huh?"
    dewitt "I used to make those all the time when I was younger!"
    show player 2
    show dewittl 2
    player_name "What are you snacking on?"
    show player 1
    show dewittl 3b at Position(xpos=0.965, ypos=1.0) with dissolve
    dewitt "Oh this?"
    show dewittl 3 at right with dissolve
    dewitt "It's one of {b}Barbara's special brownies{/b}."
    show player 2
    show dewittl 2
    player_name "I didn't know {b}Miss Ross{/b} could bake?"
    show player 1
    show dewittl 3
    dewitt "She makes the BEST brownies!"
    dewitt "I just can't get enough!"
    show player 2
    show dewittl 2
    player_name "... Neat!"
    player_name "So, do you think I could have a few of those magazines there on the table?"
    show player 1
    show dewittl 3
    dewitt "I don't see why not."
    show player 2
    show dewittl 2
    player_name "Awes-"
    show player 11
    show dewittl 6 with dissolve
    dewitt "If you can answer a question off my next test!"
    show player 10
    show dewittl 2 with dissolve
    player_name "Really?"
    show player 11
    show dewittl 3
    dewitt "Nothing's free in life, {b}[firstname]{/b}."
    dewitt "Now lets see..."
    dewitt "The flute is a member of which instrumental family?"
    return

label dewitt_dialogue_lounge_stat_pass:
    show player 2 at left
    show dewittl 2 at right
    player_name "That's easy! Woodwind."
    show player 1
    show dewittl 3
    dewitt "Very good, {b}[firstname]{/b}!"
    dewitt "I guess you've been paying attention in class after all."
    show dewittl 4 with dissolve
    dewitt "Go ahead and take as many magazines as you need."
    show player 595 with dissolve
    show dewittl 2
    player_name "Awesome!"

    player_name "Thanks, {b}Miss Dewitt{/b}! Enjoy your brownie!"
    show player 594
    show dewittl 1b at Position(xpos=0.965, ypos=1.0) with dissolve
    dewitt "Ohm, so good! Mmm..."
    return

label dewitt_dialogue_lounge_stat_fail:
    show player 10
    show dewittl 2
    player_name "[int_warn]Err... Instrument's have families?"
    show player 11
    show dewittl 3
    dewitt "[int_warn]Heh, well that's something you'd better figure out if you want these magazines."
    dewitt "[int_warn]Come back when you know the answer."
    show dewittl 2
    show player 10
    player_name "[int_warn]Ah, man..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
