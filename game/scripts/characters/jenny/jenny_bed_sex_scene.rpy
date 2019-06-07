label jenny_bed_night_button:
    $ player.go_to(L_home_sisbedroom)
    if not M_jenny.finished_state(S_jenny_give_cunni):
        call expression game.dialog_select("jenny_bed_night_pre_j17")
        $ player.go_to(L_home_hallway)
        $ game.main()
    elif M_jenny.between_states(S_jenny_give_cunni, S_jenny_night_time_sex):
        call expression game.dialog_select("jenny_bed_night_j17_j20")
        $ player.go_to(L_home_hallway)
        $ game.main()
    else:
        call expression game.dialog_select("jenny_bed_night_sex_intro")
    $ game.main()

label jenny_bed_night_pre_j17:
    scene expression player.location.background_closeup with None
    show player f_surprised_teeth with dissolve
    player_name "( There's no way I'm bothering her! )"
    player_name "( She'll kill me! )"
    hide player with dissolve
    return

label jenny_bed_night_j17_j20:
    scene expression player.location.background_closeup with None
    show player f_thinking a_dressed_thinking with dissolve
    player_name "( You know, we have been getting along better recently... )"
    player_name "( Maybe she wouldn't mind? )"
    show player f_grin
    menu:
        "Do it.":
            call expression game.dialog_select("jenny_bed_night_do_it_j17")
        "I'd better not":
            call expression game.dialog_select("jenny_bed_night_better_not")
    return

label jenny_bed_night_do_it_j17:
    scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
    show jenny b_sleep_side o_sleep_blanket a_sleep_side f_sleep_side_rolleye
    show player b_sleep_climb a_empty f_empty at Position (align=(0,0)) with dissolve
    pause
    show player b_sleep_side f_sleep_side_shy o_sleep_side_boxers
    show expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
    show jenny o_empty
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png"
    with dissolve
    pause
    show player b_sleep_cuddle f_sleep_cuddle_side_shy o_empty
    hide expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
    with dissolve
    pause
    show jenny f_sleep_side_wake
    jen "Hmm?"
    show jenny b_sleep_turn a_sleep_turn f_sleep_turn_angry_talk o_sleep_panties with dissolve
    jen "What the-"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "H-hi."
    show player f_sleep_cuddle_side_shy
    pause
    show jenny f_sleep_turn_angry_talk a_sleep_turn_push
    show player b_sleep_side o_sleep_side_boxers a_sleep_side_react f_sleep_side_shock
    jen "WHAT THE FUCK?!" with hpunch
    scene expression player.location.background_blur
    show player f_surprised_teeth b_underwear a_naked_sides
    show jenny f_angry_talk a_dressed_crossed
    with fade
    jen "Seriously, what the fuck is wrong with you?!"
    show jenny f_angry
    show player f_sad_talk
    player_name "I'm sorry... I-"
    show player f_sad
    show jenny f_angry_talk
    jen "You don't just sneak into a woman's bed while she's sleeping, {b}[firstname]{/b}!"
    jen "That is so creepy!"
    show jenny f_angry
    show player f_sad_talk
    player_name "I just thought that maybe-"
    show player f_sad_talk_down
    show jenny f_angry_talk
    jen "No, you obviously didn't think!"
    jen "Eugh, just get the fuck out!"
    show jenny f_angry
    show player f_sad
    player_name "..."
    hide player with dissolve
    show jenny f_eyeroll
    jen "Fucking loser..."
    scene black with fade
    pause
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show player f_sad_talk_down with dissolve
    player_name "( Well, that was awful... )"
    player_name "( Why did I think that was a good idea? )"
    player_name "( {b}*Sigh*{/b} I hope she doesn't tell {b}[deb_name]{/b} about this... )"
    hide player with dissolve
    return

label jenny_bed_night_better_not:
    show player f_worried a_dressed_pocket with dissolve
    player_name "( Yeah, no... )"
    player_name "( It's not worth pissing her off. )"
    hide player with dissolve
    return

label jenny_bed_night_sex_intro:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
        $ game.timer.tick(3)
    scene expression player.location.background_closeup with None
    show player f_thinking a_dressed_thinking with dissolve
    player_name "( Surely she won't get mad at me now, right? )"
    player_name "( I mean, she's been climbing into MY bed in the middle of the night... Why can't I do the same? )"
    show player f_grin
    menu:
        "Do it.":
            call expression game.dialog_select("jenny_bed_night_sex_do_it")
        "I'd better not" if store._in_replay is None:
            call expression game.dialog_select("jenny_bed_night_better_not")
    return

