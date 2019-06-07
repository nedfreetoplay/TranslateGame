label kevin_gym_take_it_easy:
    show player 14
    player_name "I'm gonna get out of here man."
    show player 13
    show kevin 11b with dissolve
    kev "Already, bro?"
    show kevin 11c
    show player 14
    player_name "Yeah, I've got some other stuff I need to do."
    show player 13
    show kevin 9 with dissolve
    kev "Ah, alright."
    show kevin 8
    show player 14
    player_name "Catch you later, {b}Kevin{/b}."
    hide kevin
    hide player
    with dissolve
    return

label kevin_gym_lets_lift:
    show player 14
    player_name "Let's just lift."
    show player 13
    show kevin 9
    kev "Oh, you're ready to pump some iron?"
    show kevin 10 with dissolve
    kev "Right on, bro."
    kev "Let's do this!"
    hide kevin
    hide player
    with dissolve
    return

label kevin_gym_intro:
    scene expression player.location.background_blur with None
    show player 13 at left
    show kevin 9 at right
    with dissolve
    kev "Hey, bro!"
    show kevin 8
    show player 14
    player_name "What's up, {b}Kevin{/b}?"
    show player 13
    show kevin 9
    kev "I've been working on my glutes all morning!"
    show kevin 13b with dissolve
    kev "Feel how tight these bad boys are!"
    show player 10b with dissolve
    player_name "Eh, no thanks..."
    show player 5b
    kev "You sure, bro?"
    kev "You don't know what you're missing!"
    show kevin 8 with dissolve
    show player 29 with dissolve
    player_name "Heh."
    show player 5 with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
