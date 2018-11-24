label helen_room:
    call expression game.dialog_select(game.telescope.helen)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_helen_morning_1:
    scene windowhelenmorning01
    player_name "( {b}Mia's mom{/b} is always praying in the morning... )"
    return

label telescope_helen_afternoon_1:
    scene windowhelenday01
    player_name "( They're not home... )"
    return

label telescope_helen_night_1:
    scene windowhelennight01
    player_name "( It's odd how they both have their own bed... )"
    player_name "( ...I've never seen them sleep together. )"
    return

label telescope_helen_night_2:
    scene location_telescope_helen_night02
    player_name "( Oh boy. )"
    player_name "( Looks like {b}Helen{/b} is mad at him... )"
    player_name "..."
    player_name "( {b}Harold{/b} always looks so sad... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
