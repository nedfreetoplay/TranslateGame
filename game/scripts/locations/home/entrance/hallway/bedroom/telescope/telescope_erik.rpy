label erik_bedroom:
    if sister.started(sis_telescope01):
        call expression game.dialog_select("telescope_erik_sister_spying")
        $ sis_telescope01.finish()
        $ M_jenny.unforce()
        $ M_jenny.place(place = L_home_diningroom)
        $ M_jenny.force(tod = 0)
        jump expression game.dialog_select("bedroom_dialogue")
    else:
        call expression game.dialog_select(game.telescope.erik)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_erik_sister_spying:
    scene
    show windowerikday 3a
    player_name "( {b}Хозяйка квартиры Эрика{/b}. )"
    show windowerikday 3b with fastdissolve
    player_name "( Она, наверное, просто проверяет как у него дела... )"
    show windowerikday 3c with fastdissolve
    player_name "..."
    player_name "( Они целуются в губы? Это странно... )"
    show windowerikday 3d with fastdissolve
    player_name "( Что... )"
    player_name "( Он только что схватил ее за грудь?? )"
    show windowerikday 3l with fastdissolve
    player_name "( Она закрывает жалюзи... )"
    show windowerikday 2 with fastdissolve
    pause
    hide windowerikday
    hide screen telescope
    show telescope_caught 1
    with dissolve

    jen "( Хм... Интересно, что он задумал. )"
    show telescope_caught 3 with dissolve
    pause
    show telescope_caught 5
    jen "( Чем он занимается? )"
    scene location_home_bedroom_telescope_window
    show player 357 at Position(xpos=456,ypos=758)
    with dissolve
    pause
    show jenny 137 at right with fastdissolve
    pause
    show jenny 138
    jen "Веселишься?"
    show jenny 137
    show player 358 at Position(xpos=448)
    player_name "!!!" with vpunch
    show player 360 at Position(ypos=768)
    show jenny 136 at Position(xpos=952)
    player_name "Что ты здесь делаешь?!"
    show player 361
    show jenny 135
    jen "Лучше спросить, что ТЫ здесь делаешь?"
    jen "Тебе больше нечем заняться, как шпионить за соседями?"
    show player 360
    show jenny 136
    player_name "Я... не понимаю о чем ты говоришь!"
    show player 361
    show jenny 135
    jen "О, хочешь сказать что наблюдаешь за птицами?"
    show player 360
    show jenny 136
    player_name "Может быть!"
    show player 359
    show jenny 135
    jen "Ха! Ты жалок..."
    hide jenny with fastdissolve
    pause
    show player 360
    player_name "Ты могла бы закрыть дверь!"
    return

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
