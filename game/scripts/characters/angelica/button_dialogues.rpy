label angelica_dialogue_ross_get_linens_pre:
    scene church_c
    show player 1 at left
    show ang 1 at right
    with dissolve
    return

label angelica_dialogue_ross_get_linens:
    show player 2
    player_name "Umm, I'm doing an art project for school and we need some white linens."
    player_name "My friend {b}Mia{/b} said you might be willing to spare some."
    show player 1
    show ang 2
    ang "Hmm, {b}Mia{/b} sent you?"
    ang "She's such a devout young woman."
    ang "I suppose I could give you some of our old Baptismal Robes. They're fraying anyways..."
    show player 2
    show ang 1
    player_name "That should work just fine! Thank you so very much."
    show player 1
    show ang 2
    ang "If you want to thank me, start showing up for service on Sundays."
    show player 11
    show ang 1
    player_name "..."
    show ang 2
    ang "Now wait here while I go and get them."
    hide ang
    with dissolve
    show player 10
    player_name "Huh, well that was easy."
    show player 11
    player_name "..."
    show player 10
    player_name "I thought for sure she'd want something in return..."
    show player 11
    pause
    show ang 40 at right with dissolve
    pause
    show ang 41
    ang "Here ya go."
    show ang 2
    show player 592
    with dissolve
    ang "Tell {b}Mia{/b} I expect to see her early for next service! She's long past due for confession."
    show player 593
    show ang 1
    player_name "O-okay, I'll let her know."
    show player 592
    ang "Hmm!"
    hide ang
    hide player
    show player 591 at Position (xpos=0.25, ypos=1.0)
    with dissolve
    player_name "... {b}Mia{/b} might end up fronting the bill on this one."
    player_name "I'd better get these {b}Linens{/b} back to {b}Miss Ross{/b}."
    return

label angelica_dialogue_change_pre:
    scene church_c with fade
    show player 10 at left
    show ang 1 at right
    with dissolve
    player_name "Hi, {b}Sister Angelica{/b}."
    show player 5
    show ang 2
    ang "You, again."
    ang "What do you want?"
    show ang 1
    return

label angelica_dialogue_change_talk:
    show player 10
    player_name "I just want to talk."
    show player 5
    show ang 2
    ang "Quiet."
    show ang 1
    show player 24
    player_name "Oh..."
    show ang 2
    ang "If you want to talk, come visit me at night in my chambers..."
    show ang 1
    show player 25
    player_name "Okay, then. Sorry."
    hide player
    hide ang
    with dissolve
    return

label angelica_dialogue_change_graveyard:
    show player 10
    player_name "How do you access the graveyard?"
    show player 5
    show ang 2
    ang "It is off limits."
    ang "Although, it is locked and still pesky kids keep finding ways to {b}sneak through the fence{/b}."
    show ang 1
    show player 12
    player_name "But my dad is buried in there."
    show player 5
    ang "..."
    show ang 2
    ang "I'm sure he is."
    show ang 1
    show player 12
    player_name "But-"
    show player 16
    show ang 2
    ang "Begone. You are wasting my time."
    hide ang
    hide player
    show player 16
    with dissolve
    player_name "..."
    show player 12
    player_name "Maybe I can find {b}a way through the fence{/b} too."
    hide player with dissolve
    return

label angelica_dialogue_change_leave:
    show player 10
    player_name "Nevermind. I have to go."
    show player 5
    ang "..."
    show ang 2
    ang "Don't waste my time like that again."
    show ang 1
    show player 25
    player_name "You're right, I'm sorry..."
    hide player
    hide ang
    with dissolve
    return

label angelica_dialogue_pre:
    scene church_c
    show ang 2 at right
    show player 1 at left
    with dissolve
    ang "Are you from this Parish, young man?"
    show ang 1
    show player 14
    player_name "Hi, I was wo-"
    show ang 2
    show player 11
    ang "Are you from this Parish, young man?"
    show ang 1
    show player 14
    player_name "Uhh... Not really."
    show ang 2
    show player 11
    ang "Do you believe in God?"
    show ang 1
    show player 10
    player_name "Well..."
    show ang 2
    show player 11
    ang "I'm sorry."
    ang "I can only help those who share the faith of our lord!"
    hide player
    hide ang
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
