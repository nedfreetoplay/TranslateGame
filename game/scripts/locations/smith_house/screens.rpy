screen smiths_frontyard():
    use mods_screens_hook("smiths_frontyard")

    add L_smith_front.background

    imagebutton:
        focus_mask True
        pos (509,451)
        idle game.timer.image("objects/object_door_119{}.png")
        hover HoverImage(game.timer.image("objects/object_door_119{}.png"))
        action Hide("smiths_frontyard"), Jump("smiths_entrance_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
