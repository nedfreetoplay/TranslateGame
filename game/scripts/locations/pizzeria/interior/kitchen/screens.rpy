screen pizzeria_kitchen:
    add L_pizzeria_kitchen.background

    imagebutton:
        focus_mask True
        pos (142,307)
        idle game.timer.image("objects/object_door_127{}.png")
        hover HoverImage(game.timer.image("objects/object_door_127{}.png"))
        action Hide("pizzeria_kitchen"), Jump("pizza_interior_dialogue")

    imagebutton:
        focus_mask True
        pos (386,316)
        idle game.timer.image("objects/object_door_126{}.png")
        hover HoverImage(game.timer.image("objects/object_door_126{}.png"))
        action Hide("pizzeria_kitchen"), Jump("pizzeria_storage_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
