label pushups_minigame_win:
    scene gym with fade
    if M_roxxy.is_state(S_roxxy_do_pushups):
        show player 13 at left
        show bridget a_dressed_crossed f_normal at flip
        show bridget at Position (xpos=150)
        show dexter 42 at right
        with dissolve
    else:

        show player 109f at left
        with dissolve

    $ renpy.pause(1, hard = True)

    if M_roxxy.is_state(S_roxxy_do_pushups):
        dex "{b}*Gasp*{/b} Eugh..."
        show dexter 42b
        show bridget a_dressed_crossed f_normal_talk
        bri "You alright, {b}Dexter{/b}?"
        bri "You don't look so good..."
        show bridget a_dressed_crossed f_normal
        hide dexter
        show player 106
        dex "{b}*Gaahhh*{/b}!!!" with hpunch
        show bridget b_bend a_empty f_bend_angry_talk_down with dissolve
        dex "..."
        bri "... Dexter?"
        dex "..."
        show bridget b_dressed a_dressed_crossed f_normal_talk with dissolve
        bri "It looks like {b}[firstname]{/b} is the winner!"
        show bridget a_dressed_crossed f_normal
        show erik 4 at right with dissolve
        eri "That was awesome, dude!"
        eri "You destroyed him!"
        show erik 1
        dex "..."
        show player 108f
        player_name "... Is he alright?"
        show player 109f
        show erik 50
        eri "..."
        show bridget a_dressed_crossed f_normal_talk
        bri "Psh, he'll be fine."
        bri "You know, {b}[firstname]{/b} you should really come try out for the basketball team."
        show bridget a_dressed_crossed f_normal
        show erik 51
        show player 108f
        player_name "Really?"
        show player 109f
        show bridget a_dressed_crossed f_normal_talk
        bri "Yeah! I could use a player with your... stamina."
        show bridget a_dressed_crossed f_normal
        show player 10
        player_name "Y-yeah... Maybe."
        player_name "I'll think about it, {b}Coach{/b}..."
        show player 5
        show bridget a_dressed_crossed f_normal_talk
        bri "Well, you know where to find me."
        hide bridget with dissolve
        show erik 5
        eri "... That was weird."
        show erik 1
        show player 14
        player_name "Heh, yeah. {b}Coach Bridget{/b} actually said something nice to me..."
        show player 13
        show erik 4
        eri "Well, you did just slay an Ogre..."
        show erik 1
        show player 17
        player_name "Hahaha!"
        show player 14
        dex "{b}*Whimper*{/b}"
        show erik 50
        eri "..."
        show player 14
        player_name "C'mon, let's get out of these clothes."
        show player 13
        show erik 5
        eri "Right behind you."
        hide player
        hide erik
        with dissolve
        dex "..."
        $ M_roxxy.trigger(T_roxxy_beaten_dexter_pushups)
    else:

        dex "..."
        show player 108f
        player_name "{b}Dexter{/b}?"
        show player 109f
        dex "..."
        show player 109f
        player_name "{b}*Sigh*{/b} I dunno why you do this to yourself..."
        show player 108f
        dex "{b}*Whimper*{/b}"
        hide player with dissolve
        dex "..."
    $ game.timer.tick()
    $ player.go_to(L_map)
    $ game.main()

label pushups_minigame_lose:
    scene gym with fade
    if M_roxxy.is_state(S_roxxy_do_pushups):
        show player 25 at left
        show bridget a_dressed_crossed f_normal at flip
        show bridget at Position (xpos=150)
        show dexter 11 at right
        with dissolve
    else:

        show player 24 at left
        show dexter 12 at right
        with dissolve

    $ renpy.pause(1, hard = True)

    if M_roxxy.is_state(S_roxxy_do_pushups):
        player_name "{b}*Wheeze*{/b} Can't... breathe..."
        show dexter 12
        dex "Hahahaha!"
        show dexter 11
        show bridget a_dressed_crossed f_normal_talk at flip
        bri "It looks like {b}Dexter{/b} is the winner!"
        show bridget a_dressed_crossed f_normal
        show dexter 12
        dex "This little nerd never stood a chance..."
        show dexter 11
        show bridget a_dressed_crossed f_normal_talk
        bri "Keep things civil you two!"
        hide bridget with dissolve
        show dexter 12
        dex "Guess I don't have to worry about you and {b}Roxxy{/b}..."
        dex "... She doesn't date losers."
        show dexter 11
        show player 24
        player_name "..."
        show dexter 12
        dex "Hahahaha!"
        show dexter 11
        show player 25
        player_name "Whatever, {b}Dexter{/b}. You just got lucky is all..."
        show dexter 12
        dex "Hahahaha!"
        show dexter 11
        show player 15
        player_name "Grr... I'll get you next time."
        show player 16
        show dexter 28 with dissolve
        dex "Bring it on, loser!"
        dex "I'll beat you every time."
        hide dexter with dissolve
        show player 5
        player_name "( Crap! This is going to be all over school now. )"
        player_name "( I need to show everyone that I'm not afraid to stand up to {b}Dexter{/b}! )"
        player_name "( ... Otherwise {b}Roxxy{/b} will never take me seriously. )"
        hide player with dissolve
    else:

        dex "Yes!"
        dex "I win, loser!"
        show dexter 11
        show player 25
        player_name "Psh, who cares?"
        hide player with dissolve
        show dexter 12
        dex "Haha!"
        show dexter 15 with dissolve
        dex "... Wait... What?!"
        dex "Where are you going?!"
        dex "... Get back here and let me laugh in your face!"
        show dexter 14
        dex "..."
        dex "Grr..."
        hide dexter with dissolve
    $ game.timer.tick()
    $ player.go_to(L_map)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
