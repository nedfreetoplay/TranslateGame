screen mrs_ross_office():
    use mods_screens_hook("mrs_ross_office")

    add game.timer.image("backgrounds/location_school_office3_day{}.jpg")

    if player.location.is_here(M_ross):
        if (M_ross.is_state(S_ross_paint_with_body) and game.timer.is_evening()) or M_ross.is_state(S_ross_end):
            imagebutton:
                focus_mask True
                pos (89,542)
                idle game.timer.image("objects/character_ross_03{}.png")
                hover HoverImage(game.timer.image("objects/character_ross_03{}.png"))
                action Hide("mrs_ross_office"), Jump("button_ross_office_dialogue")
        else:
            imagebutton:
                focus_mask True
                pos (560,463)
                idle "objects/character_ross_02.png"
                hover HoverImage("objects/character_ross_02.png")
                action Hide("mrs_ross_office"), Jump("button_ross_office_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("mrs_ross_office"), Jump("third_floor_dialogue")

screen ross_sex_options():
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("ross_sex_options"), Jump("ross_hscene_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("ross_sex_options"), Jump("ross_office_ross_sex_cum")

    if anim_toggle:
        if M_ross.get("sex speed") < .15:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("ross_sex_options"), Function(M_ross.set, "sex speed", M_ross.get("sex speed") + 0.05), Jump("ross_hscene_loop")

        if M_ross.get("sex speed") > .06:
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("ross_sex_options"), Function(M_ross.set, "sex speed", M_ross.get("sex speed") - 0.05), Jump("ross_hscene_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
