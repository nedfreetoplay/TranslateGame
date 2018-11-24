label shower_mom_sis_check:
    scene shower_cutscene1
    show text "I rushed upstairs towards {b}[jen_name]{/b}'s cursing.\nThe scene upon entering was almost comical. {b}[jen_name]{/b} was absolutely flustered and looked like a drowned rat.\nThe exposed pipe was spouting water all over the place and making quite a mess." at Position(xpos=500, ypos=700)
    with dissolve
    $ renpy.pause()
    hide shower_cutscene1
    hide text
    scene shower2
    show player 11 at left
    show jenny 27 at right
    with dissolve
    jen "About time you showed up!"
    show player 10
    show jenny 26
    player_name "How did this happen?!"
    show player 11
    show jenny 27
    jen "How should I know! Do I look like a plumber to you?! All I did was turn on the sink!"
    show player 12
    show jenny 26
    player_name "What am I supposed to do?"
    show player 11
    show jenny 27
    jen "Fix it obviously! You're the only man around here after all!"
    show jenny 26
    show player 12
    player_name "Fine! I guess I'll head {b}downstairs{/b} and see about shutting off the {b}water valve{/b}..."
    hide player
    hide jenny
    with dissolve
    return

label shower_mom_close_valve:
    scene shower2
    show jenny 27 at right
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
    show jenny 29 at Position (xpos=800)
    show player 11 at left
    with dissolve
    jen "Looks like you got it. The water stopped."
    show player 12
    show jenny 26 at right
    player_name "Yeah, I turned off the water valve. Now what?"
    show player 5
    show jenny 27
    jen "What are you asking me for? I don't know, replace it or something?"
    show player 10
    show jenny 26
    player_name "I've never worked on anything like this before!"
    show player 5
    show jenny 27
    jen "Well you're living in a house with girls now which means you need to learn how to fix these kinda things!"
    show player 10
    show jenny 26
    player_name "Okay! Okay! I guess I'll go to {b}CONSUM-R{/b} and see about getting a pipe {b}wrench{/b}."
    show player 212
    player_name "..."
    show player
    show jenny 28
    $ renpy.pause()
    show jenny 27
    jen "..."
    jen "Did you get a good look you little Perv?!"
    show player 23
    show jenny 26
    player_name "I wasn't-"
    show player 22
    show jenny 41 at Position(xpos=0.9123,ypos=1.0000)
    jen "Oh please, You think I can't tell when someone is staring at my tits?"
    player_name "..."
    jen "What's the matter with you?"
    show player 24
    show jenny 30
    player_name "I'm sorry, {b}[jen_name]{/b}. I was just-"
    show jenny 31
    jen "Oh, shut up!"
    show player 25
    jen "If you're going to stare, at least be a man about it!"
    jen "Denying it or making excuses just makes you look like a wimp."
    jen "No one wants to be checked out by a spineless little wimp!"
    show player 5
    player_name "..."
    show jenny 27 at right
    jen "If you had gotten up here to deal with this pipe situation sooner, perhaps I'd be in a better mood."
    show jenny 41 at Position(xpos=0.9123,ypos=1.0000)
    jen "... But since you decided to take your Sweet time..."
    jen "I think you should take this..."
    show player 22
    show jenny 32
    $ renpy.pause()
    show jenny 33
    $ renpy.pause()
    show player 23
    show jenny 42 at right
    jen "... Downstairs to the wash for me."
    player_name "( !!! )" with hpunch
    show player 21
    player_name "S-Sure..."
    show jenny 37
    show player 211
    jen "..."
    show jenny 38
    jen "Stop staring and go! I don't want to wait around all day for you to {b}fix that pipe{/b}!"
    show player 22
    player_name "( !!! )"
    hide player with dissolve
    show jenny 36
    jen "Heh, I knew it!"
    jen "That little loser has a thing for me!"
    hide jenny with dissolve
    hide shower2
    return

