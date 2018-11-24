label MC_computer_night_locked:
    scene expression game.timer.image("bedroom{}")
    show player 24 at left
    player_name "( I'm so tired right now, I'd better go to bed... )"
    hide player 17 at left
    return

label egay_search_dialogue:
    if erik.started(erik_orcette):
        call expression game.dialog_select("egay_search_dialogue_erik_orcette_started")
    show screen MC_computer
    call screen egay("Search")

label egay_search_dialogue_erik_orcette_started:
    scene player_computer_bg
    show player_computer_egay_search
    player_name "( Hmm... I guess I should just type in the name of the item {b}Erik{/b} wanted. )"
    player_name "( What was it again? )"
    hide player_computer_egay_search
    hide player_computer_bg
    return

label egay_purchased_dialogue:
    scene player_computer_bg
    show player_computer_egay_purchased
    player_name "( Looks like I should get the package in the mailbox on {b}Tuesday{/b}. )"
    hide player_computer_egay_purchased
    hide player_computer_bg
    show screen MC_computer
    call screen egay("Purchased")

label egay_search:
    if erik.started(erik_orcette):
        if egay_search.lower() == "orcette":
            show screen MC_computer
            call screen egay("Found")
    show screen MC_computer
    call screen egay("Fail")

label webcam_dialogue:
    scene expression game.timer.image("MC_computer{}_b")
    if not connected:
        call expression game.dialog_select("webcam_dialogue_not_connected")
        call screen MC_computer

    elif (L_home_sisbedroom.is_here(M_jenny) and game.timer.is_morning()):
        if M_jenny.is_state(S_jenny_watch_stream) or M_jenny.is_state(S_jenny_watch_stream_tier_2) or M_jenny.is_state(S_jenny_watch_stream_tier_3) or M_jenny.finished_state(S_jenny_prepare_stream_tier_4):
            hide screen MC_webcam
            hide screen MC_computer
            $ A_computer_genius.unlock()
            if M_jenny.is_state(S_jenny_watch_stream):
                label electroclit_replay:
                    call expression game.dialog_select("webcam_dialogue_sis_webcam_started_pre")
                call expression game.dialog_select("webcam_dialogue_sis_webcam01_started_pre")
                $ current_camshow = 1

            elif M_jenny.is_state(S_jenny_watch_stream_tier_2):
                label ultravibrator_replay:
                    call expression game.dialog_select("webcam_dialogue_sis_webcam_started_pre")
                call expression game.dialog_select("webcam_dialogue_sis_webcam02_started_pre")
                $ current_camshow = 2

            elif M_jenny.is_state(S_jenny_watch_stream_tier_3):
                label dualsybian_replay:
                    call expression game.dialog_select("webcam_dialogue_sis_webcam_started_pre")
                call expression game.dialog_select("webcam_dialogue_sis_webcam03_started_pre")
                $ current_camshow = 3

            elif M_jenny.finished_state(S_jenny_prepare_stream_tier_4):
                $ sis_lastwebcam_show_seen = True
                label badmonster_replay:
                    call expression game.dialog_select("webcam_dialogue_sis_webcam_started_pre")
                call expression game.dialog_select("webcam_dialogue_sis_webcam04_started_pre")
                $ current_camshow = 4
            $ anim_toggle = False
            $ xray_toggle = False
            jump expression game.dialog_select("sis_camshow_loop")
        else:

            call expression game.dialog_select("webcam_dialogue_nothing_showing")
    else:

        call expression game.dialog_select("webcam_dialogue_nothing_showing")
    show screen MC_computer
    call screen MC_webcam

label webcam_dialogue_not_connected:
    scene player_computer_bg
    show player_computer_webscreen
    player_name "( Weird. It says I can connect my computer to the {b}webcam{/b}, but it seems I can't do it from here. )"
    hide player_computer_webscreen
    hide player_computer_bg
    return

label webcam_dialogue_sis_webcam_started_pre:
    scene player_computer_bg with None
    show player_computer_webscreen_connecting
    $ renpy.pause(2, hard=True)
    hide player_computer_webscreen_connecting
    scene jennycam1
    show xtra 16 zorder 2
    show jennysex 6 zorder 1 at Position(xpos = 533, ypos = 746)
    jen "Hey guuuys!"
    jen "Are you ready for some hot camming?"
    jen "I've been looking forward to getting wet all day!"
    jen "Oh! Don't forget to subscribe to watch the next part of the show..."
    jen "Because this beauty right here needs money!"
    show jennysex 8 with fastdissolve
    jen "Now, for my special subscribers..."
    jen "... I have this brand new toy I wanted to try!"
    show jennysex 7 with fastdissolve
    pause
    return

