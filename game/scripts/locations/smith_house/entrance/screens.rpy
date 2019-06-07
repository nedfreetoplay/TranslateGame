screen smiths_entrance():
    use mods_screens_hook("smiths_entrance")

    add L_smith_entrance.background

    imagebutton:
        focus_mask True
        pos (185,226)
        idle game.timer.image("objects/object_stairs_10{}.png")
        hover HoverImage(game.timer.image("objects/object_stairs_10{}.png"))
        action Hide("smiths_entrance"), Jump("smiths_hallway_dialogue")

    imagebutton:
        focus_mask True
        pos (919,385)
        idle game.timer.image("objects/object_door_120{}.png")
        hover HoverImage(game.timer.image("objects/object_door_120{}.png"))
        action Hide("smiths_entrance"), Jump("smiths_basement_dialogue")

    imagebutton:
        focus_mask True
        align 0.5,0.97
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("smiths_entrance"), Jump("smiths_frontyard_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