label shower_mom_fix_pipe_no_wrench:
    scene shower2
    show player 11 at left
    if not game.timer.is_dark():
        show jenny 27 at right
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
    show jenny 11f at Position(xpos=0.3649,ypos=1.0000)
    show debbie 62f at left
    with dissolve
    deb "Wow!!"
    deb "Great work, {b}[firstname]{/b}!"
    show jenny 9f
    show debbie 61f
    jen "Finally..."
    show jenny 11f
    show debbie 62f
    deb "Don't be rude, {b}[jen_name]{/b}. It was nice of him to fix this for us..."
    show player 2f
    show jenny 11f
    show debbie 61f
    player_name "Heh, not problem."
    player_name "I was happy to do it."
    player_name "... Besides, {b}[jen_name]{/b} is right. Fixing stuff like this is my responsibility now."
    show player 29f
    show jenny 10f
    show debbie 62f
    deb "You're going to make some lucky girl a great husband one day!"
    show player 203f
    show jenny 9f
    show debbie 61f
    jen "Pfft..."
    jen "Don't say things like that, you'll give him a big head!"
    show player 16f
    show jenny 12f
    jen "He's still a wimp, after all."
    show player 15f
    show jenny 11f
    show debbie 61f
    player_name "I am not a wimp!"
    show player 16f
    show jenny 12f
    jen "Hah, whatever, Wimp!"
    show player 1f
    show jenny 11f
    show debbie 62f
    deb "... Don't listen to her, {b}[firstname]{/b}. She's only teasing you because she thinks you're cute."
    show jenny 9f
    show debbie 59f
    jen "... As if!"
    show player 11f
    jen "... Now can you two get out? I've been waiting to shower all day!"
    show jenny 10f
    show debbie 60f
    show player 1f
    deb "C'mon, {b}[firstname]{/b}. Let's get out of Princess's way before her foul mood infects us."
    show jenny 9f
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
    player_name "( {b}[deb_name]{/b}'s body looks real good but I don't want to peek at her too long... )"
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
    player_name "... It's a shame she only sees me as my {b}Father{/b}'s kid."
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
    scene shower_closeup
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
    scene shower_closeup
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
    scene shower_closeup
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

label shower_sis_sex_pre:
    scene shower3 with None
    player_name "( {b}[jen_name]{/b} is in the shower... )"
    player_name "( ... and she hasn't noticed me yet? )"
    player_name "( Maybe I could... )"
    return

label shower_sis_sex_peep_after_cuddle:
    scene shower05a
    player_name "( ...She left her door open again... )"
    scene shower05b
    player_name "( ...It's like she wanted me to watch? )"
    scene shower05c
    player_name "( She really has a great body. )"
    scene shower05b
    scene shower05a
    player_name "..."
    show shower 05d_05e
    player_name "( ...Is she- )"
    player_name "( Wow... )"
    player_name "( ...I should... )"
    player_name "( ...leave, before she notices... )"
    hide shower 05d_05e
    hide shower05a
    return

label shower_sis_sex_peep_before_cuddle:
    scene shower3
    player_name "Oh shit! {b}[jen_name]{/b} is in the shower..."
    scene shower4 with hpunch
    player_name "( CRAP!! She saw me! )"
    scene shower2
    show jenny 3 at right
    show player 6 at left
    with dissolve
    jen "What's wrong with you??!"
    jen "Can't you see I'm in here?"
    show jenny 2 at Position(xpos=962) with fastdissolve
    player_name "The door was unlocked!"
    show player 3 with fastdissolve
    jen "Knock first next time, you pervert!"
    show player 29
    player_name "Sorry! I thought no one was in here..."
    hide jenny
    hide player
    with dissolve
    hide shower2
    return

label shower_sis_sex_go_inside:
    scene shower2b
    show player 11 at Position(xpos=261)
    with fade
    player_name "( I can't believe I'm about to do this... )"
    show player 4 at Position(xpos=267)
    player_name "( Will she scream at me this time, or will she let me stay? )"
    player_name "( She left the door open like she's inviting me... )"
    show player 13 at Position(xpos=261)
    player_name "( I know... )"
    show player 249 at left with fastdissolve
    player_name "( I can just pretend like I didn't see her! )"
    show player 261f at Position(xpos=137) with fastdissolve
    player_name "( Alright, I'm going in... )"
    return

