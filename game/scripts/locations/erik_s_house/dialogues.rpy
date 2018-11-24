label erikshouse_erik_intro_known:
    scene erikhouse
    show player 2 at left with dissolve
    show erik 1 at right with dissolve
    player_name "Hey, {b}Erik{/b}!"
    show erik 5 at right
    show player 1 at left
    eri "Hey, {b}[firstname]{/b} ..."
    show player 10 at left
    show erik 1 at right
    player_name "You look really tired... You alright?"
    show erik 3 at right
    show player 5 at left
    eri "Well, I was on the computer all night playing this new game that came out..."
    show erik 2 at right
    show player 5 at left
    eri "...and I just hate going to school."
    show erik 3 at right
    eri "I wish I could just stay at home all the time."
    show player 10 at left
    show erik 1 at right
    player_name "Yeah, I hear ya..."
    show erik 3 at right
    show player 24 at left
    eri "Sorry to hear about your {b}Dad{/b}, by the way. How are you holding up?"
    show player 25 at left
    show erik 1 at right
    player_name "I'll be alright, man. Thanks for asking!"
    player_name "We should really get going before we're late for class."
    hide player 25 at left with dissolve
    hide erik 1 at right with dissolve
    return

label erikshouse_erik_intro_started:
    scene erikhouse
    show player 11 at left
    show erik 5 at right
    eri "Shouldn't we be going to {b}school{/b}?"
    show erik 1 at right
    show player 14 at left
    player_name "Oh, Yeah. You're right..."
    hide player 14 at left
    hide erik 1 at right
    hide erikhouse
    return

label erikshouse_erik_intro_over:
    scene erikhouse
    show player 12 with dissolve
    player_name "( There's no one here... )"
    show player 35
    player_name "( {b}Erik{/b} probably left for {b}school{/b} already. )"
    hide player 35 with dissolve
    hide erikhouse
    return

label erikshouse_erik_intro_over_weekend:
    scene erikhouse
    show player 12 with dissolve
    player_name "( There's no one here... )"
    show player 35
    player_name "( {b}Erik{/b} probably is playing videogames or shopping for some at the {b}mall{/b}. )"
    hide player 35 with dissolve
    hide erikhouse
    return

label mrs_j_intro:
    scene erikhouse
    show player 1 at left with dissolve
    show mrsj 2 at right with dissolve
    mrsjo "Hi, {b}[firstname]{/b}!"
    show mrsj 1 at right
    show player 14 at left
    player_name "{b}Mrs. Johnson{/b}! Just dropping by to see {b}Erik{/b}!"
    show mrsj 4 at right
    show player 1 at left
    eri "Hey, {b}[firstname]{/b}!"
    show mrsj 5 at right
    show player 11 at left
    mrsjo "There's my little pumpkin!"
    show mrsj 6 at right
    eri "C'mon, {b}Mrs. Johnson{/b}. I told you not to call me that..."
    show mrsj 7 at right
    show player 5 at left
    mrsjo "By the way, {b}Erik{/b} told me about your father..."
    mrsjo "I'm so sorry to hear. Let us know if you ever need anything, okay?"
    show mrsj 8 at right
    show player 10 at left
    player_name "Thanks, {b}Mrs. Johnson{/b}."
    show mrsj 7 at right
    show player 13 at left
    mrsjo "Okay, I'd best get to my Yoga class. You two behave yourselves!"
    show mrsj 8 at right
    show player 1 at left
    mrsjo "Try and get {b}Erik{/b} out of the house for a change!"
    mrsjo "It would be good for him to get some sun!"
    mrsjo "Good luck!"
    show mrsj 6 at right
    eri "Yeah, right."
    hide mrsj 6 at right with dissolve
    show erik 1 at right with dissolve
    show player 14 at left
    player_name "Dude, she is so fit! You're so lucky she's letting you rent a room!"
    show erik 3 at right
    show player 1 at left
    eri "Um... Yeah... I guess..."
    show erik 1 at right
    show player 26 at left
    player_name "C'mon, man. Admit it. For her age, she's in {i}REALLY{/i} good shape!" with hpunch
    show erik 5 at right
    show player 1 at left
    eri "Well she does hang out at the {b}Gym{/b} a lot."
    eri "They've got her teaching a yoga class now."
    show erik 1 at right
    show player 14 at left
    player_name "So, you want to hangout... or?"
    show erik 3 at right
    show player 11 at left
    eri "I can't right now. I have... I downloaded this new game and-"
    show erik 1 at right
    show player 12 at left
    player_name "It's fine, {b}Erik{/b}. I'll see you tomorrow or something."
    show player 36 at left
    show erik 7 at right
    eri "Cool. See ya later..."
    hide player 36 at left with dissolve
    hide erik 7 at right with dissolve
    hide erikhouse
    return

