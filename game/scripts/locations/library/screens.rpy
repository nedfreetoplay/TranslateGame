screen library_front():
    use mods_screens_hook("library_front")

    add game.timer.image("backgrounds/location_library_front_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (364,486)
        idle game.timer.image("objects/object_door_105{}.png")
        hover HoverImage(game.timer.image("objects/object_door_105{}.png"))
        action Hide("library_front"), Function(playSound), Jump("library_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
