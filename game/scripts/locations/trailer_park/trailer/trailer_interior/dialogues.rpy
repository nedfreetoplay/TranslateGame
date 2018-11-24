label trailer_park_first_visit:
    scene expression game.timer.image("trailer_interior{}")
    show player 10 with dissolve
    player_name "( Is this where {b}Roxxy{/b} lives? )"
    player_name "( There's trash all over the place... )"
    hide player with dissolve
    return

label trailer_interior_roxxy_get_cheerleader_outfit:
    scene trailer_interior_c
    show roxxy 1f f at Position (xpos=400)
    show player 5 zorder 1 at left
    show crystal 3 at right
    with dissolve
    crys "What the hell are you doin' home?!"
    crys "You know you ain't 'spose to be missing anymore school!"
    show crystal 1
    show roxxy 3f
    rox "Ugh, relax!"
    rox "I just came back to get something is all..."
    show roxxy 1f f
    show crystal 2
    crys "... And I see you brought that cute boyfriend of yers!"
    show player 13
    show crystal 4 with dissolve
    show roxxy 2f
    rox "... He's not my boyfriend!"
    show player 5
    show crystal 1 with dissolve
    rox "I just didn't wanna walk across town on my own!"
    show roxxy 1f f
    show crystal 2
    crys "Well, if he ain't yer boyfriend, can he be mine?!"
    show player 22
    crys "Hahahaha!"
    show crystal 1
    show roxxy 3f
    rox "... Ugh, shuddup {b}Mom{/b}!"
    hide roxxy with dissolve
    show player 5
    show crystal 3
    crys "... So what are yer intentions with my daughter?"
    show crystal 1
    show player 10
    player_name "... Huh?"
    show player 5
    show crystal 2
    crys "You know, yer intentions?!"
    crys "You plannin' on fornicatin' with her?"
    show crystal 1
    show player 21
    player_name "What?! ... No, Ma'am!"
    player_name "I'm just helping her out with school."
    show player 5
    show xtra 21 zorder 2 at left
    show crystal 2
    crys "Haha, no need to go gettin' all embarrassed!"
    show crystal 3
    crys "I'm just curious is all..."
    show crystal 2
    crys "If yer gonna be havin' the intercourse with my daughter..."
    show player 22
    crys "... You'd better find yerself a good job!"
    crys "We don't need another deadbeat 'round here."
    show crystal 1
    hide xtra
    show player 21
    player_name "... Really, Ma'am. We're just friends."
    show xtra 21 zorder 2 at left
    show player 5
    show crystal 3
    crys "Hehe, look at you turnin' red..."
    crys "I swear, yer cuter than socks on a rooster!"
    show crystal 4
    show roxxy 3cf zorder 0 at Position (xpos=400)
    with dissolve
    rox "Did you move my {b}Cheerleading uniform{/b} somewhere?"
    show roxxy 3df
    show crystal 2 with dissolve
    crys "... Not that I recall."
    show crystal 1
    show roxxy 3f
    rox "I can't find it!"
    show roxxy 3df
    show crystal 2
    crys "Well, what do you expect me to do about it?"
    show crystal 1
    show roxxy 3f
    rox "Ugh, nothing {b}Mom{/b}... Just sit on your ass and drink all day."
    rox "... As usual."
    show roxxy 3df
    show crystal 3
    crys "{b}Roxxy{/b}!"
    crys "Now, I dun told you not to be talking to me like that!"
    crys "I do plenty 'round here."
    show roxxy 2bf
    crys "Why just this mornin' yer cousin came by fer a bit of business and we was-"
    show crystal 1
    show roxxy 2cf
    show player 11
    rox "Hold on a second!"
    rox "{b}Clyde{/b} Was here this morning?!"
    show roxxy 2bf
    show crystal 2
    crys "... Yeah."
    show crystal 1
    show roxxy 3f
    rox "Damnit!"
    rox "Is he sitting out on that stupid tractor drinking again?"
    show roxxy 3df
    show crystal 2
    crys "How should I know?!"
    show crystal 1
    show roxxy 3cf
    rox "Ugh, come with me {b}[firstname]{/b}..."
    hide roxxy
    hide player
    hide xtra
    with dissolve
    show crystal 2
    crys "... That girl needs whoopin'."
    show crystal 4 with dissolve
    pause
    scene black with fade
    return

