label spin_bottle_minigame_mc:
    if M_roxxy.get("roxxy locker sex"):
        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_roxxy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_missy")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_becca")
            call expression game.dialog_select("spin_bottle_minigame_final_spin")

        elif M_player.get("beach bottle spins") == 4:
            if not M_player.get("mc beach sex"):
                call expression game.dialog_select("spin_bottle_minigame_mc_4some_intro_pre_first")
            else:
                call expression game.dialog_select("spin_bottle_minigame_mc_4some_intro_pre_repeat")
            $ anim_toggle = True
            $ animated = False
            $ M_roxxy.set("sex speed", .09)
            $ M_missy.set("sex speed", .09)
            $ M_becca.set("sex speed", .09)
            $ M_player.set("left of 4some", M_becca)
            call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_roxxy")
            call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=M_roxxy)
    else:

        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_roxxy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_missy")
            call expression game.dialog_select("spin_bottle_minigame_last_spin")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_becca")
            $ game.timer.tick()
            $ game.main()
    call screen spin_bottle_minigame

label beach_mc_4some_roxxy_replay:
    call expression game.dialog_select("beach_mc_4some_dialogue_replay")
    $ M_player.set("left of 4some", M_becca)
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_roxxy")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=M_roxxy)

label beach_mc_4some_missy_replay:
    call expression game.dialog_select("beach_mc_4some_dialogue_replay")
    $ M_player.set("left of 4some", M_roxxy)
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_missy")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=M_missy)

label beach_mc_4some_becca_replay:
    call expression game.dialog_select("beach_mc_4some_dialogue_replay")
    $ M_player.set("left of 4some", M_missy)
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_becca")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=M_becca)

label beach_mc_4some_dialogue_replay:
    call expression game.dialog_select("beach_mc_4some_dialogue_replay_intro")
    call expression game.dialog_select("button_roxxy_beach_spin_bottle")
    call expression game.dialog_select("button_roxxy_beach_spin_bottle_sex_repeat")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_intro_pre_repeat")
    $ anim_toggle = True
    $ animated = False
    $ M_roxxy.set("sex speed", .09)
    $ M_missy.set("sex speed", .09)
    $ M_becca.set("sex speed", .09)
    return

label beach_mc_4some_dialogue_replay_intro:
    scene expression game.timer.image("backgrounds/location_beach_water{}_blur.jpg")
    show player 13f at right
    show becca bikini 9 at Position (xpos=315)
    show missy bikini 2 at left
    show roxxy bikini 1f at Position (xpos=500)
    with dissolve
    return

