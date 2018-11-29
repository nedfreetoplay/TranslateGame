screen master_bedroom:
    add game.timer.image("backgrounds/location_home_debbiebedroom_day{}.jpg")

    if L_home_mombedroom.is_here(M_diane) and not M_diane.pregnancy:
        imagebutton:
            focus_mask True
            pos (532,405)
            idle "objects/character_diane_nightgown_bed_duo.png"
            hover HoverImage("objects/character_diane_nightgown_bed_duo.png")
            action Hide("master_bedroom"), Jump("diane_debbie_3way_dialogue")

    elif M_mom.is_set("sex available") and L_home_mombedroom.is_here(M_mom) and not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (550,400)
            idle "objects/character_debbie_03.png"
            hover HoverImage("objects/character_debbie_03.png")
            action Hide("master_bedroom"), Jump("mom_dialogue_button_room")

    elif M_mom.is_set("panties taken") or (game.timer.is_dark() and L_home_mombedroom.is_here(M_mom) and (M_mom.get("sex available") or M_mom.is_state(S_mom_sleepover) or not M_mom.get("bed locked"))):
        imagebutton:
            focus_mask True
            pos (435,435)
            idle game.timer.image("objects/object_bed_03{}.png")
            hover HoverImage(game.timer.image("objects/object_bed_03{}.png"))
            action Hide("master_bedroom"), Jump("mom_bed")

    if M_mom.is_state(S_mom_fetch_laundry):
        imagebutton:
            focus_mask True
            pos (247,517)
            idle "objects/object_laundry_01.png"
            hover HoverImage("objects/object_laundry_01.png")
            action Hide("master_bedroom"), Jump("mom_room_laundry")

    imagebutton:
        focus_mask True
        pos (0,459)
        idle game.timer.image("objects/object_desk_07{}.png")
        hover HoverImage(game.timer.image("objects/object_desk_07{}.png"))
        action Show("desk07_options")

    if not M_mom.is_set("panties taken"):
        imagebutton:
            focus_mask True
            align (0.5,0.97)
            idle "boxes/auto_option_12.png"
            hover HoverImage("boxes/auto_option_12.png")
            action Hide("master_bedroom"), Function(renpy.call, "home_lock_check", "Living Room", "home_livingroom_dialogue")

screen moms_drawer:
    add game.timer.image("backgrounds/location_home_debbiedrawer_day{}.jpg")

    if M_mom.is_set("fetch lotion"):
        if not M_mom.is_set("retrieved lotion"):
            imagebutton:
                focus_mask True
                pos (562,295)
                idle "objects/object_lotion_01.png"
                hover HoverImage("objects/object_lotion_01.png")
                action Function(player.get_item, "lotion"), Function(M_mom.set, "retrieved lotion", True)

    elif M_mom.is_set("panties available") and not M_mom.is_set("panties taken") and not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (-4,283)
            idle "objects/object_panties_02.png"
            hover HoverImage("objects/object_panties_02.png")
            action Hide("moms_drawer"), Jump("mom_drawer_panties")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("moms_drawer"), Jump("mom_bedroom_screen")

screen desk07_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("desk07_options")

    imagebutton:
        focus_mask True
        align (0.5,0.82)
        idle "boxes/desk07_option_01.png"
        hover HoverImage("boxes/desk07_option_01.png")
        action Hide("desk07_options"), Hide("master_bedroom"), Jump("mom_drawer")

screen mom_sex_options:
    imagebutton:
        if mom_sex_position == "missionary":
            pos (50,700)

        elif mom_sex_position in ["cowgirl", "suck tits"]:
            pos (-30,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("mom_sex_options"), Jump("mom_sex_loop")

    imagebutton:
        if mom_sex_position == "missionary":
            pos (250,700)

        elif mom_sex_position in ["cowgirl", "suck tits"]:
            pos (170,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("mom_sex_options"), Jump("mom_sex_cum_inside")

    imagebutton:
        if mom_sex_position == "missionary":
            pos (450,700)

        elif mom_sex_position in ["cowgirl", "suck tits"]:
            pos (370,700)
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("mom_sex_options"), Jump("mom_sex_cum_outside")

    if mom_sex_position in ["cowgirl", "suck tits"]:
        imagebutton:
            pos (570,700)
            if mom_sex_position == "cowgirl":
                idle "buttons/judith_stage01_03.png"
                hover HoverImage("buttons/judith_stage01_03.png")

            elif mom_sex_position == "suck tits":
                idle "buttons/debbie_stage01_07.png"
                hover HoverImage("buttons/debbie_stage01_07.png")
            action Hide("mom_sex_options"), If(mom_sex_position == "cowgirl", SetVariable("mom_sex_position", "suck tits"), SetVariable("mom_sex_position", "cowgirl")), SetVariable("animated", False), Jump("mom_sex_loop_pre")

    imagebutton:
        if mom_sex_position == "missionary":
            pos (650,700)
            idle "buttons/debbie_stage01_07.png"
            hover HoverImage("buttons/debbie_stage01_07.png")

        elif mom_sex_position in ["cowgirl", "suck tits"]:
            pos (770,700)
            idle "buttons/debbie_stage01_08.png"
            hover HoverImage("buttons/debbie_stage01_08.png")
        action Hide("mom_sex_options"), If(mom_sex_position == "missionary", SetVariable("mom_sex_position", "cowgirl"), SetVariable("mom_sex_position", "missionary")), SetVariable("animated", False), Jump("mom_sex_loop_pre")

    if mom_sex_position == "cowgirl":
        imagebutton:
            pos (370,665)
            idle "buttons/diane_stage01_04.png"
            hover HoverImage("buttons/diane_stage01_04.png")
            action Hide("mom_sex_options"), Function(M_mom.toggle, "change angle"), SetVariable("animated", False), Jump("mom_sex_loop_pre")

    if mom_sex_position in ["missionary", "cowgirl"]:
        if M_mom.get("sex speed") < .4:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("mom_sex_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") + 0.1), Jump("mom_sex_loop")

        if M_mom.get("sex speed") > .21:
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("mom_sex_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") - 0.1), Jump("mom_sex_loop")

screen xray_scr:
    imagebutton:
        focus_mask True
        pos (940,600)
        if xray:
            idle "buttons/anim_03.png"
            hover HoverImage("buttons/anim_03.png")
        else:
            idle "buttons/anim_04.png"
            hover HoverImage("buttons/anim_04.png")
        action If(xray, SetVariable("xray", False), SetVariable("xray", True))

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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