label shower_sis_sex_leave:
    player_name "( No, too risky... )"
    return

label shower_sis_sex_intro:
    $ game.timer.tick()
    if sis_shower_intro_first:
        call expression game.dialog_select("shower_sis_sex_intro_first")
        $ sis_shower_intro_first = False
    else:

        call expression game.dialog_select("shower_sis_sex_intro_repeat")
    if not store._in_replay == None:
        jump expression game.dialog_select("sis_shower_jump_1")

    elif M_jenny.is_state(S_jenny_shower_peep_bed_cuddle_tier_2):
        $ M_jenny.trigger(T_jenny_peep_cuddle_tier_2)
    menu:
        "Oops, Sorry!":
            call expression game.dialog_select("shower_sis_sex_intro_sorry")
        "Need help?":

            if sis_shower_intro_first:
                call expression game.dialog_select("shower_sis_sex_intro_help_fail")
            else:

                label sis_shower_jump_1:
                    call expression game.dialog_select("shower_sis_sex_intro_help_pass")
            $ M_jenny.set("seen MCs penis", True)
            call expression game.dialog_select("sis_shower_sex")
    hide jenny
    hide player
    with dissolve
    $ playSound()
    jump expression game.dialog_select("hallway_dialogue")

label shower_sis_sex_intro_first:
    scene shower_closeup
    show player 342 at Position(xpos=160)
    show jenny 163 at Position(xpos=791)
    with fade
    pause
    show jenny 163b with fastdissolve
    pause
    show jenny 106 with fastdissolve
    jen "Well well..."
    jen "I was wondering when you'd follow me in here."
    show jenny 105
    return

label shower_sis_sex_intro_repeat:
    scene shower_closeup
    show player 342 at Position(xpos=160)
    show jenny 163 at Position(xpos=791)
    with fade
    pause
    show jenny 163b with fastdissolve
    jen "Huh?"
    show jenny 104
    jen "{b}[firstname]{/b}?!" with hpunch
    jen "What the fuck?!"
    jen "Can't you see I'm in here?!!"
    show jenny 105
    return

label shower_sis_sex_intro_sorry:
    show jenny 105
    show player 343
    player_name "Oops!"
    player_name "Sorry! I didn't see you..."
    show jenny 106
    show player 342
    jen "Didn't I tell you to knock first?! You idiot!"
    show player 343
    show jenny 105
    player_name "I know but-"
    show jenny 104
    show player 342
    jen "Shut up and {b}GET OUT{/b}!!" with hpunch
    return

label shower_sis_sex_intro_help_fail:
    show jenny 105
    show player 343
    player_name "I thought, maybe you needed help again..."
    show jenny 107
    show player 342
    jen "Help? Ha!!"
    show jenny 106
    jen "More like me helping myself, while a perverted idiot watches..."
    jen "You really can't stop spying on me, can you?"
    show jenny 105
    player_name "..."
    return

label shower_sis_sex_intro_help_pass:
    show jenny 105
    show player 343
    player_name "I know..."
    player_name "I was wondering if... you know... you need help?"
    show jenny 104
    show player 342
    jen "Help??"
    show jenny 106
    jen "Oh! Haha!"
    show jenny 105
    show player 343
    player_name "What's so funny?"
    show player 342
    show jenny 106
    jen "Gosh... you're so {b}pathetic{/b}."
    jen "I know you just want to see me naked!"
    show jenny 105
    player_name "..."
    return

