screen mrs_bissettes_office():
    use mods_screens_hook("mrs_bissettes_office")

    add game.timer.image("backgrounds/location_school_office1_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (547,464)


        idle "objects/object_chair_04.png"
        hover HoverImage("objects/object_chair_04.png")
        action NullAction()

    if player.location.is_here(M_bissette):
        imagebutton:
            focus_mask True
            if M_bissette.is_set("night visit") and game.timer.is_dark():
                pos (210,302)
                idle game.timer.image("objects/character_bissette_03{}.png")
                hover HoverImage(game.timer.image("objects/character_bissette_03{}.png"))

            else:
                pos (633,312)
                idle "objects/character_bissette_02.png"
                hover HoverImage("objects/character_bissette_02.png")
            action Hide("mrs_bissettes_office"), Jump("bissette_office_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("mrs_bissettes_office"), Jump("third_floor_dialogue")

screen bissettes_office_sex_options():
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("bissettes_office_sex_options"), Jump("bissettes_office_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("bissettes_office_sex_options"), Jump("bissettes_office_sex_cum")

    if M_bissette.get("sex speed") < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("bissettes_office_sex_options"), Function(M_bissette.set, "sex speed", M_bissette.get("sex speed") + 0.05), Jump("bissettes_office_sex_loop")

    if M_bissette.get("sex speed") > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("bissettes_office_sex_options"), Function(M_bissette.set, "sex speed", M_bissette.get("sex speed") - 0.05), Jump("bissettes_office_sex_loop")

    imagebutton:
        pos (370,665)
        idle "buttons/diane_stage01_04.png"
        hover HoverImage("buttons/diane_stage01_04.png")
        action Hide("bissettes_office_sex_options"), Function(M_bissette.toggle, "change angle"), SetVariable("animated", False), If(M_bissette.is_set("change angle"), Jump("bissettes_office_sex_intro"), Jump("bissettes_office_chair_sex_intro"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
