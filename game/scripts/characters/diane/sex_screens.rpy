screen diane_cucumber_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("diane_cucumber_options"), Jump("diane_cucumber_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/cam_stage01_02.png"
        hover HoverImage("buttons/cam_stage01_02.png")
        action Hide("diane_cucumber_options"), Jump("diane_cucumber_cum")
        xpos 450
        ypos 700

    if M_diane.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("diane_cucumber_options"), Function(M_diane.set, "sex speed", M_diane.get("sex speed") + 0.1), Jump("diane_cucumber_loop")
            xpos 250
            ypos 735
    if M_diane.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("diane_cucumber_options"), Function(M_diane.set, "sex speed", M_diane.get("sex speed") - 0.1), Jump("diane_cucumber_loop")
            xpos 450
            ypos 735

screen diane_boobjob_options:
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("diane_boobjob_options"), Jump("diane_boobjob_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("diane_boobjob_options"), Jump("diane_boobjob_cum")
        xpos 450
        ypos 700

    if M_diane.get('sex speed') < .25:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("diane_boobjob_options"), Function(M_diane.set, "sex speed", M_diane.get("sex speed") + 0.05), Jump("diane_boobjob_loop")
            xpos 250
            ypos 735

    if M_diane.get('sex speed') > .16:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("diane_boobjob_options"), Function(M_diane.set, "sex speed", M_diane.get("sex speed") - 0.05), Jump("diane_boobjob_loop")
            xpos 450
            ypos 735

screen diane_sex_breed_options:

    imagebutton:
        pos (250,700)
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("diane_sex_breed_options"), Jump("diane_sex_breed_loop")

    imagebutton:
        pos (450,700)
        focus_mask True
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("diane_sex_breed_options"), Jump("diane_sex_breed_cum_pre")

    imagebutton:
        pos (370,665)
        idle "buttons/diane_stage01_04.png"
        hover HoverImage("buttons/diane_stage01_04.png")
        action Hide("diane_sex_breed_options"), Function(M_diane.toggle, "change angle"), SetVariable("animated", False), Jump("diane_sex_breed_loop")


    if M_diane.get('sex speed') < .09:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("diane_sex_breed_options"), Function(M_diane.set, "sex speed", M_diane.get("sex speed") + 0.03), Jump("diane_sex_breed_loop")
            xpos 250
            ypos 735

    if M_diane.get('sex speed') > .031:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("diane_sex_breed_options"), Function(M_diane.set, "sex speed", M_diane.get("sex speed") - 0.03), Jump("diane_sex_breed_loop")
            xpos 450
            ypos 735

screen diane_cum_breed_options:

    imagebutton:
        pos (250,700)
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("diane_cum_breed_options"), Jump("diane_sex_breed_cum_in")

    imagebutton:
        pos (450,700)
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("diane_cum_breed_options"), Jump("diane_sex_breed_cum_out")

screen diane_debbie_sex_options:
    imagebutton:
        pos (170,700)
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("diane_debbie_sex_options"), Jump("diane_debbie_sex_loop")

    imagebutton:
        pos (370,700)
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("diane_debbie_sex_options"), Function(M_diane.set, "cum inside", True), Jump("diane_debbie_sex_cum")

    imagebutton:
        pos (570,700)
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("diane_debbie_sex_options"), Function(M_diane.set, "cum inside", False), Jump("diane_debbie_sex_cum")

    imagebutton:
        pos (370,665)
        idle "buttons/roxxy_01.png"
        hover HoverImage("buttons/roxxy_01.png")
        action Hide("diane_debbie_sex_options"), Function(M_diane.toggle, "change partner"), Function(M_diane.set, "sex speed", .09), SetVariable("animated", False), Jump("diane_debbie_pre_sex_loop")

    if M_diane.get('sex speed') < .09:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("diane_debbie_sex_options"), Function(M_diane.set, "sex speed", M_diane.get("sex speed") + 0.03), Jump("diane_debbie_sex_loop")
            xpos 250
            ypos 735

    if M_diane.get('sex speed') > .031:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("diane_debbie_sex_options"), Function(M_diane.set, "sex speed", M_diane.get("sex speed") - 0.03), Jump("diane_debbie_sex_loop")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
