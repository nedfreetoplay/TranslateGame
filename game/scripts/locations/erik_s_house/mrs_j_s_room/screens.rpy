screen mrs_johnsons_room():
    use mods_screens_hook("mrs_johnsons_room")

    add game.timer.image("backgrounds/location_erik_house_upstairs_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (696,498)
        idle game.timer.image("objects/object_ball_01{}.png")
        hover HoverImage(game.timer.image("objects/object_ball_01{}.png"))
        action Hide("mrs_johnsons_room"), Jump("mrsj_ball")

    if player.location.is_here(M_mrsj):
        if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
            imagebutton:
                focus_mask True
                pos (826,300)
                idle "objects/character_mrsj_03.png"
                hover HoverImage("objects/character_mrsj_03.png")
                action Hide("mrs_johnsons_room"), Jump("mrsj_button_dialogue")

        elif game.timer.is_dark() and erik.over(erik_gf):
            imagebutton:
                focus_mask True
                pos (250,420)
                idle "objects/character_mrsj_04.png"
                hover HoverImage("objects/character_mrsj_04.png")
                action Hide("mrs_johnsons_room"), Jump("mrsj_button_dialogue")

        else:
            imagebutton:
                focus_mask True
                pos (0,410)
                idle game.timer.image("objects/object_bed_04_day{}.png")
                hover HoverImage(game.timer.image("objects/object_bed_04_day{}.png"))
                action Hide("mrs_johnsons_room"), Jump("mrsj_button_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("mrs_johnsons_room"), Jump("erik_indoors")

screen erimom_private_pos1_sex_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Jump("mrsj_private_yoga_pos1_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/johnson_01.png"
        hover HoverImage("buttons/johnson_01.png")
        action Jump("erimom_private_pos1_switch")
        xpos 450
        ypos 700

    if M_mrsj.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Jump("erimom_private_pos1_slower_sex")
            xpos 250
            ypos 735

    if M_mrsj.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Jump("erimom_private_pos1_faster_sex")
            xpos 450
            ypos 735

screen erimom_private_pos2_sex_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Jump("mrsj_private_yoga_pos2_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Jump("erimom_private_pos2_cum")
        xpos 450
        ypos 700

    if M_mrsj.get('sex speed') < .3:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Jump("erimom_private_pos2_slower_sex")
            xpos 250
            ypos 735

    if M_mrsj.get('sex speed') > .11:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Jump("erimom_private_pos2_faster_sex")
            xpos 450
            ypos 735

screen mrsj_3some_pos1_sex_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Jump("mrsj_3some_pos1_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/johnson_01.png"
        hover HoverImage("buttons/johnson_01.png")
        action Jump("mrsj_3some_pos1_switch")
        xpos 450
        ypos 700

    if M_mrsj.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Jump("mrsj_3some_pos1_slower_sex")
            xpos 250
            ypos 735

    if M_mrsj.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Jump("mrsj_3some_pos1_faster_sex")
            xpos 450
            ypos 735

screen mrsj_3some_pos2_sex_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Jump("mrsj_3some_pos2_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Jump("mrsj_3some_pos2_cum")
        xpos 450
        ypos 700

    if M_mrsj.get('sex speed') < .3:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Jump("mrsj_3some_pos2_slower_sex")
            xpos 250
            ypos 735

    if M_mrsj.get('sex speed') > .11:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Jump("mrsj_3some_pos2_faster_sex")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
