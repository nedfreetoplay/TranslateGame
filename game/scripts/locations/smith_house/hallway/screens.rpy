screen smiths_hallway():
    use mods_screens_hook("smiths_hallway")

    add L_smith_hallway.background

    imagebutton:
        focus_mask True
        align 0.5,0.97
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("smiths_hallway"), Jump("smiths_entrance_dialogue")

    imagebutton:
        focus_mask True
        pos (396,271)
        idle game.timer.image("objects/object_door_123{}.png")
        hover HoverImage(game.timer.image("objects/object_door_123{}.png"))
        action Hide("smiths_hallway"), Jump("smiths_bedroom_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