label webcam_dialogue_sis_webcam01_started_pre:
    show jennysex 10 with fastdissolve
    pause
    show jennysex 9
    jen "The {b}Electro Clit{/b}!"
    jen "It's a little vibrating friend ... for my clit!"
    show jennysex 11
    jen "I've always wanted one of these!"
    show jennysex 21 at Position(xpos = 543, ypos = 767) with dissolve
    jen "Let's give it a try, boys..."
    show jennysex 22 with fastdissolve
    jen "Woah! This thing is fast..."
    return

label webcam_dialogue_sis_webcam02_started_pre:
    show jennysex 13 with fastdissolve
    pause
    show jennysex 12
    jen "The {b}Ultra Vibrator 2000{/b}!"
    jen "It's a dildo! Nice and ribbed too..."
    jen "Now, since you kept asking to see some insertion with my toys..."
    jen "... I figured I'd give you all a little treat!"
    jen "Here we go, boys!"
    show jennysex 26 at Position(xpos = 0.5, ypos = 770) with dissolve
    jen "This thing looks like the perfect size for me."
    jen "Let's put it to the test..."
    show jennysex 27 with fastdissolve
    pause
    show jennysex 31 at Position(xpos = 512, ypos = 770)
    return

label webcam_dialogue_sis_webcam03_started_pre:
    show jennysex 19 at Position(xpos = 577) with fastdissolve
    pause
    show jennysex 18 with fastdissolve
    jen "The {b}Dual Sybian{/b}!"
    show jennysex 20
    jen "I've been reading complaints online that I'm scared to do anal..."
    jen "So here's proof that I am NOT scared to try it!"
    jen "In fact, why stop at one hole?"
    jen "For my fans, I'm gonna do double penetration!"
    show jennysex 18
    jen "Let me hop on top of this bull and get my anal cherry popped..."
    show jennysex 34 at Position(xpos = 344, ypos = 727) with dissolve
    pause
    show jennysex 35 at Position(xpos = 540, ypos = 582) with fastdissolve
    jen "... Oh god! That's a strange feeling."
    return

label webcam_dialogue_sis_webcam04_started_pre:
    show jennysex 16 with fastdissolve
    pause
    show jennysex 15
    jen "This right here is..."
    jen "THE {b}Bad Monster{/b}!"
    show jennysex 17
    jen "Everyone's been talking about this special toy..."
    jen "... and some of you dared me to let it ravage my pussy."
    show jennysex 15
    jen "I finally managed to get my hands on one!"
    show jennysex 17
    jen "Now get your wallets ready, because I'm about to tame this monster!"
    show jennysex 40 at Position(xpos = 427)
    jen "This one needs a LOT of lube..."
    show jennysex 41
    jen "... oh GOD!"
    jen "It's so big!"
    return

label webcam_dialogue_nothing_showing:
    scene player_computer_bg
    show player_computer_webscreen
    player_name "( Theres nothing displaying at the moment. )"
    hide player_computer_webscreen
    hide player_computer_bg
    return

label sis_camshow_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if current_camshow == 1:
                    show expression AnimatedImage("jennysex", [23,24,25,22], M_jenny) as jennysex zorder 1 at Position(xpos = 543, ypos = 767)

                elif current_camshow == 2:
                    show expression AnimatedImage("jennysex", [28,29,30,31], M_jenny) as jennysex zorder 1 at Position(xpos = 512, ypos = 770)

                elif current_camshow == 3:
                    show expression AnimatedImage("jennysex", [36,37,38,35], M_jenny) as jennysex zorder 1 at Position(xpos = 540, ypos = 582)

                elif current_camshow == 4:
                    show expression AnimatedImage("jennysex", [42,43,44,41], M_jenny) as jennysex zorder 1 at Position(xpos = 427, ypos = 746)
                $ animated = True
            pause 8
        else:

            $ pose_counter = 0
            if current_camshow == 1:
                $ pose_list = [23,24,25,22]
                $ xpos_list = [543]
                $ ypos_list = [767]

            elif current_camshow == 2:
                $ pose_list = [28,29,30,31]
                $ xpos_list = [512]
                $ ypos_list = [770]

            elif current_camshow == 3:
                $ pose_list = [36,37,38,35]
                $ xpos_list = [540]
                $ ypos_list = [582]

            elif current_camshow == 4:
                $ pose_list = [42,43,44,41]
                $ xpos_list = [427]
                $ ypos_list = [746]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jennysex {}".format(pose_list[pose_counter]) as jennysex zorder 1 at Position(xpos = xpos_list[0], ypos = ypos_list[0])
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        $ animcounter += 1

