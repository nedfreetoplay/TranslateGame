screen daisy_sex_breed_options():
    imagebutton:
        pos (170,700)
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("daisy_sex_breed_options"), Jump("daisy_sex_breed_loop")

    imagebutton:
        pos (370,700)
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("daisy_cum_breed_options"), Jump("daisy_sex_breed_cum_in")

    imagebutton:
        pos (570,700)
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("daisy_cum_breed_options"), Jump("daisy_sex_breed_cum_out")

    imagebutton:
        pos (370,665)
        idle "buttons/diane_stage01_04.png"
        hover HoverImage("buttons/diane_stage01_04.png")
        action Hide("daisy_sex_breed_options"), Function(M_daisy.toggle, "change angle"), SetVariable("animated", False), Jump("daisy_sex_breed_loop")


    if M_daisy.get('sex speed') < .09:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("daisy_sex_breed_options"), Function(M_daisy.set, "sex speed", M_daisy.get("sex speed") + 0.03), Jump("daisy_sex_breed_loop")
            xpos 250
            ypos 735

    if M_daisy.get('sex speed') > .031:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("daisy_sex_breed_options"), Function(M_daisy.set, "sex speed", M_daisy.get("sex speed") - 0.03), Jump("daisy_sex_breed_loop")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
