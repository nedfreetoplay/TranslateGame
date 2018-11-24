label yoga_room_mrsj_yoga_help_started:
    if M_anna.is_state(S_anna_start):
        $ M_anna.trigger(T_anna_intro)

    scene yoga_room_night
    if yoga_fail_retry:
        call expression game.dialog_select("yoga_room_mrsj_yoga_help_started_pre_repeat")
    else:

        call expression game.dialog_select("yoga_room_mrsj_yoga_help_started_pre_first")

    label anna_yoga_lesson:
        call expression game.dialog_select("yoga_room_mrsj_yoga_help_started_intro")
    $ yoga_position = ""
    $ yoga_stage = 1
    $ boner_fail = False
    $ game.timer.tick()
    label yoga_room_class:
        call expression game.dialog_select("yoga_room_class_position_pre")
    menu:
        "Happy Baby." if store._in_replay == None or yoga_stage == 2:
            $ yoga_position = "Happy Baby"
            if yoga_stage == 2:
                $ yoga_stage += 1
                call expression game.dialog_select("yoga_room_class_2nd_position_success")
                jump expression game.dialog_select("yoga_room_class")
            else:

                call expression game.dialog_select("yoga_room_class_failure")

        "Plow Position." if store._in_replay == None or yoga_stage == 3:
            $ yoga_position = "Plow Position"
            if yoga_stage == 3:
                $ yoga_stage += 1
                call expression game.dialog_select("yoga_room_class_3rd_position_success")
                call expression game.dialog_select("yoga_room_class_success")
            else:

                call expression game.dialog_select("yoga_room_class_failure")

        "Downward Dog." if store._in_replay == None or yoga_stage == 1:
            $ yoga_position = "Downward Dog"
            if yoga_stage == 1:
                $ yoga_stage += 1
                call expression game.dialog_select("yoga_room_class_1st_position_success")
                jump expression game.dialog_select("yoga_room_class")
            else:

                call expression game.dialog_select("yoga_room_class_failure")

        "End Lesson." if store._in_replay == None and mrsj.completed(mrsj_yoga_help):
            call expression game.dialog_select("yoga_room_class_end_lesson")
    $ game.main()

label yoga_room_mrsj_yoga_help_started_pre_repeat:
    show player 385 at left with dissolve
    show anna 2 at right with dissolve
    anna "Ready to try again?"
    show anna 1
    show player 386
    player_name "I think I've got the positions memorized this time."
    show player 385
    anna "Just tell me which positions to get into and I'll follow your lead."
    return

label yoga_room_mrsj_yoga_help_started_pre_first:
    show player 380 at left with dissolve
    show anna 12 at right with dissolve
    if not M_anna.is_state(S_anna_start):
        anna "Excuse me?"
    else:
        "Excuse me?"
    show player 385
    if not M_anna.is_state(S_anna_start):
        anna "Have you seen {b}Tammy{/b} around lately?"
    else:
        "Have you seen {b}Tammy{/b} around lately?"
    show anna 11
    show player 384
    player_name "Actually, she won't be able to make it tonight."
    show player 386
    player_name "She sent me to help teach her class..."
    show player 385
    show anna 12
    if not M_anna.is_state(S_anna_start):
        anna "Oh, has she told you what to do, {b}[firstname]{/b}?"
    else:
        "Oh, has she told you what to do?"
    show anna 11
    show player 386
    player_name "Well, {b}Mrs. Johnson{/b} gave me this list of instructions."
    show player 381
    player_name "I looked over them a bit... I think I can manage."
    if not M_anna.is_state(S_anna_start):
        show player 386
        player_name "She said you could maybe help me?"
        show player 385
        show anna 2 with dissolve
        anna "Of course I'll help you!"
        anna "And don't worry! You just tell me which positions and I'll follow your lead."
    else:

        show player 384
        player_name "Have you seen a girl named, {b}Anna{/b}?"
        player_name "{b}Mrs. Johnson{/b} said she'd be able to assist me."
        show player 385
        show anna 3 with dissolve
        anna "I'm {b}Anna{/b}!!"
        show anna 1
        show player 386
        player_name "Oh!!"
        show player 385
        show anna 3
        anna "I hope you know what you're doing. Ha ha!"
        show anna 2
        anna "I'll be there to help you through the moves, don't worry."
    return

