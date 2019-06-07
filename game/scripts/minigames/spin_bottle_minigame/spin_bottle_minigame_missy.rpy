label spin_bottle_minigame_missy:
    if M_roxxy.get("roxxy locker sex"):
        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_missy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_missy")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_becca_missy")
            call expression game.dialog_select("spin_bottle_minigame_final_spin")

        elif M_player.get("beach bottle spins") == 4:
            if not M_missy.get("missy beach sex"):
                call expression game.dialog_select("spin_bottle_minigame_missy_solo_intro_pre_first")
            else:
                call expression game.dialog_select("spin_bottle_minigame_missy_solo_intro_pre_repeat")
            call expression game.dialog_select("spin_bottle_minigame_missy_solo_intro")
            $ anim_toggle = True
            $ animated = False
            $ M_missy.set("sex speed", .09)
            call expression game.dialog_select("spin_bottle_minigame_missy_solo_intro_after")
            jump expression game.dialog_select("spin_bottle_minigame_missy_solo_loop")
    else:

        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_missy")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_missy")
            call expression game.dialog_select("spin_bottle_minigame_last_spin")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_becca_missy")
            $ game.timer.tick()
            $ game.main()
    call screen spin_bottle_minigame

label beach_missy_solo_replay:
    $ M_player.set("beach bottle spins", 4)
    $ M_roxxy.set("roxxy locker sex", 1)
    jump expression game.dialog_select("spin_bottle_minigame_missy")

label spin_bottle_minigame_missy_solo_intro_pre_first:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 6b at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 5 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "YES!!!"
    show becca sitting 10
    becca "..."
    missy "Haha, yes, yes, yessss!!!"
    show roxxy sitting 6
    rox "{b}*Sigh*{/b}"
    rox "Alright, {b}Missy{/b} wins..."
    show roxxy sitting 2
    show missy sitting 3
    missy "Damn right!"
    show missy sitting 2
    show player_sitting 3b
    show roxxy sitting 6
    rox "Just remember the rules!"
    show roxxy sitting 2
    show player_sitting 3
    player_name "..."
    show missy sitting 3
    missy "I remember, I remember! Come on {b}[firstname]{/b}!"
    show missy sitting 2
    show roxxy sitting 3
    rox "Fine."
    rox "Let's get this over with..."
    show roxxy sitting 2
    show missy sitting 5
    missy "Best. Night. EVER!"
    hide missy
    hide roxxy
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show roxxy bikini 27 with dissolve
    rox "Keep up, {b}[firstname]{/b}..."
    hide roxxy with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show missy bikini 3
    show roxxy bikini 21f at right
    pause
    show roxxy bikini 22f
    rox "Alright bitch!"
    show roxxy bikini 21f
    show missy bikini 4 with dissolve
    pause .25
    show missy bikini 4b with dissolve
    pause .25
    show missy bikini 5 with dissolve
    pause .25
    show roxxy bikini 22 at Position (xoffset=-33) with dissolve
    rox "I want you to start by-"
    show player 428
    show roxxy bikini 24 at Position (xoffset=-33)
    show missy bikini 7b with dissolve
    rox "!!!"
    show missy naked 8 with dissolve
    missy "I am SO ready!"
    show missy naked 1 with dissolve
    show player 10
    player_name "What are we doing?!"
    show player 5
    show roxxy bikini 19 with dissolve
    rox "... But I haven't-"
    show roxxy bikini 20
    show missy naked 3f with dissolve
    missy "I've literally been dreaming about that dick since the moment I saw it, {b}[firstname]{/b}..."
    show player 11
    player_name "!!!"
    show missy naked 1f with dissolve
    show player 427
    player_name "You mean we're going to-"
    show player 11
    show roxxy bikini 19
    rox "You know, you're really taking the fun outta this, {b}Missy{/b}..."
    show roxxy bikini 20
    show missy naked 2f
    missy "Oh, crap. I'm sorry, {b}Roxxy{/b}"
    missy "I forgot you were here..."
    show missy naked 9_10 at Position (xpos=300) with dissolve
    show player 428
    show roxxy bikini 24 at Position (xoffset=-33)
    rox "!!!" with hpunch
    pause
    show roxxy bikini 19 with dissolve
    rox "{b}[firstname]{/b}?"
    show roxxy bikini 20
    show player 427
    player_name "Y-yeah?"
    show player 426
    show roxxy bikini 19
    rox "Wreck this bitch!"
    show roxxy bikini 20
    show missy naked 3f at center with dissolve
    show player 11
    missy "{b}*Gasp*{/b} Yes!!!"
    show missy naked 1f with dissolve
    show player 12
    player_name "Wait, you're really okay with this?"
    show player 11
    show roxxy bikini 19
    rox "Yes."
    rox "I want you to fuck her till she's too tired to open her stupid mouth!"
    show roxxy bikini 20
    show missy naked 2f
    missy "Oh my god, that is an awesome idea!!!"
    show missy naked 1f
    show player 426
    player_name "..."
    show missy naked 2f
    missy "You heard her, {b}[firstname]{/b}!"
    show missy naked 3f with dissolve
    missy "Get over here and fuck me stupid!"
    show player 429
    player_name "... O-okay."
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    hide player
    show missy naked 6f
    with dissolve
    missy "It's finally happening!!"
    show missy naked 7f
    missy "Oh, I'm so excited!!"
    hide player
    hide missy
    hide roxxy
    with dissolve
    return

