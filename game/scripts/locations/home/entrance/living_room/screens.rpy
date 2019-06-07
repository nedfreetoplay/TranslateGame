screen living_room():
    use mods_screens_hook("living_room")

    if M_mom.get_state() in [S_mom_romance_movie, S_mom_romance_movie_two] or (M_mom.is_set("movie night") and game.timer.is_dark()):
        if Game.is_christmas():
            add "backgrounds/location_home_livingroom_christmas_night_debbie.jpg"
        else:
            add "backgrounds/location_home_livingroom_night_debbie.jpg"
    else:
        add player.location.background

    if L_home_livingroom.is_here(M_diane) and not M_mom.is_state(S_mom_romance_movie, S_mom_romance_movie_two, S_mom_spy) and not M_mom.get("movie night"):
        if M_diane.pregnancy.gave_birth:
            imagebutton:
                focus_mask True
                pos (653,386)
                idle "objects/character_diane_casual_" + M_diane.pregnancy.baby_gender +".png"
                hover HoverImage("objects/character_diane_casual_" + M_diane.pregnancy.baby_gender +".png")
                action Hide("living_room"), Jump("aunt_button_dialogue")
        else:
            imagebutton:
                focus_mask True
                pos (331,480)
                idle "objects/object_couch_02.png"
                hover HoverImage("objects/object_couch_02.png")
                action Hide("living_room"), Jump("aunt_button_dialogue")

    imagebutton:
        focus_mask True
        pos (1002,251)
        idle game.timer.image("objects/object_door_42{}.png")
        hover HoverImage(game.timer.image("objects/object_door_42{}.png"))
        action Hide("living_room"), Function(renpy.call, "home_lock_check", "Entrance", "home_entrance")

    imagebutton:
        focus_mask True
        pos (809,311)
        idle game.timer.image("objects/object_door_43{}.png")
        hover HoverImage(game.timer.image("objects/object_door_43{}.png"))
        action Hide("living_room"), Function(renpy.call, "home_lock_check", "Basement", "home_basement_dialogue")

    imagebutton:
        focus_mask True
        pos (108,312)
        idle game.timer.image("objects/object_door_44{}.png")
        hover HoverImage(game.timer.image("objects/object_door_44{}.png"))
        action Hide("living_room"), Function(renpy.call, "home_lock_check", "Master Bedroom", "mom_bedroom")

    imagebutton:
        focus_mask True
        pos (412,331)
        idle game.timer.image("objects/object_tv_01{}.png")
        hover HoverImage(game.timer.image("objects/object_tv_01{}.png"))
        action Hide("living_room"), Function(renpy.call, "home_lock_check", "Living Room TV", "home_livingroom_tv")

screen home_livingroom_tv():
    add "backgrounds/location_home_tv.jpg"

    if tv_channel == 0:
        add "buttons/tv_channel_01.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 1:
        add "buttons/tv_channel_02.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 2:
        add "buttons/tv_channel_03.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 3:
        add "buttons/tv_channel_04.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 4:
        add "buttons/tv_channel_05.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 5:
        add "buttons/tv_channel_06.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 6:
        add "buttons/tv_channel_07.png" at Position(xpos=86, ypos=107)

    elif tv_channel == 7:
        if tv_pink_channel == 7 and not tv_channel_pink:
            add "buttons/tv_channel_09.png" at Position(xpos=86, ypos=107)

        elif tv_pink_channel == 8 and not tv_channel_pink:
            add "buttons/tv_channel_10.png" at Position(xpos=86, ypos=107)

        else:
            add "buttons/tv_channel_08.png" at Position(xpos=86, ypos=107)

            $ tv_channel = 7
            default pink_screen = True

            imagemap:
                ground "pink_channel_login" at Position(xpos=0, ypos=0)
                hotspot (390,325,270,29) background "buttons/tv_channel_08.png" action SetScreenVariable("pink_screen", True)
                hotspot (390,398,270,29) background "buttons/tv_channel_08.png" action SetScreenVariable("pink_screen", False)
                if pink_screen:
                    add Input(size=20, color="#ff4bdf", default=pink_user, changed=pink_channel_user, length=12, xpos = 433, ypos = 329, allow = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
                    text "{size=20}{color=#ff4bdf}[pink_pass]{/color}{/size}" at Position(xpos = 433, ypos = 400)

                else:
                    text "{size=20}{color=#ff4bdf}[pink_user]{/color}{/size}" at Position(xpos = 433, ypos = 329)
                    add Input(size=20, color="#ff4bdf", default=pink_pass, changed=pink_channel_pass, length=12, xpos = 433, ypos = 400, allow = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

            key "K_RETURN" action Jump("tv_pink_channel_pass_check")

            imagebutton:
                idle "buttons/enter_01.png"
                hover HoverImage("buttons/enter_01.png") at Position(xpos=460, ypos= 450)
                action Jump("tv_pink_channel_pass_check")

    imagebutton:
        focus_mask True
        pos (398,633)
        idle "buttons/tv_buttons_01.png"
        hover HoverImage("buttons/tv_buttons_01.png")
        action Hide("home_livingroom_tv"), Jump("home_livingroom_dialogue")

    imagebutton:
        focus_mask True
        pos (393,677)
        idle "buttons/tv_buttons_02.png"
        hover HoverImage("buttons/tv_buttons_02.png")
        action SetVariable("tv_channel", tv_channel - 1), Jump("tv_channel_responses")

    imagebutton:
        focus_mask True
        pos (554,678)
        idle "buttons/tv_buttons_03.png"
        hover HoverImage("buttons/tv_buttons_03.png")
        action SetVariable("tv_channel", tv_channel + 1), Jump("tv_channel_responses")

screen sis_couch_sex_options():
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("sis_couch_sex_options"), Jump("sis_couch_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("sis_couch_sex_options"), Jump("sis_couch_sex_cum")

    if M_jenny.get("sex speed") < .4:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("sis_couch_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.1), Jump("sis_couch_sex_loop")

    if M_jenny.get("sex speed") > .21:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("sis_couch_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.1), Jump("sis_couch_sex_loop")

screen debbie_movie_night_couch_blowjob_options():

    imagebutton:
        pos (250,700)
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("debbie_movie_night_couch_blowjob_options"), Jump("debbie_movie_night_couch_blowjob_loop")

    imagebutton:
        pos (450,700)
        focus_mask True
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("debbie_movie_night_couch_blowjob_options"), Jump("debbie_movie_night_couch_blowjob_cum")

    if M_mom.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("debbie_movie_night_couch_blowjob_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") + 0.05), Jump("debbie_movie_night_couch_blowjob_loop")
            xpos 250
            ypos 735

    if M_mom.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("debbie_movie_night_couch_blowjob_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") - 0.05), Jump("debbie_movie_night_couch_blowjob_loop")
            xpos 450
            ypos 735

screen debbie_movie_night_couch_sex_options():

    imagebutton:
        pos (250,700)
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("debbie_movie_night_couch_sex_options"), Jump("debbie_movie_night_couch_sex_loop")

    imagebutton:
        pos (450,700)
        focus_mask True
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("debbie_movie_night_couch_sex_options"), Jump("debbie_movie_night_couch_sex_cum")

    if M_mom.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("debbie_movie_night_couch_sex_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") + 0.05), Jump("debbie_movie_night_couch_sex_loop")
            xpos 250
            ypos 735

    if M_mom.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("debbie_movie_night_couch_sex_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") - 0.05), Jump("debbie_movie_night_couch_sex_loop")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
