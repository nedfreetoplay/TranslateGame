label spin_bottle_minigame_becca:
    if M_roxxy.get("roxxy locker sex"):
        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_becca")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_becca_missy")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_becca")
            call expression game.dialog_select("spin_bottle_minigame_final_spin")

        elif M_player.get("beach bottle spins") == 4:
            if not M_becca.get("becca beach sex"):
                call expression game.dialog_select("spin_bottle_minigame_becca_solo_intro_pre_first")
            else:
                call expression game.dialog_select("spin_bottle_minigame_becca_solo_intro_pre_repeat")
            call expression game.dialog_select("spin_bottle_minigame_becca_solo_intro")
            $ anim_toggle = True
            $ animated = False
            $ M_becca.set("sex speed", .09)
            call expression game.dialog_select("spin_bottle_minigame_becca_solo_intro_after")
            jump expression game.dialog_select("spin_bottle_minigame_becca_solo_loop")
    else:

        if M_player.get("beach bottle spins") == 1:
            call expression game.dialog_select("spin_bottle_minigame_kiss_roxxy_becca")

        elif M_player.get("beach bottle spins") == 2:
            call expression game.dialog_select("spin_bottle_minigame_kiss_becca_missy")
            call expression game.dialog_select("spin_bottle_minigame_last_spin")

        elif M_player.get("beach bottle spins") == 3:
            call expression game.dialog_select("spin_bottle_minigame_kiss_mc_becca")
            $ game.timer.tick()
            $ game.main()
    call screen spin_bottle_minigame

label beach_becca_solo_replay:
    $ M_player.set("beach bottle spins", 4)
    $ M_roxxy.set("roxxy locker sex", 1)
    jump expression game.dialog_select("spin_bottle_minigame_becca")

label spin_bottle_minigame_becca_solo_intro_pre_first:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 8b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 6 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "!!!"
    show player_sitting 3
    show becca sitting 8
    show missy sitting 7
    missy "What?! NO!!"
    show missy sitting 8
    show becca sitting 8b
    show roxxy sitting 5
    rox "Hehe, looks like it's {b}Becca{/b}'s lucky night..."
    show roxxy sitting 2
    show becca sitting 8c
    becca "I don't-"
    show becca sitting 10b
    becca "I mean, are you-"
    show becca sitting 8b
    show roxxy sitting 3
    rox "Aww, look how shy she is..."
    show roxxy sitting 2
    show becca sitting 10b
    becca "I'm not!"
    show becca sitting 10
    show roxxy sitting 6
    rox "Isn't she just adorable?"
    show roxxy sitting 2
    show becca sitting 9
    becca "..."
    hide roxxy
    hide becca
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show roxxy bikini 26 with dissolve
    rox "You're going to like this..."
    hide roxxy with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show roxxy bikini 22 at right
    show becca bikini 1
    with dissolve
    rox "I can't wait for you to fuck her adorable little brains out!"
    show roxxy bikini 21
    show player 11
    player_name "!!!" with hpunch
    show becca bikini 13
    show player 10
    player_name "Are you for real?!"
    show becca bikini 1
    show player 11
    rox "Mmmhmm..."
    show roxxy bikini 22
    rox "What did you think the special reward was?!"
    show roxxy bikini 21
    show player 29 with dissolve
    player_name "I dunno, more kissing?!"
    show player 3
    show becca bikini 15
    show roxxy bikini 23
    rox "Hahaha!"
    show roxxy bikini 22
    rox "C'mon, {b}Becca{/b}..."
    rox "Get that bikini off!"
    show roxxy bikini 21
    show becca bikini 6
    becca "I uhh..."
    show becca bikini 18
    becca "O-okay."
    show becca bikini 3 with dissolve
    pause
    show becca bikini 4 with dissolve
    pause
    show becca bikini 5
    show player 428
    with dissolve
    pause
    show becca bikini 5b with dissolve
    pause
    show becca naked 1 with dissolve
    player_name "..."
    show roxxy bikini 22
    rox "Daaamn!"
    show player 426
    rox "Isn't she sexy, {b}[firstname]{/b}?"
    show roxxy bikini 21
    show player 429
    player_name "Y-yeah..."
    show player 426
    show roxxy bikini 22
    rox "Don't you just wanna ravage her?!"
    show roxxy bikini 21
    show player 429
    player_name "Y-yeah..."
    show player 426
    show roxxy bikini 22
    rox "Hehehe!"
    rox "What about you, {b}Becca{/b}?!"
    rox "Don't you want it?"
    show roxxy bikini 21
    show becca naked 2
    becca "... Yes."
    show becca naked 1
    show roxxy bikini 23
    rox "C'mon, you can do better than that!"
    show roxxy bikini 22
    rox "I want you to beg for it!"
    show roxxy bikini 21
    show player 11
    show becca naked 3
    becca "!!!"
    becca "..."
    show becca naked 2
    becca "Please..."
    show becca naked 1
    show roxxy bikini 23
    rox "Please what?"
    show roxxy bikini 21
    show becca naked 2
    becca "Please, {b}Roxxy{/b}..."
    becca "I want {b}[firstname]{/b} to fuck me!"
    show becca naked 1
    show roxxy bikini 22
    rox "Hahaha!"
    rox "Alright."
    rox "Get over there and fuck her, {b}[firstname]{/b}!"
    show roxxy bikini 21
    show player 429
    player_name "O-okay..."
    hide player
    hide becca
    hide roxxy
    with dissolve
    return

