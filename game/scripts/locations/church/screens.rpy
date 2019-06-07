screen church():
    use mods_screens_hook("church")

    if game.timer.is_weekend() and game.timer.is_morning():
        if player.location.is_here(M_helen, M_harold):
            add "backgrounds/location_church_full01_day.jpg"

        elif player.location.is_here(M_helen):
            add "backgrounds/location_church_full02_day.jpg"

        else:
            add "backgrounds/location_church_full03_day.jpg"

    else:
        add game.timer.image("backgrounds/location_church_day{}.jpg")

    if player.location.is_here(M_angelica):
        imagebutton:
            focus_mask True
            pos (810,380)
            idle "objects/character_angelica_01.png"
            hover HoverImage("objects/character_angelica_01.png")
            action Hide("church"), Jump("angelica_dialogue")

    imagebutton:
        focus_mask True
        pos (281,367)
        idle game.timer.image("objects/object_door_47{}.png")
        hover HoverImage(game.timer.image("objects/object_door_47{}.png"))
        action Hide("church"), Jump("confessional_left")

    imagebutton:
        focus_mask True
        pos (440,368)
        idle game.timer.image("objects/object_door_48{}.png")
        hover HoverImage(game.timer.image("objects/object_door_48{}.png"))
        action Hide("church"), Play("audio", sfxDoor()), Jump("confessional_right")

    imagebutton:
        focus_mask True
        pos (287,169)
        idle game.timer.image("objects/object_door_71{}.png")
        hover HoverImage(game.timer.image("objects/object_door_71{}.png"))
        action Hide("church"), Function(playSound), Play("audio", sfxDoor()), Jump("church_stairs_dialogue")

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("church"), Jump("church_front_dialogue")

screen church_front():
    use mods_screens_hook("church_front")

    add L_church_front.background
    imagebutton:
        focus_mask True
        pos (388,335)
        idle game.timer.image("objects/object_door_115{}.png")
        hover HoverImage(game.timer.image("objects/object_door_115{}.png"))
        action Hide("church_front"), Function(playSound), Play("audio", sfxDoor()), Jump("church_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
