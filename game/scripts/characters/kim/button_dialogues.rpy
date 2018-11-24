label kim_button_dialogue_intro:
    show player 13 at left
    show kim 2 at right
    with dissolve
    kim "Herro there!"
    kim "What can I do to get you into a new vehicle today?"
    show kim 1
    show player 10
    player_name "Oh, uhh..."
    show player 4 with dissolve
    return

label kim_button_dialogue_button:
    show player 14 with dissolve
    player_name "I like your button."
    player_name "You a fan of {b}Mayor Rump{/b}?"
    show player 13
    show kim 2
    kim "Oh, {b}Mayor Rump{/b} is numba 1, best mayor."
    kim "Him and {b}Kim{/b} good friends!"
    show kim 3
    show player 10
    player_name "You're friends with {b}Mayor Rump{/b}?"
    show player 13
    show kim 2
    kim "Yes, I herp him with his poricies in exchange for funding."
    show kim 6 with dissolve
    kim "When I ascend to my throne!"
    show kim 3 with dissolve
    show player 10
    player_name "... Throne?"
    show player 5
    show kim 2
    kim "Yes!"
    kim "When I take over this dearership, I will erect a mighty throne."
    show kim 5 with dissolve
    kim "Hue hue hue hue!"
    show player 12
    player_name "Well, good luck with all that..."
    show player 5
    show kim 2 with dissolve
    kim "I no need ruck..."
    hide kim with dissolve
    show player 10
    player_name "Hmm, why would our {b}Mayor{/b} be hanging out with that guy?"
    show player 12
    player_name "... Weird."
    hide player with dissolve
    return

label kim_button_dialogue_browsing:
    show player 14 with dissolve
    player_name "I'm just here to browse."
    show player 13
    show kim 2
    kim "Hmmph, a browser, eh?"
    kim "Very well."
    kim "... But should you wish to purchase something, I insist you speak with me and no one erse!"
    kim "You understand?!"
    show kim 1
    show player 10
    player_name "Uhh, yeah..."
    player_name "Sure thing."
    show player 5
    show kim 2
    kim "Good."
    kim "I will be watching!"
    hide kim
    hide player
    with dissolve
    return

label kim_button_dialogue_sign:
    show player 14 with dissolve
    player_name "Is that you on the sign?"
    show player 13
    show kim 5 with dissolve
    kim "Oh, you notice sign, eh?!"
    kim "Yes, {b}Kim{/b} is numba 1, best car salesman!"
    kim "Soon, I own this prace."
    show kim 4
    show player 12
    player_name "Oh yeah?"
    show player 13
    show kim 6 with dissolve
    kim "Oh yes... I will conquer this Car Dearership!"
    kim "I will expand it, into national chain!"
    show player 11
    kim "One day, I will cover the entire pranet with my Dearerships!!"
    show kim 3
    show player 3
    with dissolve
    player_name "..."
    show kim 5 with dissolve
    kim "Hue hue hue hue!"
    kim "I will be a dearership GOD!!!"
    show kim 4
    show player 10 with dissolve
    player_name "... Right."
    player_name "Well, I'm gonna go look around now..."
    show player 5
    show kim 2 with dissolve
    kim "Yes, you go rook."
    kim "Come find me if you want make purchase."
    hide kim with dissolve
    show player 12
    player_name "What an odd fellow."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
