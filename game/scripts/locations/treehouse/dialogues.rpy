label treehouse_first_visit:
    scene expression game.timer.image("treehouse{}_b")
    show player 32 with dissolve
    player_name "Cool! Our old treehouse is still holding up."
    hide player with dissolve
    return

label treehouse_closeup_first_visit:
    scene expression game.timer.image("treehouse_c{}")
    player_name "( That doesn't look too safe... )"
    return

label treehouse_interior_first_visit:
    scene expression game.timer.image("treehouse_inside{}_b")
    show player 2 with dissolve
    player_name "( Wow! It hasn't changed at all! )"
    player_name "( Let's have a look around... )"
    hide player with dissolve
    return

label treehouse_got_wood_pile:
    scene expression game.timer.image("treehouse{}_b")
    if M_ross.is_state(S_ross_get_easels):
        call expression game.dialog_select("treehouse_woodpile_ross_easels")

    elif M_dewitt.between_states(S_dewitt_garage_find_paint, S_dewitt_make_replacement_guitar):
        call expression game.dialog_select("treehouse_woodpile_dewitt_guitar")

    call expression game.dialog_select("treehouse_woodpile_after")
    $ player.get_item("wood_pile")
    $ game.main()

label treehouse_woodpile_ross_easels:
    show player 585 with dissolve
    player_name "These will work great!"
    show player 586
    pause
    show player 585
    player_name "I can take these to {b}Dad's old workbench{/b} at the house to build some easels."
    return

label treehouse_woodpile_dewitt_guitar:
    show player 585 with dissolve
    player_name "Yeah, this should work."
    player_name "With some tools and a little {b}paint{/b}, I can make a fake guitar no problem."
    return

label treehouse_woodpile_after:
    hide player with dissolve
    show expression "boxes/popup_item_wood1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_wood1.png" with dissolve
    return

label treehouse_got_controller:
    call expression game.dialog_select("treehouse_controller_dialogue_pre")
    $ player.get_item("controller")
    call expression game.dialog_select("treehouse_controller_dialogue_after")
    $ game.main()

label treehouse_controller_dialogue_pre:
    scene expression game.timer.image("treehouse_inside{}_b")
    show player 502b
    with dissolve
    player_name "There it is!"
    player_name "Man, {b}Erik{/b} sure did love this thing..."
    player_name "It's nice of him to let me take it."
    show expression "boxes/popup_item_controller1.png" at truecenter with dissolve

label treehouse_controller_dialogue_after:
    pause
    hide expression "boxes/popup_item_controller1.png" with dissolve
    show player 502
    player_name "I'd best get this to {b}June{/b}."
    return

label lure_02:
    call expression game.dialog_select("lure_02_dialogue_pre")
    $ player.get_item("lure01")
    call expression game.dialog_select("lure_02_dialogue_after")
    $ game.main()

label lure_02_dialogue_pre:
    scene expression "backgrounds/location_treehouse_box.jpg"
    show expression "objects/closeup_bait02.png" with dissolve
    return

label lure_02_dialogue_after:
    show unlock36 at truecenter with dissolve
    pause
    hide unlock36 with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