label sis_shower_sex:
    call expression game.dialog_select("sis_shower_sex_pre")
    if not store._in_replay == None:
        call expression game.dialog_select("sis_shower_jump_2")
    menu:
        "Leave.":
            call expression game.dialog_select("sis_shower_sex_leave")

        "Beg." if not M_jenny.finished_state(S_jenny_hallway_meetup_focus):
            call expression game.dialog_select("sis_shower_sex_first_beg_fail")

        "Beg." if M_jenny.finished_state(S_jenny_hallway_meetup_focus):
            $ M_jenny.trigger(T_jenny_peep_cuddle_tier_3)
            label sis_shower_jump_2:
                call expression game.dialog_select("sis_shower_sex_first_beg_pass")
            if not store._in_replay == None:
                call expression game.dialog_select("sis_shower_jump_3")
            menu:
                "Leave.":
                    call expression game.dialog_select("sis_shower_sex_leave")

                "Beg." if not M_jenny.finished_state(S_jenny_telescope_spying_tier_3):
                    call expression game.dialog_select("sis_shower_sex_second_beg_fail")

                "Beg." if M_jenny.finished_state(S_jenny_telescope_spying_tier_3):
                    $ M_jenny.trigger(T_jenny_peep_cuddle_tier_4)
                    label sis_shower_jump_3:
                        call expression game.dialog_select("sis_shower_sex_second_beg_pass")
                    if not store._in_replay == None:
                        call expression game.dialog_select("sis_shower_jump_4")
                    menu:
                        "Put it inside." if not M_jenny.finished_state(S_jenny_cam_show) or player.stats.dex() < 7:
                            call expression game.dialog_select("sis_shower_sex_put_it_in_fail")

                        "Put it inside." if M_jenny.finished_state(S_jenny_cam_show) and player.stats.dex() >= 7:
                            $ M_jenny.trigger(T_jenny_peep_cuddle_tier_5)
                            label sis_shower_jump_4:
                                $ M_jenny.set("sex speed", .4)
                                $ anim_toggle = True
                                $ animated = False
                                $ xray = False
                            call expression game.dialog_select("sis_shower_sex_put_it_in_pass")
                            jump expression game.dialog_select("sis_shower_sex_loop")
    hide jenny
    hide player
    with dissolve
    $ playSound()
    jump expression game.dialog_select("hallway_dialogue")

label sis_shower_sex_pre:
    show jenny 107
    show player 342
    jen "Okay, I'll let you stay..."
    show jenny 106
    jen "... but, you'll only help by {b}looking{/b} with your {b}eyes{/b}."
    show jenny 104
    jen "Got it?!"
    show jenny 105
    show player 343
    player_name "Yes, {b}[jen_name]{/b}..."
    show player 342
    show jenny 109 at right
    jen "Good."
    jen "Now..."
    show jenny 110 with fastdissolve
    jen "I like my breasts nice and soapy..."
    show jenny 111
    jen "So, I like to use loooots of soap!"
    show jenny 112 with fastdissolve
    pause
    show jenny 113 with fastdissolve
    pause
    show jenny 115 with fastdissolve
    jen "Do you like seeing all this... {b}cream{/b} on me?"
    jen "Does it make you think of something {b}else{/b}?"
    show jenny 114
    show player 343
    player_name "I... I don't know..."
    show player 342
    jen "Hmm..."
    show jenny 115
    show player 344
    jen "Let's lather them up a little!"
    show jenny 116 at Position(xpos=984) with fastdissolve
    pause
    show jenny 117_118_119_116 at Position(xpos=980)
    pause 8
    show player 345 at left
    show jenny 122 at Position(xpos=980)
    player_name "Uh oh..."
    show jenny 120b
    show player 346 with fastdissolve
    pause 0.05
    show player 347 with vpunch
    pause
    show jenny 120
    jen "Well, that was easy!"
    show player 348 at Position(xpos=60)
    show jenny 109 at Position(xpos=1024)
    jen "Since you seem to be enjoying this, maybe we can wash {b}another{/b} part of my body..."
    show jenny 108
    show player 349
    player_name "Okay..."
    show jenny 109
    show player 348
    jen "First, I want to hear you {b}beg{/b} for it."
    show jenny 167
    show player 349
    player_name "What do you mean?"
    show jenny 166
    show player 348
    jen "Which part of that didn't you understand?"
    show jenny 164
    jen "... I'm not doing it, unless you {b}beg{/b} for it!"
    show jenny 167
    show player 349
    player_name "Beg... for what exactly?"
    show jenny 109
    show player 348
    jen "I want you to {b}beg{/b} to see my pussy."
    show jenny 108
    return

