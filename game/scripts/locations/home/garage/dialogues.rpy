label home_garage_pick_up_shovel:
    scene expression game.timer.image("backgrounds/location_home_garage{}_blur.jpg")
    show player 244 with dissolve
    player_name "Yeah, this should work!"
    player_name "It'll be nice to have some money for a change..."
    show player 243
    jen "{b}*Ahem*{/b}"
    player_name "!!!" with hpunch
    show player 243 at left
    show jenny 9 at right
    with dissolve
    jen "What are you doing with that shovel?"
    show jenny 9b
    show player 244
    player_name "... Huh?"
    player_name "Oh! I'm taking it to {b}Diane's{/b} house."
    player_name "I'm going to be working for her this summer."
    show player 243
    show jenny 9
    jen "{b}Diane{/b} gave you a job?"
    jen "... She's never offered me any work!"
    show jenny 9b
    show player 14 with dissolve
    player_name "Well, it's physical labor in her garden."
    player_name "She probably just assumed you wouldn't be interested..."
    show player 13
    show jenny 9
    jen "Ugh, in this heat?"
    jen "Yeah, no way. Screw that!"
    show jenny 9b
    show player 10
    player_name "What are you doing in the garage?"
    player_name "You never come out here..."
    show player 5
    show jenny 6d with dissolve
    jen "I need some batteries. Don't we still have some out here?"
    show jenny 6c
    show player 4 with dissolve
    pause
    show player 14 with dissolve
    player_name "Yeah, I think so."
    player_name "Try that box on bottom shelf there."
    show player 13
    pause
    show jenny 16f at Position (xoffset=190) with dissolve
    show player 428
    player_name "!!!"
    pause
    show jenny 182 with dissolve
    show player 12
    player_name "Holy crap, what do you need so many for?"
    show player 5
    show jenny 183
    jen "None of your business, loser!"
    jen "Just take your shovel and beat it."
    show jenny 182
    show player 12
    player_name "Tch, whatever."
    show player 90
    show jenny 183
    jen "Have fun busting your ass for {b}Diane{/b}..."
    show jenny 184
    jen "Hahaha!"
    hide jenny with dissolve
    show player 12
    player_name "... She's such a bitch."
    show player 90
    show screen popup("boxes/popup_item_shovel1.png")
    $ player.get_item("shovel")
    hide player with dissolve
    $ game.main()

label car_dialogue:
    if M_mom.is_state(S_mom_mall_outing):
        call expression game.dialog_select("garage_car_mom_mall_outing")
        jump expression game.dialog_select("mall_dialogue")

    scene expression game.timer.image("home_garage{}")
    if M_mom.is_state(S_mom_check_car):
        $ player.go_to(L_home_car)
        call expression game.dialog_select("garage_car_mom_check_car")
        $ player.location.call_screen(False)
    else:

        if seen_garage_locked:
            call expression game.dialog_select("garage_car_seen")
        else:
            call expression game.dialog_select("garage_car_not_seen")
            $ seen_garage_locked = True
    $ game.main()

