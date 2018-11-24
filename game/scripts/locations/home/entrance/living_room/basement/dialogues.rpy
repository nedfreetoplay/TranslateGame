label basement_mom_wash_clothes:
    scene home_basement_sideview
    show player 324 at Position(xpos=860)
    show debbie 136 at Position(xpos=550,ypos=805)
    deb "... Oh good, you brought those dirty clothes down."
    show debbie 137
    deb "{b}*Giggle*{/b}"
    show player 325
    show debbie 135
    player_name "What's so funny?"
    show player 326
    show debbie 136
    deb "Your clothes! They're a mess!"
    show player 324
    show debbie 137
    deb "You were really working hard out there, huh?"
    show player 325
    show debbie 135
    player_name "Yeah, I should probably have changed into something else before starting..."
    show player 324
    show debbie 136
    deb "It's okay, sweetie! We'll get you all cleaned up."
    deb "Just hand over your clothes and I'll add them to the laundry."
    show player 325
    show debbie 135
    player_name "It's okay, {b}[deb_name]{/b}. I can do it."
    show player 324
    show debbie 136
    deb "It's no problem. I was just getting ready to start a load anyways."
    show debbie 135
    show player 327 at Position(xoffset=-27) with fastdissolve
    pause

    scene expression "backgrounds/location_home_basement_cutscene.jpg"
    show expression FilteredText("It was a little embarrassing stripping down in front of {b}[deb_name]{/b}. \nShe didn't seem to notice though. She just hurriedly stuffed my clothes into the machine. \nI couldn't help but notice the view as she went about her work.\nNeedless to say, I forgot my embarrassment rather quickly...") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade

    scene home_basement_sideview
    show player 330 at Position(xpos=860)
    show debbie 142 at Position(xpos=550,ypos=805)
    with fade
    deb "( He's probably going to wear those stinky boxers all day now. )"
    deb "( I should add them too. Otherwise they might end up laying on his floor for the next week... )"
    show debbie 136
    deb "Boxers too, {b}[firstname]{/b}."
    show player 332
    deb "Might as well get it all done now."
    show debbie 135
    player_name "( !!! )"
    show player 331
    player_name "Really? No, It's okay. I'll just toss them in the dirty clothes basket upstairs..."
    show debbie 136
    show player 330
    deb "Don't be silly, you're here now. Let's just toss them in and you can go have a shower!"
    show debbie 135
    show player 333
    player_name "... Yeah, but-"
    show debbie 136
    show player 330
    deb "No need to feel embarrassed. It's nothing I haven't seen a million times before."
    deb "Let's just hurry up and get it over with."
    show debbie 138
    show player 334 with fastdissolve
    pause
    show player 335 with fastdissolve
    pause
    show player 336 with fastdissolve
    pause 0.1
    show debbie 139
    show player 337 at Position(xpos=855) with vpunch
    pause
    show debbie 140
    show player 338 at Position(xpos=853)
    deb "Oh my..."
    deb "..."
    deb "Wow! That's umm... That's..."
    deb "Let me grab something for you to cover yourself up."
    show debbie 141 with fastdissolve
    pause
    show player 339 at Position(xpos=845)
    show debbie 142
    with fastdissolve
    pause
    show player 341
    player_name "I'm sorry, {b}[deb_name]{/b}."
    show player 340
    show debbie 143
    deb "Heh, not a problem, sweetie."
    deb "These things happen."
    show debbie 140
    deb "It's perfectly natural."
    show debbie 142
    deb "Heh."
    show debbie 143
    deb "That hand towel isn't really equal to the task is it?"
    deb "Sorry I don't have anything larger down here..."
    deb "You'd best run along now and take your shower."
    show debbie 142
    show player 341
    player_name "Yes, Ma'am"
    hide player with dissolve

    show debbie 139
    deb "( Goodness... )"
    deb "( ... I had no idea he was so... Gifted. )"
    scene black with fade
    return

label basement_mom_close_valve:
    scene home_basement
    show player 34 with dissolve
    player_name "( The water valve should be next to the water heater. )"
    player_name "( I'd better shut it off before the upstairs floods. )"
    hide player with dissolve
    return