label spin_bottle_minigame_mc_4some_intro_pre_first:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 8b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 6b at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "Whoa, wait a second..."
    missy "What happens now?"
    show missy sitting 6
    show becca sitting 8c
    becca "Yeah, I never even thought about it landing on {b}[firstname]{/b}..."
    show becca sitting 8b
    show player_sitting 3b
    show roxxy sitting 3
    rox "Oh, well this means {b}[firstname]{/b} wins."
    show roxxy sitting 2
    show becca sitting 7
    becca "Huh?"
    show becca sitting 8
    show player_sitting 3
    show missy sitting 3
    missy "So what, he is taking himself to the changing room for a special reward?"
    show missy sitting 2
    show becca sitting 5
    show roxxy sitting 5
    rox "Hahaha, nope."
    show roxxy sitting 3
    show player_sitting 3b
    rox "This means we're all going!"
    show roxxy sitting 2
    show player_sitting 5
    show becca sitting 8b
    becca "!!!"
    show missy sitting 6b
    missy "Seriously?!"
    show missy sitting 6
    show roxxy sitting 3
    rox "Yup!"
    show roxxy sitting 2
    show becca sitting 9
    becca "..."
    show missy sitting 5
    missy "AWESOME!"
    player_name "..."
    show player_sitting 3b
    show roxxy sitting 3
    rox "You're going to love this, {b}[firstname]{/b}."
    show roxxy sitting 2
    show player_sitting 3
    show becca sitting 8
    show missy sitting 3
    missy "Look how nervous {b}Becca{/b} is!!"
    show missy sitting 5
    show becca sitting 8b
    missy "Hahaha!"
    show becca sitting 8
    show roxxy sitting 5
    rox "Hahaha!"
    show becca sitting 7b
    becca "Shut up, skanks!"
    hide becca
    hide missy
    hide roxxy
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show becca bikini 20 at right
    show roxxy bikini 27 at Position (xpos=400)
    with dissolve
    rox "Are you ready for this, {b}[firstname]{/b}?"
    hide roxxy
    hide becca
    with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 10 at left
    show roxxy bikini 5 at right
    show becca bikini 1 at Position (xpos=575)
    show missy bikini 1 at Position (xpos=375)
    with dissolve
    player_name "So are we going to-"
    show roxxy bikini 6 with dissolve
    show player 428
    player_name "!!!"
    show roxxy bikini 7 with dissolve
    pause .15
    show roxxy bikini 8 with dissolve
    pause .15
    show player 426
    show roxxy bikini 9 with dissolve
    pause .15
    show roxxy bikini usa 5 with dissolve
    pause .15
    show roxxy 22 with dissolve
    pause .15
    show roxxy 24 with dissolve
    rox "C'mon girls, time's wasting!"
    show roxxy 23
    show becca bikini 13
    show missy bikini 3 with dissolve
    pause .25
    show becca bikini 16
    show missy bikini 4 with dissolve
    pause .25
    show becca bikini 3
    show missy bikini 4b
    with dissolve
    pause .2
    show becca bikini 4
    show missy bikini 5
    with dissolve
    pause .15
    show becca bikini 5
    show missy bikini 7b
    with dissolve
    pause .15
    show becca bikini 5b
    show missy naked 1
    with dissolve
    pause .15
    show becca naked 1 with dissolve
    show player 427
    player_name "Okay, not that I'm complaining or anything..."
    show player 12
    player_name "... But what exactly is going on?!"
    show player 5
    show roxxy 24
    rox "We're going to be sharing you tonight."
    show roxxy 23
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "{b}*Gulp*{/b} Y-you mean-"
    show player 5
    show roxxy 24
    rox "That's right!"
    rox "Get undressed, {b}[firstname]{/b}."
    show roxxy 23
    player_name "..."
    show player 10
    player_name "Okay..."
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player 430 with dissolve
    pause
    hide player
    hide becca
    hide missy
    show roxxy 109 at center
    with dissolve
    rox "I'll start us off..."
    pause
    show roxxy 109c
    rox "Wanna make sure you all remember who's the {b}Alpha Bitch{/b} here!"
    hide roxxy with dissolve
    return

label spin_bottle_minigame_mc_4some_intro_pre_repeat:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 5 zorder 1 at right
    show becca sitting 8b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 6 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    rox "{b}[firstname]{/b} wins!"
    show player_sitting 3
    show roxxy sitting 2
    show missy sitting 2
    show becca sitting 3
    becca "That means we all go, right?"
    show becca sitting 2
    show roxxy sitting 3
    rox "That's right."
    show roxxy sitting 2
    show becca sitting 9
    show missy sitting 5
    missy "Yes!!!"
    player_name "..."
    show missy sitting 2
    show roxxy sitting 3
    show player_sitting 3b
    rox "You're going to love this, {b}[firstname]{/b}."
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 3
    missy "Look how nervous {b}Becca{/b} is!!"
    show missy sitting 5
    show becca sitting 8b
    missy "Hahaha!"
    show becca sitting 8
    show roxxy sitting 5
    rox "Hahaha!"
    show becca sitting 7b
    becca "Shut up, skanks!"
    hide roxxy
    hide missy
    hide becca
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show becca bikini 20 at right
    show roxxy bikini 27 at Position (xpos=400)
    with dissolve
    rox "Are you ready for this, {b}[firstname]{/b}?"
    hide roxxy
    hide becca
    with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show roxxy bikini 5 at right
    show becca bikini 1 at Position (xpos=575)
    show missy bikini 1 at Position (xpos=375)
    with dissolve
    pause .15
    show roxxy bikini 6 with dissolve
    show player 426
    pause .15
    show roxxy bikini 7 with dissolve
    pause .15
    show roxxy bikini 8 with dissolve
    pause .15
    show roxxy bikini 9 with dissolve
    pause .15
    show roxxy bikini usa 5 with dissolve
    pause .15
    show roxxy 22 with dissolve
    pause .15
    show roxxy 24 with dissolve
    rox "C'mon girls, time's wasting!"
    show roxxy 23
    show becca bikini 13
    show missy bikini 3 with dissolve
    pause .25
    show becca bikini 16
    show missy bikini 4 with dissolve
    pause .25
    show becca bikini 3
    show missy bikini 4b
    with dissolve
    pause .2
    show becca bikini 4
    show missy bikini 5
    with dissolve
    pause .15
    show becca bikini 5
    show missy bikini 7b
    with dissolve
    pause .15
    show becca bikini 5b
    show missy naked 1
    with dissolve
    pause .15
    show becca naked 1 with dissolve
    show missy naked 2
    missy "Mmm, can I go first this time?!"
    show missy naked 1
    show becca naked 2
    becca "No, {b}Roxxy{/b} goes first. You know the rules!"
    show roxxy 24
    rox "That's right!"
    rox "Get undressed, {b}[firstname]{/b}."
    show roxxy 23
    show player 429
    player_name "Alright."
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player 430 with dissolve
    pause
    hide player
    hide becca
    hide missy
    show roxxy 109c at center
    with dissolve
    rox "I'll start us off..."
    pause
    rox "Wanna make sure you all remember who's the {b}Alpha Bitch{/b} here!"
    hide roxxy with dissolve
    return