label trailer_interior_crystal_sex_offer_pre_first:
    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show player 13 at left
    show crystal 2 zorder 1 at right
    with dissolve
    crys "Well, well, well... If it isn't {b}Roxxy{/b}'s new beau..."
    show crystal 4 with dissolve
    show player 10
    player_name "Eh, beau?"
    show player 5
    show crystal 2 with dissolve
    crys "You here lookin' to knock boots with my little gal again?"
    show crystal 1
    show player 10
    player_name "... Knock boots?"
    show player 12
    player_name "I'm not sure what you're talking about, ma'am."
    show player 5
    show crystal 2
    crys "Ma'am?"
    show crystal 2b
    crys "Hahahaha!!"
    crys "Ain't nobody ever called me, \"Ma'am,\" before..."
    show crystal 2
    crys "Just call me, {b}Crystal{/b}."
    show crystal 3 with dissolve
    crys "... And as fer the boot knockin'..."
    show crystal 3b_3c with dissolve
    pause
    show player 22
    player_name "!!!" with hpunch
    show crystal 4 with dissolve
    show player 29 with dissolve
    player_name "Oh! I wasn't..."
    show crystal 1 with dissolve
    player_name "I mean, we don't..."
    show player 3
    show crystal 2b
    crys "Hahaha!"
    show crystal 3 with dissolve
    crys "Of course ya do!"
    show crystal 2 with dissolve
    crys "Ya think I can't hear y'all going at it in there?!"
    show player 22 with dissolve
    crys "This trailer don't exactly offer a lot in the way of privacy!"
    show crystal 1
    show player 21
    player_name "Heh, yea... I guess you're right."
    player_name "Sorry."
    show player 5
    show crystal 2
    crys "Oh, it's nothin' to apologize fer."
    crys "{b}Roxxy{/b}'s had to listen to me ruttin' around with a fella, more than once."
    show crystal 1
    show player 10
    player_name "Yeah, umm... Is she here?"
    show player 5
    show crystal 2
    crys "I'm afraid not..."
    show crystal 1
    show player 10
    player_name "... Oh."
    show player 36
    player_name "Well, I'll get out of your hair then-"
    hide player
    show crystal 17 at left
    with dissolve
    crys "Now, there's no need to rush off..."
    crys "I can tell from all the wailin' that yer takin' real good care of my daughter, {b}[firstname]{/b}..."
    show crystal 17b
    player_name "Um..."
    show player 106 zorder 0 at left
    show crystal 16c at Position (xpos=134)
    with dissolve
    crys "She helpin' you get rid of all that poison?"
    show crystal 16d
    show player 108f
    player_name "P-poison?"
    show player 109f
    show crystal 16c
    crys "Hehe, yeah..."
    show crystal 18_18b
    show crystal_talking_head zorder 2
    with dissolve
    crys "It's important for young boys to get that stuff out."
    hide crystal_talking_head
    show player 106
    player_name "!!!"
    show player 108f
    player_name "What are you-"
    show player 109f
    show crystal_talking_head zorder 2
    crys "Shh, it's alright..."
    crys "I don't mind helpin' out."
    hide crystal_talking_head
    show player 10
    player_name "... What about {b}Roxxy{/b}?!"
    show player 5
    show crystal_talking_head zorder 2
    crys "Oh, don't you worry about {b}Roxxy{/b}..."
    crys "What she don't know, won't hurt her."
    hide crystal_talking_head
    show player 5
    player_name "..."
    show crystal undress 1 at center with dissolve
    pause
    show crystal undress 2 with dissolve
    show player 428
    crys "You just let {b}Crystal{/b} handle it..."
    show crystal undress 3 with dissolve
    show player 427
    player_name "{b}*Gulp{/b}"
    show player 428
    show crystal undress 4 with dissolve
    crys "Once you get a taste of this, you won't ever wanna leave my baby girl!"
    show player 426
    show crystal undress 5 with dissolve
    pause
    show crystal undress 6 with dissolve
    pause
    show crystal undress 7 at right with dissolve
    crys "... Just bring that fine piece of man meat over here to {b}Momma{/b}..."
    show crystal undress 7b
    show player 427
    player_name "Oh, I dunno..."
    show player 426
    show crystal undress 7
    crys "Hehe, no need to be shy honey."
    show crystal undress 10 with dissolve
    crys "I been thinkin' bout ridin' that big dick of yers fer awhile now."
    crys "It's got my pussy wet as October!"
    show crystal undress 10b
    player_name "..."
    show crystal undress 10
    crys "Unless.."
    crys "... You'd prefer to kick in mah back door?"
    show crystal undress 9 with dissolve
    show player 427
    player_name "Huh?"
    player_name "What do you mean your-"
    show player 428
    show crystal undress 11_11b
    player_name "!!!" with hpunch
    crys "You can use me any way you want, {b}[firstname]{/b}!"
    show player 429
    player_name "R-really?"
    show player 426
    crys "Mmmhmm!"
    return

label trailer_interior_crystal_sex_offer_pre_repeat:
    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show player 10 at left
    show crystal 1 at right
    with dissolve
    player_name "So about what you said earlier..."
    show player 5
    show crystal 2
    crys "Oh, finally comin' around, are ya?"
    show crystal 1
    show player 24
    player_name "..."
    show crystal undress 1 with dissolve
    crys "You won't regret it, honey."
    show crystal undress 3 with dissolve
    show player 428
    crys "If there's one thing I know, it's how to please a man..."
    show crystal undress 4 with dissolve
    pause
    show crystal undress 5 with dissolve
    pause
    show crystal undress 6 with dissolve
    pause
    show crystal undress 7b
    player_name "!!!" with hpunch
    show crystal undress 7
    crys "Hehe!"
    crys "... You have no idea how bad I want it, {b}[firstname]{/b}!"
    show crystal undress 9 with dissolve
    show player 426
    player_name "..."
    show crystal undress 11_11b with dissolve
    crys "Mmm, don't you wanna give it to me?"
    return

