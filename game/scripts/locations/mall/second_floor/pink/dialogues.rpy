label pink_jenny_buy_bad_monster_callback:
    scene expression player.location.background_closeup with None
    show player 286b with dissolve
    player_name "( This thing is scary! )"
    player_name "( I hope {b}[jen_name]{/b} likes it... )"

    hide player with dissolve
    return

label pink_jenny_buy_bad_monster:
    scene expression player.location.background_closeup with None
    show player 13 with dissolve
    player_name "( Alright, I'm looking for a toy called {b}Bad Monster{/b} for {b}[jen_name]{/b}. )"
    player_name "( It's gotta be here somewhere. )"
    hide player with dissolve
    return

label pink_jenny_buy_vibrator:
    scene expression player.location.background_blur with None
    show player 288c at left
    show jenny b_casual f_upset a_dressed_hips_toy1
    with dissolve
    player_name "I think this is the right one?"
    show player 288b
    show jenny f_upset_talk
    jen "Ugh, it's not that hard to figure out dummy... Everything is labeled."
    show jenny f_upset
    show player 288d
    "*Click*"
    "*BZZZZZZ*{p=1}{nw}"
    show player 288g
    show jenny f_angry
    player_name "!!!" with hpunch
    show player 288e
    player_name "Whoa!"
    player_name "This thing is crazy!"
    show jenny f_upset_talk a_dressed_hips_toy1b
    show player 11
    with fastdissolve
    jen "Give me that!"
    jen "You're hopeless."
    show jenny f_upset
    show player 10
    player_name "What are you doing with all this stuff {b}[jen_name]{/b}?!"
    show player 5
    show jenny f_upset_talk
    jen "None of your business, loser."
    show jenny f_upset
    show player 12
    player_name "I'm going to find out eventually, you know?"
    show player 5
    show jenny f_upset_talk
    jen "Whatever."
    show ivy zorder 0
    show jenny f_normal_talk at flip
    show jenny zorder 1 at Position (xpos=600)
    with dissolve
    jen "I'll take these."
    show jenny f_normal a_dressed_side with dissolve
    show ivy f_normal_talk zorder 2
    ivy "Oh, those {b}UltraVibes{/b} are great!"
    ivy "It's amazing how powerful they are..."
    show ivy f_normal
    show jenny f_normal_talk
    jen "Uh huh, could you just ring me up, please?"
    show ivy f_shy
    ivy "..."
    show ivy f_shy_talk a_dressed_buttplug with dissolve
    ivy "You ever used one of these before?"
    show ivy f_shy
    show jenny f_sad_talk
    jen "No, why?"
    show jenny f_sad
    show ivy f_shy_talk
    ivy "You shoud really start with something smaller, sweetie..."
    show ivy f_shy a_dressed_front with dissolve
    show jenny f_upset_talk a_dressed_crossed with dissolve
    jen "Nah, it's fine... I've got lube."
    show jenny f_upset a_money with dissolve
    show player 11
    pause
    show jenny f_grin_talk a_dressed_hips
    show ivy a_dressed_money
    with dissolve
    jen "Besides, it's for him."
    show jenny f_grin
    show player 22
    show ivy a_dressed_front
    player_name "!!!" with hpunch
    show ivy f_normal_talk
    ivy "Oh, I didn't realize-"
    show ivy f_normal
    show player 23
    player_name "It's not for me!"
    show player 22
    show jenny f_laugh
    jen "Hahahahaaah!"
    show jenny f_grin
    show player 10
    player_name "Not funny."
    show player 90
    show jenny f_grin_talk
    jen "C'mon loser, let's go home."
    hide jenny with dissolve
    pause
    show player 29 with dissolve
    player_name "Seriously, that's not-"
    show player 3
    show ivy f_laugh
    ivy "Hehe, you'll get no judgement from me, cutie."
    show ivy f_normal
    show player 24 with dissolve
    player_name "{b}*Sigh*{/b}"
    hide player
    hide ivy
    with dissolve
    return

label pink_jenny_shop_for_toys:
    scene expression player.location.background_blur with None
    show player 12 at left
    show jenny b_casual f_normal
    with dissolve
    player_name "There you are."
    show player 90
    jen "..."
    show player 12
    player_name "You just took off on me."
    show player 90
    show jenny f_upset_talk
    jen "I can't stand that stupid bitch!"
    show jenny f_upset
    show player 10
    player_name "She seemed nice to me..."
    show player 5
    show jenny f_upset_talk
    jen "Yeah right, rubbing all her success in my face..."
    jen "She's always been jealous of me."
    show jenny f_upset
    if M_jenny.get("dominance") <= 0:
        show player 10
        player_name "I don't think she-"
        show player 11
        show jenny f_angry_talk
        jen "Fuck her!"
        show jenny f_upset_talk
        jen "I don't want even want to talk about it."
    else:
        show player 12
        player_name "Yeah, I bet you're right."
        player_name "A broke, college drop out, living at home with no boyfriend."
        player_name "Who wouldn't be jealous?"
        show player 90
        show jenny f_angry_talk
        jen "Fuck you!"
        show jenny f_angry
        jen "Grr!"
        show jenny f_upset_talk
        jen "Just-"
    jen "Just help me find these toys I need."
    show jenny f_upset
    show player 10
    player_name "Okay, what am I looking for?"
    show player 5
    show jenny f_upset_talk
    jen "I need the {b}UltraVibe 2000{/b} annnnnd..."
    show jenny f_grin_talk a_dressed_hips_toy1 with dissolve
    jen "This."
    show jenny f_grin
    show player 22b with dissolve
    player_name "!!!"
    show player 23 with dissolve
    player_name "Is that a buttplug?"
    show player 22
    show jenny f_upset_talk
    jen "Yeah, so?"
    show jenny f_upset
    show player 10
    player_name "It's huge!"
    player_name "You aren't really gonna..."
    show player 22
    show jenny f_eyeroll
    jen "They want to see big."
    show jenny f_upset
    show player 4 with dissolve
    pause
    show player 30 with dissolve
    player_name "Who's they?!"
    show player 5
    show jenny f_upset_talk a_dressed_hips with dissolve
    jen "Tsk, nevermind!"
    jen "Quit being such a perv and go find that {b}UltraVibe 2000{/b}!"
    show jenny f_upset
    show player 12c with dissolve
    player_name "M-me?!"
    show player 12 with dissolve
    player_name "You're the one who's buying-"
    show player 11
    show jenny f_angry
    pause
    show player 24
    player_name "Fine."
    hide player with dissolve
    pause
    show jenny f_grin_down a_dressed_hips_toy1 with dissolve
    pause
    show jenny f_sad
    jen "( Maybe I should get more lube while I'm here... )"
    hide jenny with dissolve
    return

