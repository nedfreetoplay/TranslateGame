label smiths_basement_dialogue:
    $ player.go_to(L_smith_basement)
    $ player.location.visited()
    call smiths_basement_whatfor
    $ game.main()

label smiths_basement_whatfor:
    if game.timer.is_dark():
        scene expression "backgrounds/location_smith_basement_night_blur_fix.jpg"
    else:
        scene expression "backgrounds/location_smith_basement_day_blur_fix.jpg"
    show player 34 with dissolve
    player_name "( Зачем добавили это место? )"
    show player 4 at Position (xoffset=5) with dissolve
    player_name "( Думаю, мне незачем здесь находиться... )"
    hide player with dissolve
    return

label smith_basement_sneaking:
    scene expression "backgrounds/location_smith_basement_night_blur.jpg"
    show player 11 with dissolve
    player_name "..."
    show player 10
    player_name "Это очень стремно!"
    player_name "... А что это за дыра в полу?"
    player_name "Хмм. Я надеюсь, что тесты не где-то там внизу..."
    player_name "Я ни в коем случае не пойду через эти ворота!"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
