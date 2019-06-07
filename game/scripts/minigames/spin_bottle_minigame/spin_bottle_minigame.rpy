label spin_bottle_minigame_kiss_mc_roxxy:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show roxxy front sitting 1 at Position (xoffset=3)
    show player car 2b zorder 1 at Position (xoffset=-3)
    show player_arms car 1 zorder 2 at Position (xoffset=-3)
    with dissolve
    pause
    show player front sitting 7 at Position (xoffset=-3)
    show player_shadow front sitting 1 zorder 0
    show player_arms front sitting 3 at Position (xoffset=3-3)
    show roxxy front sitting 3b at Position (xoffset=3)
    show roxxy_arm front sitting 1 at Position (xoffset=3)
    with dissolve
    rox "Mmm."
    player_name "..."
    show player front sitting 7b at Position (xoffset=-3)
    show roxxy front sitting 3 at Position (xoffset=3)
    pause
    show player front sitting 7 at Position (xoffset=-3)
    show roxxy front sitting 3b at Position (xoffset=3)
    if randomizer() < 33:
        missy "They're so cute together, aren't they {b}Becca{/b}?"
        becca "..."
    elif randomizer() < 66:
        rox "He's like, the best kisser..."
        missy "I'm so jelly right now."
        becca "..."
    else:
        becca "{b}Roxxy's{/b} really skilled with her tongue..."
        missy "Yeah, but so is {b}[firstname]{/b}!"
        becca "..."
    show player front sitting 7b at Position (xoffset=-3)
    show roxxy front sitting 3 at Position (xoffset=3)
    pause
    hide player
    hide roxxy
    hide roxxy_arm
    hide player_arms
    hide player_shadow
    with dissolve
    return

label spin_bottle_minigame_kiss_mc_becca:
    if randomizer() > 50:
        scene expression "backgrounds/location_beach_fire_kiss.jpg"
        show becca front sitting 1
        show player car 2b zorder 1
        show player_arms car 1 zorder 2
        with dissolve
        pause
        show player front sitting 7b
        show player_shadow front sitting 1 zorder 0
        show player_arms front sitting 3
        show becca front sitting 3
        with dissolve
        becca "Mmm."
        player_name "..."
        show player front sitting 7
        show becca front sitting 3b
        pause
        show player front sitting 7b
        show becca front sitting 3
        if randomizer() < 33:
            rox "Yeah, that's it..."
            rox "Play with her nipples!"
            missy "Hehe, look how turned on she is!"
        elif randomizer() < 66:
            missy "I'm sorry you have to kiss that ugly freckle faced ginger, {b}[firstname]{/b}..."
            rox "Shut up, {b}Missy{/b}..."
        else:
            rox "This is really hot!"
        show player front sitting 7
        show becca front sitting 3b
        if randomizer() < 50:
            rox "C'mon {b}Becca{/b}, use more tongue!"
            becca "..."
        else:
            missy "Bleh, {b}Becca{/b} is a boring kisser."
            missy "Just wait till it's my turn, {b}[firstname]{/b}!"
        show player front sitting 7b
        show becca front sitting 3
    else:

        scene expression "backgrounds/location_beach_fire_kiss.jpg"
        show becca front sitting 1
        show player car 2b zorder 1
        show player_arms car 1 zorder 2
        with dissolve
        pause
        show player_shadow front sitting 1 zorder 0
        show player front sitting 7
        show player_arms front sitting 4
        show becca front sitting 3b
        with dissolve
        if randomizer() < 33:
            becca "Ngghhh!"
        else:
            becca "Mmm."
            player_name "..."
        show player front sitting 7b
        show player_arms front sitting 4d
        show becca front sitting 3
        pause
        show player front sitting 7
        show player_arms front sitting 4
        show becca front sitting 3b
        if randomizer() < 33:
            rox "Yeah, that's it..."
            rox "Play with her nipples!"
            missy "Hehe, look how turned on she is!"
        elif randomizer() < 66:
            missy "I'm sorry you have to kiss that ugly freckle faced ginger, {b}[firstname]{/b}..."
            rox "Shut up, {b}Missy{/b}..."
        else:
            rox "This is really hot!"
        show player front sitting 7b
        show player_arms front sitting 4d
        show becca front sitting 3
        if randomizer() < 50:
            rox "C'mon {b}Becca{/b}, use more tongue!"
            becca "..."
        else:
            missy "Bleh, {b}Becca{/b} is a boring kisser."
            missy "Just wait till it's my turn, {b}[firstname]{/b}!"
        show player front sitting 7
        show player_arms front sitting 4
        show becca front sitting 3b
    pause
    hide player
    hide player_arms
    hide player_shadow
    hide becca
    with dissolve
    return