label pink_diane_get_outfit_package:
    scene expression "backgrounds/location_pink_blur.jpg"
    show player 3
    player_name "( Hmm? )"
    player_name "( I don't see anybody minding the store... )"
    show player 4 with dissolve
    pause
    show player 10 with dissolve
    player_name "... Is anyone here?"
    show player 5
    pause
    show player 10
    player_name "H-hello?!"
    show player 5
    ivy "Just a moment!!"
    pause
    show player 4 with dissolve
    player_name "( Huh, I wonder what she's doing back there? )"
    show player 5 with dissolve
    ivy "Be right with you!!"
    show player 10
    player_name "Okay!"
    show player 9f at left with dissolve
    pause
    pause
    show player 34 with dissolve
    player_name "( Hmm, what could {b}Diane{/b} have ordered from a place like this?! )"
    pause
    show ivy b_naked a_naked_sheet_cover f_normal_talk with dissolve
    ivy "Sorry about that."
    show ivy f_normal
    show player 23
    player_name "!!!"
    show ivy f_normal_talk
    ivy "I was just finishing up with a customer."
    show ivy f_normal
    show player 11
    player_name "..."
    pause
    player_name "..."
    show ivy f_shy_talk
    ivy "Can I help you with something, cutie?"
    show ivy f_shy
    show player 37 with dissolve
    player_name "Oh sheesh, I'm sorry!"
    show player 3 with dissolve
    show ivy f_laugh
    ivy "Hehe, it's alright."
    show ivy f_normal
    show player 29
    player_name "I umm..."
    show player 26 with dissolve
    pause
    show player 24
    player_name "I'm supposed to... Uhh..."
    pause
    show player 4 with dissolve
    pause
    show player 17 with dissolve
    player_name "... Pick up a package!"
    show player 13
    show ivy f_normal_talk
    ivy "What's the name?"
    show ivy f_normal
    show player 10
    player_name "{b}Diane{/b}?"
    show player 13
    show ivy f_sexy_talk
    ivy "Hmm, you don't look like a {b}Diane{/b}..."
    show ivy f_sexy
    show player 10
    player_name "I don't?"
    show player 12
    player_name "I mean, no, she's my-"
    show player 5
    show ivy f_laugh
    ivy "Hehe, I'm just joking with you."
    show ivy f_normal_talk
    ivy "One second, I'll get your package."
    hide ivy with dissolve
    pause
    show player 26
    player_name "( Wow, she is really beautiful... )"
    player_name "( ... And she's practically naked! )"
    player_name "( Does she have someone else back there with her? )"
    show ivy b_naked a_naked_sheet_cover f_shy_talk with dissolve
    show player 13
    ivy "I can't seem to find-"
    show ivy f_laugh
    ivy "Oh, silly me! Here it is!"
    show ivy b_naked_pickup a_empty f_empty with dissolve
    show player 426
    pause
    ivy "Here you go."
    show ivy b_naked a_naked_sheet_box f_normal with dissolve
    show player 22
    player_name "!!!" with hpunch
    show ivy f_surprised_down
    with dissolve
    ivy "Oopsie!"
    show player 171b
    show ivy a_naked_sheet_cover f_shy
    with dissolve
    show player 171
    pause
    show ivy f_shy_talk
    ivy "Sorry about that."
    show ivy f_shy
    show player 170c
    player_name "N-no problem."
    show player 169c
    show ivy f_sexy_talk
    ivy "Aww, you're so adorable when you blush!"
    show ivy f_sexy
    show player 170c
    player_name "... I am?"
    show player 169c
    ivy "Mmhmm."
    show player 171
    vero "What's taking so long out here?!"
    show ivy b_hug_vero a_empty f_hug_vero_normal_back
    show vero f_sexy_talk b_empty a_empty
    with dissolve
    vero "I'm not done with you yet!"
    hide vero
    show ivy b_hug_vero_kiss f_hug_vero_laugh
    with dissolve
    ivy "Oh, haah..."
    show ivy f_hug_vero_normal_talk_back
    ivy "I was just helping this young man with order."
    show ivy f_hug_vero_normal_back
    show player 170b
    player_name "{b}Veronica{/b}?!"
    show player 169b
    show ivy b_hug_vero
    show vero f_sexy_talk b_empty a_empty
    with dissolve
    vero "{b}[firstname]{/b}?"
    show vero f_sexy
    show player 170b
    player_name "What are you doing here?"
    show player 169b
    show vero f_sexy_talk
    vero "Oh, just blowing off a little steam."
    vero "I never would have expected to see you in a place like this..."
    show vero f_sexy
    show player 170b
    player_name "I wasn't..."
    player_name "I mean, I'm just here to pick something up..."
    player_name "... F-for a friend!"
    show player 169b
    show vero f_sexy_talk
    vero "Oh, reeeeeally?"
    show vero f_sexy
    show ivy f_hug_vero_normal_talk_back
    ivy "Someone named {b}Diane{/b} apparently."
    show ivy f_hug_vero_normal
    show vero f_normal_talk
    vero "{b}*Gasp*{/b} That package is for {b}Diane{/b}?!"
    show ivy a_naked_sheet_cover b_naked f_normal
    show vero f_normal_talk b_disheveled a_disheveled_hip at Position (xpos=250)
    with dissolve
    vero "Oh, lemme see! Lemme see!!!"
    show vero f_normal
    show player 170b
    player_name "I dunno, she told me not to open it..."
    show player 169b
    show vero f_normal_talk
    vero "Well, did she tell you that I couldn't open it?"
    show vero f_normal
    show player 171c
    player_name "N-no..."
    show player 170b
    player_name "She didn't say anything about you."
    player_name "... But I don't think-"
    show player 169b
    show vero f_normal_talk
    vero "Oh, c'mon!"
    vero "Just a quick peek!"
    show vero f_normal a_disheveled_box with dissolve
    show player 10
    with dissolve
    player_name "O-okay, I guess..."
    show player 5
    show vero f_sexy_down a_disheveled_box_open with dissolve
    pause
    vero "..."
    show vero f_sexy_talk_down
    vero "Whoa."
    vero "I wasn't expecting this..."
    show vero f_sexy_talk a_disheveled_hip
    show player 169b
    with dissolve
    vero "What in the heck is she up to over there?!"
    show vero f_sexy
    show player 170b
    player_name "I uhh..."
    show player 170c
    player_name "Heh, I couldn't say."
    show player 169c
    show vero f_sexy_talk
    vero "Well, she's definitely doing something kinky and I'm terribly jealous!"
    vero "Tell her, she had better call me!"
    vero "I want all the juicy details!"
    show vero f_sexy
    show player 170c
    player_name "Y-yeah, okay."
    show player 169c
    show ivy f_sexy_talk
    ivy "C'mon, gorgeous..."
    ivy "Let's get back to it, shall we?"
    show ivy f_sexy with None
    show player 171 with None
    show vero f_sexy_talk at flip
    show vero at Position (xpos=800)
    with dissolve
    vero "Mmm yes, we definitely shall!"
    show vero at unflip
    show vero at Position (xpos=250)
    with dissolve
    vero "See ya, {b}[firstname]{/b}!"
    hide vero
    hide ivy
    with dissolve
    pause
    show player 170
    player_name "... B-bye."
    show player 169
    pause
    player_name "( Phew, {b}Veronica{/b} is really pushy when it comes to {b}Diane{/b}. )"
    player_name "( Speaking of {b}Diane{/b}, {b}I should get this package back to her right away!{/b} )"
    hide player with dissolve
    return

