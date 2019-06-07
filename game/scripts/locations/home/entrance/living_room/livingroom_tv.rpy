label hide_home_tv:
    hide home_tv_channel_01
    hide home_tv_channel_02
    hide home_tv_channel_03
    hide home_tv_channel_04
    hide home_tv_channel_05
    hide home_tv_channel_06
    hide home_tv_channel_07
    hide home_tv_channel_08
    hide home_tv_channel_09
    hide home_tv_channel_10
    return

label cant_watch_porn_during_day:
    player_name "( I can't watch porn during the day! )"
    player_name "( {b}[deb_name]{/b} could catch me. )"
    player_name "( I am {b}NOT{/b} having that conversation {i}again{/i}... )"
    return

label home_livingroom_tv:
    if M_player.get("masturbated tv"):
        if M_jenny.get("had_couch_sex"):
            call expression game.dialog_select("home_livingroom_tv_masturbated_tv_sis")
        else:
            call expression game.dialog_select("home_livingroom_tv_masturbated_tv")
        jump expression game.dialog_select("home_livingroom_dialogue")
    $ tv_channel = 0
    jump expression game.dialog_select("tv_channel_responses")

label home_livingroom_tv_locked:
    scene expression game.timer.image("home_livingroom{}_b") with None
    show popup_tv_locked at truecenter with dissolve
    pause
    hide popup_tv_locked with dissolve
    $ game.main()

label home_livingroom_tv_masturbated_tv_sis:
    scene home_livingroom_night_b with None
    show player 11
    with dissolve
    player_name "( I'm not risking that again, tonight... )"
    player_name "( I should go to bed. )"
    hide player with dissolve
    hide home_livingroom_night_b
    return

label home_livingroom_tv_masturbated_tv:
    scene home_livingroom_night_b with None
    show player 11
    with dissolve
    player_name "( I think that's enough for one night. )"
    player_name "( I should go to bed. )"
    hide player with dissolve
    hide home_livingroom_night_b
    return

label tv_channel_responses:
    scene home_livingroom_tv
    $ pink_user = ""
    $ pink_pass = ""
    if tv_channel == -1:
        $ tv_channel = 7
    elif tv_channel == 8:
        $ tv_channel = 0
    if tv_channel in range(7) and tv_channel not in game.seen_tv_channels:
        $ renpy.call(game.dialog_select("tv_channel_channel_0{}_first_view".format(tv_channel+1)))
        $ game.seen_tv_channels.append(tv_channel)

    elif tv_channel == 7:
        if game.timer.is_day():
            call cant_watch_porn_during_day
            call hide_home_tv
            $ game.main()
        elif not M_jenny.finished_state(S_jenny_figure_out_password):
            call sis_pink_pass
            call hide_home_tv
            $ game.main()
        elif game.timer.is_evening():
            $ tv_pink_channel = 8
        elif M_jenny.finished_state(S_jenny_catch_her_jilling):
            $ tv_pink_channel = renpy.random.randint(7,8)
        else:
            $ tv_pink_channel = 7

        if tv_pink_channel in (7, 8) and not tv_channel_pink:
            call expression game.dialog_select("tv_channel_pink_intro")
            if tv_pink_channel == 7:
                show home_tv_channel_09 at Position(xpos=522, ypos=521)
            elif tv_pink_channel == 8:
                show home_tv_channel_10 at Position(xpos=522, ypos=521)
            if game.timer.is_evening():
                if M_jenny.get("force_couch_sex"):
                    $ rn = 50
                else:
                    $ rn = random.randint(1, 100)
                if rn <= 40:
                    call expression game.dialog_select("tv_channel_channel_08_finishes_himself")
                elif rn <= 80 and M_jenny.finished_state(S_jenny_catch_her_jilling):
                    call expression game.dialog_select("tv_channel_channel_08_jenny_interrupts")
                else:
                    call expression game.dialog_select("tv_channel_channel_08_mom_interrupts")
                $ M_player.set("masturbated tv", True)
                $ game.timer.tick()
                jump expression game.dialog_select("home_livingroom_dialogue")

        elif 8 not in game.seen_tv_channels:
            show home_tv_channel_08 at Position(xpos=522, ypos=522)
            call expression game.dialog_select("sis_pink_pass")
            $ tv_channel = 7
            $ game.seen_tv_channels.append(8)

    call hide_home_tv
    call screen home_livingroom_tv

