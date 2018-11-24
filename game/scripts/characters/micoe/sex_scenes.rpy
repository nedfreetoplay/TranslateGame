label micoe_bj_scene_repeatable:
    scene expression "backgrounds/location_hospital_room_blur.jpg"
    show player 10 at left
    show micoe at flip
    with dissolve
    player_name "Remember when you helped me... Umm, extract my sample for testing."
    show player 5
    show micoe f_sexy_talk
    micoe "You mean, when I sucked your cock in the bathroom?"
    show micoe f_sexy
    show player 11
    player_name "!!!"
    show player 29 with dissolve
    player_name "Y-yeah."
    show player 3
    show micoe f_laugh
    micoe "Hehehe, I think we're past being shy, {b}[firstname]{/b}."
    show micoe f_sexy_talk
    micoe "You here to let me have another taste?"
    show micoe f_sexy
    show player 17 with dissolve
    player_name "Uh huh."
    hide player
    show micoe b_pulling f_empty a_empty
    with dissolve
    micoe "C'mon cutie."

    scene expression "backgrounds/location_hospital_bathroom.jpg"
    show player 13f at right
    show micoe f_sexy_talk
    with dissolve
    micoe "What are you waiting for?"
    micoe "Get that cock out!"
    show micoe f_sexy
    show player 14f
    player_name "O-okay."
    show player 261b with dissolve
    pause
    show player 263b at Position (xoffset=-150)
    show micoe knees
    with dissolve
    pause
    show micoe knees_talk
    micoe "Mmm, I'll suck this beautiful cock anytime you want, {b}[firstname]{/b}!"

    $ M_micoe.set('sex speed', .12)
    $ anim_toggle = True
    $ animated = True
    scene expression "backgrounds/location_hospital_bathroom_closeup.jpg"
    show expression AnimatedImage("micoe_bj", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], M_micoe) as micoe_bj at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    micoe "{b}*Slurp*{/b}"
    player_name "Oh, god..."
    player_name "That feels amazing, {b}Micoe{/b}."
    micoe "Mmhmm!"
    return

