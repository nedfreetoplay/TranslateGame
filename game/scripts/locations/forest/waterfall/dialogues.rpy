label waterfall_okita_get_ingredients:
    scene location_forest_waterfall_day_blur
    show player 2
    with dissolve
    player_name "Wow, this place is beautiful!"
    player_name "... And it looks like the perfect spot to look for that {b}Horny Toad{/b} Okita wants."
    return

label take_toad:
    call expression game.dialog_select("take_toad_dialogue")
    $ player.get_item("toad")
    $ game.main()

label take_toad_dialogue:
    show expression game.timer.image("backgrounds/location_forest_waterfall_day{}.jpg")
    show expression "boxes/popup_item_toad1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_toad1.png" with dissolve
    scene location_forest_waterfall_day_blur
    show player 531b
    with dissolve
    player_name "Yup, I was right."
    player_name "That is one ugly frog!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
