screen annies_house_front:
    add L_annie_front.background

    imagebutton:
        focus_mask True
        pos (236,371)
        idle game.timer.image("objects/object_door_132{}.png")
        hover HoverImage(game.timer.image("objects/object_door_132{}.png"))
        action Hide("annies_house_front"), Jump("annies_house_livingroom_dialogue")

    imagebutton:
        focus_mask True
        pos (648,364)
        idle game.timer.image("objects/object_door_133{}.png")
        hover HoverImage(game.timer.image("objects/object_door_133{}.png"))
        action Hide("annies_house_front"), Jump("annies_house_daycare_dialogue")

    if L_annie_front.is_here(M_richard):
        imagebutton:
            focus_mask True
            pos (381,385)
            idle "objects/character_richard_02.png"
            hover HoverImage("objects/character_richard_02.png")
            action Hide("annies_house_front"), Jump("richard_button_dialogue")

screen annies_house_livingroom:
    add L_annie_livingroom.background

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("annies_house_livingroom"), Jump("annies_house_front_dialogue")

    if M_diane.is_state(S_diane_help_annie):
        if not player.has_item("hammer"):
            imagebutton:
                focus_mask True
                pos (167,312)
                idle game.timer.image("objects/object_hammer_01{}.png")
                hover HoverImage(game.timer.image("objects/object_hammer_01{}.png"))
                action Hide("annies_house_livingroom"), Jump("annies_house_get_hammer")

        if not player.has_item("handsaw"):
            imagebutton:
                focus_mask True
                pos (140,480)
                idle game.timer.image("objects/object_saw_01{}.png")
                hover HoverImage(game.timer.image("objects/object_saw_01{}.png"))
                action Hide("annies_house_livingroom"), Jump("annies_house_get_saw")

    if L_annie_livingroom.is_here(M_annie):
        imagebutton:
            focus_mask True
            pos (784,417)
            idle "objects/character_annie_03.png"
            hover HoverImage("objects/character_annie_03.png")
            action Hide("annies_house_livingroom"), Jump("annie_button_home_dialogues")

    if L_annie_livingroom.is_here(M_richard):
        imagebutton:
            focus_mask True
            pos (196,381)
            idle "objects/character_richard_01.png"
            hover HoverImage("objects/character_richard_01.png")
            action Hide("annies_house_livingroom"), Jump("richard_button_dialogue")

    if L_annie_livingroom.is_here(M_lucy):
        imagebutton:
            focus_mask True
            pos (498,377)
            idle "objects/character_lucy_01.png"
            hover HoverImage("objects/character_lucy_01.png")
            action Hide("annies_house_livingroom"), Jump("lucy_button_dialogue")

screen annies_house_daycare:
    add L_annie_daycare.background

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("annies_house_daycare"), Jump("annies_house_front_dialogue")

    if L_annie_daycare.is_here(M_lucy):
        imagebutton:
            focus_mask True
            pos (773,325)
            idle "objects/character_lucy_02.png"
            hover HoverImage("objects/character_lucy_02.png")
            action Hide("annies_house_daycare"), Jump("lucy_button_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
