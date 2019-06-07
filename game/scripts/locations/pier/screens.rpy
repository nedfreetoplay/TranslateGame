screen pier():
    use mods_screens_hook("pier")

    if M_terry.get_state() == S_terry_end:
        add game.timer.image("backgrounds/location_pier_tigger{}.jpg")

    elif M_terry.get_state() == S_terry_drunk:
        add game.timer.image("backgrounds/location_pier_missing_day{}.jpg")

    else:
        add game.timer.image("backgrounds/location_pier_day{}.jpg")

        imagebutton:
            focus_mask True
            pos (548,469)
            idle game.timer.image("objects/object_board_02{}.png")
            hover HoverImage(game.timer.image("objects/object_board_02{}.png"))
            action Hide("pier"), Jump("pier_board")

    if player.location.is_here(M_terry):
        imagebutton:
            focus_mask True
            pos (602,364)
            if M_terry.get_state() != S_terry_nemesis:
                if not game.timer.is_dark():
                    idle "objects/character_terry_01.png"
                    hover HoverImage("objects/character_terry_01.png")
                else:
                    idle "objects/character_terry_02.png"
                    hover HoverImage("objects/character_terry_02.png")

            else:
                if not game.timer.is_dark():
                    idle "objects/character_terry_03.png"
                    hover HoverImage("objects/character_terry_03.png")
                else:
                    idle "objects/character_terry_04.png"
                    hover HoverImage("objects/character_terry_04.png")
            action Hide("pier"), Jump("terry_button_dialogue")

    imagebutton:
        focus_mask True
        pos (184,449)
        idle game.timer.image("objects/object_chair_01{}.png")
        hover HoverImage(game.timer.image("objects/object_chair_01{}.png"))
        action [Hide("pier"),
                If(
                    game.timer.is_dark(),
                    Jump("fishing_night"),
                    If(
                        player.has_item("fishing_rod"),
                        Jump("before_fishing"),
                        Jump("no_fish_rod")
                    )
                )
        ]

    imagebutton:
        focus_mask True
        pos (890,399)
        idle game.timer.image("objects/character_sploosh_01{}.png")
        hover HoverImage(game.timer.image("objects/character_sploosh_01{}.png"))
        action Hide("pier"), Jump("sploosh_button_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
