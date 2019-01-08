label police_lobby_first_visit:
    scene police_lobby_b
    show player 11 with dissolve
    player_name "( Полицейский участок... Ну, я очень рад, что раньше никогда здесь не был. )"
    hide player with dissolve
    return

label police_lobby_mia_clues:
    scene police_lobby_b
    show player 35 with dissolve
    player_name "( Хмм... Откуда же начать... )"
    player_name "( Нужно вначале {b}спросить его напарника{/b}. )"
    player_name "( Он должен знать, где искать {b}Гарольда{/b}... )"
    hide player with dissolve
    return

label police_lobby_roxxy_ask_earl_release:
    scene police_lobby_b
    show player 5 at left
    show roxxy 33 at right
    with dissolve
    rox "... Хорошо, что теперь?"
    show roxxy 32
    show player 10
    player_name "Нужно {b}найти полицейского и поговорить с ним.{/b}"
    hide player
    hide roxxy
    with dissolve
    return

label police_board:
    scene police_board
    with dissolve
    player_name "( Это наверное стенд с информацией... )"
    pause
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