label spin_bottle_minigame_kiss_mc_missy:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show missy front sitting 1
    show player car 2b zorder 1 at Position (xoffset=-7)
    show player_arms car 1 zorder 2 at Position (xoffset=-7)
    pause
    show player_shadow front sitting 1 zorder 0
    show player front sitting 7 at Position (xoffset=-7)
    show player_arms front sitting 4 at Position (xoffset=-7)
    show missy front sitting 3b
    show missy_arm front sitting 1 zorder 3
    missy "Mmm."
    player_name "..."
    show player front sitting 7b at Position (xoffset=-7)
    show player_arms front sitting 4c
    show missy front sitting 3
    pause
    show player front sitting 7 at Position (xoffset=-7)
    show player_arms front sitting 4 at Position (xoffset=-7)
    show missy front sitting 3b
    if randomizer() < 33:
        rox "Yeah, squeeze those tits, {b}[firstname]{/b}!"
        becca "There's barely anything there to squeeze..."
        rox "Shut up, {b}Becca{/b}."
    if randomizer() < 66:
        becca "God, she's a sloppy kisser!"
        becca "Just what in the hell is she trying to do with her tongue, anyways?!"
        rox "I know, right?"
        rox "Somebody needs to teach that girl how to french..."
    else:
        rox "Slow down, {b}Missy{/b}!"
        rox "She's so freaking impatient..."
        becca "Yeah, I think she just needs to get laid."
    show player front sitting 7b at Position (xoffset=-7)
    show player_arms front sitting 4c
    show missy front sitting 3
    pause
    hide player
    hide player_shadow
    hide player_arms
    hide missy
    hide missy_arm
    with dissolve
    return

label spin_bottle_minigame_kiss_becca_missy:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show becca front sitting 1f at Position (xoffset=-4)
    show missy front sitting 1 at Position (xoffset=4)
    with dissolve
    pause
    show becca front sitting 3bf at Position (xoffset=-4)
    show missy front sitting 3 at Position (xoffset=4)
    show missy_arm front sitting 1 at Position (xoffset=4)
    with dissolve
    pause
    show becca front sitting 3f at Position (xoffset=-4)
    show missy front sitting 3b at Position (xoffset=4)
    if randomizer() < 33:
        rox "Isn't this hot, {b}[firstname]{/b}?"
        player_name "Y-yeah..."
    if randomizer() < 66:
        rox "Mmm, c'mon {b}Missy{/b}..."
        rox "You gotta be assertive with {b}Becca{/b}!"
        rox "She likes it rough!"
    else:
        becca "Mmm."
    show becca front sitting 3bf at Position (xoffset=-4)
    show missy front sitting 3 at Position (xoffset=4)
    if randomizer() < 33:
        rox "{b}Becca{/b} pretends that she doesn't like it but look how hard her nipples are!"
        player_name "..."
    if randomizer() < 66:
        player_name "..."
    else:
        rox "Oh, it sounds like {b}Missy's{/b} starting to get the hang of it!"
    show becca front sitting 3f at Position (xoffset=-4)
    show missy front sitting 3b at Position (xoffset=4)
    pause
    show becca front sitting 3bf at Position (xoffset=-4)
    show missy front sitting 3 at Position (xoffset=4)
    if randomizer() < 50:
        player_name "..."
        rox "Is this making you hard, {b}[firstname]{/b}?"
        player_name "Y-yes..."
        rox "Hehehe!"
    show becca front sitting 3f at Position (xoffset=-4)
    show missy front sitting 3b at Position (xoffset=4)
    pause
    hide missy
    hide becca
    hide missy_arm
    with dissolve
    return

