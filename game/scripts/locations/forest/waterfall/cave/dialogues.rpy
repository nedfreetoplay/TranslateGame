label cave_okita_get_ingredients:
    scene location_forest_cave_night_blur
    show player 10
    with dissolve
    player_name "Hmm, it looks like something is nesting in here!"
    player_name "I'd better find that {b}flower{/b} and get out before whatever it is comes home."
    player_name "Okita said they only bloom {b}at night{/b}..."
    return

label take_caveflower:
    call expression game.dialog_select("take_caveflower_dialogue")
    $ player.get_item("caveflower")
    $ game.main()

label take_caveflower_dialogue:
    show expression game.timer.image("backgrounds/location_forest_cave{}_blur.jpg")
    show expression "boxes/popup_item_flower1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_flower1.png" with dissolve
    scene location_forest_cave_night_blur
    show player 559
    with dissolve
    player_name "It's... Glowing!"
    player_name "I need to get this back to Okita."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
