label aqua_dialogue_night:
    show player 10 with dissolve
    player_name "It's getting late..."
    player_name "I should find my way out of this underwater cavern before it gets too dark."
    hide player with dissolve
    return

label aqua_dialogue_aqua_found:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0) with dissolve
    pause
    show player 16 zorder 2 at Position(xpos=.125, ypos=1.0) with dissolve
    show aqua 1
    aqua "(!!!)" with hpunch
    aqua "You!!"
    show player 15
    show aqua 2
    player_name "That's right! Me!"
    player_name "You said I had to come get it. Well here I am!"
    player_name "Now give me back the shiny!"
    show player 16
    show aqua 1
    aqua "Hahahaha! You funny human!"
    aqua "You come long way. You mussst be good ssswimmer, like Aqua!"
    show player 24
    show aqua 2
    player_name "*cough* I guess..."
    show player 30
    player_name "What is this place anyways?"
    show player 16
    show aqua 1
    aqua "Thisss Aqua's nessst!"
    show player 12
    show aqua 2
    player_name "You live here?"
    show player 11
    show aqua 1
    aqua "Yesss."
    show player 10
    show aqua 2
    player_name "By yourself?"
    show player 11
    show aqua 4
    aqua "Yesss."
    show player 10
    show aqua 3
    player_name "Are there more of you?"
    show player 11
    show aqua 4
    aqua "More... of me?"
    show player 10
    show aqua 3
    player_name "You know, other nests with other... Umm, Aquas?"
    show player 11
    show aqua 4
    aqua "Oooh, no."
    show aqua 5
    aqua "No othersss. Just Aqua. Lassst of kind."
    show player 10
    show aqua 3
    player_name "Aww, well that's kinda sad. Sounds lonely."
    show player 5
    show aqua 1
    aqua "Not lonely. Have fishies!"
    show aqua 2b
    aqua "Fishies you steals!"
    show player 15
    show aqua 1b
    player_name "I told you that wasn't me! It's {b}CAPTAIN Terry{/b}."
    show player 16
    show aqua 4
    aqua "Caplan Terry? Hmm..."
    show aqua 5
    pause
    show aqua 4
    aqua "Maybe you tell truth..."
    show player 12
    show aqua 3
    player_name "I'm telling the truth, Aqua. I promise."
    show player 16
    show aqua 2b
    aqua "Well what Aqua do then? Fishies keep getting steals!"
    show aqua 4
    aqua "If fishies all gone, who Aqua talk to?"
    show player 11
    show aqua 5
    aqua "Aqua go crazy before find mate."
    show player 10
    show aqua 3
    player_name "Mate?"
    show player 11
    show aqua 4
    aqua "Yesss, Aqua waiting for Mate. Make baby Aquasss."
    show player 10
    show aqua 5
    player_name "Really? How long have you been waiting?"
    show aqua 4
    show player 11
    aqua "Aqua dunno. Looooong time. Nobody come. Nobody find Aqua."
    show player 10
    show aqua 5
    player_name "Hmm... Well I found you."
    show player 13
    show aqua 1
    aqua "Yesss! You find Aqua!"
    show aqua 2
    aqua "..."
    show aqua 9
    aqua "If you talk true and promissse not steals fishies. Me give you back Shiny."
    show player 14
    show aqua 8
    player_name "Yes! Thank you Aqua."
    show player 13
    show aqua 9
    aqua "You promissse?"
    show player 14
    show aqua 8
    player_name "I promise, I won't steal 'fishies.'"
    show player 13
    show aqua 9
    aqua "Ookaay."
    show aqua 10
    pause
    show aqua 2
    show player 471
    show popup_lure zorder 3 at truecenter with dissolve
    pause
    hide popup_lure with dissolve
    player_name "Phew... Thank you Aqua!"
    show player 470
    show aqua 1
    aqua "Just remember not to steal Aqua's fishies..."
    hide player
    hide aqua
    with dissolve
    return

label aqua_sex:
    $ game.timer.tick()
    if M_aqua.is_state(S_aqua_mate):
        call expression game.dialog_select("aqua_sex_pre_first")

    call expression game.dialog_select("aqua_sex_pre")
    if M_aqua.is_state(S_aqua_mate):
        label aqua_sex_replay:
            call expression game.dialog_select("aqua_sex_after_first")

    call expression game.dialog_select("aqua_sex_after")
    jump expression game.dialog_select("aqua_sex_loop")

