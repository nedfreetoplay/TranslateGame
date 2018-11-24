screen garage:
    add game.timer.image("backgrounds/location_home_garage_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (380,356)
        idle game.timer.image("objects/object_car_01{}.png")
        hover HoverImage(game.timer.image("objects/object_car_01{}.png"))
        action Hide("garage"), Jump("car_dialogue")

    imagebutton:
        focus_mask True
        pos (43,486)
        idle game.timer.image("objects/object_mower_01{}.png")
        hover HoverImage(game.timer.image("objects/object_mower_01{}.png"))
        action Hide("garage"), Jump("lawnmower_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_08.png"
        hover HoverImage("boxes/auto_option_08.png")
        action Hide("garage"), Jump("home_front")

    if not player.has_picked_up_item("shovel") and M_diane.is_state(S_diane_need_shovel):
        imagebutton:
            focus_mask True
            pos (30,250)
            idle game.timer.image("objects/object_shovel_01{}.png")
            hover HoverImage(game.timer.image("objects/object_shovel_01{}.png"))
            action Hide("garage"), Jump("home_garage_pick_up_shovel")

    if not player.has_picked_up_item("stool"):
        imagebutton:
            focus_mask True
            pos (257,250)
            idle game.timer.image("objects/object_stool_01{}.png")
            hover HoverImage(game.timer.image("objects/object_stool_01{}.png"))
            action Function(player.get_item, "stool"), Show("popup", Image = "boxes/popup_item_stool1.png")

    if not player.has_picked_up_item("drill") and M_dewitt.is_state(S_dewitt_make_new_flute):
        imagebutton:
            focus_mask True
            pos (251,344)
            idle game.timer.image("objects/object_drill_01{}.png")
            hover HoverImage(game.timer.image("objects/object_drill_01{}.png"))
            action Hide("garage"), Jump("garage_dewitt_drill")

    imagebutton:
        focus_mask True
        pos (872,426)
        idle game.timer.image("objects/object_workbench_01{}.png")
        hover HoverImage(game.timer.image("objects/object_workbench_01{}.png"))
        action Hide("garage"), Jump("garage_use_workbench")

screen car_engine:
    add game.timer.image("backgrounds/location_home_garage_car_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (110,97)
        idle game.timer.image("objects/object_engine_01{}.png")
        hover HoverImage(game.timer.image("objects/object_engine_01{}.png"))
        action Hide("car_engine"), Jump("engine_broken")

screen car_mom_jerk_options:
    imagebutton:
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("car_mom_jerk_options"), Jump("mom_car_jerk_loop")

    imagebutton:
        pos (450,700)
        idle "buttons/cam_stage01_02.png"
        hover HoverImage("buttons/cam_stage01_02.png")
        action Hide("car_mom_jerk_options"), Jump("home_front_mom_car_fixed_check_car_finished")

screen car_mom_sex_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("car_mom_sex_options"), Jump("car_mom_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        if M_mom.is_set("car jerk"):
            idle "buttons/cam_stage01_02.png"
            hover HoverImage("buttons/cam_stage01_02.png")
        else:
            idle "buttons/diane_stage01_02.png"
            hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("car_mom_sex_options"), Jump("car_mom_sex_cum")

    if (M_mom.get("sex speed") < .225 and M_mom.is_set("car jerk")) or (M_mom.get("sex speed") < .175 and not M_mom.is_set("car jerk")):
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("car_mom_sex_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") + 0.05), Jump("car_mom_slower_dialogue")

    if (M_mom.get("sex speed") > .126 and M_mom.is_set("car jerk")) or (M_mom.get("sex speed") > .076 and not M_mom.is_set("car jerk")):
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("car_mom_sex_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") - 0.05), Jump("car_mom_faster_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
