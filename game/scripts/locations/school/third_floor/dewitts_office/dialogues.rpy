label dewitts_office_first_visit:
    scene school_office2_b with fade
    show player 14 with dissolve
    player_name "Wow... {b}Miss Dewitt's{/b} office has a sweet setup!"
    player_name "Looks like she brings students for private recordings..."
    player_name "...And she has a couch to hang out!!"
    hide player with dissolve
    return

label dewitts_office_dewitt_office_reward:
    scene expression game.timer.image("dewitt_office_c{}"):
    show player 55f at right
    show tyrone 6f at Position (xpos=500)
    show eve 5f at Position (xpos=400)
    show dewitt 28 at left
    with dissolve
    player_name "*Cough*"
    show player 10f with dissolve
    player_name "Jeez, what is going on in here?!"
    show player 11f
    show eve 6f
    eve "Hot box!"
    show eve 5f
    show tyrone 7f
    tyrone "Close the door, honky! You're letting all the smoke out!"
    show tyrone 8f at Position (xoffset=16) with dissolve
    show dewitt 30
    dewitt "Hey, be nice to {b}[firstname]{/b}! He's my little sugar!"
    show dewitt 28
    show tyrone 7f with dissolve
    tyrone "Pfft, hahaha!"
    show tyrone 6f
    show player 10f
    player_name "{b}Miss Dewitt{/b}?"
    player_name "What happened to your clothes?!"
    show player 11f
    pause
    show dewitt 29
    dewitt "Hmm?"
    dewitt "Oh! Yeah, I dunno. They're somewhere around here."
    show dewitt 28
    show tyrone 8f at Position (xoffset=16) with dissolve
    show player 212f
    player_name "..."
    show dewitt 30
    dewitt "Come dance with me!"
    show dewitt 28
    show tyrone 6f with dissolve
    show player 29f with dissolve
    player_name "Heh, I'm not much of a dancer."
    show player 3f at Position (xoffset=-8)
    show dewitt 29
    dewitt "Well that's alright, sugar."
    show dewitt 30
    dewitt "Just have a seat and I'll dance for you!"
    show dewitt 28
    show player 29f
    player_name "O-okay..."
    hide player
    hide dewitt
    hide eve
    hide tyrone
    with dissolve

    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_twerk{}")
    show dewitts 1
    show dewitt cloths 1c
    show player dewitts 1 zorder 2 at left
    dewitt "Check this out!"
    hide dewitts
    hide dewitt
    show expression AnimatedImage("dewitt_twerk", ["1c","2c","3c","4c","5c","6c","7c","8c","9c","10c"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve

    tyrone "Dayum! You really know how to shake that thing, {b}Miss Dewitt{/b}."
    eve "No shit! You think you can teach me to do that?"
    tyrone "Oh please, you gotta have some junk in your trunk to pull off those kinda moves!"
    eve "Hey dick! Don't be talking shit or I'll whoop your ass!"
    tyrone "You gotta catch me first, wonderbread!"
    eve "... Motherfucker!"
    scene expression game.timer.image("dewitt_office_sex{}")
    show expression AnimatedImage("dewitt_twerk", ["1c","2c","3c","4c","5c","6c","7c","8c","9c","10c"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    show player dewitts 1 zorder 2 at left
    with fastdissolve
    pause
    hide dewitt_twerk
    show dewitts 1
    show dewitt cloths 1c zorder 1
    with dissolve
    dewitt "Thank goodness they're gone."
    dewitt "So how about it, {b}[firstname]{/b}? You like my dancing?"
    show dewitts 2
    player_name "Y-Yeah!"
    player_name "You have the nicest butt!"
    show dewitts 1
    dewitt "Heh, you better believe it."
    dewitt "It's alright, sugar. You can touch it if you want."
    show dewitts 2
    player_name "Really?"
    hide player
    show dewitts 3b at left
    with dissolve
    pause
    show dewitts 4b
    dewitt "Mmmhmm."
    show dewitts 3b
    pause
    show dewitts 4b
    pause
    show player dewitts 1 zorder 2 at left
    hide dewitts
    show dewitts 1
    with dissolve
    dewitt "You like that juicy booty?"
    show dewitts 2
    player_name "..."
    show player dewitts 1b with hpunch
    show dewitts 2b
    dewitt "Eep!{p=1}{nw}"
    show player dewitts 1 with dissolve
    show dewitts 1
    dewitt "Oh my goodness, you naughty boy!"
    show dewitts 2
    show player dewitts 1b with hpunch
    pause 1
    show player dewitts 1 with dissolve
    show dewitts 1
    dewitt "Mmm."
    hide player
    show dewitts 3b at left
    with dissolve
    pause
    show dewitts 4b
    dewitt "..."
    show dewitts 3b
    pause
    show dewitts 4b
    pause
    show player dewitts 1 zorder 2 at left
    hide dewitts
    show dewitts 1
    with dissolve
    dewitt "Alright, we'd better stop. You're getting me all worked up!"
    show dewitts 2
    player_name "Oh, yeah. Okay."
    player_name "I suppose it is getting late."
    show dewitts 1
    dewitt "Time flies when you're having fun!"
    dewitt "Thanks again for today, {b}[firstname]{/b}. It really was an incredible surprise!"
    show dewitts 2
    player_name "My pleasure, {b}Miss Dewitt{/b}."
    player_name "See ya, tomorrow."
    show dewitts 1
    dewitt "Good night, sugar."
    hide dewitts
    hide dewitt cloths
    hide player
    with dissolve
    return

label dewitt_office_dewitt_night_visit:
    scene expression game.timer.image("dewitt_office_c{}")
    show dewitt 18 at left
    show player 14f at right
    with dissolve
    player_name "Hey {b}Miss Dewitt{/b}."
    player_name "What are you up to?"
    show player 13f
    show dewitt 19
    dewitt "Call me {b}Melody{/b}, sugar."
    dewitt "I was just giving this new track here a listen."
    dewitt "What do you think of it?"
    show dewitt 18
    show player 17f
    player_name "Hmm, it's nice! I like the beat of it!"
    show player 14f
    player_name "Who is it?"
    show player 13f
    show dewitt 19
    dewitt "Heh, it's one of mine!"
    show dewitt 18
    show player 14f
    player_name "Really?!"
    player_name "I didn't know you made your own music!"
    show player 13f
    show dewitt 19
    dewitt "Well I try..."
    dewitt "I made this one for somebody special."
    show dewitt 18
    show player 14f
    player_name "Oh yeah?"
    player_name "Anybody I would know?"
    show player 13f
    show dewitt 19
    dewitt "Mmm, Yeah. I think you might have heard of him..."
    dewitt "He really helped me out of a jam recently."
    show dewitt 18
    show player 14f
    player_name "Sounds like a nice guy..."
    show player 13f
    show dewitt 19
    dewitt "Heh, oh sugar. He's a VERY nice guy."
    dewitt "... And he needs to take a seat right here..."
    show dewitt 18
    show player 10f
    player_name "What's going on, {b}Melody{/b}?"
    show player 5f
    show dewitt 19
    dewitt "Well, you put on such a good show for me..."
    dewitt "It's only fair I return the favor."
    show dewitt 20 with dissolve
    show player 26f
    pause
    show dewitt 31f with dissolve
    pause
    show dewitt 32f with dissolve
    pause
    show dewitt 18b with dissolve
    pause
    show player 435f
    player_name "... Wow!"
    player_name "You look... Beautiful, {b}Miss Dewitt{/b}!"
    show dewitt 19b
    dewitt "Hehe, I've got curves in all the right places, sugar!"
    dewitt "... But I know what you want."

    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_sex{}"):
    show dewitts 1
    show player dewitts 1 zorder 2 at left
    with dissolve
    dewitt "What do you think of that ass, {b}[firstname]{/b}?"
    player_name "{b}*Gulp*{/b}"
    player_name "It's..."
    player_name "It's amazing!"
    player_name "I love the way it jiggles!"
    dewitt "Mmm, then you're gonna love this, sugar!"
    hide dewitts
    show expression AnimatedImage("dewitt_twerk", ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"], M_dewitt) as dewitt_twerk at top
    with dissolve
    player_name "!!!"
    pause
    player_name "This is so sexy, {b}Miss Dewitt{/b}!"
    dewitt "{b}Melody{/b}, {b}[firstname]{/b}..."
    player_name "Sorry. This is so sexy, {b}Melody{/b}!"
    dewitt "Heh, well I'm glad you like it..."
    dewitt "Why don't you take out that big dick of yours?"
    player_name "Really?"
    dewitt "Mmmhmm..."
    scene black with fade
    pause 0.25
    scene expression game.timer.image("dewitt_office_sex{}"):
    show dewitts 1
    show player dewitts 2 zorder 2 at left
    with dissolve
    dewitt "Damn, that's a nice one!"
    dewitt "I wonder if it feels as nice as it tastes?"
    show dewitts 2
    player_name "You mean I can-"
    player_name "... Y-you want me to..."
    hide player
    show dewitts 3 at left
    with dissolve
    dewitt "Mmm, I want you to give it to me, {b}[firstname]{/b}!"
    show dewitts 4
    dewitt "Right there, sugar..."
    show dewitts 5 with dissolve
    pause
    show expression AnimatedImage("dewitts", [5,6,7,8,9,10,11,12,13,14], M_dewitt) as dewitts
    jump expression game.dialog_select("dewitt_sex_loop")

label dewitt_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("dewitts", [5,6,7,8,9,10,11,12,13,14], M_dewitt) as dewitts
                $ animated = True
            pause 1
            call expression game.dialog_select("dewitt_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [5,6,7,8,9,10,11,12,13,14]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "dewitts {}".format(pose_list[pose_counter]) as dewitts
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("dewitt_hscene_dialog")
        $ animcounter += 1
    call screen dewitt_sex_options

label dewitt_bj_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("dewitts_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_dewitt) as dewitts_bj
                $ animated = True
            pause 1
            call expression game.dialog_select("dewitt_bj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "dewitts_bj {}".format(pose_list[pose_counter]) as dewitts_bj
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("dewitt_bj_hscene_dialog")
        $ animcounter += 1
    call screen dewitt_office_bj_options

label dewitt_twerk_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("dewitt_twerk", ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
                $ animated = True
            pause 1
            call expression game.dialog_select("dewitt_twerk_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "dewitt_twerk {}".format(pose_list[pose_counter]) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("dewitt_twerk_hscene_dialog")
        $ animcounter += 1
    call screen dewitt_twerk_options

label dewitt_hscene_dialog:
    if animcounter == 0:
        if randomizer() <= 50:
            dewitt "Oh, fuck yeah!{p=2}{nw}"
            dewitt "That's it big boy!{p=2}{nw}"
            dewitt "Mmm...{p=1}{nw}"

        elif not M_dewitt.is_state(S_dewitt_office_night_visit):
            dewitt "Oh yeah, baby!{p=2}{nw}"
            dewitt "This is just what I needed!{p=2}{nw}"
        else:

            player_name "Oh, wow!{p=1}{nw}"
            player_name "{b}Melody{/b}! This is awesome!{p=2}{nw}"
            dewitt "Mmmhmm...{p=1}{nw}"

    elif animcounter == 2:
        if randomizer() <= 50:
            dewitt "Pound that pussy, sugar!{p=2}{nw}"
            dewitt "Give it to me, {b}[firstname]{/b}!{p=2}{nw}"
            dewitt "Ahhh!{p=1}{nw}"

        elif not M_dewitt.is_state(S_dewitt_office_night_visit):
            dewitt "Fuck, this dick is so good!{p=2}{nw}"
            player_name "I love watching you ride it, {b}Miss Dewitt{/b}...{p=3}{nw}"
            dewitt "Heh, Mmm...{p=1}{nw}"

    elif animcounter == 3:
        if randomizer() <= 50:
            dewitt "Fuuuck, it's so deep!!{p=2}{nw}"
            dewitt "That's it, Baby! I'm gonna cum all over that big dick!{p=3}{nw}"
            dewitt "Mmmm!!{p=1}{nw}"

        elif not M_dewitt.is_state(S_dewitt_office_night_visit):
            dewitt "Ahhh!{p=1}{nw}"
            dewitt "Give it to me harder, baby!{p=2}{nw}"
            dewitt "Fuuuuuu!!!{p=1}{nw}"
    return

label dewitt_bj_hscene_dialog:
    if animcounter == 1:
        if randomizer() <= 50:
            player_name "Ohh...{p=1}{nw}"
        else:

            player_name "Uhh!{p=1}{nw}"

    elif animcounter == 3 and randomizer() <= 50:
        dewitt "Mmmmm!{p=1}{nw}"
    return

label dewitt_twerk_hscene_dialog:
    if animcounter == 0:
        if randomizer() <= 50:
            player_name "Ohh...{p=1}{nw}"
        else:
            player_name "Uhh!{p=1}{nw}"

    elif animcounter == 2 and randomizer() <= 50:
        dewitt "Mmm!!!{p=1}{nw}"

    elif animcounter == 3 and randomizer() <= 50:
        show player dewitts 1b with hpunch
        show player dewitts 1 with dissolve
        dewitt "Nnnggh!{p=1}{nw}"
        dewitt "You gonna make me beg for it, {b}[firstname]{/b}?{p=2}{nw}"
    return

label dewitt_sex_cum_first:
    player_name "{b}Melody{/b}, I'm gonna..."
    player_name "I'm gonna!!"
    dewitt "Do it, Baby!"
    dewitt "I'm ready!"
    $ M_dewitt.set("sex speed", 0.4)
    show dewitts 15_16 at left with flash
    player_name "HNNGGG!!!"
    dewitt "AH, FUCK YEEEEAAAHHH!!"
    player_name "{b}Miss Dewitt{/b}!!"
    dewitt "NNGGHH!!!"
    player_name "Haaah... Haaah..."
    show dewitts 17 with dissolve
    dewitt "{b}*Phew*{/b}."
    show dewitts 18 with dissolve
    dewitt "Damn, that was good!"
    dewitt "You got something special there, sugar!"
    player_name "Y-yeah! You too, {b}Melody{/b}..."
    hide dewitts with dissolve

    scene expression game.timer.image("dewitt_office_c{}")
    show player 13f at right
    show dewitt 19b at left
    with dissolve
    dewitt "You gotta come back and do that again!"
    show dewitt 18b
    show player 14f
    player_name "For real?!"
    show player 13f
    show dewitt 19b
    dewitt "Absolutely!"
    dewitt "I ain't letting you get away!"
    dewitt "I want that dick on the regular!"
    show dewitt 18b
    show player 17f
    player_name "Heh, I'm down for that."
    show player 13f
    show dewitt 19b
    dewitt "Good! You come and see me anytime, sugar!"
    dewitt "My doors always open."
    show dewitt 18b
    show player 14f
    player_name "Thanks, {b}Melody{/b}."
    show player 434f
    pause
    hide player
    hide dewitt
    with dissolve
    $ renpy.end_replay()
    return

label dewitt_sex_cum_repeat:
    player_name "OH! Here it comes!"
    dewitt "Fill me up, sugar!"
    dewitt "Mmm!"
    dewitt "I'm gonna cum all over those balls!"
    $ M_dewitt.set("sex speed", 0.4)
    show dewitts 15_16 at left with flash
    player_name "HNNGGG!!!"
    dewitt "NNGGHH!!!"
    dewitt "Fuck!!"
    player_name "Haaah... Haaah..."
    show dewitts 17 with dissolve
    dewitt "{b}*Phew*{/b}."
    show dewitts 18 with dissolve
    dewitt "Mmm..."
    dewitt "Good boy."
    hide dewitts with dissolve

    scene expression game.timer.image("dewitt_office_c{}")
    show player 13f at right
    show dewitt 19b at left
    with dissolve
    dewitt "Thanks for the good time, sugar."
    dewitt "See you again, soon?"
    show dewitt 18b
    show player 14f
    player_name "Of course!"
    show player 434f
    pause
    show dewitt 19b
    dewitt "Heh, Sweet Dreams, baby!"
    show dewitt 18b
    show player 14f
    player_name "Goodnight, {b}Melody{/b}!"
    hide player
    hide dewitt
    with dissolve
    $ renpy.end_replay()
    return

label dewitt_sex_cum:
    if M_dewitt.is_state(S_dewitt_office_night_visit):
        call expression game.dialog_select("dewitt_sex_cum_first")
        $ persistent.cookie_jar["Dewitt"]["gallery"]["03_unlocked"] = True
        $ M_dewitt.trigger(T_dewitt_sex_it_up)
        $ M_dewitt.set_default_locations([[L_school_musicclassroom, L_school_dewittoffice, L_school_dewittoffice, L_NULL],
                                          [L_NULL, L_NULL, L_NULL, L_NULL]])
    else:

        call expression game.dialog_select("dewitt_sex_cum_repeat")
    $ player.go_to(L_school_floor3)
    $ game.timer.tick()
    $ game.main()

label dewitt_bj_cum:
    hide dewitts_bj
    show dewitt bj 5 at left
    with flash
    player_name "OHHH!!!"
    show dewitt bj 6
    player_name "{b}Miss Dewitt{/b}!"
    show dewitt bj 7
    dewitt "Mmmmm..."
    scene black with fade

    scene expression game.timer.image("dewitt_office_c{}")
    show player 13f at right
    show dewitt 19 at left
    with dissolve
    dewitt "I was hoping to hear another rousing speech!"
    dewitt "Or was my encore so good it left you speechless?"
    show dewitt 18
    show player 14f
    player_name "Heh. You were awesome."
    show player 13f
    show dewitt 19
    dewitt "Come back for more! I'll blow on that flute any day!"
    hide player
    hide dewitt
    with dissolve
    $ player.go_to(L_school_floor3)
    $ game.timer.tick()
    $ game.main()

label dewitts_office_night_lock:
    scene expression game.timer.image("school_hall_third_floor{}_b"):
    show player 55 at Position (xoffset=12) with dissolve
    pause
    show player 56 with dissolve
    player_name "I should go home and get some rest."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