label trailer_interior_crystal_sex_offer_menu:
    menu:
        "Okay...":
            call expression game.dialog_select("trailer_interior_crystal_sex_offer_accept")
            call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_menu")
            $ anim_toggle = True
            $ animated = False
            jump expression game.dialog_select("trailer_interior_crystal_sex_loop")

        "I can't do this..." if not M_crystal.is_set("crystal sex offer denied"):
            call expression game.dialog_select("trailer_interior_crystal_sex_offer_denied_first")
            $ M_crystal.set("crystal sex offer denied", True)

        "I still can't do this..." if M_crystal.is_set("crystal sex offer denied"):
            call expression game.dialog_select("trailer_interior_crystal_sex_offer_denied_repeat")
    $ game.main()

label trailer_interior_crystal_sex_offer_accept:
    show player 429
    player_name "O-okay."
    show player 426 zorder 2
    show crystal undress 10 with dissolve
    crys "That's the spirit!"
    crys "You can take me any way you want, honey!"
    show crystal undress 10b
    return

label trailer_interior_crystal_sex_offer_denied_first:
    show player 24
    player_name "I..."
    show crystal undress 9 with dissolve
    crys "Hehe, c'mon honey, don't make me beg fer it..."
    show player 37 with dissolve
    player_name "I can't..."
    show crystal undress 8 with dissolve
    crys "Hmm?"
    crys "... What do you mean, you can't?!"
    crys "It ain't difficult! Just whip that bad boy out and choose a hole..."
    show crystal undress 8b
    show player 12 with dissolve
    player_name "No, I mean... I can't do it to {b}Roxxy{/b}..."
    show player 5
    show crystal undress 8
    crys "Psh, I dun told ya. {b}Roxxy{/b} ain't never got to know!"
    show crystal undress 8b
    show player 10
    player_name "Yeah but I would know..."
    show player 12
    player_name "... And I don't want to be that guy."
    show player 5
    show crystal undress 6 with dissolve
    crys "..."
    show crystal undress 5 with dissolve
    pause
    show crystal undress 4 with dissolve
    crys "Sheesh, you know... You really are a good kid."
    show crystal undress 2 with dissolve
    crys "I don't understand how in the world my {b}Roxxy{/b} managed to get ahold of you..."
    show crystal undress 1 with dissolve
    crys "{b}*Sigh*{/b}"
    show crystal 6 with dissolve
    crys "Suit yerself..."
    crys "... But the offer's on the table, honey. Should you ever change yer mind."
    show crystal 16
    crys "Mmm, I'll be waitin'."
    show crystal 14
    show player 11
    player_name "..."
    hide crystal with dissolve
    show player 10
    player_name "... Well, that was awkward."
    hide player with dissolve
    return

label trailer_interior_crystal_sex_offer_denied_repeat:
    show player 24
    player_name "I..."
    show player 25
    player_name "I'm sorry, {b}Crystal{/b}. I can't do it..."
    show crystal undress 9 with dissolve
    crys "..."
    show crystal undress 6 with dissolve
    crys "Tch, I don't like bein' teased, {b}[firstname]{/b}!"
    show crystal undress 5 with dissolve
    show player 10
    player_name "... I'm sorry."
    show player 5
    show crystal undress 5 with dissolve
    pause
    show crystal undress 1 with dissolve
    crys "Suit yerself."
    show crystal 6 with dissolve
    crys "You know where to find me, iffin' you should change yer mind."
    hide crystal with dissolve
    player_name "..."
    hide player with dissolve
    return

label trailer_interior_crystal_sex_or_anal_menu:
    menu:
        "Sex.":
            $ M_crystal.set("crystal anal", False)
            if M_roxxy.get("roxxy crystal sex") and not L_trailer.is_here(M_crystal):
                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_sex_first")

            elif L_trailer.is_here(M_crystal):
                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_sex_outside")
            else:

                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_sex_repeat")
        "Anal.":

            $ M_crystal.set("crystal anal", True)
            if M_roxxy.get("roxxy crystal sex") and not L_trailer.is_here(M_crystal):
                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_anal_first")

            elif L_trailer.is_here(M_crystal):
                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_anal_outside")
            else:

                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_anal_repeat")
    return

label trailer_interior_crystal_sex_or_anal_choose_sex_first:
    show crystal undress 10 with dissolve
    crys "That works for me, honey."
    show crystal undress 10b
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    pause
    hide player
    show crystal undress 12
    with dissolve
    crys "Mmm, gimme that monster!"
    hide crystal

    scene expression "backgrounds/location_trailer_sex.jpg"
    show crystals insert 1 at left
    show trailer_counter at right
    with dissolve
    pause
    show crystals cum 2 with dissolve
    crys "!!!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
    with dissolve
    pause
    return

label trailer_interior_crystal_sex_or_anal_choose_sex_outside:
    show crystal undress 10 with dissolve
    crys "Alright, honey."
    show crystal undress 10b
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    pause
    hide player
    show crystal undress 12
    with dissolve
    crys "Remember I want it nice and deep..."
    pause
    hide crystal

    scene expression "backgrounds/location_trailer_sex_night.jpg"
    show crystals insert 1
    show trailer_counter_night at right
    with dissolve
    crys "Mmm..."
    show crystals cum 2 with dissolve
    crys "Such a big boy!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
    with dissolve
    pause
    crys "That's it..."
    crys "Get it all out, honey."
    pause
    crys "Mmm..."
    pause
    crys "Aaahh!"
    pause
    crys "Fill me up, {b}[firstname]{/b}!"
    return