label jenny_bed_night_sex_do_it:
    if store._in_replay is not None or M_jenny.get("bed_sex_first_time"):
        $ M_jenny.set("bed_sex_first_time", False)
        scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
        show jenny b_sleep_side o_sleep_blanket a_sleep_side f_sleep_side_sleeping
        show player b_sleep_climb a_empty f_empty at Position (align=(0,0)) with dissolve
        pause
        show player b_sleep_side f_sleep_side_shy o_sleep_side_boxers
        show expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
        show jenny o_empty
        show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 3
        with dissolve
        pause
        show player b_sleep_cuddle f_sleep_cuddle_side_shy o_empty a_empty
        hide expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
        with dissolve
        pause
        show jenny f_sleep_side_wake
        jen "Hmm?"
        show jenny b_sleep_turn a_sleep_turn f_sleep_turn_angry_talk o_sleep_panties with dissolve
        jen "{b}[firstname]{/b}?"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "H-hi."
        show player f_sleep_cuddle_side_shy
        pause
        show jenny f_sleep_turn_angry_talk
        jen "What the fuck are you doing?"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "Uhh, going to bed?"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "Go get in your own bed, loser!"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "Aww, c'mon {b}[jen_name]{/b}... You climb into my bed all the time!"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "Yeah, because I wanna fuck... Not to cuddle up and slobber all over you while you're trying to sleep."
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "I don't slobber..."
        show player f_sleep_cuddle_side_shy
        show jenny b_sleep_side a_sleep_side f_sleep_side_tired_talk with dissolve
        jen "Yeah, right."
        show jenny f_sleep_side_sleeping
        pause
        show jenny b_sleep_turn a_sleep_turn f_sleep_turn_normal with dissolve
        jen "..."
        show jenny f_sleep_turn_normal_talk
        jen "Fine, just hurry it up!"
        show jenny f_sleep_turn_normal
        player_name "Hmm?"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_normal_talk
        jen "I'm tired, {b}[firstname]{/b}!"
        jen "So, if you're going to fuck me then hurry up and do it already... Otherwise get the fuck out!"
        show jenny b_sleep_side a_sleep_side f_sleep_side_sleeping with dissolve
        show player f_sleep_cuddle_side_shock
        menu:
            "Forget it." if store._in_replay is None:
                show player b_sleep_leave a_empty f_empty
                show jenny b_sleep_turn a_sleep_turn f_sleep_turn_normal o_sleep_blanket
                hide expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png"
                with dissolve
                player_name "Fine, just forget it..."
                hide player with dissolve
                show jenny f_sleep_turn_normal_talk
                jen "Gladly."
                $ player.go_to(L_home_hallway)
                $ game.main()
            "Okay.":

                show player f_sleep_cuddle_side_shy_talk
                player_name "O-okay."
                show player f_sleep_cuddle_side_shy
                pause
                show player f_sleep_cuddle_side_shy_talk
                player_name "Umm..."

                label jenny_bed_night_grope_in_bed:
                    show player f_sleep_cuddle_side_kiss b_empty
                    show jenny b_sleep_side_grope
                    with dissolve
                    pause
                    jen "Mmm."
                    show player b_sleep_side f_sleep_side_shy o_sleep_side_boxers_boner
                    show expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
                    show jenny b_sleep_turn a_sleep_turn_remove_top1 f_sleep_turn_normal
                    with dissolve
                    pause
                    show jenny b_sleep_turn_shirtup a_sleep_turn_remove_top2
                    with dissolve
                    player_name "..."
                    show jenny b_sleep_side_shirtup a_sleep_side f_sleep_side_normal with dissolve
                    pause
                    show player f_sleep_cuddle_side_kiss b_empty o_empty a_empty
                    hide expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
                    show jenny b_sleep_side_grope_shirtup f_sleep_side_enjoy
                    with dissolve
                    pause
                    jen "Okay, that feels really good..."
                    show jenny b_sleep_side_grope_hump_shirtup
                    show jenny f_sleep_side_rolleye
                    jen "Ngghhh!"
                    pause
                    show player f_sleep_cuddle_side_shy_talk
                    player_name "You glad I woke you up yet?"
                    show player f_sleep_cuddle_side_shy
                    show jenny f_sleep_side_tired_talk
                    jen "Shut up..."
                    show player f_sleep_cuddle_side_kiss
                    show jenny f_sleep_side_enjoy
                    pause
                    menu jenny_bed_night_whatcha_do:
                        "Go further.":
                            jump jenny_bed_night_go_further
                        "Continue.":
                            pause
                            jump jenny_bed_night_whatcha_do
    else:

        scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
        show jenny b_sleep_side o_sleep_blanket a_sleep_side f_sleep_side_sleeping
        show player b_sleep_climb a_empty f_empty at Position (align=(0,0)) with dissolve
        pause
        show player b_sleep_cuddle f_sleep_cuddle_side_shy
        show jenny o_empty
        show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 3
        with dissolve
        show jenny f_sleep_side_wake
        jen "Hmm?"
        show jenny b_sleep_turn a_sleep_turn f_sleep_turn_angry_talk o_sleep_panties with dissolve
        jen "{b}[firstname]{/b}?"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "H-hi."
        show player f_sleep_cuddle_side_shy
        pause
        show jenny f_sleep_turn_angry_talk
        jen "This shit again?"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "I thought you liked it?"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "What the fuck gave you that idea?"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "S-so, you didn't like it?"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "That's not-"
        show jenny f_sleep_turn_angry
        pause
        show jenny f_sleep_turn_angry_talk
        jen "Nevermind, just hurry it up, would you?!"
        show jenny b_sleep_side a_sleep_side f_sleep_side_sleeping with dissolve
        jump jenny_bed_night_grope_in_bed