label tv_channel_pink_intro:
    scene home_livingroom_tv
    show home_tv_channel_09 at Position(xpos=522, ypos=521) with dissolve
    player_name "( Oh, lesbians! )"
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show player b_couch_sit_watching f_couch_sit_watching_straight a_couch_boner_covered
    player_name "( Everyone's asleep... This is the perfect opportunity to rub one out! )"
    show player a_couch_boner_pull1 with dissolve
    pause
    show player a_couch_boner_pull2 with dissolve
    show player a_couch_boner with dissolve
    pause
    show player a_couch_boner_jerk with dissolve
    player_name "( Damn these chicks are hot! )"
    pause
    pause
    show player f_couch_sit_watching_jerking
    player_name "( I'm getting close! )"
    pause
    return

label tv_channel_sis_couch03_started:
    scene home_livingroom_couch01 with None
    show playersex 82 at Position(xpos=497)
    with dissolve
    player_name "Let's see what's on TV..."

    scene home_livingroom_tv
    show home_tv_channel_08 at Position(xpos = 522, ypos = 521)
    player_name "( Someone left it on the Pink Channel? )"
    player_name "The password was..."
    pause .4
    show text "{color=#ff4bdf}L6bv12R{/color}" as username at Position(xpos = 433, ypos = 341)
    pause .4
    show text "{color=#ff4bdf}12345{/color}" as password at Position(xpos = 423, ypos = 411)
    pause 1
    hide username
    hide password
    show home_tv_channel_10 at Position(xpos = 522, ypos = 521)
    player_name "Woah!"
    player_name "( I've never seen someone use their feet like {b}that{/b}. )"
    player_name "( Actually, that's kind of hot. )"
    return

label tv_channel_channel_01_first_view:
    show home_tv_channel_01 at Position(xpos=522, ypos=521)
    player_name "Hmm... Let's see what's on TV."
    return

label tv_channel_channel_02_first_view:
    show home_tv_channel_02 at Position(xpos=522, ypos=521)
    player_name "( Local news. Boring! )"
    return

label tv_channel_channel_03_first_view:
    show home_tv_channel_03 at Position(xpos=522, ypos=521)
    player_name "( That's the kind of sport I could get into. )"
    return

label tv_channel_channel_04_first_view:
    show home_tv_channel_04 at Position(xpos=522, ypos=521)
    player_name "( Hey, it's Mayor Rump! )"
    return

label tv_channel_channel_05_first_view:
    show home_tv_channel_05 at Position(xpos=522, ypos=521)
    player_name "..."
    player_name "( These nature channels are so strange... )"
    return

label tv_channel_channel_06_first_view:
    show home_tv_channel_06 at Position(xpos=522, ypos=521)
    player_name "( Who watches this stuff? )"
    return

label tv_channel_channel_07_first_view:
    show home_tv_channel_07 at Position(xpos=522, ypos=521)
    player_name "( This channel's a dud. )"
    return

label tv_channel_channel_08_mom_interrupts:
    scene home_livingroom_couch02
    show player b_couch_sit_watching f_couch_sit_watching_jerking a_couch_boner_jerk
    with fade
    deb "{b}[firstname]{/b}?"
    show player b_couch_sit f_couch_sit_down_surprised a_couch_boner_jerk1 with dissolve
    player_name "( Oh, crap! )"
    show player f_couch_sit_right_talk
    player_name "( {b}[deb_name]{/b} is coming! )"
    show debbie 126 at Position (xpos=917,ypos=694)
    show player 303 at left
    with dissolve
    deb "Is somebody out here?!"
    show debbie 127 at Position (xpos=872,ypos=540) with dissolve
    deb "Hello?!"
    deb "Oh, they left the tv-"
    show debbie 128 at Position (xpos=862,ypos=511) with dissolve
    deb "!!!"
    show debbie 132 at Position (xpos=680,ypos=768) with dissolve
    deb "Oh, my."
    pause
    deb "Who in the world was-"
    pause
    deb "Wow, they're really going at it..."
    pause
    deb "I shouldn't be watching this!"
    deb "{b}[firstname]{/b} or {b}[jen_name]{/b} could walk in here any second!"
    show debbie 133 at Position (xpos=812,ypos=767) with dissolve
    pause
    hide debbie with dissolve
    pause
    scene expression player.location.background_closeup with None
    show player f_worried_talk
    player_name "That was close!"
    player_name "I'd better just go to bed..."
    hide player with dissolve
    hide home_livingroom_couch01
    return