label pink_first_visit:
    scene pink
    show player 23 with dissolve
    player_name "( Wow! )"
    show player 21
    player_name "( That's... There's a lot of weird stuff in here. )"
    show player 29
    player_name "( Hmm... Maybe these will come in handy one day... )"
    hide player 29 with dissolve
    return

label pink_mia_helen_outfit_request:
    scene pink
    show player 12 with dissolve
    player_name "I should look through that clothing rack..."
    player_name "...They must have a selection of lingerie."
    hide player with dissolve
    return

label pink_mia_angelicas_whip:
    scene pink with fade
    show player 12 with dissolve
    player_name "There has to be something in here that looks like {b}a whip{/b}..."
    hide player with dissolve
    return

label ivy_paizuri:
    call expression game.dialog_select("ivy_paizuri_pre")
    if M_ivy.get("first visit"):
        call expression game.dialog_select("ivy_paizuri_first")
        $ M_ivy.set("first visit", False)
    else:

        call expression game.dialog_select("ivy_paizuri_repeat")
    $ M_ivy.set("sex speed", 0.8)
    $ animcounter = 0
    $ anim_toggle = True
    $ animated = False
    $ xray_needed = False
    jump expression game.dialog_select("ivy_paizuri_loop")

label ivy_paizuri_pre:
    scene pink
    show player 174 at left
    show ivy 5 at right
    with dissolve
    player_name "I'll try the basic."
    ivy "Testing the waters, huh?"
    show player 29
    player_name "I uhh..."
    show ivy 3
    ivy "Heh, I'm just teasing!"
    show ivy 12
    ivy "Follow me."
    scene massage_room_closeup with fade
    show player 1 at left
    show ivy 2 at right
    with dissolve
    return

