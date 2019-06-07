screen eriks_house_entrance() tag eriks_house:


    add game.timer.image("backgrounds/location_erik_house_inside_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (401,40)
        idle game.timer.image("objects/object_door_30{}.png")
        hover HoverImage(game.timer.image("objects/object_door_30{}.png"))
        action If(
            not erik.completed(erik_breastfeeding),
            [Hide("eriks_house_entrance"), Jump("mrsj_room_locked_dialogue")],
            If(
                erik.over(erik_path_split) and erik.started(erik_sex_ed),
                [Hide("eriks_house_entrance"), Jump("erikentrance_erik_sex_ed_block")],
                If(
                    mrsj_filled,
                    [Hide("eriks_house_entrance"), Jump("mrsj_filled_block")],
                    [Hide("eriks_house_entrance"), Function(playSound), Play("audio", sfxDoor()), Jump("mrsj_room")],
                )
            )
        )

    imagebutton:
        focus_mask True
        pos (340,0)
        idle game.timer.image("objects/object_door_68{}.png")
        hover HoverImage(game.timer.image("objects/object_door_68{}.png"))
        action If(
                   erik_funky and L_erikhouse_erikroom.is_here(M_june),
                   [Hide("eriks_house_entrance"), Jump("erik_funky_block")],
                   [Hide("eriks_house_entrance"), Function(playSound), Play("audio", sfxDoor()), Jump("erik_room_dialogue")],
               )

    imagebutton:
        focus_mask True
        pos (576,325)
        idle game.timer.image("objects/object_door_31{}.png")
        hover HoverImage(game.timer.image("objects/object_door_31{}.png"))
        action Hide("eriks_house_entrance"), Function(playSound), Play("audio", sfxDoor()), Jump("erik_basement")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_08.png"
        hover HoverImage("boxes/auto_option_08.png")
        action Hide("eriks_house_entrance"), Jump(game.dialog_select("erik_house_dialogue"))

    if player.location.is_here(M_mrsj):
        imagebutton:
            focus_mask True
            pos (700,300)
            idle "objects/character_mrsj_01.png"
            hover HoverImage("objects/character_mrsj_01.png")
            action Hide("eriks_house_entrance"), Jump("mrsj_button_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
