label mia_bedroom:
    if M_jenny.is_state(S_jenny_telescope_spying_tier_2):
        call expression game.dialog_select("telescope_mia_sister_spying")
        $ persistent.cookie_jar["Mia"]["unlocked"] = True
        $ persistent.cookie_jar["Mia"]["gallery"]["02_unlocked"] = True
        $ M_jenny.trigger(T_jenny_spied_on_neighbour_tier_2)
        jump expression game.dialog_select("bedroom_dialogue")
    else:
        call expression game.dialog_select(game.telescope.mia)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_mia_sister_spying:
    scene
    show windowmiaday 3
    player_name "( Oh my... )"
    player_name "( What's {b}Mia{/b} doing? )"
    player_name "( I hope she doesn't get caught doing that... )"
    hide windowmiaday
    hide screen telescope
    show telescope_caught 1
    with dissolve

    jen "( Hmm... I wonder what he's up to. )"
    show telescope_caught 3 with dissolve
    pause
    show telescope_caught 5
    jen "( Again?! )"
    scene location_home_bedroom_telescope_window
    show player 357 at Position(xpos=456,ypos=758)
    with dissolve
    pause
    show jenny 137 at right with fastdissolve
    pause
    show jenny 138
    jen "You seem to be enjoying this."
    show jenny 137
    show player 358 at Position(xpos=448)
    player_name "!!!" with vpunch
    show player 360 at Position(ypos=768)
    player_name "Could you stop sneaking up on me like that?!"
    show jenny 138
    show player 361
    jen "I was just gonna borrow a pencil."
    jen "I didn't expect to catch you perving on our neighbors again..."
    show player 360
    show jenny 137
    player_name "I'm not!"
    show player 361
    show jenny 138
    jen "Oh, really?"
    jen "Let's see, then."
    show player 360
    show jenny 137
    player_name "What?"
    show player 361
    show jenny 138
    jen "Move over."
    show player 361 at left
    show jenny 142 at Position(xpos=806,ypos=768)
    with fastdissolve
    jen "Let's have a look..."
    show jenny 140
    pause
    show windowmiaday 3 with dissolve
    pause
    scene location_home_bedroom_telescope_window
    show player 361 at left
    show jenny 140 at Position(xpos=545,ypos=768)
    with dissolve
    jen "... Is that the girl from your class?"
    show jenny 142
    jen "Do you enjoy watching girls masturbate?"
    show jenny 141
    show player 360
    player_name "It's not like that! I..."
    player_name "It was an accident, I didn't know she was there!"
    show jenny 142
    show player 361
    jen "Yeah, right."
    jen "I bet you love watching her do things in her room..."
    jen "Do you jack off while watching her?"
    show jenny 141
    show player 360
    player_name "No..."
    show jenny 142
    show player 361
    jen "Haha! Sure..."
    show jenny 138 at right with fastdissolve
    jen "Forget the pencil..."
    jen "I'll just let you finish whatever you started here..."
    hide jenny with fastdissolve
    show player 359
    pause
    $ renpy.end_replay()
    return

label telescope_mia_morning_1:
    scene windowmiamorning01
    if game.timer.dayOfWeek() == "Sun":
        player_name "( She's getting ready for church. )"
    elif game.timer.is_weekend():
        player_name "( I wonder what she's doing today? )"
    else:
        player_name "( She's getting ready for school. )"
    return

label telescope_mia_morning_2:
    scene windowmiamorning02
    player_name "( Too late... I always miss the best part! )"
    return

label telescope_mia_afternoon_1:
    scene windowmiaday 1
    player_name "( Her blinds are closed. She's probably not home. )"
    return

label telescope_mia_afternoon_2:
    scene windowmiaday 2
    player_name "( She's not home. )"
    return

label telescope_mia_night_1:
    scene windowmianight01
    player_name "( She's always reading or studying... )"
    return

label telescope_mia_night_2:
    if not M_mia.get("telescope teddy seen"):
        $ persistent.cookie_jar["Mia"]["unlocked"] = True
        $ persistent.cookie_jar["Mia"]["gallery"]["01_unlocked"] = True
        $ M_mia.set("telescope teddy seen", True)
        scene windowmianight03a_b
        player_name "( What's she doing? )"
        player_name "..."
        player_name "( She's... )"
        player_name "( ...Humping her {b}Teddy Bear{/b}? )"
        player_name "( Wow... )"
        player_name "( That's really hot- )"
        scene windowmianight03c with hpunch
        player_name "!!!"
        scene windowmianight03d
        player_name "( Oh, crap! )"
        player_name "( I think she just got caught... )"
        player_name "( Her {b}Mom{/b} must be furious... She's always so strict with her... )"
        $ renpy.end_replay()
    else:
        call telescope_mia_night_3
    return

label telescope_mia_night_3:
    scene windowmianight02
    player_name "( She must be sleeping. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