label spin_bottle_minigame_mc_4some_loop_pre(current_character_machine, next_character_machine):
    $ anim_toggle = True
    $ animated = False
    $ M_roxxy.set("sex speed", .09)
    $ M_missy.set("sex speed", .09)
    $ M_becca.set("sex speed", .09)
    if current_character_machine == M_roxxy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_from_roxxy")

    elif current_character_machine == M_missy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_from_missy")

    elif current_character_machine == M_becca:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_from_becca")

    if next_character_machine == M_roxxy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_to_roxxy")
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_roxxy")

    elif next_character_machine == M_missy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_to_missy")
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_missy")

    elif next_character_machine == M_becca:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_change_to_becca")
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop_pre_becca")
    call expression game.dialog_select("spin_bottle_minigame_mc_4some_loop") pass (character_machine=next_character_machine)

label spin_bottle_minigame_mc_4some_loop_pre_change_from_roxxy:
    show roxxys_beach 13 at Position (xalign = 0.5) with dissolve
    pause .4
    show roxxys_beach 11 with dissolve
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_from_missy:
    show missys_beach 13 at Position (xalign = 0.5) with dissolve
    pause .4
    show missys_beach 11 with dissolve
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_from_becca:
    show beccas_beach 13 at Position (xalign = 0.7) with dissolve
    pause .4
    show beccas_beach 11 with dissolve
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_to_roxxy:
    player_name "Alright, {b}Roxxy{/b}. Ready for another round?"
    rox "Oh, I'm always ready for you, {b}[firstname]{/b}."
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_to_missy:
    player_name "Alright {b}Missy{/b}, your turn."
    missy "Yes, finally!"
    return

label spin_bottle_minigame_mc_4some_loop_pre_change_to_becca:
    player_name "{b}Becca{/b}, you want a turn?"
    becca "Y-yeah... Okay."
    return