label yoga_room_mrsj_yoga_help_started_intro:
    hide player
    hide anna
    scene black
    with fade
    scene yoga_front
    show anna 14
    show player 411 at left
    with dissolve
    player_name "Hmm..."
    show player 412
    player_name "Okay, we have to do three consecutive positions, in the right order..."
    show player 411
    show anna 13
    anna "Ummm... Are you ready?"
    show anna 14
    show player 414 with dissolve
    player_name "I think so?"
    show player 413
    show anna 13
    anna "Well, which pose do we start with first?"
    show anna 14
    show player 412 with dissolve
    return

label yoga_room_class_position_pre:
    if yoga_stage == 1:
        call expression game.dialog_select("yoga_room_class_1st_position_pre")

    elif yoga_stage == 2:
        call expression game.dialog_select("yoga_room_class_2nd_position_pre")

    elif yoga_stage == 3:
        $ boner_fail = True
        call expression game.dialog_select("yoga_room_class_3rd_position_pre")
    return

label yoga_room_class_1st_position_pre:
    player_name "The first position is..."
    return

label yoga_room_class_2nd_position_pre:
    player_name "Okay, for the second position, I think we should try..."
    return

label yoga_room_class_3rd_position_pre:
    player_name "The last position should follow up this one..."
    return

label yoga_room_class_failure:
    call expression game.dialog_select("yoga_room_class_failure_dialogue")
    return

label yoga_room_class_failure_dialogue:
    if boner_fail:
        show player 419 at left
        show anna 21
    else:
        show player 418 at left
    with dissolve
    player_name "Umm... I think {b}[yoga_position]{/b} is the next position."
    player_name "I'm not really sure though."
    player_name "I can't remember..."
    if boner_fail:
        show player 420
    else:
        show player 417
    show anna 13 with dissolve
    if mrsj.started(mrsj_yoga_help):
        anna "It's probably best if we just skip this class for now."
    anna "We can try again tomorrow."
    if boner_fail:
        show player 419
    else:
        show player 418
    show anna 14
    player_name "Yeah..."
    player_name "Sorry."
    if boner_fail:
        show player 420
    else:
        show player 417
    show anna 13
    if mrsj.started(mrsj_yoga_help):
        anna "Just look over {b}Tammy's{/b} notes and be sure to memorize them for the next class."
    else:
        anna "Just look over {b}Tammy's{/b} notes and be sure to memorize them for next time."
    if boner_fail:
        show player 419
    else:
        show player 418
    show anna 14
    player_name "Alright. I'll do my best..."
    hide anna
    hide player
    with dissolve
    scene yoga_room_night
    show player 24 with dissolve
    player_name "Damn... I couldn't do it."
    if mrsj.started(mrsj_yoga_help):
        player_name "I should memorize the moves and try again tomorrow."
        show player 25
        player_name "I can't let {b}Mrs. Johnson{/b} and {b}Anna{/b} down like that..."
    else:
        player_name "I should memorize the moves and try again."
    hide player with dissolve
    return

label yoga_room_class_1st_position_success:
    show player 414 with dissolve
    player_name "We need to do the {b}[yoga_position]{/b}?"
    show player 413
    show anna 15
    anna "Oh, right. I love that position!"
    show anna 18 with dissolve
    anna "Why don't I get myself on the mat and you help me stretch?"
    show anna 17
    show player 416
    player_name "Uhh... Okay."
    hide player
    show anna 19
    with dissolve
    pause
    pause
    anna "Don't hesitate to add some force to your push!"
    show anna 19_20
    pause
    show player 411 at left
    show anna 18
    with dissolve
    anna "That was good! I already feel more limber!"
    show anna 17
    show player 412
    return

label yoga_room_class_2nd_position_success:
    player_name "...the {b}[yoga_position]{/b}?"
    show player 413 with dissolve
    show anna 18
    anna "Of course!"
    anna "It's one of my favorites."
    anna "Let me get on my back so you can push on my legs to stretch..."
    show anna 21 with dissolve
    show player 416
    player_name "!!!"
    hide player
    show anna 23
    with dissolve
    player_name "Push on your legs?"
    show anna 24
    anna "Yeah!"
    anna "Just push them back so I can stretch..."
    show anna 25 with dissolve
    pause
    pause
    pause
    show anna 27 with dissolve
    anna "That felt great..."
    show anna 28
    player_name "..."
    anna "Oh!!"
    show anna 26
    player_name "Ha ha! I think we are ready for the last position!"
    return

