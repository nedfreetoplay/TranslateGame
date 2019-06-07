screen mrs_dewitts_office():
    use mods_screens_hook("mrs_dewitts_office")

    add game.timer.image("backgrounds/location_school_office2_day{}.jpg")

    if player.location.is_here(M_dewitt):
        imagebutton:
            focus_mask True
            if M_dewitt.is_state(S_dewitt_end):
                pos (230,441)
                idle game.timer.image("objects/character_dewitt_04{}.png")
                hover HoverImage(game.timer.image("objects/character_dewitt_04{}.png"))

            else:
                pos (582,361)
                idle "objects/character_dewitt_02.png"
                hover HoverImage("objects/character_dewitt_02.png")
            action Hide("mrs_dewitts_office"), Jump("dewitt_office_button_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("mrs_dewitts_office"), Jump("third_floor_dialogue")

screen dewitt_sex_options():
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("dewitt_sex_options"), Jump("dewitt_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("dewitt_sex_options"), Jump("dewitt_sex_cum")

    if anim_toggle:
        if M_dewitt.get("sex speed") < .175:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("dewitt_sex_options"), Function(M_dewitt.set, "sex speed", M_dewitt.get("sex speed") + 0.05), Jump("dewitt_sex_loop")

        if M_dewitt.get("sex speed") > .076:
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("dewitt_sex_options"), Function(M_dewitt.set, "sex speed", M_dewitt.get("sex speed") - 0.05), Jump("dewitt_sex_loop")

screen dewitt_twerk_options():
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/cam_stage01_01.png"
        hover HoverImage("buttons/cam_stage01_01.png")
        action Hide("dewitt_twerk_options"), Jump("dewitt_twerk_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/cam_stage01_02.png"
        hover HoverImage("buttons/cam_stage01_02.png")
        action Hide("dewitt_twerk_options"), Jump("dewitt_twerk_end")

    if M_dewitt.get('sex speed') < .125:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("dewitt_twerk_options"), Function(M_dewitt.set, "sex speed", M_dewitt.get("sex speed") + 0.05), Jump("dewitt_twerk_loop")

    if M_dewitt.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("dewitt_twerk_options"), Function(M_dewitt.set, "sex speed", M_dewitt.get("sex speed") - 0.05), Jump("dewitt_twerk_loop")

screen dewitt_office_bj_options():
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/cam_stage01_01.png"
        hover HoverImage("buttons/cam_stage01_01.png")
        action Hide("dewitt_office_bj_options"), Jump("dewitt_bj_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/cam_stage01_02.png"
        hover HoverImage("buttons/cam_stage01_02.png")
        action Hide("dewitt_office_bj_options"), Jump("dewitt_bj_cum")

    if M_dewitt.get("sex speed") < .125:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("dewitt_office_bj_options"), Function(M_dewitt.set, "sex speed", M_dewitt.get("sex speed") + 0.05), Jump("dewitt_bj_loop")

    if M_dewitt.get("sex speed") > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("dewitt_office_bj_options"), Function(M_dewitt.set, "sex speed", M_dewitt.get("sex speed") - 0.05), Jump("dewitt_bj_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