label micoe_bj_scene:
    scene expression "backgrounds/location_hospital_bathroom.jpg"
    show player 691b with dissolve
    player_name "Alright, she said I just need to ejaculate into this cup..."
    show player 261bf with dissolve
    pause
    $ M_player.set("sex speed", .4)
    show player 694_694b with dissolve
    pause
    player_name "( C'mon. )"
    pause
    pause
    player_name "..."
    pause
    pause
    player_name "( Hmm, it usually doesn't take me this long... )"
    pause
    $ M_player.set("sex speed", .3)
    show player 694_694b
    pause
    player_name "( Come on you stupid thing! )"
    "*{b}Knock, knock{/b}*"
    show player 695 with hpunch
    player_name "!!!"
    show player 692d
    player_name "Y-yeah?"
    show player 692c
    micoe "Everything alright in there, tiger?"
    show player 692d
    player_name "I uhh..."
    player_name "I'm not sure."
    show player 692c
    micoe "Problem?"
    show player 692d
    player_name "Umm... Stage fright, I guess?"
    show micoe at flip
    show micoe at Position (xpos=200)
    with dissolve
    show player 692d
    player_name "Whoa, what are you-"
    show player 692c
    show micoe f_normal_talk
    micoe "Shh, let me have a look..."
    show micoe f_normal
    show player 692d
    player_name "No, really that's-"
    hide player
    show micoe b_jerk1 a_empty at unflip
    show micoe at Position (xpos=26)
    player_name "!!!" with hpunch
    show micoe f_normal_talk
    micoe "Wow, you are one gifted kid!"
    show micoe b_jerk
    micoe "That girlfriend of yours is a lucky lady!"
    show micoe f_normal
    player_name "..."
    player_name "!!!"
    show micoe f_normal_talk b_dressed a_dressed_front
    show player 263c at right
    with dissolve
    micoe "There we go."
    show micoe f_laugh
    micoe "Problem solved!"
    show micoe f_normal
    show player 262b
    player_name "Heh."
    show player 263c
    show micoe f_normal_talk
    micoe "I'll leave you to it now..."
    show micoe f_normal
    pause
    show micoe f_sexy_talk
    micoe "... Unless, you'd rather I stay here and help?"
    show micoe f_sexy
    show player 262g with dissolve
    player_name "W-what do you mean?"
    show player 262e
    show micoe f_sexy_talk
    micoe "I could stay and provide a little... Medical assistance."
    show micoe f_empty a_dressed_fingersuck with dissolve
    show player 262g
    player_name "O-oh!"
    show player 262e
    pause
    show player 262g
    player_name "I don't..."
    show player 262e
    menu:
        "No.":
            show player 262d with dissolve
            player_name "That's, I... I don't think my friend-"
            player_name "I mean, girlfriend would be happy about that..."
            show player 262c
            show micoe f_sexy_talk a_dressed_front with dissolve
            micoe "She doesn't have to find out."
            show micoe f_sexy
            show player 262d
            player_name "Uhh, really... I'm good."
            show player 262c
            show micoe f_sexy_talk
            micoe "Well, well, handsome and faithful."
            micoe "Alright, I respect that."
            show micoe f_normal_talk_down
            micoe "Mmm, what I'd do to you..."
            show micoe f_normal_down
            player_name "..."
            show micoe f_sexy_talk
            micoe "{b}*Ahem*{/b} I'll be just outside if you change your mind."
            show micoe f_sexy
            show player 262d
            player_name "T-thanks..."
            show player 262c
            hide micoe with dissolve
            pause
            show player 262b
            player_name "Holy crap!"
            player_name "Well, I'm definitly hard now."
            player_name "I'd better get back to work."
            show player 263c
            scene black with fade
            pause

            scene expression "backgrounds/location_hospital_room_blur.jpg"
            show micoe f_normal
            show player 691df at right
            with dissolve
            player_name "Here you go."
            show player 691cf
            show micoe f_laugh
            micoe "Good lord!"
            $ renpy.end_replay()
            call expression game.dialog_select("diane_check_up_results")

            $ M_diane.trigger(T_diane_cup_o_jizz)
            $ player.go_to(L_hospital_floor2)
            $ game.main()
        "Yes.":

            show player 263c
            player_name "..."
            show player 262b
            player_name "Okay."
            show player 263c
            show micoe f_sexy_talk
            micoe "Oh, I was hoping you'd say that!"
            show micoe knees_talk with dissolve
            show player 263b
            micoe "I wanted you the second I saw you in that waiting room."
            show micoe knees
            show player 262h
            player_name "You did?"

            scene expression "backgrounds/location_hospital_bathroom_closeup.jpg"
            show micoe_bj look
            with dissolve
            micoe "Mmmhmm."
            show micoe_bj talk
            micoe "... And then I saw this massive dick you were hiding and I could barely control myself!"
            show micoe_bj look
            player_name "You're really forward, you know that?"

            $ anim_toggle = True
            $ animated = True
            $ M_micoe.set('sex speed', .12)
            show expression AnimatedImage("micoe_bj", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], M_micoe) as micoe_bj at Position(xalign = 0.0, yoffset = 0)
            player_name "!!!" with hpunch
            player_name "REALLY, REALLY FORWARD!!"
            micoe "Mmmhmmph!"
            jump micoe_bj_loop