label yoga_room_class_3rd_position_success:
    player_name "...The {b}[yoga_position]{/b}?"
    show anna 27
    anna "Perfect!"
    show player 420 at left
    show anna 29
    with dissolve
    pause
    show anna 30
    anna "All you have to do is press your... pelvis against my butt."
    show anna 29
    show player 421
    player_name "Umm... Okay..."
    hide player
    show anna 31
    with dissolve
    pause
    show anna 32
    anna "Ahh, yes!"
    hide anna
    show anna_slow 31_32
    pause
    anna "Just a bit more!!"
    hide anna_slow 31_32
    show anna_fast 31_32
    pause
    hide anna_fast 31_32
    return

label yoga_room_class_success:
    call expression game.dialog_select("yoga_room_class_success_pre")
    if store._in_replay == None:
        if mrsj.completed(mrsj_yoga_help):
            $ game.main()
        $ M_mrsj.unforce()
        $ mrsj_yoga_help.finish()
        $ mrsj.add_event(mrsj_yoga_help_2)

    call expression game.dialog_select("yoga_room_class_success_after")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Anna"]["unlocked"] = True
    $ persistent.cookie_jar["Anna"]["gallery"]["01_unlocked"] = True
    show unlock43 at truecenter with dissolve
    pause
    hide unlock43 with dissolve
    $ A_yoga_apprentice.unlock()
    return

label yoga_room_class_success_pre:
    show player 420 at left
    show anna 22
    with dissolve
    anna "That was... excellent!"
    show anna 21
    show player 419
    player_name "I... I'm sorry about..."
    show player 420
    show anna 15 with dissolve
    anna "Oh! Ha ha!"
    show anna 13
    anna "It's fine!"
    anna "That always happens to guys who come to our class!"
    show anna 16
    anna "And I didn't mind the extra... push..."
    return

label yoga_room_class_success_after:
    scene yoga_room_night
    show player 82 at left
    show anna 2 at right
    with dissolve
    anna "I'm impressed!"
    anna "You did such a great job..."
    show anna 3
    anna "...And I really enjoyed being your assistant!"
    show anna 1
    show player 83
    player_name "I was just trying to help {b}Mrs. Johnson{/b}."
    show player 79 with dissolve
    player_name "It was kinda fun."
    show player 82 at left with dissolve
    show anna 2
    anna "Hopefully, you can come by again soon to teach the class... with my help?"
    anna "That is... if you'd like to..."
    show anna 1
    show player 79 with dissolve
    player_name "That might be fun!"
    show player 82 at left with dissolve
    show anna 2
    anna "Just make sure you come at night."
    anna "It's when {b}Tammy{/b} is away and I need the help..."
    show anna 1
    show player 83
    player_name "Umm... Sure."
    hide player
    hide anna
    with dissolve
    return

label yoga_room_class_end_lesson:
    scene yoga_room_night
    if boner_fail:
        show player 82 at left
        show player 79
    else:
        show player 14 at left
    show anna 1 at right
    with dissolve
    player_name "That was fun!"
    if boner_fail:
        show player 82 at left with dissolve
    else:
        show player 13
    show anna 3
    anna "Yeah!"
    show anna 2
    anna "You sure did good this time. I'm impressed!"
    show anna 1
    if boner_fail:
        show player 79 with dissolve
    else:
        show player 14
    player_name "Thanks!"
    player_name "I was just trying to help."
    if boner_fail:
        show player 82 at left with dissolve
    else:
        show player 13
    show anna 2
    anna "I wouldn't mind doing it again with you..."
    anna "...If you'd like."
    show anna 1
    if boner_fail:
        show player 79 with dissolve
    else:
        show player 14
    player_name "Of course!"
    if boner_fail:
        show player 82 at left with dissolve
    else:
        show player 13
    show anna 2
    anna "Great! See you next time..."
    hide player
    hide anna
    with dissolve
    return

label yoga_room_strangers_only:
    scene expression game.timer.image("yoga_room{}")
    show player 12
    with dissolve
    player_name "( There's no one I know here... )"
    show player 35
    player_name "( I should come back another time, perhaps... )"
    hide player 35 with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
