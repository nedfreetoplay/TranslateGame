screen pizzeria_interior:
    add L_pizzeria_interior.background

    if M_tony.is_state(S_tony_end):
        imagebutton:
            focus_mask True
            pos (163,256)
            idle "objects/character_tony_01.png"
            hover HoverImage("objects/character_tony_01.png")
            action Hide("pizzeria_interior"), Jump("tony_dialogue")

    if M_tony.get("deliver"):
        imagebutton:
            focus_mask True
            pos (380,400)
            idle "objects/object_pizza_01.png"
            hover HoverImage("objects/object_pizza_01.png")
            action Hide("pizzeria_interior"), Jump("pizza_minigame")
    imagebutton:
        focus_mask True
        pos (0,223)
        idle game.timer.image("objects/object_door_125{}.png")
        hover HoverImage(game.timer.image("objects/object_door_125{}.png"))
        action Hide("pizzeria_interior"), Jump("pizzeria_kitchen_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_08.png"
        hover HoverImage("boxes/auto_option_08.png")
        action Hide("pizzeria_interior"), Jump("pizza_exterior_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
