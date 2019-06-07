label jenny_dining_room_sex_intro:
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "Shh!!"
    show jenny f_breakfast_grin
    show player f_diningroom_table_surprised_teeth_down
    show debbie b_breakfast_mug a_empty f_breakfast_standing_mug_normal_talk at Position (align=(0,0)) with dissolve
    deb "Did you say something, dear?"
    show debbie f_breakfast_standing_mug_normal
    show jenny f_breakfast_grin_talk
    jen "Would you make me some breakfast?"
    show player f_diningroom_table_shy_down
    show jenny f_breakfast_grin
    show debbie f_breakfast_standing_mug_normal_talk
    deb "You want me to cook for you?"
    show debbie f_breakfast_standing_mug_normal
    show jenny f_breakfast_grin_talk
    jen "Yes."
    show jenny f_breakfast_grin
    show debbie f_breakfast_standing_mug_normal_talk
    deb "Well, of course I will dear!"
    deb "I always worry about you not getting enough to eat-"
    show debbie f_breakfast_standing_mug_sad
    show jenny f_breakfast_eyeroll
    jen "Yeah, I know {b}[deb_name]{/b}... You tell me all the time!"
    show jenny f_breakfast_upset
    show debbie f_breakfast_standing_mug_sad_talk
    deb "R-right... Umm..."
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    show debbie f_breakfast_standing_mug_normal_talk
    deb "I'll whip you up some eggs and bacon right now!"
    show player f_diningroom_table_looking_down_food a_dinner_sitting_resting with dissolve
    show debbie f_breakfast_standing_mug_normal
    show jenny f_breakfast_grin_talk
    jen "Thanks."
    show jenny f_breakfast_grin
    show debbie f_breakfast_standing_mug_normal_talk
    deb "It'll just be a few minutes, dear."
    show player f_diningroom_table_surprised_high_food with None
    show expression "characters/xtra/overlay_o_dinner_mug.png"
    hide debbie
    with dissolve
    show jenny f_breakfast_laugh a_breakfast_dressed_laugh with dissolve
    jen "Hehe..."
    show jenny b_breakfast_gettingup a_empty f_breakfast_getup_grin_down with dissolve
    pause
    show jenny b_breakfast_remove f_empty with dissolve
    if M_jenny.get("first_sex_dining"):
        $ M_jenny.set("first_sex_dining", False)
        show player f_diningroom_table_worried_talk_high
        player_name "Okay, so now wha-"
        show jenny b_breakfast_leaning f_breakfast_lean_grin with dissolve
        show player f_diningroom_table_surprised_teeth_left
        player_name "!!!"
        if M_jenny.get("dominance") <= 0:
            show player f_magic_sit_stand_worried_talk
            player_name "W-we can't-"
            show player f_magic_sit_stand_worried
            show jenny f_breakfast_lean_upset_talk
            jen "{b}*Sigh*{/b} Well, not if you're going to be a little bitch about it..."
            show jenny b_breakfast_remove f_empty with dissolve
            pause 1
            show jenny b_breakfast_gettingup a_empty f_breakfast_getup_upset_talk with dissolve
            jen "... And here I thought you were finally starting to grow a backbone."
            show jenny f_breakfast_getup_upset
            show player f_magic_sit_stand_worried_talk
            player_name "Fine!"
            show jenny b_breakfast_remove f_empty with dissolve
            player_name "Let's just hurry, okay?"
            show player f_magic_sit_stand_worried
            show jenny b_breakfast_leaning f_breakfast_lean_grin_talk with dissolve
            jen "Yeah, yeah... Get your cock out already!"
        else:
            show player f_magic_sit_stand_worried_talk
            player_name "Are you out of your mind?!"
            show player f_magic_sit_stand_worried
            show jenny b_breakfast_standing_panties_down a_breakfast_standing_hips f_breakfast_standing_sexy_talk_down with dissolve
            jen "C'mon, {b}[firstname]{/b}... You know you want to."
            show jenny f_breakfast_standing_sexy_down
            show player f_magic_sit_stand_worried_talk
            player_name "{b}*Sigh*{/b} Fine."
            show player f_magic_sit_stand_worried
            show jenny f_breakfast_standing_sexy_talk_down
            jen "You'd better hurry up, we only have a few minutes..."
            show jenny f_breakfast_standing_sexy_down
            show player f_magic_sit_stand_worried_talk
            player_name "Just shut up and get back down there!"
            show player f_magic_sit_stand_worried
            show jenny b_breakfast_leaning f_breakfast_lean_laugh a_empty with dissolve
            jen "Hehehe!"
            show jenny f_breakfast_lean_grin
    else:
        show player f_magic_sit_stand_worried_talk
        player_name "Why can't we just go upstairs?!"
        show player f_magic_sit_stand_worried
        show jenny f_breakfast_lean_grin_talk b_breakfast_leaning with dissolve
        jen "Just shut up and fuck me, {b}[firstname]{/b}!"
        show jenny f_breakfast_lean_grin
        show player f_diningroom_table_tired_talk
        player_name "{b}*Sigh*{/b}"
        scene black with fade
        pause

