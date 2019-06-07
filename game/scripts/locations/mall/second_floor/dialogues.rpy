label photo_booth_roxxy_take_picture:
    scene expression "backgrounds/location_mall_upstairs_booth.jpg"
    show roxxy_booth 1 at right
    show roxxy 1 at right
    show player 10 at left
    with dissolve
    player_name "Have you ever used this thing before?"
    show player 13
    show roxxy 2
    rox "No..."
    show roxxy 1
    rox "..."
    show roxxy 1h
    rox "How do I look?"
    show roxxy 1g
    show player 29 with dissolve
    player_name "... You look pretty."
    show player 13 with dissolve
    show roxxy 1b
    rox "I do?"
    show roxxy 1
    show player 14
    player_name "Yeah!"
    show player 26
    player_name "You always look pretty!"
    show player 13
    show roxxy 4
    rox "..."
    rox "Oh, shut up!"
    show roxxy 1h
    rox "I don't always look pretty..."
    show roxxy 1g
    show player 26
    player_name "Yeah you do."
    show player 13
    show roxxy 1h
    rox "Whatever."
    show roxxy 1g
    show player 5
    player_name "..."
    rox "..."
    show roxxy 1h
    rox "Alright, I'm getting in."
    hide roxxy_booth
    show roxxy booth 2
    with dissolve
    show player 14
    player_name "... Okay."
    show player 13
    hide roxxy
    show roxxy_booth 1 at right with dissolve
    pause
    show player 5
    player_name "..."
    show player 10
    player_name "You sure you know how to work everything?"
    show player 5
    rox "It's not rocket science!"
    rox "You just put the money in and push the button."
    show player 14
    player_name "Heh, alright."
    show player 13
    show roxxy_booth 1 with flash
    pause
    show player 9 with dissolve
    show roxxy_booth 1 with flash
    pause
    show roxxy_booth 1 with flash
    pause
    player_name "..."
    show player 10 with dissolve
    player_name "... Are you done?"
    player_name "Did you get everything you needed?"
    show player 5
    rox "I just need one more picture."
    show player 10
    player_name "... Okay."
    show player 11
    hide roxxy_booth
    show roxxy booth 2 at right
    with dissolve
    rox "Get in here!"
    hide player
    show roxxy booth 3
    player_name "!!!" with hpunch
    show roxxy booth 4
    pause
    scene expression "backgrounds/location_mall_upstairs_booth_inside.jpg"
    show roxxy booth 5 at right with dissolve
    rox "say cheese, {b}[firstname]{/b}!"
    show roxxy booth 6 with dissolve
    player_name "Whoa, whoa, whoa!!!"
    show roxxy booth 7 with dissolve
    rox "!!!" with hpunch
    show roxxy booth 7 with flash
    rox "What the fuck, {b}[firstname]{/b}!!"
    scene black with fade
    scene expression "backgrounds/location_mall_upstairs_booth.jpg"
    show roxxy_booth 1 at right
    show roxxy 1 at right
    show player 10 at left
    with dissolve
    player_name "... Sorry."
    player_name "I slipped!"
    show player 5
    show roxxy 2
    rox "... Yeah, right."
    rox "I was just trying to give you a little reward you know..."
    show roxxy 68 with dissolve
    pause
    hide player
    hide roxxy
    show roxxy_picture 1
    with dissolve
    rox "..."
    pause
    hide roxxy_picture
    show roxxy 69 at right
    show player 5 at left
    with dissolve
    rox "Hahaha!"
    show player 13
    show roxxy 72
    rox "I guess, you're getting a bigger reward than I intended..."
    show roxxy 1g
    show player 645
    with dissolve
    player_name "!!!"
    show player 646
    player_name "... Umm, thanks, I guess?"
    show player 645
    show roxxy 1h
    rox "Oh, c'mon..."
    rox "You just got a photo of your face buried my tits."
    rox "What more could a nerd like you ask for?"
    show roxxy 1g
    show player 4 with dissolve
    player_name "..."
    show roxxy 2
    rox "Just don't hurt yourself jerking off to it..."
    show roxxy 1g
    show player 10 with dissolve
    player_name "I'm not gonna... I mean, I don't-"
    show player 5
    show roxxy 2
    rox "Whatever, Perv!"
    show roxxy 3c
    rox "Don't show it to anybody either!"
    rox "If {b}Dexter{/b} finds out about that he'll kill us both!"
    show roxxy 1
    show player 14
    player_name "Yeah, yeah... I won't."
    show player 645 with dissolve
    show roxxy 1g
    rox "..."
    show roxxy 68 with dissolve
    pause
    show roxxy 72 with dissolve
    rox "Here."
    show roxxy 1b with dissolve
    rox "Think that one will work for me?"
    show roxxy 1
    show player 646
    player_name "Yeah, I think so..."
    show player 13 with dissolve
    show roxxy 1b
    rox "Good."
    rox "Gimme a call when the ID is ready."
    show roxxy 1
    show player 14
    player_name "Yeah, okay."
    show player 13
    hide roxxy with dissolve
    player_name "( ... )"
    show player 5
    player_name "( Well, that was weird. )"
    player_name "( I fell face first into {b}Roxxy's{/b} boobs and she didn't even get mad... )"
    player_name "( I should get {b}This photo to Captain Terry{/b} at {b}the pier{/b}. )"
    hide player with dissolve
    return

label photo_booth_generic_dialogue:
    scene expression player.location.background
    show player 2
    player_name "Hmm, I don't need to take any photos right now..."
    hide player
    return

label photo_booth_first_visit:
    scene expression player.location.background
    show player 2
    player_name "Hey, I've never noticed this photo-booth here before..."
    player_name "... It must be new!"
    show player 17
    player_name "Cool!"
    hide player
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
