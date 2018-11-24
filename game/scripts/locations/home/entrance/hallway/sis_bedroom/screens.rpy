screen sybianscr:
    modal True

    if sybian_stage == 0:
        imagebutton:
            pos (50,320)
            idle "images/buttons/sybian_04.png"
            hover HoverImage("images/buttons/sybian_04.png")
            action Hide("sybianscr"), SetVariable("sybian_stage", 1), SetVariable("sis_sybian_speed", sis_sybian_speed - 0.25), Jump(game.dialog_select("sybian_stage1"))

    if sybian_stage == 1:
        imagebutton:
            pos (50,320)
            idle "images/buttons/sybian_01.png"
            hover HoverImage("images/buttons/sybian_01.png")
            action Hide("sybianscr"), SetVariable("sybian_stage", 2), SetVariable("sis_sybian_speed", sis_sybian_speed - 0.25), Jump(game.dialog_select("sybian_stage2"))

    if sybian_stage == 2:
        imagebutton:
            pos (50,320)
            idle "images/buttons/sybian_02.png"
            hover HoverImage("images/buttons/sybian_02.png")
            action Hide("sybianscr"), SetVariable("sybian_stage", 3), SetVariable("sis_sybian_speed", sis_sybian_speed - 0.25), Jump(game.dialog_select("sybian_stage3"))

screen diary_next:
    imagebutton:
        idle "objects/object_diary_button01.png"
        hover HoverImage("objects/object_diary_button01.png")
        action Return()
        xpos 900
        ypos 330

screen upstairs_bedroom:
    add game.timer.image("backgrounds/location_home_jennybedroom_day{}.jpg")


    imagebutton:
        focus_mask True
        pos (30,327)
        idle game.timer.image("objects/object_desk_02{}.png")
        hover HoverImage(game.timer.image("objects/object_desk_02{}.png"))
        action Show("desk02_options")


    imagebutton:
        focus_mask True
        pos (865,483)
        idle game.timer.image("objects/object_bedtable_01{}.png")
        hover HoverImage(game.timer.image("objects/object_bedtable_01{}.png"))
        action Show("bedtable01_options")


    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_01.png"
        hover HoverImage("boxes/auto_option_01.png")
        action Hide("upstairs_bedroom"), Jump("hallway_dialogue")


    if not player.has_picked_up_item("condom"):
        imagebutton:
            focus_mask True
            pos (465,590)

            idle "objects/object_condom_01.png"
            hover HoverImage("objects/object_condom_01.png")
            action Function(player.get_item, "condom"), Hide("upstairs_bedroom"), Jump("condom")


    if player.location.is_here(M_jenny) and game.timer.is_dark():


        imagebutton:
            focus_mask True
            pos (362,416)
            idle "objects/object_bed_02_night.png"
            hover HoverImage("objects/object_bed_02_night.png")
            action Show("sisbed_options")

    elif player.location.is_here(M_jenny):
        if M_jenny.finished_state(S_jenny_hallway_noises):
            $ img_i = "objects/character_jenny_03.png"
            $ img_h = HoverImage("objects/character_jenny_03.png")
            $ img_x = 580
            $ img_y = 420

        elif sis_panties_bought:
            $ img_i = "objects/character_jenny_01.png"
            $ img_h = HoverImage("objects/character_jenny_01.png")
            $ img_x = 660
            $ img_y = 320

        else:
            $ img_i = "objects/character_jenny_02.png"
            $ img_h = HoverImage("objects/character_jenny_02.png")
            $ img_x = 600
            $ img_y = 400

        imagebutton:
            focus_mask True
            pos (img_x, img_y)
            idle img_i
            hover img_h
            action Hide("upstairs_bedroom"), Jump(game.dialog_select("sis_button_dialogue"))


    else:
        if M_jenny.is_state(S_jenny_read_diary) and not L_home_sisbedroom.is_here(M_jenny):
            imagebutton:
                focus_mask True
                pos (610,520)

                idle "objects/object_diary_item01.png"
                hover HoverImage("objects/object_diary_item01.png")
                action Hide("upstairs_bedroom"), Jump("diary_dialogue")