label garage_car_mom_mall_outing:
    scene expression "backgrounds/location_car_cutscene01.jpg"
    show expression FilteredText("So we hopped in the car and made our way to the mall.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression FilteredText("I found that time passed quickly when I was with {b}[deb_name]{/b}...") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide cutscene
    show expression FilteredText("... Her pleasant company and infectious smile never failed to brighten my mood.") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide cutscene
    scene black
    with fade
    return

label garage_car_mom_check_car:
    show player 4 with dissolve
    player_name "( She's right. The car doesn't want to start. )"
    show player 5
    player_name "( I'd better check the engine. )"
    if game.timer.is_dark():
        player_name "( It sure is dark in here. )"
    return

label garage_car_seen:
    show player 34 at left with dissolve
    player_name "Hmm..."
    show player 35
    player_name "I don't need to use {b}[deb_name]{/b}'s car."
    hide player 35 with dissolve
    return

label garage_car_not_seen:
    show player 2 at left with dissolve
    player_name "{b}[deb_name]{/b}'s car ... wish I had a reason to drive it..."
    hide player 2 at left with dissolve
    return

label engine_broken:
    call expression game.dialog_select("engine_broken_dialogue")
    $ M_mom.trigger(T_mom_check_engine)
    jump expression game.dialog_select("home_garage")

label engine_broken_dialogue:
    scene expression game.timer.image("home_garage{}")
    show player 23 with dissolve
    player_name "( !!! )"
    show player 22
    player_name "( What the hell?! It looks like someone worked it over with a hammer! )"
    pause
    show player 16
    player_name "( I wonder if this has something to do with those shady guys in the suits? )"
    player_name "( Those Scumbags! )"
    show player 11
    player_name "( There's no way I can fix this. We have to get a whole new engine or something. )"
    player_name "( I should probably tell {b}[deb_name]{/b} about this. She won't be happy! )"
    return

label lawnmower_dialogue:
    $ player.go_to(L_home_garage)
    if M_mom.is_state(S_mom_fill_mower) and not player.has_item("gas_can"):
        if not game.timer.is_dark():
            call expression game.dialog_select("garage_mom_fill_mower_no_gas")
        else:
            call expression game.dialog_select("garage_mom_fill_mower_night")

    elif M_mom.is_state(S_mom_fill_mower) and player.has_item("gas_can"):
        if not game.timer.is_dark():
            call expression game.dialog_select("garage_mom_fill_mower_success")

            $ player.remove_item("gas_can")
            $ M_mom.trigger(T_mom_filled_mower)
            jump expression game.dialog_select("home_front")
        else:

            call expression game.dialog_select("garage_mom_fill_mower_night")
    else:
        call expression game.dialog_select("garage_lawnmower_not_needed")
    $ game.main()

label garage_mom_fill_mower_night:
    scene expression game.timer.image("home_garage{}")
    show player 35f with dissolve
    player_name "( Why would I use the lawn mower at night? I should return during the day... )"
    hide player 35 with dissolve
    return

label garage_mom_fill_mower_no_gas:
    scene home_garage_closeup
    show player 428f at right
    player_name "( I haven’t used a lawn mower in years... do I even remember how to use one? )"
    player_name "( {b}Dad{/b} used to pull the cord and it would start. Let me try that. )"
    scene home_garage_closeup
    show player 197
    with dissolve
    pause
    show player 200 at Position (xpos=566)
    pause
    show player 197 at center
    scene home_garage
    show player 35f
    with dissolve
    player_name "( It must be out of gas. It barely started, so at least I know it’s running. )"
    show player 2f
    player_name "( Well it’s not going to start without gas. I should probably get some from {b}CONSUM-R{/b}. )"
    return

label garage_mom_fill_mower_success:
    scene home_garage_closeup
    show player 202 at Position (xpos=521) with dissolve
    player_name "( I finally have some gas for the mower. )"
    show player 201 at Position (xpos=509)
    player_name "( That should be enough. )"
    show player 196 at Position (xpos=521)
    player_name "Hope this works. I don’t know what else to do after this..."
    show player 197 at center
    pause
    show player 200 at Position (xpos=566)
    pause
    show player 197 at center
    pause
    show player 200 at Position (xpos=566)
    pause
    show player 199 at center
    player_name "Hmm... it's not working. I'll try pulling it a bit harder..."
    show player 200 at Position (xpos=566)
    pause
    show player 198 at center
    player_name "It worked!"
    return

label garage_lawnmower_not_needed:
    scene expression game.timer.image("home_garage{}")
    show player 35 with dissolve
    player_name "( Why would I use the lawn mower? The grass looks fine... )"
    hide player 35 with dissolve
    return

label garage_use_workbench:
    if M_dewitt.is_state(S_dewitt_make_new_flute) and player.has_item("drill") and player.has_item("stick"):
        call expression game.dialog_select("garage_dewitt_make_new_flute")
        $ player.remove_item("broken_flute")
        $ player.remove_item("drill")
        $ player.remove_item("stick")
        $ player.get_item("flute")
        $ game.timer.tick()
        $ M_dewitt.trigger(T_dewitt_fix_flute)

    elif M_dewitt.is_state(S_dewitt_make_replacement_guitar) and player.has_item("paint") and player.has_item("wood_pile"):
        call expression game.dialog_select("garage_dewitt_make_replacement_guitar")
        $ player.remove_item("wood_pile")
        $ player.remove_item("paint")
        $ player.get_item("fake_guitar")
        $ game.timer.tick()
        $ M_dewitt.trigger(T_dewitt_made_replacement_guitar)

    elif M_ross.is_state(S_ross_get_easels) and player.has_item("wood_pile"):
        call expression game.dialog_select("garage_build_easels")
        $ player.remove_item("wood_pile")
        $ player.get_item("easels")
        $ game.timer.tick()
    else:

        call expression game.dialog_select("garage_workbench_not_needed")
    $ game.main()

label garage_dewitt_drill:
    call expression game.dialog_select("garage_dewitt_drill_dialogue")
    $ player.get_item("drill")
    $ game.main()

label garage_dewitt_drill_dialogue:
    scene expression game.timer.image("home_garage{}")
    show player 14 with dissolve
    player_name "Here is an old drill!"
    player_name "The batteries are still charged too."
    show player 12
    player_name "Now I just need to look for {b}a fallen tree branch{/b}."
    hide player with dissolve
    return

label garage_dewitt_make_new_flute:
    scene home_garage_cs1
    with fade
    show text "You know, it was oddly satisfying, building this flute by hand.\nI'm actually pretty excited to play this thing now!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene expression game.timer.image("home_garage{}")
    show player 566 with dissolve
    player_name "There!"
    player_name "Doesn't look all that bad!"
    show player 567
    pause
    show player 566
    player_name "Let's see what it does when I put my lips on it and blow..."
    show player 567d with dissolve
    pause
    show player 566 with dissolve
    player_name "Hey, this thing sounds pretty good!"
    player_name "I bet {b}Ms. Dewitt{/b} is gonna freak out when she see's I built a flute from scratch!"
    hide player with dissolve
    return

label garage_dewitt_find_paint:
    scene expression game.timer.image("home_garage{}")
    show player 32 at Position (xoffset=68) with dissolve
    player_name "I don't see any paint in here..."
    pause
    show player 10 with dissolve
    player_name "Maybe {b}[deb_name]{/b} knows where it went."
    hide player with dissolve
    return

label garage_dewitt_make_replacement_guitar:
    scene home_garage_cs2
    with fade
    show text "You know, I'm really starting to dig all this woodworking.\nPerhaps I should look into becoming a carpentar someday." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene expression game.timer.image("home_garage{}")
    show player 575 with dissolve
    player_name "Yikes! Then again, maybe I'm not as talented as I thought."
    player_name "I hope this is good enough to fool {b}Mrs. Johnson{/b}."
    hide player with dissolve
    return

label garage_build_easels:
    scene location_home_garage_cutscene03
    with fade
    show text "Yeah, I think that looks right." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I hope {b}Miss Ross{/b} likes it!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I really don't want to let her down..." at Position (xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve
    return

label garage_workbench_not_needed:
    scene expression game.timer.image("home_garage{}")
    show player 12 with dissolve
    player_name "( I have no reason to use this right now. )"
    hide player with dissolve
    return

label debbie_car_sex_pre:
    scene car_interior
    show player car 2d
    show player_arms car 1

    show debbie car 4 at right
    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
    show xtra 30 at right
    with dissolve
    return

label debbie_car_sex_pre_first_time:
    pause
    show debbie car 4b
    deb "You know, I really wasn't expecting you to bring me to the car."
    show debbie car 5g
    deb "I was sceptical at first but now that we're sitting here..."
    show player car 3
    deb "... It's kinda turning me on."
    deb "Imagine if we were parked out in public somewhere?!"
    deb "Mmm..."
    deb "I'm getting wet just thinking about it!"
    show debbie car 5f
    show player car 4g
    player_name "I'd be down to try something like that..."
    show player car 5
    player_name "... You wouldn't be embarrassed?"
    show player car 5b
    show debbie car 5c
    show debbie_arms_car 5 at Position(xalign = 0.357, yalign = 0.558)

    deb "..."
    show debbie car 5g
    deb "Heh, I dunno... I would probably be mortified if we got caught!."
    deb "... But..."
    deb "... That's what makes it so exciting, you know?!"
    deb "Well, at least it gets me excited..."
    deb "I'm getting wet just thinking about it!"
    show debbie car 5f
    show player car 4h
    player_name "..."
    show player car 5
    player_name "You are?"
    show player car 5b
    show debbie car 3b
    deb "Hehe, yes..."
    deb "So what are we gonna do about this big, hard cock here?"
    show debbie car 3
    show player car 2d
    return

label debbie_car_sex_pre_repeat:
    show debbie car 4b
    show debbie_arms_car 5c at Position(xalign = 0.357, yalign = 0.558)
    deb "I like feeling this big guy stiffen up in my hand."
    show debbie car 4
    pause
    show player car 4b
    show debbie car 3b
    show debbie_arms_car 5 with dissolve
    deb "Young cocks sure do get hard fast."
    show debbie car 4
    pause
    show player car 2d
    show debbie car 5b with dissolve
    deb "It looks so... Delicious!"
    show debbie car 3b
    deb "Want me to take you in my mouth?"
    show debbie car 3
    return

label debbie_car_sex_jerk_off:
    show player car 2c
    player_name "Just keep doing what you're doing!"
    show player car 2d
    show debbie car 3b
    deb "Alright, sweetie."
    show debbie car 4
    return

label debbie_car_sex_bj:
    show player car 2c
    player_name "Would you... Use your mouth?"
    show player car 2d
    show debbie car 3b
    deb "Absolutely!"
    scene car_interior bj
    show player car 4c
    show player_arms car 1
    show debbie_car_bj 11 at right
    show xtra 30 zorder 2 at right
    with dissolve
    pause
    show debbie_car_bj 12 with dissolve
    pause
    show debbie_car_bj 7
    show player_boner car 3
    with dissolve
    pause
    hide player_boner
    show debbie_car_bj 8 zorder 1 at Position(xalign = 0.93, yalign = 1.0)
    with dissolve
    pause
    show player car 4c
    return

label debbie_car_sex_leave:
    show player car 5
    player_name "I think I'm good for now."
    player_name "That felt good."
    show player car 5b
    show debbie car 5g
    deb "Really?"
    deb "But you haven't even cum yet?"
    show debbie car 5f
    show player car 2
    player_name "That's fine."
    show player car 5b
    show debbie car 5g
    deb "Did I do something wrong?"
    show debbie car 5f
    show player car 2c
    player_name "It was good {b}[deb_name]{/b}! Don't worry."
    player_name "I have to get going is all."
    show player car 5b
    deb "..."
    show debbie car 5g
    deb "Alright..."
    return

label debbie_car_sex:
    $ M_mom.set("sex speed", .175)
    $ animated = False
    call expression game.dialog_select("debbie_car_sex_pre")
    if not M_mom.is_set("car sex"):
        call expression game.dialog_select("debbie_car_sex_pre_first_time")
        $ M_mom.set("car sex", True)
    else:

        call expression game.dialog_select("debbie_car_sex_pre_repeat")
    menu:
        "Jerk me off.":
            $ M_mom.set("car jerk", True)
            call expression game.dialog_select("debbie_car_sex_jerk_off")
            jump expression game.dialog_select("car_mom_sex_loop")
        "Blowjob.":

            $ M_mom.set("car jerk", False)
            call expression game.dialog_select("debbie_car_sex_bj")
            jump expression game.dialog_select("car_mom_sex_loop")

        "Leave." if store._in_replay == None:
            call expression game.dialog_select("debbie_car_sex_leave")
    scene black with fade
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["05_unlocked"] = True
    $ player.go_to(L_home_garage)
    $ game.timer.tick()
    $ game.main()

label car_mom_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_mom.is_set("car jerk"):
                    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                else:
                    show expression AnimatedImage("debbie_car_bj", [8,"8b","8c","8d","8e","8f","8g"], M_mom) as debbie_car_bj zorder 1 at Position(xalign = 0.93, yalign = 1.0)
                $ animated = True
            pause 4
            if animcounter in [1,3]:
                call expression game.dialog_select("car_mom_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            if M_mom.is_set("car jerk"):
                $ pose_list = [5,"5b","5c","5b"]
            else:
                $ pose_list = [8,"8b","8c","8d","8e","8f","8g"]
            $ poses_done = []
            while poses_done != pose_list:
                if M_mom.is_set("car jerk"):
                    show expression "debbie_arms_car {}".format(pose_list[pose_counter]) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                else:
                    show expression "debbie_car_bj {}".format(pose_list[pose_counter]) as debbie_car_bj zorder 1 at Position(xalign = 0.93, yalign = 1.0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("car_mom_hscene_dialog")
        $ animcounter += 1
    call screen car_mom_sex_options

label car_mom_hscene_dialog:
    if M_mom.is_set("car jerk"):
        if animcounter == 3:
            if randomizer() <= 50:
                show debbie car 4b
                show player car 5b
                deb "I can't believe your cock is so big!{p=2}{nw}"
                deb "I love how soft it feels.{p=2}{nw}"
                show debbie car 4
            else:

                show debbie car 5b
                show player car 5b
                deb "I just love your big cock!?{p=2}{nw}"
                deb "Cum for me, {b}[firstname]{/b}!{p=2}{nw}"
                show player car 4b
                pause 1
                show debbie car 4
                show player car 4c
                player_name "Okay...{p=2}{nw}"
                show player car 4h
    else:
        if animcounter == 1:
            deb "Mmmm...{p=1}{nw}"

        elif animcounter == 3:
            player_name "Oh...{p=1}{nw}"
            show player car 4d
            player_name "Right there, {b}[deb_name]{/b}.{p=2}{nw}"
            show player car 4c
    return

label car_mom_faster_dialogue:
    show player car 4c
    player_name "Faster, {b}[deb_name]{/b}."
    show player car 4h
    jump expression game.dialog_select("car_mom_sex_loop")

label car_mom_slower_dialogue:
    show player car 4c
    player_name "Go slower..."
    show player car 4h
    jump expression game.dialog_select("car_mom_sex_loop")

label car_mom_sex_cum:
    if M_mom.is_set("car jerk"):
        call expression game.dialog_select("car_mom_jerk_cum")
    else:
        call expression game.dialog_select("car_mom_bj_cum")
    scene black with fade
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["05_unlocked"] = True
    $ player.go_to(L_home_garage)
    $ game.timer.tick()
    $ game.main()

label car_mom_jerk_cum:
    show player car 4c
    pause
    show player car 4d
    show player_arms car 2
    show debbie_arms_car 5d at Position(xalign = 0.357, yalign = 0.558)
    with dissolve
    player_name "( !!! )"
    show debbie car 4b
    deb "Whoa!!!"
    show debbie car 5b
    deb "Oh, sweetie!"
    show player car 2b
    show player_arms car 1 with dissolve
    deb "I always forget just how big your loads are!"
    show debbie car 4b
    deb "At least we didn't get any on the car..."
    show debbie car 3
    show player car 2c
    player_name "That was great..."
    scene car_interior kiss
    show debbie car 6 at right
    show player_boner car 1b
    show xtra 30 at right
    with dissolve
    pause
    scene car_interior
    show player car 2c
    show player_arms car 1
    show player_boner car 1b
    show debbie car 3 at right
    show debbie_arms_car 1
    show xtra 30 at right
    with dissolve
    player_name "Thanks, {b}[deb_name]{/b}."
    show player car 2d
    show debbie car 3b
    deb "You're welcome, sweetie."
    show debbie car 4b
    deb "Let's head back inside before {b}[jen_name]{/b} starts wondering where we snuck off to."
    show debbie car 3b
    deb "I don't want her to find out what we're doing out here!"
    return

label car_mom_bj_cum:
    show player_arms car 2
    show player car 4d
    player_name "{b}[deb_name]{/b}, I'm gonna..."
    player_name "( !!! )"
    show debbie_car_bj 9
    show player_arms car 2
    with flash
    deb "Mmmmph!!"
    scene car_interior
    show player car 4d
    show player_arms car 1
    show player_boner car 2
    show debbie_car_bj 10 at right
    show xtra 30 at right
    with dissolve
    pause
    show player car 2d
    deb "{b}*Gulp*{/b}"
    deb "... {b}*Gulp*{/b}"
    show debbie car 2 at right
    hide debbie_arms_car
    show debbie_arms_car 1
    hide xtra
    show xtra 30 at right
    with dissolve
    pause
    show debbie car 3b
    deb "Wow! That was so much!"
    deb "Phew... I guess I won't have much of an appetite at dinner tonight."
    show debbie car 3
    show player car 2c
    player_name "That was awesome! You're so good at that!"
    show player car 2d
    show debbie car 3b
    deb "Hehe, well I'm glad you enjoy it, {b}[firstname]{/b}. Cause I love sucking your cock!"
    show debbie car 3b
    deb "Let's head back inside before {b}[jen_name]{/b} starts wondering where we snuck off to."
    show debbie car 3
    show player car 5
    player_name "Alright."
    player_name "Just let me clean myself up first..."
    show player car 3
    show debbie car 3b
    deb "I'll see you in there, sweetie!"
    show player car 5b
    show debbie car 4b
    deb "Don't take too long..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
