label erik_bedroom:
    call expression game.dialog_select(game.telescope.erik)
    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_erik_morning_1:
    scene windowerikmorning01
    if game.timer.is_weekend():
        player_name "( He's not in his room. )"
    else:
        player_name "( He probably already left for school. )"
    return

label telescope_erik_morning_2:
    scene windowerikmorning02
    if game.timer.is_weekend():
        player_name "( He probably stayed up all night playing that game... )"
    else:
        player_name "( He's playing games? He should be getting ready for school... )"
    return

label telescope_erik_afternoon_1:
    scene windowerikday 1
    player_name "( He's not home. )"
    return

label telescope_erik_afternoon_2:
    scene windowerikday 2
    player_name "( The blinds are closed. He must be using his lotion again. )"
    return

label telescope_erik_afternoon_3:
    scene windowerikday04a_b
    player_name "( What's {b}Erik{/b} looking at? )"
    player_name "( That looks oddly familiar... )"
    return

label telescope_erik_afternoon_4:
    scene windowerikday05a_b
    player_name "Uhh!!" with hpunch
    player_name "( I can see why he was so excited about getting it... )"
    return

label telescope_erik_night_1:
    scene windoweriknight01
    player_name "( He's always playing that game... )"
    return

label telescope_erik_night_2:
    scene windoweriknight02
    player_name "( The blinds are closed. He must be using his lotion again. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
