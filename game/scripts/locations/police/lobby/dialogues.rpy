label police_lobby_first_visit:
    scene police_lobby_b
    show player 11 with dissolve
    player_name "( The Police station... Man, I'm sure glad I never had to come here before. )"
    hide player with dissolve
    return

label police_lobby_mia_clues:
    scene police_lobby_b
    show player 35 with dissolve
    player_name "( Hmm... Where to start... )"
    player_name "( I should {b}question his partner{/b} first. )"
    player_name "( They may know where he could be... )"
    hide player with dissolve
    return

label police_lobby_roxxy_ask_earl_release:
    scene police_lobby_b
    show player 5 at left
    show roxxy 33 at right
    with dissolve
    rox "... Okay, so what now?"
    show roxxy 32
    show player 10
    player_name "We should {b}find an officer to talk to.{/b}"
    hide player
    hide roxxy
    with dissolve
    return

label police_board:
    scene police_board
    with dissolve
    player_name "( This looks like the info board... )"
    pause
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
