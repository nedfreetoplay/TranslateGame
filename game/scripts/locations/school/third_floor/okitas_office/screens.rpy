screen mrs_okitas_office:
    add game.timer.image("backgrounds/location_school_office4_day{}.jpg")

    if not player.has_picked_up_item("goggles"):
        imagebutton:
            focus_mask True
            pos (126,471)
            idle "objects/object_goggles_01.png"
            hover HoverImage("objects/object_goggles_01.png")
            action Hide("mrs_okitas_office"), Jump("picked_up_goggles")

    if not player.has_picked_up_item("blueprints"):
        imagebutton:
            focus_mask True
            pos (250,577)
            idle "objects/object_blueprints_01.png"
            hover HoverImage("objects/object_blueprints_01.png")
            action Hide("mrs_okitas_office"), Jump("picked_up_blueprints")

    imagebutton:
        focus_mask True
        pos (451,442)
        idle game.timer.image("objects/object_chair_03{}.png")
        hover HoverImage(game.timer.image("objects/object_chair_03{}.png"))
        action NullAction()

    if player.location.is_here(M_okita):
        if M_okita.is_state(S_okita_xray_perving):
            imagebutton:
                focus_mask True
                pos (196,309)
                idle "objects/character_okita_02.png"
                hover HoverImage("objects/character_okita_02.png")
                action Hide("mrs_okitas_office"), Jump("button_okita_xray")

        if M_okita.is_state(S_okita_end):
            imagebutton:
                focus_mask True
                pos (486,415)
                idle "objects/character_okita_03.png"
                hover HoverImage("objects/character_okita_03.png")
                action Hide("mrs_okitas_office"), Jump("okita_pre_hscene_repeatable")

    imagebutton:
        focus_mask True
        pos (862,445)
        idle game.timer.image("objects/object_konterina_01{}.png")
        hover HoverImage(game.timer.image("objects/object_konterina_01{}.png"))
        action Hide("mrs_okitas_office"), Jump("konterina_button_dialogue")

    if not player.has_picked_up_item("labcoat"):
        imagebutton:
            focus_mask True
            pos (816,569)
            idle "objects/object_coat_01.png"
            hover HoverImage("objects/object_coat_01.png")
            action Hide("mrs_okitas_office"), Jump("picked_up_labcoat")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("mrs_okitas_office"), If(not M_okita.is_state(S_okita_get_items_from_office), true=Jump("third_floor_dialogue"), false=Jump("okitas_office_missing_items"))

screen okita_sex_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("okita_sex_options"), Jump("okita_h_scene_loop")

    imagebutton:
        focus_mask True
        pos (350,665)
        idle "buttons/ar_switch_01.png"
        hover HoverImage("buttons/ar_switch_01.png")
        action Hide("okita_sex_options"), Function(M_okita.toggle, "in augmented reality"), SetVariable("animated", False), Jump("okita_h_scene_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("okita_sex_options"), If(M_okita.is_set("repeatable unlocked"), Jump("okitas_office_hscene_cum"), Jump("okitas_office_hscene_aftermath"))

    if anim_toggle:
        if M_okita.get("sex speed") < .15:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("okita_sex_options"), Function(M_okita.set, "sex speed", M_okita.get("sex speed") + 0.05), Jump("okita_h_scene_loop")

        if M_okita.get("sex speed") > .051:
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("okita_sex_options"), Function(M_okita.set, "sex speed", M_okita.get("sex speed") - 0.05), Jump("okita_h_scene_loop")

label button_okita_xray:
    call expression game.dialog_select("okitas_office_okita_xray_perving")
    $ M_okita.trigger(T_okita_xray_perving_aftermath)

    $ game.timer.tick(2)
    $ player.go_to(L_map)
    $ game.main()
    return

screen okita_handjob_options:

    imagebutton:
        pos (250,700)
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("okita_handjob_options"), Jump("okita_handjob_loop")

    imagebutton:
        pos (450,700)
        focus_mask True
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("okita_handjob_options"), Jump("okita_handjob_cum")

    if M_okita.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("okita_handjob_options"), Function(M_okita.set, "sex speed", M_okita.get("sex speed") + 0.1), Jump("okita_handjob_loop")
            xpos 250
            ypos 735

    if M_okita.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("okita_handjob_options"), Function(M_okita.set, "sex speed", M_okita.get("sex speed") - 0.1), Jump("okita_handjob_loop")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
