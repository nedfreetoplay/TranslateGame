label pier_first_visit:
    scene expression game.timer.image("backgrounds/location_pier{}.jpg")
    show player 2 at left with dissolve
    player_name "( Здесь пахнет так, как буд то поблизости океан. )"
    player_name "( Люди говорят что тут лучшее место для {b}рыбалки{/b}. )"
    return

label pier_board_first_visit:
    scene expression game.timer.image("pier{}")
    show player 4 at left with dissolve
    player_name "( Это должны быть {b}виды рыб{/b}, которую можно поймать на Пирсе и какую {b}приманку{/b} нужно использовать. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
