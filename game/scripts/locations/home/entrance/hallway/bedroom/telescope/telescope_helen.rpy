label helen_room:
    call expression game.dialog_select(game.telescope.helen)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_helen_morning_1:
    scene windowhelenmorning01
    player_name "( {b}Мама Мии{/b} всегда молится по утрам... )"
    return

label telescope_helen_afternoon_1:
    scene windowhelenday01
    player_name "( Их нет дома... )"
    return

label telescope_helen_night_1:
    scene windowhelennight01
    player_name "( Странно, что у них у каждого своя кровать... )"
    player_name "( ...Я никогда не видел, чтобы они спали вместе. )"
    return

label telescope_helen_night_2:
    scene location_telescope_helen_night02
    player_name "( О, боже. )"
    player_name "( Похоже, {b}Хелен{/b} злится на него... )"
    player_name "..."
    player_name "( {b}Гарольд{/b} всегда выглядит грустным... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