label aqua_sex_pre_first:
    scene location_lair_mount
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Aqua, I have some good news!"
    show player 1
    show aqua 1
    aqua "*Gasp* You learn to breathe underwater, like Aqua?!"
    show player 12
    show aqua 2
    player_name "What? ... No."
    show player 1
    show aqua 7
    aqua "Oh. Ookaay. What news then?"
    show player 2
    show aqua 6
    player_name "I convinced {b}Captain Terry{/b} to stop fishing!"
    show player 1
    show aqua 7
    aqua "You mean fishies safe!?"
    aqua "No more {b}Captain Terry{/b}!?"
    show player 17
    show aqua 6
    player_name "Hey, you said it right that time!"
    show player 1
    show aqua 7
    aqua "Huh?"
    show player 2
    show aqua 6
    player_name "You said '{b}Captain Terry{/b}' correctly that time."
    show player 1
    show aqua 7
    aqua "Yesss. Caplan Terry!"
    show player 90
    show aqua 6
    player_name "..."
    show aqua 6b
    aqua "..."

    show player 37
    player_name "... Just nevermind."
    show player 2
    player_name "Your fish should be safe now."
    show player 1
    show aqua 7
    aqua "Oh thank you! Thank you! Thank you!"
    show aqua 14
    aqua "You good human! Strong human!"
    show player 29
    show aqua 13
    player_name "You're welcome, Aqua..."
    show player 1
    show aqua 11
    aqua "..."
    show aqua 12
    aqua "Is... human ready to mate with Aqua?"
    show player 21
    show aqua 13
    player_name "R-right now?"
    show player 297
    show aqua 14
    aqua "Yesss. Aqua wait long enough. Mate take her ssstrongly in water!"
    show player 10
    show aqua 13
    player_name "In the water?"
    show player 11
    show aqua 14
    aqua "Yesss. Come!"
    return

label aqua_sex_pre:
    scene location_lair_cutscene
    with fade
    show text "Aqua's touch was soft and gentle as she took my hand and started towards the luminescent pool." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I struggled to keep pace, fumbling with my clothes." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "But she didn't seem to notice, her excitement palpable as she lead her mate into the water." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    return

label aqua_sex_after_first:
    scene location_lair_water with fade
    show aswim 1 at left
    show pswim 1 at right
    pause
    show aswim 2
    aqua "Ooh, mate has good body."
    show aswim 1
    show pswim 2
    player_name "Thanks Aqua..."
    show aswim 3
    show pswim 1
    pause
    show aswim 2
    aqua "Your eel isss sleeping."
    show aswim 1
    show pswim 2
    player_name "Huh?"
    show aswim 3
    pause
    show pswim 3
    pause
    show pswim 2
    player_name "Oh. Yeah..."
    show aswim 2
    show pswim 1
    aqua "Does mate like Aqua's body?"
    show aswim 1
    show pswim 2
    player_name "Yes... Umm, 'mate' likes Aqua's body very much."
    show aswim 2
    show pswim 1
    aqua "Good. Aqua's body belong to you now."
    aqua "Mate's eel can play inssside Aqua whenever it wants."
    show aswim 3
    pause
    show aswim 2
    aqua "It's warm inssside Aqua..."
    show aswim 3
    pause
    show aswim 2
    aqua "... and soft..."
    show aswim 3
    pause
    show aswim 2
    aqua "... and wet."
    show pswim 3
    pause
    show aswim 3
    show pswim 4
    pause
    show aswim 4
    show pswim 5
    pause
    show pswim 9
    pause
    show aswim 2
    show pswim 6
    aqua "Ooh, eel likes this, yes?!"
    show aswim 3
    show pswim 7
    player_name "Y-yes..."
    show aswim 4
    aqua "Mmm, good. Aqua wantsss it."
    show aswim 3
    show pswim 8
    player_name "..."
    show aswim 4
    aqua "Aqua wantsss it now!"
    hide pswim
    show aswim 5 with dissolve
    pause
    show aswim 6 at right with dissolve
    player_name "*Gulp*"
    aqua "Aaah, yessss. Come eel, you play inssside Aqua."
    aqua "Give Aqua ssstrong babies..."
    player_name "Oh wow!"
    aqua "Mmm..."
    return