label ivy_paizuri_first:
    show player 43
    player_name "{b}*Whistle*{/b} Cool room."
    show player 1
    show ivy 3 with dissolve
    ivy "{b}*Chuckle*{/b} It'll be even cooler once we get started."
    show ivy 2
    ivy "Now, strip down and lay on the bed. You can put your clothes on the table."
    ivy "I'll give you a few minutes to prepare."
    ivy "Have to make sure nobody can interrupt us..."
    hide ivy with dissolve
    show player 18
    player_name "( Phew! That was way less awkward than I expected it to be! )"
    scene massage_room_closeup with fade
    show player 175 at left
    with dissolve
    player_name "( I didn't expect it to be so straightforward, though... )"
    show player 57
    player_name "( Am I really ready for this yet? )"
    player_name "( ...I can't turn back now. )"
    show player 175
    player_name "( Might as well enjoy it. )"
    hide player with dissolve
    scene massage_room
    show playersex 19 zorder 1
    show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
    show ivy 18 zorder 3 at Position (xpos=870,ypos=655) with dissolve
    with dissolve
    ivy "{b}*Chuckle*{/b} Why are you still wearing that?"
    ivy "We don't need towels for this kind of massage."
    player_name "Oh. Sorry..."
    show ivy 14 at Position (xpos=780,ypos=655) with dissolve
    pause 0.5
    hide expression "characters/ivy/char_ivy_13.png"
    show ivy 15 at Position (xpos=804,ypos=655) with vpunch
    ivy "There! That's much better, isn't it?"
    player_name "Yeah, it is."
    show ivy 16 at Position (xpos=870,ypos=658)
    pause 1
    show ivy 17 at Position (xpos=870,ypos=655)
    pause 1
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "How on Earth do you hide that thing?"
    ivy "In any case: name's Ivy."
    ivy "Now, my turn to prepare..."
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    ivy "Like what you see?"
    player_name "Yeah..."
    ivy "{b}*Giggle*{/b} Well, your friend sure looks like he does."
    ivy "I guess I'll have to take care of that..."
    hide ivy
    show ivysex 1 zorder 2
    with dissolve
    show ivysex 7 with dissolve
    ivy "Before we start, I should let you know something."
    ivy "This room is soundproof..."
    player_name "( Oh? )"
    ivy "...so you don't have to hold anything back."
    ivy "Now, juuussst relax..."
    return

label ivy_paizuri_repeat:
    show player 1
    ivy "You know the drill. I'll be back in a minute."
    hide ivy with dissolve
    pause 0.5
    hide player with dissolve
    scene massage_room with fade
    show playersex 19 zorder 1
    with dissolve
    pause 2
    show ivy 18 at Position (xpos=870,ypos=655) with dissolve
    ivy "Okay! Good to go!"
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    ivy "Let's do this!"
    hide ivy
    show ivysex 1 zorder 2
    with dissolve
    show ivysex 6
    return

label ivy_paizuri_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("ivysex", [6,5], M_ivy) as ivysex zorder 2
                $ animated = True
            pause 4
        else:

            $ pose_counter = 0
            $ pose_list = [6,5]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "ivysex {}".format(pose_list[pose_counter]) as ivysex zorder 2
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        call expression game.dialog_select("ivy_paizuri_hscene_dialog")
        $ animcounter += 1
        if animcounter < 3:
            call screen ivy_paizuri_options
    $ renpy.end_replay()
    $ persistent.cookie_jar["Ivy"]["unlocked"] = True
    $ persistent.cookie_jar["Ivy"]["gallery"]["01_unlocked"] = True
    $ game.main()

label ivy_paizuri_hscene_dialog:
    if animcounter == 1:
        if not anim_toggle:
            show ivysex 5
        ivy "I bet it doesn't feel this good when you use your hand..."
        if not anim_toggle:
            show ivysex 6
        player_name "( Not even fucking close! )"
        if not anim_toggle:
            show ivysex 5
        player_name "Faster..."
        if not anim_toggle:
            show ivysex 6

    elif animcounter == 2:
        if not anim_toggle:
            show ivysex 5
        ivy "Are you-{b}*huff*{/b}-getting close?"
        if not anim_toggle:
            show ivysex 6
        player_name "Yeah..."
        ivy "Then let's kick it into high gear!"
        player_name "Aahh-gonna..."

    elif animcounter == 3:
        if not anim_toggle:
            show ivysex 5
        player_name "...Gonna...CUM!"
        show ivysex 7
        ivy "Do it!"
        show white zorder 4 with dissolve
        hide white with dissolve
        show expression "characters/player/char_player_sex_25.png" as playersex_cum zorder 3
        with Dissolve(0.3)
        show expression "characters/player/char_player_sex_26.png" as playersex_cum zorder 3
        with Dissolve(0.3)
        show expression "characters/player/char_player_sex_27.png" as playersex_cum zorder 3
        with Dissolve(0.3)
        show expression "characters/player/char_player_sex_28.png" as playersex_cum zorder 3
        with Dissolve(0.3)
        ivy "Wow.... there's so much..."
        ivy "Did you enjoy yourself?"
        player_name "Yeah... you're great at this."
        ivy "{b}*Giggle*{/b} I know."
        ivy "Such a mess though..."
        ivy "Let's get ourselves cleaned up."
    return

label ivy_blowjob:
    call expression game.dialog_select("ivy_blowjob_pre")
    if M_ivy.get("first visit"):
        call expression game.dialog_select("ivy_blowjob_first")
        $ M_ivy.set("first visit", False)
    else:

        call expression game.dialog_select("ivy_blowjob_repeat")
    $ M_ivy.set("sex speed", 0.8)
    $ animcounter = 0
    $ anim_toggle = True
    $ animated = False
    $ xray_needed = False
    jump expression game.dialog_select("ivy_blowjob_loop")

label ivy_blowjob_pre:
    scene pink
    show player 174 at left
    show ivy 5 at right
    with dissolve
    player_name "Yeah. I'd like the classic, please."
    ivy "Oh? Been eying my lips?"
    show player 29
    player_name "I ehh..."
    show ivy 3
    ivy "Ease up, I'm just messing!"
    show ivy 12
    ivy "Follow me."
    scene massage_room_closeup with fade
    show player 1 at left
    show ivy 3 at right
    with dissolve
    ivy "Okay, I'll just make sure nobody can interrupt us."
    return

