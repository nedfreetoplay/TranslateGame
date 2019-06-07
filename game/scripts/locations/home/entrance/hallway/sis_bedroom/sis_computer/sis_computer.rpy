label pass_check:
    if sis_pass.lower().strip() == "bad monster" or sis_pass.lower().strip() == "badmonster":
        scene jenny_comp
        $ M_jenny.set("comp locked", False)
        if not sispc_desktop_seen:
            show screen sis_computer
            player_name "( Got it! )"
            player_name "( Alright, now let's see what she's been up to... )"
            call screen sis_computer
        $ sispc_desktop_seen = True
    else:

        scene jenny_comp
        show jenny_wrong_pass at Position(xpos=570, ypos= 448) with dissolve
        $ renpy.pause()
        hide jenny_wrong_pass with dissolve
    call screen sis_computer

label upstairs_bedroom_enter_laptop:
    if L_home_sisbedroom.is_here(M_jenny) and not game.timer.is_night():
        call expression game.dialog_select("jenny_bedroom_cannot_snoop")
        $ game.main()
    if not M_jenny.finished_state(S_jenny_snoop_around_for_laptop) or M_jenny.is_state(S_jenny_snoop_around_for_laptop):
        call expression game.dialog_select("jenny_bedroom_no_password")
        $ game.main()
    if M_jenny.is_state(S_jenny_check_laptop) and game.timer.is_dark():
        call expression game.dialog_select("jenny_bedroom_no_password")
        $ game.main()
    if M_jenny.is_state(S_jenny_check_laptop) and game.timer.is_day():
        scene expression "backgrounds/location_computer_jenny_01.jpg"
        player_name "( Oh crap, it's locked. )"
        player_name "( I need her password! )"
        scene expression player.location.background_closeup with None
        show player 4 with dissolve
        pause
        player_name "( \"My favorite toy...\" )"
        player_name "( Didn't she mention something about a toy in {b}her Diary{/b}? )"
        jen "{b}[deb_name]{/b}, have you seen my hair straightener?!"
        show player 22 with dissolve
        player_name "( Oh crap, it sounds like {b}[jen_name]{/b} is done with her shower! )"
        deb "No, sweetie."
        jen "Well, I can't find it!"
        player_name "( I'd better get out of here! )"
        hide player with dissolve
        $ player.go_to(L_home_hallway)
        scene expression player.location.background_closeup with None
        show player 11 at left
        show jenny b_towel a_towel_hips f_upset_talk
        with dissolve
        jen "Did you just come out of my room?!"
        show jenny f_upset
        show player 10
        player_name "Huh?"
        player_name "No..."
        show player 5
        show jenny f_angry
        pause
        show player 6 with dissolve
        player_name "Please don't hit me with the hair dryer again!"
        show jenny f_eyeroll
        jen "Ugh, just get out of my way, loser!"
        hide jenny with dissolve
        pause
        show player 37 with dissolve
        player_name "( Phew, that was close! )"
        pause
        show player 5 with dissolve
        player_name "( Who knows how long it will take me to find naughty stuff on {b}her laptop{/b}... )"
        player_name "( I should only attempt this when I know I'll have plenty of time to snoop around. )"
        pause
        show player 4 with dissolve
        player_name "( Maybe {b}at night{/b}, when {b}she's sleeping{/b}? )"
        pause
        show player 17 with dissolve
        player_name "( I'll have to be careful but I think it's worth a shot. )"
        hide player with dissolve
        $ game.timer.tick()
        $ player.go_to(L_home_hallway)
        $ M_jenny.trigger(T_jenny_return_from_shower)
        $ game.main()
    if M_jenny.is_state(S_jenny_figure_out_password) and game.timer.is_day():
        call siscomp_day
        $ player.go_to(L_home_hallway)
        $ game._in_shower = None
        $ game.main()
    else:
        $ M_player.set("on_jenny_pc", True)
        call screen sis_computer

label jenny_computer_camslut:
    $ game.in_dialogue = True
    if not sispc_livecrush_seen:
        player_name "( Here it is. )"
        pause
        player_name "( Ugh, her profile is awful... )"
        player_name "( Twenty-four year old goddess? Haha! )"
        pause
        player_name "( Oh, there's a videos tab! )"
        $ sispc_livecrush_seen = True
    $ game.in_dialogue = False
    call screen jenny_camslut

label jenny_camslut_videos_tab:
    $ game.in_dialogue = True
    show screen jenny_camslut_videos
    if not jenny_camslut_videos_tab_seen:
        player_name "( She's got two videos saved here! )"
        pause
        player_name "( I can't watch these in her room though... She might wake up! )"
        pause
        player_name "( Maybe there's some way to {b}connect her computer to mine{/b}? )"
        $ jenny_camslut_videos_tab_seen = True
    elif M_player.get("on_jenny_pc") and game.timer.is_dark():
        player_name "( I can't watch those in her room... She might wake up! )"
        pause
    elif M_jenny.is_state(S_jenny_check_for_new_video):
        player_name "( Dang it! )"
        pause
        player_name "( Not a single new video... )"
        pause
        player_name "( It says she was online yesterday... I wonder why she's not saving her new shows? )"
        $ M_jenny.trigger(T_jenny_checked_pc_for_new_vids)
    elif M_jenny.is_state(S_jenny_video_3_uploaded):
        player_name "( It worked, she saved a new video! )"
    $ renpy.hide_screen("jenny_camslut")
    $ game.in_dialogue = False
    call screen jenny_camslut_videos

label jenny_camslut_video_choice(video=1):
    if not M_player.get("on_jenny_pc"):
        if not (M_jenny.get("watched_video_1") or M_jenny.get("watched_video_2")):
            player_name "( Nice! )"
            player_name "( Now let's check out those videos! )"
        hide screen MC_computer
        hide screen sis_computer
        hide screen jenny_camslut_videos
        call expression game.dialog_select("jenny_computer_video_{}".format(video))
        $ M_jenny.set("watched_video_{}".format(video), True)
        if M_jenny.get("watched_video_1") and M_jenny.get("watched_video_2") and M_jenny.is_state(S_jenny_figure_out_password):
            scene expression player.location.background_closeup with None
            show player 5
            player_name "( A real penis? )"
            player_name "( Is she talking about fucking someone on camera?! )"
            player_name "( Surely, she wouldn't go that far, would she? )"
            pause
            show player 403
            player_name "( Man, I hope she makes more videos! )"
            hide player with dissolve
            hide screen comp_screen
            hide screen sis_computer
            $ M_jenny.trigger(T_jenny_a_real_penis)
            $ game.main()
        if M_jenny.is_state(S_jenny_video_3_uploaded):
            $ M_jenny.trigger(T_jenny_checked_new_vid)
    else:
        $ game.in_dialogue = True
        show screen jenny_camslut_videos
        show screen sis_computer
        player_name "I can't watch that here! She might wake up!"
        $ game.in_dialogue = False
    show screen sis_computer
    call screen jenny_camslut_videos
    return

label jenny_bedroom_no_password:
    scene expression "backgrounds/location_computer_jenny_01.jpg"
    player_name "( It's password locked... )"
    player_name "( I should try to figure out the password first. )"
    player_name " ( Maybe she left some kind of clue around )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