label spin_bottle_minigame_mc_4some_loop_pre_roxxy:
    scene expression "backgrounds/location_beach_cabin_sex_foursome.jpg"
    if M_player.get("left of 4some") == M_becca:
        show beccas_beach_side at Position (xpos = 50)
        show missys_beach_side at Position (xpos = 925)
    else:

        show missys_beach_sidef at Position (xpos = 150)
        show beccas_beach_sidef at Position (xpos = 975)
    show roxxys_beach 12 at Position (xalign = 0.5)
    with dissolve
    rox "Now pay close attention girls..."
    rox "I'll show you how it's done!"
    show roxxys_beach 11
    missy "Can you really take the entire thing?"
    show roxxys_beach 13 with dissolve
    rox "Heh, yeah. It's a piece of ca-"
    show roxxys_beach 14
    rox "-aaAAAAKE!" with hpunch
    show expression AnimatedImage("roxxys_beach", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_beach at Position (xalign = 0.5)
    pause
    return

label spin_bottle_minigame_mc_4some_loop_pre_missy:
    scene expression "backgrounds/location_beach_cabin_sex_foursome.jpg"
    if M_player.get("left of 4some") == M_becca:
        show beccas_beach_side at Position (xpos = 50)
        show roxxys_beach_side at Position (xpos = 950)
    else:

        show roxxys_beach_sidef at Position (xpos = 50)
        show beccas_beach_sidef at Position (xpos = 975)
    show missys_beach 12 at Position (xalign = 0.5)
    with dissolve
    missy "I'm gonna blow your mind, {b}[firstname]{/b}!"
    show missys_beach 11
    becca "Hahah, yeah right!"
    becca "Like you have the first clue what you're doing..."
    show missys_beach 13 with dissolve
    missy "Hey shut up, I know exactly what I'm-"
    show missys_beach 14
    missy "{b}*Gasp*{/b}" with hpunch
    pause
    player_name "Oh, she's really tight!"
    show expression AnimatedImage("missys_beach", [1,2,3,4,5,6,7,8,9,10], M_missy) as missys_beach at Position (xalign = 0.5)
    pause
    return

label spin_bottle_minigame_mc_4some_loop_pre_becca:
    scene expression "backgrounds/location_beach_cabin_sex_foursome.jpg"
    if M_player.get("left of 4some") == M_roxxy:
        show roxxys_beach_sidef at Position (xpos = 50)
        show missys_beach_side at Position (xpos = 925)
    else:

        show missys_beach_sidef at Position (xpos = 150)
        show roxxys_beach_side at Position (xpos = 950)
    show beccas_beach 11 at Position (xalign = 0.7)
    with dissolve
    becca "Just be careful, I'm not used to something this big..."
    show beccas_beach 12
    rox "Oh please! Her pussy's so wet!"
    show beccas_beach 13 with dissolve
    rox "It's gonna slide right in."
    show beccas_beach 14
    becca "Haaah!" with hpunch
    rox "See..."
    becca "That's so fucking deep!"
    show expression AnimatedImage("beccas_beach", [1,2,3,4,5,6,7,8,9,10], M_becca) as beccas_beach at Position (xalign = 0.7)
    pause
    return

label spin_bottle_minigame_mc_4some_loop(character_machine):
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if character_machine == M_roxxy:
                    show expression AnimatedImage("roxxys_beach", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_beach at Position (xalign = 0.5)

                elif character_machine == M_missy:
                    show expression AnimatedImage("missys_beach", [1,2,3,4,5,6,7,8,9,10], M_missy) as missys_beach at Position (xalign = 0.5)

                elif character_machine == M_becca:
                    show expression AnimatedImage("beccas_beach", [1,2,3,4,5,6,7,8,9,10], M_becca) as beccas_beach at Position (xalign = 0.7)
                $ animated = True
            pause 5
            call expression game.dialog_select("spin_bottle_minigame_mc_4some_hscene_dialog") pass (character_machine=character_machine)
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                if character_machine == M_roxxy:
                    show expression "roxxys_beach {}".format(pose_list[pose_counter]) as roxxys_beach at Position (xalign = 0.5)

                elif character_machine == M_missy:
                    show expression "missys_beach {}".format(pose_list[pose_counter]) as missys_beach at Position (xalign = 0.5)

                elif character_machine == M_becca:
                    show expression "beccas_beach {}".format(pose_list[pose_counter]) as beccas_beach at Position (xalign = 0.3)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("spin_bottle_minigame_mc_4some_hscene_dialog") pass (character_machine=character_machine)
        $ animcounter += 1
    call screen spin_bottle_minigame_mc_4some_options(character_machine)

label spin_bottle_minigame_mc_4some_hscene_dialog(character_machine):
    if animcounter == 0:
        if randomizer() < 25:
            if character_machine == M_roxxy:
                rox "AAHHH! Fuck!{p=1}{nw}"
                missy "Haha!{p=1}{nw}"

            elif character_machine == M_missy:
                player_name "Ngghhh, holy crap!{p=2}{nw}"
                missy "Ohmygod, ohmygod, ohmygod!!!{p=1}{nw}"

            elif character_machine == M_becca:
                becca "Ahhh!{p=1}{nw}"
                missy "Wow, {b}Becca{/b} looks so cute when she's getting railed by that big dick...{p=3}{nw}"
                rox "I know, right?!{p=2}{nw}"
        else:

            if character_machine == M_missy:
                missy "It's so fucking thick!!{p=2}{nw}"

    elif animcounter == 1:
        if randomizer() < 25:
            if character_machine == M_roxxy:
                becca "Mmm, I love watching her tits bounce...{p=2}{nw}"
                missy "Yeah, it is kinda hypnotic.{p=2}{nw}"
                pause 1
                missy "Boingy, boingy, boingy!{p=1}{nw}"
                becca "Hahaha!{p=1}{nw}"
                rox "Oh, my god shut up!{p=2}{nw}"
                rox "I'm trying to enjoy th-{p=2}{nw}"
                if M_roxxy.get("sex speed") > .031:
                    $ M_roxxy.set("sex speed", M_roxxy.get("sex speed") - 0.03)
                rox "-iiIIISSS!!!{p=1}{nw}"

            elif character_machine == M_missy:
                rox "Harder, {b}[firstname]{/b}!{p=1}{nw}"
                rox "Fuck some smarts into that dumb bitch!{p=2}{nw}"
                if M_missy.get("sex speed") > .031:
                    $ M_missy.set("sex speed", M_missy.get("sex speed") - 0.03)
                missy "Oh, GOD!!{p=1}{nw}"
                becca "Wow, he's really giving it to her!{p=2}{nw}"
                rox "I know.{p=1}{nw}"
                rox "My man is a monster in the sack!{p=2}{nw}"

            elif character_machine == M_becca:
                becca "Oh my god, this is so good!{p=2}{nw}"
                rox "C'mon {b}[firstname]{/b}, do it harder!{p=2}{nw}"
                missy "Yeah, fuck those dumb freckles off her face!{p=2}{nw}"
                becca "Shut up, {b}Missy{/b}!{p=2}{nw}"
                if M_becca.get("sex speed") > .031:
                    $ M_becca.set("sex speed", M_becca.get("sex speed") - 0.03)
                becca "AAAHHHH!!!{p=1}{nw}"
                pause 1
                rox "Yeah, that's more like it!{p=2}{nw}"

    elif animcounter == 2:
        if randomizer() < 25:
            if character_machine == M_roxxy:
                rox "Holy shit!{p=1}{nw}"

            elif character_machine == M_missy:
                missy "I'm-{p=1}{nw}"
                missy "AAAAHHH!!{p=1}{nw}"
                becca "Mmm, I can't believe how much this is turning me on...{p=2}{nw}"
                rox "I know, right?!{p=1}{nw}"

            elif character_machine == M_becca:
                becca "Haah! FUCK!!{p=1}{nw}"
                missy "Oh, she's getting close!{p=2}{nw}"

    elif animcounter == 3:
        if randomizer() < 25:
            if character_machine == M_roxxy:
                rox "I'm gonna cum!{p=1}{nw}"
                rox "Oh my god!{p=1}{nw}"
                rox "I'm gonna-{p=1}{nw}"
                pause 1
                rox "NGGHHH!!!{p=1}{nw}"

            elif character_machine == M_missy:
                missy "Nggghh!!{p=1}{nw}"
                missy "HAAAAAAAHHH!!!{p=1}{nw}"

            elif character_machine == M_becca:
                becca "AAAHHH!!{p=1}{nw}"
                becca "{b}*Whimper*{/b}{p=1}{nw}"
                pause 1
                rox "God, she's so fucking adorable when she cums!{p=2}{nw}"
    return

label spin_bottle_minigame_mc_4some_cum(character_machine):
    if character_machine == M_roxxy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_roxxy_cum_dialogue")

    elif character_machine == M_missy:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_missy_cum_dialogue")

    elif character_machine == M_becca:
        call expression game.dialog_select("spin_bottle_minigame_mc_4some_becca_cum_dialogue")

    call expression game.dialog_select("spin_bottle_minigame_mc_4some_after_cum_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Roxxy"]["unlocked"] = True
    $ persistent.cookie_jar["Roxxy"]["gallery"]["08_unlocked"] = True
    $ persistent.cookie_jar["Becca & Missy"]["unlocked"] = True
    $ persistent.cookie_jar["Becca & Missy"]["gallery"]["03_unlocked"] = True
    $ persistent.cookie_jar["Becca & Missy"]["gallery"]["04_unlocked"] = True
    $ M_player.machine_trigger(T_mc_beach_sex)
    $ game.timer.tick()
    $ game.main()

label spin_bottle_minigame_mc_4some_roxxy_cum_dialogue:
    player_name "{b}Roxxy{/b}, I'm getting close!"
    rox "Don't stop, {b}[firstname]{/b}!"
    rox "I want all of it inside me!"
    pause
    show roxxys_beach 14_15 at Position (xalign = 0.5)
    player_name "HNNGGG!!!" with flash
    rox "AAAHHHH!!!"
    show roxxys_beach 15
    show xray_roxxy_3some_beach at Position (align=(0,0))
    missy "Awesome!"
    pause
    hide xray_roxxy_3some_beach
    show roxxys_beach 16
    with dissolve
    rox "Oh my god that felt so good!"
    show roxxys_beach 17 with dissolve
    pause
    becca "Holy shit, look at that huge load!"
    missy "I'm so jelly right now..."
    return

label spin_bottle_minigame_mc_4some_missy_cum_dialogue:
    player_name "I'm gonna blow!"
    rox "Don't stop, {b}[firstname]{/b}."
    rox "Fill that dumb bitch up!"
    missy "Oh yess!!!"
    missy "Thank you, thank you, THANK YOU!!"
    pause
    show missys_beach 14_15 at Position (xalign = 0.5)
    player_name "HNNGGG!!!" with flash
    missy "{b}*Gasp*{/b}"
    show missys_beach 15
    show xray_missy_3some_beach at Position (align=(0,0))
    pause
    hide xray_missy_3some_beach
    show missys_beach 16
    with dissolve
    missy "Haah... Haah..."
    show missys_beach 17
    missy "That was epic!"
    show missys_beach 18
    becca "Yeah, he totally wrecked you!"
    rox "That was really hot..."
    return

label spin_bottle_minigame_mc_4some_becca_cum_dialogue:
    player_name "I can't hold it much longer..."
    becca "Oh, can I have it {b}Roxxy{/b}?!"
    becca "Please!"
    rox "{b}*Sigh*{/b} Alright, fine..."
    missy "Aww but I wanted it!"
    rox "Shut up, {b}Missy{/b}!"
    pause
    player_name "Here it comes!"
    show beccas_beach 14_15 at Position (xalign = 0.7)
    player_name "HNNGGG!!!" with flash
    becca "{b}*Whimper*{/b}"
    show beccas_beach 15
    show xray_becca_3some_beach at Position (align=(0,0))
    pause
    hide xray_becca_3some_beach
    show beccas_beach 16
    with dissolve
    pause
    show beccas_beach 17 with dissolve
    becca "Oh my god, that was amazing..."
    show beccas_beach 18
    missy "Whoa, that's so much cum!"
    rox "You owe me big time, {b}Becca{/b}!"
    return

label spin_bottle_minigame_mc_4some_after_cum_dialogue:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 366f at right
    show becca naked 4 at Position (xpos=315)
    show roxxy 106 at Position (xpos=600)
    show missy naked 5 at left
    with dissolve
    missy "That was by far the coolest thing we've ever done!"
    show missy naked 4
    show becca naked 5
    becca "You are such a dork, {b}Missy{/b}..."
    show becca naked 4
    show missy naked 5
    missy "What?!"
    missy "I'm serious!"
    missy "We should totally do this again next week!"
    show missy naked 4
    becca "..."
    show roxxy 107
    rox "{b}*Sigh*{/b}"
    rox "We'll see..."
    show roxxy 106
    show missy naked 5
    missy "Yaaay!!!"
    show missy naked 4
    show becca naked 5
    becca "C'mon, stupid..."
    becca "Let's give these love birds some alone time."
    show becca naked 4
    missy "Hmm?"
    show missy naked 5
    missy "Oh..."
    missy "Okay."
    missy "Thanks for fucking us, {b}[firstname]{/b}!!!"
    show missy naked 4
    becca "!!!" with hpunch
    show missy naked 5
    missy "It was REALLY good!"
    missy "Byeee!!"
    hide missy with dissolve
    show becca naked 5
    becca "I..."
    becca "She shouldn't have..."
    show becca naked 4
    becca "..."
    show becca naked 5
    becca "Hehe, uhh..."
    becca "Bye {b}[firstname]{/b}."
    hide becca with dissolve
    show roxxy 108
    rox "Well, that was smooth..."
    show roxxy 106
    show player 365f
    player_name "I think they're adorable."
    show player 366f
    show roxxy 107f at Position (xpos=500) with dissolve
    rox "Yeah, but don't let them know that."
    rox "I trust you enjoyed that?"
    show roxxy 106f
    show player 365f
    player_name "Y-yeah!"
    show player 367f
    player_name "You sure you're okay with all this?"
    show player 368f
    show roxxy 107f
    rox "So long as it only happens when I'm present."
    show roxxy 108f
    rox "... Yeah!"
    show player 366f
    show roxxy 107f
    rox "I actually think it's REALLY sexy."
    rox "Watching you fuck them."
    show roxxy 106f
    show player 365f
    player_name "Wow, you're like the best girlfriend ever, {b}Roxxy{/b}!"
    show player 366f
    show roxxy 107f
    rox "I know, right?!"
    rox "Now, c'mon!"
    show roxxy 108f
    rox "I wanna go skinny dipping!"
    hide roxxy with dissolve
    show player 365f
    player_name "Heh, wait up!"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