label ivy_blowjob_first:
    show player 43
    player_name "{b}*Whistle*{/b} Cool room."
    show player 1
    ivy "{b}*Chuckle*{/b} It'll be even cooler once we get started."
    show ivy 2
    ivy "Now, strip down and lay on the bed. You can put your clothes on the table."
    ivy "I'll give you a few minutes to prepare."
    ivy "Have to make sure nobody can interrupt us..."
    hide ivy with dissolve
    show player 18
    player_name "( Phew, that was way less awkward than I expected it to be! )"
    show player 175 with dissolve
    player_name "( I didn't expect it to be so straightforward, though... )"
    show player 57
    player_name "( Am I really ready for this yet? )"
    player_name "( ...Nah, I can't turn back now. )"
    show player 175
    player_name "( Might as well enjoy it. )"
    hide player with dissolve
    scene massage_room
    show playersex 19 zorder 1
    show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
    with dissolve
    show ivy 18 zorder 3 at Position (xpos=870,ypos=655) with dissolve
    ivy "{b}*Chuckle*{/b} Why are you still wearing that?"
    ivy "We don't need towels for this kind of massage."
    player_name "Oh, sorry..."
    show ivy 14 at Position (xpos=780,ypos=655) with dissolve
    pause 0.5
    hide expression "characters/ivy/char_ivy_13.png"
    show ivy 15 at Position (xpos=804,ypos=655) with vpunch
    ivy "There, that's much better, isn't it?"
    player_name "Yeah, it is."
    show ivy 16 at Position (xpos=870,ypos=658)
    pause 1
    show ivy 17 at Position (xpos=870,ypos=655)
    pause 1
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "How on Earth do you hide that thing?"
    ivy "In any case: name's Ivy."
    ivy "Now, my turn to prepare..."
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    ivy "Like what you see?"
    player_name "Yeah..."
    ivy "{b}*Giggle*{/b} Well, your friend sure looks like he does."
    ivy "I guess I'll have to take care of that..."
    hide ivy
    show ivysex 1 zorder 2
    with dissolve
    show ivysex 2 with dissolve
    ivy "Before we start, I should let you know something."
    ivy "This room is soundproof..."
    player_name "( Oh? )"
    ivy "...so you don't have to hold anything back."
    ivy "Oh, and let me know when you're close, alright?"
    player_name "Sure thing."
    ivy "Now, just lay back and relax..."
    return

label ivy_blowjob_repeat:
    ivy "You know the drill, I'll be back in a minute."
    hide ivy with dissolve
    pause 0.5
    hide player
    scene massage_room
    show playersex 19 zorder 1
    with dissolve
    pause 2
    show ivy 18 at Position (xpos=870,ypos=655) with dissolve
    ivy "Okay! Good to go!"
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    ivy "Let's do this!"
    hide ivy
    show ivysex 1 zorder 2
    with dissolve
    show ivysex 2
    return

label ivy_blowjob_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("ivysex", [4,3], M_ivy) as ivysex zorder 2
                $ animated = True
            pause 4
        else:

            $ pose_counter = 0
            $ pose_list = [4,3]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "ivysex {}".format(pose_list[pose_counter]) as ivysex zorder 2
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        call expression game.dialog_select("ivy_blowjob_hscene_dialog")
        $ animcounter += 1
        if animcounter < 3:
            call screen ivy_blowjob_options
    $ renpy.end_replay()
    $ persistent.cookie_jar["Ivy"]["unlocked"] = True
    $ persistent.cookie_jar["Ivy"]["gallery"]["02_unlocked"] = True
    $ game.main()

label ivy_blowjob_hscene_dialog:
    if animcounter == 1:
        if not anim_toggle:
            show ivysex 3
        player_name "( Man, if her mouth feels this good, actual sex must be insane... )"
        if not anim_toggle:
            show ivysex 4
        player_name "Aaah... Faster..."

    elif animcounter == 2:
        if not anim_toggle:
            show ivysex 3
        player_name "( Crap, I'm getting close... )"
        if not anim_toggle:
            show ivysex 4
        player_name "Faster."

    elif animcounter == 3:
        if not anim_toggle:
            show ivysex 3 zorder 2
        player_name "( Gotta warn her... )"
        if not anim_toggle:
            show ivysex 4
        player_name "I'm about to-"
        show ivysex 3
        player_name "SHIT!"
        show white zorder 4 with dissolve
        hide white
        show ivysex 24
        with dissolve
        show ivysex 25 with dissolve
        player_name "I uhh..."
        show ivysex 26
        ivy "{b}*Cough*{/b} {b}*Cough*{/b}"
        ivy "What happened to the whole \"let me know\" part?"
        player_name "Uhh, sorry about that..."
        ivy "You know, usually I charge extra for swallowing."
        player_name "I..."
        player_name "( Crap, maybe I shouldn't have done that. )"
        show ivysex 1
        ivy "{b}*Giggle*{/b} Oh man, you should see the look on your face!"
        ivy "Don't worry about it, you were good practice! It's on the house."
        player_name "*nervous laugh* Thanks."
        player_name "Again, sorry about that..."
        ivy "Really, it's fine... You know, my usual customers don't usually pack this much {b}heat{/b}."
        player_name "Oh, uh, thanks, I guess."
        ivy "Now, let's get ourselves cleaned up."
    return

