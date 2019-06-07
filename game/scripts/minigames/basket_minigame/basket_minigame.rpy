label basketball_minigame_prepare_but_with_a_background_this_time:
    scene basketball_b
label basketball_minigame_prepare:
    if M_roxxy.get("basketball unlocked"):
        if game.cheat_mode:
            menu:
                "Skip Minigame (Cheat)":
                    jump basketball_success
                "Play minigame":

                    call screen basketball_minigame
        else:

            call screen basketball_minigame
    else:

        scene expression L_basketball_court.background_blur
        show player 16 at left
        show dexter 4 at right
        dex "What do you think you're doing?!"
        dex "This court is for men, not skinny little losers!"
        show dexter 6
        dex "Get lost!"
        player_name "( Grr, he's such an asshole! )"
        player_name "( One day, he's gonna get what's coming to him... )"
    $ player.go_to(L_basketball_court)
    $ game.main()

label basketball_success:
    if M_roxxy.is_state(S_roxxy_basketball_challenge) and (game.timer.is_afternoon() or not M_roxxy.is_set("done basketball")):
        scene expression "backgrounds/location_basketball_cutscene02.jpg"
        with fade
        show text "I was on fire!\nPractically running circles around {b}Dexter{/b}..." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "Swiping the ball and sinking threes before he could even take a step." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        hide text
        with dissolve
        scene expression "backgrounds/location_basketball_cutscene03.jpg"
        with fade
        show text "... And then it happened." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "I faked left, then faked right, and then blew past him!\n{b}Dexter{/b} grunted, stumbling over his own feet and crashing to the ground." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "I've no idea how he managed to lose his pants though..." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        hide text
        with dissolve
        scene basketball_b
        show chad 5f at Position (xpos=500)
        show tyrone 2f at Position (xpos=300)
        show dexter 43b at right
        show kevin 35f at left
        with dissolve
        tyrone "Oh, shit son!"
        tyrone "{b}[firstname]{/b} just juked that fool so hard his pants came off!"
        show tyrone 1f
        show chad 6f
        chad "That was doooope, yo!"
        show chad 5f
        show kevin 36f with dissolve
        kev "... What the hell is that?"
        show chad 12f
        chad "Huh?"
        show tyrone 9f
        kev "What is that?!"
        tyrone "... Is that his dick?!"
        show tyrone 10f with dissolve
        show dexter 43
        kev "I dunno bro, I can't tell..."
        show kevin 36bf
        kev "... Did anybody bring a magnifying glass?!"
        show chad 13f
        chad "Hahahaha! It looks like a belly button!"
        show tyrone 3f
        tyrone "Hahaha, yeah man! With two tiny little nuts hanging off it!"
        show tyrone 1f
        show chad 1f
        show dexter 43c
        dex "Shut up, you guys!"
        show dexter 43b with hpunch
        show kevin 32f with dissolve
        kev "Hahaha, {b}Dexter{/b} has a tiny penis!"
        bri "Alright, that's enough!"
        hide kevin
        hide chad
        hide tyrone
        with dissolve
        tyrone "He's smaller than tiny, Dawg..."
        tyrone "That's a straight up Micropenis!"
        show bridget a_dressed_crossed f_normal_talk at flip
        show bridget at Position (xpos=100)
        with dissolve
        bri "What's all the commotion abo-"
        show bridget f_laughing_hold a_dressed_laugh with dissolve
        bri "!!!"
        show dexter 44 with dissolve
        dex "!!!"
        bri "..."
        show dexter 44c
        dex "Stop laughing!"
        dex "Don't you know who I am?!"
        dex "Nobody laughs at me!"
        show dexter 45
        show player 649 at left with dissolve
        player_name "Hey, {b}Dexter{/b}..."
        player_name "Your ball, bitch!"
        show player 664
        show dexter 45b
        with dissolve
        pause
        show player 91
        show bridget f_laugh a_dressed_hips with dissolve
        bri "PFFFT, HAHAHAHAHA!"
        hide bridget
        show dexter 45c
        dex "GRR, FUCK ALL OF YOU!" with hpunch
        show player 11
        dex "{b}[firstname]{/b}, you are fucking dead!"
        dex "YOU HEAR ME?!" with hpunch
        dex "DEAD!"
        show dexter 46 with dissolve
        pause 1
        hide dexter with dissolve
        pause
        show kevin 32 at Position (xpos=700)
        show erik 1 at right
        with dissolve
        kev "Yo, {b}Dexter{/b}! You forgot your pants, bro!!"
        kev "Hahaha!"
        eri "..."
        kev "{b}[firstname]{/b} that was the funniest thing I've ever seen!"
        show kevin 23
        show player 14
        player_name "Heh, yeah?"
        show player 13
        show kevin 9b
        kev "For real, Bro!"
        show kevin 23
        show erik 5
        eri "... It was so tiny."
        show erik 1
        show kevin 32
        kev "Hahaha, yeah it was!"
        kev "Oh my god! This is gonna spread like wildfire!"
        show kevin 23
        show player 12
        player_name "... Yeah."
        player_name "{b}*Sigh*{/b} There's no way to avoid it now."
        show player 5
        show erik 5
        eri "What do you mean?"
        show erik 52
        show player 10
        player_name "{b}Dexter's{/b} gonna want blood after this..."
        player_name "I'll have to fight him next time for sure."
        show player 5
        show erik 5
        eri "Yeah, I think you're right about that."
        show erik 52
        show kevin 24
        kev "{b}You better hit the gym and prepare yourself.{/b}"
        show kevin 23
        show player 12
        player_name "That's a good idea."
        show player 5
        show kevin 24
        kev "You let me know if you need some help, yeah?"
        show kevin 23
        show player 14
        player_name "Thanks, {b}Kevin{/b}."
        show player 13
        show kevin 24
        kev "No problem, bro."
        hide kevin with dissolve
        show erik 5
        eri "... C'mon, lets hit the showers."
        show erik 3
        eri "I think I need to change my pants after all that!"
        show erik 2 with dissolve
        show player 17
        player_name "Haha, right behind you."
        hide player
        hide erik
        with dissolve
        show expression "boxes/popup_basketball_minigame.png" at truecenter with dissolve
        pause
        hide expression "boxes/popup_basketball_minigame.png" with dissolve
        $ M_roxxy.trigger(T_roxxy_humiliated_dexter)
        $ M_roxxy.set("done basketball", True)
    else:

        scene basketball_b
        show player 10
        player_name "That wasn't too bad... I should probably train some more to get even better at this."
    $ game.timer.tick()
    $ player.go_to(L_basketball_court)
    $ game.main()

