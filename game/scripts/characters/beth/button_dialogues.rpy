label beth_dialogue_pre:
    scene donut_c
    show beth 2 zorder 1 at right
    show xtra 27 zorder 2 at center
    show player 1 zorder 3 at left
    with dissolve
    beth "Howdy, mister!"
    show player 14
    show beth 1
    player_name "Hi."
    show player 1
    show beth 2
    beth "Looking to buy some sweet holes, are ya?"
    show beth 1
    return

label beth_dialogue_do_not_know:
    show player 14
    player_name "Hmm... I'm not sure what I need to buy yet."
    show player 1
    show beth 2
    beth "You don't know?"
    show player 14
    show beth 1
    player_name "Well, I'm buying these for someone as a gift but I'm not sure what he likes."
    show player 1
    show beth 2
    beth "I can't help ya if you don't know what ya'd like!"
    show player 14
    show beth 1
    player_name "I'll come back later when I know the toppings."
    return

label beth_dialogue_want_donuts:
    show player 14
    player_name "I'd like to buy a small box, please."
    show player 1
    show beth 2
    beth "Sure thing!"
    beth "What kind of glaze and topping would you like on them?"
    return

label beth_dialogue_leave:
    show player 14
    player_name "I'm fine, thanks!"
    player_name "Perhaps another time..."
    show player 1
    show beth 2
    beth "Sure thing, see ya!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
