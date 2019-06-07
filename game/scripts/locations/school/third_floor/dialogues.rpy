label okita_office_door:
    $ player.go_to(L_school_floor3)
    if M_okita.is_set("office locked"):
        if player.has_item("keycode_note"):
            call screen okita_keypad
        else:

            call expression game.dialog_select("okita_office_door_need_keycode")
    else:

        if M_okita.is_state(S_okita_tired_from_belt):
            call expression game.dialog_select("okita_office_door_okita_tired")
        else:

            jump expression game.dialog_select("mrs_okitas_office_dialogue")
    $ game.main()

label okita_office_door_need_keycode:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10
    with dissolve
    player_name "Hmm, I guess {b}Miss Okita{/b} keeps her office locked when she's not inside?"
    player_name "It's got one of those automated keypad locks too."
    show player 11
    pause
    show player 10
    player_name "I'm definitely not getting in there without a {b}keycode{/b}."
    return

label okita_office_door_okita_tired:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10
    with dissolve
    player_name "I should let her rest for now."
    return

label okita_office_unlock:
    $ M_okita.set("office locked", False)
    jump expression game.dialog_select("mrs_okitas_office_dialogue")

label okita_office_locked:
    $ player.go_to(L_school_floor3)
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10
    with dissolve
    player_name "Oops! That wasn't the right code..."
    show player 34
    player_name "Hmm, I'd better double check that {b}keycode{/b} I got out of {b}Principal Smith's{/b} desk before trying again."
    $ game.main()

label third_floor_okita_get_ingredients:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10 with dissolve
    player_name "Hmm, I need to get into {b}Principal Smith's{/b} office again to look for some kind of DNA sample..."
    player_name "I should go in when she's not there."
    return

label annie_enter_office_dialogue:
    $ player.go_to(L_school_floor3)
    if not M_okita.is_set("talked to annie"):
        call expression game.dialog_select("smith_office_annie_guarding")
        $ M_okita.set("talked to annie", True)
    else:

        call expression game.dialog_select("smith_office_annie_guarding_repeat")
        if player.has_required_chr(7):
            call expression game.dialog_select("smith_office_annie_guarding_distract_pass")
            $ player.go_to(L_school_smithoffice)
            $ game.main()
        else:

            call expression game.dialog_select("smith_office_annie_guarding_distract_fail")
    $ game.main()

label smith_office_annie_guarding_distract_pass:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 2 at left
    show annie 1 at right
    player_name "I just overheard your thief bragging downstairs near the boys locker room..."
    show player 1
    show annie 3
    ann "What? Really!?"
    show player 2
    show annie 1
    player_name "Yup and if you hurry you might still catch him..."
    show player 1
    show annie 3
    ann "Principal Smith will definitely reward me for that!"
    ann "Would you mind watching this door for me?"
    show player 2
    show annie 1
    player_name "Not at all. Go get him!"
    hide annie
    hide player
    show player 1f
    show annie 16 at left
    with dissolve
    ann "Ahahahahaah!"
    hide annie with dissolve

    show player 2f
    player_name "Well that should keep her busy for awhile..."
    player_name "Now I search the office for something with {b}Principal Smith's DNA{/b} on it."
    return

label smith_office_annie_guarding_distract_fail:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10 at left
    show annie 1 at right
    player_name "[chr_warn]O-okay..."
    player_name "[chr_warn]... I was just looking for {b}Principal Smith{/b}."
    show player 11
    show annie 3
    ann "[chr_warn]Yeah, well she isn't here."
    show annie 4
    ann "[chr_warn]So beat it!"
    show player 12
    show annie 1
    player_name "[chr_warn]Alright, sheesh! You don't have to get your panties in a bunch!"
    return

label smith_office_annie_guarding_repeat:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 11 at left
    show annie 3 at right
    with dissolve
    ann "Nobody is getting past me, {b}[firstname]{/b}!"
    return

label smith_office_annie_guarding:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10 at left
    show annie 1 at right
    with dissolve
    player_name "Annie, what are you doing here?"
    show player 11
    show annie 3
    ann "I'm {b}guarding {b}Principal Smith's{/b} office{/b} while she's away."
    show player 10
    show annie 1
    player_name "... Why?"
    show player 11
    show annie 3
    ann "Umm, because she asked me too? Duh."
    show annie 1
    player_name "..."
    show annie 3
    ann "She said someone keeps sneaking in and going through her stuff."
    show annie 5
    ann "You wouldn't happen to know anything about that, would you?!"
    show player 10
    show annie 6
    player_name "M-me? No, I don't know anything about that!"
    show player 11
    show annie 5
    ann "Uh huh..."
    show annie 3
    ann "Well whoever it is, {b}they aren't getting past me!{/b}"
    show player 10
    player_name "Okay, well good luck with that..."
    hide annie with dissolve
    hide player
    show player 5 with dissolve
    player_name "( I have to figure out into that office... )"
    show player 34
    player_name "( Perhaps I can {b}trick her{/b} somehow? )"
    return

label third_floor_roxxy_intro:
    scene expression game.timer.image("school_hall_third_floor{}_b")
    show player 30 with dissolve
    player_name "( ... )"
    player_name "( It looks like {b}Roxxy{/b} is arguing with some of the teachers... )"
    show player 33
    player_name "( I should take a closer look! )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
