label peep_hole_dialogue:
    if M_player.get("peep_hole_first"):
        scene expression player.location.background_blur
        player_name "( That's one ugly rug... )"
        player_name "( I wonder why it's up here? )"
        scene expression game.timer.image("backgrounds/location_home_attic_cutscene01{}.jpg")
        player_name "( Hmm? )"
        player_name "( There's a little hole in the floorboards here... )"
        pause
        player_name "( I-is that- )"
        $ M_player.set("peep_hole_first", False)
        call expression game.dialog_select("peep_hole_{}_first".format(game.timer._tod))
    else:
        scene expression game.timer.image("backgrounds/location_home_attic_cutscene01{}.jpg")
        pause
        player_name "( Let's see what {b}[jen_name]{/b} is up to? )"
        call expression game.dialog_select("peep_hole_{}".format(game.timer._tod))
    $ game.main()

label peep_hole_0_first:
label peep_hole_1_first:
    scene expression "backgrounds/location_home_attic_peep_morning.jpg"
    pause
    player_name "( !!! )" with hpunch
    player_name "( It's a peephole, right over {b}[jen_name]'s{/b} bed! )"
    pause
    player_name "( Well, that's convenient... )"
    player_name "( I wonder how it got here? )"
    return

label peep_hole_2_first:
label peep_hole_3_first:
    scene expression "backgrounds/location_home_attic_peep_night.jpg"
    pause
    player_name "( !!! )" with hpunch
    player_name "( It's a peephole, right over {b}[jen_name]'s{/b} bed! )"
    pause
    player_name "( Well, that's convenient... )"
    player_name "( I wonder how it got here? )"
    return

label peep_hole_0:
    scene expression "backgrounds/location_home_attic_peep_morning.jpg"
    pause
    player_name "( Hmm, just an empty bed... )"
    player_name "( I wonder where she's at? )"
    return

label peep_hole_1:
    scene expression "backgrounds/location_home_attic_peep_day_01.jpg"
    pause
    player_name "( Hmm, she's just laying around, writing in her diary... )"
    scene expression "backgrounds/location_home_attic_peep_day_02.jpg"
    pause
    player_name "( Booooring!! )"
    return

label peep_hole_2:
    scene expression "backgrounds/location_home_attic_peep_evening_01.jpg"
    pause
    player_name "( I-is she- )"
    player_name "( !!! )" with hpunch
    player_name "( She's masturbating! )"
    scene expression "backgrounds/location_home_attic_peep_evening_02.jpg"
    pause
    player_name "( Oh, this is awesome!! )"
    pause
    return

label peep_hole_3:
    scene expression "backgrounds/location_home_attic_peep_night.jpg"
    pause
    player_name "( Aww, she's already gone to bed for the night. )"
    pause
    player_name "( Heh, she looks kinda cute and innocent when she's sleeping... )"
    player_name "( ... Not at all like the bitchzilla she really is! )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
