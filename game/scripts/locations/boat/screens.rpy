screen boat_bridge():
    use mods_screens_hook("boat_bridge")

    add L_boat_bridge.background

    imagebutton:
        focus_mask True
        pos (679,278)
        idle game.timer.image("objects/object_door_140{}.png")
        hover HoverImage(game.timer.image("objects/object_door_140{}.png"))
        action MoveTo(L_boat_cabin)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
