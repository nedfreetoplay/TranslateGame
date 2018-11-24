label obituary_records(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Hmm..."
    player_name "It seems like the only name under Boatsmith is..."
    player_name "...Ben Dover?"
    player_name "Now I just need to visit the cemetary and find the right tomb stone."
    $ M_aqua.trigger(T_aqua_obituary_records)
    return

label keycode_note_closeup(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "This is the {b}code to Okita's office{/b}. {b}6219{/b}."
    return


label scroll(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Hmm..."
    player_name "There's a strange picture on it."
    player_name "It looks like a crescent moon..."
    player_name "{b}It must be useful for something...{/b}"
    return

label treasure_map(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "This is too cool! An actual treasure map!"
    player_name "Hmm..."
    player_name "It looks like a drawing of the {b}coast...{/b}"
    player_name "...And that looks like our local beach?"
    player_name "... and here, there's an X on a {b}small island...{/b}"
    player_name "I wonder what it leads to?"
    $ M_aqua.trigger(T_aqua_obituary_records)
    return

label weird_coin(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Huh?"
    player_name "That looks like a really old coin."
    player_name "Just look at these odd {b}symbols{/b}!"
    player_name "I should keep it. Maybe it's worth something?"
    return

label old_book(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "This book looks like it would be useful decoding something."
    player_name "..."
    if not player.has_item("weird_coin"):
        player_name "Heh. Maybe some {b}hidden pirate treasure{/b} someone tossed aside carelessly."
        player_name "But that's just {b}wishful thinking{/b}."
    else:
        player_name "I think that {b}pirate coin{/b} had a four digit number on it."
        player_name "I should look at it again."
    return

label golden_compass(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Whoa!!"
    player_name "I can't believe it! I found the treasure!."
    player_name "This has to be the compass Terry was talking about."
    return

label tigger(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Whew, this mean bastard put up quite a fight."
    player_name "... and just look at those teeth!"
    player_name "It's no wonder why Terry wanted him dead."
    player_name "I can't wait to show him!"
    return


label pregnax_pills(item):
    scene expression player.location.background_blur
    if M_player.get("took pregnax"):
        show player 705 with dissolve
        player_name "( Hmm, the directions say I need to {b}take one pill, orally, prior to engaging in sexual activity{/b}. )"
        player_name "( {b}Effects will last for 24 hours.{/b} )"
        player_name "( {b}There's also a warning label, \"Do not use this medication if your partner is currently menstruating or has undergone menopause.\"{/b} )"
        player_name "( I've already taken a dose today. )"
        player_name "( I definitely shouldn't take another. )"
        hide player with dissolve
    else:
        show player 705 with dissolve
        player_name "( Hmm, the directions say I need to {b}take one pill, orally, prior to engaging in sexual activity{/b}. )"
        player_name "( {b}Effects will last for 24 hours.{/b} )"
        player_name "( {b}There's also a warning label, \"Do not use this medication if your partner is currently menstruating or has undergone menopause.\"{/b} )"
        player_name "( Should I take a {b}Pregnax{/b} pill? )"
        menu:
            "Yes.":
                show player 706 with dissolve
                player_name "( Welp, here goes nothing... )"
                show player 707 with dissolve
                pause
                $ player.pregnancy_chance *= 2
            "No":
                show player 705
                player_name "Nah, I don't think now is the best time to take one of these."
        hide player with dissolve
        $ M_player.set("took pregnax", True)
    $ game.main()

label condom:
    scene expression game.timer.image("jennybedroom{}")
    show expression "objects/closeup_condom.png" with dissolve
    player_name "A {b}condom{/b}?!"
    player_name "{b}[jen_name]{/b} must be hiding them in her room..."
    player_name "She probably won't notice if I only take one..."
    hide expression "objects/closeup_condom.png" with dissolve
    show expression "boxes/popup_condom.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_condom.png" with dissolve
    $ game.main()

label mysterious_statue_1(item):
    scene expression player.location.background_blur
    show player 688
    with dissolve
    player_name "( Hmm, it looks like the lower half a nude woman. )"
    player_name "( What's with the tail though? )"
    show player 689
    player_name "( There's something written on the bottom of it. )"
    show expression item.closeup
    hide player
    player_name "{b}\"Delmont.\"{/b}"
    player_name "Hmm, {b}Delmont{/b}..."
    player_name "It sounds familiar."
    hide expression item.closeup
    $ game.main()

label attic_key:
    $ suffix = ""
    if (M_mom.get_state() == S_mom_diane_visit and game.timer.is_evening()):
        $ suffix = "_evening"
    elif game.timer.is_dark():
        $ suffix = "_night"
    scene expression "home_entrance{}".format(suffix)
    show expression "objects/closeup_key.png" with dissolve
    player_name "( I've never seen this key before. )"
    player_name "( It's rather small... )"
    hide expression "objects/closeup_key.png" with dissolve
    show expression "boxes/popup_key.png" at truecenter with dissolve
    $ renpy.pause()
    $ player.get_item("attic_key")
    hide expression "boxes/popup_key.png" with dissolve
    jump home_entrance

label ring:
    scene expression game.timer.image("attic{}")
    show expression "objects/closeup_ring.png" with dissolve
    player_name "( That looks like an expensive ring! )"
    player_name "( What was it doing all the way up there? )"
    hide expression "objects/closeup_ring.png" with dissolve
    show expression "boxes/popup_ring.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_ring.png" with dissolve
    jump attic_dialogue

label cheerleader_outfit:
    scene expression game.timer.image("attic{}")




    show expression "boxes/popup_item_outfit1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_outfit1.png" with dissolve
    jump attic_dialogue

label fishing_rod:
    scene expression game.timer.image("attic{}")
    show expression "objects/closeup_rod.png" with dissolve
    player_name "That's {b}Dad{/b}'s old {b}fishing rod{/b}!!"
    player_name "( I remember when we used to go fishing by the {b}pier{/b}, when I was little. )"
    player_name "{b}*Sigh*{/b}"
    player_name "I miss {b}Dad{/b}..."
    hide expression "objects/closeup_rod.png" with dissolve
    show expression "boxes/popup_item_rod1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_rod1.png" with dissolve
    if L_pier.locked:
        $ L_pier.unlock()
    jump attic_dialogue

label backpack_pickup_dialogue:
    scene location_park_day_blur
    show player 608
    with dissolve
    pause
    show player 608b
    player_name "This is definately {b}Eve's{/b} backpack."
    player_name "Hmm, I don't see her {b}Art Pad{/b} though."
    show player 610 with dissolve
    player_name "I should {b}ask her about it when I return this{/b}."
    show expression "boxes/popup_item_backpack1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_backpack1.png"
    $ player.get_item("eve_backpack")
    jump park_dialogue

label roxxy_homework_pickup_dialogue:
    scene mc_locker
    player_name "Ah, here it is!"
    player_name "Now I just need to {b}Bring this to Roxxy.{/b}."
    show expression 'boxes/popup_item_homework5.png' at truecenter with dissolve
    pause
    hide expression 'boxes/popup_item_homework5.png'
    $ player.get_item("roxxy_homework")
    $ player.go_to(L_school_hall)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