label ivy_reverse_cowgirl:
    call expression game.dialog_select("ivy_reverse_cowgirl_pre")
    if M_ivy.get("first visit"):
        call expression game.dialog_select("ivy_reverse_cowgirl_first")
        $ M_ivy.set("first visit", False)
    call expression game.dialog_select("ivy_reverse_cowgirl_after")
    $ M_ivy.set("sex speed", 0.8)
    $ animcounter = 0
    $ anim_toggle = True
    $ animated = False
    $ ivy_cum_inside = False
    $ xray_needed = True
    jump expression game.dialog_select("ivy_reverse_cowgirl_loop")

label ivy_reverse_cowgirl_pre:
    scene pink
    show player 174 at left
    show ivy 5 at right
    with dissolve
    player_name "Yeah, I'll try the premium, please."
    ivy "Ohoh, quite bold for your age!"
    show player 29
    player_name "I uhh..."
    show ivy 3
    ivy "{b}*Giggle*{/b} I like an eager man!"
    show ivy 2
    ivy "Follow me."
    scene massage_room_closeup with fade
    show ivy 2 at right
    show player 43 at left
    with dissolve
    ivy "Alright, I'll just make sure nobody can interrupt us."
    return

label ivy_reverse_cowgirl_first:
    player_name "{b}*Whistle*{/b} Cool room."
    show player 1
    show ivy 3 at right
    ivy "{b}*Chuckle*{/b} It'll be even cooler once we get started."
    show ivy 2
    ivy "Now, strip down and lay on the bed. You can put your clothes on the table."
    ivy "I'll give you a few minutes to prepare."
    ivy "Have to make sure nobody can interrupt us."
    hide ivy 2 with dissolve
    show player 18
    player_name "( Phew, that was way less awkward than I expected it to be! )"
    show player 175 with dissolve
    player_name "( I didn't expect it to be so straightforward though... )"
    show player 57
    player_name "( Am I really ready for this yet? )"
    player_name "( ...Nah, I can't turn back now. )"
    show player 175
    player_name "( Might as well enjoy it. )"
    hide player with dissolve
    scene massage_room
    show playersex 19 zorder 1
    show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
    with dissolve
    show ivy 18 zorder 3 at Position (xpos=870,ypos=655) with dissolve
    ivy "{b}*Chuckle*{/b} Why are you still wearing that?"
    ivy "We don't need towels for this kind of massage."
    player_name "Oh. sorry..."
    show ivy 14 at Position (xpos=780,ypos=655) with dissolve
    pause 0.5
    hide expression "characters/ivy/char_ivy_13.png"
    show ivy 15 at Position (xpos=804,ypos=655) with vpunch
    ivy "There! That's much better, isn't it?"
    player_name "Yeah, it is."
    show ivy 16 at Position (xpos=870,ypos=658)
    pause 1
    show ivy 17 at Position (xpos=870,ypos=655)
    pause 1
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "How on Earth do you hide that thing?"
    ivy "In any case: Name's Ivy."
    ivy "Now, my turn to prepare..."
    return

label ivy_reverse_cowgirl_after:
    hide player
    scene massage_room
    show playersex 19 zorder 1
    show ivy 7 zorder 2 at Position (xpos=800,ypos=656)
    with dissolve
    ivy "We're gonna need a condom for this one."
    show ivy 6 at Position (xpos=799,ypos=655)
    player_name "Aww, man..."
    show ivy 7 at Position (xpos=800,ypos=656)
    ivy "Oh don't fret! you won't even notice that it's there. Trust me."
    show ivy 9 at Position (xpos=730,ypos=674) with dissolve
    pause
    show ivy 10 at Position (xpos=730,ypos=697) with dissolve
    pause
    show expression "characters/player/char_player_sex_29.png" zorder 2
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "And for the final part..."
    hide player
    scene massage_room
    show playersex 19 zorder 1
    show expression "characters/player/char_player_sex_29.png" zorder 2
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    pause
    hide ivy
    show ivysex 15 zorder 2
    with dissolve
    pause
    show ivysex 16 with dissolve
    pause
    show ivysex 17 with dissolve
    ivy "{b}*Giggle*{/b} I wonder if it'll fit..."
    ivy "You ready to feel heaven?"
    player_name "{b}*Gulp*{/b} Yeah."
    ivy "Here we go..."
    show playersex 22
    show ivysex 18 with dissolve
    show ivysex 19 with dissolve
    player_name "Haaah-"
    show ivysex 20
    ivy "You okay back there?"
    player_name "Yeah, go ahead..."
    return

label ivy_reverse_cowgirl_loop:
    show screen sex_xray_anim_buttons
    pause
    hide screen sex_xray_anim_buttons
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("ivysex", [18,19], M_ivy) as ivysex zorder 2
                $ animated = True
            pause 4
        else:

            $ pose_counter = 0
            $ pose_list = [18,19]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "ivysex {}".format(pose_list[pose_counter]) as ivysex zorder 2
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        call expression game.dialog_select("ivy_reverse_cowgirl_hscene_dialog")
        $ animcounter += 1
        if animcounter < 3:
            call screen ivy_rcowgirl_options
    $ renpy.end_replay()
    $ persistent.cookie_jar["Ivy"]["unlocked"] = True
    $ persistent.cookie_jar["Ivy"]["gallery"]["03_unlocked"] = True
    $ game.main()