label spin_bottle_minigame_missy_solo_intro_pre_repeat:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 6b at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 5 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "YES!!!"
    show becca sitting 10
    becca "..."
    missy "Haha, yes, yes, yessss!!!"
    show roxxy sitting 6
    rox "{b}*Sigh*{/b}"
    show player_sitting 3b
    rox "Alright, {b}Missy{/b} wins..."
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 3
    missy "Damn right!"
    show missy sitting 2
    show roxxy sitting 6
    rox "Just remember the rules!"
    show roxxy sitting 2
    player_name "..."
    show missy sitting 3
    missy "I remember, I remember! Come on {b}[firstname]{/b}!"
    show missy sitting 2
    show roxxy sitting 3
    rox "Fine."
    rox "Let's get this over with..."
    show roxxy sitting 2
    show missy sitting 5
    missy "Best. Night. EVER!"
    hide missy
    hide roxxy
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show roxxy bikini 27 with dissolve
    rox "Keep up, {b}[firstname]{/b}..."
    hide roxxy with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show roxxy bikini 19 at right
    show missy bikini 1b
    with dissolve
    rox "Are you gonna do what I tell you this time?!"
    show roxxy bikini 20
    show missy bikini 2b
    missy "Yes, {b}Roxxy{/b}..."
    show missy bikini 1b
    show roxxy bikini 22 with dissolve
    rox "Take off your clothes."
    show roxxy bikini 21
    show missy bikini 3 with dissolve
    pause .25
    show missy bikini 4 with dissolve
    show player 426
    pause .25
    show missy bikini 4b with dissolve
    pause .25
    show missy bikini 5 with dissolve
    show roxxy bikini 22
    rox "That's a good little bitch..."
    show missy bikini 7b with dissolve
    rox "Isn't she a good little bitch, {b}[firstname]{/b}?"
    show missy naked 1 with dissolve
    show roxxy bikini 21
    show player 429
    player_name "Y-yeah."
    show player 426
    show roxxy bikini 23
    rox "Hahaha!"
    show roxxy bikini 22
    rox "Now, come over here and beg {b}[firstname]{/b} to fuck you..."
    show roxxy bikini 21
    show missy naked 2f at Position (xpos=450) with dissolve
    show player 13
    missy "Please, fuck me {b}[firstname]{/b}."
    show player 426
    show missy naked 3f
    missy "Please..."
    show missy naked 9_10 at Position (xpos=300) with dissolve
    show player 426
    missy "I want it so bad..."
    show roxxy bikini 22
    rox "Hmm, that was pretty good."
    rox "What do you say, {b}[firstname]{/b}?"
    show roxxy bikini 23
    rox "Has she earned it?"
    show roxxy bikini 21
    show player 429
    player_name "Definitely!"
    show missy naked 8 at center with dissolve
    show player 426
    show roxxy bikini 22
    rox "Hahaha!"
    rox "Alright then."
    rox "Go ahead."
    hide player
    hide missy
    hide roxxy
    with dissolve
    return

label spin_bottle_minigame_missy_solo_intro:
    scene expression "backgrounds/location_beach_cabin_sex_missy.jpg"
    show missys_solo 1 at left
    with dissolve
    missy "Yes, yes, YES!!!"
    show missys_solo 2 with dissolve
    pause
    show missys_solo 3
    missy "{b}*Gasp*{/b}!!!" with hpunch
    player_name "Wow, that's really tight!"
    missy "..."
    player_name "{b}Missy{/b}?"
    missy "..."
    player_name "Is she alright?"
    rox "... Huh."
    rox "It really did shut her up..."
    missy "..."
    rox "Hahaha!"
    return

label spin_bottle_minigame_missy_solo_intro_after:
    show expression AnimatedImage("missys_solo", [7,8,9,10,11,12,13,14,15,16,17,18], M_missy) as missys_solo at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    pause
    return