label spin_bottle_minigame_kiss_roxxy_becca:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show roxxy front sitting 1 at Position (xoffset=5)
    show becca front sitting 1f
    with dissolve
    pause
    show roxxy front sitting 3 at Position (xoffset=5)
    show roxxy_arm front sitting 2d
    show becca front sitting 3bf
    if randomizer() < 33:
        becca "Ngghhh..."
    if randomizer() < 66:
        missy "Hehe, I love watching {b}Roxxy{/b} man handle {b}Becca{/b}..."
        missy "Cause she's usually such a stuck up bitch, you know?"
        player_name "Y-yeah."
        missy "... But look at her now."
        missy "Moaning like a dirty little whore."
        player_name "..."
    else:
        becca "Mmm."
    show roxxy front sitting 3b at Position (xoffset=5)
    show roxxy_arm front sitting 2c
    show becca front sitting 3f
    if randomizer() < 50:
        missy "Damn!"
        missy "Look at {b}Becca{/b} squirming!"
    else:
        missy "Doesn't {b}Roxxy{/b} taste good, {b}Becca{/b}?"
        becca "Mmmhmm..."
        missy "Hehe."
    show roxxy front sitting 3 at Position (xoffset=5)
    show roxxy_arm front sitting 2d
    show becca front sitting 3bf
    if randomizer() < 50:
        player_name "..."
        missy "{b}Roxxy{/b} really knows how to push her buttons."
    show roxxy front sitting 3b at Position (xoffset=5)
    show roxxy_arm front sitting 2c
    show becca front sitting 3f
    pause
    hide roxxy
    hide roxxy_arm
    hide becca
    with dissolve
    return

label spin_bottle_minigame_kiss_roxxy_missy:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show roxxy front sitting 1 at Position (xoffset=2)
    show missy front sitting 1f at Position (xoffset=-2)
    with dissolve
    pause
    show roxxy front sitting 3b at Position (xoffset=2)
    show missy front sitting 3f at Position (xoffset=-2)
    show missy_arm front sitting 1f at Position (xoffset=-2)
    show roxxy_arm front sitting 1 at Position (xoffset=2)
    with dissolve
    if randomizer() < 50:
        missy "Ngghhh!!!"
    show roxxy front sitting 3 at Position (xoffset=2)
    show missy front sitting 3bf at Position (xoffset=-2)
    if randomizer() < 50:
        becca "Yeah, pinch that skanks nipples!"
        becca "Hahaha!"
    else:
        becca "Mmm, this {b}Goldschwagger{/b} is so delicious!"
        becca "You sure you don't want some, {b}[firstname]{/b}?"
        player_name "Heh, nah that's alright."
        player_name "Just beer for me."
        becca "Booo!!"
    show roxxy front sitting 3b at Position (xoffset=2)
    show missy front sitting 3f at Position (xoffset=-2)
    if randomizer() < 50:
        becca "Ugh, look at {b}Missy's{/b} technique..."
        becca "... So sloppy."
        player_name "Maybe you two should practice during the week?"
        becca "We practice together all the time, she just doesn-"
        becca "!!!"
        becca "I mean..."
        becca "We don't..."
        becca "That's just the booze talking, {b}[firstname]{/b}!"
        player_name "Heh, alright."
    show roxxy front sitting 3 at Position (xoffset=2)
    show missy front sitting 3bf at Position (xoffset=-2)
    pause
    hide missy
    hide missy_arm
    hide roxxy_arm
    hide roxxy
    with dissolve
    return

label spin_bottle_minigame_last_spin:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 1 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 1 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    rox "Mmm..."
    show roxxy sitting 3
    rox "Okay, last spin."
    return

label spin_bottle_minigame_final_spin:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 1 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 1 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    rox "Mmm..."
    show roxxy sitting 3
    rox "Okay, last spin."
    rox "Winner goes to the changing room with {b}[firstname]{/b}!"
    show roxxy sitting 2
    show becca sitting 2
    show missy sitting 2
    show player_sitting 3b
    pause
    show player_sitting 3
    pause
    show player_sitting 5
    pause
    show player_sitting 11
    pause
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