label basketball_fail:
    if M_roxxy.is_state(S_roxxy_basketball_challenge) and (game.timer.is_afternoon() or not M_roxxy.is_set("done basketball")):
        if M_roxxy.get("done basketball"):
            scene basketball_b
            show bridget a_dressed_crossed f_normal at flip
            show bridget at Position (xpos=100)
            show player 24 at left
            show dexter 32 at right
            with dissolve
            dex "Yeah, that's right you little bitch!"
            dex "You can't hang with {b}Dexter{/b}!"
            dex "{b}Roxxy{/b} should be embarrassed, kissing a loser like you!"
            show dexter 31
            player_name "..."
            show dexter 32
            dex "Hahahahaha!"
            show dexter 31
            show bridget a_dressed_crossed f_normal_talk
            bri "Alright, that's enough."
            show dexter 29 with dissolve
            bri "{b}Dexter{/b} you were fouling left and right out there."
            show bridget a_dressed_crossed f_normal
            show player 11
            show dexter 30
            dex "What?! Not this again. I wasn't-"
            show dexter 29
            show bridget a_dressed_crossed f_angry_talk
            bri "That was clearly charging!"
            show dexter 2 with dissolve
            show bridget a_dressed_crossed f_normal_talk
            bri "{b}*Sigh*{/b} Do we have to discuss the rules again?!"
            show bridget a_dressed_crossed f_normal
            show dexter 8
            dex "... No."
            show dexter 2
            show bridget a_dressed_crossed f_normal_talk
            bri "I'm afraid I'll have to disqualify you and give the win to {b}[firstname]{/b}."
            show bridget a_dressed_crossed f_normal
            show dexter 8
            dex "That's bullshit!"
            show dexter 2
            show player 10
            player_name "... No."
            show player 12
            player_name "I don't want to win on a technicality."
            show player 90
            show dexter 8
            dex "A techni- Whaaa?"
            show dexter 2
            show bridget a_dressed_crossed f_normal_talk
            bri "You're sure, {b}[firstname]{/b}?"
            show bridget a_dressed_crossed f_normal
            show player 12
            player_name "I'm sure."
            show player 90
            show bridget a_dressed_crossed f_normal_talk
            bri "Very well."
            bri "I guess we'll just have to play another game tomorrow."
            show bridget a_dressed_crossed f_normal
            show dexter 30 with dissolve
            dex "Pssh, fine with me!"
            show dexter 32 with dissolve
            dex "I could beat this loser blind folded and with one hand tied behind my back..."
            show dexter 31
            show player 12
            player_name "Yeah, we'll see..."
            show player 90
            show bridget a_dressed_crossed f_normal_talk
            bri "We'll {b}meet here tomorrow afternoon{/b} for the rematch."
            show bridget a_dressed_crossed f_normal
            show dexter 32
            dex "Hah, see you then."
            show player 647
            show dexter 33
            with dissolve
            dex "Bitch."
            hide dexter with dissolve
            show player 648 with dissolve
            pause
            hide bridget
            show bridget a_dressed_crossed f_normal
            with dissolve
            player_name "..."
            show bridget a_dressed_crossed f_normal_talk
            bri "Practice, {b}[firstname]{/b}!"
            bri "He's not going to keep falling for my excuses..."
            show bridget a_dressed_crossed f_normal
            player_name "Hmm?"
            show bridget a_dressed_crossed f_normal_talk
            bri "I expect a better performance tomorrow."
            show bridget a_dressed_crossed f_normal
            show player 649
            player_name "Y-yes, ma'am."
            show player 648
            hide bridget with dissolve
            player_name "..."
            show player 649
            player_name "I should probably practice more."
            hide player with dissolve
        else:

            scene expression "backgrounds/location_basketball_cutscene01.jpg"
            with fade
            show text "There's a reason {b}Dexter{/b} was made Captain of the basketball team.\nHe overpowered me at every turn..." at Position (xpos= 512, ypos= 700) with dissolve
            pause
            show text "Defensively he was like a wall, I just couldn't get past him!\nHe was slow though and clumsy if I got a step on him." at Position (xpos= 512, ypos= 700) with dissolve
            pause
            show text "There were opportunities and with a little practice, I'm sure I can beat him!" at Position (xpos= 512, ypos= 700) with dissolve
            pause
            hide text
            with dissolve
            scene basketball_b
            show bridget a_dressed_crossed f_normal at flip
            show bridget at Position (xpos=100)
            show player 24 at left
            show dexter 3 at right
            with dissolve
            dex "Yeah, that's right you little bitch!"
            dex "You can't hang with {b}Dexter{/b}!"
            show dexter 6 with dissolve
            dex "{b}Roxxy{/b} should be embarrassed, kissing a loser like you!"
            show dexter 3 with dissolve
            dex "Hahahahaha!"
            player_name "..."
            show bridget a_dressed_crossed f_normal_talk
            show player 27
            bri "Alright, that's enough."
            show dexter 2
            bri "{b}Dexter{/b} you were fouling left and right out there."
            show bridget a_dressed_crossed f_normal
            show player 11
            show dexter 8
            dex "What?! No, I wasn't..."
            show dexter 2
            show bridget a_dressed_crossed f_angry_talk
            bri "Yes, you were! I counted no less than a dozen personal fouls and a couple were pretty flagrant."
            show bridget a_dressed_crossed f_normal_talk
            bri "I'm afraid I'll have to disqualify you and give the win to {b}[firstname]{/b}."
            show bridget a_dressed_crossed f_normal
            show dexter 6 with dissolve
            dex "That's not fair!"
            show dexter 2 with dissolve
            show player 12
            player_name "... No."
            player_name "I don't want to win on a technicality."
            show player 5
            show dexter 8
            dex "A techni- Whaaa?"
            show dexter 2
            show bridget a_dressed_crossed f_normal_talk
            bri "You're sure, {b}[firstname]{/b}?"
            show bridget a_dressed_crossed f_normal
            show player 10
            player_name "I'm sure."
            show player 5
            show bridget a_dressed_crossed f_normal_talk
            bri "Very well."
            bri "I guess we'll just have to play another game tomorrow."
            show bridget a_dressed_crossed f_normal
            show dexter 3
            dex "Pssh, fine with me!"
            dex "I could beat this loser blind folded and with one hand tied behind my back..."
            show dexter 1
            show player 12
            player_name "Yeah, we'll see..."
            show player 90
            show bridget a_dressed_crossed f_normal_talk
            bri "We'll {b}meet here tomorrow afternoon{/b} for the rematch."
            show bridget a_dressed_crossed f_normal
            show dexter 3
            dex "Hah, see you then."
            show player 647
            show dexter 33
            with dissolve
            dex "Bitch."
            hide dexter with dissolve
            show player 5 with dissolve
            player_name "..."
            hide bridget
            show bridget a_dressed_crossed f_normal_talk
            with dissolve
            bri "I suggest you practice, {b}[firstname]{/b}!"
            bri "He might not fall for that again..."
            show bridget a_dressed_crossed f_normal
            player_name "Hmm?"
            show bridget a_dressed_crossed f_normal_talk
            bri "I expect a better performance tomorrow."
            show bridget a_dressed_crossed f_normal
            show player 10
            player_name "Y-yes, ma'am."
            show player 5
            hide bridget with dissolve
            player_name "..."
            show player 109f
            eri "Uuhhhh..."
            show player 108f
            player_name "{b}*Sigh*{/b} I should get him to the locker room."
            player_name "... I hope he's got a change of pants here at school."
            hide player with dissolve
            show expression "boxes/popup_basketball_minigame.png"
            pause
            hide expression "boxes/popup_basketball_minigame.png"
            $ M_roxxy.set("done basketball", True)
    else:

        scene basketball_b
        show player 10
        player_name "Damn, I failed again... I should probably train some more to get better at this."
    $ game.timer.tick()
    $ player.go_to(L_basketball_court)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