label sis_shower_sex_leave:
    show player 349
    show jenny 167
    player_name "I think I'll just leave..."
    show player 348
    jen "???"
    show jenny 166
    jen "You won't do it?"
    show player 349
    show jenny 165
    player_name "No, sorry."
    show player 354
    show jenny 164
    jen "You think you're {b}too good{/b} for this?!"
    show player 349
    show jenny 165
    player_name "It's not like-"
    show player 354
    show jenny 164
    jen "Shut up and {b}GET OUT{/b}!!" with hpunch
    return

label sis_shower_sex_first_beg_fail:
    show player 349
    show jenny 108
    player_name "Can... you show me your pussy?"
    show player 348
    show jenny 109
    jen "I didn't hear a {b}please{/b}."
    show player 349
    show jenny 167
    player_name "Can you please show me your pussy, {b}[jen_name]{/b}?"
    show player 348
    show jenny 166
    jen "You know what..."
    jen "I don't think you deserve this, even if you begged for it."
    jen "You're too pathetic, anyway."
    show player 349
    show jenny 167
    player_name "But, I thought you needed help-"
    show player 348
    show jenny 166
    jen "Maybe later... if you treat me a little better..."
    show jenny 164
    show player 354
    jen "Now, {b}GET OUT{/b}!!" with hpunch
    return

label sis_shower_sex_first_beg_pass:
    show player 349
    show jenny 108
    player_name "Can... you show me your pussy?"
    show jenny 109
    show player 348
    jen "I didn't hear a {b}please{/b}."
    show jenny 108
    show player 349
    player_name "Can you please show me your pussy, {b}[jen_name]{/b}?"
    show player 348
    show jenny 109
    jen "Alright..."
    show jenny 127
    show player 344b
    with fastdissolve
    jen "Let's wash this part of my body... right here..."
    show jenny 124_125_126_123
    pause 8
    jen "Hmm..."
    show jenny 127
    jen "You know what?"
    jen "I can't reach back there so... I might need some help after all..."
    show player 349 at Position(xpos=60)
    show jenny 123
    player_name "...My help?"
    show player 348
    show jenny 109 at Position(xpos=1024) with fastdissolve
    jen "Not exactly..."
    jen "First, put some soap on it."
    show jenny 167
    show player 349
    player_name "On it?"
    show player 348
    show jenny 166
    jen "On your {b}dick{/b}, you idiot!"
    show jenny 111 with fastdissolve
    jen "Here, take it!"
    show jenny 108
    show player 356
    with fastdissolve
    pause
    show player 350 with fastdissolve
    pause
    show player 348 with fastdissolve
    show jenny 109
    jen "Now, you know what to do..."
    show jenny 108
    show player 349
    player_name "I don't know..."
    show jenny 109
    show player 348
    jen "I want to hear you {b}beg{/b} for it, but for {b}REAL{/b} this time..."
    show jenny 108
    return

label sis_shower_sex_second_beg_fail:
    show player 349
    show jenny 167
    player_name "Can I... please help you, {b}[jen_name]{/b}?"
    show jenny 164
    show player 354
    jen "WRONG!!" with hpunch
    show jenny 109
    show player 348
    jen "I want you to call me {b}princess{/b}..."
    show jenny 167
    show player 349
    player_name "Can I please help you, {b}princess{/b}?"
    show player 348
    show jenny 166
    jen "You know what?"
    jen "I don't think you deserve this, even if you begged for it."
    jen "You're too pathetic anyway."
    show player 349
    show jenny 167
    player_name "But, I thought you needed help-"
    show player 348
    show jenny 166
    jen "Maybe later... if you treat me a little better..."
    show jenny 164
    show player 354
    jen "Now, {b}GET OUT{/b}!!" with hpunch
    return

