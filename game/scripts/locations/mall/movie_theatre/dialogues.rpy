label movie_theatre_first_visit:
    scene movie_lobby
    show player 14 with dissolve
    player_name "Круто!"
    show player 14
    player_name "( Недавно вышедшие фильмы! )"
    show player 17
    player_name "( Хмм... Может мне стоит привести кого-то сюда на свидание... )"
    hide player 17 with dissolve
    return

label movie_theatre_movie_select_pre:
    scene movie_lobby
    show movie_desk zorder 2
    show player 1f zorder 3 at right
    show bub 2 zorder 1 at Position(ypos=570, xpos=440)
    bub "Привет!"
    bub "Идешь на свидание, хех?"
    show bub 1
    show player 14f
    player_name "Эмм... Да?"
    show bub 2
    show player 1f
    bub "Отлииично!"
    bub "Есть какой-то определенный фильм, который ты хотел бы посмотреть?"
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
    bub "Хороший выбор!"
    show bub 3 at Position (xpos=470)
    bub "Твой билет."
    show bub 1 at Position (xpos=420)
    show player 14f
    player_name "Спасибо."
    show player 1f
    show bub 2
    bub "Только не мусори возле себя."
    bub "Я ненавижу убирать эту дрянь!"
    show bub 1
    show player 11f
    player_name "..."
    show bub 2
    bub "Наслаждайся!"
    return

label movie_theatre_watch_movie:
    scene movie with fade
    show popup_unfinished at truecenter with dissolve
    pause
    hide popup_unfinished with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
