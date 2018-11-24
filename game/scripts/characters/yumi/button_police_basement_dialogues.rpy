label yumi_police_basement_dialogue_pre:
    scene police_c_3 with None
    show yumi 2 at right
    show player 1 at left
    with dissolve
    yum "Hello, are you a visitor or are you here to post bail?"
    show yumi 1
    return

label yumi_police_basement_dialogue_donuts:
    show player 14 at left
    show yumi 1 at right
    player_name "I know you only recently started working with him..."
    show yumi 3
    player_name "... But would you happen to know what kind of donuts {b}Harold{/b} likes?"
    show player 1
    show yumi 4
    yum "Huh?"
    yum "Why do you ask?"
    show yumi 1
    show player 14
    player_name "Oh, I'm... trying to get him to like me."
    show player 1
    show yumi 2
    yum "Huh. That's... strange."
    show player 14
    show yumi 1
    player_name "I know, but I'm friends with his daughter and-"
    show player 11
    show yumi 2
    yum "You don't need to explain. I think I got the picture."
    show player 1
    yum "Well, every time we visit the donut shop... he puts {b}[harold_topping]{/b} on the top of his donuts."
    show player 14
    show yumi 1
    player_name "Really?"
    show player 1
    show yumi 2
    yum "Yeah, he always gets that topping."
    show player 17
    show yumi 1
    player_name "Okay, thanks for helping me!"
    show player 1
    show yumi 2
    yum "No problem!"
    return

label yumi_police_basement_dialogue_harold:
    show player 12
    player_name "Do you know where {b}Harold{/b} could be?"
    player_name "I need to err... return something to him!"
    show player 5
    show yumi 4
    yum "You know, I saw him just this morning!"
    yum "He looked... off... and smelled like alcohol..."
    show yumi 3
    show player 10
    player_name "Alcohol?!"
    show player 11
    show yumi 4
    yum "Yeah, but don't tell anyone!"
    yum "The poor guy's been having problems with his wife."
    yum "I just don't get it, you know? He's such a nice guy..."
    yum "...I think he deserves better, that's for sure!"
    show yumi 3
    show player 12
    player_name "You don't know where he went after this morning do you?"
    show player 5
    show yumi 4
    yum "Hmm... I'm not sure, but he took his car."
    show yumi 3
    show player 35
    player_name "So he went for a drive somewhere..."
    show player 14
    player_name "...Alright, thanks!"
    hide player
    hide yumi
    with dissolve
    return

label yumi_police_basement_dialogue_leave:
    show player 14 at left
    show yumi 1 at right
    player_name "I'm just here to visit someone."
    show yumi 2
    show player 1
    yum "Sure. Make sure you leave your backpack in the bin, and stay behind the line."
    yum "There's no touching allowed."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
