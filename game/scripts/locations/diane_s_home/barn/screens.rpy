screen dianes_barn_building:
    add L_diane_barn_building.background
    if L_diane_barn_building.is_here(M_diane):
        imagebutton:
            focus_mask True
            pos (635,506)
            idle "objects/character_diane_shirtless_construction.png"
            hover HoverImage("objects/character_diane_shirtless_construction.png")
            action Hide("dianes_barn_building"), Jump("aunt_button_dialogue")

screen dianes_barn:
    add L_diane_barn.background

    imagebutton:
        focus_mask True
        pos (563,482)
        idle game.timer.image("objects/object_door_107{}.png")
        hover HoverImage(game.timer.image("objects/object_door_107{}.png"))
        action Hide("dianes_barn"), Jump("barn_garden_dialogue")

    imagebutton:
        focus_mask True
        pos (247,472)
        idle game.timer.image("objects/object_door_134{}.png")
        hover HoverImage(game.timer.image("objects/object_door_134{}.png"))
        action Hide("dianes_barn"), Jump("barn_dialogue")

screen dianes_barn_interior:
    add L_diane_barn_interior.background
    if player.location.is_here(M_daisy):
        if game.timer.is_dark():
            imagebutton:
                focus_mask True
                pos (44,46)
                idle "objects/character_daisy_sleeping.png"
                hover HoverImage("objects/character_daisy_sleeping.png")
                action TalkTo("daisy")
        else:
            imagebutton:
                focus_mask True
                if M_daisy.pregnancy.gave_birth:
                    pos (27,413)
                    idle "objects/character_daisy_baby_" + M_daisy.pregnancy.baby_gender +".png"
                    hover HoverImage("objects/character_daisy_baby_" + M_daisy.pregnancy.baby_gender +".png")
                else:
                    pos (27,413)
                    idle "objects/character_daisy_[M_daisy.get_naked_str][M_daisy.pregnancy.to_string].png"
                    hover HoverImage("objects/character_daisy_" + M_daisy.get_naked_str + M_daisy.pregnancy.to_string + ".png")
                action TalkTo("daisy")
    imagebutton:
        focus_mask True
        pos (929,364)
        idle game.timer.image("objects/object_door_138{}.png")
        hover HoverImage(game.timer.image("objects/object_door_138{}.png"))
        action Hide("dianes_barn_interior"), Jump("barn_garden_dialogue")

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("dianes_barn_interior"), Jump("barn_front_dialogue")

    if player.location.is_here(M_diane):
        imagebutton:
            focus_mask True
            if M_diane.pregnancy.gave_birth:
                pos (715,375)
                idle "objects/character_diane_casual_" + M_diane.pregnancy.baby_gender +".png"
                hover HoverImage("objects/character_diane_casual_" + M_diane.pregnancy.baby_gender +".png")
            else:
                pos (613,357)
                idle "objects/character_diane_[M_diane.get_naked_str][M_diane.pregnancy.to_string].png"
                hover HoverImage("objects/character_diane_" + M_diane.get_naked_str + M_diane.pregnancy.to_string + ".png")
            action Hide("dianes_barn_interior"), Jump("aunt_button_dialogue")

screen dianes_barn_garden:
    add L_diane_barn_garden.background

    imagebutton:
        focus_mask True
        pos (55,395)
        idle game.timer.image("objects/object_door_135{}.png")
        hover HoverImage(game.timer.image("objects/object_door_135{}.png"))
        action Hide("dianes_barn_garden"), Jump("barn_dialogue")

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("dianes_barn_garden"), Jump("barn_front_dialogue")

    imagebutton:
        focus_mask True
        pos (686,315)
        idle game.timer.image("objects/object_door_09{}_02.png")
        hover HoverImage(game.timer.image("objects/object_door_09{}_02.png"))
        action Hide("dianes_barn_garden"), Function(playSound), Jump(game.dialog_select("shed"))

    imagebutton:
        focus_mask True
        if not game.timer.is_dark():
            pos (928,420)
        else:
            pos (928,416)
        idle game.timer.image("objects/object_crack_01{}.png")
        hover HoverImage(game.timer.image("objects/object_crack_01{}.png"))
        action Hide("dianes_barn_garden"), Jump("church_graveyard_dialogue")

    if M_daisy.is_state(S_daisy_assembled_statue, S_daisy_viewed_statue):
        imagebutton:
            focus_mask True
            pos (150,496)
            idle "objects/object_statue_garden_01.png"
            hover HoverImage("objects/object_statue_garden_01.png")
            action Hide("dianes_barn_garden"), Jump("barn_garden_statue_dialogue")

    imagebutton:
        focus_mask True
        pos (36,535)
        idle game.timer.image("objects/object_garden_01{}.png")
        hover HoverImage(game.timer.image("objects/object_garden_01{}.png"))
        action Show("garden01_options")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