label jenny_bed_night_go_further:
    show player b_sleep_side f_sleep_side_shy o_sleep_side_boxers_boner
    show expression "characters/player/layeredimage/player_arms_a_sleep_side_normal.png"
    show jenny b_sleep_turn_shirtup o_sleep_panties f_sleep_turn_normal_talk
    with dissolve
    jen "Alright, that's enough foreplay."
    show jenny a_sleep_turn_remove1 o_empty f_sleep_turn_normal with dissolve
    pause
    show player a_sleep_side_remove1_boner f_sleep_side_normal o_empty zorder 1
    show jenny a_sleep_turn_remove2 zorder 2
    with dissolve
    pause
    show player b_sleep_side a_sleep_side_remove2
    show jenny a_sleep_turn o_sleep_panties_down
    with dissolve
    pause
    show player a_sleep_side_insert o_sleep_side_boxers_down with dissolve
    pause
    scene expression "backgrounds/location_home_jennybedroom_sex_sleep.jpg"
    show jenny_sleeping_sex default
    show jenny_sleeping_sex_face normal_talk
    show player_jenny_sleeping_sex pre
    show jenny_sex_sleep_blanket
    with fade
    jen "Put it inside me."
    hide jenny_sleeping_sex_face
    show jenny_sleeping_sex insert
    hide player_jenny_sleeping_sex
    with dissolve
    player_name "Alright."
    show jenny_sleeping_sex 1 with dissolve
    jen "Fuuuuck..."
    $ anim_toggle = True
    $ animated = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_sleeping_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_sleeping_sex at Position(xalign = 0.0, yoffset = 0)
    jump jenny_jenny_bed_sex_loop

label jenny_jenny_bed_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_sleeping_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_sleeping_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_jenny_bed_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_sleeping_sex {}".format(pose_list[pose_counter]) as jenny_sleeping_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_jenny_bed_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_jenny_bed_sex_options

label jenny_jenny_bed_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 25:
        jen "Mmm, that feels good...{p=1}{nw}"
    if animcounter == 1 and randomizer() < 25:
        player_name "Mmhmm.{p=1}{nw}"
    if animcounter == 2 and randomizer() < 25:
        jen "Ahhh!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 25:
        jen "Oh, right there!{p=1}{nw}"
        jen "Yeah!{p=1}{nw}"
    return

label jenny_jenny_bed_sex_cum_outside:
    $ M_jenny.set("jenny_bed_cum_inside", False)
    jen "Don't stop!"
    player_name "I'm going to cum!"
    jen "DON'T STOP!!"
    show jenny_sleeping_sex insert with dissolve
    jen "DON'T-"
    show jenny_sleeping_sex default
    show jenny_sleeping_sex_face cum
    show player_jenny_sleeping_sex cum
    player_name "HNNGGG!!!" with flash
    show jenny_sleeping_sex_face angry_talk
    jen "Oh, what the fuck, {b}[firstname]{/b}!"
    scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
    show jenny b_sleep_after a_empty f_sleep_turn_angry
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 1
    show player f_sleep_cuddle_side_shy b_empty a_empty at Position (align=(0,0))
    with fade
    player_name "Hmm?"
    show jenny f_sleep_turn_angry_talk
    jen "Eugh, it's fucking everywhere!"
    jen "How am I supposed to sleep now?"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "S-sorry..."
    show player f_sleep_cuddle_side_shy
    show jenny f_sleep_turn_angry_talk
    jen "For fucks sake..."
    show jenny f_sleep_turn_angry
    pause
    show jenny f_sleep_turn_angry_talk
    jen "Get out!"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "What?!"
    player_name "Are you serious?"
    show player f_sleep_cuddle_side_shy
    show jenny f_sleep_turn_angry_talk
    jen "Yes, you're disgusting!"
    show jenny f_sleep_turn_angry
    jump jenny_bed_sex_night_end

