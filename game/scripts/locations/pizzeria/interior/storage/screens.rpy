screen pizzeria_storage:
    add L_pizzeria_storage.background

    imagebutton:
        focus_mask True
        pos (68,226)
        idle game.timer.image("objects/object_door_128{}.png")
        hover HoverImage(game.timer.image("objects/object_door_128{}.png"))
        action Hide("pizzeria_storage"), Jump("pizzeria_kitchen_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
