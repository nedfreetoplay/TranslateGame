screen MC_computer():
    if M_player.get("computer locked"):
        add game.timer.image("backgrounds/location_computer_player_01{}.jpg")
        add Input(size = 20, color = "#5d9aff", default = "", changed = MC_comp, length = 12, xpos = 425, ypos = 422, allow = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        key "K_RETURN" action Jump("MC_pass_check")

        imagebutton:
            focus_mask True
            pos (780,405)
            idle "buttons/enter_03.png"
            hover HoverImage("buttons/enter_03.png")
            action Jump("MC_pass_check")

        imagebutton:
            focus_mask True
            pos (109,576)
            idle "buttons/computer_button_01.png"
            hover HoverImage("buttons/computer_button_01.png")
            action Hide("MC_computer"), Jump("bedroom_dialogue")
    else:
        add game.timer.image("backgrounds/location_computer_player_02{}.jpg")

        imagebutton:
            focus_mask True
            pos (105,603)
            idle "buttons/computer_button_02.png"
            hover HoverImage("buttons/computer_button_02.png")
            action Hide("MC_computer"), Jump("bedroom_dialogue")

        imagebutton:
            focus_mask True
            pos (105,140)
            idle "buttons/computer_icon_01.png"
            hover HoverImage("buttons/computer_icon_01.png")
            action Show("MC_recycle")

        imagebutton:
            focus_mask True
            pos (105,250)
            idle "computer_icon2"
            hover HoverImage("computer_icon2")
            action Show("MC_family")

        imagebutton:
            focus_mask True
            pos (105,360)
            idle "buttons/computer_icon_03.png"
            hover HoverImage("buttons/computer_icon_03.png")
            action Show("summertime_mc")

        imagebutton:
            focus_mask True
            pos (105,470)
            idle "buttons/computer_icon_24.png"
            hover HoverImage("buttons/computer_icon_24.png")
            action If(
                not M_jenny.get("hacked pc"),
                [Hide("MC_computer"), Jump("webcam_dialogue")],
                [Show("sis_computer")]
            )

        imagebutton:
            focus_mask True
            pos (215,140)
            idle "buttons/computer_icon_13.png"
            hover HoverImage("buttons/computer_icon_13.png")
            action Hide("MC_computer"), Jump("bedroom_study01")

        imagebutton:
            focus_mask True
            pos (215,250)
            idle "buttons/computer_icon_14.png"
            hover HoverImage("buttons/computer_icon_14.png")
            action Hide("MC_computer"), Jump("maze_minigame_prepare")

        imagebutton:
            focus_mask True
            pos (215,360)
            idle "buttons/computer_icon_23.png"
            hover HoverImage("buttons/computer_icon_23.png")
            action Hide("MC_computer"), Jump("egay_search_dialogue")

screen summertime_mc():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    imagebutton:
        focus_mask True
        pos (270,150)
        idle "buttons/computer_window_07.png"
        action Hide("summertime_mc"), Show("summertime_mc_1")

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("summertime_mc")

screen summertime_mc_1():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    imagebutton:
        focus_mask True
        pos (270,150)
        idle "buttons/computer_window_07b.png"
        action Hide("summertime_mc_1"), Show("summertime_mc_2")

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("summertime_mc_1")

screen summertime_mc_2():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    imagebutton:
        focus_mask True
        pos (270,150)
        idle "buttons/computer_window_07c.png"
        action Hide("summertime_mc_2"), Show("summertime_error_mc")

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("summertime_mc_2")

screen summertime_error_mc():
    $ A_inception.unlock()
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    add "buttons/computer_window_08.png" pos 270,150

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("summertime_error_mc")

screen egay(state):
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    if state == "Search":
        add "buttons/computer_window_12.png" pos 270,150

        add Input(size = 20, color = "#5d9aff", default = "", changed = egay_search_string, length = 10, xpos = 575, ypos = 281, allow = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        key "K_RETURN" action Hide("egay"), Hide("MC_computer"), Jump("egay_search")

    elif state == "Fail":
        add "buttons/computer_window_13.png" pos 270,150

        add Input(size = 20, color = "#5d9aff", default = "", changed = egay_search_string, length = 10, xpos = 575, ypos = 281, allow = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        key "K_RETURN" action Hide("egay"), Hide("MC_computer"), Jump("egay_search")

    elif state == "Found":
        imagemap:
            ground "buttons/computer_window_14.png" at Position(xpos = 270, ypos = 150)
            hotspot (206,397,192,41) background "buttons/computer_window_14.png" action If(player.has_money(300),
                [Function(player.spend_money, 300), Function(erik_orcette.finish),
                  Hide("MC_computer"), Jump("egay_purchased_dialogue")],
                [Show('popup', None, "boxes/popup_shopping_fail01.png")]
            )

    elif state == "Purchased":
        add "buttons/computer_window_15.png" pos 270,150

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("egay")

screen MC_recycle():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    add "buttons/computer_window_03.png" pos 270,150

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("MC_recycle")

    imagebutton:
        focus_mask True
        pos (290,210)
        idle "buttons/computer_icon_17.png"
        hover HoverImage("buttons/computer_icon_17.png")
        action NullAction()

    imagebutton:
        focus_mask True
        pos (380,213)
        idle "buttons/computer_icon_18.png"
        hover HoverImage("buttons/computer_icon_18.png")
        action NullAction()

    imagebutton:
        focus_mask True
        pos (470,199)
        idle "buttons/computer_icon_19.png"
        hover HoverImage("buttons/computer_icon_19.png")
        action NullAction()

screen MC_webcam():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    add "buttons/computer_window_09.png" pos 270,150

    if not connected:
        add "buttons/computer_window_10.png" pos 304,302

    else:
        imagebutton:
            focus_mask True
            pos (370,380)
            idle "buttons/computer_icon_20.png"
            hover HoverImage("buttons/computer_icon_20.png")
            action Hide("MC_webcam"), Hide("MC_computer"), Jump("webcam_dialogue")

        imagebutton:
            focus_mask True
            pos (500,380)
            idle "buttons/computer_icon_21.png"
            hover HoverImage("buttons/computer_icon_21.png")
            action NullAction()

        imagebutton:
            focus_mask True
            pos (623,380)
            idle "buttons/computer_icon_21.png"
            hover HoverImage("buttons/computer_icon_21.png")
            action NullAction()

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("MC_webcam")

screen MC_family():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action NullAction()

    add "computer_window1" pos 270,150

    imagebutton:
        focus_mask True
        pos (815,154)
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("MC_family")

    imagebutton:
        focus_mask True
        pos (290,210)
        idle "buttons/computer_icon_16.png"
        hover HoverImage("buttons/computer_icon_16.png")
        action Show("MC_picture", number = 2)

    imagebutton:
        focus_mask True
        pos (390,210)
        idle "buttons/computer_icon_15.png"
        hover HoverImage("buttons/computer_icon_15.png")
        action Show("MC_picture", number = 1)

screen MC_picture(number):
    imagebutton idle "backgrounds/menu_ground.png" action Hide("MC_picture")

    if number == 1:
        add "buttons/computer_pic_06.png" pos 220,150

    elif number == 2:
        add "buttons/computer_pic_07.png" pos 220,150

screen camshow_options():
    if not store._in_replay == None:
        imagebutton:
            focus_mask True
            pos (250,700)
            idle "buttons/cam_stage01_01.png"
            hover HoverImage("buttons/cam_stage01_01.png")
            action Hide("camshow_options"), Jump("sis_camshow_loop")

        imagebutton:
            focus_mask True
            pos (450,700)
            idle "buttons/cam_stage01_02.png"
            hover HoverImage("buttons/cam_stage01_02.png")
            action Hide("camshow_options"), Jump("sis_camshow_finish")

    else:
        imagebutton:
            focus_mask True
            pos (175,700)
            idle "buttons/cam_stage01_01.png"
            hover HoverImage("buttons/cam_stage01_01.png")
            action Hide("camshow_options"), Jump("sis_camshow_loop")

        imagebutton:
            focus_mask True
            pos (375,700)
            idle "buttons/cam_stage01_02.png"
            hover HoverImage("buttons/cam_stage01_02.png")
            action Hide("camshow_options"), Jump("sis_camshow_finish")

        imagebutton:
            focus_mask True
            pos (575,700)
            idle "buttons/cam_stage01_03.png"
            hover HoverImage("buttons/cam_stage01_03.png")
            action If(current_camshow < 4, progressCamShow(current_camshow + 1), progressCamShow(1)), Jump("sis_camshow_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
