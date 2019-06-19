label erik_bedroom:
    call expression game.dialog_select(game.telescope.erik)
    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_erik_morning_1:
    scene windowerikmorning01
    if game.timer.is_weekend():
        player_name "( Его нет в комнате. )"
    else:
        player_name "( Наверное, он уже ушел в школу. )"
    return

label telescope_erik_morning_2:
    scene windowerikmorning02
    if game.timer.is_weekend():
        player_name "( Вероятно, он не спал всю ночь, играя в эту игру... )"
    else:
        player_name "( Он играет в игры? Он должен готовиться к школе... )"
    return

label telescope_erik_afternoon_1:
    scene windowerikday 1
    player_name "( Его сейчас нет дома. )"
    return

label telescope_erik_afternoon_2:
    scene windowerikday 2
    player_name "( Жалюзи закрыты. Должно быть, он снова пользуется лосьоном. )"
    return

label telescope_erik_afternoon_3:
    scene windowerikday04a_b
    player_name "( Что это {b}Эрик{/b} смотрит? )"
    player_name "( Это выглядит странно знакомым... )"
    return

label telescope_erik_afternoon_4:
    scene windowerikday05a_b
    player_name "Ухх!!" with hpunch
    player_name "( Я понимаю, почему он был так рад получить его... )"
    return

label telescope_erik_night_1:
    scene windoweriknight01
    player_name "( Он всегда играет в эту игру... )"
    return

label telescope_erik_night_2:
    scene windoweriknight02
    player_name "( Жалюзи закрыты. Должно быть, он снова пользуется лосьоном. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
