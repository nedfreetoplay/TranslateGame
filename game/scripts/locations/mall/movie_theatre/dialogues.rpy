label movie_theatre_first_visit:
    scene movie_lobby
    show player 14 with dissolve
    player_name "Cool!"
    show player 14
    player_name "( New movies just came out! )"
    show player 17
    player_name "( Hmm... Maybe I could bring someone on a date here... )"
    hide player 17 with dissolve
    return

label movie_theatre_movie_select_pre:
    scene movie_lobby
    show movie_desk zorder 2
    show player 1f zorder 3 at right
    show bub 2 zorder 1 at Position(ypos=570, xpos=440)
    bub "Hi!"
    bub "Going on a date, huh?"
    show bub 1
    show player 14f
    player_name "Uhh... Yeah?"
    show bub 2
    show player 1f
    bub "Niiiice!"
    bub "Is there a particular movie you'd like to watch?"
    return

label movie_theatre_movie_select_after:
    call expression game.dialog_select("movie_theatre_movie_select_after_dialogue")
    call expression game.dialog_select("movie_theatre_watch_movie")
    $ player.go_to(L_mall)
    $ game.main()

label movie_theatre_movie_select_after_dialogue:
    scene movie_lobby
    show movie_desk zorder 2
    show player 1f zorder 3 at right
    show bub 2 zorder 1 at Position(ypos=570, xpos=420) with dissolve
    bub "Good pick!"
    show bub 3 at Position (xpos=470)
    bub "Here's your ticket."
    show bub 1 at Position (xpos=420)
    show player 14f
    player_name "Thanks."
    show player 1f
    show bub 2
    bub "Just don't make a mess on the seats."
    bub "I hate cleaning that stuff off!"
    show bub 1
    show player 11f
    player_name "..."
    show bub 2
    bub "Enjoy!"
    return

label movie_theatre_watch_movie:
    scene movie with fade
    show popup_unfinished at truecenter with dissolve
    pause
    hide popup_unfinished with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
