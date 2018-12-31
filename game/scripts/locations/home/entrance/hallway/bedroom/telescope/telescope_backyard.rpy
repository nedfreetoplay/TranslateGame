label backyard:
    call expression game.dialog_select(game.telescope.backyard)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_backyard_morning_1:
    scene windowbackyardday01
    player_name "( Там коврик для йоги {b}Миссис Джонсон{/b} ... )"
    player_name "( ...На заднем дворе никого нет. )"
    return

label telescope_backyard_afternoon_1:
    scene windowbackyardday01
     player_name "( Там коврик для йоги {b}Миссис Джонсон{/b} ... )"
    player_name "( ...На заднем дворе никого нет. )"
    return

label telescope_backyard_afternoon_2:
    scene windowbackyardday02
    player_name "( Блин... )"
    player_name "( {b}Миссис Джонсон{/b} такая... гибкая... )"
    return

label telescope_backyard_afternoon_3:
    scene windowbackyardday03
    player_name "( {b}Миссис Джонсон{/b} всегда занимается йогой... )"
    player_name "( Думаю, ей нравится оставаться в форме. )"
    return

label telescope_backyard_afternoon_4:
    scene windowbackyardday04
    player_name "( О, да... )"
    player_name "( Это моя любимая поза. )"
    player_name "( Я так возбуждаюсь, когда она так делает... Я не знаю, почему. )"
    return

label telescope_backyard_night_1:
    scene windowbackyardnight01
    player_name "( {b}Миссис Джонсон{/b} оставила коврик для йоги снаружи. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
