screen boat_cabin():
    use mods_screens_hook("boat_cabin")

    add L_boat_cabin.background

    imagebutton:
        focus_mask True
        pos (175,273)
        idle game.timer.image("objects/object_door_141{}.png")
        hover HoverImage(game.timer.image("objects/object_door_141{}.png"))
        action MoveTo(L_boat_bridge)

    imagebutton:
        focus_mask True
        pos (952,406)
        idle game.timer.image("objects/object_nuke_01{}.png")
        hover HoverImage(game.timer.image("objects/object_nuke_01{}.png"))
        action Jump("nuke_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