label jenny_dining_room_sex_pre_insert:
    scene expression "backgrounds/location_home_diningroom_sex.jpg"
    show jenny_sex_table b_default f_back
    show player_jenny_diningroom_sex pre
    with fade
    player_name "Just don't get too loud..."
    show jenny_sex_table f_back_talk
    jen "Oh, please... I'm pretty sure I can control my-"
    hide jenny_sex_table
    hide player_jenny_diningroom_sex
    show jenny_diningroom_sex insert
    with dissolve
    pause 1
    show jenny_diningroom_sex 1
    jen "SELF!!!" with hpunch
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_diningroom_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
    jen "Oh, fuuuck!"
    player_name "Shhh!!!"
    jen "Ngghhh!"
    pause
    jen "Holy-"
    jen "!!!"
    player_name "You have to be quiet or I'm going to stop!"
    jen "Don't you dare fucking stop!"
    pause
    player_name "You're squeezing me too tight!"
    jen "I can't help it, this is really turning me on!"
    pause
    deb "{b}[jen_name]{/b}?!"
    hide jenny_diningroom_sex
    show jenny_sex_table b_default f_surprised
    show player_jenny_diningroom_sex pre
    with dissolve
    player_name "!!!" with hpunch
    jen "!!!"
    show jenny_sex_table f_angry_talk
    jen "Y-yes?"
    show jenny_sex_table f_angry
    deb "Do you want your eggs scrambled or over easy?"
    show jenny_sex_table f_angry_talk
    jen "Oh, umm... Scrambled is fine!"
    hide jenny_sex_table
    hide player_jenny_diningroom_sex
    show expression AnimatedImage("jenny_diningroom_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0) with hpunch
    deb "Okay, dear."
    jen "Hurry up, {b}[firstname]{/b}!"
    pause
    player_name "I'm getting close."
    jen "Me too!"

label jenny_diningroom_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_diningroom_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_diningroom_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_diningroom_sex {}".format(pose_list[pose_counter]) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_diningroom_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_diningroom_sex_options

label jenny_diningroom_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jen "Ahh!!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jen "It's so good!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jen "FUUUUUCK!!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        player_name "Uhh!{p=1}{nw}"
    return

label jenny_diningroom_sex_cum_inside:
    player_name "Here it comes!"
    jen "Don't stop!!"
    show jenny_diningroom_sex cum
    player_name "HNNGGG!!!" with flash
    show jenny_diningroom_sex cum2
    show xray_jenny_diningroom_table at Position (align=(0,0))
    jen "NGGHHH!!!"
    hide xray_jenny_diningroom_table
    pause
    show jenny_diningroom_sex 1 with dissolve
    player_name "Haah... Haah..."
    jen "Holy shit..."
    player_name "Yeah..."
    jen "Get off me."
    hide jenny_diningroom_sex
    show jenny_sex_table b_default f_angry
    show player_jenny_diningroom_sex after
    with dissolve
    pause
    call call_pregnancy_minigame ("jenny_diningroom_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_diningroom_sex_cum_inside_post_pregnancy:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_standing_panties_down a_breakfast_standing_cum2 f_breakfast_standing_upset_down_talk zorder 1 at Position (align=(0,0))
    show player b_dinner_sitting a_dinner_sitting_resting f_diningroom_table_shy_down zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    show expression "characters/xtra/overlay_o_dinner_mug.png" zorder 2
    with fade
    jen "God damnit, {b}[firstname]{/b}!"
    jen "If I get pregnant I'm going to kill you!"
    show jenny f_breakfast_standing_upset_down a_breakfast_standing_cum1 with dissolve
    show player f_diningroom_table_flirt_talk_left
    player_name "You told me not to stop..."
    show player f_diningroom_table_flirt_left
    show jenny f_breakfast_standing_gross_down_talk
    jen "Yeah but I didn't tell you to cum inside me, did I?"
    show jenny f_breakfast_standing_gross_down
    player_name "..."
    show jenny f_breakfast_standing_gross_down_talk
    jen "Fucking moron..."
    show jenny f_breakfast_standing_gross_down
    show player f_magic_sit_stand_worried_talk
    player_name "Shut up!"
    show player f_magic_sit_stand_worried
    deb "Okay, who's hungry?!"
    show player f_magic_sit_stand_surprised
    show jenny f_breakfast_standing_surprised
    jen "!!!" with hpunch
    show jenny b_breakfast_remove a_empty f_empty with dissolve
    pause
    show jenny b_breakfast_dressed a_breakfast_dressed_spoon f_breakfast_upset_down with dissolve
    show player f_diningroom_table_normal_high
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal_talk zorder 1 at Position (align=(0,0)) with dissolve
    deb "Two eggs scrambled and three strips of bacon, just like you wanted."
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_normal_talk
    jen "T-thanks, {b}[deb_name]{/b}."
    show jenny f_breakfast_normal
    show player f_diningroom_table_shy_down
    show debbie f_breakfast_standing_normal_talk
    deb "You're welcome dear!"
    hide expression "characters/xtra/overlay_o_dinner_mug.png"
    show debbie b_breakfast_sitting a_breakfast_mug f_breakfast_sitting_normal
    with dissolve
    pause
    show debbie f_breakfast_sitting_normal_talk
    deb "{b}[firstname]{/b}, you look tired..."
    deb "Are you feeling okay, sweetie?"
    show debbie f_breakfast_sitting_normal
    show player f_magic_sit_stand_surprised
    player_name "Hmm?"
    show jenny f_breakfast_normal_talk
    jen "He's fine."
    show jenny f_breakfast_normal
    show player f_diningroom_table_normal_talk
    player_name "Yeah, I feel fine."
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "Alright, just make sure you're getting enough rest, okay?"
    show debbie f_breakfast_sitting_normal
    show player f_diningroom_table_normal_talk
    player_name "O-okay."
    show player f_diningroom_table_shy_down
    show debbie a_breakfast_mug_drink f_breakfast_sitting_kiss with dissolve
    pause
    show debbie f_breakfast_sitting_sad_talk a_breakfast_mug with dissolve
    deb "Mmm, does it smell weird in here?"
    show debbie f_breakfast_sitting_sad
    show player f_diningroom_table_worried_talk
    player_name "N-no?"
    show player f_diningroom_table_worried
    show debbie f_breakfast_sitting_normal
    show jenny f_breakfast_normal_talk
    jen "I don't smell anything."
    show jenny f_breakfast_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "Hmm, something smells funny..."
    show debbie f_breakfast_sitting_normal
    show jenny f_breakfast_laugh a_breakfast_dressed_phone with dissolve
    show player f_diningroom_table_worried_talk
    player_name "Y-yeah, I dunno {b}[deb_name]{/b}..."
    show player f_diningroom_table_worried
    jen "Hehehe!"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["15_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_diningroom)
    $ game.main()

label jenny_diningroom_sex_cum_outside:
    player_name "Here it comes!"
    jen "Don't stop!!"
    hide jenny_diningroom_sex
    show jenny_sex_table b_default f_angry
    show player_jenny_diningroom_sex after
    with dissolve
    pause
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_standing_panties_down a_breakfast_standing_hips f_breakfast_standing_gross_down_talk zorder 1 at Position (align=(0,0))
    show player b_dinner_standing_cumming a_empty f_diningroom_table_cum_surprised_teeth_down zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with fade
    jen "What the fuck, {b}[firstname]{/b}?!"
    show jenny f_breakfast_standing_gross_down
    show player f_diningroom_table_cum_brag
    player_name "HNNGGG!!!" with flash
    show jenny f_breakfast_standing_gross_down_talk
    jen "I told you not to stop!"
    show player f_diningroom_table_cum_surprised_teeth_down
    show jenny f_breakfast_standing_gross_down
    pause
    show player b_dinner_sitting a_dinner_sitting_resting f_diningroom_table_tired_talk zorder 0 at Position(align=(0,0))
    show expression "characters/xtra/overlay_o_dinner_mug.png" zorder 2
    with dissolve
    player_name "Haah... Haah..."
    show player f_magic_sit_stand_worried_talk
    player_name "What do you want me to do, {b}[jen_name]{/b}?!"
    player_name "Am I supposed to cum inside you?!"
    show player f_magic_sit_stand_worried
    show jenny b_breakfast_remove a_empty f_empty with dissolve
    pause
    show jenny b_breakfast_dressed a_breakfast_dressed_spoon f_breakfast_upset_talk with dissolve
    jen "N-no..."
    jen "{b}*Sigh*{/b} It just would have been nice to finish, asshole!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Shut up!"
    show player f_magic_sit_stand_worried
    deb "Okay, who's hungry?!"
    show player f_magic_sit_stand_surprised
    show jenny f_breakfast_surprised
    jen "!!!" with hpunch
    show player f_diningroom_table_normal_high
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal_talk zorder 1 at Position (align=(0,0)) with dissolve
    deb "Two eggs scrambled and three strips of bacon, just like you wanted."
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_normal_talk
    jen "T-thanks, {b}[deb_name]{/b}."
    show jenny f_breakfast_normal
    show debbie f_breakfast_standing_normal_talk
    show player f_diningroom_table_shy_down
    deb "You're welcome dear!"
    hide expression "characters/xtra/overlay_o_dinner_mug.png"
    show debbie b_breakfast_sitting a_breakfast_mug f_breakfast_sitting_normal
    with dissolve
    pause
    show debbie f_breakfast_sitting_normal_talk
    deb "{b}[firstname]{/b}, you look tired..."
    deb "Are you feeling okay, sweetie?"
    show debbie f_breakfast_sitting_normal
    show player f_magic_sit_stand_surprised
    player_name "Hmm?"
    show jenny f_breakfast_normal_talk
    jen "He's fine."
    show jenny f_breakfast_normal
    show player f_diningroom_table_normal_talk
    player_name "Yeah, I feel fine."
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "Alright, just make sure you're getting enough rest, okay?"
    show debbie f_breakfast_sitting_normal
    show player f_diningroom_table_normal_talk
    player_name "O-okay."
    show player f_diningroom_table_surprised_talk
    show jenny f_breakfast_surprised
    show debbie a_breakfast_mug_drink f_breakfast_sitting_kiss with dissolve
    player_name "W-wait-"
    show player f_magic_sit_stand_surprised
    pause
    show jenny f_breakfast_laugh
    show debbie f_breakfast_sitting_gross_talk a_breakfast_mug with dissolve
    deb "Eugh, this coffee tastes awful!"
    show debbie f_breakfast_sitting_gross
    show player f_diningroom_table_worried_talk
    player_name "R-really?"
    show player f_diningroom_table_worried
    show debbie f_breakfast_sitting_gross_talk
    deb "Yeah!"
    show debbie f_breakfast_sitting_gross
    jen "{b}*Snort*{/b}"
    show jenny f_breakfast_grin
    show debbie f_breakfast_sitting_gross_talk
    deb "I don't understand, it tasted fine a few minutes ago..."
    show debbie f_breakfast_sitting_gross
    show player f_diningroom_table_worried_talk
    player_name "W-weird..."
    player_name "You should probably dump it out and get a new cup."
    show player f_diningroom_table_worried
    show debbie f_breakfast_sitting_gross_talk
    deb "Yeah, I think so too."
    deb "Yuck!"
    show debbie f_breakfast_sitting_gross
    show jenny f_breakfast_laugh
    jen "Hehehe!"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["15_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_diningroom)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