label door18_locked_dialogue:
    if player.location == L_erikhouse:
        scene erikhouse
    elif player.location == L_erikhouse_backyard:
        scene eriks_backyard_b
    show player 11 at left
    show erik 5 at right
    eri "Umm... Why are we going in my house?"
    eri "Shouldn't we be going to {b}school{/b}?"
    show erik 1 at right
    show player 14 at left
    player_name "Oh, yeah! You're right..."
    hide player 14 at left
    hide erik 1 at right
    $ game.main()

label erik_gf_stolen:
    if player.location == L_erikhouse:
        scene expression game.timer.image("erikhouse{}")
    elif player.location == L_erikhouse_backyard:
        scene expression game.timer.image("eriks_backyard{}_b")
    show player 10
    with dissolve
    player_name "I shouldn't make this any more awkward..."
    player_name "I'll wait until tomorrow to talk to them."
    hide player
    with dissolve
    $ game.main()

label erik_thief_block:
    scene erikhouse_night
    show player 2 with dissolve
    player_name "I should go catch that {b}burglar{/b} first."
    hide player 2 with dissolve
    $ game.main()

label closed_erik:
    if not game.timer.is_dark():
        if player.location == L_erikhouse:
            scene erikhouse
        elif player.location == L_erikhouse_backyard:
            scene eriks_backyard_b
        show player 12 with dissolve
        player_name "( There's no one here... )"
        show player 35
        player_name "{b}Erik{/b} probably left for {b}school{/b} already."
    else:

        if player.location == L_erikhouse:
            scene erikhouse_night
        elif player.location == L_erikhouse_backyard:
            scene eriks_backyard_night_b
        show player 2 with dissolve
        player_name "( {b}Erik{/b} is probably asleep. I should come back tomorrow. )"
        hide player 2 with dissolve
    $ game.main()

label closed_erik_weekend:
    if player.location == L_erikhouse:
        scene erikhouse
    elif player.location == L_erikhouse_backyard:
        scene eriks_backyard_b
    show player 12 with dissolve
    player_name "( There's no one here. )"
    show player 35
    player_name "( {b}Erik{/b} probably went out with {b}Mrs. Johnson{/b} somewhere. )"
    hide player 35 with dissolve
    $ game.main()

label erik_mailbox:
    scene expression game.timer.image("erik_mailbox{}")
    if game.mail["erik"] == "m_magazine":
        show expression "objects/object_mailbox_item01_closeup.png" with dissolve
        player_name "( Huh. A magazine. I wonder who it could be for... )"
        player_name "( Milfness? Well, I know it's for {b}Mrs. Johnson{/b}. I didn't know she subscribed to these, though... )"
        player_name "( I'd better put this back. )"
        hide expression "objects/object_mailbox_item01_closeup.png" with dissolve

    elif game.mail["erik"] == "m_dad_letter":
        player_name "( I didn't know they received letters. I wonder who it's addressed to... )"
        player_name "( It's for {b}Erik{/b}. )"
        menu:
            "Leave it alone.":
                call screen erik_mailbox
            "Open it.":

                show mailbox_letter at Position(xpos = 565, ypos = 768) with dissolve
                player_name "( A letter from D?! )"
                player_name "I'd better put this back."
                hide mailbox_letter with dissolve
                call screen erik_mailbox

    elif game.mail["erik"] == "m_pizza_pamphlet":
        player_name "( This looks like junk mail. )"
        show expression "objects/object_mailbox_item02_closeup.png" with dissolve
        player_name "( {b}Tony's Pizza{/b}. I haven't been to that place in a while. )"
        player_name "( I'd better put this back. )"
        hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
        $ L_pizzeria_exterior.unlock()
        $ L_dealership_front.unlock()

    elif game.mail["erik"] == "m_newspaper":
        player_name "( Local news. This should be interesting... )"
        show expression "objects/object_newspaper.png" with dissolve
        player_name "( The thief is still on the loose? You would've thought they would've caught him by now. )"
        player_name "( I'd better put this back. )"
        hide expression "objects/object_newspaper.png" with dissolve
    call screen erik_mailbox
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
