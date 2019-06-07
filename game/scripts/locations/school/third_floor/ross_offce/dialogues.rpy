label ross_office_first_visit:
    scene school_office3_b with fade
    show player 11 with dissolve
    player_name "*Sniff*"
    show player 12
    player_name "What's that smell?"
    player_name "It's like...incense...and herbs..."
    player_name "{b}Miss Ross{/b} must be spending a lot of time in here."
    hide player with dissolve
    return

label ross_hscene_start:
    $ M_ross.set ("sex speed", 0.15)
    if M_ross.is_state(S_ross_paint_with_body):
        call expression game.dialog_select("ross_office_hscene")
        call expression game.dialog_select("ross_hscene_first_time")
    else:
        $ persistent.cookie_jar["Ross"]["gallery"]["02_unlocked"] = True
        scene location_school_office3_closeup_sex
        show rosss 1 at right
        with dissolve
    $ animated = False
    jump ross_hscene_loop

label ross_office_hscene:
    scene expression player.location.background_closeup
    show ross 13 at Position(xpos=0.35, ypos=1.0)
    show player 1f at Position(xpos=0.85, ypos=1.0)
    with dissolve
    ross "There's my little hero!"
    show ross 12
    show player 2f
    player_name "Wow, it smells really good in here!"
    show ross 13
    show player 1f
    ross "You like that? It's my favorite incense."
    ross "It really enhances the mood, don't you think?"
    show ross 12
    show player 10f
    player_name "Uhh, Sure. I guess..."
    player_name "What's with the giant canvas?"
    show player 11f
    show ross 13
    ross "Hehe, patience, {b}[firstname]{/b}. You can't rush this or the art will suffer."
    show player 10f
    show ross 12
    player_name "... Oh, okay."
    show player 11f
    show ross 13
    ross "Why don't you go lock the door. We don't want anyone to disturb us..."
    show player 2f
    show ross 12
    player_name "Alright."
    hide player with dissolve
    pause
    show ross 14 at Position(xpos=0.37, ypos=1.0) with dissolve
    pause
    show player 2f at Position(xpos=0.85, ypos=1.0)
    show ross 15 at Position(xpos=0.37, ypos=1.0)
    with dissolve
    player_name "... Okay, now wh-"
    show ross 16 at Position(xpos=0.35, ypos=1.0)
    show player 11f
    with dissolve
    pause
    show player 10f
    show ross 17 at Position(xpos=0.34, ypos=1.0) with dissolve
    player_name "... Eh?"
    show ross 37 at Position(xpos=0.36, ypos=1.0) with dissolve
    player_name "What are you doing, {b}Miss Ross{/b}?"
    show player 11f
    show ross 36
    ross "Oh, you'll need to undress as well..."
    ross "... We're going to be using our bodies to paint, {b}[firstname]{/b}."
    show ross 37
    show player 10f
    player_name "... Our bodies?"
    hide ross
    show rossp 9 at Position(xpos=0.34, ypos=1.0)
    with dissolve
    show player 11f
    player_name "( !!! )" with hpunch
    show rossp 10
    ross "That's right!"
    ross "Don't be shy now..."
    ross "Lose those clothes!"
    show rossp 9
    show player 10f
    player_name "... O-okay."
    show player 8f with dissolve
    pause
    show player 261 with dissolve
    pause
    show player 430f with dissolve
    show rossp 10
    ross "Wonderful!"
    ross "You're such a gifted young man, {b}[firstname]{/b}..."
    show player 430bf
    show rossp 9
    player_name "Heh, thanks."
    show player 430f
    ross "Mmmhmm."
    show rossp 10
    ross "Okay, for the next step..."
    ross "We're gonna need to add a little paint to the equation..."
    show rossp 9
    show player 430bf
    player_name "I'm not sure I..."
    hide ross
    show rossp 6 at Position(xpos=0.46, ypos=1.0)
    with dissolve
    show player 430f
    ross "Here take this."
    show rossp 9 at Position(xpos=0.34, ypos=1.0)
    show player 613 at Position(xpos=0.83, ypos=1.0)
    with dissolve
    pause
    show player 614
    player_name "... W-what am I painting exactly?"
    hide ross
    show rossp 1 at Position(xpos=0.41, ypos=1.0)
    with dissolve
    show player 613
    ross "Hehe, me silly!"
    ross "Don't worry, I'll show you."
    show rossp 2
    pause
    hide rossp
    hide player
    with dissolve
    scene black with fade
    ross "That's it, {b}[firstname]{/b}..."
    ross "Just go nuts with it!"
    player_name "..."
    ross "Hehe, that tickles!"
    scene expression player.location.background_closeup with fade
    show ross 48 zorder 0 at Position(xpos=0.43, ypos=1.0)
    show rosso 1 zorder 1 at Position(xpos=0.43, ypos=0.99)
    show player 616 zorder 2 at Position(xpos=0.73, ypos=1.0)
    with dissolve


    pause
    show player 615 at Position(xpos=0.745, ypos=1.0) with dissolve
    show ross 47
    ross "Well done, {b}[firstname]{/b}!"
    ross "Oh, I really love this technique!"
    hide rosso
    hide ross
    show rossp 3_4_5_4 at Position(xpos=0.43, ypos=1.0)
    with dissolve
    pause
    hide rossp
    show ross 47 zorder 0 at Position(xpos=0.43, ypos=1.0)
    show rosso 1 zorder 1 at Position(xpos=0.43, ypos=0.99)
    with dissolve
    ross "... This feels so amazing!"
    hide ross
    hide rosso
    show rossp 3_4_5_4 at Position(xpos=0.43, ypos=1.0)
    show player 432f at Position(xpos=0.855, ypos=1.0)
    with dissolve
    player_name "Where did you learn this anyways?"
    show rossp 10 zorder 0 at Position(xpos=0.4, ypos=1.0)
    show rosso 1 zorder 1 at Position(xpos=0.42, ypos=0.99)
    with dissolve
    show player 431f
    ross "Oh, it's just something I came up with a long time ago."
    ross "My first year of teaching actually."
    show rossp 9
    show player 432f
    player_name "Really?"
    show player 431f
    ross "Mmmhmm..."
    show rossp 10
    ross "... But we haven't even gotten to the best part yet."
    show rossp 9
    show player 432f
    player_name "... What's the best part?"
    show rossp 10
    show player 431f
    ross "I want you to make love to me, {b}[firstname]{/b}!"
    show player 430f
    player_name "( !!! )" with hpunch
    show player 430bf
    show rossp 9
    player_name "What?!"
    show player 430f
    show rossp 10
    ross "Make love to me! Right here on this canvas!"
    ross "Use my body to paint your masterpiece!"
    show player 430bf
    show rossp 9
    player_name "You really want to... With me?"
    hide player
    hide rosso
    show rossp 11_12 at Position(xpos=0.785, ypos=1.0)
    with dissolve
    ross "Of course I want to!"
    ross "I've wanted this big dick of yours inside me since the moment I saw that cute little giraffe you made out of clay."
    player_name "... You did?"
    ross "Oh, yes!"
    ross "Nothing turns me on more than a talented young artist!"
    player_name "... This feels really good."
    ross "It's about to feel a whole lot better!"
    ross "Come lay down."
    return