label spin_bottle_minigame_becca_solo_intro_pre_repeat:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 8b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 6 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "!!!"
    show player_sitting 3
    show missy sitting 7
    missy "What?! NO!!"
    show missy sitting 8
    show roxxy sitting 3
    show player_sitting 3b
    rox "Hehe, looks like it's {b}Becca{/b}'s lucky night..."
    show player_sitting 3
    show roxxy sitting 2
    show becca sitting 8c
    becca "I don't-"
    show becca sitting 10b
    becca "I mean, are you-"
    show becca sitting 8b
    show roxxy sitting 3
    rox "Aww, look how shy she is..."
    show roxxy sitting 2
    show becca sitting 8c
    becca "I'm not!"
    show becca sitting 9
    show roxxy sitting 6
    rox "Isn't she just adorable?"
    show roxxy sitting 2
    becca "..."
    hide becca
    hide roxxy
    hide player_sitting
    with dissolve

    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show roxxy bikini 26 with dissolve
    rox "You're going to like this..."
    hide roxxy with dissolve

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 13 at left
    show roxxy bikini 22 at right
    show becca bikini 1
    with dissolve
    rox "C'mon, {b}Becca{/b}..."
    rox "Get that bikini off!"
    show roxxy bikini 21
    show becca bikini 6
    becca "I uhh..."
    show becca bikini 18
    becca "O-okay."
    show becca bikini 3 with dissolve
    pause
    show becca bikini 4 with dissolve
    pause
    show becca bikini 5
    show player 428
    with dissolve
    pause
    show becca bikini 5b with dissolve
    pause
    show becca naked 1 with dissolve
    player_name "..."
    show roxxy bikini 22
    rox "Daaamn!"
    show player 426
    rox "Isn't she sexy, {b}[firstname]{/b}?"
    show roxxy bikini 21
    show player 429
    player_name "Y-yeah..."
    show player 426
    show roxxy bikini 22
    rox "Don't you just wanna ravage her?!"
    show roxxy bikini 21
    show player 429
    player_name "Y-yeah..."
    show player 426
    show roxxy bikini 22
    rox "Hehehe!"
    rox "What about you, {b}Becca{/b}?!"
    rox "Don't you want it?"
    show roxxy bikini 21
    show becca naked 2
    becca "... Yes."
    show becca naked 1
    show roxxy bikini 23
    rox "C'mon, you can do better than that!"
    show roxxy bikini 22
    rox "I want you to beg for it!"
    show roxxy bikini 21
    show player 11
    show becca naked 3
    becca "!!!"
    becca "..."
    show becca naked 2
    becca "Please..."
    show becca naked 1
    show roxxy bikini 23
    rox "Please what?"
    show roxxy bikini 21
    show becca naked 2
    becca "Please, {b}Roxxy{/b}..."
    becca "I want {b}[firstname]{/b} to fuck me!"
    show becca naked 1
    show roxxy bikini 22
    rox "Hahaha!"
    rox "Alright."
    rox "Get over there and fuck her, {b}[firstname]{/b}!"
    show roxxy bikini 21
    show player 429
    player_name "O-okay..."
    hide player
    hide becca
    hide roxxy
    with dissolve
    return

label spin_bottle_minigame_becca_solo_intro:
    scene expression "backgrounds/location_beach_cabin_sex_becca.jpg"
    show beccas_solo 1
    with dissolve
    pause
    show beccas_solo 2 with dissolve
    pause
    show beccas_solo 3
    becca "!!!" with hpunch
    becca "Holy shit!"
    rox "Hahaha!"
    rox "I know, right?!"
    becca "It's so big!"
    rox "C'mon, {b}[firstname]{/b}. She can take it!"
    show beccas_solo 4 with dissolve
    becca "AAhhh!!"
    return