label aqua_sex_after:
    scene location_lair_watersex
    show aquas 1 at Position(xalign = 1.0, yalign = 1.0)
    aqua "{b}Aqua{/b} needs it inssside her!"
    aqua "Hurry my mate!"
    player_name "..."
    show aquas 2
    aqua "Hissss."
    aqua "Your eel sssooo big!"
    aqua "Take me ssstrong!"
    $ M_aqua.set("sex speed", .175)
    show expression AnimatedImage("aquas", [3,4,5,6,7], M_aqua) as aquas
    with fade
    aqua "Ooohh!."
    pause
    aqua "So ssstrong!"
    pause
    aqua "and deep!"
    $ M_aqua.set("sex speed", .125)
    aqua "Aaahh!"
    pause
    aqua "Mmm, my mate."
    aqua "Faster!"
    $ M_aqua.set("sex speed", .075)
    pause
    return

label aqua_sex_loop:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("aquas", [3,4,5,6,7], M_aqua) as aquas
                $ animated = True
            pause 5
            call expression game.dialog_select("aqua_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "aquas {}".format(pose_list[pose_counter]) as aquas
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("aqua_hscene_dialog")
        $ animcounter += 1
    call screen aqua_sex_options

label aqua_hscene_dialog:
    if animcounter == 1:
        aqua "Ahhhh!!!{p=1}{nw}"

    elif animcounter == 3:
        aqua "Take me!!!{p=1}{nw}"
        player_name "Uhhh...{p=1}{nw}"
    return

label aqua_sex_cum:
    call expression game.dialog_select("aqua_sex_cum_pre")
    if not store._in_replay == None or M_aqua.is_state(S_aqua_mate):
        call expression game.dialog_select("aqua_sex_cum_first")

    $ renpy.end_replay()
    $ persistent.cookie_jar["Aqua"]["unlocked"] = True
    $ persistent.cookie_jar["Aqua"]["gallery"]["01_unlocked"] = True
    $ M_aqua.trigger(T_aqua_mated)
    hide player
    hide aqua
    with dissolve
    $ game.main()

label aqua_sex_cum_pre:
    player_name "This is unbelievable!"
    player_name "{b}Aqua{/b}, I'm gonna..."
    aqua "Yesss... YESSS MY MATE!"
    aqua "Give {b}Aqua{/b} your ssseeeeeeds!"
    aqua "HISSSSS!!!"
    show aquas 8 with flash
    player_name "UHHH!!"
    aqua "AAAAHHH!!!!"
    pause
    show aquas 9
    player_name "Wow!"
    player_name "That was incredible!"
    aqua "Yesss..."
    aqua "... {b}Aqua{/b} can feel strong babies swimming inssside her!"
    pause
    scene black with fade
    return

label aqua_sex_cum_first:
    scene location_lair_mount
    show aqua 11 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "So you enjoyed that?"
    show player 1
    show aqua 12
    aqua "Yesss. Aqua enjoy much! Ssstill feel tingle dancing in legs!"
    show player 2
    show aqua 11
    player_name "You were incredible! I've never felt anything like that before."
    show player 1
    show aqua 14
    aqua "Yesss, this Aqua's first time too."
    show aqua 12
    aqua "... But Aqua wants more."
    show aqua 14
    aqua "Mate comes back, give Aqua more ssseed. Yes?"
    show player 2
    show aqua 13
    player_name "Absolutely, I'll come back really soon!"
    show player 1
    show aqua 14
    aqua "Mate promissse?"
    show player 2
    show aqua 13
    player_name "Oh, I promise!"
    show player 1
    show aqua 12
    aqua "Good. Aqua want much more!"
    show aqua 14
    aqua "Come back sssoon, Human."
    show aqua 11
    aqua "Aqua wait here until tingle ssstop dancing..."
    return

label aqua_dialogue_pre:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0) with dissolve
    show player 36 zorder 2 at Position(xpos=.125, ypos=1.0) with dissolve
    player_name "Hi, Aqua!"
    show player 1
    show aqua 1
    aqua "Yess..."
    show player 2
    show aqua 2
    player_name "I wanted to speak with you."
    show player 1
    show aqua 4
    aqua "What doesss human boy want?"
    return

label aqua_dialogue_the_others:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 10 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Aqua, what happened to the rest of your kind?"
    show player 11
    show aqua 4
    aqua "Hmm, Aqua not sssure. They just gone one day. Aqua lassst one."
    show aqua 5
    show player 10
    player_name "Aww, I'm sorry Aqua."
    show player 11
    show aqua 1
    aqua "You asssk more quessstions?"
    show aqua 2
    return

