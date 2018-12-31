label cave_okita_get_ingredients:
    scene location_forest_cave_night_blur
    show player 10
    with dissolve
    player_name "Хмм, похоже что тут чьё-то гнездо!"
    player_name "Надо найти {b}цветок{/b} и уходить пока гнездо пустое."
    player_name "Окита говорила, что они цветут только {b}ночью{/b}..."
    return

label take_caveflower:
    call expression game.dialog_select("take_caveflower_dialogue")
    $ player.get_item("caveflower")
    $ game.main()

label take_caveflower_dialogue:
    show expression game.timer.image("backgrounds/location_forest_cave{}_blur.jpg")
    show expression "boxes/popup_item_flower8.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_flower8.png" with dissolve
    scene location_forest_cave_night_blur
    show player 559
    with dissolve
    player_name "Они... Светятся!"
    player_name "Над собрать и отнести Оките."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
