label ronda_pool_dialogue_pre_cassie_fun:
    show ronda b_swim a_swim_sides f_normal at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ron "..."
    show ronda f_normal_talk
    ron "What are you even doing here?"
    show ronda f_normal
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "Just getting some exercise!"
    player_name "I figured I had to start somewhere, and it can help me get ready for the qualifiers!"
    show ronda f_normal_talk
    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ron "Look: I ain't helping you, let alone go in the water at the same time as you... So forget it, okay?"
    show ronda f_normal
    if wearing_swimsuit:
        show player 53
    else:
        show player 26
    player_name "That's fine!"
    player_name "I can manage on my own..."
    show ronda f_rolleyes
    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ron "Ugh... Whateva."
    return

label ronda_pool_dialogue_after_cassie_fun:
    show ronda b_swim a_swim_sides f_upset_talk at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ron "Here to pay {b}Cassie{/b} a little visit?"
    show ronda f_upset
    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Uhh... I'm just here to swim?"
    show ronda f_upset_talk
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ron "You can stop pretending..."
    ron "...You ain't here to train, like I am."
    show ronda f_upset
    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Uhh... okay?"
    show ronda f_upset_angry
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ron "Ugh... you're pathetic."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