label spin_bottle_minigame_missy_solo_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("missys_solo", [7,8,9,10,11,12,13,14,15,16,17,18], M_missy) as missys_solo at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("spin_bottle_minigame_missy_solo_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [7,8,9,10,11,12,13,14,15,16,17,18]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "missys_solo {}".format(pose_list[pose_counter]) as missys_solo at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("spin_bottle_minigame_missy_solo_hscene_dialog")
        $ animcounter += 1
    call screen spin_bottle_minigame_solo_sex_options(M_missy)

label spin_bottle_minigame_missy_solo_hscene_dialog:
    if animcounter == 1:
        if randomizer() < 25:
            missy "FUUUUUCK!!!{p=1}{nw}"
            player_name "There she is!{p=2}{nw}"
            player_name "I thought we had lost you for a second there...{p=2}{nw}"
            missy "...{p=1}{nw}"
            player_name "{b}Missy{/b}?!{p=1}{nw}"
            missy "...{p=1}{nw}"
            rox "C'mon, {b}[firstname]{/b}. Fuck her harder!{p=3}{nw}"
            if M_missy.get("sex speed") > .031:
                $ M_missy.set("sex speed", M_missy.get("sex speed") - 0.03)
            missy "AAAHH!!!{p=1}{nw}"
            pause 1
            missy "Ohmygod, ohmygod, OH. MY. GOD!!!{p=2}{nw}"

    elif animcounter == 2:
        if randomizer() < 25:
            missy "It's so fucking deep!{p=2}{nw}"
            rox "Hahaha!{p=1}{nw}"

    elif animcounter == 3:
        if randomizer() < 25:
            player_name "She's so tight!{p=2}{nw}"
            rox "Really?{p=1}{nw}"
            rox "I guess you aren't a slut afterall, {b}Missy{/b}.{p=2}{nw}"
            missy "I'll be whatever you want me to be...{p=2}{nw}"
            missy "Just don't stop!{p=2}{nw}"
    return

label spin_bottle_minigame_missy_solo_cum:
    call expression game.dialog_select("spin_bottle_minigame_missy_solo_cum_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Becca & Missy"]["unlocked"] = True
    $ persistent.cookie_jar["Becca & Missy"]["gallery"]["01_unlocked"] = True
    $ M_missy.machine_trigger(T_missy_beach_sex)
    $ game.timer.tick()
    $ game.main()

label spin_bottle_minigame_missy_solo_cum_dialogue:
    player_name "I'm getting close."
    missy "I want him to finish inside me."
    missy "Please, {b}Roxxy{/b}!"
    missy "Please, please, please!"
    rox "Haha, well since you asked so nicely..."
    rox "Go ahead, {b}[firstname]{/b}..."
    pause
    player_name "Here it comes..."
    pause
    show missys_solo 3_4
    player_name "HNNGGG!!!" with flash
    missy "YESSSS!!!"
    show missys_solo 4
    show xray_missy_1o1_beach at Position (align=(0,0))
    pause
    hide xray_missy_1o1_beach
    show missys_solo 5
    with dissolve
    missy "Oh my god."
    show missys_solo 6 with dissolve
    missy "What a load..."
    rox "Hahaha!"

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 366 at left
    show missy naked 5
    show roxxy 1g at right
    with dissolve
    missy "That was so awesome!"
    show missy naked 4
    show roxxy 1h
    rox "It was pretty hot..."
    show roxxy 1g
    show player 365
    player_name "Yeah, that was really nice!"
    show player 366
    show missy naked 5
    missy "We absolutely have to do that again sometime!"
    show missy naked 4
    show roxxy 2
    rox "God, you are such a greedy bitch, {b}Missy{/b}!"
    show roxxy 1g
    show missy naked 5
    missy "C'mon, please {b}Roxxy{/b}!!"
    show missy naked 4
    show roxxy 1
    rox "{b}*Sigh*{/b}"
    show roxxy 2
    rox "Maybe next {b}Saturday{/b}..."
    show roxxy 1g
    show missy naked 5
    missy "Yessss!!!"
    missy "Thank you, thank you, THANK YOU!!!"
    show missy naked 4
    show roxxy 2
    rox "Ugh, really?"
    show roxxy 1g
    show missy naked 5
    missy "Your boyfriend has like, the best dick ever!"
    show missy naked 4
    show roxxy 1h
    rox "Uhh, yeah. Tell me something I don't know!"
    show roxxy 1g
    show missy naked 5f with dissolve
    missy "Seriously, {b}[firstname]{/b}."
    missy "Like, THE BEST!"
    missy "I can't wait to tell {b}my sister{/b} about it!"
    show missy naked 4f
    show roxxy 3c
    rox "What?!"
    rox "Hell no!"
    rox "Don't tell that skank anything about this!"
    show roxxy 3b
    show missy naked 5 with dissolve
    missy "Aww, but-"
    show missy naked 4
    show roxxy 3
    rox "Not a word, {b}Missy{/b}!"
    show roxxy 3b
    missy "..."
    show missy naked 5
    missy "Alright, I won't tell her, sheesh..."
    show missy naked 4
    show roxxy 2
    rox "Good. Now put your damn clothes on and go sit by the fire with {b}Becca{/b}!"
    show roxxy 1g
    show missy naked 5
    missy "{b}*Sigh*{/b} Fine."
    hide missy
    hide player
    hide roxxy
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