label sis_shower_sex_second_beg_pass:
    show jenny 167
    show player 349
    player_name "Can I... please help you, {b}[jen_name]{/b}?"
    show player 354
    show jenny 164
    jen "WRONG!!" with hpunch
    show jenny 109
    show player 348
    jen "I want you to call me {b}princess{/b}..."
    show jenny 108
    show player 349
    player_name "Can I please help you, {b}princess{/b}?"
    show player 354
    show jenny 164
    jen "LOUDER!!" with hpunch
    show player 355
    show jenny 108
    player_name "Can..."
    player_name "{b}CAN I PLEASE HELP YOU, PRINCESS{/b}?!!" with hpunch
    show player 348
    show jenny 109
    jen "MUCH better!"
    jen "Sure."
    jen "I'll let you help me..."
    show jenny 166
    jen "... but, {b}NO TOUCHING{/b} with your hands!!"
    hide player
    hide jenny
    show jennysex 96
    with fastdissolve
    jen "Understood?!"
    show jennysex 95 at Position(xpos=511)
    player_name "Yes, {b}[jen_name]{/b}..."
    show jennysex 92_93_94_95 at Position(xpos=511)
    pause 8
    show jennysex 96 at Position(xpos=512)
    jen "You like that, you little pervert?"
    show jennysex 93 at Position(xpos=534)
    pause
    show jennysex 94 at Position(xpos=513)
    pause
    show jennysex 95 at Position(xpos=511)
    return

label sis_shower_sex_put_it_in_fail:
    hide jennysex
    show jenny 129 zorder 1 at Position(xpos=443)
    show player 351 zorder 2 at Position(xpos=260)
    jen "[dex_warn]Not so fast, pervert!!" with hpunch
    jen "[dex_warn]Just what are you trying to do here?!"
    show jenny 128
    player_name "!!!"
    show jenny 130
    jen "Didn't I tell you {b}NO HANDS{/b}??"
    show player 351b
    show jenny 131
    player_name "Sorry... I couldn't resist..."
    show jenny 132
    show player 351
    jen "You're lucky I let you go this far!"
    show jenny 131
    show player 351b
    player_name "I..."
    player_name "I'm sorry!!"
    show jenny 130
    show player 351
    jen "Shut up and {b}GET OUT{/b}!!" with hpunch
    return

label sis_shower_sex_put_it_in_pass:
    show jennysex 98
    jen "Ahh!!!" with hpunch
    show jennysex 97
    jen "What are you DOING?!!"
    show jennysex 101 at Position(xpos=476)
    player_name "I want you, {b}[jen_name]{/b}!!!"
    return

