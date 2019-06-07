init 1 python:
    class JennyCamslutVideoButton(renpy.Displayable):
        def __init__(self, **properties):
            super(JennyCamslutVideoButton, self).__init__(**properties)
            self._bg = renpy.displayable("buttons/computer_video_button.png")
            self._text = FilteredText("Videos", style="style_jenny_video_button")
        
        def get_render(self, width, height, st, at):
            return renpy.render(self._bg, width, height, st, at)
        
        def render(self, width, height, st, at):
            render = self.get_render(width, height, st, at)
            text_r = renpy.render(self._text, width, height, st, at)
            tw, th = text_r.get_size()
            x = 50
            y = 5
            render.blit(text_r, (x, y))
            return render
        def event(self, ev, x, y, st):
            pass

    class JennyCamslutVideoButtonHover(JennyCamslutVideoButton):
        def get_render(self, width, height, st, at):
            return renpy.render(im.MatrixColor(self._bg, HoverImage.h_matrix), width, height, st, at)

screen sis_computer():
    if not M_jenny.is_set("comp locked"):
        add "backgrounds/location_computer_jenny_02.jpg"
        imagebutton:
            idle "buttons/computer_button_02.png"
            hover HoverImage("buttons/computer_button_02.png")
            action [Hide("sis_computer"), Hide("comp_screen"), If(M_player.get("on_jenny_pc"), Jump("sis_bedroom_dialogue"), Show("MC_computer"))]
            xpos 105
            ypos 603

        imagebutton:
            idle "buttons/computer_icon_01.png"
            hover HoverImage("buttons/computer_icon_01.png")
            action Show("sis_recycle")
            xpos 105
            ypos 140

        imagebutton:
            idle "computer_icon2"
            hover HoverImage("computer_icon2")
            action Show("sis_family")
            xpos 105
            ypos 250

        imagebutton:
            idle "buttons/computer_icon_03.png"
            hover HoverImage("buttons/computer_icon_03.png")
            action Show("summertime")
            xpos 105
            ypos 360

        imagebutton:
            idle "buttons/computer_icon_24.png"
            hover HoverImage("buttons/computer_icon_24.png")
            action [Hide("sis_computer"), Jump("hacking_minigame_pre")]
            xpos 105
            ypos 470

        imagebutton:
            idle "buttons/computer_icon_05.png"
            hover HoverImage("buttons/computer_icon_05.png")
            action [Hide("sis_computer"), Jump("sispc_toylist_response")]
            xpos 215
            ypos 140

        imagebutton:
            idle "buttons/computer_icon_06.png"
            hover HoverImage("buttons/computer_icon_06.png")
            action [Show("jenny_camslut"), Jump("jenny_computer_camslut")]
            xpos 215
            ypos 250

        imagebutton:
            idle "buttons/computer_icon_22.png"
            hover HoverImage("buttons/computer_icon_22.png")
            action [Hide("sis_computer"), Jump("sispc_email_response")]
            xpos 215
            ypos 360

    else:
        add "backgrounds/location_computer_jenny_01.jpg"
        add Input(size=20, color="#5d9aff", default="", changed=sis_comp, length=12, xpos= 425, ypos = 422, allow = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        key "K_RETURN" action Jump("pass_check")
        imagebutton idle "buttons/enter_02.png" hover HoverImage("buttons/enter_02.png") at Position(xpos = 780, ypos = 405) action Jump("pass_check")
        imagebutton idle "buttons/computer_button_01.png" hover HoverImage("buttons/computer_button_01.png") action [Hide("sis_computer"), Jump("sis_bedroom_dialogue")] pos 109,576

screen summertime() tag comp_screen:


    imagebutton idle "buttons/computer_window_07.png" action [Hide("sis_computer"), Hide("summertime"), Jump("sispc_summertime_response")] pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action [Hide("summertime")]
        xpos 816
        ypos 154

screen summertime_error() tag comp_screen:


    add "buttons/computer_window_08.png" pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("summertime_error")
        xpos 816
        ypos 154

screen sis_list() tag comp_screen:


    add "buttons/computer_window_04.png" pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("sis_list")
        xpos 816
        ypos 154

screen jenny_camslut() tag comp_screen:


    use sis_computer
    add "buttons/computer_window_05.png" pos 270,150

    imagebutton:
        focus_mask True
        pos 560,215
        idle JennyCamslutVideoButton()
        hover JennyCamslutVideoButtonHover()
        action [If(game.in_dialogue, NullAction(), [Hide("jenny_camslut"), Jump("jenny_camslut_videos_tab")])]

    if M_jenny.is_state(S_jenny_figure_out_password):
        imagebutton:
            pos 816, 154
            idle "buttons/computer_button_03.png"
            action NullAction()
    else:
        imagebutton:
            idle "buttons/computer_button_03.png"
            hover HoverImage("buttons/computer_button_03.png")
            action If(game.in_dialogue, NullAction(), Hide("jenny_camslut"))
            xpos 816
            ypos 154

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action If(game.in_dialogue, NullAction(), (Hide("jenny_camslut"),
                                                   Show('sis_computer')))
        xpos 816
        ypos 154

screen jenny_camslut_videos() tag comp_screen:


    use sis_computer
    add "buttons/computer_window_05b.png" pos 270,150

    imagebutton:
        focus_mask True
        pos 560,215
        idle JennyCamslutVideoButton()
        hover JennyCamslutVideoButtonHover()
        action If(game.in_dialogue, NullAction(), [Hide("jenny_camslut_videos"), Show("jenny_camslut")])

    imagebutton:
        focus_mask True
        pos 503, 278
        idle "buttons/computer_video_01.png"
        hover HoverImage("buttons/computer_video_01.png")
        action If(game.in_dialogue, NullAction(), Call("jenny_camslut_video_choice", 1))

    imagebutton:
        focus_mask True
        pos 640, 278
        idle "buttons/computer_video_02.png"
        hover HoverImage("buttons/computer_video_02.png")
        action If(game.in_dialogue, NullAction(), Call("jenny_camslut_video_choice", 2))

    if M_jenny.finished_state(S_jenny_deliver_bad_monster):
        imagebutton:
            focus_mask True
            pos 503, 395
            idle "buttons/computer_video_03.png"
            hover HoverImage("buttons/computer_video_03.png")
            action If(game.in_dialogue, NullAction(), Call("jenny_camslut_video_choice", 3))

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action If(game.in_dialogue, NullAction(), (Hide("jenny_camslut_videos"),
                                                   Show('sis_computer')))
        xpos 816
        ypos 154

screen sis_recycle() tag comp_screen:


    add "buttons/computer_window_03.png" pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("sis_recycle")
        xpos 816
        ypos 154

    imagebutton:
        idle "buttons/computer_icon_12.png"
        hover HoverImage("buttons/computer_icon_12.png")
        action [Hide("sis_computer"), Hide("sis_recycle"), Jump("sispc_nude_response")]
        xpos 290
        ypos 210

screen sis_family() tag comp_screen:


    add "computer_window1" pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("sis_family")
        xpos 816
        ypos 154

    imagebutton:
        idle "buttons/computer_icon_07.png"
        hover HoverImage("buttons/computer_icon_07.png")
        action Show("sis_newfolder")
        xpos 290
        ypos 210

    imagebutton:
        idle "computer_icon9"
        hover HoverImage("computer_icon9")
        action [Hide("sis_computer"), Hide("sis_family"), Jump("sispc_igor_response")]
        xpos 390
        ypos 210

    imagebutton:
        idle "buttons/computer_icon_08.png"
        hover HoverImage("buttons/computer_icon_08.png")
        action [Hide("sis_computer"), Hide("sis_family"), Jump("sispc_family_response")]
        xpos 490
        ypos 210

screen sis_newfolder() tag comp_screen:


    add "buttons/computer_window_02.png" pos 270,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("sis_newfolder")
        xpos 816
        ypos 154

    imagebutton:
        idle "buttons/computer_icon_10.png"
        hover HoverImage("buttons/computer_icon_10.png")
        action [Hide("sis_computer"), Hide("sis_newfolder"), Jump("sispc_swimsuit_response")]
        xpos 290
        ypos 210

    imagebutton:
        idle "buttons/computer_icon_11.png"
        hover HoverImage("buttons/computer_icon_11.png")
        action Show("sis_picture", number = 2)
        xpos 390
        ypos 210

screen sis_email() tag comp_screen:


    add "buttons/computer_window_11.png" pos 135,150

    imagebutton:
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("sis_email")
        xpos 839
        ypos 154

    if sis_email_01_read == True:
        imagebutton:
            idle "buttons/computer_email_01_read.png"
            hover HoverImage("buttons/computer_email_01_read.png")
            action Show("sis_email_open", email = 1)
            xpos 235
            ypos 251
    else:
        imagebutton:
            idle "buttons/computer_email_01.png"
            hover HoverImage("buttons/computer_email_01.png")
            action [SetVariable("sis_email_01_read", True), Show("sis_email_open", email = 1)]
            xpos 235
            ypos 251

    if sis_email_02_read == True:
        imagebutton:
            idle "buttons/computer_email_02_read.png"
            hover HoverImage("buttons/computer_email_02_read.png")
            action Show("sis_email_open", email = 2)
            xpos 235
            ypos 291
    else:
        imagebutton:
            idle "buttons/computer_email_02.png"
            hover HoverImage("buttons/computer_email_02.png")
            action [SetVariable("sis_email_02_read", True), Show("sis_email_open", email = 2)]
            xpos 235
            ypos 291

    imagebutton:
        idle "buttons/computer_email_03_read.png"
        hover HoverImage("buttons/computer_email_03_read.png")
        action Show("sis_email_open", email = 3)
        xpos 235
        ypos 331

    imagebutton:
        idle "buttons/computer_email_04_read.png"
        hover HoverImage("buttons/computer_email_04_read.png")
        action [SetVariable("sis_email_04_read", True), Show("sis_email_open", email = 4)]
        xpos 235
        ypos 371

    imagebutton:
        idle "buttons/computer_email_05_read.png"
        hover HoverImage("buttons/computer_email_05_read.png")
        action Show("sis_email_open", email = 5)
        xpos 235
        ypos 411

    imagebutton:
        idle "buttons/computer_email_06_read.png"
        hover HoverImage("buttons/computer_email_06_read.png")
        action Show("sis_email_open", email = 6)
        xpos 235
        ypos 451

screen sis_picture(number):
    imagebutton idle "backgrounds/menu_ground.png" action [Hide("sis_picture")]

    if number == 1:
        add "buttons/computer_pic_01.png" pos 270,150
    elif number == 2:
        add "buttons/computer_pic_02.png" pos 270,150
    elif number == 3:
        add "buttons/computer_pic_03.png" pos 270,150
    elif number == 4:
        add "buttons/computer_pic_04.png" pos 270,150
    else:
        add "buttons/computer_pic_05.png" pos 270,150

screen sis_email_open(email):
    imagebutton idle "backgrounds/menu_ground.png" action [Hide("sis_email_open"), Show("sis_email")]

    if email == 1:
        add "buttons/computer_email_01_popup.png" pos 235,251
    elif email == 2:
        add "buttons/computer_email_02_popup.png" pos 235,251
    elif email == 3:
        add "buttons/computer_email_03_popup.png" pos 235,251
    elif email == 4:
        add "buttons/computer_email_04_popup.png" pos 235,251
    elif email == 5:
        add "buttons/computer_email_05_popup.png" pos 235,251
    else:
        add "buttons/computer_email_06_popup.png" pos 235,251
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
