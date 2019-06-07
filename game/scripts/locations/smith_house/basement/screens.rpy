screen smiths_basement():
    use mods_screens_hook("smiths_basement")

    add L_smith_basement.background

    imagebutton:
        focus_mask True
        pos (0,155)
        if L_smith_basement.locked:
            idle game.timer.image("objects/object_door_121{}.png")
        else:
            idle game.timer.image("objects/object_door_122{}.png")
        action NullAction()

    imagebutton:
        focus_mask True
        align 0.5,0.97
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("smiths_basement"), Jump("smiths_entrance_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
