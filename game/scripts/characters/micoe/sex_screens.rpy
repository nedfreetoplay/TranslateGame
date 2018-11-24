screen micoe_bj_options:

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("micoe_bj_options"), Jump("micoe_bj_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("micoe_bj_options"), Jump("micoe_bj_cum")
        xpos 450
        ypos 700

    if M_micoe.get('sex speed') < .12:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("micoe_bj_options"), Function(M_micoe.set, "sex speed", M_micoe.get("sex speed") + 0.03), Jump("micoe_bj_loop")
            xpos 250
            ypos 735

    if M_micoe.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("micoe_bj_options"), Function(M_micoe.set, "sex speed", M_micoe.get("sex speed") - 0.03), Jump("micoe_bj_loop")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
