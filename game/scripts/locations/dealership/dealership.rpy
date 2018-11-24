label dealership_dialogue:
    if game.timer.is_dark():
        scene expression L_dealership_front.background_blur
        show player 10
        player_name "The car dealership is closed..."
        player_name "I should go there {b}tomorrow morning{/b}"
        $ game.main()
    else:
        $ player.go_to(L_dealership)
    $ game.main()

label dealership_front_dialogue:
    $ player.go_to(L_dealership_front)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