label spin_bottle_minigame_becca_solo_intro_after:
    show expression AnimatedImage("beccas_solo", [7,8,9,10,11,12,13,14,15,16], M_becca) as beccas_solo
    with dissolve
    pause
    return

label spin_bottle_minigame_becca_solo_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("beccas_solo", [7,8,9,10,11,12,13,14,15,16], M_becca) as beccas_solo
                $ animated = True
            pause 5
            call expression game.dialog_select("spin_bottle_minigame_becca_solo_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [7,8,9,10,11,12,13,14,15,16]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "beccas_solo {}".format(pose_list[pose_counter]) as beccas_solo
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("spin_bottle_minigame_becca_solo_hscene_dialog")
        $ animcounter += 1
    call screen spin_bottle_minigame_solo_sex_options(M_becca)

label spin_bottle_minigame_becca_solo_hscene_dialog:
    if animcounter == 0:
        if randomizer() < 25:
            becca "Oh my god!{p=2}{nw}"
            becca "OH MY GOD!!{p=2}{nw}"
            rox "Hahaha!{p=1}{nw}"

    elif animcounter == 1:
        if randomizer() < 25:
            rox "That's it, {b}[firstname]{/b}!{p=2}{nw}"
            rox "Fuck her brains out!{p=2}{nw}"

    elif animcounter == 2:
        if randomizer() < 25:
            becca "AAAHH!!{p=1}{nw}"
            becca "I'm cumming!{p=1}{nw}"
            becca "{b}*Whimper*{/b}{p=1}{nw}"
            pause
            rox "Hahaha, that was fast!{p=2}{nw}"
            rox "She is making the most adorable faces!{p=2}{nw}"
            rox "Keep going, {b}[firstname]{/b}!{p=2}{nw}"

    elif animcounter == 3:
        if randomizer() < 25:
            becca "Ngghh!!{p=1}{nw}"
            pause 1
        else:

            becca "{b}*Whimper*{/b}{p=1}{nw}"
    return

label spin_bottle_minigame_becca_solo_cum:
    call expression game.dialog_select("spin_bottle_minigame_becca_solo_cum_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Becca & Missy"]["unlocked"] = True
    $ persistent.cookie_jar["Becca & Missy"]["gallery"]["02_unlocked"] = True
    $ M_becca.machine_trigger(T_becca_beach_sex)
    $ game.timer.tick()
    $ game.main()

label spin_bottle_minigame_becca_solo_cum_dialogue:
    player_name "I'm getting close!"
    becca "Finish inside me!"
    rox "Excuse me?!"
    becca "..."
    rox "That didn't sound like begging to me..."
    becca "{b}*Whimper*{/b}"
    pause
    becca "Ngghhh!!!"
    becca "Please, {b}Roxxy{/b}!!!"
    becca "AAhhh!!! Please, please please!"
    rox "Hahaha!"
    rox "Alright, {b}[firstname]{/b}..."
    rox "Give it to her!"
    pause
    becca "OH MY GOD!!!"
    show beccas_solo 3_4
    player_name "HNNGGG!!!" with flash
    pause
    show beccas_solo 5 with dissolve
    player_name "Haaah... Haaah..."
    becca "{b}*Whimper*{/b}"
    show beccas_solo 6 with dissolve
    rox "Haha, wow you really did a number on her..."
    rox "That was so fucking hot!"

    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 365 at left
    show becca naked 4
    show roxxy 1g at right
    with dissolve
    player_name "You alright, {b}Becca{/b}?"
    show player 366
    show becca naked 5
    becca "Mmmhmm, I just can't... Exactly... Feel my legs..."
    show becca naked 4
    show roxxy 1h
    rox "Hehe, I think you exhausted her."
    show roxxy 1g
    pause
    show player 365
    player_name "I feel kinda bad for {b}Missy{/b}."
    player_name "Out there all by herself..."
    show player 366
    show roxxy 1h
    rox "Psh, screw that greedy bitch."
    rox "Besides, she's been at the door watching almost the entire time..."
    rox "Haven't you, {b}Missy{/b}?!"
    show roxxy 1g
    pause
    missy "... No."
    show roxxy 4
    show player 365
    rox "Hahaha!"
    player_name "Hahaha!"
    hide player
    hide roxxy
    hide becca
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