label jenny_jenny_bed_sex_cum_inside:
    $ M_jenny.set("jenny_bed_cum_inside", True)
    jen "Don't stop!"
    player_name "I'm going to cum!"
    jen "DON'T STOP!!"
    jen "NGGHHH!!!"
    show jenny_sleeping_sex cum
    player_name "HNNGGG!!!" with flash
    show xray_jenny_jenny_bed at Position (align=(0,0))
    show jenny_sleeping_sex cum2
    with dissolve
    pause
    hide xray_jenny_jenny_bed
    show jenny_sleeping_sex pullout
    with dissolve
    jen "Oh, wow!"
    show jenny_sleeping_sex default
    show jenny_sleeping_sex_face normal
    show player_jenny_sleeping_sex after
    with dissolve
    player_name "Haah... Haah..."
    call call_pregnancy_minigame ("jenny_bed_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_bed_sex_cum_inside_post_pregnancy:
    scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
    show jenny b_sleep_after a_empty f_sleep_turn_angry_talk
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 1
    show player f_sleep_cuddle_side_shy b_empty a_empty at Position (align=(0,0))
    with fade
    jen "Did you fucking you cum inside me?"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "Yeah."
    show player f_sleep_cuddle_side_shy
    show jenny f_sleep_turn_angry_talk
    jen "God damnit, {b}[firstname]{/b}!"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "You did say not to stop..."
    show player f_sleep_cuddle_side_shy
    show jenny f_sleep_turn_angry_talk
    jen "You know that's not what I meant!"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "Well, I'm sorry..."
    player_name "We were just really into it and everything felt so good, I-"
    show player f_sleep_cuddle_side_shy
    show jenny f_sleep_turn_angry_talk
    jen "{b}*Sigh*{/b} For fucks sake..."
    jen "Just get out!"
    show jenny f_sleep_turn_angry
    show player f_sleep_cuddle_side_shy_talk
    player_name "What?!"
    player_name "Are you serious?"
    show player f_sleep_cuddle_side_shy
    show jenny f_sleep_turn_angry_talk
    jen "Yes, you're disgusting!"
    show jenny f_sleep_turn_angry
    jump jenny_bed_sex_night_end

label jenny_bed_sex_night_end:
    if M_jenny.get("dominance") > 0:
        show player f_sleep_cuddle_side_normal_talk
        player_name "Would you just chill out?"
        if M_jenny.get("jenny_bed_cum_inside"):
            player_name "Everything will be fine."
        else:
            player_name "It's not like you've never had my semen on you before..."
        show player f_sleep_cuddle_side_normal
        jen "..."
        show player f_sleep_cuddle_side_normal_talk
        player_name "Just shut up and go to sleep, we can deal with it in the morning."
        show player f_sleep_cuddle_side_normal
        show jenny f_sleep_turn_angry_talk
        jen "Fine."
        jen "... Asshole."
        show jenny f_sleep_turn_angry
        scene black with fade
        pause
    else:
        show player f_sleep_cuddle_side_shy_talk
        player_name "C'mon, {b}[jen_name]{/b}..."
        player_name "Can't we just sleep?"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "I don't want you snoring in my ear all night!"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "You're the one who snores!!!"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "Fuck you!"
        show jenny f_sleep_turn_angry
        pause
        show jenny f_sleep_turn_angry_talk
        jen "Fine."
        jen "You big fucking baby!"
        show jenny f_sleep_turn_angry
        show player f_sleep_cuddle_side_shy_talk
        player_name "Thank you!"
        show player f_sleep_cuddle_side_shy
        show jenny f_sleep_turn_angry_talk
        jen "Eugh..."
        show jenny f_sleep_turn_angry
        scene black with fade
        pause
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["17_unlocked"] = True
    jump jenny_bed_sex_sleeping

label jenny_bed_sex_sleeping:
    $ Sleep()
    if M_player.is_set("just wokeup"):
        $ renpy.call(game.dialog_select("player_just_wokeup"), woke_with = M_jenny)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