label sis_camshow_finish:
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["05_unlocked"] = True
    if current_camshow == 1:
        call expression game.dialog_select("sis_camshow_01_finish")
        $ M_jenny.trigger(T_jenny_watched_stream)

    elif current_camshow == 2:
        call expression game.dialog_select("sis_camshow_02_finish")
        $ persistent.cookie_jar["Jenny"]["gallery_labels"]["05_label"] = "webcam_menu_2"
        $ M_jenny.trigger(T_jenny_watched_stream_tier_2)

    elif current_camshow == 3:
        call expression game.dialog_select("sis_camshow_03_finish")
        $ persistent.cookie_jar["Jenny"]["gallery_labels"]["05_label"] = "webcam_menu_3"
        $ M_jenny.trigger(T_jenny_watched_stream_tier_3)

    elif current_camshow == 4:
        call expression game.dialog_select("sis_camshow_04_finish")
        $ persistent.cookie_jar["Jenny"]["gallery_labels"]["05_label"] = "webcam_menu_4"
    $ game.timer.tick()
    $ game.main()

label sis_camshow_01_finish:
    show jennysex 25b
    jen "Ahhh!!!" with vpunch
    jen "{b}*panting*{/b}"
    jen "That was awesome!"
    hide xtra
    hide jennycam1
    hide jennysex
    scene bedroom_desk
    show player 311 at Position(xpos = 672)
    with fade
    player_name "Woah..."
    player_name "( {b}[jen_name]'s{/b} a camgirl?! )"
    show player 310
    player_name "( It's so weird seeing her like that... )"
    show player 312
    player_name "( Man, she is so hot... )"
    show player 310
    player_name "( I think that's enough for now. )"
    hide player
    with dissolve
    $ renpy.end_replay()
    return

label sis_camshow_02_finish:
    show jennysex 28b
    jen "Oh my... I'm almost there..."
    show jennysex 29b
    jen "I'm... Cumming!!"
    show jennysex 32
    jen "Ahh!!!" with vpunch
    show jennysex 33 with dissolve
    jen "I... I've never had this happen before..."
    jen "What a mess..."
    hide xtra
    hide jennycam1
    hide jennysex
    scene bedroom_desk
    show player 311 at Position(xpos = 672)
    with fade
    player_name "( So that's what squirting looks like. )"
    show player 310
    player_name "There was so much! She even hit the camera!"
    player_name "( I had no idea {b}[jen_name]{/b} could do that... )"
    hide player
    with dissolve
    $ renpy.end_replay()
    return

label sis_camshow_03_finish:
    show jennysex 39 at Position(xpos = 540)
    jen "Ahhh!!!" with hpunch
    jen "{b}*panting*{/b}"
    jen "I've never cum this hard before..."
    hide xtra
    hide jennycam1
    hide jennysex
    scene bedroom_desk
    show player 311 at Position(xpos = 672)
    with fade
    player_name "Wow..."
    player_name "( She really loves riding that thing. )"
    show player 310
    player_name "( I wonder what else she's willing to do on camera... )"
    hide player
    with dissolve
    $ renpy.end_replay()
    return

label sis_camshow_04_finish:
    show jennysex 43 at Position(xpos = 427)
    jen "Ahhh!!!" with vpunch
    show jennysex 45 with fastdissolve
    jen "What a GOOD monster..."
    jen "... my pussy will be sore for days!"
    hide xtra
    hide jennycam1
    hide jennysex
    scene bedroom_desk
    show player 311 at Position(xpos = 672)
    with fade
    player_name "( I thought that thing was just for show. )"
    player_name "( Apparently it's possible to fit it in there! )"
    player_name "She did it so easily too..."
    player_name "( I hope she doesn't get in trouble for doing this sort of thing on camera. )"
    hide player
    with dissolve
    $ renpy.end_replay()
    return

label webcam_menu_2:
    label webcam_menu_3:
        label webcam_menu_4:
            scene blank
    menu:
        "Electro Clit":
            jump expression game.dialog_select("electroclit_replay")

        "UltraVibrator 2000" if store._in_replay in ["webcam_menu_2", "webcam_menu_3", "webcam_menu_4"]:
            jump expression game.dialog_select("ultravibrator_replay")

        "Dual Sybian" if store._in_replay in ["webcam_menu_3", "webcam_menu_4"]:
            jump expression game.dialog_select("dualsybian_replay")

        "Bad Monster" if store._in_replay == "webcam_menu_4":
            jump expression game.dialog_select("badmonster_replay")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
