screen mayor_rumps_frontyard():
    use mods_screens_hook("mayor_rumps_frontyard")

    add L_rump_front.background
    imagebutton:
        focus_mask True
        pos (854, 398)
        idle game.timer.image("objects/object_door_142{}.png")
        hover HoverImage(game.timer.image("objects/object_door_142{}.png"))
        action Hide("mayor_rumps_frontyard"), Jump("mayor_rumps_house_locked")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
