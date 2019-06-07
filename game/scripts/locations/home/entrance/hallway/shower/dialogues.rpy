label shower_jenny_pregnant:
    scene expression L_home_shower.background_blur
    show jenny b_towel a_magic_preggo_towel f_gross_down at flip
    show jenny at Position (xpos=500)
    show player f_flirt with dissolve
    pause 1
    show jenny f_gross_down_talk
    jen "{b}*Sigh*{/b} I am never going to forgive him for this shit..."
    show player f_surprised_teeth a_dressed_surprised_up_both with dissolve
    jen "That bastard should be waiting on me twenty-four, seven!"
    show player at Position (xoffset=-100) with dissolve
    jen "Catering to my every need!"
    hide player with dissolve
    jen "Rubbing feet..."
    scene expression L_home_hallway.background_blur
    show player f_worried with dissolve
    player_name "( Yeah, I probably shouldn't go in there right now... )"
    hide player with dissolve
    return

label shower_jenny_peep:
    player_name "( Is she... Masturbating?! )"
    player_name "( Oh, this is awesome! )"
    pause
    player_name "( I wish, I could stand here and keep watching... )"
    pause
    player_name "( I'd better go before she sees me. )"
    return

label shower_jenny_pissed_at_handjob:
    pause
    player_name "( I wonder if she realizes I'm watching her? )"
    pause
    player_name "( Would she even care if I joined her? )"
    player_name "( I mean, after what we've been doing for her camshows, showering together doesn't seem so taboo... )"
    pause
    player_name "( Nah, she'd might freak out and hit me with something. )"
    player_name "( Not worth it. )"
    return

