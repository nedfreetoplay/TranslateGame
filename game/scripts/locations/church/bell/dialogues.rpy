label church_bell:
    scene location_church_bell_closeup
    if M_aqua.is_state(S_aqua_bell_search):
        call expression game.dialog_select("church_bell_aqua_bell_search")
        $ M_aqua.trigger(T_aqua_bell_engraving)
    else:

        pause
    $ game.main()

label church_bell_aqua_bell_search:
    player_name "Этот колокол массивный!"
    player_name "( Интересно, как Бен Довер с ним связан? )"
    player_name "( Может он участвовал в установке колокола? )"
    player_name "( ...Колокол выглядит очень старым, и... )"
    player_name "( на нём какая-то гравировка, похожая на ту что на надгробие! )"
    player_name "Хмм..."
    player_name "( Похоже на какой-то {b}камень{/b}, вокруг которого {b}деревья{/b} и освещающая {b}луна{/b} . )"
    player_name "( У одного дерева то ли дупло, то ли {b}отверстие{/b} . )"
    player_name "( Интересно, что с этим связано? )"
    player_name "( Надо подумать, где в городе я могу найти что-то похожее? )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