label aqua_dialogue_how_are_you:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Aqua, how are you?"
    show player 1
    show aqua 4
    aqua "How am I?"
    show player 2
    show aqua 3
    player_name "Yes, how are you feeling?"
    show player 1
    show aqua 5
    aqua "Hmm, Aqua okay. Lonely with so few fishies..."
    show aqua 4
    aqua "... but likes that human boy come visssit."
    show player 2
    show aqua 3
    player_name "I like talking with you too Aqua."
    show player 1
    show aqua 1
    aqua "Yesss, like talking."
    aqua "You asssk more quessstions?"
    show aqua 2
    return

label aqua_dialogue_mating_pre:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 10 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Aqua, what kind of mate are you looking for?"
    show player 11
    show aqua 4
    aqua "Man. Ssstrong man. Make Aqua ssstrong babies."
    show aqua 1
    aqua "you know man like this?"
    show player 34
    show aqua 3
    player_name "Hmm."
    return

label aqua_dialogue_mating_stat_fail:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 29 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "[chr_warn]How about me?"
    show player 3
    show aqua 4
    aqua "[chr_warn]You ssstrong man?"
    show player 29
    show aqua 3
    player_name "[chr_warn]Yes?"
    show player 3
    show aqua 5
    aqua "..."
    aqua "Hmm..."
    pause
    show aqua 4
    aqua "[chr_warn]Aqua thinks... No. Bad idea."
    show player 24
    show aqua 3
    player_name "[chr_warn]Bummer..."
    return

label aqua_dialogue_mating_stat_pass:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Maybe I could help?"
    show player 1
    show aqua 7
    aqua "You?"
    show player 2
    show aqua 6
    player_name "Well I mean, I did swim all the way down here to find you."
    show player 1
    show aqua 7
    aqua "You did."
    show player 2
    show aqua 6
    player_name "... And I fought a very mean squid along the way."
    show player 1
    show aqua 7 with hpunch
    aqua "You fight Inky?!"
    show player 2
    show aqua 6
    player_name "Inky? Yes. I fight Inky."
    show aqua 7
    aqua "Oooh, Inky ssstrong!"
    show aqua 12
    pause
    show aqua 11
    aqua "Maybe you do give Aqua ssstrong babies."
    show player 14
    show aqua 13
    player_name "Really?!"
    show player 1
    show aqua 14
    aqua "Yesss. But no mate yet. First you prove strength."
    show player 10
    show aqua 13
    player_name "Prove my strength? How am I supposed to do that?"
    show player 1
    show aqua 7
    aqua "You sssay Caplan Terry steals fishies, yesss?"
    show player 12
    show aqua 6
    player_name "{b}CAPTAIN Terry{/b}. Yes, he's the guy who's been fishing off the dock."
    show player 11
    show aqua 7
    aqua "Hmm, you go make Caplan Terry ssstop."
    show aqua 11
    aqua "You do this and then you mate with Aqua."
    show player 10
    show aqua 13
    player_name "Well I suppose I can give it a shot."
    show player 11
    show aqua 14
    aqua "Good. You go then. Sssave fishies!"
    return

label aqua_dialogue_mating_hint:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 12 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "What do I need to do again, Aqua? To prove my strength?"
    show player 11
    show aqua 7
    aqua "You sssave fishies from Caplan Terry!"
    show player 10
    show aqua 6
    player_name "Oh, right. {b}CAPTAIN Terry{/b}."
    show player 11
    show aqua 7
    aqua "That's what Aqua say! Caplan Terry!"
    show player 12
    show aqua 6
    player_name "CAPT- Nevermind. I guess I should go try and talk to him."
    show player 5
    show aqua 7
    aqua "Yesss. You go, sssave fishies!"
    return

label aqua_dialogue_mate:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 21 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "I thought maybe you would like to... Get in the water again?"
    show player 26
    show aqua 3
    aqua "..."
    show aqua 1
    aqua "Oh! You want make babies?"
    show player 21
    show aqua 12
    player_name "I, err... Sure?"
    show player 26
    show aqua 11
    aqua "Hahaha! Funny Human. You Aqua's mate now."
    show aqua 14
    aqua "Aqua always ready for more ssseeds! Mate take her ssstrongly in water whenever he wants."
    return

label aqua_dialogue_nothing:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 36 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Nothing, I was just saying hi!"
    show player 1
    show aqua 4
    aqua "Human boy isss... Funny..."
    show aqua 1
    aqua "...I like human boy..."
    show player 21
    show aqua 2
    player_name "I err... Like you too!"
    show player 13
    aqua "..."
    show player 29
    player_name "Anwyay, I should get going."
    show player 3
    show aqua 1
    aqua "You come back, see Aqua sssoon."
    show player 17
    show aqua 2
    player_name "You bet!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
