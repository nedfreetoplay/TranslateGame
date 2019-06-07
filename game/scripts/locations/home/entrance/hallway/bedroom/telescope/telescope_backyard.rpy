label backyard:
    call expression game.dialog_select(game.telescope.backyard)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_backyard_morning_1:
    scene windowbackyardday01
    player_name "( {b}Mrs. Johnson's{/b} yoga mat is there... )"
    player_name "( ...There's no one in the backyard. )"
    return

label telescope_backyard_afternoon_1:
    scene windowbackyardday01
    player_name "( {b}Mrs. Johnson's{/b} yoga mat is there... )"
    player_name "( ...There's no one in the backyard. )"
    return

label telescope_backyard_afternoon_2:
    scene windowbackyardday02
    player_name "( Man... )"
    player_name "( {b}Mrs. Johnson{/b} is so... flexible... )"
    return

label telescope_backyard_afternoon_3:
    scene windowbackyardday03
    player_name "( {b}Mrs. Johnson{/b} is always doing yoga... )"
    player_name "( I guess she likes to stay in shape. )"
    return

label telescope_backyard_afternoon_4:
    scene windowbackyardday04
    player_name "( Oh, yeah... )"
    player_name "( That's my favorite position. )"
    player_name "( I get turned on so much when she does that... I don't know why. )"
    return

label telescope_backyard_night_1:
    scene windowbackyardnight01
    player_name "( {b}Mrs. Johnson{/b} left her yoga mat outside. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
