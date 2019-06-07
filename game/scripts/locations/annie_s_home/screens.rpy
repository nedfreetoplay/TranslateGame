screen annies_house_front():
    use mods_screens_hook("annies_house_front")

    add L_annie_front.background

    imagebutton:
        focus_mask True
        pos (236,371)
        idle game.timer.image("objects/object_door_132{}.png")
        hover HoverImage(game.timer.image("objects/object_door_132{}.png"))
        action MoveTo(L_annie_livingroom)

    imagebutton:
        focus_mask True
        pos (648,364)
        idle game.timer.image("objects/object_door_133{}.png")
        hover HoverImage(game.timer.image("objects/object_door_133{}.png"))
        action MoveTo(L_annie_daycare)

    if L_annie_front.is_here(M_richard):
        imagebutton:
            focus_mask True
            pos (381,385)
            idle "objects/character_richard_02.png"
            hover HoverImage("objects/character_richard_02.png")
            action TalkTo(M_richard)

screen annies_house_livingroom():
    use mods_screens_hook("annies_house_livingroom")

    add L_annie_livingroom.background

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_annie_front)

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
            action TalkTo(M_annie)

    if L_annie_livingroom.is_here(M_richard):
        imagebutton:
            focus_mask True
            pos (196,381)
            idle "objects/character_richard_01.png"
            hover HoverImage("objects/character_richard_01.png")
            action TalkTo(M_richard)

    if L_annie_livingroom.is_here(M_lucy):
        imagebutton:
            focus_mask True
            pos (498,377)
            idle "objects/character_lucy_01.png"
            hover HoverImage("objects/character_lucy_01.png")
            action TalkTo(M_lucy)

screen annies_house_daycare():
    use mods_screens_hook("annies_house_daycare")

    add L_annie_daycare.background

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_annie_front)

    if L_annie_daycare.is_here(M_lucy):
        imagebutton:
            focus_mask True
            pos (773,325)
            idle "objects/character_lucy_02.png"
            hover HoverImage("objects/character_lucy_02.png")
            action TalkTo(M_lucy)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