label micoe_bj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("micoe_bj", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], M_micoe) as micoe_bj at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("micoe_bj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "micoe_bj {}".format(pose_list[pose_counter]) as micoe_bj at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("micoe_bj_hscene_dialog")
        $ animcounter += 1
    call screen micoe_bj_options

label micoe_bj_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        player_name "Holy crap!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 50:
        micoe "{b}*Slurp*{/b}{p=1}{nw}"
    if animcounter == 2 and randomizer() < 50:
        player_name "You're really good at this!{p=2}{nw}"
    if animcounter == 3 and randomizer() > 50:
        player_name "I'm getting close...{p=2}{nw}"
        if M_micoe.get("sex speed") > 0.061:
            $ M_micoe.set("sex speed", M_micoe.get("sex speed") - 0.03)
        player_name "Oh my god!{p=1}{nw}"
    return

label micoe_bj_cum:
    if M_diane.is_state(S_diane_jizz_checkup_extra_hand):
        player_name "Ahh, here it comes!"
        pause
        show micoe_bj cum
        player_name "HNNGGG!!!" with flash
        pause
        player_name "Haah... Haah..."
        pause

        scene expression "backgrounds/location_hospital_bathroom.jpg"
        show player 263c at right
        show micoe f_full a_dressed_cup1
        with dissolve
        pause
        show micoe f_spit a_dressed_cup2 with dissolve
        micoe "{b}*Spit*{/b}"
        show micoe f_laugh a_dressed_cup3 with dissolve
        micoe "Mmm, tastes pretty fertile to me!"
        show micoe f_sexy
        show player 262b
        player_name "That was incredible!"
        show player 263c
        show micoe f_sexy_talk
        micoe "Thank you."
        micoe "Come back and we'll do it again sometime, yeah?"
        show micoe f_sexy
        show player 262b
        player_name "Y-yeah, okay."
        show player 263c
        show micoe f_laugh
        micoe "Hehe."
        hide micoe with dissolve
        pause
        show player 261b with dissolve
        pause
        hide player with dissolve

        scene expression "backgrounds/location_hospital_room_blur.jpg"
        call expression game.dialog_select("diane_check_up_results")
        $ M_diane.trigger(T_diane_cup_o_jizz)
    else:

        player_name "Oh, shit."
        pause
        player_name "I'm gonna cum!"
        player_name "I'm gonna-"
        show micoe_bj cum
        player_name "HNNGGG!!!" with flash
        pause
        player_name "Haaah... Haah..."
        show micoe_bj mouth_full with dissolve
        micoe "Ahhh."
        show micoe_bj look with dissolve
        micoe "Mmm."
        show micoe_bj talk with dissolve
        micoe "Hehehe!"

        scene expression "backgrounds/location_hospital_bathroom.jpg"
        show player 261b at right
        show micoe
        with dissolve
        pause
        show player 14f
        player_name "Wow, you swallowed it!"
        show player 13f with dissolve
        show micoe f_sexy_talk
        micoe "I know..."
        micoe "I'm a naughty girl, aren't I?"
        show micoe f_sexy
        show player 29f with dissolve
        player_name "Y-yes..."
        show player 13f with dissolve
        show micoe f_laugh
        micoe "Hehehe!"
        show micoe f_sexy
        pause
        show micoe f_sexy_talk
        micoe "Alright, cutie."
        micoe "I should get back to work."
        show micoe f_sexy
        show player 14f
        player_name "Okay."
        show player 13f
        show micoe f_sexy_talk
        micoe "Come back and see me soon though, okay?"
        show micoe f_sexy
        show player 14f
        player_name "I will."
        hide micoe
        show player 13 at left
        with dissolve
        pause
        show player 29 with dissolve
        player_name "... Wow!"
        hide player with dissolve
        $ game.timer.tick()
    $ persistent.cookie_jar["Micoe"]["unlocked"] = True
    $ persistent.cookie_jar["Micoe"]["gallery"]["01_unlocked"] = True
    $ renpy.end_replay()
    $ player.go_to(L_hospital_floor2)
    $ game.main()

label diane_check_up_results:
    show player 13f at right
    show micoe f_normal_talk a_dressed_cup3
    with dissolve
    micoe "I've never seen anyone fill the entire cup!"
    show micoe f_normal
    show player 14f
    player_name "Heh, yeah."
    show player 13f
    show micoe f_normal_talk
    micoe "I'll get it up to the lab right away."
    micoe "If you wanna just wait here, your girlfriend should be back pretty soon."
    show micoe f_normal
    show player 14f
    player_name "Alright, thanks."
    show player 13f
    show micoe a_dressed_front at flip
    show micoe at Position (xpos=100)
    with dissolve
    pause
    hide micoe
    show micoe f_normal_talk
    with dissolve
    micoe "You know, if things with your girlfriend ever go south."
    show micoe f_sexy_talk
    micoe "You should come back and see me."
    micoe "I'll rock your world, kiddo."
    show micoe f_wink
    show player 29f with dissolve
    player_name "Y-yeah, okay."
    show player 3f at Position (xoffset=-8)
    show micoe f_laugh
    micoe "Hehe, you're so damn cute!"
    show micoe f_sexy
    show player 29f
    player_name "T-thanks."
    show player 3f at Position (xoffset=-8)
    hide micoe with dissolve
    pause
    show player 12f with dissolve
    player_name "Wow, that is one extremely forward woman..."
    show player 13f
    show diane b_gown a_gown_sides f_normal_talk at flip with dissolve
    dia "Hey there, handsome."
    show diane f_normal
    show player 14f
    player_name "Hey, {b}Diane{/b}."
    player_name "What's the verdict?"
    show player 13f
    show diane f_normal_talk
    dia "I'm not sure yet."
    show diane f_normal
    show player 10f
    player_name "Oh?"
    show player 13f
    show diane f_normal_talk
    dia "The nurse is supposed to come back with the results."
    show diane f_normal
    show player 14f
    player_name "Y-yeah, mine too."
    show player 13f
    show diane b_gown_dress a_empty f_down_front with dissolve
    show player 426f
    pause
    show diane b_casual_remove6 f_empty with dissolve
    pause
    show diane b_casual_remove5 f_normal_talk with dissolve
    dia "Everything go alright on your end?"
    show diane b_casual_remove4 f_empty with dissolve
    show player 5f
    player_name "Hmm?"
    show diane b_casual_remove1 with dissolve
    show player 17f
    player_name "Oh, yeah!"
    show diane b_casual a_casual_sides f_normal with dissolve
    show player 14f
    player_name "No, problems."
    show player 13f
    show diane f_normal_talk
    dia "Good."
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "I guess we just need to-"
    show diane f_normal
    "*Knock, knock*"
    show player 14f
    player_name "Come in."
    show player 13f zorder 1 with None
    show diane at unflip
    show diane zorder 0 at Position (xpos=-150)
    show micoe f_normal_talk at Position (xpos=350)
    with dissolve
    micoe "Alright, I've got the results right here."
    show micoe f_normal
    show diane f_sad_talk
    dia "Oh, please be good news..."
    dia "I'm not barren am I?"
    show diane f_sad
    show micoe f_laugh
    micoe "Haha, no sweetie."
    show diane f_normal
    show micoe f_normal_talk
    micoe "You aren't barren."
    micoe "With your age, it won't be easy but you can still definitely concieve."
    show micoe f_normal
    show diane f_normal_talk
    dia "Oh, what a relief!"
    show diane f_normal
    show player 14f
    player_name "What about me?"
    show player 13f
    show micoe f_normal_talk
    micoe "You on the other hand are extremely fertile!"
    micoe "The doctor said he's surprised I didn't get pregnant just carrying the bottle up to the lab."
    show micoe f_laugh
    show diane f_laugh
    show player 17f
    micoe "Haha!"
    dia "Haha!"
    show micoe f_normal
    player_name "..."
    show diane f_normal
    show player 13f
    show micoe f_normal_talk
    micoe "So you two should be good to go."
    show micoe f_normal
    show diane f_normal_talk
    dia "Anything else we should know?"
    show diane f_normal
    show micoe f_normal
    micoe "Just make sure you're having intercourse as often as possible for the best chances."
    show diane f_smirk_talk
    dia "That shouldn't be a problem..."
    show diane f_smirk
    show player 3f at Position (xoffset=-8) with dissolve
    show micoe f_sexy_talk
    micoe "You're a lucky woman."
    show micoe f_sexy
    show diane f_laugh
    dia "Don't I know it!"
    show diane f_normal
    show micoe f_normal
    pause
    show diane f_normal_talk at flip
    show diane at Position (xpos=300)
    with dissolve
    dia "Come on handsome."
    dia "{b}Let's get back home.{/b}"
    dia "I'm exhausted."
    show diane f_normal
    show player 13f with dissolve
    show micoe f_normal_talk with None
    show diane zorder 0 at Position (xpos=-150)
    show diane at flip
    with dissolve
    micoe "Good luck!"
    show micoe f_normal
    show player 14f
    player_name "Thanks!"
    hide player
    hide diane
    hide micoe
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
