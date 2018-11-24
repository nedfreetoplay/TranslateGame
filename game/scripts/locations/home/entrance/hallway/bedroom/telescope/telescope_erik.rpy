label erik_bedroom:
    if M_jenny.is_state(S_jenny_telescope_spying):
        call expression game.dialog_select("telescope_erik_sister_spying")
        $ M_jenny.trigger(T_jenny_spied_on_neighbour)
        jump expression game.dialog_select("bedroom_dialogue")
    else:
        call expression game.dialog_select(game.telescope.erik)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_erik_sister_spying:
    scene
    show windowerikday 3a
    player_name "( {b}Erik's landlady{/b} is there. )"
    show windowerikday 3b with fastdissolve
    player_name "( She's probably just checking on him... )"
    show windowerikday 3c with fastdissolve
    player_name "..."
    player_name "( They're kissing on the mouth? That's weird... )"
    show windowerikday 3d with fastdissolve
    player_name "( What the... )"
    player_name "( Did he just grab her boob?? )"
    show windowerikday 3l with fastdissolve
    player_name "( She's closing his blinds... )"
    show windowerikday 2 with fastdissolve
    pause
    hide windowerikday
    hide screen telescope
    show telescope_caught 1
    with dissolve

    jen "( Hmm... I wonder what he's up to. )"
    show telescope_caught 3 with dissolve
    pause
    show telescope_caught 5
    jen "( What is he doing? )"
    scene location_home_bedroom_telescope_window
    show player 357 at Position(xpos=456,ypos=758)
    with dissolve
    pause
    show jenny 137 at right with fastdissolve
    pause
    show jenny 138
    jen "Having fun?"
    show jenny 137
    show player 358 at Position(xpos=448)
    player_name "!!!" with vpunch
    show player 360 at Position(ypos=768)
    show jenny 136 at Position(xpos=952)
    player_name "What are you doing here?!"
    show player 361
    show jenny 135
    jen "The better question would be, what are YOU doing here?"
    jen "Don't you have anything better to do than to spy on our neighbors?"
    show player 360
    show jenny 136
    player_name "I... don't know what you're talking about!"
    show player 361
    show jenny 135
    jen "Oh, so you were watching birds then?"
    show player 360
    show jenny 136
    player_name "Maybe I am!"
    show player 359
    show jenny 135
    jen "Hah! You're pathetic..."
    hide jenny with fastdissolve
    pause
    show player 360
    player_name "You could at least close the door!"
    return

label telescope_erik_morning_1:
    scene windowerikmorning01
    if game.timer.is_weekend():
        player_name "( He's not in his room. )"
    else:
        player_name "( He probably already left for school. )"
    return

label telescope_erik_morning_2:
    scene windowerikmorning02
    if game.timer.is_weekend():
        player_name "( He probably stayed up all night playing that game... )"
    else:
        player_name "( He's playing games? He should be getting ready for school... )"
    return

label telescope_erik_afternoon_1:
    scene windowerikday 1
    player_name "( He's not home. )"
    return

label telescope_erik_afternoon_2:
    scene windowerikday 2
    player_name "( The blinds are closed. He must be using his lotion again. )"
    return

label telescope_erik_afternoon_3:
    scene windowerikday04a_b
    player_name "( What's {b}Erik{/b} looking at? )"
    player_name "( That looks oddly familiar... )"
    return

label telescope_erik_afternoon_4:
    scene windowerikday05a_b
    player_name "Uhh!!" with hpunch
    player_name "( I can see why he was so excited about getting it... )"
    return

label telescope_erik_night_1:
    scene windoweriknight01
    player_name "( He's always playing that game... )"
    return

label telescope_erik_night_2:
    scene windoweriknight02
    player_name "( The blinds are closed. He must be using his lotion again. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