label basement_mom_give_laundry:
    scene home_basement_c
    show debbie 125 at right
    show player 277 at left
    with dissolve
    player_name "Oh, there you are!"
    show player 276
    player_name "I brought your laundry down like you asked."
    show player 13
    show debbie 121
    with dissolve
    pause
    show debbie 123
    deb "Thanks, sweetie."
    deb "That was just an excuse to get you down here..."
    show debbie 124
    show player 10
    player_name "Oh? What are you up to?"
    show player 5
    show debbie 123
    deb "Hehe..."
    show debbie 63 with dissolve
    deb "I left you that note this morning because I wanted to see you before you leave."
    show debbie 61
    show player 11
    player_name "Huh?"
    show debbie 39
    deb "I want you, {b}[firstname]{/b}!"
    show debbie 62
    show player 1
    deb "I want to ride that big cock of yours!"
    show debbie 61
    show player 2
    player_name "SSS-Sure!"
    show player 13
    show debbie 62
    deb "Get those clothes off!"
    show player 11
    show debbie 125
    player_name "( !!! )"
    show player 297
    player_name "Y-Yes, Ma'am!"
    show player 13
    show debbie 62
    deb "{b}[jen_name]{/b} won't find us down here."
    show player 21
    show debbie 125
    player_name "Well... okay."
    return

label basement_mom_sex:
    $ M_mom.set("sex speed", .175)
    $ player.go_to(L_home_basement)
    $ cum = False
    $ anim_toggle = True
    $ animated = False
    $ xray = False
    if not M_mom.is_state(S_mom_give_laundry) and randomizer() <= 50:
        $ mom_basement_rand = True
    else:
        $ mom_basement_rand = False
    call expression game.dialog_select("basement_mom_sex_pre")
    jump expression game.dialog_select("basement_mom_sex_loop")

label basement_mom_sex_pre:
    if mom_basement_rand:
        scene home_basement_c
        show debbie 62 at right
        show player 13 at left
        with dissolve
        deb "Sit up on the washer for me."
    scene home_basement_sex_01
    show player 270 zorder 1 at Position(xpos=466,ypos=768)
    show debbie 107 zorder 0 at Position(xpos=200)
    with fade
    pause
    show player 271 at Position(xpos=655,ypos=768)
    pause
    if mom_basement_rand:
        player_name "Good?"
        show debbie 108
        deb "Perfect."
        deb "That cock of yours is just perfect."
    else:

        show debbie 108
        deb "My turn..."
    show debbie 109 at Position(xpos=205)
    pause
    show debbie 110
    pause
    show debbie 111 at Position(xpos=207)
    pause
    show debbie 112 at Position(xpos=196)
    pause
    show debbie 113 at Position(xpos=203)
    pause
    show debbie 114
    pause
    show debbie 115
    if mom_basement_rand:
        deb "Now sit back and let me help you with your dirty sticky load."
    else:

        deb "Like what you see?"
        show debbie 114
        player_name "You're beautiful, {b}[deb_name]{/b}."
        show debbie 115
        deb "Just sit back and relax, sweetie."
        deb "Let's start nice and slow..."
    hide player
    hide debbie
    show debbies 124 at Position(xpos=650)
    with dissolve
    pause
    show debbies 125 at Position(xpos=655) with dissolve
    pause
    show debbies 126f at Position(xpos=660) with dissolve
    deb "Oh!"
    show debbies 126e
    pause
    show debbies 126d
    pause
    show debbies 126c
    pause
    show debbies 126b
    pause
    show debbies 126
    if mom_basement_rand:
        deb "Mmmm..."
        deb "I can barely fit you all in."
    else:

        deb "Ahh..."
        player_name "( !!! )"
        player_name "You're so warm..."
    return