label ivy_reverse_cowgirl_hscene_dialog:
    if animcounter == 1:
        if not anim_toggle:
            show ivysex 19
        player_name "( Holy shit, this feels amazing! )"
        if not anim_toggle:
            show ivysex 18
        player_name "You can go faster... I think I can handle it..."
        if not anim_toggle:
            show ivysex 19
        ivy "Okay. You asked for it!"

    elif animcounter == 2:
        if not anim_toggle:
            show ivysex 19
        player_name "( Gotta hold out for just a while longer... )"
        if not anim_toggle:
            show ivysex 18
        ivy "Haah-I gotta say..."
        if not anim_toggle:
            show ivysex 19
        ivy "...you may be just a teenager..."
        if not anim_toggle:
            show ivysex 18
        ivy "...but you-aah-put some of my clients to shame!"
        if not anim_toggle:
            show ivysex 19
        player_name "( That's one way to boost my ego. )"
        if not anim_toggle:
            show ivysex 18
        player_name "( I wonder how she'd react to... )"
        if not anim_toggle:
            show ivysex 19

    elif animcounter == 3:
        if not anim_toggle:
            show ivysex 19
        player_name "( Crap, I'm at my limit! )"
        if not anim_toggle:
            show ivysex 18
        player_name "( She's way too good at this! )"
        if not anim_toggle:
            show ivysex 19
        player_name "I'm gonna cum!"
        if not anim_toggle:
            show ivysex 18
        ivy "Haah- go ahead!"

        call screen ivy_rcowgirl_cum_options

        if ivy_cum_inside:
            show playersex 22
            show ivysex 19 zorder 2
        else:
            hide expression "characters/player/char_player_sex_29.png"
            show playersex 19
            show ivysex 22 zorder 2
            show expression "characters/player/char_player_sex_25.png" as playersex_cum zorder 3
        show white zorder 3 with hpunch
        hide white
        with dissolve
        ivy "Haaa..."
        if not ivy_cum_inside:
            show expression "characters/player/char_player_sex_51.png" as playersex_cum zorder 3
        ivy "Haah... You lasted a pretty long time there... for a teenager."

        hide expression "characters/player/char_player_sex_29.png"
        if ivy_cum_inside:
            show playersex 19
            show ivysex 22 zorder 2
            show expression "characters/player/char_player_sex_35.png" zorder 3
        player_name "Thanks. You're amazing..."
        hide expression "characters/player/char_player_sex_35.png"
        show playersex 19
        show ivysex 15 zorder 2
        if not ivy_cum_inside:
            show expression "characters/player/char_player_sex_52.png" as playersex_cum zorder 3
        else:
            show expression "characters/player/char_player_sex_31.png" zorder 3
        pause
        ivy "Let's get ourselves cleaned up..."
    return

label ivy_slap_ass:
    show playersex 23
    show ivysex 20
    pause 0.2
    show ivysex 21
    show playersex 24 with vpunch
    pause 0.2
    ivy "{b}*Giggle*{/b} Getting even bolder?"
    ivy "Faster it is, then!"
    show playersex 22
    show ivysex 20
    $ animated = False
    jump expression game.dialog_select("ivy_reverse_cowgirl_loop")

label ivy_cowgirl:
    call expression game.dialog_select("ivy_cowgirl_pre")
    if M_ivy.get("first visit"):
        call expression game.dialog_select("ivy_cowgirl_first")
        $ M_ivy.set("first visit", False)
    call expression game.dialog_select("ivy_cowgirl_after")
    $ M_ivy.set("sex speed", 0.8)
    $ animcounter = 0
    $ anim_toggle = True
    $ animated = False
    $ ivy_cum_inside = False
    $ xray_needed = True
    jump expression game.dialog_select("ivy_cowgirl_loop")

label ivy_cowgirl_pre:
    scene pink
    show ivy 5 at right
    show player 174 at left
    with dissolve
    player_name "Yeah, I'll have the ultimate, please."
    ivy "{b}*Giggle*{/b} You want to see it all, don't you?"
    show player 29
    player_name "I uhh..."
    show ivy 3
    ivy "I like myself an eager man."
    show ivy 2
    ivy "Follow me."
    scene massage_room_closeup with fade
    show ivy 2 at right
    show player 43 at left
    with dissolve
    ivy "Alright, I'll just make sure nobody can interrupt us."
    return

label ivy_cowgirl_first:
    player_name "{b}*Whistle*{/b} Cool room."
    show player 1
    show ivy 3
    ivy "{b}*Chuckle*{/b} It'll be even cooler once we get started."
    show ivy 2
    ivy "Now, strip down and lay on the bed. You can put your clothes on the table."
    ivy "I'll give you a few minutes to prepare."
    hide ivy 2
    scene blank with dissolve
    scene massage_room_closeup
    show player 175 at left
    with dissolve
    player_name "( Phew, that was way less awkward than I expected it to be! )"
    player_name "( I didn't expect this to be so straightforward, though. )"
    player_name "( Maybe I'm not really ready for something like this yet... )"
    player_name "( ...Nah. I can't turn back now. )"
    player_name "( I might as well enjoy it. )"
    scene massage_room
    hide player
    show playersex 19
    show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
    show ivy 18 zorder 3 at Position (xpos=870,ypos=655)
    with dissolve
    ivy "{b}*Chuckle*{/b} Why are you still wearing that?"
    ivy "We don't need towels for this kind of massage."
    player_name "Oh, sorry..."
    show ivy 14 at Position (xpos=780,ypos=655) with dissolve
    pause 0.5
    hide expression "characters/ivy/char_ivy_13.png"
    show ivy 15 at Position (xpos=804,ypos=655) with vpunch
    ivy "There! That's much better, isn't it?"
    player_name "Yeah, it is."
    show ivy 16 at Position (xpos=870,ypos=658)
    pause 1
    show ivy 17 at Position (xpos=870,ypos=655)
    pause 1
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "How on Earth do you hide that thing?"
    ivy "In any case: name's Ivy."
    ivy "Now, my turn to prepare..."
    return