label sis_shower_sex_loop:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jennysex", [98,99,100,101], M_jenny) as jennysex at Position(xpos = 511)
                $ animated = True
            pause 5
            if animcounter in [1,3]:
                call expression game.dialog_select("jenny_shower_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [98,99,100,101]
            $ xpos_list = [511,518,497,476]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jennysex {}".format(pose_list[pose_counter]) as jennysex at Position(xpos = xpos_list[pose_counter])
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("jenny_shower_hscene_dialog")
        $ animcounter += 1
    jen "Don't you dare cum inside me...{p=2}{nw}"
    if not anim_toggle:
        show jennysex 97 at Position(xpos=511)
    jen "... I swear, I'll {b}KILL YOU{/b}!!{p=2}{nw}"
    call screen sis_shower_sex_options

label jenny_shower_hscene_dialog:
    if animcounter == 1:
        jen "Ahhhh!!!{p=1}{nw}"

    elif animcounter == 3:
        jen "Oh!!!{p=1}{nw}"
        player_name "Uhhh...{p=1}{nw}"
    return

label sis_shower_sex_cum_1:
    if anim_toggle:
        call expression game.dialog_select("sis_shower_sex_cum_1_pre_animation")
    else:
        call expression game.dialog_select("sis_shower_sex_cum_1_pre_manual")
    $ xray = False
    call expression game.dialog_select("sis_shower_sex_cum_1_after")
    $ playSound()
    jump expression game.dialog_select("hallway_dialogue")

label sis_shower_sex_cum_1_pre_animation:
    show jennysex 98_99_100_101
    pause 5
    hide jennysex
    return

label sis_shower_sex_cum_1_pre_manual:
    show jennysex 101 at Position(xpos=476)
    pause
    show jennysex 98 at Position(xpos=511)
    pause
    show jennysex 99 at Position(xpos=518)
    pause
    show jennysex 100 at Position(xpos=497)
    pause
    show jennysex 101 at Position(xpos=476)
    pause
    hide jennysex
    return

label sis_shower_sex_cum_1_after:
    show jenny 130 zorder 1 at Position(xpos=443)
    show player 351 zorder 2 at Position(xpos=260)
    jen "[str_warn]What the {b}FUCK{/b}??" with hpunch
    jen "[str_warn]Were you about to cum {b}INSIDE{/b} me!?"
    show jenny 131
    show player 351b
    player_name "No..."
    show jenny 130
    show player 351
    jen "What's wrong with you?!"
    jen "You know I can get {b}PREGNANT{/b}, right??! YOU IDIOT!"
    show jenny 131
    show player 351b
    player_name "I..."
    player_name "I'm sorry!!"
    show jenny 130
    show player 351
    jen "Yeah right! We're done here! {b}GET OUT{/b}!!" with hpunch
    hide jenny
    hide player
    with dissolve
    return

label sis_shower_sex_cum_2:
    if anim_toggle:
        call expression game.dialog_select("sis_shower_sex_cum_2_animation")
    else:
        call expression game.dialog_select("sis_shower_sex_cum_2_manual")
    call expression game.dialog_select("sis_shower_sex_cum_2_pre")
    $ xray = False
    call expression game.dialog_select("sis_shower_sex_cum_2_after")
    $ playSound()
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["09_unlocked"] = True
    jump expression game.dialog_select("hallway_dialogue")

label sis_shower_sex_cum_2_animation:
    show jennysex 98_99_100_101
    pause 5
    return

label sis_shower_sex_cum_2_manual:
    show jennysex 101 at Position(xpos=476)
    pause
    show jennysex 98 at Position(xpos=511)
    pause
    show jennysex 99 at Position(xpos=518)
    pause
    show jennysex 100 at Position(xpos=497)
    pause
    show jennysex 101 at Position(xpos=476)
    pause
    return

label sis_shower_sex_cum_2_pre:
    show white
    show jennysex 102 at Position(xpos=516)
    jen "{b}Aahhh!!!!{/b}" with hpunch
    hide white with dissolve
    pause
    show jennysex 103 at Position(xpos=511) with fastdissolve
    pause
    show jennysex 102_103 at Position(xpos = 516)
    pause 2.5
    show jennysex 103 at Position(xpos=511)
    return

label sis_shower_sex_cum_2_after:
    jen "{b}*Panting*{/b}"
    jen "Oh god..."
    hide jennysex
    show jenny 134 zorder 1 at Position(xpos=600)
    show player 353 zorder 2 at Position(xpos=260)
    with dissolve
    jen "What the FUCK?!"
    jen "I felt that!!!"
    show player 352
    jen "You just kept shooting cum deep inside!!"
    show jenny 133
    show player 349 at Position(xpos=254)
    player_name "It was a reflex!"
    player_name "I... I couldn't stop..."
    show jenny 134
    show player 348
    jen "Don't you get it, you idiot?!"
    jen "If you keep cumming inside me like that every time, I could get {b}PREGNANT{/b}!!"
    show jenny 133
    show player 349
    player_name "I..."
    player_name "I'm sorry!!"
    show jenny 134
    show player 353 at Position(xpos=260)
    jen "Sh-Shut up and {b}GET OUT{/b}!!" with hpunch
    hide jenny
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
