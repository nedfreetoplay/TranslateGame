screen trailer_park():
    use mods_screens_hook("trailer_park")

    add L_trailerpark.background

    imagebutton:
        focus_mask True
        pos (3,327)
        idle game.timer.image("objects/object_shack_01{}.png")
        hover HoverImage(game.timer.image("objects/object_shack_01{}.png"))
        action Hide("trailer_park"), Function(renpy.call, "trailer_lock_check", "trailer_shack")

    imagebutton:
        focus_mask True
        pos (366,432)
        idle game.timer.image("objects/object_tractor_01{}.png")
        hover HoverImage(game.timer.image("objects/object_tractor_01{}.png"))
        action Hide("trailer_park"), Function(renpy.call, "trailer_lock_check", "trailer_tractor")

    imagebutton:
        focus_mask True
        pos (716,382)
        idle game.timer.image("objects/object_trailer_01{}.png")
        hover HoverImage(game.timer.image("objects/object_trailer_01{}.png"))
        action Hide("trailer_park"), Function(renpy.call, "trailer_lock_check", "trailer")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