label shower_jenny_blowjob_intro_repeat:
    player_name "( Heh, and there's my cue... )"
    menu:
        "Enter.":
            call scene_shower_with_vfx
            show jenny f_sexy_talk b_shower a_naked_hips
            show player b_naked a_naked_sides f_normal od_naked_dick3
            with fade
            jen "It's about damn time!"
            jen "I didn't think you were ever going to join me!"
            show jenny f_sexy
            show player f_normal_talk
            player_name "Well, here I am..."
            show jenny f_grin_down a_shower_soap1 with dissolve
            player_name "So, what do you wanna-"
            show player f_surprised
            show jenny a_shower_soap2 with dissolve
            pause
            show jenny a_shower_soap3 with dissolve
            pause
            show jenny f_grin b_shower_soaping a_empty with dissolve
            player_name "..."
            show jenny f_grin_talk
            jen "What were you saying?"
            show jenny f_grin
            show player f_worried_talk
            player_name "Was I saying something?"
            show player f_worried
            show jenny f_laugh
            jen "Hahaha!"
            show jenny f_grin
            menu:
                "Blowjob":

                    show jenny f_grin_talk
                    jen "You wanna have a little fun?"
                    show jenny f_grin b_shower a_naked_hips with dissolve
                    show player f_normal_talk
                    player_name "Yes!"
                    show player f_normal
                    if M_jenny.get("dominance") <= 0:
                        show jenny f_grin_talk
                        jen "Well then, you know what comes next..."
                        show jenny f_grin
                        show player f_worried_talk
                        player_name "Do I have to?"
                        show player f_worried
                        show jenny f_grin_talk
                        jen "C'mon, doggy..."
                        jen "You gotta beg for your treat!"
                        show jenny f_grin
                        show player f_worried_talk
                        player_name "{b}*Sigh*{/b}"
                        jump bj_shower_repeat_sub
                    else:
                        show player f_skeptical_talk
                        player_name "And before you ask, I'm not begging!"
                        show player f_skeptical
                        show jenny f_upset_talk
                        jen "Yeah, yeah."
                        jen "I'm well aware."
                        show jenny f_upset
                        call scene_shower_with_vfx_zoom
                        show jenny_shower_bj_mc
                        show jenny_shower_bj pre_talk
                        with fade
                        jen "Just shut up and enjoy, asshole."
                        jump bj_shower_repeat_dom

                "Sex" if M_jenny.finished_inclusive(S_jenny_end):

                    label jenny_shower_sex_intro_replay:
                    if store._in_replay is not None:
                        $ player.location = L_home_shower
                        call scene_shower_with_vfx
                        show jenny f_grin b_shower_soaping a_empty
                        show player b_naked a_naked_sides f_worried od_naked_dick3
                        with fade
                        pause
                    show jenny f_grin_talk b_shower a_naked_hips with dissolve
                    jen "Hmm, I think I deserve the treat today."
                    show jenny f_grin
                    show player f_worried_talk
                    player_name "What do you mean?"
                    show player f_worried
                    show jenny f_grin_talk
                    jen "I mean, you're going to fuck me."
                    show jenny f_grin
                    show player f_surprised
                    player_name "!!!"
                    show player f_normal_talk
                    player_name "Okay, sure!"
                    show player f_normal
                    show jenny b_shower_back a_shower_back_down f_shower_overshoulder_back_look_normal_talk o_shower_back_soap at Position (align=(0,0)) with dissolve
                    jen "Ah ah ah, not so fast!"
                    show player b_side_naked_forward a_side_naked_react f_side_shock_down od_empty zorder 0
                    show jenny b_shower_butt1 f_shower_butt1_talk a_empty o_empty zorder 1
                    with dissolve
                    jen "You wanna stick it in?"
                    jen "You've gotta beg for it!"
                    show jenny b_shower_butt f_empty with dissolve
                    show player f_side_shy_down_talk
                    player_name "Ugh, this again?!"
                    show player f_side_shy_down
                    show jenny b_shower_butt1 f_shower_butt1_talk with dissolve
                    jen "C'mon, loser."
                    jen "Beg your princess!"
                    show jenny b_shower_butt f_empty with dissolve
                    if M_jenny.get("dominance") <= 0:
                        show player f_side_shy_down_talk
                        player_name "{b}*Sigh*{/b}"
                        player_name "Please, {b}Princess [jen_name]{/b}..."
                        show player f_side_shy_down
                        show jenny b_shower_butt1 f_shower_butt1_talk with dissolve
                        jen "Please what?"
                        show jenny f_shower_butt1
                        show player f_side_shy_down_talk
                        player_name "Please, can I stick it inside you?"
                        show player f_side_shy_down
                        show jenny f_shower_butt1_talk
                        jen "Hmm, I think you can do better..."
                        show jenny f_shower_butt1
                        show player f_side_shy_down_talk
                        player_name "PLEASE?!"
                        show player f_side_shy_down
                        show jenny f_shower_butt1_talk
                        jen "Hahahaah!!"
                        jen "Alright, do it!"
                        show jenny_shower_sex 1
                        hide player
                        hide jenny
                        jen "!!!" with hpunch
                        $ animated = True
                        $ anim_toggle = True
                        $ M_jenny.set('sex speed', .12)
                        show expression AnimatedImage("jenny_shower_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
                        jen "Wow, you really are excited!"
                        player_name "Y-yeah!"
                    else:
                        pause
                        show jenny_shower_sex 1
                        hide player
                        hide jenny
                        jen "What the-" with hpunch
                        $ animated = True
                        $ anim_toggle = True
                        $ M_jenny.set('sex speed', .12)
                        show expression AnimatedImage("jenny_shower_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
                        jen "... Oh, Fuuuuuuuuck!"
                        pause
                        jen "I didn't say you could-"
                        player_name "You want me to stop?"
                        jen "NO!"
                        jen "Don't stop!"
                    jump jenny_shower_sex_loop
        "Not Now.":
            player_name "( Hmm, nah... )"
            player_name "( I'm not really in the mood to mess with her today. )"
            pause
            $ renpy.end_replay()
            return

label shower_jenny_blowjob_intro_first:
    if store._in_replay is not None:
        $ player.location = L_home_shower
        call scene_shower_with_vfx
        with None
        $ M_jenny.set('rng', randomizer())
        if M_jenny.get('rng') > 50:
            show jenny b_shower_scene_d1 a_empty f_empty
            pause
            show jenny b_shower_scene_d_rub with dissolve
        else:
            show jenny b_shower_scene_e_rub a_empty f_empty
    player_name "( I wonder if she realizes I'm watching her? )"
    pause
    player_name "( Would she even care if I joined her? )"
    player_name "( I mean, after what we've been doing for her camshows, showering together doesn't seem so taboo... )"
    pause
    player_name "( Nah, she'd might freak out and hit me with- )"
    jen "Are you just gonna stand there and watch?"
    player_name "!!!" with hpunch

    if M_jenny.get('rng') > 50:
        show jenny b_shower a_naked_hips f_sexy_camera at Position (xoffset=-200) with dissolve
    else:
        show jenny b_shower_back f_shower_overshoulder_back_look_normal a_shower_back_down at Position (align=(0,0)) with dissolve
    player_name "Huh?!"
    player_name "I wasn't-"
    if M_jenny.get('rng') > 50:
        show jenny f_sexy_camera_talk at Position (xoffset=-200)
    else:
        show jenny f_shower_overshoulder_back_look_normal_talk
    jen "Hehe, would you just take your clothes off and get in here already!"
    if M_jenny.get('rng') > 50:
        show jenny f_sexy_camera at Position (xoffset=-200)
    else:
        show jenny f_shower_overshoulder_back_look_normal
    player_name "R-really?"
    if M_jenny.get('rng') > 50:
        show jenny f_sexy_camera_talk at Position (xoffset=-200)
    else:
        show jenny f_shower_overshoulder_back_look_normal_talk
    jen "Yes!"
    if M_jenny.get('rng') > 50:
        show jenny f_sexy_camera at Position (xoffset=-200)
    else:
        show jenny f_shower_overshoulder_back_look_normal
    player_name "Okay."
    call scene_shower_with_vfx
    show jenny f_sexy b_shower a_naked_hips
    show player b_naked a_naked_sides f_worried_talk od_naked_dick3
    with fade
    player_name "So, ehh..."
    player_name "Do you need a hand or something?"
    show player f_worried
    show jenny f_grin_talk
    jen "Did you seriously just ask if I needed a hand?"
    show jenny f_grin
    player_name "..."
    show jenny f_laugh
    jen "Pfft, hahahaha!"
    jen "That's so pathetic!"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Shut up!"
    show player f_skeptical
    show jenny f_laugh
    jen "Haha!"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Did you just invite me in to make fun of me?"
    show player f_skeptical
    show jenny f_grin_talk a_shower_soap1 with dissolve
    jen "No."
    jen "I actually was thinking we would mess around a little bit."
    show jenny f_grin_down a_shower_soap2 with dissolve
    pause
    show jenny a_shower_soap3 with dissolve
    show player f_worried_talk
    player_name "{b}*Gulp*{/b} R-really?"
    show player f_worried
    show jenny f_grin_talk a_shower_soap2 o_shower_soap1 with dissolve
    jen "Yeah."
    show jenny f_grin
    pause
    show jenny f_upset_talk a_shower_soap1 with dissolve
    jen "Of course, that was before you fed me that stupid line."
    show jenny f_grin_down a_shower_soap4 with dissolve
    player_name "..."
    show jenny f_grin_talk b_shower_soaping a_empty o_empty with dissolve
    jen "So now, I'm thinking... You'll have to beg for it."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Huh?"
    show player f_skeptical
    pause
    show jenny f_eyeroll b_shower a_naked_hips with dissolve
    jen "You wanna help me wash, don't you?"
    show jenny f_upset
    show player f_worried_talk
    player_name "Y-yes."
    show player f_worried
    show jenny f_grin_talk
    jen "Then be a good doggy and beg!"
    show jenny f_grin
    show player f_worried_talk
    player_name "You want me to beg?"
    show player f_worried
    show jenny f_grin_talk
    jen "Go on."
    show jenny f_grin
    player_name "..."
    if M_jenny.get("dominance") <= 0:
        show player f_worried_talk
        player_name "P-please?"
        show player f_worried
        show jenny f_grin_talk
        jen "Please what?"
        show jenny f_grin
        show player f_worried_talk
        player_name "Please, let me wash you..."
        show player f_worried
        show jenny f_grin_talk
        jen "Now bark like a dog."
        show jenny f_grin
        show player f_worried_talk
        player_name "Seriously?!"
        show player f_worried
        show jenny f_laugh
        jen "Ah ah ah, I said bark!"
        show jenny f_grin
        player_name "..."
        jump bj_shower_repeat_sub
    else:
        show player f_skeptical_talk
        player_name "No way!"
        show player f_skeptical
        show jenny f_grin_talk
        jen "Yes, way!"
        show jenny f_grin
        player_name "..."
        show jenny f_upset_talk
        jen "C'mon {b}[firstname]{/b}, do it!"
        show jenny f_upset
        show player f_skeptical_talk
        player_name "No!"
        show player f_skeptical
        show jenny f_angry_talk
        jen "Beg or get out!"
        show jenny f_angry
        show player f_skeptical_talk
        player_name "Screw this, I'm outta here."
        show player f_skeptical
        show jenny f_angry_talk
        jen "What?!"
        jen "You're seriously going to walk away from me right now?!"
        show jenny f_angry
        show player f_skeptical_talk
        player_name "You know I hate this humiliation stuff, {b}[jen_name]{/b}!"
        player_name "If that's all you brought me in here for, then just forget it!"
        show player f_skeptical
        show jenny f_angry_pouting
        jen "..."
        show jenny f_angry_talk
        jen "Grr, fine!"
        show jenny f_angry
        call scene_shower_with_vfx_zoom
        show jenny_shower_bj_mc
        show jenny_shower_bj pre_look
        with fade
        player_name "!!!"
        show jenny_shower_bj pre_talk
        jen "You really take the fun out of all this!"
        show jenny_shower_bj pre_look
        player_name "W-what are you doing?!"
        show jenny_shower_bj pre_talk
        jen "What the fuck does it look like I'm doing?!"
        jump bj_shower_repeat_dom

label shower_jenny_snoop_around_for_laptop:
    scene expression player.location.background_closeup with None
    show player 17 with dissolve
    player_name "( Hmm, this is {b}my chance to sneak into her room and look through her diary{/b}. )"
    player_name "( I should hurry! )"
    hide player with dissolve
    return

label shower_jenny_snoop_around:
    scene expression player.location.background_closeup with None
    show player 13 with dissolve
    player_name "( Hmm, this is {b}my chance to sneak into her room and look for that camera{/b}. )"
    player_name "( I should hurry! )"
    hide player with dissolve
    return

label shower_mom_sis_check:
    scene shower_cutscene1
    show text "I rushed upstairs towards {b}[jen_name]'s{/b} cursing.\nThe scene upon entering was almost comical. {b}[jen_name]{/b} was absolutely flustered and looked like a drowned rat.\nThe exposed pipe was spouting water all over the place and making quite a mess." at Position(xpos=500, ypos=700)
    with dissolve
    $ renpy.pause()
    hide shower_cutscene1
    hide text
    scene shower2
    show player 11 at left
    show jenny f_upset_talk b_wet a_dressed_hips
    with dissolve
    jen "About time you showed up!"
    show player 10
    show jenny f_upset
    player_name "How did this happen?!"
    show player 11
    show jenny f_upset_talk
    jen "How should I know! Do I look like a plumber to you?! All I did was turn on the sink!"
    show player 12
    show jenny f_upset
    player_name "What am I supposed to do?"
    show player 11
    show jenny f_upset_talk
    jen "Fix it obviously! You're the only man around here after all!"
    show jenny f_gross
    show player 12
    player_name "Fine! I guess I'll head {b}downstairs{/b} and see about shutting off the {b}water valve{/b}..."
    hide player
    hide jenny
    with dissolve
    return

label shower_mom_close_valve:
    scene shower2
    show jenny f_upset_talk b_wet a_dressed_hips
    show player 11 at left
    with dissolve
    jen "The water's still spraying everywhere!"
    jen "Go to the {b}basement{/b} and shut off the water {b}valve{/b}!"
    hide player
    hide jenny
    with dissolve
    return

label shower_mom_pipe_check:
    scene shower2
    show jenny b_wet a_dressed_hips f_upset_talk
    show player 11 at left
    with dissolve
    jen "Looks like you got it. The water stopped."
    show player 12
    show jenny f_upset
    player_name "Yeah, I turned off the water valve. Now what?"
    show player 5
    show jenny f_upset_talk
    jen "What are you asking me for? I don't know, replace it or something?"
    show player 10
    show jenny f_upset
    player_name "I've never worked on anything like this before!"
    show player 5
    show jenny f_upset_talk
    jen "Well you're living in a house with girls now which means you need to learn how to fix these kinda things!"
    show player 10
    show jenny f_gross
    player_name "Okay! Okay! I guess I'll go to {b}CONSUM-R{/b} and see about getting a pipe {b}wrench{/b}."
    show player 212
    player_name "..."
    show player
    show jenny f_normal_low
    pause
    show jenny f_angry
    jen "..."
    show jenny f_angry_talk
    jen "Did you get a good look you little perv?!"
    show player 23
    show jenny f_angry
    player_name "I wasn't-"
    show player 22
    show jenny f_angry_talk
    jen "Oh please, You think I can't tell when someone is staring at my tits?"
    show jenny f_angry
    player_name "..."
    show jenny f_angry_talk
    jen "What's the matter with you?"
    show jenny f_angry
    show player 24
    player_name "I'm sorry, {b}[jen_name]{/b}. I was just-"
    show jenny f_angry_talk
    jen "Oh, shut up!"
    show player 25
    jen "If you're going to stare, at least be a man about it!"
    jen "Denying it or making excuses just makes you look like a wimp."
    jen "No one wants to be checked out by a spineless little wimp!"
    show jenny f_angry
    show player 5
    player_name "..."
    show jenny f_upset_talk at right
    jen "If you had gotten up here to deal with this pipe situation sooner, perhaps I'd be in a better mood."
    jen "... But since you decided to take your sweet time..."
    show jenny f_grin_talk
    jen "I think you should take this..."
    show player 22
    show jenny f_grin_down a_empty b_pull1_wet with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show player 23
    show jenny b_panties f_upset_talk a_panties_shirt with dissolve
    jen "... Downstairs to the wash for me."
    show jenny f_upset
    player_name "( !!! )" with hpunch
    show player 21
    player_name "S-Sure..."
    show jenny a_naked_hips f_angry
    show player 211
    with dissolve
    jen "..."
    show jenny f_angry_talk
    jen "Stop staring and go! I don't want to wait around all day for you to {b}fix that pipe{/b}!"
    show jenny f_angry
    show player 22 with dissolve
    player_name "( !!! )"
    hide player with dissolve
    pause
    show jenny f_grin_talk
    jen "Heh, I knew it!"
    jen "That little loser has a thing for me!"
    hide jenny with dissolve
    hide shower2
    return

label shower_mom_fix_pipe_no_wrench:
    scene shower2
    show player 11 at left
    if not game.timer.is_dark():
        show jenny f_upset_talk b_panties a_naked_hips
        with dissolve
        jen "Are you finally going to fix the sink?"
        jen "Hurry it up already!"
        hide jenny with dissolve
        show player 4
    with dissolve
    player_name "( I need a {b}wrench{/b} to fix the broken pipe. )"
    hide player
    with dissolve
    return

label shower_mom_fix_pipe_wrench:
    scene expression "backgrounds/location_home_bathroom_cutscene02.jpg"
    show expression FilteredText("Once I got back home I headed upstairs to fix the bathroom sink.\nI replaced the joint with a new length of pipe and tightened it as much as I could.\nIt kind of felt weird having {b}[deb_name]{/b} and {b}[jen_name]{/b} watch me the whole time.\nLucky for me, the repairs all went smoothly...") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade

    scene shower2
    show player 203f at right
    show jenny f_upset a_dressed_crossed at flip
    show jenny at Position (xpos=200)
    show debbie 62f at left
    with dissolve
    deb "Wow!!"
    deb "Great work, {b}[firstname]{/b}!"
    show jenny f_upset_talk
    show debbie 61f
    jen "Finally..."
    show jenny f_upset
    show debbie 62f
    deb "Don't be rude, {b}[jen_name]{/b}. It was nice of him to fix this for us..."
    show player 2f
    show debbie 61f
    player_name "Heh, not problem."
    player_name "I was happy to do it."
    player_name "... Besides, {b}[jen_name]{/b} is right. Fixing stuff like this is my responsibility now."
    show player 29f
    show jenny f_gross
    show debbie 62f
    deb "You're going to make some lucky girl a great husband one day!"
    show player 203f
    show debbie 61f
    jen "Pfft..."
    show jenny f_upset_talk
    jen "Don't say things like that, you'll give him a big head!"
    show player 16f
    show jenny f_grin_talk
    jen "He's still a wimp, after all."
    show player 15f
    show jenny f_grin
    show debbie 61f
    player_name "I am not a wimp!"
    show player 16f
    show jenny f_grin_talk
    jen "Hah, whatever, Wimp!"
    show player 1f
    show jenny f_grin
    show debbie 62f
    deb "... Don't listen to her, {b}[firstname]{/b}. She's only teasing you because she thinks you're cute."
    show jenny f_angry_talk
    show debbie 59f
    jen "... As if!"
    show player 11f
    show jenny f_eyeroll
    jen "... Now can you two get out? I've been waiting to shower all day!"
    show jenny f_upset
    show debbie 60f
    show player 1f
    deb "C'mon, {b}[firstname]{/b}. Let's get out of Princess's way before her foul mood infects us."
    show jenny f_grin_talk
    show debbie 59f
    jen "Heh, like calling me \"Princess\" is an insult..."
    hide debbie
    hide jenny
    hide player
    with dissolve
    return

label shower_mom_shower_peek_after:
    scene location_home_hallway_day
    show player 3
    player_name "( {b}[deb_name]'s{/b} body looks real good but I don't want to peek at her too long... )"
    player_name "( It would be really awkward if she caught me. )"
    hide player with dissolve
    return

label shower_mom_shower_peek:
    player_name "( !!! )"
    show debbie_shower 6a_6b_6c
    player_name "( {b}[deb_name]'s{/b} in the shower! )"
    player_name "( Wow... )"
    player_name "( She has such a great body! )"
    player_name "( I can't believe she left the door cracked like this! "
    player_name "( I can see everything! )"
    hide debbie_shower 6a_6b_6c
    scene shower06a
    player_name "..."
    scene shower06d
    player_name "( I'd better go before she sees me. )"
    scene hallway
    show player 79 with dissolve
    player_name "Wow..."
    player_name "I can't believe I'm living with this beautiful woman now!"
    player_name "... It's a shame she only sees me as my {b}Father's{/b} kid."
    show player 78 with dissolve
    player_name "( !!! )"
    show player 81
    player_name "I'd better get back to my room before somebody sees this tent I'm pitching..."
    hide player with dissolve
    return

label shower_mom_walk_in:
    player_name "( Awesome! )"
    show debbie_shower 6a_6b_6c
    pause
    player_name "( I wonder if her breasts feel as soft as her legs. )"
    player_name "( They look... perfect! )"
    hide debbie_shower 6a_6b_6c
    scene shower06a
    pause
    scene shower06d
    player_name "( I wonder what would happen if I just walked in there? )"
    player_name "( She would probably get mad but what if she's ok with it? )"
    show debbie_shower 6a_6b_6c
    player_name "( I could always pretend like I didn't realize she was in the shower... )"
    return

label shower_mom_walk_in_yes:
    player_name "( I can't resist... I'm going in! )"
    hide debbie_shower 6a_6b_6c
    call scene_shower_with_vfx
    show player 5 at left
    show debbie 35b at right
    with dissolve
    deb "( !!! )"
    show player 29 with dissolve
    player_name "Oops!"
    show player 3
    show debbie 35c
    deb "Sweetie, what are you doing in here?!!"
    show debbie 35
    deb "I'm naked!"
    show debbie 34
    show player 42 at Position (xoffset=38) with dissolve
    player_name "Sorry, {b}[deb_name]{/b}! I didn't think anyone was in here!"
    deb "..."
    show debbie 35
    deb "It's...alright.."
    deb "If you need something in the bathroom, just knock."
    deb "I'll be done in a few minutes, okay?"
    show debbie 34
    show player 37 with dissolve
    player_name "Okay..."
    show player 3 with dissolve
    show debbie 35
    deb "Now let me finish my shower, sweetie."
    show debbie 33
    deb "And close the door behind you!"
    show debbie 32
    show player 29
    player_name "Will do!"
    hide player with dissolve
    show debbie 35
    deb "Is this because of the-"
    deb "..."
    deb "The kissing..."
    deb "I should be more careful with him."
    hide debbie with dissolve
    scene hallway
    show player 24 with dissolve
    player_name "( Ugh... That was awkward... )"
    player_name "( Why did I think that was a good idea? )"
    pause
    show player 37 at Position (xoffset=41) with dissolve
    player_name "( I hope she isn't too mad at me. )"
    hide player with dissolve
    return

label shower_mom_walk_in_no:
    player_name "I probably shouldn't."
    player_name "I don't want her to be upset."
    hide debbie_shower 6a_6b_6c
    return

label shower_mom_sex:
    show debbie_shower 6a_6b_6c
    return

label shower_mom_sex_walk_in_pre:
    call scene_shower_with_vfx
    with dissolve
    show debbie 35 at right
    show player 1 at left
    deb "Oh, {b}[firstname]{/b}... I didn't expect you to just barge in like that!"
    show debbie 33
    deb "Though, now that you're here..."
    show debbie 36
    deb "Care to join me, sweetie?"
    hide debbie
    hide player
    show debbies 37 with dissolve
    return

label shower_mom_sex_walk_in_after:
    call scene_shower_with_vfx
    show debbies 37_36 at Position (xpos=474)
    pause 4.8
    show debbies 35
    player_name "I love showering with you, {b}[deb_name]{/b}"
    show debbies 76 with dissolve
    pause .1
    show debbies 41_76
    pause 4
    show debbies 42 at Position (xoffset=38)
    deb "Can I help you down here too?"
    show debbies 43 at Position (xoffset=38)
    deb "So..."
    show debbies 44 at Position (xoffset=38)
    deb "What do you have planned today?"
    show debbies 43 at Position (xoffset=38)
    deb "Something fun?"
    show debbies 72_71 at Position (xoffset=38)
    pause 4
    show debbies 45 at Position (xoffset=38) with dissolve
    deb "You're all hard. It's up to you now, sweetie..."
    show debbies 73 at Position (xoffset=38) with dissolve
    return

label shower_mom_sex_wash:
    player_name "I want to wash you this time."
    show debbies 50 with dissolve
    deb "Go ahead, sweetie."
    show debbies 51
    pause 1
    show debbies 52_53_52_51
    pause
    show debbies 54
    player_name "So soft..."
    return

label shower_mom_sex_wash_handjob:
    show debbies 45 with dissolve
    pause .4
    show debbies 73_74
    pause
    show debbies 73
    player_name "{b}[deb_name]{/b}, I'm gonna..."
    show debbies 47 at Position(xpos=526,ypos=768)
    player_name "HNNGGG!!!"
    show white zorder 4 with dissolve
    show debbies 47 at Position(xpos=526,ypos=768)
    show playersex 33 zorder 3 at Position(xpos=610,ypos=880)
    hide white with dissolve
    pause
    show debbies 48
    hide playersex
    with dissolve
    deb "Mmm, good boy."
    return

label shower_mom_sex_finger:
    player_name "I haven't washed {b}everywhere{/b} yet..."
    show debbies 55 at Position(xpos=688,ypos=768) with dissolve
    pause .35
    show debbies 56_55
    pause 4
    deb "... I'm almost there, sweetie..."
    show debbies 56
    deb "I-Aaaaah!!!"
    show debbies 50 at Position(xpos=498,ypos=768) with dissolve
    deb "How do you always know exactly where to rub?"
    show debbies 49
    player_name "I dunno, just a feeling I guess?"
    show debbies 50
    return

label shower_mom_sex_blowjob:
    show debbies 111 with dissolve
    deb "How about a special treat?"
    show debbies 110
    player_name "Yes, please..."
    show debbies 112 at Position(xpos=512) with dissolve
    pause .3
    show expression AnimatedImage("debbies", [113,114], M_mom) as debbies at Position(xpos=513) with dissolve
    $ animated = True
    call screen debbie_shower_blowjob_options

label debbie_shower_blowjob_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbies", [113,114], M_mom) as debbies at Position(xpos=513) with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("debbie_shower_blowjob_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [113,114]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xpos=513) with dissolve
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("debbie_shower_blowjob_hscene_dialog")
        $ animcounter += 1
    call screen debbie_shower_blowjob_options

label debbie_shower_blowjob_hscene_dialog:
    if animcounter == 1 and randomizer() < 25:
        player_name "Oh, god!{p=1}{nw}"
    if animcounter == 4 and randomizer() < 25:
        player_name "I can't-{p=1}{nw}"
    return

label debbie_shower_blowjob_cum_in:
    show debbies 113 at Position(xpos=513)
    pause .3
    show debbies 116 at Position(xpos=517)
    player_name "HNNGGG!!!"
    deb "( !!! )"
    show white with dissolve
    hide white with dissolve
    pause
    show debbies 117 at Position(xpos=523) with dissolve
    deb "HMMPH!!!"
    show debbies 118 at Position(xpos=516)
    deb "{b}*Gulp*{/b}"
    show debbies 115 at Position(xpos=531)
    deb "... Oh, that was a lot!"
    show debbies 110 at Position(xpos=512)
    player_name "Sorry, {b}[deb_name]{/b}."
    show debbies 111
    deb "No, don't apologize, sweetie."
    deb "I love the taste!"
    return

label debbie_shower_blowjob_cum_out:
    show debbies 113 at Position(xpos=513)
    pause .3
    show debbies 116 at Position(xpos=517)
    player_name "HNNGGG!!!"
    deb "( !!! )"
    show white with dissolve
    show debbies 115 at Position(xpos=531)
    show playersex 74 at Position(xpos=530,ypos=519)
    hide white with dissolve
    pause
    show playersex 75 at Position(xpos=574,ypos=655)
    deb "Heheh, look at the mess you made of my face!"
    deb "... I’m covered..."
    player_name "Sorry, {b}[deb_name]{/b}."
    deb "It’s okay!"
    deb "We're in the shower so it's easy to clean off!"
    deb "... Just help me get it out of my hair."
    return

label shower_mom_sex_already_fingered:
    show debbies 49
    player_name "Can I put it in?"
    show debbies 50
    deb "Sweetie, I just came... It's a little too sensitive right now..."
    deb "I'll finish you off with my hand."
    return

label shower_mom_sex_fuck_pre:
    show debbies 49 with dissolve
    if randomizer() <= 33:
        player_name "{b}[deb_name]{/b}..."
        player_name "Can I put it inside you?"
        show debbies 50
        deb "Of course, sweetie..."
        show debbies 57 at Position(xpos=688,ypos=768) with dissolve
        deb "Oh, I've been waiting all day for this..."
    elif randomizer() <= 66:
        player_name "{b}[deb_name]{/b}, I want to do it with you."
        show debbies 50
        deb "Oh, sweetie..."
        deb "You are insatiable."
        deb "Hold my leg and give me that big cock!"
        show debbies 57 at Position(xpos=688,ypos=768) with dissolve
        pause
    else:
        player_name "{b}[deb_name]{/b}, I want you."
        show debbies 50
        deb "I was hoping you would."
        deb "Give me that beautiful cock of yours."
        show debbies 57 at Position(xpos=688,ypos=768) with dissolve
        pause
    show debbies 58 with dissolve
    deb "Haah!"
    show debbies 59 with dissolve
    pause
    return

label mom_shower_sex_loop:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbies", [59,60,61], M_mom) as debbies at Position(xpos = 688,ypos = 768)
                $ animated = True
            pause 5
            if animcounter in [1,2,3]:
                call expression game.dialog_select("debbie_shower_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [59,60,61]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xpos = 688,ypos = 768)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,2,3]:
                call expression game.dialog_select("debbie_shower_hscene_dialog")
        $ animcounter += 1
    call screen shower_mom_sex_options

label debbie_shower_hscene_dialog:
    if randomizer() <= 33:
        if animcounter == 1:
            deb "Ahhhh!!!{p=1}{nw}"
            deb "Give it to me, sweetie!{p=2}{nw}"
        elif animcounter == 3:
            deb "Cum for me!{p=2}{nw}"
    elif randomizer() <= 66:
        if animcounter == 1:
            deb "Ohh!!{p=1}{nw}"
        elif animcounter == 2:
            deb "Sweetie! Deeper!{p=2}{nw}"
        elif animcounter == 3:
            player_name "{b}[deb_name]{/b}, I love you!{p=2}{nw}"
            deb "I love you too!{p=2}{nw}"
    else:
        if animcounter == 2:
            player_name "I love the way your tits bounce.{p=2}{nw}"
            deb "Yeah, well I love your huge cock!{p=2}{nw}"
        elif animcounter == 3:
            deb "Ahh!!{p=1}{nw}"
            deb "Yes, that's the spot!{p=2}{nw}"
    return

label mom_shower_sex_cum:
    call expression game.dialog_select("mom_shower_sex_cum_pre")
    $ cum = True
    call expression game.dialog_select("mom_shower_sex_cum_after")
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["07_unlocked"] = True
    jump expression game.dialog_select("mom_shower_end")

label mom_shower_sex_cum_pre:
    if randomizer() <= 33:
        player_name "UHHH!"
    elif randomizer() <= 66:
        deb "Give it to me, sweetie!"
        deb "Cum deep inside me!"
    else:
        deb "HAAAAAHH!"
    return

label mom_shower_sex_cum_after:
    show debbies 60
    show white zorder 4 with dissolve
    hide white with dissolve
    pause
    if randomizer() <= 50:
        player_name "That felt good..."

    show playersex 53 zorder 3 at Position(xpos=663,ypos=632)
    show debbies 57
    with dissolve
    if randomizer() <= 50:
        deb "You let out so much..."
        deb "Such a mess."
        deb "Good thing we're in the shower..."
    else:
        deb "Ohh!"
        deb "God, I love this cock of yours!"
        player_name "Hehe, I'm pretty sure it feels the same way about you..."
        deb "Ha Ha Ha!"
        deb "Hold on to me for a second. My legs are a little wobbly after all that!"
    return

label mom_shower_end_dialogue:
    hide playersex
    hide debbies
    show debbies 34 at Position(xpos=474,ypos=768)
    with dissolve
    if randomizer() <= 50:
        deb "That was fun but I should really get back downstairs and start dinner."
        deb "We'll do this again, okay?"
        deb "Make sure {b}[jen_name]{/b} doesn't see you leave the bathroom, okay?"
    else:
        deb "I hope {b}[jen_name]{/b} didn't hear us..."
        show debbies 35
        player_name "I doubt it. Not with the shower running..."
        show debbies 34
        deb "... Yeah, I suppose I'm worrying too much."
        deb "I should get downstairs and start cooking dinner..."
        deb "Fetch me a towel?"
        show debbies 35
        player_name "Sure thing, {b}[deb_name]{/b}!"
    hide debbie_shower
    hide debbie
    hide debbies
    hide player
    with dissolve
    return

label mom_shower_end:
    call expression game.dialog_select("mom_shower_end_dialogue")
    $ renpy.end_replay()
    $ game.timer.tick()
    $ playSound()
    jump expression game.dialog_select("hallway_dialogue")

label shower_mom_sex_leave:
    player_name "I probably shouldn't."
    player_name "I don't want her to be upset."
    return

label shower_jenny_shower_spy_repeat:
    call scene_shower_with_vfx_peep
    $ M_jenny.set('rng', randomizer())
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1_blurred f_empty a_empty
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1_blurred f_empty a_empty
    else:
        show jenny b_shower_scene_c1_blurred f_empty a_empty
    with dissolve
    pause
    player_name "( Hmm, it's so steamy... )"
    player_name "( I can't quite make out- )"
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1
    else:
        show jenny b_shower_scene_c1
    show bathroom_door_left at Position (xoffset=-50)
    show bathroom_door_right at Position (xoffset=50)
    with dissolve
    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        player_name "( Hello, {b}[jen_name]{/b}... )"
    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        player_name "( Oh, here we go. )"
        player_name "( I hope I haven't missed the show! )"
    elif M_jenny.finished_state(S_jenny_talked_to_cedric):
        player_name "( Hehe, it's {b}[jen_name]{/b} again! )"
    else:
        player_name "( Whoa!! )"
        player_name "( It's {b}[jen_name]{/b}! )"
    pause

    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a2
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b2
    else:
        show jenny b_shower_scene_c2
    with dissolve

    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        player_name "( I can't believe how much has happened between us! )"
        player_name "( A few weeks ago she would have freaked out about this but now... )"
    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        pause
    elif M_jenny.finished_state(S_jenny_talked_to_cedric):
        player_name "( She should take her webcam in there with her, she'd probably make a fortune... )"
        pause
    else:
        player_name "( Oh man, she would be so pissed if she knew I was spying on her! )"
        pause

    if M_jenny.get('rng') > 75:
        show jenny b_shower_scene_a3
    elif 75 > M_jenny.get('rng') > 50:
        show jenny b_shower_scene_b3
    elif 50 > M_jenny.get('rng') > 25:
        show jenny b_shower_scene_c3
    else:
        show jenny b_shower_scene_e3
    with dissolve

    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        player_name "( I can just walk in there and join her, whenever I want! )"
    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        player_name "( C'mon {b}[jen_name]{/b}, you know you want to... )"
    elif M_jenny.finished_state(S_jenny_talked_to_cedric):
        player_name "( Mmm, I could watch her scrub that body all- )"
    else:
        player_name "( It's a shame she's such a bitch all the time... )"
        player_name "( With a body like that, she could probably get any guy she wants. )"
        pause
        player_name "( I should get out of here before she catches me. )"
        pause
        scene black with fade
        jump jenny_shower_peep_end

    if M_jenny.get('rng') > 50:
        show jenny b_shower_scene_d1
    else:
        show jenny b_shower_scene_e_rub

    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        pause
    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        player_name "( Bingo! )"
    else:
        player_name "( !!! )" with hpunch

    if M_jenny.get('rng') > 50:
        show jenny b_shower_scene_d_rub with dissolve
    return

label shower_jenny_shower_spy:
    call scene_shower_with_vfx_peep
    $ M_jenny.set('rng', randomizer())
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1_blurred f_empty a_empty
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1_blurred f_empty a_empty
    else:
        show jenny b_shower_scene_c1_blurred f_empty a_empty
    with dissolve
    pause
    player_name "( Hmm, it's so steamy... )"
    player_name "( I can't quite make out- )"
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1
    else:
        show jenny b_shower_scene_c1
    show bathroom_door_left at Position (xoffset=-50)
    show bathroom_door_right at Position (xoffset=50)
    with dissolve
    player_name "( Whoa!! )"
    player_name "( It's {b}[jen_name]{/b}! )"
    pause
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a2
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b2
    else:
        show jenny b_shower_scene_c2
    with dissolve
    player_name "( Oh man, she would be so pissed if she knew I was spying on her! )"
    pause
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a3
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b3
    else:
        show jenny b_shower_scene_c3
    with dissolve
    player_name "( Just look at that body though! )"
    player_name "( She's like a perfect- )"
    show jenny b_shower_caught_front_surprised
    player_name "( !!! )" with hpunch
    jen "What the fuck, {b}[firstname]{/b}!!!"
    player_name "( Uh oh... )"

    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 6 at left
    show jenny b_towel a_towel_hit f_angry_talk at Position (xpos=350)
    with dissolve
    jen "You!"
    show jenny f_angry a_towel_hit2 with dissolve
    player_name "Ack!"
    show jenny f_angry_talk a_towel_hit with dissolve
    jen "Little!"
    show jenny f_angry a_towel_hit2 with dissolve
    player_name "Ow!!"
    show jenny f_angry_talk a_towel_hit with dissolve
    jen "PERVERT!!!"
    show jenny f_angry a_towel_hit2 with dissolve
    player_name "Ouch!!"
    show player 12
    show jenny a_towel_hit
    with dissolve
    player_name "Stop hitting me!!!"
    show player 90
    hide jenny
    show jenny b_towel f_angry_talk a_towel_hips with dissolve
    jen "What the hell is the matter with you?!"
    show jenny f_angry
    show player 12
    player_name "Nothing, I just saw the door cracked and I-"
    show player 24
    show jenny f_angry_talk
    jen "... And you what?!"
    jen "Thought it was alright to peep on people in the shower?!"
    show jenny f_angry
    show player 25
    player_name "It's not like that..."
    show jenny f_gross
    pause
    show player 24
    pause
    player_name "Well, okay. It's a little like that but..."
    show jenny f_angry_talk
    jen "It's exactly like that, you pathetic little-"
    show jenny f_angry
    show player 10
    player_name "I'm sorry, alright?!"
    show player 5
    pause
    show jenny f_angry_talk
    jen "{b}*Sigh*{/b} Just get outta here or I'm telling {b}[deb_name]{/b}!"
    show jenny f_angry
    show player 23
    player_name "No, no, please don't tell {b}[deb_name]{/b}!"
    player_name "I'm leaving right now!"
    hide player with fastdissolve
    pause
    show jenny f_gross
    jen "( Grr, he's such a freaking loser! )"
    jen "( I just wanna wring his stupid neck! )"
    hide jenny with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