label tv_channel_channel_08_finishes_himself:
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show player b_couch_sit_watching f_couch_sit_watching_jerking a_couch_boner_jerk1
    player_name "HNNGGG!!!" with flash
    show player o_couch_boner_cum
    pause
    player_name "( Phew, that felt awesome! )"
    show player f_couch_sit_watching_straight
    pause
    player_name "( I guess, I'd better go and get cleaned up. )"
    hide player with dissolve
    return

label tv_channel_channel_08_jenny_interrupts:
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show player b_couch_sit_watching f_couch_sit_watching_jerking a_couch_boner_jerk
    show jenny b_couch_behind a_empty f_empty
    with fade
    jen "Surprise, perv!"
    show player f_couch_sit_down_surprised b_couch_sit a_couch_boner
    player_name "!!!" with hpunch
    show player f_couch_sit_right_talk a_couch_boner_covered_shirt with dissolve
    player_name "You scared me!"
    show player f_couch_sit_right
    if M_diane.finished_state(S_diane_couch_crashing):
        jen "Where's {b}Diane{/b}?"
        show player f_couch_sit_right_talk
        player_name "I dunno, she must be working late or something..."
        show player f_couch_sit_right
    show jenny b_couch_sit f_couch_sit_upset_talk a_couch_rest with dissolve
    jen "Who said you could use my {b}Pink Channel{/b} account?"
    show jenny f_couch_sit_upset
    show player f_couch_sit_right_talk
    player_name "I didn't think you would mind-"
    show player f_couch_sit_right
    show jenny f_couch_sit_upset_talk
    jen "Ugh, lesbians..."
    show jenny f_couch_sit_grin_talk
    jen "Don't you think that's kinda boring?"
    show jenny f_couch_sit_grin
    show player f_couch_sit_right_talk
    player_name "Not really."
    show player f_couch_sit_right
    show jenny f_couch_sit_grin_talk
    jen "It just seems kinda pointless when there's no dick involved..."
    show jenny f_couch_sit_grin
    player_name "..."
    show jenny f_couch_sit_surprised
    jen "Oh my god, were you jerking it?!"
    show jenny f_couch_sit_sexy
    show player f_couch_sit_right_talk
    player_name "N-no..."
    show player f_couch_sit_right
    show jenny f_couch_sit_sexy_talk
    jen "Yes, you were."
    show jenny f_couch_sit_laugh
    jen "Look at your dick, it's rock hard!"
    show jenny f_couch_sit_sexy
    pause
    show jenny f_couch_sit_sexy_talk
    jen "You know, if you ask me real nice... I might just help you out with that."
    show jenny f_couch_sit_sexy
    show player f_couch_sit_right_talk
    player_name "R-really?"
    show player f_couch_sit_right
    show jenny f_couch_sit_sexy_talk
    jen "Yeah but only if you beg me for it."
    show jenny f_couch_sit_sexy
    if M_jenny.get("dominance") <= 0:
        player_name "..."
        show player f_couch_sit_right_talk
        player_name "P-please?"
        show player f_couch_sit_right
        show jenny f_couch_sit_eyeroll
        jen "Oh c'mon, that was pathetic!"
        show jenny f_couch_sit_sexy
        player_name "..."
        show jenny f_couch_sit_sexy_talk
        jen "Say this:"
        jen "Please, {b}Princess [jen_name]{/b}."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Please, {b}Princess [jen_name]{/b}."
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "I know, I'm just a pathetic little loser..."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "{b}*Sigh*{/b} I know, I'm just a pathetic little loser..."
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "... Not even worthy of your feet."
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "... Not even worthy of your feet."
        show player f_couch_sit_right
        show jenny f_couch_sit_laugh
        jen "Hahahaah!"
        show jenny f_couch_sit_sexy
        show player f_couch_sit_right_talk
        player_name "Shh, you're going to wake up {b}[deb_name]{/b}!"
        show player f_couch_sit_right
        show jenny f_couch_sit_sexy_talk
        jen "Yeah, yeah... Alright, get it out, loser."
        show jenny f_couch_sit_sexy_down
        show player a_couch_boner with dissolve
        pause
        show player f_couch_sit_down a_couch_sides
        $ M_jenny.set('sex speed', .3)
        show jenny a_empty
        show expression AnimatedImage("jenny_couch_dick_rub", [1,2,3], M_jenny) as jenny_couch_dick_rub zorder 3 at Position(xalign = 0.0, yoffset = 0)
        with dissolve
    else:
        show player f_couch_sit_right_talk
        player_name "Screw you!"
        show player f_couch_sit_right
        show jenny f_couch_sit_upset_talk
        jen "What?!"
        show jenny f_couch_sit_upset
        show player f_couch_sit_right_talk
        player_name "I'm not begging you for anything."
        show player f_couch_sit_right
        show jenny f_couch_sit_angry_talk
        jen "Don't talk to me like that!"
        show jenny f_couch_sit_angry
        show player f_couch_sit_right_talk
        player_name "Shh, you're going to wake up {b}[deb_name]{/b}!"
        show player f_couch_sit_right
        jen "Grr!"
        show player a_couch_boner with dissolve
        show player f_couch_sit_right_talk
        player_name "Just go away and let me finish."
        show player f_couch_sit_right
        show jenny f_couch_sit_angry_pouting
        jen "..."
        show jenny f_couch_sit_upset_talk
        jen "You are such an asshole!"
        show jenny f_couch_sit_upset
        player_name "You're the one who's trying to make me beg for it!"
        show jenny f_couch_sit_upset_talk
        jen "Whatever."
        show jenny f_couch_sit_gross_down
        pause
        show jenny f_couch_sit_upset_talk
        jen "{b}*Sigh*{/b} Here..."
        show jenny f_couch_sit_sexy_down
        show player f_couch_sit_down_talk a_couch_sides
        $ M_jenny.set('sex speed', .3)
        show jenny a_empty
        show expression AnimatedImage("jenny_couch_dick_rub", [1,2,3], M_jenny) as jenny_couch_dick_rub zorder 3 at Position(xalign = 0.0, yoffset = 0)
        player_name "!!!" with hpunch
        player_name "I thought you didn't want to-"
        show player f_couch_sit_down
        show jenny f_couch_sit_sexy_talk_down
        jen "Just shut up!"
        jen "I walked all the way down here, I might as well have some fun."
        show jenny f_couch_sit_sexy_down
        pause
    show jenny f_couch_sit_sexy_talk_down
    jen "How does that feel?"
    show jenny f_couch_sit_sexy_down
    show player f_couch_sit_down_talk
    player_name "So good!"
    show player f_couch_sit_down
    pause
    show jenny f_couch_sit_sexy_talk_down
    jen "You are such a pervert, you know that?"
    jen "Getting off to my feet?"
    show jenny f_couch_sit_sexy_down
    show player f_couch_sit_down_talk
    player_name "This was your idea..."
    show player f_couch_sit_down
    show jenny f_couch_sit_laugh
    jen "Hahahaah!"
    show jenny f_couch_sit_sexy_down
    $ M_player.set("masturbated tv", True)
    jump jenny_couch_fj_loop
    return

label sis_pink_pass:
    scene home_livingroom_tv
    show home_tv_channel_08 at Position(xpos=522, ypos=521) with dissolve
    player_name "( Man, I wish I could access this channel. )"
    pause
    player_name "( {b}[jen_name]{/b} watches a lot of porn... )"
    player_name "( I wonder if {b}she has a subscription{/b}? )"
    return

label tv_pink_channel_pass_check:
    if M_jenny.finished_state(S_jenny_figure_out_password):
        if pink_user.lower().strip() == "l6bv12r" and pink_pass.strip() == "12345":
            $ tv_channel_pink = False
            player_name "( !!! )"
            player_name "( It worked! )"
            pause
        else:
            show home_tv_channel_08 at Position(xpos=522, ypos=522)
            show jenny_wrong_pass at Position(xpos=520, ypos= 510) with dissolve
            pause 1
            hide jenny_wrong_pass with dissolve
            $ game.main()
        jump expression game.dialog_select("tv_channel_responses")
    else:
        call sis_pink_pass
        $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
