label treehouse_first_visit:
    scene expression game.timer.image("treehouse{}_b")
    show player 32 with dissolve
    player_name "Класс! Наш старый домик на дереве всё ещё держится."
    hide player with dissolve
    return

label treehouse_closeup_first_visit:
    scene expression game.timer.image("treehouse_c{}")
    player_name "( Выглядит не безопасно... )"
    return

label treehouse_interior_first_visit:
    scene expression game.timer.image("treehouse_inside{}_b")
    show player 2 with dissolve
    player_name "( Уау! Здесь ни чего не изменилось! )"
    player_name "( Надо осмотреться вокруг... )"
    hide player with dissolve
    return

label treehouse_got_wood_pile:
    scene expression game.timer.image("treehouse{}_b")
    if M_ross.is_state(S_ross_get_easels):
        call expression game.dialog_select("treehouse_woodpile_ross_easels")

    elif M_dewitt.between_states(S_dewitt_garage_find_paint, S_dewitt_make_replacement_guitar):
        call expression game.dialog_select("treehouse_woodpile_dewitt_guitar")

    call expression game.dialog_select("treehouse_woodpile_after")
    $ player.get_item("wood_pile")
    $ game.main()

label treehouse_woodpile_ross_easels:
    show player 585 with dissolve
    player_name "Выглядит великолепно!"
    show player 586
    pause
    show player 585
    player_name "Надо их взять домой чтобы {b}на папином станке{/b} сделать несколько мольбертов."
    return

label treehouse_woodpile_dewitt_guitar:
    show player 585 with dissolve
    player_name "Да, это должно сработать."
    player_name "С некоторым инструментом и немного {b}краски{/b}, я легко смогу сделать макет гитары."
    return

label treehouse_woodpile_after:
    hide player with dissolve
    show expression "boxes/popup_item_wood1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_wood1.png" with dissolve
    return

label treehouse_got_controller:
    call expression game.dialog_select("treehouse_controller_dialogue_pre")
    $ player.get_item("controller")
    call expression game.dialog_select("treehouse_controller_dialogue_after")
    $ game.main()

label treehouse_controller_dialogue_pre:
    scene expression game.timer.image("treehouse_inside{}_b")
    show player 502b
    with dissolve
    player_name "Вот оно!"
    player_name "Насколько помню, {b}Эрику{/b} она очень нравилась..."
    player_name "Очень мило что он позволил мне её взять."
    show expression "boxes/popup_item_controller1.png" at truecenter with dissolve

label treehouse_controller_dialogue_after:
    pause
    hide expression "boxes/popup_item_controller1.png" with dissolve
    show player 502
    player_name "Отнесу его лучше {b}Джун{/b}."
    return

label lure_02:
    call expression game.dialog_select("lure_02_dialogue_pre")
    $ player.get_item("lure01")
    call expression game.dialog_select("lure_02_dialogue_after")
    $ game.main()

label lure_02_dialogue_pre:
    scene expression "backgrounds/location_treehouse_box.jpg"
    show expression "objects/closeup_bait02.png" with dissolve
    return

label lure_02_dialogue_after:
    show unlock36 at truecenter with dissolve
    pause
    hide unlock36 with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
