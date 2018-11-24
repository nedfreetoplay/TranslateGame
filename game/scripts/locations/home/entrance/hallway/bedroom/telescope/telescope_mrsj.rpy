label erikmom_bedroom:
    if M_jenny.is_state(S_jenny_telescope_spying_tier_3):
        call expression game.dialog_select("telescope_mrsj_sister_spying")
        $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
        $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["02_unlocked"] = True
        $ M_jenny.trigger(T_jenny_spied_on_neighbour_tier_3)
        jump expression game.dialog_select("bedroom_dialogue")
    else:

        call expression game.dialog_select(game.telescope.mrsj)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_mrsj_sister_spying:
    show windowmrsjday 3a
    player_name "( Woah! She's completely naked!! )"
    show windowmrsjday 3b with fastdissolve
    player_name "( Is that a bouncing ball... with a dildo on it?! )"
    show windowmrsjday 3c with fastdissolve
    player_name "( Why didn't she close the blinds? )"
    show windowmrsjday 3c-d
    player_name "( It's like she wants to be seen... )"
    player_name "( I think she knows... )"
    player_name "( She's staring right at me. )"
    hide windowmrsjday
    hide screen telescope
    show telescope_caught 1
    with dissolve

    jen "( Hmm... I wonder what he's up to. )"
    show telescope_caught 3 with dissolve
    pause
    show telescope_caught 5
    jen "( Busted! )"
    scene location_home_bedroom_telescope_window
    show player 357 at Position(xpos=456,ypos=758)
    with dissolve
    pause
    show jenny 136 at Position(xpos=725,ypos=0,xanchor=0,yanchor=0) with fastdissolve
    pause
    show jenny 135
    jen "Gosh, you're such a pervert!!"
    show jenny 136
    show player 358 at Position(xpos=448)
    player_name "!!!" with vpunch
    show player 360 at Position(ypos=768)
    player_name "How did you-"
    show player 361
    show jenny 135
    jen "Oh, I knew you'd be here."
    jen "You can't get enough of that telescope..."
    jen "Let me see what you've found this time."
    show player 360 at Position(ypos=768)
    show jenny 136
    player_name "Wait-"
    show player 361
    show jenny 138
    jen "Move over."
    show player 361 at left
    show jenny 142 at Position(xpos=284,ypos=231)
    with fastdissolve
    jen "Let's have a look..."
    show jenny 140 at Position(ypos=229)
    pause
    show windowmrsjday 3c-d with dissolve
    jen "{b}Mrs. Johnson{/b}?!!"
    jen "Well, damn..."
    jen "She's naughty, isn't she?"
    scene location_home_bedroom_telescope_window
    show player 361 at left
    show jenny 140 at Position(xpos=284,ypos=229,xanchor=0,yanchor=0)
    with dissolve
    pause
    show jenny 142 at Position(xpos=284,ypos=231,xanchor=0,yanchor=0)
    jen "Does she always do this kind of stuff in front of her window?"
    show jenny 140 at Position(xpos=284,ypos=229,xanchor=0,yanchor=0)
    jen "It's as if she wants to be seen..."
    show player 360
    player_name "...I guess?"
    show player 361
    jen "This is hot... The way she's grinding on that ball..."
    show jenny 145_146_147_148 at Position(xpos=286,ypos=229,xanchor=0,yanchor=0) with fastdissolve
    pause
    show player 364
    player_name "!!!"
    show player 361
    jen "I love the way her ass bounces off it."
    show player 362
    jen "I wish that was me sitting on that ball..."
    show jenny 144 at Position(ypos=231)
    show player 361
    jen "What's the matter?"
    jen "I can't enjoy myself?"
    show player 360
    show jenny 143
    player_name "I didn't say that..."
    show player 361
    show jenny 144
    jen "Which do you prefer?"
    jen "Watching {b}Mrs. Johnson{/b}... or watching {b}me{/b}?"
    show player 360
    show jenny 143
    player_name "I don't know..."
    show jenny 139 at right with fastdissolve
    show player 361
    jen "Oops!"
    jen "Well, would you look at that..."
    jen "I'm all {b}wet{/b}!"
    jen "I should keep these for later... Maybe trade them for something..."
    hide jenny with dissolve
    pause
    show player 362
    pause
    $ renpy.end_replay()
    return

label telescope_mrsj_morning_1:
    scene windowmrsjmorning01
    player_name "( ...is that {b}Erik's landlady{/b}?! )"
    scene windowmrsjmorning01b
    player_name "( Oh wow! She's getting dressed... )"
    scene windowmrsjmorning01c
    player_name "( No! Just a little bit longer! )"
    scene windowmrsjmorning01d
    player_name "( Damn! Show's over... )"
    return

label telescope_mrsj_morning_2:
    scene windowmrsjday02
    player_name "( Her blinds are closed. She's probably not home. )"
    return

label telescope_mrsj_afternoon_1:
    scene windowmrsjday01
    player_name "( She's not home. )"
    return

label telescope_mrsj_afternoon_2:
    show windowmrsjday 3a
    player_name "( Woah... She's completely naked!! )"
    show windowmrsjday 3b with fastdissolve
    player_name "( Is that a bouncing ball... with a dildo on it?! )"
    show windowmrsjday 3c with fastdissolve
    player_name "( Why didn't she close the blinds? )"
    show windowmrsjday 3c-d
    player_name "( It's like she wants to be seen... )"
    player_name "( I think she knows... )"
    player_name "( She's staring right at me. )"
    return

label telescope_mrsj_afternoon_3:
    scene windowmrsjday02
    player_name "( Her blinds are closed. She's probably not home. )"
    return

label telescope_mrsj_night_1:
    scene windowmrsjnight03
    player_name "( ...Is she practicing yoga? )"
    player_name "( ...On her bed? )"
    scene windowmrsjnight04
    player_name "..."
    player_name "( {b}Erik's landlady{/b} is so fit... )"
    player_name "( ...she really does have a great body... )"
    return

label telescope_mrsj_night_2:
    scene windowmrsjnight01
    player_name "( She's not in her room... )"
    return

label telescope_mrsj_night_3:
    scene windowmrsjnight02
    player_name "( She must be sleeping. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
