screen shower:
    $ player.go_to(L_home_shower)
    add game.timer.image("backgrounds/location_home_shower_02{}.jpg")

    if M_mom.get_state() == S_mom_fetch_towel and not player.has_item("towel"):
        imagebutton:
            focus_mask True
            pos (657,370)
            idle "objects/object_towel_01.png"
            hover HoverImage("objects/object_towel_01.png")
            action Function(player.get_item, "towel"), Show("popup", Image = "boxes/popup_item_towel1.png")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_01.png"
        hover HoverImage("boxes/auto_option_01.png")
        action Hide("shower"), Jump("hallway_dialogue")

screen shower_sex_buttons:
    imagebutton:
        focus_mask True
        pos (940,600)
        if xray:
            idle "buttons/anim_03.png"
            hover HoverImage("buttons/anim_03.png")
        else:
            idle "buttons/anim_04.png"
            hover HoverImage("buttons/anim_04.png")
        action If(
            xray,
            SetVariable("xray", False),
            SetVariable("xray", True)
        )

    imagebutton:
        focus_mask True
        pos (10,600)
        if anim_toggle:
            idle "buttons/anim_02.png"
            hover HoverImage("buttons/anim_02.png")
        else:
            idle "buttons/anim_01.png"
            hover HoverImage("buttons/anim_01.png")
        action [
            If(
                anim_toggle,
                [SetVariable("anim_toggle", False),SetVariable("animated", False)],
                SetVariable("anim_toggle", True)
            ),
            Return
        ]

screen shower_mom_sex_options:
    imagebutton:
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("shower_mom_sex_options"), Jump("mom_shower_sex_loop")

    imagebutton:
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("shower_mom_sex_options"), Jump("mom_shower_sex_cum")

    if anim_toggle:
        if M_mom.get("sex speed") < .4:
            imagebutton:
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("shower_mom_sex_options"), Function(M_mom.set, "sex speed", M_mom.get('sex speed') + 0.1), Jump("mom_shower_sex_loop")

        if M_mom.get("sex speed") > .21:
            imagebutton:
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("shower_mom_sex_options"), Function(M_mom.set, "sex speed", M_mom.get('sex speed') - 0.1), Jump("mom_shower_sex_loop")

screen sis_shower_sex_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("sis_shower_sex_options"), Jump(game.dialog_select("sis_shower_sex_loop"))

    if store._in_replay == None and player.stats.str() < 7:
        imagebutton:
            focus_mask True
            pos (450,700)
            idle "buttons/diane_stage01_02.png"
            hover HoverImage("buttons/diane_stage01_02.png")
            action Hide("sis_shower_sex_options"), Jump(game.dialog_select("sis_shower_sex_cum_1"))

    if not store._in_replay == None or player.stats.str() >= 7:
        imagebutton:
            focus_mask True
            pos (450,700)
            idle "buttons/diane_stage01_02.png"
            hover HoverImage("buttons/diane_stage01_02.png")
            action Hide("sis_shower_sex_options"), Jump(game.dialog_select("sis_shower_sex_cum_2"))

    if M_jenny.get("sex speed") < .4:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("sis_shower_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.1), Jump(game.dialog_select("sis_shower_sex_loop"))

    if M_jenny.get("sex speed") > .21:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("sis_shower_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.1), Jump(game.dialog_select("sis_shower_sex_loop"))


screen debbie_shower_blowjob_options:

    imagebutton:
        pos (170,700)
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("debbie_shower_blowjob_options"), Jump("debbie_shower_blowjob_loop")

    imagebutton:
        pos (370,700)
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("debbie_shower_blowjob_options"), Jump("debbie_shower_blowjob_cum_in")

    imagebutton:
        pos (570,700)
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("debbie_shower_blowjob_options"), Jump("debbie_shower_blowjob_cum_out")

    if M_mom.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("debbie_shower_blowjob_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") + 0.1), Jump("debbie_shower_blowjob_loop")
            xpos 250
            ypos 735

    if M_mom.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("debbie_shower_blowjob_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") - 0.1), Jump("debbie_shower_blowjob_loop")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