label trailer_interior_crystal_sex_or_anal_choose_sex_repeat:
    show crystal undress 10
    crys "You got it, honey!"
    show crystal undress 10b
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    pause
    hide player
    show crystal undress 12
    with dissolve
    crys "Mmm, I don't need no foreplay, {b}[firstname]{/b}..."
    crys "Gimme all of it!"
    player_name "Y-yes, ma'am..."
    hide crystal

    scene expression "backgrounds/location_trailer_sex.jpg"
    show crystals insert 1 at left
    show trailer_counter at right
    with dissolve
    pause
    show crystals cum 2
    crys "God damn, honey!" with hpunch
    crys "That dick is somethin' special!"
    crys "Phew!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
    with dissolve
    pause
    return

label trailer_interior_crystal_sex_or_anal_choose_anal_first:
    show crystal undress 10 with dissolve
    crys "Mmm, my favorite!"
    show crystal undress 10b
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    crys "Get that monster in my ass!"
    hide player
    show crystal undress 12b
    with dissolve
    pause
    hide crystal

    scene expression "backgrounds/location_trailer_sex.jpg"
    show crystals insert 1 at left
    show trailer_counter at right
    with dissolve
    player_name "You ready?"
    crys "Do it!"
    show crystals cum 2
    crys "!!!" with hpunch
    crys "NGGHHH!!!"
    pause
    player_name "You're shaking..."
    crys "..."
    player_name "Ma'am?"
    crys "Shut up and give it to me!"
    player_name "O-okay!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
    with dissolve
    pause
    return

label trailer_interior_crystal_sex_or_anal_choose_anal_outside:
    show crystal undress 10 with dissolve
    crys "Oh, I was hoping you'd say that!"
    show crystal undress 10b
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    pause
    hide player
    show crystal undress 12b
    with dissolve
    crys "Mmm, that's it honey..."
    hide crystal

    scene expression "backgrounds/location_trailer_sex_night.jpg"
    show crystals insert 1 at left
    show trailer_counter_night at right
    with dissolve
    crys "Give Momma the good stuff!"
    show crystals cum 2
    crys "!!!" with hpunch
    crys "Fuuuuuuu-"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
    with dissolve
    pause
    crys "God damn!"
    player_name "Shhh!!"
    player_name "YOu have to be quiet or {b}Roxxy{/b} will hear us!"
    pause
    crys "{b}*Whimper*{/b}"
    pause
    crys "OOohh, it's so deep!"
    crys "Ahh, fuck my ass {b}[firstname]{/b}!"
    player_name "SHH!!"
    return

label trailer_interior_crystal_sex_or_anal_choose_anal_repeat:
    crys "Oh, I was hoping you'd say that!"
    show player 429
    player_name "You were?"
    show player 426
    crys "Hell yeah!"
    crys "Don't get me wrong now."
    crys "I love regular sex too..."
    crys "... But the orgasms are so much more intense when I'm gettin' my ass fucked!"
    crys "Always have been."
    show player 427
    player_name "... Really?"
    show player 426
    crys "Mmmhmm!"
    show crystal undress 10 with dissolve
    crys "Go on, stick it in there and I'll show ya."
    show crystal undress 10b
    show player 429
    player_name "O-okay..."
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    pause
    hide player
    show crystal undress 12b
    with dissolve
    crys "That's it, honey."

    scene expression "backgrounds/location_trailer_sex.jpg"
    show crystals insert 1
    show trailer_counter at right
    with dissolve
    crys "Don't be scared to push it in there!"
    crys "I can take it!"
    show crystals cum 2
    crys "!!!" with hpunch
    crys "Oooh, sweet Baby Jesus!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
    with dissolve
    crys "NNGGGHHH!!!"
    crys "God damn, that's deep!"
    pause
    crys "Feels like yer 'bout to break my spine!"
    player_name "Should I stop?!"
    crys "GGRRRAAAHHH!!!"
    player_name "{b}Crystal{/b}!"
    crys "IT'S SO DAMN GOOD!!!"
    crys "C'mon, honey. Fuck me harder!"
    pause
    $ M_crystal.set("sex speed", .125)
    crys "{b}*Gasp*{/b}"
    pause
    crys "AAAAAHHHHH!!!"
    crys "Don't stop!"
    pause
    crys "DON'T STOP!!!"
    pause
    crys "NGGHHH!!!" with hpunch
    return

