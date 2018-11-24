label button_ross_paint_with_body:
    scene location_school_art_closeup
    show ross 1 at left
    show player 2f at right
    with dissolve
    player_name "You said you had one final technique to teach me?"
    show ross 2
    show player 1f
    ross "Oh yes! It's a good one too!"
    ross "I can't teach you here though. You'll have to come see me in {b}my office{/b} this {b}evening{/b}."
    show ross 1
    show player 2f
    player_name "It sounds really awesome!"
    player_name "I'll see you there, {b}Miss Ross{/b}."
    return

label button_ross_end_intro:
    scene location_school_art_closeup
    show player 1f at right
    show ross 2 at left
    with dissolve
    ross "There's my little hero!"
    show player 2f
    show ross 1
    player_name "Heh, hey {b}Miss Ross{/b}."
    show player 1f
    show ross 13 with dissolve
    ross "Are you busy {b}tonight{/b}?"
    ross "I was hoping you might be interested in some more... \"Private Lessons\"?"
    ross "I'm just aching to teach you more..."
    show ross 12
    return

label button_ross_end_yes:
    show player 2f
    player_name "Sure, that sounds awesome!"
    show player 1f
    show ross 11
    ross "Wonderful!"
    ross "Just come {b}visit me in my office{/b} later today."
    show ross 10
    show player 2f
    player_name "I can't wait!"
    show player 1f
    show ross 11
    ross "Now, is there anything else I can help you with?"
    show ross 10
    return

label button_ross_end_no:
    show player 10f
    player_name "Oh, I can't tonight, {b}Miss Ross{/b}..."
    player_name "... I have other plans."
    show player 11f
    show ross 25
    ross "Aww, that's too bad."
    ross "... Just let me know if anything changes."
    show ross 11
    ross "I'll always make time for you, {b}[firstname]{/b}"
    show player 1f
    ross "Now, is there anything else I can help you with?"
    show ross 10
    return

label button_ross_get_paint_grace_reminder:
    scene location_school_art_closeup
    show player 2f at right
    show ross 10 at left
    player_name "... Who was I supposed to {b}ask about the paint{/b} again?"
    show player 1f
    show ross 11
    ross "Start with {b}Eve{/b}."
    ross "If we're lucky she might have some extra paint at home that we can use."
    show player 2f
    show ross 10
    player_name "Alright, I'll go and ask her."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
