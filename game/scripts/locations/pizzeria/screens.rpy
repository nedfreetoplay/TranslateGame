screen pizzeria_exterior:
    add game.timer.image("backgrounds/location_pizza_outside_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (353,465)
        idle game.timer.image("objects/object_door_37{}.png")
        hover HoverImage(game.timer.image("objects/object_door_37{}.png"))
        if not game.timer.is_dark():
            action Hide("pizzeria_exterior"), Jump("pizza_interior_dialogue")
        else:
            action Hide("pizzeria_exterior"), Jump("pizza_closed")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