label ivy_cowgirl_after:
    scene massage_room
    hide player
    show playersex 19
    show ivy 7 zorder 2 at Position (xpos=800,ypos=656)
    with dissolve
    ivy "We're gonna need a condom for this one."
    show ivy 6 at Position (xpos=799,ypos=655)
    player_name "Aww man..."
    show ivy 7 at Position (xpos=800,ypos=656)
    ivy "Oh don't fret, you won't even notice that it's there. Trust me."
    show ivy 9 at Position (xpos=730,ypos=674) with dissolve
    pause
    show ivy 10 at Position (xpos=730,ypos=697) with dissolve
    pause
    show expression "characters/player/char_player_sex_29.png" zorder 2
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "And for the final part..."
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    pause
    hide ivy
    show ivysex 8 zorder 2
    with dissolve
    pause
    show ivysex 9 with dissolve
    pause
    show playersex 20
    show ivysex 10 with dissolve
    ivy "{b}*Giggle*{/b} I wonder if it'll fit..."
    ivy "You ready to feel heaven?"
    player_name "{b}*gulp*{/b} Yeah."
    ivy "Here we go..."
    show playersex 21
    show ivysex 11
    player_name "Haaah-"
    show playersex 20
    show ivysex 10
    ivy "You okay?"
    player_name "Yeah, go ahead..."
    return

label ivy_cowgirl_loop:
    show screen sex_xray_anim_buttons
    pause
    hide screen sex_xray_anim_buttons
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("playersex", [20,21], M_ivy) as playersex
                show expression AnimatedImage("ivysex", [10,11], M_ivy) as ivysex zorder 2
                $ animated = True
            pause 4
        else:

            $ pose_counter = 0
            $ pose_list = [10,11]
            $ player_pose_list = [20,21]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "playersex {}".format(player_pose_list[pose_counter]) as playersex
                show expression "ivysex {}".format(pose_list[pose_counter]) as ivysex zorder 2
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        call expression game.dialog_select("ivy_cowgirl_hscene_dialog")
        $ animcounter += 1
        if animcounter < 3:
            call screen ivy_cowgirl_options
    $ renpy.end_replay()
    $ persistent.cookie_jar["Ivy"]["unlocked"] = True
    $ persistent.cookie_jar["Ivy"]["gallery"]["04_unlocked"] = True
    $ game.main()

label ivy_cowgirl_hscene_dialog:
    if animcounter == 1:
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        player_name "( Holy shit, this feels amazing! )"
        if not anim_toggle:
            show playersex 21
            show ivysex 11
        player_name "You can go faster... I think I can handle it..."
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        ivy "Okay. You asked for it!"

    elif animcounter == 2:
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        player_name "( Gotta hold out for just a while longer... )"
        if not anim_toggle:
            show playersex 21
            show ivysex 11
        ivy "Haah-I gotta say..."
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        ivy "...you may be just a teenager..."
        if not anim_toggle:
            show playersex 21
            show ivysex 11
        ivy "...but you-aah-put some of my clients to shame!"
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        player_name "( That's one way to boost my ego. )"
        if not anim_toggle:
            show playersex 21
            show ivysex 11
        player_name "( I wonder how she'd react to... )"

    elif animcounter == 3:
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        player_name "( Crap, I'm at my limit! )"
        if not anim_toggle:
            show playersex 21
            show ivysex 11
        player_name "( She's way too good at this! )"
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        player_name "I'm gonna cum!"
        if not anim_toggle:
            show playersex 21
            show ivysex 11
        ivy "Haah- go ahead!"

        call screen ivy_cowgirl_cum_options

        if ivy_cum_inside:
            show playersex 21
            show ivysex 11 zorder 2
        else:
            hide expression "characters/player/char_player_sex_29.png"
            show playersex 20
            show ivysex 13 zorder 2
            show expression "characters/player/char_player_sex_32.png" as playersex_cum zorder 3
        show white zorder 3 with hpunch
        hide white
        with dissolve
        ivy "Haaa..."
        if not ivy_cum_inside:
            show expression "characters/player/char_player_sex_33.png" as playersex_cum zorder 3
        ivy "Haah... You lasted a pretty long time there... for a teenager."
        if not ivy_cum_inside:
            show ivysex 14 zorder 2
            show expression "characters/player/char_player_sex_34.png" as playersex_cum zorder 3
        player_name "Thanks... You're amazing..."
        hide playersex_cum
        hide expression "characters/player/char_player_sex_29.png"
        show playersex 19
        show ivysex 9 zorder 3
        if ivy_cum_inside:
            show expression "characters/player/char_player_sex_30.png" zorder 2
            with dissolve
        pause
        hide expression "characters/player/char_player_sex_30.png"
        show ivysex 8 zorder 3
        if ivy_cum_inside:
            show expression "characters/player/char_player_sex_31.png" zorder 2
            with dissolve
        pause
        ivy "Let's get ourselves cleaned up..."
    return

label ivy_no_money:
    show player 13 at left
    show ivy 4 at right
    with dissolve
    player_name "( Darn, I can't afford this. )"
    player_name "On second thought, maybe some other time."
    $ game.main()

label pink_just_browsing:
    scene expression player.location.background_blur with None
    show player 4
    player_name "( Hmm, I don't have any reason to buy this at the moment... )"
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