screen sisbed_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("sisbed_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/bed02_option_01.png"
        hover HoverImage("boxes/bed02_option_01.png")
        action Hide("sisbed_options"), Hide("upstairs_bedroom"), Jump("sneak_in_sis_bed")

screen desk02_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("desk02_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/desk02_option_01.png"
        hover HoverImage("boxes/desk02_option_01.png")
        action If(
            not game.timer.is_dark(),
            [Hide("desk02_options"), Hide("upstairs_bedroom"), Jump("siscomp_day")],
            [Hide("desk02_options"), Hide("upstairs_bedroom"), Jump("sis_computer")]
        )

screen bedtable01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("desk04_options")
    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/bedtable01_option_01.png"
        hover HoverImage("boxes/bedtable01_option_01.png")
        action If(
            not game.timer.is_dark(),
            [Hide("bedtable01_options"), Hide("upstairs_bedroom"), Jump("bedside01_dialogue")],
            [Hide("bedtable01_options"), Hide("upstairs_bedroom"), Jump("bedtable_night")]
        )

screen bedside01:
    add "backgrounds/location_home_jennytable.jpg"
    imagebutton:
        focus_mask True
        pos (382,302)
        idle "objects/object_panties_01.png"
        hover HoverImage("objects/object_panties_01.png")
        action Hide("bedside01"), Function(M_jenny.trigger, T_jenny_panty_caught), Jump ("sis_bedroom_dialogue")

screen sis_cheerleader_sex_options:
    imagebutton:
        focus_mask True
        if sis_cheerleader_sex2_menu:
            pos (250,700)
        else:
            pos (150,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("sis_cheerleader_sex_options"), Jump(game.dialog_select("sis_cheerleader_fuck_looprep"))

    if not sis_cheerleader_sex2_menu:
        imagebutton:
            focus_mask True
            pos (350,700)
            idle "buttons/diane_stage01_03.png"
            hover HoverImage("buttons/diane_stage01_03.png")
            action Hide("sis_cheerleader_sex_options"), Jump(game.dialog_select("sis_cheerleader_fuck_cum_outside"))

    if sis_cheerleader_sex2_menu:
        imagebutton:
            focus_mask True
            pos (450,700)
            idle "buttons/diane_stage01_02.png"
            hover HoverImage("buttons/diane_stage01_02.png")
            if sis_final_cum == "Outside":
                action Hide("sis_cheerleader_sex_options"), Jump(game.dialog_select("sis_cheerleader_fuck_cum_inside_unhappy"))
            elif sis_final_cum == "Inside" and M_jenny.finished_state(S_jenny_cam_show):
                action Hide("sis_cheerleader_sex_options"), Jump(game.dialog_select("sis_cheerleader_fuck_cum_inside_happy"))

    if store._in_replay == None and player.stats.str() < 7 and not sis_cheerleader_sex2_menu:
        imagebutton:
            focus_mask True
            pos (550,700)
            idle "buttons/jenny_break_01.png"
            hover HoverImage("buttons/jenny_break_01.png")
            action Hide("sis_cheerleader_sex_options"), Jump(game.dialog_select("sis_cheerleader_break_free_fail"))

    if not sis_cheerleader_sex2_menu and not store._in_replay == None or store._in_replay == None and not sis_cheerleader_sex2_menu and player.stats.str() >= 7:
        imagebutton:
            focus_mask True
            pos (550,700)
            idle "buttons/jenny_break_01.png"
            hover HoverImage("buttons/jenny_break_01.png")
            action Hide("sis_cheerleader_sex_options"), Jump(game.dialog_select("sis_cheerleader_break_free_pass"))

    if M_jenny.get('sex speed') < .3:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("sis_cheerleader_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.1), Jump("sis_cheerleader_fuck_looprep")

    if M_jenny.get('sex speed') > .11:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("sis_cheerleader_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.1), Jump("sis_cheerleader_fuck_looprep")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