label trailer_interior_crystal_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
                $ animated = True
            pause 5
            call expression game.dialog_select("crystal_trailer_interior_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "crystals {}".format(pose_list[pose_counter]) as crystals
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("crystal_trailer_interior_hscene_dialog")
        $ animcounter += 1
    if not M_roxxy.get("roxxy crystal sex") and store._in_replay == None:
        $ M_roxxy.trigger(T_roxxy_crystal_sex)
    call screen crystal_sex_options

label crystal_trailer_interior_hscene_dialog:
    $ random_count = randomizer()
    if animcounter == 0:
        if not M_roxxy.get("roxxy crystal sex"):
            crys "Good lord!{p=1}{nw}"
            crys "This is definitely the biggest I've ever had!{p=2}{nw}"
            pause
            crys "It feels like yer 'bout to split me in two!{p=2}{nw}"
            player_name "Should I stop?{p=2}{nw}"
            crys "Hell no!{p=1}{nw}"
            crys "Fuck me harder, honey!{p=1}{nw}"

        elif M_roxxy.get("roxxy crystal sex"):
            if random_count <= 33:
                if M_crystal.is_set("crystal anal"):
                    crys "Rrraaahh!!{p=1}{nw}"
                    crys "That's so damn good!{p=1}{nw}"
                else:

                    crys "Mmm, that's it honey!{p=1}{nw}"
                    crys "You get all that poison out!{p=2}{nw}"

            elif random_count > 33 and random_count <= 66:
                if M_crystal.is_set("crystal anal"):
                    crys "Oh yeah, honey...{p=1}{nw}"
                    pause
                    crys "This is just what {b}Momma{/b} needed today!{p=2}{nw}"
                    player_name "Feels good?{p=1}{nw}"
                    crys "You betcha.{p=1}{nw}"
            else:

                if M_crystal.is_set("crystal anal"):
                    player_name "I can't believe you like anal so much...{p=2}{nw}"
                    crys "Oh honey, I LOVE anal!{p=2}{nw}"
                    crys "I can't even begin to explain all the sensations.{p=2}{nw}"
                    player_name "...{p=1}{nw}"
                    crys "... And if you angle it just right, it hits me right in my-{p=2}{nw}"
                    crys "AAAHHH!!{p=1}{nw}"
                    pause
                    crys "That's the angle right there!{p=2}{nw}"
                    crys "Don't you dare stop!{p=1}{nw}"
                else:

                    crys "Mmm, that feels so good, {b}[firstname]{/b}!{p=2}{nw}"
                    player_name "Yeah it does.{p=1}{nw}"

    elif animcounter == 1:
        if M_roxxy.get("roxxy crystal sex"):
            if random_count <= 33:
                if M_crystal.is_set("crystal anal"):
                    crys "C'mon, {b}[firstname]{/b}! Deeper!{p=1}{nw}"
                    player_name "Yes, ma'am.{p=1}{nw}"
                    if M_crystal.get("sex speed") > .076:
                        $ M_crystal.set("sex speed", M_crystal.get("sex speed") - 0.05)
                else:

                    crys "Give it to {b}Momma{/b}!{p=1}{nw}"

            elif random_count > 33 and random_count <= 66:
                if M_crystal.is_set("crystal anal"):
                    crys "Mmm, that's it {b}[firstname]{/b}!{p=1}{nw}"
                    crys "Keep giving me those nice deep strokes!{p=2}{nw}"
                else:

                    crys "Say, {b}[firstname]{/b}?{p=1}{nw}"
                    player_name "Hmm?{p=1}{nw}"
                    crys "Is my daughter tighter than me?{p=2}{nw}"
                    player_name "Yeah, she's a lot tighter than you...{p=2}{nw}"
                    pause
                    crys "Hmm, she doesn't take it this deep though does she?{p=2}{nw}"
                    player_name "No, she does not!{p=1}{nw}"
                    crys "Hehehe, well I guess experience counts for somethin-{p=2}{nw}"
                    $ M_crystal.set("sex speed", .075)
                    crys "Oh Jesus!!!{p=1}{nw}" with hpunch
                    pause
                    crys "AAAAAAHHHHH!!!{p=1}{nw}"
            else:

                if M_crystal.is_set("crystal anal"):
                    crys "GRAAAHHH!!!{p=1}{nw}"
                else:

                    crys "Aah!{p=1}{nw}"
        else:

            crys "Fuck me harder, honey!{p=2}{nw}"

    elif animcounter == 2:
        if not M_roxxy.get("roxxy crystal sex"):
            crys "Aaah!!{p=1}{nw}"
            crys "You been stickin' to my daughter with this monster?!{p=2}{nw}"
            player_name "Y-yes, ma'am...{p=1}{nw}"
            pause
            player_name "Though she never takes it this deep!{p=2}{nw}"
            crys "I should hope not!{p=1}{nw}"
            crys "Poor girl ain't ready for this kinda deep dickin'!{p=2}{nw}"

        elif M_roxxy.get("roxxy crystal sex"):
            if random_count <= 33:
                if M_crystal.is_set("crystal anal"):
                    crys "God damn, honey!{p=1}{nw}"
                    crys "AAahhhh!!{p=1}{nw}"
                else:

                    crys "Aaahh!!{p=1}{nw}"
                    crys "Harder!!{p=1}{nw}"

            elif random_count > 33 and random_count <= 66:
                if M_crystal.is_set("crystal anal"):
                    player_name "It's so tight!{p=1}{nw}"
                    crys "Mmm, don't stop!{p=1}{nw}"
            else:

                crys "Yer dick sure is somethin' special, {b}[firstname]{/b}!{p=2}{nw}"
                player_name "Hehe, thanks!{p=1}{nw}"

    elif animcounter == 3:
        if M_roxxy.get("roxxy crystal sex"):
            if random_count <= 33:
                if not M_crystal.is_set("crystal anal"):
                    crys "Nngghhh!{p=1}{nw}"

            elif random_count > 66:
                if not M_crystal.is_set("crystal anal"):
                    crys "I'm gonna-{p=1}{nw}"
                    crys "NGGHHH!!!{p=1}{nw}"
        else:

            if random_count > 50:
                crys "Aaah!!{p=1}{nw}"
                crys "I'm gettin' close!{p=1}{nw}"
    return

label trailer_interior_crystal_sex_cum:
    if L_trailer.is_here(M_crystal):
        if M_crystal.is_set("crystal anal"):
            call expression game.dialog_select("trailer_interior_crystal_sex_outside_cum_anal")
        else:

            call expression game.dialog_select("trailer_interior_crystal_sex_outside_cum")

    elif M_roxxy.get("roxxy crystal sex"):
        if M_crystal.is_set("crystal anal"):
            call expression game.dialog_select("trailer_interior_crystal_sex_cum_repeat_anal")
        else:

            call expression game.dialog_select("trailer_interior_crystal_sex_cum_repeat")

    elif M_crystal.is_set("crystal anal"):
        call expression game.dialog_select("trailer_interior_crystal_sex_cum_first_anal")
        $ M_roxxy.set("roxxy crystal sex", 0)
    else:

        call expression game.dialog_select("trailer_interior_crystal_sex_cum_first")
        $ M_roxxy.set("roxxy crystal sex", 0)
    $ renpy.end_replay()
    $ persistent.cookie_jar["Crystal"]["unlocked"] = True
    $ persistent.cookie_jar["Crystal"]["gallery"]["01_unlocked"] = True
    $ M_roxxy.trigger(T_roxxy_crystal_sex)
    $ game.timer.tick()
    $ game.main()

label trailer_interior_crystal_sex_outside_cum_anal:
    player_name "I'm gonna cum!"
    crys "Me too!"
    pause
    crys "FUCK ME!!!"
    crys "NGGHHH!!!"
    player_name "Shh-"
    show crystals cum 2_2b
    player_name "HNNGGG!!!" with flash
    pause
    show crystals retract 3
    show crystals_anal_cum
    with dissolve
    crys "{b}*Whimper*{/b}"
    pause
    hide crystals
    hide crystals_anal_cum
    with dissolve

    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show crystal undress 10b at right
    show crystal_anal_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal 13b
    with dissolve
    player_name "Holy crap..."
    hide player_slick_boner
    show player 261f at left
    with dissolve
    pause
    show player 8 with dissolve
    rox "{b}Mom{/b}? What the hell are you doing out there?!"
    show player 23
    player_name "!!!" with hpunch
    show crystal undress 10
    crys "Haaah... Haaah..."
    show player 22
    crys "I ain't doin' nothin'!"
    crys "Just stubbed my damn toe is all!"
    show crystal undress 10b
    rox "Well, keep it down. I'm on the phone!"
    show crystal undress 10
    crys "Haah... You'd best get in there."
    show crystal undress 10b
    show player 29 with dissolve
    player_name "Y-yeah..."
    hide player with dissolve
    crys "..."
    hide crystal_anal_cum
    show crystal undress 11_11b
    with dissolve
    crys "Mmm, god damn that was hot!"
    pause
    hide crystal with dissolve
    return

label trailer_interior_crystal_sex_outside_cum:
    player_name "Here it comes!"
    crys "Shhh, quietly honey..."
    pause
    show crystals cum 2_2b
    player_name "HNNGGG!!!" with flash
    pause
    show crystals retract 3 with dissolve
    crys "Mmm..."
    crys "Hehe, now that's better, isn't {b}[firstname]{/b}?"
    player_name "Phew, yeah..."
    hide crystals with dissolve
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show crystal undress 10 at right
    show crystal_pussy_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal 13b
    with dissolve
    crys "Well, you'd best get in there..."
    crys "My daughter's probably waitin' fer ya."
    show crystal undress 10b
    player_name "Yeah, okay..."
    hide crystal_pussy_cum
    show crystal undress 6
    hide player_slick_boner
    show player 261f at left
    with dissolve
    pause
    show crystal undress 5
    show player 8
    with dissolve
    pause
    show crystal undress 2
    show player 26
    with dissolve
    player_name "Thanks, {b}Crystal{/b}."
    show player 13
    show crystal undress 1 with dissolve
    crys "My pleasure, honey."
    hide player
    hide crystal
    with dissolve
    return

label trailer_interior_crystal_sex_cum_repeat_anal:
    player_name "Your ass it so tight!"
    player_name "I can't hold it..."
    crys "Just a little more!"
    pause
    crys "Oh, fuck. I'm gonna cum!"
    player_name "Me too!!"
    show crystals cum 2_2b
    crys "AAAHHHH!!!"
    player_name "HNNGGG!!!" with flash
    pause
    show crystals retract 3
    show crystals_anal_cum
    with dissolve
    player_name "Wow, that was intense!"
    hide crystals
    hide crystals_anal_cum
    with dissolve

    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show crystal undress 10b at right
    show crystal_anal_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal
    with dissolve
    crys "{b}*Whimper*{/b}"
    hide crystal_anal_cum
    show crystal undress 11
    with dissolve
    player_name "..."
    player_name "You alright, ma'am?"
    crys "Y-yeah... Just-"
    show crystal undress 11b with dissolve
    crys "Tch!"
    crys "..."
    show crystal undress 9 with dissolve
    crys "Aftershocks, heh..."
    show crystal undress 7 with dissolve
    crys "Go fetch me a couple cold ones from the fridge, would ya?"
    show crystal undress 7b
    player_name "Sure thing!"
    hide player
    hide player_slick_boner
    with dissolve
    pause
    show crystal undress 7
    crys "God damn, that boy is gifted!"
    hide crystal with dissolve
    return

label trailer_interior_crystal_sex_cum_repeat:
    player_name "I'm getting close!"
    crys "Let it out, honey!"
    crys "You just get it all outta your system!"
    show crystals cum 2_2b
    player_name "HNNGGHHH!!!" with flash
    crys "Ahhh!!"
    pause
    show crystals retract 3 with dissolve
    pause
    crys "Phew! That was exactly what I needed!"
    hide crystals with dissolve

    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show crystal undress 10 at right
    show crystal_pussy_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal
    with dissolve
    crys "You feel better now, honey?"
    hide crystal_pussy_cum
    show crystal undress 6
    hide player_slick_boner
    show player 261f at left
    with dissolve
    pause
    show crystal undress 5
    show player 8
    with dissolve
    player_name "Yeah, much better."
    show player 111f
    show crystal undress 4
    with dissolve
    crys "Good boy!"
    show crystal undress 2 with dissolve
    show player 13
    crys "You just come on back and see me when you need another release..."
    show crystal undress 1 with dissolve
    crys "Alright?"
    show crystal 4 with dissolve
    show player 14
    player_name "Sure thing, {b}Crystal{/b}."
    show player 13
    show crystal 2b with dissolve
    crys "Hehehe!"
    hide player
    hide crystal
    with dissolve
    return

label trailer_interior_crystal_sex_cum_first_anal:
    player_name "I can't hold it any longer!"
    crys "..."
    pause
    player_name "{b}Crystal{/b}?!"
    crys "..."
    pause
    player_name "{b}CRYSTAL{/b}!?!"
    player_name "I'm gonna-"
    pause
    show crystals cum 2_2b
    player_name "HNNGGG!!!" with flash
    crys "NGGHHHAAAAAAAAAHHHH!!!" with hpunch
    pause
    show crystals retract 3
    show crystals_anal_cum
    with dissolve
    pause
    hide crystals
    hide crystals_anal_cum
    with dissolve
    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show crystal undress 10b at right
    show crystal_anal_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal
    with dissolve
    player_name "You alright, ma'am?"
    crys "..."
    player_name "Ma'am?!"
    show crystal undress 10
    crys "... Mmmhmm."
    show crystal undress 10b
    player_name "Sheesh, you had me worried there for a second."
    show crystal undress 10
    crys "I just need a minute, honey."
    crys "Jesus, that was crazy!"
    show crystal undress 10b
    hide player_slick_boner
    show player 261f at left
    with dissolve
    player_name "..."
    show player 8 with dissolve
    show crystal undress 10
    crys "I ain't gonna be walkin' right fer a week!"
    show crystal undress 10b
    show player 427
    player_name "I'm sorry."
    show player 426
    show crystal undress 10
    crys "Phew! No need to be sorry!"
    crys "I haven't cum that hard in years!"
    hide crystal_anal_cum
    show crystal undress 11b
    with dissolve
    crys "Feel me shakin'!"
    show player 429
    player_name "Heh, I guess I did good then?"
    show player 426
    show crystal undress 11 with dissolve
    crys "Better than good!"
    show crystal undress 9 with dissolve
    pause
    show crystal undress 7 with dissolve
    crys "Wow! I don't think I can even stand..."
    crys "You stuck that thing up my daughter's ass yet?"
    show crystal undress 7b
    show player 429
    player_name "... No, ma'am."
    show player 426
    show crystal undress 7
    crys "Good!"
    crys "The poor girl ain't ready for that monster up her ass!"
    crys "Not yet anyways."
    show crystal undress 7b
    player_name "..."
    show crystal undress 7
    crys "Grab me a couple cold ones outta the fridge, will ya?"
    show crystal undress 7b
    show player 427
    player_name "You want two?"
    show player 426
    show crystal undress 7
    crys "Hehe, yes."
    crys "One for me and one for my asshole!"
    crys "You really did a number on it!"
    show crystal undress 7b
    show player 429
    player_name "Haha, alright."
    hide player with dissolve
    pause
    show crystal undress 7
    crys "God damn, my daughter better be treatin' this one right..."
    crys "She lets him get away and I'll disown her for sure!"
    hide crystal with dissolve
    return

label trailer_interior_crystal_sex_cum_first:
    player_name "Yeah, I'm getting close too."
    crys "Give it to me now, honey!"
    crys "I want you to fill me to burstin'!"
    player_name "Nngghh!"
    pause
    crys "That's it!"
    crys "Oh, shit! Here it comes!"
    show crystals cum 2_2b
    player_name "HNNGGG!!" with flash
    crys "AAAhhhh!!!"
    pause
    show crystals retract 3 with dissolve
    crys "Haaah... Haaah..."
    crys "God damn, honey!"
    crys "Haaah..."
    hide crystals with dissolve
    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show crystal undress 10 at right
    show crystal_pussy_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal
    with dissolve
    crys "Ain't no way I'm ever lettin' you get away."
    show crystal undress 10b
    hide player_slick_boner
    show player 261f at left
    with dissolve
    player_name "..."
    show player 8 with dissolve
    show crystal undress 10
    crys "My daughter ever leaves you unsatisfied..."
    show player 110f with dissolve
    crys "... You just come see ole' Crystal!"
    crys "You hear me?!"
    show crystal undress 10b
    show player 111f
    player_name "Yes, ma'am."
    show player 110f
    hide crystal_pussy_cum
    show crystal undress 5
    with dissolve
    crys "Phew!"
    show crystal undress 2 with dissolve
    show player 13
    pause
    show crystal undress 1 with dissolve
    crys "Alright, I need a beer after gettin' fucked like that!"
    show crystal 6 with dissolve
    crys "You want one?"
    show crystal 5
    show player 14
    player_name "No, thanks..."
    player_name "I should probably get going."
    show player 13
    show crystal 6
    crys "... Suit yerself."
    crys "Come back and see me real soon, honey."
    hide player
    hide crystal
    with dissolve
    return

label trailer_interior_crystal_sex_repeat_inside:
    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show player 14 zorder 2 at left
    show crystal 1 at right
    with dissolve
    player_name "You wanna have a bit of fun while I'm here?"
    show player 13
    show crystal 2
    crys "Oh, you know I do!"
    show crystal undress 1 with dissolve
    crys "I told ya I'd take real good care of you, honey."
    show crystal undress 2 with dissolve
    pause
    show crystal undress 4 with dissolve
    pause
    show crystal undress 5 with dissolve
    pause
    show crystal undress 6 with dissolve
    show player 426
    pause
    show crystal undress 7 with dissolve
    crys "Now then..."
    show crystal undress 10 with dissolve
    crys "You want my pussy?"
    show crystal undress 9 with dissolve
    crys "Or..."
    show crystal undress 11_11b with dissolve
    crys "My ass?"
    return

label trailer_interior_crystal_sex_repeat_outside_offer_pre:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 13 at left
    show crystal 6 at right
    with dissolve
    crys "Hey, how 'bout a quickie before you head inside?"
    show crystal 5
    show player 10
    player_name "What?!" with hpunch
    player_name "... But {b}Roxxy's{/b} right there!"
    show player 5
    show crystal 16b with dissolve
    crys "Oh, she's probably on the phone or somethin'!"
    crys "It'll be fine so long as we're real quiet."
    show crystal 5 with dissolve
    player_name "..."
    show player 10
    player_name "I dunno..."
    show player 5
    show crystal 9
    crys "Oh, c'mon honey!"
    show crystal 15
    crys "Don't you want a quick release?"
    crys "{b}Momma{/b} needs that sweet dick of yours, REAL bad!"
    show crystal 14
    show player 12
    player_name "What about your neighbors?"
    show player 5
    show crystal 11
    crys "Huh?"
    show crystal 6
    crys "Oh, who gives a damn what the neighbors think?!"
    show crystal 1 at left
    show crystal 18_18b at Position (xpos=134)
    show crystal_talking_head
    with dissolve
    crys "Besides, it's dark enough out here, they won't see nothin'."
    hide crystal_talking_head
    show player 114
    player_name "..."
    show player 5
    return

label trailer_interior_crystal_sex_repeat_outside_offer_menu:
    menu:
        "O-okay.":
            call expression game.dialog_select("trailer_interior_crystal_sex_repeat_outside_offer_accept")
            call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_menu")
            $ anim_toggle = True
            $ animated = False
            jump expression game.dialog_select("trailer_interior_crystal_sex_loop")
        "No way!":

            call expression game.dialog_select("trailer_interior_crystal_sex_repeat_outside_offer_denied")
    $ game.main()

label trailer_interior_crystal_sex_repeat_outside_offer_accept:
    show player 14
    player_name "Alright but let's be quick!"
    show player 13
    show crystal undress 1 at center with dissolve
    crys "That's a good boy!"
    show crystal undress 3 with dissolve
    crys "So..."
    show player 426 zorder 2
    show crystal undress 4 at right with dissolve
    pause
    show crystal undress 5 with dissolve
    pause
    show crystal undress 6 with dissolve
    pause
    show crystal undress 7 with dissolve
    pause
    show crystal undress 10 with dissolve
    crys "What are you in the mood for?"
    crys "Pussy?"
    show crystal undress 9 with dissolve
    crys "Or..."
    show crystal undress 11_11b with dissolve
    crys "My ass?"
    return

label trailer_interior_crystal_sex_repeat_outside_offer_denied:
    show player 12
    player_name "We can't do that!"
    player_name "Not with {b}Roxxy{/b} so close!"
    show player 5
    show crystal 11 at center with dissolve
    crys "Tsk, fine."
    show crystal 6
    crys "I guess, I'll just entertain myself then..."
    show crystal 5
    show player 11
    player_name "..."
    show crystal 6
    crys "Have fun with my daughter, {b}[firstname]{/b}."
    hide player
    hide crystal
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
