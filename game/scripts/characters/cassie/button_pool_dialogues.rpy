label cassie_pool_dialogue_rules:
    scene location_pool_closeup1
    show cassie 2 at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    cas "Can I help you with something?"
    show cassie 4
    if wearing_swimsuit:
        show player 45
    else:
        show player 108f
    player_name "Umm... What are the {b}rules{/b} again?"
    if wearing_swimsuit:
        show player 53f
    else:
        show player 1
    show cassie 2
    cas "Well, you can't swim in your clothes..."
    show cassie 3
    cas "You have to use one of the {b}changing rooms{/b} to put on a {b}swimsuit{/b}!"
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    show cassie 4
    player_name "Oh. Great! Thanks!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