label ross_hscene_first_time:
    scene location_school_office3_closeup_sex
    show rosss 1 at right
    with dissolve
    ross "Oh, I can't believe it's finally happening!"
    ross "..."
    show rosss 2 with dissolve
    ross "Oooh, wow!"
    $ M_ross.set ("sex speed", 0.2)
    show expression AnimatedImage("rosss", [2,3,4,5,6,7,8,9,10,11], M_ross) as rosss at right
    pause 3
    ross "Oh my goddess! It's even better than I imagined!"
    pause 2
    player_name "Oh, {b}Miss Ross{/b}!"
    $ M_ross.set ("sex speed", 0.1)
    pause 5
    ross "It's never felt so good!"
    pause 5
    ross "This is incredible!"
    pause 2
    player_name "Ahhh!"
    pause 2
    ross "Why is this so good?!"
    $ M_ross.set ("sex speed", 0.06)
    pause 5
    ross "Oh, fuck me!"
    player_name "I can't-"
    player_name "You're going too fast!"
    pause 5
    ross "I love your dick, {b}[firstname]{/b}!"
    pause 2
    ross "Oh, I love it so much!"
    return

label ross_hscene_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("rosss", [2,3,4,5,6,7,8,9,10,11], M_ross) as rosss at right
                $ animated = True
            pause 1
            if animcounter in [1,3]:
                call expression game.dialog_select("ross_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [2,3,4,5,6,7,8,9,10,11]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "rosss {}".format(pose_list[pose_counter]) as rosss at right
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("ross_hscene_dialog")
        $ animcounter += 1
    call screen ross_sex_options

label ross_hscene_dialog:
    if M_ross.is_state(S_ross_paint_with_body):
        $ temp = choice_randomizer([(1, 1), (2, 2), (3, 1)])
    else:
        $ temp = choice_randomizer([(1, 1), (2, 2), (3, 2), (4, 1)])

    if temp == 1:
        if M_ross.is_state(S_ross_paint_with_body):
            ross "Oh my goddess! It's even better than I imagined!"
            player_name "Oh, {b}Miss Ross{/b}!"
        else:

            ross "Oh, I'm so glad you came by today!"
            ross "I really needed this!"
            player_name "Oh, that feels so good!"
            ross "Mmm, I love this dick so much!"
            ross "Give it to me, {b}[firstname]{/b}!"
            ross "That's it!"
            ross "AAAHHH!"

    elif temp == 2:
        if M_ross.is_state(S_ross_paint_with_body):
            ross "It's never felt so good!"
            ross "This is incredible!"
            player_name "Ahhh!"
            ross "Why is this so good?!"
        else:

            ross "That's it, {b}[firstname]{/b}!"
            ross "Oh, this is so beautiful!"
            ross "I want you to come a lot for me this time!"
            player_name "Oh, wow!"
            player_name "Ahhh!!"
            ross "That's it!"
            ross "Paint a white masterpiece on my ovarian canvas!"

    elif temp == 3:
        if M_ross.is_state(S_ross_paint_with_body):
            ross "Oh, fuck me!"
            player_name "I can't-"
            player_name "You're going too fast!"
            ross "I love your dick, {b}[firstname]{/b}!"
            ross "Oh, I love it so much!"
        else:

            ross "Oh, I'm still a little sore from our last session..."
            player_name "Should we stop?"
            ross "Don't you dare stop!"
            ross "Oh, yes!"
            ross "Yes! Yes! Fuck me!"
            ross "It's so good, {b}[firstname]{/b}!"
            player_name "Oh, {b}Miss Ross{/b}!!!"

    elif temp == 4:
        ross "I've been thinking about this all day!"
        player_name "You have?"
        ross "Yes..."
        ross "... All day..."
        ross "... just thinking about your happy little dick..."
        ross "... And how much I need it inside my happy little vagina!"
        player_name "..."
        ross "Oh, I'm gonna cum!"
        ross "OH FUCK!"
        ross "AAAHHHHH!!!"
    return

label ross_office_ross_sex_cum_dialogue:
    player_name "I can't hold it!"
    ross "Oh, I love it! I love it! I love it!"
    pause
    ross "AAAhhhh!!!"
    pause
    show rosss 12_13 at right with flash
    player_name "HNNGGG!!!"
    ross "{b}*GASP*{/b}!"
    ross "Mmmph!"
    pause
    show rosss 14 with dissolve
    ross "Haaah... Haaah..."
    ross "Wow!"
    ross "... {b}[firstname]{/b}."
    ross "That was..."
    show rosss 15 with dissolve
    pause
    show rosss 16 with dissolve

    ross "... I mean I've had a lot of sex in my life..."
    ross "... A lot of good sex!"
    ross "... But that was something else, entirely!"
    player_name "... Y-yeah."
    scene expression player.location.background_closeup
    show rossp 10 zorder 0 at Position(xpos=0.2, ypos=1.0)
    show rosso 1 zorder 1 at Position(xpos=0.22, ypos=1.0)
    show player 8f at right
    with dissolve
    ross "We need to do that again!"
    show player 1f with dissolve
    ross "I've never came so hard before!"
    show rossp 9
    player_name "..."
    show rossp 10
    ross "You wouldn't mind doing it again sometime, would you {b}[firstname]{/b}?"
    show rossp 9
    show player 2f
    player_name "Of course not!"
    player_name "I'll do that anytime you want!"
    show rossp 10
    show player 1f
    ross "Hehe, well I think that's enough for today..."
    ross "I'm exhausted..."
    show player 2f
    show rossp 9
    player_name "Yeah, me too."
    show player 1f
    show rossp 10
    ross "You come and find me in {b}my office{/b} whenever you need another \"private lesson.\" Okay?"
    show player 2f
    show rossp 9
    player_name "Heh, yes Ma'am!"
    return

label ross_office_ross_sex_cum:
    call expression game.dialog_select("ross_office_ross_sex_cum_dialogue")
    $ renpy.end_replay()
    $ game.timer.tick()
    $ M_ross.trigger(T_ross_sexual_body_painting)
    $ M_ross.set_default_locations([[L_school_artclassroom, L_school_rossoffice, L_school_rossoffice, L_NULL],
                                    [L_NULL, L_NULL, L_NULL, L_NULL]])
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
