label jenny_couch_sex:
    if M_jenny.get("dominance") <= 0:
        hide jenny_couch_dick_rub
        show jenny a_couch_dick3 f_couch_sit_sexy_talk
        jen "Alright, I'm bored of this..."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right
        player_name "Hmm?"
        show player a_couch_boner zorder 1
        show jenny b_couch_remove f_empty a_empty zorder 0
        with dissolve
        pause
        show jenny b_couch_sit f_couch_sit_sexy_talk a_couch_rest o_couch_teasing with dissolve
        jen "Get over here and fuck me."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "What?!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "You heard me."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "B-but, {b}[deb_name]{/b} is right in there!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "I know, it's exciting! Isn't it?"
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "N-no?"
        show player f_couch_sit_right
        show jenny f_couch_sit_eyeroll
        jen "{b}*Sigh*{/b} Yes, it is!"
        show jenny f_couch_sit_sexy
        player_name "..."
        show jenny f_couch_sit_sexy_talk
        jen "Don't be a pussy."
        show jenny f_couch_sit_sexy_talk_down
        jen "I want that big dick!"
        show jenny f_couch_sit_sexy_down
    else:
        show jenny f_couch_sit_sexy_talk_down
        jen "Are you getting close?"
        show jenny f_couch_sit_sexy_down
        show player f_couch_sit_down_talk
        player_name "Y-yes."
        show player f_couch_sit_right
        hide jenny_couch_dick_rub
        show jenny a_couch_dick3 f_couch_sit_sexy_down
        pause
        show player f_couch_sit_right_talk
        player_name "What are you doing?!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "I'm bored of this..."
        show jenny f_couch_sit_sexy
        pause
        show jenny f_couch_sit_sexy_talk
        jen "Let's fuck!"
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Huh?!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "You heard me."
        show player a_couch_boner zorder 1
        show jenny b_couch_remove f_empty a_empty zorder 0
        with dissolve
        pause
        show jenny b_couch_sit f_couch_sit_sexy_talk a_couch_rest o_couch_teasing with dissolve
        jen "I want you inside me."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "B-but, {b}[deb_name]{/b} is right in there!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "So?"
        jen "I can be quiet."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Yeah, right."
        show player f_couch_sit_right
        show jenny f_couch_sit_upset_talk
        jen "C'mon, please?"
        show jenny f_couch_sit_upset
        show player f_couch_sit_down_surprised
        player_name "!!!"
        show player f_couch_sit_right_talk
        player_name "Did you just say, please?"
        show player f_couch_sit_right
        show jenny f_couch_sit_eyeroll
        jen "... Maybe."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Wow, you really do want it."
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_down
        jen "Mmhmm!"
    show player f_couch_sit_right_talk
    player_name "Fine."
    show player b_couch_remove a_empty f_empty
    with dissolve
    pause
    show player b_couch_jump
    show jenny b_couch_jump o_empty f_empty a_empty
    with dissolve
    jen "Oh, fuuuuck!"
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .09)
    hide jenny
    scene expression "backgrounds/location_home_livingroom_couch_sex.jpg"
    show expression AnimatedImage("jenny_couch_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_couch_sex at Position(xalign = 0.0, yoffset = 0)
    with fade
    player_name "Shhh!"
    player_name "{b}[deb_name]{/b} will freak out if she finds us!"
    jen "I know!"
    jen "It's just so deep, I can't-"
    jump jenny_couch_sex_loop

label jenny_couch_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_couch_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_couch_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_couch_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_couch_sex {}".format(pose_list[pose_counter]) as jenny_couch_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_couch_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_couch_sex_options

label jenny_couch_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jen "Ahh!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "I love your dick so much!{p=2}{nw}"
        jen "Oh, god!!{p=1}{nw}"
        jen "I love it, I love it, I LOVE IT!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "FUUUCK, YES!{p=1}{nw}"
        player_name "Shh!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        jen "C'mon, {b}[firstname]{/b}!{p=1}{nw}"
        jen "Fuck me harder!{p=1}{nw}"
        player_name "Stop pulling on me!{p=2}{nw}"
        if M_jenny.get("sex speed") > 0.061:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jen "Oh, right there!{p=1}{nw}"
    return

label jenny_couch_sex_cum_outside:
    player_name "I'm going to cum!"
    jen "Me too!"
    jen "NGGHHH!!!"
    show jenny_couch_sex cumshot
    player_name "HNNGGG!!!" with flash
    pause
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show jenny b_couch_after3 f_empty a_empty
    show player b_couch_sit_naked f_couch_sit_right_talk a_couch_naked_after
    with fade
    player_name "Wow..."
    show player f_couch_sit_right
    show jenny b_couch_after4
    jen "Haah... Haah..."
    show jenny b_couch_after3
    show player f_couch_sit_right_talk
    player_name "That was intense!"
    show player f_couch_sit_right
    show jenny b_couch_after4
    jen "You came all over me!"
    show jenny b_couch_after3
    show player f_couch_sit_right_talk
    player_name "Would you rather I had cum inside of you?"
    show player f_couch_sit_right
    show jenny b_couch_after4
    jen "No... But you could have-"
    show jenny b_couch_after3
    pause
    show jenny b_couch_after4
    jen "{b}*Sigh*{/b} Nevermind."
    show jenny b_couch_remove with dissolve
    jen "I'm going to go take a shower."
    show jenny b_couch_transition with dissolve
    pause 1
    hide jenny with dissolve
    jen "Later, loser."
    show player f_couch_sit_right_talk
    player_name "Yeah, see ya."
    show player f_couch_sit_right
    pause
    show player f_couch_sit_down_surprised
    player_name "( Phew, I guess we're just fucking whenever now... )"
    player_name "( Awesome! )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["08_unlocked"] = True
    call hide_home_tv
    $ M_jenny.set("couch_sex_first", False)
    $ M_jenny.set("had_couch_sex", True)
    $ game.timer.tick()
    $ game.main()

label jenny_couch_sex_cum_inside:
    player_name "I'm going to cum!"
    jen "Me too!"
    player_name "Let go of me!"
    jen "NGGHHH!!!"
    player_name "{b}[jen_name]{/b} I can't-"
    show jenny_couch_sex cum
    player_name "HNNGGG!!!" with flash
    jen "AHHHH!!!"
    show jenny_couch_sex cum 2
    show xray_jenny_couch at Position (align=(0,0))
    pause
    hide xray_jenny_couch
    show jenny_couch_sex pullout 1
    with dissolve
    player_name "Holy crap..."
    show jenny_couch_sex pullout 2 with dissolve
    jen "Haah... Haah..."
    call call_pregnancy_minigame ("jenny_couch_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_couch_sex_cum_inside_post_pregnancy:
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show jenny b_couch_after2 f_empty a_empty
    show player b_couch_sit_naked f_couch_sit_right_talk a_couch_naked_after
    with fade
    show player f_couch_sit_right
    show jenny b_couch_after1
    jen "Oh my god, did you cum inside me?!"
    show jenny b_couch_after2
    show player f_couch_sit_right_talk
    player_name "I tried pulling out but you wouldn't let go of me!"
    show player f_couch_sit_right
    show jenny b_couch_after1
    jen "Well, I was focused on cumming!"
    show jenny b_couch_after2
    pause
    show jenny b_couch_after1
    jen "FUCK!"
    jen "You are so dead if I get pregnant!"
    show jenny b_couch_after2
    show player f_couch_sit_right_talk
    player_name "M-me?!"
    player_name "You're the one who held me there!"
    show player f_couch_sit_right
    show jenny b_couch_after1
    jen "Shut up!"
    show jenny b_couch_remove with dissolve
    jen "Grr, I'm getting in the shower!"
    show jenny b_couch_transition_mad with dissolve
    pause 1
    hide jenny with dissolve
    jen "Asshole..."
    show player f_couch_sit_right_talk
    player_name "Oh, so it's all my fault, huh?!"
    show player f_couch_sit_right
    pause
    player_name "( She's gone... )"
    pause
    show player f_couch_sit_down_surprised
    player_name "( Phew, I guess we're just fucking whenever now... )"
    player_name "( Awesome! )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["09_unlocked"] = True
    call hide_home_tv
    $ M_jenny.set("had_couch_sex", True)
    $ M_jenny.set("couch_sex_first", False)
    $ game.timer.tick()
    $ game.main()

label jenny_shower_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_shower_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_shower_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_shower_sex {}".format(pose_list[pose_counter]) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_shower_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_shower_sex_options

label jenny_shower_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jen "Ahh!!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "It's so deep!{p=1}{nw}"
        jen "Oh, fuck me!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "FUUUUUCK!!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        player_name "Uhh!{p=1}{nw}"
    return

label jenny_shower_sex_cum_inside:
    jen "I'm cumming! I'm cumming!"
    jen "NGGHHH!!!"
    player_name "Yeah, I'm getting close too"
    pause
    player_name "{b}[jen_name]{/b}?"
    show jenny_shower_sex cum
    player_name "HNNGGG!!!" with flash
    jen "AAAHHHH!!!"
    show jenny_shower_sex cum 2
    show xray_jenny_shower at Position (align=(0,0))
    pause
    call call_pregnancy_minigame ("jenny_mc_shower_sex_cum_inside_post_pregnancy_minigame", M_jenny)

label jenny_mc_shower_sex_cum_inside_post_pregnancy_minigame:
    call scene_shower_with_vfx
    show player b_naked a_naked_sides f_tired_talk od_naked_dick1
    show jenny b_shower_back a_shower_back_push f_shower_overshoulder_back_look_normal at Position (align=(0,0))
    with fade
    player_name "Haah... Haah..."
    show jenny a_shower_back_butt f_shower_overshoulder_back_look_surprised with dissolve
    show player f_normal_talk
    player_name "Holy crap!"
    show player f_normal
    show jenny b_shower_back_creampie a_empty with dissolve
    jen "Did you cum in me?!"
    show player f_worried_talk
    player_name "Y-yeah, a little..."
    show player f_surprised
    show jenny b_naked a_naked_crossed f_angry_talk with dissolve
    jen "A LITTLE?!"
    jen "THAT'S A LOT YOU MORON!"
    show jenny f_angry
    show player f_worried_talk
    player_name "I'm sorry."
    player_name "I guess, I got a little carried away there at the end..."
    show player f_worried
    show jenny f_angry_talk
    jen "What if I get pregnant?!"
    show jenny f_angry
    show player f_worried_talk
    player_name "I didn't-"
    show player f_worried
    show jenny f_angry_talk
    jen "Damnit, {b}[firstname]{/b}!"
    jen "Get the fuck out!"
    show jenny f_angry
    show player f_worried_talk
    player_name "Alright, alright..."
    player_name "I said I was sorry, sheesh."
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["14_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label jenny_shower_sex_cum_outside:
    jen "I'm cumming! I'm cumming!"
    jen "NGGHHH!!!"
    player_name "Yeah, I'm getting close too"
    pause
    player_name "{b}[jen_name]{/b}?"
    hide jenny_shower_sex
    show jenny b_shower_cumshot a_empty f_shower_cumshot
    show player b_side_naked_forward od_side_naked_forward_cum1 f_side_react a_side_naked_up_clench
    player_name "HNNGGG!!!" with flash
    show player od_side_naked_forward_cum2 o_side_naked_forward_cum3 with dissolve
    pause
    show player b_naked a_naked_sides f_tired_talk od_naked_dick1 o_empty
    show jenny b_naked a_naked_side f_sexy_down at Position (align=(0,0))
    with dissolve
    player_name "Haah... Haah..."
    show player f_normal
    show jenny f_sexy_talk
    jen "Haah... Holy shit!"
    show jenny f_sexy_talk_down
    jen "I think-"
    jen "I need to go lie down for a bit."
    show jenny f_sexy
    show player f_worried_talk
    player_name "You alright?"
    show player f_worried
    show jenny f_sexy_talk
    jen "Y-yeah, it's just the steam and the sex and..."
    show player f_normal
    show jenny f_laugh
    jen "Fuck, I can barely walk!"
    show jenny f_sexy
    show player f_grin
    player_name "Heh."
    show player f_normal_talk
    player_name "Here, I'll help you."
    show player f_worried
    show jenny f_upset_talk a_naked_hips with dissolve
    jen "No, fuck off!"
    jen "I'm fine!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Alright, sheesh."
    player_name "I'm just trying to be considerate..."
    show player f_worried
    show jenny f_upset_talk
    jen "Well, cut it out!"
    hide jenny with dissolve
    pause
    player_name "( She's so weird sometimes... )"
    show player f_grin
    player_name "( Oh well, that was awesome! )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["14_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label bj_shower_repeat_sub:
    show player f_worried_talk_low
    player_name "Arf!"
    show player f_worried_low
    show jenny f_grin_talk
    jen "Heh, more!"
    show jenny f_grin
    show player f_worried_talk_low
    player_name "{b}*Sigh*{/b}"
    show player f_shock
    player_name "Arf! Arf! Arf!"
    show player f_worried_low
    show jenny f_laugh
    jen "Hahahaah!!"
    show player b_side_naked a_side_naked_react f_side_shy_down od_side_naked_dick3
    show jenny b_shower_kneeling f_shower_kneeling_talk a_empty
    with dissolve
    if randomizer() > 50:
        jen "Good doggy!"
    else:
        jen "There's a good boy!"
    call scene_shower_with_vfx_zoom
    show jenny_shower_bj_mc
    show jenny_shower_bj pre_talk
    with fade
    jen "Now you get a reward!"

label bj_shower_repeat_dom:
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .14)
    show expression AnimatedImage("jenny_shower_bj", [1,2,3,4,5,6,7], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
    player_name "!!!" with hpunch

    if M_jenny.get('first_time_deep_bj'):
        $ M_jenny.set('first_time_deep_bj', False)
        player_name "{b}*Gasp*{/b}"
        pause
        player_name "Wow, okay..."
        player_name "Ahh!"
        pause
        player_name "Mm, that feels so good!"
        jen "Mmhrmm."
        pause
        show jenny_shower_bj_mc
        show jenny_shower_bj pre_talk
        with dissolve
        jen "Alright, I'm going to try something now..."
        show jenny_shower_bj pre_look
        player_name "Hmm?"
        show jenny_shower_bj pre_talk
        jen "My fans have been asking me for something and I'm going to test it out on you."
        show jenny_shower_bj pre_look
        player_name "What is it?"
        show jenny_shower_bj pre_talk
        jen "You'll see."
        jen "Just try and stay still!"
        show expression AnimatedImage("jenny_shower_bj", [1,2,3,4,5,6,7], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
        player_name "You're not going to do anything weird, are you?"
        pause
        player_name "{b}[jen_name]{/b}?"
    else:
        player_name "Mmm."
        pause
        player_name "Very nice!"
        jen "Shrmmup!!"
        player_name "Ohh!"
        pause
        player_name "Mm, that feels so good!"
        jen "Mmhrmm."
        pause

    $ M_jenny.set('sex speed', .4)
    show expression AnimatedImage("jenny_shower_bj_deep", [1,2], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
    $ M_jenny.set("jenny_bj_deep", True)
    player_name "!!!" with hpunch
    player_name "Oh my god!!"
    pause
    player_name "That feels incredible!!!"
    jen "{b}*Gllrrkkk*{/b}"
    pause
    jen "{b}*Bllgghhh*{/b}"
    player_name "{b}[jen_name]{/b}, I can't-"

    label jenny_shower_bj_loop:
        show screen sex_anim_buttons
        pause
        hide screen sex_anim_buttons
        $ animcounter = 0
        while animcounter < 4:
            if anim_toggle:
                if not animated:
                    if M_jenny.get("jenny_bj_deep"):
                        $ M_jenny.set('sex speed', .4)
                        show expression AnimatedImage("jenny_shower_bj_deep", [1,2], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0) with dissolve
                    else:
                        $ M_jenny.set('sex speed', .14)
                        show expression AnimatedImage("jenny_shower_bj", [1,2,3,4,5,6,7], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0) with dissolve
                    $ animated = True
                pause 5
                call expression game.dialog_select("jenny_shower_bj_hscene_dialog")
                pause 3
            else:

                $ pose_counter = 0
                if M_jenny.get("jenny_bj_deep"):
                    $ pose_list = [1,2]
                else:
                    $ pose_list = [1,2,3,4,5,6,7]
                $ poses_done = []
                while poses_done != pose_list:
                    if M_jenny.get("jenny_bj_deep"):
                        show expression "jenny_shower_bj_deep {}".format(pose_list[pose_counter]) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
                    else:
                        show expression "jenny_shower_bj {}".format(pose_list[pose_counter]) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
                    pause
                    $ poses_done.append(pose_list[pose_counter])
                    $ pose_counter += 1
                call expression game.dialog_select("jenny_shower_bj_hscene_dialog")
            $ animcounter += 1
        call screen jenny_shower_bj_options

label jenny_shower_bj_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        player_name "Mmm.{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        player_name "Very nice!{p=1}{nw}"
        jen "Shrmmup!!{p=1}{nw}"
        player_name "Ohh!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        player_name "{b}*Gasp*{/b}"
    if animcounter == 3 and randomizer() < 10:
        player_name "Wow, okay..."
        player_name "Ahh!"
    if animcounter == 3 and randomizer() < 10:
        player_name "Mm, that feels so good!"
        jen "Mmhrmm."
    return

label jenny_shower_bj_cum:
    player_name "I'm getting close!"
    jen "{b}*Sluuuuurp*{/b}"
    pause
    player_name "{b}[jen_name]{/b}!"
    pause
    show jenny_shower_bj cum
    player_name "HNNGGG!!!" with flash
    jen "!!!"
    show jenny_shower_bj after with dissolve
    pause
    call scene_shower_with_vfx
    show jenny b_naked a_naked_hips f_cheeks_surprised
    show player b_naked a_naked_sides f_normal_talk od_naked_dick1
    with fade
    if M_jenny.get("first_shower_time"):
        $ M_jenny.set("first_shower_time", False)
        player_name "Phew, that was-"
        player_name "I mean, I wasn't expecting you to-"
        show player f_surprised
        show jenny f_cheeks_swallow a_naked_shocked with dissolve
        player_name "!!!"
        show jenny f_normal_talk
        jen "Damn, that was a lot of cum!"
        show jenny f_normal a_naked_hips with dissolve
        show player f_worried_talk
        player_name "You swallowed it!"
        show player f_surprised
        show jenny f_normal_talk
        jen "Yeah, so?"
        show jenny f_normal
        show player f_normal_talk
        player_name "I thought you didn't like doing that?!"
        show player f_normal
        show jenny f_upset_talk
        jen "When did I ever say that?"
        show jenny f_upset
        show player f_skeptical_talk
        player_name "When you blew me on stream!"
        player_name "You said you only swallowed because your fans pay extra for it!"
        show player f_skeptical
        show jenny f_normal_talk
        jen "Oh, right..."
        show jenny f_normal
        show player f_skeptical_talk
        player_name "They can't see us in here, {b}[jen_name]{/b}!"
        show player f_skeptical
        show jenny f_upset_talk
        jen "Maybe I didn't wanna make a mess, you ever think of that?!"
        show jenny f_upset
        show player f_worried_talk
        player_name "You didn't wanna make a mess... In the shower?"
        show player f_worried
        jen "..."
        show jenny f_upset_talk
        jen "Oh my god, just-"
        jen "Whatever."
        show jenny f_eyeroll
        jen "{b}*Sigh*{/b} I like it, okay?"
        show jenny f_upset
        show player f_surprised
        player_name "..."
        show jenny f_upset_talk
        jen "I like swallowing your cum..."
        jen "Are you fucking happy now?!"
        show jenny f_upset
        show player f_normal_talk
        player_name "Heh, I can't believe you just said that..."
        show player f_normal
        show jenny f_eyeroll a_naked_crossed with dissolve
        jen "Ugh..."
        show jenny f_upset_talk
        jen "Don't get any ideas, loser!"
        jen "Just because I like your cum and your big cock, it doesn't mean I like you!"
        show jenny f_upset
        show player f_worried
        player_name "..."
        show jenny f_upset_talk
        jen "Now go away and let me finish my shower!"
        show jenny f_upset
        show player f_worried_talk
        player_name "Alright."
        show player f_normal_talk
        player_name "Thanks for the-"
        show player f_surprised
        show jenny f_angry_talk
        jen "Get out!!"
        hide player with dissolve
        jen "For fucks sake!"
        show jenny f_angry_pouting

        $ player.go_to(L_home_hallway)
        scene expression player.location.background_closeup
        show player f_grin with dissolve
        player_name "( That was so awesome! )"
        player_name "( Does this mean {b}I can join her in the shower whenever I want{/b}? )"
        show player f_thinking a_dressed_thinking with dissolve
        pause
        show player f_grin
        player_name "( I think it does! )"
    else:
        player_name "Phew..."
        player_name "You're getting really good at that!"
        show player f_normal
        show jenny f_cheeks_swallow a_naked_shocked with dissolve
        pause
        show jenny f_grin_talk
        jen "Pfft, was I ever not good at it?"
        show jenny f_grin
        show player f_normal_talk
        player_name "Heh, good point."
        show player f_normal
        pause
        show jenny f_normal_talk
        jen "Alright, beat it so I can finish my shower."
        show jenny f_normal
        show player f_normal_talk
        player_name "Yeah, okay."
        player_name "Thanks for the blowjob!"
        show player f_grin
        show jenny f_eyeroll a_naked_crossed with dissolve
        jen "Oh my god."
        show jenny f_upset_talk
        jen "Get out!"
        show jenny f_upset
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["13_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label jenny_mc_room_sex_on_sleep:
    if store._in_replay is not None:
        $ player.location = L_home_bedroom
        $ game.timer.tick(3)
    scene expression "backgrounds/location_home_bedroom_cutscene18.jpg"
    jen "Psst!"
    jen "{b}[firstname]{/b}, you awake?"
    scene expression "backgrounds/location_home_bedroom_cutscene17.jpg"
    player_name "Mmm."
    pause
    scene expression "backgrounds/location_home_bedroom_sex01c.jpg"
    show player b_visit a_empty f_visit_sleep
    show jenny b_visit_sit a_visit_sit_down f_visit_sexy_talk with dissolve
    if M_jenny.is_state(S_jenny_night_time_sex):
        jen "{b}[firstname]{/b}?"
        show jenny f_visit_sexy
        player_name "Nnnhhh."
        pause
        show jenny f_visit_sexy_talk
        jen "C'mon, wake up."
        show jenny f_visit_sexy
        player_name "No."
        show jenny f_visit_sexy_down a_visit_sit_reach with dissolve
        show player f_visit_normal_talk
        player_name "Damnit, {b}[jen_name]{/b}..."
        player_name "It's the middle of the night!"
        show player b_visit_up2 f_visit_up_tired
        show jenny f_visit_sexy_talk_down a_visit_sit_pull
        with dissolve
        jen "Oh, shut up."
        show jenny f_visit_sexy_down a_visit_sit_up with dissolve
        show jenny a_visit_sit_up2 with dissolve
        pause
        show jenny a_visit_sit_stroke with dissolve
        show player f_visit_up_tired_talk
        player_name "What are you doing, {b}[jen_name]{/b}?"
        player_name "I'm trying to slee-"
        show player f_visit_up_tired
        show jenny f_visit_sexy_talk_down
        jen "What does it look like I'm doing?!"
        show jenny b_visit_remove1 a_visit_dick f_empty with dissolve
        show player f_visit_up_surprised
        pause
        show player f_visit_up_tired_talk
        show jenny b_visit_remove2 with dissolve
        player_name "We really have to do this, right now?!"
        show jenny b_visit_climb a_empty with dissolve
        jen "Yes, I'm fucking horny and I want it right now!"

        scene expression "backgrounds/location_home_bedroom_sex05.jpg"
        show jenny_mc_room_sex insert
        with fade
        player_name "!!!"
        player_name "Damnit {b}[jen_name]{/b}, I'm tired..."
        jen "Oh, for fucks sake... All you have to do is lay there!"
        jen "I'm the one doing all the work!"
        show jenny_mc_room_sex 1 with dissolve
        jen "{b}*Gasp*{/b}"
        jen "God, I love your dick!"
        jump jenny_mc_room_sex_start
    else:
        jen "Wake up, {b}[firstname]{/b}."
        show jenny f_visit_sexy
        show player f_visit_normal_talk
        player_name "{b}[jen_name]{/b}?"
        show player f_visit_normal
        show jenny f_visit_sexy_talk a_visit_sit_reach with dissolve
        jen "C'mon, I need it."
        show player b_visit_up2 f_visit_up_tired
        show jenny f_visit_sexy_talk_down a_visit_sit_pull
        with dissolve
        pause
        show jenny f_visit_sexy_down a_visit_sit_up with dissolve
        show jenny a_visit_sit_up2 with dissolve
        pause
        show jenny a_visit_sit_stroke with dissolve
        menu:
            "Right now?":
                show player f_visit_up_tired_talk
                player_name "Right now?"
                show jenny b_visit_remove1 a_visit_dick f_empty with dissolve
                show player f_visit_up_surprised
                pause
                show jenny b_visit_remove2 with dissolve
                pause
                show jenny b_visit_climb a_empty with dissolve
                jen "Yes, I want it right now."

                scene expression "backgrounds/location_home_bedroom_sex05.jpg"
                show jenny_mc_room_sex insert
                with fade
                player_name "!!!"
                player_name "O-okay."
                jen "God, I can't get this dick out of my head!"
                player_name "Wow, you're really wet..."
                show jenny_mc_room_sex 1 with dissolve
                jen "{b}*Gasp*{/b}"
                jen "Ohh, fuck."
                jump jenny_mc_room_sex_start
            "Not tonight" if store._in_replay is None:
                if M_jenny.get("dominance") <= 0:
                    show player f_visit_up_tired_talk
                    player_name "Not right now, {b}[jen_name]{/b}."
                    show player f_visit_up_tired
                    show jenny f_visit_sexy_talk_down
                    jen "C'mon, you know you want it..."
                    show jenny f_visit_sexy_down
                    show player f_visit_up_tired_talk
                    player_name "Let's just do it tomorrow, okay?"
                    show player f_visit_up_tired
                    show jenny f_visit_sexy_talk
                    jen "I don't want it tomorrow, I want it now!"
                    show jenny f_visit_sexy_down
                    show player f_visit_up_tired_talk
                    player_name "Ahhh, I'm tiiiiired..."
                    show player f_visit_up_tired
                    show jenny f_visit_angry_talk a_visit_sit_up2 with dissolve
                    jen "Seriously?!"
                    jen "You've got a mega hot girl stroking you cock right now and you're saying no?!"
                    show jenny f_visit_angry
                    show player f_visit_up_tired_talk
                    player_name "{b}*Sigh*{/b} I'm sorry... I didn't-"
                    show player f_visit_up_tired
                    show jenny f_visit_angry_talk
                    jen "Just forget it!"
                    show jenny f_visit_angry
                    show player f_visit_up_tired_talk
                    player_name "N-no, we can if you really want to-"
                    show player f_visit_up_tired
                    show jenny f_visit_angry_talk
                    jen "I'm not in the mood anymore!"
                    show jenny a_visit_dick b_empty f_empty with dissolve
                    jen "You are such a little bitch sometimes, I swear!"
                    show player f_visit_up_tired_talk
                    player_name "{b}[jen_name]{/b}, I'm sorry, I-"
                    show player f_visit_up_tired
                    player_name "..."
                else:
                    show player f_visit_up_tired_talk
                    player_name "Not right now, {b}[jen_name]{/b}."
                    show player f_visit_up_tired
                    show jenny f_visit_sexy_talk_down
                    jen "C'mon, you know you want it..."
                    show jenny f_visit_sexy_down
                    show player f_visit_up_tired_talk
                    player_name "No, I just wanna sleep... Okay?"
                    show player f_visit_up_tired
                    show jenny f_visit_sexy_talk
                    jen "Please, {b}[firstname]{/b}?"
                    show jenny f_visit_sexy
                    show player f_visit_up_tired_talk
                    player_name "I said no!"
                    show player f_visit_up_tired
                    show jenny f_visit_angry_talk a_visit_sit_up2 with dissolve
                    jen "Seriously?!"
                    jen "I'm trying to be nice here, the way you like it... I even said please!"
                    show jenny f_visit_angry
                    show player f_visit_up_tired_talk
                    player_name "I'm just not in the mood, okay?"
                    show player f_visit_up_tired
                    jen "..."
                    show jenny f_visit_angry_talk
                    jen "FINE!"
                    show jenny a_visit_dick b_empty f_empty with dissolve
                    jen "I don't know why I waste my time on you..."
                    show player f_visit_up_tired_talk
                    player_name "Whatever."
                    show player f_visit_up_tired
                scene black with fade
                pause
                $ game.timer.sleep()
                $ game.main()

label jenny_mc_room_sex_start:
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
    jen "Ahh!"
    pause
    player_name "Okay, that feels really good..."
    if M_jenny.is_state(S_jenny_night_time_sex):
        jen "See, and you were all whining about it!"
        player_name "Well, we could have done this tomorrow!"
        jen "Yeah and we probably will..."
        player_name "R-really?"
        jen "Uhh, yeah... Camshows, dummy."
        player_name "Oh, right."
        jen "Just shut up and let me enjoy this!"
    else:
        jen "Ahh!"
        pause
        player_name "Okay, that feels really good..."
        jen "Yeah it does!"
    pause
    jen "Ahh, fuuuuck!"
    pause
    jen "Mmm, I'm gonna cum all over that big dick of yours, {b}[firstname]{/b}!"
    if M_jenny.get("dominance") <= 0:
        jen "You'd like that, wouldn't you?!"
        player_name "Y-yes."
        if M_jenny.get("sex speed") > 0.061:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jen "Ahh!"
        jen "C'mon, say it!"
        jen "Say you want me to cum on your big dick!"
        player_name "I want you to cum on my big dick!"
        if not M_jenny.is_state(S_jenny_night_time_sex):
            jen "I think you can do better..."
            pause
            jen "Tell me I'm a sex goddess!"
            player_name "Y-you're a sex godess!"
            jen "Come on, bitch!"
            jen "I can't hear you!"
            player_name "You're a sex godess!!!"
            jen "You worship this pussy, don't you?!"
            player_name "Y-yes!"
        jen "Hahahaah!!"
    else:
        player_name "Then do it!"
        if M_jenny.get("sex speed") > 0.061:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jen "Ahh, shit!"
        player_name "Tell me you want it!"
        jen "Mmm, I want it!"
        pause
        player_name "C'mon {b}[jen_name]{/b}, faster!"
        jen "Oh my god!"
        pause
        if M_jenny.is_state(S_jenny_night_time_sex):
            jen "Ahh, fuck me!!"
        else:
            player_name "Beg me to give it to you!"
            jen "Ahh!"
            jen "Please!!"
            pause
            player_name "C'mon, you can do better!"
            jen "Fuuuuck!"
            jen "Please, {b}[firstname]{/b}!!"
            jen "Give it to me!!!"

    player_name "Shh!"
    player_name "You're gonna wake up, {b}[deb_name]{/b}..."
    jen "I don't fucking care!"
    pause
    jen "Ahh, I'm so close!"

label jenny_mc_room_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_mc_room_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_mc_room_sex {}".format(pose_list[pose_counter]) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_mc_room_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_mc_room_sex_options

label jenny_mc_room_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jen "Ahh, fuuuuck!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "Fuuuuck!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "Hahahaah!!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        player_name "Oh my god!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "Ahh, fuck me!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        player_name "I'm getting close...{p=1}{nw}"
    return

label jenny_mc_room_sex_cum_inside:
    jen "Oh my god, oh my god, OH MY GOD!"
    pause
    jen "I'm cumming! I'm cumming!"
    player_name "Me too!"
    jen "AAAHHH, FUCK!!!"
    player_name "{b}[jen_name]{/b}, get off!"
    jen "NGGHHH!!!"
    player_name "Ah, crap!"
    $ M_jenny.set('sex speed', .4)
    show expression AnimatedImage("jenny_mc_room_sex cum", [1,2], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
    player_name "HNNGGG!!!" with flash
    show jenny_mc_room_sex cum 2
    show xray_jenny_mcbedroom at Position (align=(0,0))
    pause
    call call_pregnancy_minigame ("jenny_mc_room_sex_cum_inside_post_pregnancy_minigame", M_jenny)

label jenny_mc_room_sex_cum_inside_post_pregnancy_minigame:
    scene expression "backgrounds/location_home_bedroom_sex05.jpg"
    show jenny_mc_room_sex pullout
    with fade
    player_name "Haah... Haah..."
    hide jenny_mc_room_sex
    show jenny b_visit_after f_visit_after_angry_talk_down o_visit_after_creampie a_empty
    with dissolve
    jen "Oh my god..."
    show jenny f_visit_after_angry_down
    pause
    show jenny f_visit_after_angry_talk
    jen "Did you cum in me?!"
    show jenny f_visit_after_angry
    player_name "I told you to get off me!"
    show jenny f_visit_after_angry_talk
    jen "God damnit, {b}[firstname]{/b}!"
    show jenny f_visit_after_angry
    player_name "What?!"
    show jenny f_visit_after_angry_talk
    jen "I could get pregnant you moron!"
    show jenny f_visit_after_angry
    player_name "Well, I'm sorry but I did warn you..."
    show jenny f_visit_after_angry_talk
    jen "Ugh, whatever."
    show jenny f_visit_after_angry_down
    pause
    show jenny f_visit_after_normal_talk
    jen "{b}*Sigh*{/b} Fuck it..."
    jen "Heh, my legs are shaking like crazy!"
    if M_jenny.get('girlfriend_in_progress'):
        jump jenny_mc_room_sex_end_girlfriend_experience
    else:
        jump jenny_mc_room_sex_end

label jenny_mc_room_sex_cum_outside:
    jen "Oh my god, oh my god, OH MY GOD!"
    pause
    jen "I'm cumming! I'm cumming!"
    jen "NGGHHH!!!"
    pause
    player_name "Me too!"
    show jenny_mc_room_sex cumshot
    player_name "HNNGGG!!!{p=1}{nw}" with flash
    show jenny o_visit_cumshot f_empty a_empty b_empty
    pause
    hide jenny_mc_room_sex
    show jenny b_visit_after f_visit_after_normal a_empty o_visit_cumshot2
    with dissolve
    player_name "Haah... Haah..."
    show jenny f_visit_after_normal_talk
    jen "Phew, that was awesome..."
    show jenny f_visit_after_normal
    pause
    show jenny f_visit_after_normal_talk
    jen "Hahaha, you're a fucking mess!"
    show jenny f_visit_after_normal
    player_name "Heh, I don't even care... I'm so exhausted."
    show jenny f_visit_after_normal_talk
    jen "{b}*Snort*{/b} Hehehe!"
    jen "You should clean yourself up, you look ridiculous..."
    if M_jenny.get('girlfriend_in_progress'):
        jump jenny_mc_room_sex_end_girlfriend_experience
    else:
        jump jenny_mc_room_sex_end

label jenny_mc_room_sex_end_girlfriend_experience:
    scene expression "backgrounds/location_home_bedroom_bed.jpg"
    show jenny b_sleep_side_naked a_sleep_side_naked f_sleep_side_tired at flip
    show jenny at Position (xpos=500)
    show player b_sleep_side f_sleep_side_normal_talk a_sleep_side_poke o_sleep_side_dick2
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent2.png"
    with fade
    if M_jenny.get("jenny_girlfriend_first_time"):
        player_name "Tonight was a lot of fun!"
        show player f_sleep_side_normal
        show jenny f_sleep_side_tired_talk
        jen "I'm glad you enjoyed yourself."
        show jenny f_sleep_side_tired
        show player f_sleep_side_normal_talk
        player_name "... And I'm really happy you're not rushing off this time."
        show player f_sleep_side_normal
        show jenny f_sleep_side_tired_talk
        jen "Well, you did pay me not to, remember?"
        show jenny f_sleep_side_tired
        show player f_sleep_side_normal_talk
        player_name "Yeah."
        show player f_sleep_side_normal
        show jenny f_sleep_side_tired_talk
        jen "Hahahaah!"
        show jenny f_sleep_side_tired
        show player f_sleep_side_normal_talk
        player_name "You had fun too, didn't you?"
        show player f_sleep_side_normal
        show jenny f_sleep_side_rolleye
        jen "Yes, {b}[firstname]{/b}..."
        show jenny f_sleep_side_tired_talk
        jen "Now can you shut up and let me sleep?"
        show jenny f_sleep_side_sleeping
        show player f_sleep_side_normal_talk
        player_name "Sorry..."
        show player f_sleep_side_kiss
    else:
        player_name "Hehe, I'm really enjoying the nights we do this..."
        show player f_sleep_side_normal
        show jenny f_sleep_side_tired_talk
        jen "Yeah, me too."
        jen "I'm glad I came up with the idea."
        show jenny f_sleep_side_tired
        show player f_sleep_side_normal_talk
        player_name "Uhh, you know, this was technically MY idea..."
        show player f_sleep_side_normal
        show jenny f_sleep_side_tired_talk
        jen "Oh, shut up!"
        show jenny f_sleep_side_tired
        show player f_sleep_side_normal_talk
        player_name "I'm just saying..."
        show player f_sleep_side_normal
        show jenny f_sleep_side_tired_talk
        jen "Yeah, I know what you're saying... Now zip it!"
        jen "You're ruining my post coital bliss."
        show jenny f_sleep_side_tired
        show player f_sleep_side_normal_talk
        player_name "Sorry."
        show player f_sleep_side_normal
        show jenny f_sleep_side_rolleye
        jen "Go to sleep."
        show jenny f_sleep_side_sleeping
        show player f_sleep_side_kiss
    $ Sleep()
    if M_player.is_set("just wokeup"):
        $ renpy.call(game.dialog_select("player_just_wokeup"), woke_with = M_jenny)
    $ game.main()

label jenny_mc_room_sex_end:
    show jenny f_visit_after_normal
    if M_jenny.is_state(S_jenny_night_time_sex):
        player_name "You staying?"
    else:
        player_name "You leaving again?"
    jen "Hmm?"
    if M_jenny.is_state(S_jenny_night_time_sex):
        player_name "Do you wanna sleep here with me tonight?"
        show jenny f_visit_after_normal_talk
        jen "Eww, no!"
        jen "I'm not your fucking girlfriend, doofus..."
    else:
        player_name "You can sleep here, you know?"
        show jenny f_visit_after_normal_talk
        jen "For fucks sake..."
        jen "Didn't we go over this already?"
    show jenny f_visit_after_normal

    if store._in_replay is not None:
        $ player.location = L_home_bedroom
    scene expression player.location.background_closeup with None
    show jenny b_naked a_naked_side f_normal o_empty at Position (xpos=100)
    show player b_underwear a_naked_sides f_skeptical_talk at flip
    with dissolve
    if M_jenny.is_state(S_jenny_night_time_sex):
        player_name "Wait!"
    else:
        player_name "Alright, fine.... Whatever."
    show player f_worried
    hide jenny
    if M_jenny.is_state(S_jenny_night_time_sex):
        $ M_jenny.trigger(T_jenny_didnt_sleep_much)
        show jenny b_naked a_naked_crossed f_upset_talk at flip
        with dissolve
        jen "What, {b}[firstname]{/b}?!"
        show jenny f_upset
        show player f_worried_talk
        player_name "I wasn't trying to-"
        player_name "{b}*Sigh*{/b} Just, explain this to me..."
        show player f_skeptical_talk
        player_name "So, we can have sex whenever we want but you won't sleep in my bed?"
        show player f_worried
        show jenny f_eyeroll
        jen "Umm, no... We can have sex whenever {b}{i}I{/i}{/b} want..."
        show jenny f_upset_talk
        jen "... So long as it doesn't interfere with my camshows."
        show jenny f_upset
        pause
        show jenny f_upset_talk
        jen "... And no, I won't sleep in your bed!"
        jen "{b}I'm not your fucking girlfriend and you're sure as hell not my boyfriend{/b}!"
        jen "Get that through your thick skull, dummy!"
        show jenny f_upset
        show player f_skeptical_talk
        player_name "I don't get you at all..."
        show player f_skeptical
        show jenny f_upset_talk
        jen "Yeah, well... You don't have to {i}get{/i} me."
        jen "That's just the way things are."
        jen "Deal with it."
        show jenny f_upset
        player_name "..."
    else:
        show jenny b_naked a_naked_crossed f_upset at flip
        with dissolve
        show player f_skeptical_talk
        player_name "Just forget I said anything."
        show player f_skeptical
        show jenny f_upset_talk
        jen "Gladly."
        show jenny f_upset
        pause
    show jenny f_upset_talk
    jen "Now go to sleep!"
    show jenny f_grin_talk
    jen "My fans are expecting a good show tomorrow."
    hide jenny with dissolve
    pause
    show player f_worried
    player_name "..."
    scene black with fade
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["12_unlocked"] = True
    jump resume_sleeping_bedroom

label jenny_sex_intro_repeat:
    show player f_worried_talk
    player_name "Sex. Please."
    show player f_worried
    show jenny f_upset_talk
    jen "Hurry up."
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show player f_surprised
    pause
    show jenny b_panties a_naked_hips f_upset with dissolve
    show jenny f_upset_talk
    jen "Well?"
    player_name "Hmm?"
    jen "Get those clothes off!"
    show jenny b_naked f_grin_down a_naked_panties_remove with dissolve
    show player f_worried_talk
    player_name "R-right..."
    show player b_dressed_changing a_empty f_empty
    show jenny b_cheer_dress1 f_empty a_empty
    with dissolve
    pause
    show jenny b_cheer_dress3 f_grin_down with dissolve
    pause
    show jenny b_cheer_dress2 f_empty with dissolve
    show player f_worried_talk b_shorts a_naked_sides with dissolve
    player_name "You're going to wear that again?"
    show player f_worried
    show jenny b_cheer a_cheer_hips f_sexy_talk with dissolve
    jen "Of course!"
    jen "My fans like it."
    show jenny f_sexy
    show player b_dressed_changing2 a_empty f_empty with dissolve
    player_name "..."
    show player b_underwear a_naked_sides f_worried with dissolve
    show jenny f_sexy_talk
    jen "Get on the bed."
    show jenny f_sexy
    hide player with dissolve
    pause
    show jenny f_sexy_talk
    jen "... And put your mask on!"
    show jenny f_sexy
    label finger_blasting_sex:
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show player b_bed_jenny_sit a_empty f_jenny_bed_sit_shy_down of_jenny_bed_sit_mask at Position (align=(0,0))
    show jenny o_under_body_laptop o_naked_bed_belly_cheer b_naked_bed_bellytype a_empty f_bed_facing_comp_sexy_talk_down at Position (align=(0,0))
    with dissolve
    pause
    jen "You boys ready for another show?"
    show jenny f_bed_facing_comp_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_facing_comp_laugh
    jen "Hehehe!"
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Alright, let me get things ready..."
    show jenny b_bed_climbing a_empty f_empty o_cheer_bed_climbing
    show player b_bed_jenny_laying_undies_arms f_empty a_empty of_bed_jenny_laying_undies_arms_mask
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png" zorder 2
    show expression "characters/jenny/layeredimage/jenny_overlay_o_laptop.png"
    with dissolve
    jump jenny_cheer_sex_intro_prepare

label jenny_cheer_sex_intro_prepare:
    player_name "Are we really going to-"
    jen "Shh!"
    pause
    show jenny b_bed_back_sit o_cheer_bed_back
    show expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_handcuffs.png" zorder 1
    with dissolve
    player_name "Aww, c'mon {b}[jen_name]{/b}!"
    player_name "You know I hate these things..."
    show jenny a_bed_back_sit_tie
    hide expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_handcuffs.png"
    show expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_tie.png" zorder 1
    show player oh_bed_jenny_laying_undies_handcuffs
    with dissolve
    jen "Shut your mouth!"
    if M_jenny.get("dominance") <= 0:
        player_name "..."
        pause
        show jenny a_bed_back_sit_hips
        hide expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_tie.png"
        show expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_hips.png" zorder 1
        with dissolve
        if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay:
            jen "And if you hate them that much, quit moaning about them and do something."
            jen "They're only plastic, I'm sure the boys would love to see you try and {b}break free{/b}!"
        else:
            jen "Good."
        jen "Now, beg for it."
        player_name "What?!"
        jen "You want me to take that big cock of yours for a ride, don't you?"
        player_name "Y-yes..."
        jen "Then you're going to beg me for it, in front of my fans!"
        player_name "..."
        jen "Go on!"
        player_name "Please..."
        jen "Princess!"
        player_name "..."
        player_name "Please, {b}Princess [jen_name]{/b}..."
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        jen "HAHAHAAH!"
        show jenny b_bed_front_sit a_bed_front_sit_pull1 f_bed_front_sit_sexy_down o_cheer_bed_front_sit2
        hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png"
        hide expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_hips.png"
        show jenny a_bed_front_sit_pull1
        with dissolve
        pause
        show jenny a_bed_front_sit_pull2 f_bed_front_sit_sexy_talk_down o_cheer_bed_front_sit3 with dissolve
        jen "You boys ready?"
    else:
        player_name "I don't like them!"
        jen "HOLD STILL!"
        player_name "Grr!"
        jen "I'm in charge here, not you!"
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        show jenny a_bed_back_sit_hips
        hide expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_tie.png"
        show expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_hips.png" zorder 1
        with dissolve
        jen "There!"
        jen "Sheesh, I don't know what you're complaining about..."
        show jenny b_bed_front_sit a_bed_front_sit_pull1 f_bed_front_sit_sexy_talk_down o_cheer_bed_front_sit2
        hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png"
        hide expression "characters/jenny/layeredimage/jenny_arms_a_bed_back_sit_hips.png"
        show jenny a_bed_front_sit_pull1
        with dissolve
        jen "Here I am, offering to fuck your brains out and you're whining about stupid handcuffs!"
        show jenny a_bed_front_sit_pull2 o_cheer_bed_front_sit3 with dissolve
        jen "You boys wouldn't put up a fight, would you?!"
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny a_bed_front_sit_sides f_bed_front_sit_sexy_down o_cheer_bed_front_sit
    with dissolve
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_front_sit_sexy_talk_down
    jen "Heh, they're excited..."
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg"
    show jenny_cheer_sex tied insert
    with fade
    jen "( Here we go, {b}[firstname]{/b}... The moment you've been dreaming of! )"
    jen "Ohh!"
    jen "Holy shit!"
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .09)
    show expression AnimatedImage("jenny_cheer_sex_tied_mask", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
    jen "Oh my god, you guys..."
    jen "This is a REALLY big dick!"
    jump jenny_cheer_sex_loop_tied

label jenny_cheer_sex_loop_tied:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_jenny.get("cam show mask"):
                    show expression AnimatedImage("jenny_cheer_sex_tied_mask", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression AnimatedImage("jenny_cheer_sex_tied", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_tied")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
            $ poses_done = []
            while poses_done != pose_list:
                if M_jenny.get("cam show mask"):
                    show expression "jenny_cheer_sex_tied_mask {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression "jenny_cheer_sex_tied {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_tied")
        $ animcounter += 1
    call screen jenny_cheer_sex_options_tied

label jenny_cheer_sex_hscene_dialog_tied:
    if animcounter == 0 and randomizer() < 10:
        jen "Ahh!{p=1}{nw}"
    if animcounter == 0 and randomizer() < 10:
        jen "This is so fucking good!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "Oh, fuck!{p=1}{nw}"
        jen "I'm gonna squirt all over that big dick!{p=2}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "Mmm, fuck!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "It's so good!!{p=1}{nw}"
        player_name "I'm getting close!{p=1}{nw}"
        jen "SO FUCKING GOOD!!{p=1}{nw}"
        player_name "{b}[jen_name]{/b}!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        player_name "You're really good at this!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 5:
        jen "You like that, don't you?!{p=1}{nw}"
        player_name "Y-yeah.{p=1}{nw}"
        jen "Tell me you like it!{p=1}{nw}"
        player_name "I like it!{p=1}{nw}"
        jen "Tell me you love my pussy!{p=1}{nw}"
        player_name "Ahh, I love it!{p=1}{nw}"
        jen "Hahahaah!{p=1}{nw}"
        if M_jenny.get("sex speed") > 0.031:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jen "Mmm, yeah!{p=1}{nw}"
    return

label jenny_cheer_sex_cum_inside_tied:
    if M_jenny.is_state(S_jenny_cheerleader_sex):
        player_name "I can't hold it!"
    else:
        player_name "Get off!"
    pause
    player_name "{b}[jen_name]{/b}!!!"
    jen "NGGHHH!!!"
    player_name "I can't-"
    pause
    show jenny_cheer_sex tied cum
    player_name "HNNGGG!!!" with flash
    show jenny_cheer_sex tied cum 2
    show xray_jenny_cheer_bedroom at Position (align=(0,0))
    pause
    call call_pregnancy_minigame ("jenny_cheer_sex_cum_inside_tied_post_pregnancy", M_jenny)

label jenny_cheer_sex_cum_inside_tied_post_pregnancy:
    hide screen pregnancy_minigame
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg"
    show jenny_cheer_sex tied pullout 1
    with fade
    jen "Haah... Haaah..."
    show jenny_cheer_sex tied pullout 2 with dissolve
    jen "Fuuuck, that was incredi-"
    show jenny_cheer_sex tied pullout 3 with dissolve
    jen "!!!"
    show jenny_cheer_sex tied pullout 4 with dissolve
    if M_jenny.is_state(S_jenny_cheerleader_sex):
        jen "Did you cum inside me?!"
        player_name "Y-you told me not to stop..."
        jen "Yeah but I didn't say to finish inside me you idiot!"
        player_name "I'm sorry, I didn't mean to-"
        jen "What if I get pregnant?!"
        player_name "..."
    else:
        jen "Did you cum inside me?!"
        player_name "I warned you!"
        jen "I didn't hear anything!"
        player_name "Well, what do you want me to do?!"
        player_name "I'm handcuffed to your bed!"
        jen "I could get pregnant you moron!"
        player_name "Then you should have gotten off when I warned you!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Oh for fucks sake..."
    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_cum_outside_tied:
    player_name "I'm going to cum!"
    jen "Hold it!"
    player_name "W-what?! It doesn't work like that!"
    jen "I'm so close!"
    player_name "{b}[jen_name]{/b}!!!"
    jen "FUCK!!"
    show jenny_cheer_sex tied cumshot
    show jenny_cheer_sex_mc tied cumshot initial
    player_name "HNNGGG!!!" with flash
    show jenny_cheer_sex_mc tied cumshot
    pause
    player_name "Haah... Haah..."
    jen "You couldn't have lasted another ten seconds?!"
    if randomizer() > 50:
        player_name "S-sorry."
    else:
        player_name "It's difficult when I'm handcuffed to the bed!"
    jen "Whatever..."
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "oh for fucks sake..."
    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_break_free:
    if player.has_required_str(7) or store._in_replay is not None:
        show jenny_cheer_sex free break
        jen "!!!" with hpunch
        $ animated = True
        $ anim_toggle = True
        $ M_jenny.set('sex speed', .08)
        if M_jenny.get("cam show mask"):
            show expression AnimatedImage("jenny_cheer_sex_free_mask", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
        else:
            show expression AnimatedImage("jenny_cheer_sex_free", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
        jen "OH FUCK!!{p=1}{nw}"
        pause 1
        jen "OHMYGOD, OHMYGOD, OHMYGOD!!!{p=1}{nw}"
        pause 1
        jen "AHHH!!!{p=1}{nw}"
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}{p=1}{nw}"
        pause 1
        jen "FUUUUCK MEEEE!!!{p=1}{nw}"

        label jenny_cheer_sex_loop_free:
            show screen sex_anim_buttons
            pause
            hide screen sex_anim_buttons
            $ animcounter = 0
            while animcounter < 4:
                if anim_toggle:
                    if not animated:
                        if M_jenny.get("cam show mask"):
                            show expression AnimatedImage("jenny_cheer_sex_free_mask", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        else:
                            show expression AnimatedImage("jenny_cheer_sex_free", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        $ animated = True
                    pause 5
                    call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_free")
                    pause 3
                else:

                    $ pose_counter = 0
                    $ pose_list = [1,2,3,4,5]
                    $ poses_done = []
                    while poses_done != pose_list:
                        if M_jenny.get("cam show mask"):
                            show expression "jenny_cheer_sex_free_mask {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        else:
                            show expression "jenny_cheer_sex_free {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        pause
                        $ poses_done.append(pose_list[pose_counter])
                        $ pose_counter += 1
                    call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_free")
                $ animcounter += 1
            call screen jenny_cheer_sex_options_free

        label jenny_cheer_sex_hscene_dialog_free:
            if animcounter == 0 and randomizer() < 30:
                jen "OH FUCK!!{p=1}{nw}"
            if animcounter == 1 and randomizer() < 10:
                jen "FUCK ME!{p=.5}{nw}"
                jen "FUCK ME!{p=.5}{nw}"
                jen "FUUUUCK MEEEE!!!{p=1}{nw}"
            if animcounter == 2 and randomizer() < 30:
                jen "AHHH!!!{p=1}{nw}"
            return
    else:

        jen "[str_warn]Oh my god!{p=1}{nw}"
        pause 1
        jen "[str_warn]Fuck me!{p=1}{nw}"
        pause 1
        jen "[str_warn]FUCK ME!!{p=1}{nw}"
        jump jenny_cheer_sex_loop_tied

label jenny_cheer_sex_cum_inside_free:
    player_name "I'm getting close!"
    pause
    jen "Don't stop!"
    player_name "{b}[jen_name]{/b}, I can't-"
    jen "DON'T STOP!"
    pause
    jen "NGGHHH!!!"
    show jenny_cheer_sex free cum
    player_name "HNNGGG!!!" with flash
    show jenny_cheer_sex free cum 2
    show xray_jenny_cheer_bedroom at Position (align=(0,0))
    pause
    call call_pregnancy_minigame ("jenny_cheer_sex_cum_inside_free_post_pregnancy", M_jenny)

label jenny_cheer_sex_cum_inside_free_post_pregnancy:
    hide screen pregnancy_minigame
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg"
    pause
    show jenny_cheer_sex free pullout 1 with dissolve
    jen "Haah... Haaah..."
    show jenny_cheer_sex free pullout 2 with dissolve
    jen "Fuuuck, that was incredi-"
    show jenny_cheer_sex free pullout 3 with dissolve
    jen "!!!"
    show jenny_cheer_sex free pullout 4 with dissolve
    jen "Did you cum inside me?!"
    player_name "You told me not to stop..."
    jen "I didn't mean for you to cum inside me, idiot!"
    player_name "Don't start in with the name calling..."
    jen "What if I get pregnant!!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Oh for fucks sake..."
    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_cum_outside_free:
    player_name "I'm getting close!"
    pause
    jen "Don't stop!"
    player_name "{b}[jen_name]{/b}, I can't-"
    jen "DON'T STOP!"
    pause
    jen "NGGHHH!!!"
    show jenny_cheer_sex free cumshot
    show jenny_cheer_sex_mc tied cumshot initial
    player_name "HNNGGG!!!" with flash
    show jenny_cheer_sex_mc tied cumshot
    pause
    player_name "Haah... Haah..."
    jen "What the fuck, I told you not to stop!!"
    player_name "What, do you want me to cum inside you?!"
    jen "N-no, it just... Felt really good and-"
    jen "{b}*Sigh*{/b} Nevermind..."
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "oh for fucks sake..."
    jen "Show's over, pervs!"
    jen "Tune in next time!"
    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_aftermath:
    scene expression player.location.background_closeup with None
    show jenny f_upset b_cheer a_cheer_hips
    show player f_normal_talk b_underwear a_naked_sides
    with dissolve
    player_name "That was awesome!"
    show player f_normal
    show jenny f_eyeroll
    jen "Yeah, whatever."
    show jenny f_upset_talk
    jen "You were alright."
    show player f_worried
    jen "Now, get out!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Can't we just-"
    show player f_worried
    show jenny f_upset_talk a_cheer_hips_money
    jen "No, take your stupid money and get out!"
    hide jenny with dissolve
    show player f_worried_talk
    player_name "Alright, sheesh..."
    hide player with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player f_grin with dissolve
    player_name "( I just had sex with {b}[jen_name]{/b}... )"
    player_name "( On camera in front of hundreds of people! )"
    pause
    player_name "( How crazy is that?! )"
    player_name "( I hope we do it again. )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["11_unlocked"] = True
    call screen money_popup(amount=200)
    $ M_jenny.trigger(T_jenny_had_cheerleader_sex)
    $ player.get_money(200)
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label jenny_cunni_intro_repeat:
    show player f_worried_talk
    player_name "So no camshow today?"
    show player f_worried
    show jenny f_upset_talk
    jen "No, I'm not in the mood..."
    show jenny f_upset
    show player f_worried_talk
    player_name "What?!"
    player_name "You're always in the mood."
    show player f_worried
    show jenny f_upset_talk
    jen "To be gawked at, asshole!"
    jen "I'm not in the mood to be gawked at!"
    show jenny f_upset
    show player f_laugh
    player_name "Oh heh. Gotcha."
    show player f_normal
    show jenny f_upset_talk
    jen "I need a day off..."
    show jenny f_upset
    show player f_grumpy_talk at flip
    show player at Position (xpos=-100)
    with dissolve
    player_name "I'll leave you to it then."
    show player f_grumpy
    show jenny f_upset_talk
    jen "Wait."
    show jenny f_upset
    hide player
    show player f_normal
    with dissolve
    player_name "..."
    show jenny f_grin_talk
    jen "Since you're already here..."
    show jenny f_grin
    show player f_worried
    player_name "Hmm?"
    show jenny f_grin_talk
    jen "C'mon."
    hide jenny
    hide player
    with dissolve
    label finger_blasting_cunni:
    scene expression "backgrounds/location_home_hallway_cutscene.jpg" with dissolve
    player_name "Where are we going?!"
    jen "I think, you need more practice..."
    player_name "W-why are we going to my room?!"
    jen "Oh, shut up!"
    $ player.go_to(L_home_bedroom)
    scene expression player.location.background_closeup with None
    show player f_worried
    show jenny b_dressed_panties_remove_down a_empty f_empty
    with dissolve
    pause
    show player f_worried_talk
    show jenny b_pantieless a_dressed_hips f_grin with dissolve
    player_name "What are you doing?"
    show player f_worried
    show jenny f_grin_talk
    jen "You're going to lick my pussy."
    show jenny f_grin
    if M_jenny.get("dominance") <= 0:
        show player f_worried_talk
        player_name "I am?"
        show player f_worried
        show jenny f_grin_talk
        jen "Yup."
        jen "C'mon, loser!"
        jen "I'm going to cum all over that idiot face of yours!"
    else:
        show player f_worried_talk
        player_name "Oh really?"
        show player f_worried
        show jenny f_grin_talk
        jen "Yup."
        show jenny f_grin
        show player f_worried_talk
        player_name "Maybe if you ask me nicely."
        show player f_worried
        show jenny f_upset_talk
        jen "Ugh, you're still hung up on that shit?!"
        show jenny f_upset
        show player f_skeptical_talk
        if randomizer() > 50:
            player_name "If you wanna go back to masturbating, suit yourself..."
        else:
            player_name "I'm not your little whipping boy, {b}[jen_name]{/b}..."
        show player f_skeptical
        show jenny f_upset_talk
        jen "Grr, you are such a pain in the ass!"
        jen "Fine."
        show jenny f_angry_pouting a_dressed_crossed with dissolve
        pause
        show jenny f_upset_talk
        jen "{b}[firstname]{/b}, would you please lick my pussy?"
        show jenny f_upset
        show player f_laugh
        player_name "Haha, sure!"
        show player f_skeptical
        show jenny f_eyeroll
        jen "Just, c'mon!"
    jump jenny_cunni_repeat


label jenny_cunni_repeat:
    scene bedroom_sex2
    if M_jenny.is_state(S_jenny_give_cunni):
        show jennysex 135 at right
    else:
        show jennysex 137 at right
    show jennysex_cunnilingus_player at right
    with fade
    if M_jenny.is_state(S_jenny_give_cunni):
        jen "Hehe, remember that cum you shot all over my comforter?!"
        jen "It's payback time, bitch!"
        show jennysex 134
        player_name "Hey, I washed it for you!"
        show jennysex 135
        jen "Hahaha!"
        show jennysex 137 with dissolve
    pause
    show jennysex 137b
    jen "Well, what are you waiting for, an invitation?!"
    jen "Lick my puss-"
    $ M_jenny.set('sex speed', .3)
    show expression AnimatedImage("jenny_lick_shirt", [1,2,3,4], M_jenny) as jennysex at Position(xalign = 0.0, yoffset = 0)
    hide jennysex_cunnilingus_player
    with fastdissolve
    jen "EEyyyy!!!"
    pause
    jen "Fuuuuuck!"
    pause
    jen "Mmm, your tongue feels amazing!"
    jen "Ahh!"
    pause
    show jennysex 135
    show jennysex_cunnilingus_player at right
    with dissolve
    jen "Focus on my clit more, dummy!"
    jen "... And play with my tits too!"
    show jennysex 134
    if M_jenny.get("dominance") <= 0:
        player_name "Alright."
        show jennysex 135
        jen "{b}*Ahem*{/b} Alright, what?"
        show jennysex 134
        player_name "{b}*Sigh*{/b} Alright, {b}Princess Jenny{/b}..."
        show jennysex 135
        jen "Hahaha!"
        jen "That's right, loser!"
    else:
        player_name "Ask nicely or I'm stopping..."
        show jennysex 135
        jen "What?!"
        jen "Oh my god, you can't stop now!"
        show jennysex 134
        player_name "Watch me."
        show jennysex 135
        jen "No, no, no!"
        show jennysex 134
        jen "Grr!"
        show jennysex 135
        jen "Please, play with my tits, {b}[firstname]{/b}..."
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .2)
    show expression AnimatedImage("jenny_lick", [1,2,3,4], M_jenny) as jennysex at Position(xalign = 0.0, yoffset = 0)
    hide jennysex_cunnilingus_player
    with dissolve
    jump jenny_lick_loop

label jenny_lick_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_lick", [1,2,3,4], M_jenny) as jennysex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_lick_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_lick {}".format(pose_list[pose_counter]) as jennysex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_lick_hscene_dialog")
        $ animcounter += 1
    call screen jenny_lick_options

label jenny_lick_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jen "!!!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "Right there!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "Just like that.{p=1}{nw}"
        jen "Yesss!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        jen "Mmm, I'm getting close!{p=2}{nw}"
    return

label jenny_lick_cum:
    jen "I'm gonna-"
    jen "Oh fuck!"
    pause
    show jennysex 143
    jen "NGGHHH!!!" with flash
    show jennysex 135c
    show jennysex_cunnilingus_player at right
    with dissolve
    jen "Haah... Haah..."
    show jennysex 134c
    player_name "Sheesh, you soaked me."
    pause
    show jennysex 135c
    jen "Psh, you like it!"
    show jennysex 134c
    player_name "Yeah, right..."
    show jennysex 135c
    jen "Hehehe!"
    hide jennysex
    hide jennysex_cunnilingus_player
    with dissolve
    scene expression player.location.background_closeup with None
    show jenny f_normal_talk b_pantieless
    show player f_worried
    with dissolve
    jen "Phew, alright... That was pretty good."
    show jenny f_normal
    show player f_worried_talk
    player_name "Yeah, for you."
    show player f_worried
    show jenny f_laugh
    jen "Hahaha!"
    show jenny f_normal_talk
    jen "Don't worry, I'll take care of you later."
    show jenny f_grin_talk
    jen "Maybe..."
    show jenny f_grin
    pause
    show jenny f_grin_talk
    jen "... If you're a good boy."
    show jenny f_grin
    show player f_worried_talk
    player_name "C'mon, {b}[jen_name]{/b}..."
    show player f_worried
    show jenny f_upset_talk
    jen "No."
    show jenny f_grin_talk
    jen "Besides, don't you have some laundry to do?!"
    show jenny f_grin
    show player f_grumpy
    player_name "..."
    show jenny f_grin_talk a_pantieless_panties with dissolve
    jen "Later, loser!"
    hide jenny with dissolve
    jen "Hahahaah!"
    show player f_unimpressed_talk
    player_name "{b}*Sigh*{/b}"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["10_unlocked"] = True
    $ player.go_to(L_home_bedroom)
    $ game.timer.tick()
    $ M_jenny.trigger(T_jenny_gave_cunni)
    $ game.main()


label jenny_bj_intro_repeat:
    show player f_worried_talk
    player_name "Oral."
    show player f_worried
    show jenny f_upset_talk
    jen "Hurry up."
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show player f_surprised
    pause
    show jenny b_panties a_naked_hips f_upset with dissolve
    show jenny f_upset_talk
    jen "Well?"
    player_name "Hmm?"
    jen "Get those clothes off!"
    show jenny f_grin_down b_naked a_naked_panties_remove with dissolve
    show player f_worried_talk
    player_name "R-right..."
    show player f_worried
    show jenny b_naked_panties_remove_down a_empty f_empty with dissolve
    pause
    label finger_blasting_bj:
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_cutscene05.jpg" with dissolve
    jen "You know the drill."
    jen "Mask on and keep your mouth shut."
    player_name "Yeah, I remember."
    jen "I'll handle the rest."
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show player b_bed_jenny_sit a_empty f_jenny_bed_sit_shy_down of_jenny_bed_sit_mask at Position (align=(0,0))
    show jenny o_under_body_laptop b_naked_bed_bellytype a_empty f_bed_facing_comp_sexy_talk_down at Position (align=(0,0))
    with dissolve
    jen "Hi again, everybody!"
    jen "I brought my boy toy back to give you guys another show."
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_laugh
    jen "Hehe, of course!"
    show jenny b_bed_climbing a_empty f_empty
    show player b_bed_jenny_laying_undies_arms f_empty a_empty of_bed_jenny_laying_undies_arms_mask od_bed_jenny_laying_dick1
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick1.png"
    with dissolve
    pause
    show jenny b_bed_back_sit a_bed_back_sit_handcuffs with dissolve
    player_name "Handcuffs again?!"
    show jenny a_bed_back_sit_tie
    show player oh_bed_jenny_laying_undies_handcuffs
    with dissolve
    jen "Shh!"
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick1.png"
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png"
    with dissolve
    player_name "{b}[jen_name]{/b}, I don't wanna-"
    jen "Shut up!"
    show jenny b_bed_back_look a_bed_back_look_up f_bed_back_look_normal_talk with dissolve
    jen "There."
    jen "Let's see if our friend is awake yet, hmm?"
    show jenny b_bed_front_sit a_bed_front_sit_sides f_bed_front_sit_sexy_down with dissolve
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png"
    show jenny a_bed_front_sit_pull1
    with dissolve
    pause
    show jenny a_bed_front_sit_pull2 with dissolve
    jen "!!!"
    show jenny f_bed_front_sit_sexy_talk_down
    jen "Hello, big fella."
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    show player od_bed_jenny_laying_dick6
    show jenny b_bed_front_laying a_empty f_bed_front_laying_sexy_talk_down
    with dissolve
    jen "You boys ready to have some fun?"
    show jenny f_bed_front_laying_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    player_name "What are we going-"
    show jenny b_bed_pussy1 f_bed_pussy1_sexy_down
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    player_name "!!!" with hpunch
    player_name "Mrphmmmll-"
    show jenny f_bed_pussy1_sexy_talk_down
    jen "What was that, boy toy?"
    jen "We can't hear you... Hahahaah!"
    show player od_empty
    show jenny b_bed_pussy f_bed_pussy_sexy_down
    with dissolve
    pause
    show jenny f_bed_pussy_sexy_talk_down
    jen "Mmm, fuck yeah!"
    show jenny f_bed_pussy_sexy_down
    pause
    show jenny f_bed_pussy_nipple2
    jen "Ahh!"
    show jenny f_bed_pussy_nipple3
    pause
    show jenny f_bed_pussy_nipple2
    jen "You're so fucking good at this!"
    show jenny f_bed_pussy_nipple3
    player_name "Errmmhnnn!"
    show jenny f_bed_pussy_nipple2
    jen "Hahaha!"
    show jenny f_bed_pussy_nipple3
    pause
    show jenny f_bed_pussy_nipple2
    jen "I'm getting close!"
    show jenny f_bed_pussy_nipple3
    pause
    show jenny f_bed_pussy_nipple2
    jen "Oh, god!"
    jen "Right there!!"
    show jenny f_bed_pussy_nipple3
    pause
    show jenny b_bed_pussy1 f_bed_pussy1_nipple2
    jen "NGGHHH!!!" with flash
    pause
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny b_bed_front_laying a_empty f_bed_front_laying_nipple2
    show player od_bed_jenny_laying_dick6
    with dissolve
    jen "Haah... Haaah..."
    player_name "{b}*Gasp*{/b}"
    player_name "{b}*Cough* *Sputter* *Cough*{/b}"
    player_name "Damnit, {b}[jen_name]{/b}!"
    player_name "You know I can't breathe when you do that!"
    show jenny f_bed_front_laying_laugh
    jen "Hehehe!"
    show jenny f_bed_front_laying_sexy_down
    player_name "It's not funny!"
    show jenny f_bed_front_laying_sexy_talk_down
    jen "Oh, shut up..."
    jen "My fans don't wanna hear your bitching."
    show jenny f_bed_front_laying_sexy_down
    pause
    show jenny f_bed_front_laying_sexy_talk_down
    jen "Oh, really?"
    show jenny f_bed_front_laying_sexy_down
    pause
    show jenny f_bed_front_laying_eyeroll
    jen "{b}*Sigh*{/b} Again?!"
    show jenny f_bed_front_laying_sexy_down
    pause
    show jenny f_bed_front_laying_sexy_talk_down
    jen "Well, I'm not going to do it unless you guys-"
    show jenny f_bed_front_laying_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_front_laying_surprised_down_talk
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "For fucks sake..."
    show jenny f_bed_front_laying_sexy_down
    player_name "Now what's happening?"
    show jenny f_bed_front_laying_sexy_talk_down
    jen "You're about to get your cock sucked again."
    show jenny f_bed_front_laying_sexy_down
    player_name "R-really?"
    player_name "That's awe-"
    show jenny b_bed_pussy1 f_bed_pussy1_sexy_down
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    with dissolve
    player_name "Srrrmmmph!"
    show jenny f_bed_pussy1_sexy_talk_down
    jen "Shut up!"
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    show expression AnimatedImage("jenny_bj", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
    player_name "Nnnrrrmmph-" with hpunch
    jen "{b}*Gluullggh*{/b}"
    jump jenny_bj_loop

label jenny_bj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_bj", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_bj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_bj {}".format(pose_list[pose_counter]) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_bj_hscene_dialog")
        $ animcounter += 1
    call screen jenny_bj_options

label jenny_bj_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        jen "Mmm.{p=1}{nw}"
    if animcounter == 1 and randomizer() > 50:
        jen "{b}*Slurp*{/b}{p=1}{nw}"
    if animcounter == 2 and randomizer() < 50:
        player_name "...{p=1}{nw}"
    if animcounter == 3 and randomizer() > 50:
        jen "{b}*Slurrrrrp*{/b}{p=1}{nw}"
    return

label jenny_bj_cum:
    player_name "Jrrnnnneeeee!"
    player_name "mmy grrn krrrwwws!!"
    pause
    player_name "Jrrnnnneeeee!!!"
    pause
    show jenny_bj cum
    player_name "HrrrNNGGG!!!" with flash
    jen "!!!"
    pause
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    show player b_bed_jenny_laying_undies_arms f_empty a_empty of_bed_jenny_laying_undies_arms_mask oh_bed_jenny_laying_undies_handcuffs od_bed_jenny_laying_dick3 at Position (align=(0,0))
    show jenny b_bed_front_sit a_bed_front_sit_shocked f_bed_front_sit_cheeks_surprised o_laptop at Position (align=(0,0))
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick3.png"
    with dissolve
    jen "{b}*Gulp*{/b}"
    show jenny f_bed_front_sit_cheeks_angry
    jen "{b}*Cough* *Sputter* *Cough*{/b}"
    if M_jenny.is_state(S_jenny_start_camshow_blowjob):
        show jenny b_bed_back_sit f_empty a_bed_back_sit_hips with dissolve
        jen "God damnit!!"
        jen "You came right down my fucking throat!"
        show jenny b_bed_climbing a_empty with dissolve
        jen "Eugh, I swallowed a bunch of it!"
        show jenny b_bed_side f_bedside_angry a_bed_side_laptop with dissolve
        player_name "I tried to warn you..."
        show jenny f_bedside_angry_talk
        jen "Bullshit, I didn't hear anything!"
        show jenny f_bedside_angry
        player_name "Yeah, probably because you were humping my face!"
        show jenny f_bedside_angry_talk
        jen "Tch, whatever..."
        show jenny b_bed_side_laptop f_bedside_laptop_gross_down with dissolve
        pause
        show jenny f_bedside_laptop_gross_down_talk
        jen "Grr, it's not funny!"
        jen "It's disgusting!"
        show jenny f_bedside_laptop_gross_down
        pause
        show jenny f_bedside_laptop_gross_down_talk
        jen "Ugh, you're all assholes!"
        jen "Shows over!"
        show jenny f_bedside_laptop_gross_down
        scene black with fade
        pause
        scene expression player.location.background_closeup with None
        show jenny b_naked a_naked_hips f_angry_talk
        show player 101e at left
        with dissolve
        jen "Unbelievable!"
        show jenny f_angry
        show player 101
        player_name "I really did try to warn-"
        show player 101e
        show jenny f_angry_talk
        jen "I don't wanna hear it!"
        jen "Just shut up!"
        show jenny f_gross_down_talk
        jen "Eugh, I gotta go brush my fucking teeth!"
        hide jenny with dissolve
        pause
        show player 101g
        player_name "Hey, what about my money?!"
        show player 100
        pause
        player_name "( Hmm, I guess I'll just ask her about it tomorrow. )"
        $ M_jenny.trigger(T_jenny_done_camshow_blowjob)
    else:
        show jenny b_bed_back_sit f_empty a_bed_back_sit_hips with dissolve
        jen "Phew, happy now?"
        player_name "I warned you again!"
        jen "I know."
        pause
        jen "I just wasn't expecting so much..."
        show jenny b_bed_climbing a_empty with dissolve
        player_name "W-wait, so you-"
        show jenny b_bed_side_laptop f_bedside_laptop_sexy_talk_down a_bed_side_laptop with dissolve
        jen "Shows over boys!"
        jen "Thanks for tuning in!"
        show jenny f_bedside_laptop_sexy_down
        pause
        show jenny f_bedside_laptop_sexy_talk_down
        jen "Hehe, we'll see you next time!"
        show jenny f_bedside_laptop_sexy_talk_down
        scene black with fade
        pause
        scene expression player.location.background_closeup with None
        show jenny b_naked a_naked_hips f_normal
        show player 101c at left
        with dissolve
        player_name "Y-you swallowed on purpose?"
        show player 100c
        show jenny f_upset_talk
        jen "Yeah?"
        show jenny f_upset
        show player 101e
        player_name "!!!"
        show jenny f_upset_talk
        jen "Don't get any ideas, it's just what the fans want to see..."
        show jenny f_upset
        show player 101c
        player_name "O-oh."
        show player 100c
        show jenny f_upset_talk a_naked_money with dissolve
        jen "Here's your cut."
        call screen money_popup(amount=100)
        $ player.get_money(100)
        show jenny f_upset a_naked_side with dissolve
        show player 101c
        player_name "Thanks."
        show player 100c
        show jenny f_angry_talk
        jen "Now get the fuck out!"
        hide jenny with dissolve
        jen "Eugh, I need some mouth wash!"
        player_name "..."
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["09_unlocked"] = True
    $ player.go_to(L_home_hallway)
    $ game.timer.tick()
    $ game.main()

label jenny_couch_fj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_couch_dick_rub", [1,2,3], M_jenny) as jenny_couch_dick_rub at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_couch_fj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_couch_dick_rub {}".format(pose_list[pose_counter]) as jenny_couch_dick_rub at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_couch_fj_hscene_dialog")
        $ animcounter += 1
    call screen jenny_couch_fj_options

label jenny_couch_fj_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        show jenny f_couch_sit_sexy_talk_down
        jen "Does it feel good?{p=1}{nw}"
        show jenny f_couch_sit_sexy_down
        show player f_couch_sit_down_talk
        player_name "Yes.{p=1}{nw}"
        show player f_couch_sit_down
    if animcounter == 1 and randomizer() < 10:
        show jenny f_couch_sit_sexy_talk_down
        jen "Are you getting close?{p=1}{nw}"
        show jenny f_couch_sit_sexy_down
        show player f_couch_sit_down_talk
        player_name "Y-yes.{p=1}{nw}"
        show player f_couch_sit_down
    if animcounter == 2 and randomizer() < 10:
        show player f_couch_sit_right_talk
        if randomizer() > 50:
            player_name "You're really good at this!{p=2}{nw}"
        else:
            player_name "Holy crap!{p=1}{nw}"
        show player f_couch_sit_down
        show jenny f_couch_sit_laugh
        jen "Hehehe!{p=1}{nw}"
        show jenny f_couch_sit_sexy_down
    return

label jenny_couch_fj_cum:
    if M_jenny.finished_state(S_jenny_catch_her_jilling):
        show player f_couch_sit_down_surprised
        player_name "Here it comes!"
        pause
        show player f_couch_sit_down_surprised
    show player f_couch_sit_down_surprised
    hide jenny_couch_dick_rub
    show jenny a_couch_dick3
    player_name "HNNGGG!!!" with flash
    show jenny_player_couch_cum zorder 3 with dissolve
    show player f_couch_sit_down
    pause
    show player f_couch_sit_right
    show jenny f_couch_sit_laugh
    jen "Pfft, hahaha!"
    hide jenny_player_couch_cum
    show player a_couch_boner
    show jenny a_couch_after2 f_couch_sit_sexy_talk_down
    with dissolve
    if M_jenny.is_state(S_jenny_catch_her_jilling):
        $ M_jenny.trigger(T_jenny_gave_footjob)
        jen "I just made you cum with my feet!"
        jen "I'm like, a total sex goddess!!"
        show jenny a_couch_after1 f_couch_sit_sexy_down with dissolve
        show player f_couch_sit_right_talk
        player_name "That was amazing!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk_down
        jen "I know, right?"
        jen "You're welcome, loser."
        show jenny b_couch_transition f_empty a_empty zorder 0 with dissolve
        show player f_couch_sit_right_talk
        player_name "Where are you going?"
        show player f_couch_sit_right
        show jenny b_couch_sit a_couch_rest f_couch_sit_sexy_talk with dissolve
        jen "Umm, to wash my feet?"
        show jenny a_couch_after2 with dissolve
        jen "Unless you wanna clean them with your tongue?"
    else:
        jen "Sheesh, look at the mess you made of my pretty little feet!"
        jen "You sure you don't wanna clean them up with your tongue?!"
    show jenny f_couch_sit_sexy a_couch_after1 with dissolve
    if M_jenny.get("dominance") <= 0:
        show player f_couch_sit_right_talk
        player_name "Please, don't make me do that..."
        show player f_couch_sit_right
        show jenny f_couch_sit_laugh
        jen "Hahaha!"
        show jenny f_couch_sit_sexy_talk
        jen "Don't ask stupid questions then."
    else:
        show player f_couch_sit_right_talk
        player_name "Eugh, no way!"
        show player f_couch_sit_right
        show jenny f_couch_sit_laugh
        jen "Hahaha!"
        show jenny f_couch_sit_sexy_talk
        jen "Aww, c'mon..."
        show jenny f_couch_sit_sexy a_couch_after2 with dissolve
        jen "Lick my toes, {b}[firstname]{/b}!"
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Forget it!"
        show player f_couch_sit_right
        show jenny f_couch_sit_laugh
        jen "Hahaha!"
        show jenny f_couch_sit_sexy_talk
        jen "Fine."
    jen "I'm going to go take a shower."
    jen "See ya, perv."
    hide jenny with dissolve
    show player f_couch_sit_down
    player_name "( Phew, that was awesome! )"
    show player b_couch_sit_watching f_couch_sit_watching_straight with dissolve
    player_name "( I should turn this off and get to bed before {b}[deb_name]{/b} hears it. )"
    hide player with dissolve
    $ renpy.end_replay()
    $ game.timer.tick()
    $ game.main()

label jenny_computer_video_1:
    scene expression "backgrounds/location_home_jennybedroom_cam1.jpg"
    show jenny b_cam_intro a_cam_intro_cover f_cam_intro_normal_talk
    show expression "characters/jenny/layeredimage/jenny_webcam_border.png"
    with dissolve
    jen "Sorry boys... This next part is for subscribers only."
    jen "You'd better pay quickly if you don't wanna miss out!!"
    show jenny f_cam_intro_normal
    pause
    show jenny f_cam_intro_normal_talk a_cam_intro_reveal with dissolve
    jen "Hehe, alright. Who's ready to get naughty?"
    show jenny a_cam_intro_electro f_cam_intro_normal_talk_left with dissolve
    jen "I've got a nice new toy here... Just for you guys!"
    jen "Mmm, I can't wait to tease my clit with this..."
    show jenny f_cam_intro_normal_left
    pause
    show jenny f_cam_intro_normal_talk
    jen "Why don't you guys give me a little incentive?"
    show jenny f_cam_intro_normal_down
    "{b}*PING*{/b}"
    "{b}*PING*{/b}"
    show jenny f_cam_intro_normal_talk_down
    jen "Oh, c'mon now... You can do better than that, can't you?"
    jen "My pussy's absolutely aching for some attention..."
    show jenny f_cam_intro_normal_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_cam_intro_normal_talk_down
    jen "Hehe, that's better!"
    show jenny f_cam_intro_normal_down
    pause
    show jenny b_cam_electro_talk a_empty f_empty with dissolve
    jen "Ah, I'm so wet..."
    show expression AnimatedImage("jenny_electro", [1,2,3,4], M_jenny) as jenny with dissolve
    jen "Oh, yes!"
    pause
    jen "It's so good!"
    pause
    jen "Mmm, c'mon boys, I need more love!"
    "{b}*PING*{/b} {b}*PING*{/b}"
    jen "That's it! I'm getting closer!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny b_cam_electro_insert a_empty f_empty
    jen "Ahh!!" with hpunch
    pause
    show jenny b_cam_electro_talk with dissolve
    jen "Hehe! How was that?!"
    scene expression game.timer.image("backgrounds/location_home_bedroom_desk_cam{}.jpg") as cutscene
    show player 311 at Position(xpos = 672)
    with dissolve
    jen "Hmm, you want me to get something bigger next time?"
    pause
    jen "Anal?!"
    jen "You seriously want me to stick something up my ass, {b}sam9{/b}?"
    jen "Tch, you guys are so demanding!"
    pause
    jen "Hmm, if I get thirty more subscribers, I'll get something bigger, okay?"
    pause
    jen "Yes, I promise."
    pause
    jen "I don't know about the anal, {b}sam9{/b}... We'll see..."
    pause
    player_name "( Wow, that was pretty hot! )"
    player_name "( I should see what else she has... )"
    hide cutscene
    hide player
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["03_unlocked"] = True
    return

label jenny_computer_video_2:
    scene expression "backgrounds/location_home_jennybedroom_cam1.jpg"
    show jenny b_cam_intro a_cam_intro_cover f_cam_intro_normal_talk
    show expression "characters/jenny/layeredimage/jenny_webcam_border.png"
    with dissolve
    jen "Sorry boys... This next part is for subscribers only."
    jen "You can still get in and watch if you hurry!!"
    show jenny f_cam_intro_normal
    pause
    show jenny f_cam_intro_normal_talk a_cam_intro_reveal with dissolve
    jen "Hehe, alright. I made a promise to you guys, didn't I?"
    show jenny a_cam_intro_vibrate f_cam_intro_normal_talk_left with dissolve
    jen "What do you think of this big guy, huh?"
    jen "I told you all I would get something bigger."
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk_down a_cam_intro_back with dissolve
    jen "No, {b}sam9{/b}... It's not going in my butt."
    jen "Yes, yes... Maybe in the future, we'll see."
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk_down
    jen "Now how about some incentive for your sex goddess?"
    show jenny f_cam_intro_normal_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_cam_intro_normal_talk_down
    jen "Hehe, that's what I like to see!"
    jen "Just a little bit more!"
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk_down a_cam_intro_vibrate with dissolve
    jen "Don't you wanna see me cum all over this toy?"
    show jenny f_cam_intro_normal_down
    "{b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_cam_intro_normal_talk_down
    jen "There we go!"
    show jenny f_cam_intro_normal_down
    pause
    show jenny b_cam_vibrate_talk a_empty f_empty with dissolve
    jen "Hehe, I don't know if it will fit inside my tight little pussy..."
    show expression AnimatedImage("jenny_vibrate", [1,2,3,4], M_jenny) as jenny with dissolve
    pause
    jen "Oh, fuck..."
    pause
    jen "Haah!"
    pause
    jen "Mmm, c'mon boys, show me the money!"
    "{b}*PING*{/b} {b}*PING*{/b}"
    jen "That's it! It feels so good!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "I'm getting close!!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Oh fuck yes!!"
    show jenny b_cam_vibrate_cum1 a_empty f_empty
    jen "Ahh!!" with hpunch
    pause
    pause
    show jenny b_cam_vibrate_cum2 with dissolve
    jen "Hehe, I think I made a mess..."
    scene expression game.timer.image("backgrounds/location_home_bedroom_desk_cam{}.jpg") as cutscene
    show player 311 at Position(xpos = 672)
    with dissolve
    player_name "( Wow, did she just squirt?! )"
    jen "I guess, I'll have to wash my sheets..."
    pause
    jen "What?!"
    jen "I'm not sending you my sheets!"
    pause
    jen "You'll pay me how much?"
    pause
    jen "I'll think about it..."
    jen "For now, I just wanna-"
    jen "Hmm?"
    pause
    jen "You guys want to see me with a real penis?"
    pause
    jen "Maaaaybe..."
    pause
    jen "Hah, {b}sam9{/b} wants to see me with a real penis, in my ass... Big surprise."
    pause
    jen "You guys are dorks."
    player_name "( Wow, I can see why she's making money doing this... )"
    jen "I'll see you boys soon, okay?"
    player_name "( Hmm, I guess that's it for that video. )"
    hide cutscene
    hide player
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["04_unlocked"] = True
    return

label jenny_computer_video_3:
    scene expression "backgrounds/location_home_jennybedroom_cam1.jpg"
    show jenny b_cam_intro a_cam_intro_cover f_cam_intro_normal_talk
    show expression "characters/jenny/layeredimage/jenny_webcam_border.png"
    with dissolve
    jen "Sorry boys... This next part is for subscribers only."
    jen "You guys should really pay up and join us today!"
    jen "Spoiler alert!"
    show jenny a_cam_intro_monster f_cam_intro_normal_talk_left with dissolve
    jen "This thing is going inside me today!"
    jen "I hope to see you there!"
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk_down a_cam_intro_back with dissolve
    jen "Hehe, alright. Let's wait just a second and see if anyone else joins..."
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk_down
    jen "Yes, I'm serious!"
    jen "I'm gonna fuck myself silly on this monster!"
    show jenny f_cam_intro_normal
    pause
    show jenny f_cam_intro_normal_talk
    jen "Ugh, yeah... Alright, {b}sam9{/b}. I'll put it in."
    jen "You see that guys?"
    jen "I give {b}sam9{/b} what he wants because he's always so generous with his tips!"
    show jenny f_cam_intro_normal
    pause
    show jenny f_cam_intro_normal_talk
    jen "That's right, tip more and you'll get what you want too."
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk_down
    jen "Holy shit, we've got almost two-hundred new subs in here for this show!"
    jen "I guess you guys are thirsty for your sex goddess, huh?"
    show jenny f_cam_intro_normal_down
    pause
    show jenny f_cam_intro_normal_talk
    jen "Okay, first things first..."
    show jenny b_cam_monster_talk a_empty f_empty with dissolve
    jen "This is for {b}sam9{/b}!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny b_cam_monster_talk2 with dissolve
    jen "NGGGHHH!!"
    jen "Fucking sam!"
    pause
    jen "Yeah, I know... It's growing on me."
    pause
    jen "I just said I like it, didn't I?!"
    jen "Pay attention, dummy!"
    pause
    jen "No, that doesn't mean I'm getting something bigger."
    pause
    jen "Alright, enough with the anal stuff..."
    show jenny b_cam_monster_talk3 with dissolve
    jen "It's time for the main event!"
    pause
    jen "Are you boys ready?"
    "{b}*PING*{/b} {b}*PING*{/b}"
    jen "I can't hear you!!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Hehe, here we go!"
    pause
    show jenny b_cam_monster_anim1 with dissolve
    jen "Haah..."
    show jenny b_cam_monster_anim2 with dissolve
    jen "Oh my god..."
    jen "It's fucking huge!"
    pause
    show jenny b_cam_monster_anim3 with dissolve
    jen "Holy shit!!!"
    pause
    jen "Okay..."
    $ M_jenny.set("sex speed", 0.175)
    show expression AnimatedImage("jenny_monster", [4,1,2,3], M_jenny) as jenny with dissolve
    pause
    jen "Ahh!!"
    pause
    jen "Oh, yes, yes, YES!!!"
    pause
    jen "Oh my god you guys, this is amazing!"
    "{b}*PING*{/b} {b}*PING*{/b}"
    pause
    jen "AH FUCK!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "I'm gonna cum!!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "YES!!"
    $ M_jenny.set("sex speed", 0.6)
    show expression AnimatedImage("jenny_monster", [2,3], M_jenny) as jenny
    jen "Ngghhh!!!" with hpunch
    pause
    show jenny b_cam_monster_after f_empty a_empty with dissolve
    pause
    jen "Haah... haah..."
    jen "Wow, that was-"
    pause
    scene expression game.timer.image("backgrounds/location_home_bedroom_desk_cam{}.jpg") as cutscene
    show player 311 at Position(xpos = 672)
    with dissolve
    player_name "( Holy crap! )"
    jen "Oh my god, look at how much I'm shaking..."
    pause
    jen "Phew, just give me a second."
    pause
    jen "Hahaha! I told you guys it was gonna be worth it."
    pause
    jen "I know, right?"
    pause
    jen "Yeah, I know you want to see me ride a real dick..."
    jen "It's coming, okay?"
    jen "Just have your wallets ready, cause I'm expecting a LOT of tips for that show."
    pause
    jen "Hehe, yeah."
    pause
    jen "You're welcome, {b}sam9{/b}."
    pause
    jen "Yeah, I'll see you all next time."
    pause
    jen "Buh bye, boys."
    player_name "( Totally worth it. )"
    player_name "( That was awesome! )"
    hide cutscene
    hide player
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["05_unlocked"] = True
    return

label jenny_hj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_hj", [1,2,3,4,5,4,3,2], M_jenny) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_hj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,4,3,2]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_hj {}".format(pose_list[pose_counter]) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_hj_hscene_dialog")
        $ animcounter += 1
    call screen jenny_hj_options

label jenny_hj_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        player_name "Holy crap!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        player_name "Oh my god!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "Mmm, I can feel it throbbing...{p=2}{nw}"
        "{b}*PING*{/b} {b}*PING*{/b}{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        player_name "I'm getting close...{p=2}{nw}"
        if M_jenny.get("sex speed") > 0.051:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.025)
        player_name "Oh my god!{p=1}{nw}"
    return

label jenny_hj_cum:
    if M_jenny.is_state(S_jenny_start_camshow_handjob):
        jen "I wonder what else I shou-"
        hide jenny_hj
        show jenny_hj_mc cum
        player_name "HNNGGG!!!{p=1}{nw}" with flash
        show jenny_hj_cum
        jen "{b}*Gasp*{/b}"
        pause
        jen "What the fuck!"
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        player_name "Phew..."
        scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
        show player b_bed_jenny_laying a_empty f_empty od_bed_jenny_laying_dick3 of_bed_jenny_laying_mask
        show jenny b_bed_side f_bedside_angry_talk o_laptop a_bed_side_cum at Position (align=(0,0))
        with dissolve
        jen "Why didn't you warn me!"
        show jenny f_bedside_angry
        player_name "You didn't tell me to warn you..."
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        show jenny f_bedside_angry_talk
        jen "Well, I thought that was fucking obvious you moron!"
        jen "Oh my god, it's everywhere!"
        show jenny f_bedside_angry
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        show jenny f_bedside_angry_talk
        jen "Ugh, okay... Stream's over!"
        show jenny f_bedside_angry
        player_name "B-but they're still tipping-"
        show jenny f_bedside_angry_talk
        jen "GET THE FUCK OUT OF MY ROOM!"
        show jenny f_bedside_angry
        player_name "Okay, okay..."
        hide player with dissolve
        show jenny f_bedside_gross_down_talk
        jen "Eugh."
        show jenny f_bedside_gross_down
        pause
        show jenny b_bed_side_laptop f_bedside_laptop_gross_down_talk with dissolve
        jen "It's not funny!"
        show jenny f_bedside_laptop_gross_down
        scene black with fade
        pause
        $ game.timer.tick()
        $ M_jenny.trigger(T_jenny_gave_handjob)
        $ player.go_to(L_home_bedroom)
        scene expression player.location.background_closeup with None
        show player 101h with dissolve
        player_name "( Wow! )"
        player_name "( I can't believe {b}[jen_name]{/b} just jerked me off... )"
        player_name "( That was so hot!! )"
        pause
        show player 100c
        player_name "( Man, I hope I get to do that again! )"
        hide player with dissolve
    else:
        player_name "Here it comes!"
        jen "Hmm?"
        hide jenny_hj
        show jenny_hj_mc cum
        player_name "HNNGGG!!!{p=1}{nw}" with flash
        show jenny_hj_cum
        jen "!!!"
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
        show player b_bed_jenny_laying a_empty f_empty od_bed_jenny_laying_dick3 of_bed_jenny_laying_mask
        show jenny b_bed_side f_bedside_angry_talk o_laptop a_bed_side_cum at Position (align=(0,0))
        with hpunch
        jen "Again?!"
        jen "God damnit, you asshole!"
        show jenny f_bedside_angry
        player_name "I warned you!"
        show jenny f_bedside_angry_talk
        jen "Well, I wasn't paying attention!"
        show jenny f_bedside_angry
        "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
        show jenny f_bedside_gross_down_talk
        jen "Eugh."
        show jenny b_bed_side_laptop f_bedside_laptop_gross_down_talk with dissolve
        jen "Yeah, yeah... Very funny."
        jen "Show's over pervs!"
        hide jenny
        hide player
        with dissolve
        scene expression player.location.background_closeup with None
        show player 100c at left
        show jenny b_naked f_upset_talk a_naked_hips
        with dissolve
        jen "You're washing my sheets this time!"
        show jenny f_upset
        show player 101c
        player_name "Fine, whatever."
        show player 100c
        show jenny f_upset_talk
        jen "I'm getting in the shower."
        show jenny a_naked_money with dissolve
        jen "Take this and get the fuck out!"
        hide jenny with dissolve
        pause
        show player 101c
        player_name "Sweet!"
        call screen money_popup(50)
        $ player.get_money(50)
        $ game.timer.tick()
        $ player.go_to(L_home_basement)
        scene expression player.location.background_closeup
        show player f_normal_talk
        with fade
        player_name "Phew!"
        player_name "Alright, that's done."
        show player f_normal
        pause
        show player f_laugh
        player_name "Totally worth it!"
        hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
    $ game.main()

label jenny_hj_intro_repeat:
    show jenny f_upset_talk
    jen "Hurry up."
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show player f_surprised
    pause
    show jenny b_panties a_naked_hips f_upset with dissolve
    show jenny f_upset_talk
    jen "Well?"
    show jenny f_grin_down b_naked a_naked_panties_remove with dissolve
    show player f_worried
    player_name "Hmm?"
    show jenny b_naked_panties_remove_down a_empty f_empty with dissolve
    pause
    show jenny b_naked a_naked_hips f_upset_talk with dissolve
    jen "Get those clothes off!"
    show jenny f_upset
    show player f_worried_talk
    player_name "R-right..."
    show player f_worried
    label finger_blasting_hj:
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_cutscene05.jpg" with dissolve
    jen "You know the drill."
    jen "Mask on and keep your mouth shut."
    player_name "Yeah, I remember."
    jen "I'll handle the rest."
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show player b_bed_jenny_sit a_empty f_jenny_bed_sit_shy_down of_jenny_bed_sit_mask at Position (align=(0,0))
    show jenny o_under_body_laptop b_naked_bed_bellytype a_empty f_bed_facing_comp_sexy_talk_down at Position (align=(0,0))
    with dissolve
    jen "Hi again, everybody!"
    show jenny b_naked_bed_belly with dissolve
    jen "I brought my boy toy back to give you guys another show."
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_laugh
    jen "Hehe, of course!"
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Well, let's find out, shall we?"
    show jenny o_laptop b_bed_side a_bed_side_laptop f_bedside_sexy_talk_down
    show player b_bed_jenny_laying f_empty od_bed_jenny_laying_dick1 of_bed_jenny_laying_mask
    with dissolve
    jen "I bet he's good and ready this time."
    show jenny a_bed_side_pull1 f_bedside_sexy_down with dissolve
    pause
    show player od_empty
    show jenny a_bed_side_pull2
    with dissolve
    pause
    show jenny a_bed_side_point
    show player od_bed_jenny_laying_dick4
    with fastdissolve
    show player od_bed_jenny_laying_dick5 with fastdissolve
    show player od_bed_jenny_laying_dick6 with fastdissolve
    jen "!!!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    pause
    show jenny b_bed_side_laptop f_bedside_laptop_sexy_talk_down with dissolve
    jen "Hehe, I know it's big!"
    jen "I wouldn't settle for anything less, would I?"
    show jenny f_bedside_laptop_sexy_down
    pause
    show jenny f_bedside_laptop_sexy_talk_down
    jen "Yeah, I think I should too."
    $ M_jenny.set("sex speed",0.4)
    show jenny b_bed_side f_bedside_sexy_down a_bed_side_jerk with dissolve
    player_name "!!!"
    pause
    player_name "Oh, god!"
    show jenny f_bedside_sexy_talk_down
    jen "Yeah, you like that, don't you?"
    show jenny f_bedside_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    pause
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .1)
    show jenny_hj_mc
    show expression AnimatedImage("jenny_hj", [1,2,3,4,5,4,3,2], M_jenny) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    jen "C'mon, boy toy!!"
    jen "Tell everybody how much you love me stroking your big, hard cock..."
    player_name "I love it!"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Hahaha!"
    pause
    player_name "{b}[jen_name]{/b}, I'm gonna-"
    jen "You boys seeing this?!"
    jen "Hehe, oh you like my big tits, huh?"
    "{b}*PING*{/b} {b}*PING*{/b}"
    jump jenny_hj_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