label basement_mom_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbies", ["126","126b","126c","126d","126e","126f","126g","126h","126i","126j"], M_mom) as debbies at Position(xpos = 660)
                $ animated = True
            pause 4
            call expression game.dialog_select("debbie_basement_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = ["126","126b","126c","126d","126e","126f","126g","126h","126i","126j"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xpos = 660)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("debbie_basement_hscene_dialog")
        $ animcounter += 1
    call screen basement_mom_sex_options

label debbie_basement_hscene_dialog:
    if animcounter == 1:
        if mom_basement_rand:
            deb "Oh, baby!{p=1}{nw}"
            deb "Yes!{p=1}{nw}"
        else:

            deb "Ahhhh!!!{p=1}{nw}"

    elif animcounter == 2:
        deb "Ahh!!!{p=1}{nw}"

    elif animcounter == 3:
        if mom_basement_rand:
            deb "Oh!{p=1}{nw}"
        else:

            deb "Oh, sweetie!!!{p=1}{nw}"
            player_name "Uhhh...{p=1}{nw}"
    return

label basement_mom_sex_cum:
    player_name "{b}[deb_name]{/b}!"
    show white
    show debbies 129 at Position(xpos=609) with vpunch
    hide white with dissolve
    if mom_basement_rand:
        deb "Oh, sweetie!"
        deb "I'm cumming too!"
        show debbies 129 with flash
        deb "AHH!!!"
    else:

        deb "Ahh!!!"
    jump expression game.dialog_select("basement_mom_sex_after")

label basement_mom_sex_after:
    if M_mom.is_state(S_mom_give_laundry):
        call expression game.dialog_select("basement_mom_sex_after_pre_give_laundry")

    elif mom_basement_rand:
        call expression game.dialog_select("basement_mom_sex_after_pre_random")
    else:

        call expression game.dialog_select("basement_mom_sex_after_pre")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["12_unlocked"] = True
    $ game.timer.tick()
    if M_mom.is_state(S_mom_give_laundry):
        jump expression game.dialog_select("basement_confession_kiss")
    $ game.main()

label basement_confession_kiss:
    call expression game.dialog_select("basement_confession_kiss_pre")
    if randomizer() <= M_mom.get("mom concerned"):
        if M_mom.get("mom concerned") > 0:
            $ M_mom.set("mom concerned", M_mom.get("mom concerned") - 20)

        if M_mom.get("mom concerned") < 0:
            $ M_mom.set("mom concerned", 0)

        call expression game.dialog_select("basement_confession_kiss_concerned_random")
    call expression game.dialog_select("basement_confession_kiss_after")
    $ M_mom.trigger(T_mom_basement_fun)

    $ game.main()

label basement_mom_sex_after_pre_give_laundry:
    show debbies 132 at Position(xpos=650) with fade
    deb "Thanks for bringing me the laundry..."
    show debbies 131
    player_name "Anytime, {b}[deb_name]{/b}."
    show debbies 132
    deb "Let me know if you want to do it again down here."
    show debbies 131
    player_name "Definitely."
    return

label basement_mom_sex_after_pre_random:
    show debbies 130 at Position(xpos=650) with fade
    deb "That was wonderful, sweetie!"
    show debbies 131
    player_name "Yeah it was!"
    player_name "I like doing it with you in the basement!"
    player_name "We can be as loud as we want down here."
    show debbies 132
    deb "Hehe, Yeah. That's definitely a perk!"
    return

label basement_mom_sex_after_pre:
    show debbies 132 at Position(xpos=650) with fade
    deb "That was good, sweetie."
    deb "Thanks for the invite!"
    show debbies 131
    player_name "Anytime!"
    return

label basement_confession_kiss_pre:
    scene home_basement_c
    show player 227 at Position(xpos=200)
    show debbie 73 at Position(xpos=650)
    with fade
    deb "Sweetie..."
    return

label basement_confession_kiss_concerned_random:
    deb "I want you to tell me if you don't want to do this anymore, okay?"
    show player 228
    show debbie 76
    player_name "No, it's fine, {b}[deb_name]{/b}..."
    player_name "I always feel like doing it with you."
    show player 227
    show debbie 77
    deb "Really?"
    show player 228
    player_name "Yeah, that's all I think about doing when I see you..."
    show player 227
    show debbie 75
    deb "You're always so sweet..."
    return

label basement_confession_kiss_after:
    deb "Give me a kiss."
    hide player
    show debbie 80 at Position(xpos=500)
    with dissolve
    pause
    show debbie 79 with dissolve
    pause
    show debbie 80 with dissolve
    pause
    show player 228 at Position(xpos=200)
    show debbie 78 at Position(xpos=650)
    with dissolve
    player_name "I love you, {b}[deb_name]{/b}!"
    show player 227
    show debbie 75
    deb "I love you too, sweetie..."
    scene home_basement
    hide debbie
    hide player
    with fade
    return

label broken_pipe:
    call expression game.dialog_select("broken_pipe_dialogue")
    $ M_mom.trigger(T_mom_closed_valve)
    $ game.main()

label broken_pipe_dialogue:
    scene home_basement
    show popup_pipe_fixed at truecenter with dissolve
    pause
    hide popup_pipe_fixed with dissolve
    scene home_basement_c
    show player 2
    with dissolve
    player_name "Okay, the valve's shut."
    player_name "I should go back to the {b}bathroom{/b} to see if I can fix the {b}sink{/b}."
    hide player
    with dissolve
    return

label laundry_dialogue:
    call expression game.dialog_select("laundry_dialogue_pre")
    menu:
        "Let me help.":
            call expression game.dialog_select("laundry_dialogue_help")
            $ M_mom.trigger(T_mom_cleaned_laundry)
        "You're busy.":


            call expression game.dialog_select("laundry_dialogue_busy")
    $ M_mom.set("chores", False)
    $ game.main()

label laundry_dialogue_pre:
    scene home_basement_c
    show debbie 123 at right
    show player 1 at left
    with dissolve
    deb "Oh! Hi, sweetie!"
    deb "You need something?"
    show debbie 124
    return

label laundry_dialogue_help:
    show debbie 124
    show player 14
    player_name "I can do the laundry, {b}[deb_name]{/b}. Why don't you take a break."
    show debbie 123
    show player 5
    deb "It's fine. I can do it."
    show debbie 122
    show player 10
    player_name "You deserve a rest. You do so much work around the house."
    player_name "Besides, I enjoy helping you."
    show debbie 123
    show player 11
    deb "Oh, {b}[firstname]{/b}. You've been such a big help around here lately!"
    show player 1
    deb "What did I do to deserve such a wonderful tenant?"
    show player 275
    show debbie 62
    deb "You know how everything works?"
    show debbie 125
    show player 276
    player_name "Yup, it's not my first time doing a load of laundry."
    show debbie 63
    show player 275
    deb "Thanks so much for doing this, {b}[firstname]{/b}."
    deb "I really appreciated it."
    deb "Your {b}Father{/b} would be so proud of you!"
    show debbie 125
    show player 277
    player_name "Heh, thanks!"
    scene expression "backgrounds/location_home_cutscene03.jpg"
    show expression FilteredText("It's been really fun helping {b}[deb_name]{/b} out around the house. \nI think she's enjoying it as well. Always so eager to strike up a conversation and learn more about my life. \nWe've certainly been getting a lot closer as of late and I can't help but admire her beauty and charm. \nShe seems to be growing more comfortable with me too. The way she looks at me, her innocent touches...") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade

    scene home_basement_c
    show debbie 2 at right
    show player 13 at left
    with dissolve
    deb "Heh, thanks again for this, {b}[firstname]{/b}."
    deb "I've really been enjoying our little talks."
    show debbie 1
    show player 14
    player_name "Yeah, me too!"
    show player 13
    show debbie 13
    deb "You've been such a big help recently..."
    deb "Would you mind running upstairs and grabbing the {b}lotion{/b} out of my drawer?"
    deb "My legs are feeling a bit dry."
    show debbie 1
    show player 12
    player_name "Where is it upstairs?"
    show player 5
    show debbie 13
    deb "Just look in the {b}drawer in my bedroom{/b}."
    deb "It should be in there."
    show debbie 1
    show player 14
    player_name "Okay, I'll be right back!"
    hide player
    hide debbie
    with dissolve
    show popup_debbiebedroom at truecenter with dissolve
    pause
    hide popup_debbiebedroom with dissolve
    return

label laundry_dialogue_busy:
    show player 14
    player_name "Looks like you're busy."
    player_name "I'll come back later."
    return

label mom_lotion_fun:
    if M_mom.is_set("lotion fun"):
        if player.location == L_home_basement:
            scene home_basement_c

        elif player.location == L_home_kitchen:
            scene homekitchen_closeup
            if M_mom.is_set("sex available"):
                call expression game.dialog_select("mom_lotion_fun_kitchen_sex_available")
                $ player.remove_item("lotion")
                $ M_mom.set("fetch lotion", False)
                $ M_mom.set("retrieved lotion", False)

                pause
                $ M_mom.set("sex speed", .225)
                $ M_mom.set("sex flip", False)
                $ M_mom.set("robe on", True)
                $ first_pass = True
                $ animated = False
                jump expression game.dialog_select("mom_finger_loop")

        call expression game.dialog_select("mom_lotion_fun_pre")
        call expression game.dialog_select("mom_lotion_fun_location_dialogue")
        call expression game.dialog_select("mom_lotion_fun_location_dialogue_after")

        if player.location == L_home_basement:
            $ player.go_to(L_home_livingroom)
            scene home_livingroom_b with fade

        elif player.location == L_home_kitchen:
            $ player.go_to(L_home_entrance)
            scene expression L_home_entrance.background with fade

        call expression game.dialog_select("mom_lotion_fun_after")
    else:

        call expression game.dialog_select("mom_lotion_fun_first_pre")
        menu:
            "Help her.":
                call expression game.dialog_select("mom_lotion_fun_first_help_her")
                $ player.go_to(L_home_livingroom)
                $ M_mom.set("lotion fun", True)
            "Leave.":

                call expression game.dialog_select("mom_lotion_fun_first_leave")

        $ M_mom.trigger(T_mom_lotion_applied)
    hide player
    hide debbie
    with dissolve
    $ player.remove_item("lotion")
    $ M_mom.set("fetch lotion", False)
    $ M_mom.set("retrieved lotion", False)

    $ game.timer.tick()
    $ game.main()

label mom_lotion_fun_kitchen_sex_available:
    show debbie 1 at right
    show player 485 at left
    with dissolve
    player_name "Here it is, {b}[deb_name]{/b}!"
    show player 484
    show debbie 2
    deb "Thanks, sweetie."
    deb "Let me just sit up on the counter so you don't have to bend over."
    show debbie 183 with dissolve
    pause
    show debbie 184 zorder 2
    show debbie_robe 184f zorder 2
    with dissolve
    pause
    show debbie 185
    show debbie_robe 185j
    with dissolve
    pause
    hide player
    show player 487c zorder 1
    show player_arms 488 zorder 3
    with dissolve
    pause
    show player_arms 488b
    with dissolve
    pause
    show player_arms 488c_488d with dissolve
    show player 487g
    show debbie 185b
    deb "Oh, that tickles!"
    show debbie 185g
    deb "You like taking care of me, don't you?"
    show debbie 185f
    show player 487f
    player_name "Always!"
    show player 487g
    show player_arms 488c_488d_488e with dissolve
    pause
    show debbie 185b
    deb "I'd say you're such a good boy..."
    deb "...But I know why you like to do this."
    show debbie 185f
    show player 487
    player_name "..."
    show debbie 185g
    deb "You just like the little show I give you..."
    show debbie 185f
    show player 487g
    player_name "!!!"
    show debbie 185g
    deb "You're little massage makes me so horny."
    show debbie 185b
    show player 487d
    deb "Keep massaging and maybe you can help me with a little something else..."
    show debbie 185f
    show player 487f
    player_name "Yes, ma'am!"
    show player 487g
    show debbie_robe 185k
    show player_arms 488e_488f
    with dissolve
    pause
    show debbie 185b
    deb "That feels really good. I'm like butter in your hands."
    hide player_arms
    show player 13 at Position (xoffset=-118)
    hide debbie_robe
    show debbie 189
    with dissolve
    deb "Even my clothes want to slip off it seems."
    show debbie 188
    show player 26 at Position (xoffset=-118)
    player_name "And when did your panties come off?"
    show player 13 at Position (xoffset=-118)
    show debbie 189
    deb "{b}*Giggle*{/b}"
    show debbie 187
    deb "I wondered if you'd notice."
    show debbie 189
    deb "Well then, are you up for trying something else?"
    show debbie 188
    show player 14 at Position (xoffset=-118)
    player_name "Of course!"
    show player 110f at Position (xoffset=-118)
    show debbie 191
    show debbie_robe 191b zorder 2
    with dissolve
    deb "Then be a good boy and use your fingers to make me cum..."
    show debbie 190
    show player 26 at Position (xoffset=-119)
    player_name "Yes, {b}[deb_name]{/b}."
    show player finger 193b zorder 3
    show debbie 192
    show debbie_robe 194b at right
    with dissolve
    return

label mom_lotion_fun_pre:
    show debbie 1 at right
    show player 485 at left
    with dissolve
    player_name "Got it!"
    show player 484
    show debbie 2
    deb "Great! One sec."
    show player 486
    show debbie 183 with dissolve
    pause
    show debbie 184b zorder 2
    show debbie_robe 184e zorder 2
    with dissolve
    deb "Ready!"
    show player 484
    show debbie 185
    show debbie_robe 185h
    with dissolve
    pause
    hide player
    show player 487c zorder 1
    show player_arms 488 zorder 3
    with dissolve
    pause
    show player_arms 488b
    with dissolve
    show debbie 185d
    deb "Oh! That's cold."
    show player 487d
    deb "Rub the lotion in your hands a bit before you apply it."
    show player 487c
    show debbie 185
    show player_arms 488c_488d with dissolve
    show debbie 185b
    deb "That feels good."
    show debbie 185
    show player 487f
    show player_arms 488b with dissolve
    player_name "Good!"
    show player 487g
    show player_arms 488c_488d with dissolve
    pause
    show player 487f
    show player_arms 488 with dissolve
    player_name "Anywhere else?"
    show player 487g
    show debbie 185c
    deb "Hmm?"
    show player 487e
    player_name "Did you want me to put lotion anywhere else?"
    show player 487d
    show debbie 185d
    deb "Oh..."
    show debbie 185g
    deb "Umm... If you don't mind you could rub some a bit higher on my leg..."
    show debbie 185f
    show player 487e
    player_name "O... Okay..."
    show player_arms 488b with dissolve
    show player 487c
    pause
    show player_arms 488c_488d_488e with dissolve
    show debbie 185d
    deb "Mmm... Dig your hands in a bit deeper there."
    show player_arms 488e with dissolve
    deb "Feel that knot?"
    deb "Try and rub that out..."
    show debbie 185c
    show player 487b
    player_name "O... Okay..."
    show player 487c
    show player_arms 488e_488f with dissolve
    pause
    show debbie 185b
    deb "Mmm... That feels good."
    show debbie 185
    show player 487f
    player_name "!!!"
    show player 487g
    player_name "( She's really relaxing now! )"
    player_name "( I wonder if she realizes I can see through her panties! )"
    show debbie 185d
    deb "Oh, your fingers feel so good."
    deb "Have you been practicing?"
    show debbie 185g
    deb "Some little lady is going to love how helpful and attentive you are."
    show debbie 185d
    deb "Oh! Right there..."
    show debbie 185f
    pause
    show debbie_robe 185i with dissolve
    pause
    show debbie 185e
    deb "!!!"
    hide player_arms
    show player 3 at Position (xpos=420)
    show xtra 21 zorder 2 at Position (xpos=289)
    hide debbie_robe
    show debbie 187
    with dissolve
    deb "...Um... Thank you, sweetie..."
    show debbie 186
    show player 29
    player_name "...You're welcome..."
    show player 3
    show debbie 187
    deb "Listen, I should... um..."
    return

label mom_lotion_fun_location_dialogue:
    if player.location == L_home_basement:
        deb "I should probably finish this load... of laundry..."
        deb "Go on upstairs and... um..."

    elif player.location == L_home_kitchen:
        deb "I should probably finish the dishes..."
    return

label mom_lotion_fun_location_dialogue_after:
    show debbie 186
    show player 29
    player_name "Yeah... I was just about done."
    show player 3
    show debbie 187
    deb "Thanks... again, sweetie."
    show debbie 186
    show player 29
    player_name "You're welcome."
    return

label mom_lotion_fun_after:
    show player 24 with dissolve
    player_name "Damn..."
    player_name "I think she noticed me looking..."
    show player 34
    pause
    show player 35
    player_name "Was she getting wet?"
    show player 43
    pause
    show player 81 with dissolve
    pause
    show player 83
    player_name "I'd better find something else to do."
    return

label mom_lotion_fun_first_pre:
    scene home_basement_c
    show debbie 1 at right
    show player 485 at left
    with dissolve
    player_name "I've got your {b}lotion{/b}, {b}[deb_name]{/b}."
    show player 484
    show debbie 2
    deb "Oh, thank you so much!"
    show debbie 8b
    deb "Ow!"
    show player 486
    pause
    show debbie 11b
    deb "This dang back pain just won't relent!"
    deb "It's really no fun getting old, {b}[firstname]{/b}. I don't recommend it!"
    show debbie 10b
    return

label mom_lotion_fun_first_help_her:
    show player 485
    player_name "Do you want me to help you?"
    show player 484
    show debbie 13
    deb "Hmm?"
    deb "You mean... with my lotion?"
    show debbie 10b
    show player 485
    player_name "Well, yeah... If you want?"
    show player 484
    show debbie 11b
    deb "You wouldn't mind?"
    show debbie 10b
    show player 485
    player_name "Of course not! I'd be very happy to!."
    player_name "I can apply the lotion and give you a massage all at once!"
    player_name "How does that sound?!"
    show player 484
    show debbie 14
    deb "..."
    show debbie 2
    deb "That sounds wonderful, sweetie!"
    deb "How could a girl say no to a free massage?"
    deb "One second..."
    deb "... Let me just get comfortable."
    show player 486
    show debbie 183 with dissolve
    pause
    show debbie 184 zorder 2
    show debbie_robe 184e zorder 2
    with dissolve
    show player 485
    player_name "You said your legs feel dry?"
    show player 484
    show debbie 184b
    deb "Yeah, they always seem to be the worst this time of year!"
    show debbie 184
    show player 485
    player_name "Okay."
    show player 484
    show debbie 185
    show debbie_robe 185h
    with dissolve
    pause
    hide player
    show player 487c zorder 1
    show player_arms 488 zorder 3
    with dissolve
    pause
    show player_arms 488b
    with dissolve
    player_name "( !!! )"
    show debbie 185c
    show player 487b
    player_name "Oops, I wasn't expecting it to come out that fast!"
    show player 487d
    show debbie 185b
    deb "Heh."
    show debbie 185d
    deb "It's alright, sweetie. There's a lot of ground to cover!"
    show debbie 185
    show player 487b
    player_name "O-okay."
    show player 487c
    show player_arms 488c_488d with dissolve
    show player 487
    show debbie 185d
    deb "Mmm, that feels nice..."
    show debbie 185
    show player 487c
    show player_arms 488b with dissolve
    player_name "..."
    show player_arms 488c_488d with dissolve
    pause
    show player_arms 488 with dissolve
    show player 487e
    player_name "That takes care of the lower half."
    player_name "Did you want me to do your thighs as well?"
    show player 487d
    show debbie 185b
    deb "... Yeah, I suppose. So long as you're sure you don't mind?"
    show debbie 185
    show player 487b
    player_name "Not at all."
    show player 487c
    show player_arms 488b with dissolve
    pause
    show player_arms 488c_488d_488e with dissolve
    pause
    show debbie 185d
    deb "Mmm, you're pretty good at this, {b}[firstname]{/b}..."
    show player_arms 488e with dissolve
    deb "You can rub a bit harder if you want."
    deb "I've definitely got some tension stored up in my thigh muscles..."
    show debbie 185c
    show player 487b
    player_name "Y-yeah, I can feel it."
    show player 487c
    show player_arms 488e_488f with dissolve
    pause
    show debbie 185b
    deb "Oh, This is heaven..."
    show debbie 185
    show player 487f
    player_name "( !!! )"
    show player 487g
    player_name "( She's really relaxed right now! )"
    player_name "( I wonder if she realizes I can see through her panties? )"
    show debbie 185d
    deb "You have wonderful hands, {b}[firstname]{/b}!"
    deb "You should consider becoming a masseur..."
    show debbie 185g
    deb "I bet you would make a fortune!"
    show debbie 185d
    deb "Oh! Right there..."
    show debbie 185f
    pause
    show debbie_robe 185i with dissolve
    pause
    show debbie 185e
    deb "( !!! )"
    hide player_arms
    show player 3 at Position (xpos=420)
    show xtra 21 zorder 2 at Position (xpos=289)
    hide debbie_robe
    show debbie 187
    with dissolve
    deb "... Heh, that's probably enough. I can finish from here."
    show debbie 186
    show player 29
    player_name "You're sure?"
    show player 3
    show debbie 187
    deb "Why don't you head on upstairs?"
    deb "I've gotta keep an eye on this laundry..."
    deb "... and get the dryer going."
    show debbie 186
    show player 29
    player_name "Y-Yeah, okay."
    show player 3
    show debbie 187
    deb "Thanks again, sweetie."
    show debbie 186
    show player 29
    player_name "You're welcome."
    scene home_livingroom_b with fade
    show player 24 with dissolve
    player_name "Dang..."
    player_name "She must have noticed me peeking."
    show player 34
    pause
    show player 35
    player_name "Was she getting excited or did I just imagine it?"
    show player 43
    pause
    show player 81 with dissolve
    pause
    show player 83
    player_name "... I should probably get my mind off it!"
    return

label mom_lotion_fun_first_leave:
    show player 485
    player_name "Anything else, {b}[deb_name]{/b}?"
    show player 484
    show debbie 11b
    deb "Nope, that will do it."
    deb "Thanks again for all the help, sweetie."
    show debbie 10b
    show player 485
    player_name "You're welcome, {b}[deb_name]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
