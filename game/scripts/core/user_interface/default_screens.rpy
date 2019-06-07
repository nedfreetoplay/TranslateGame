screen say(who, what, side_image=None, two_window=False):
    if not two_window:
        window:
            id "window"
            has vbox:
                style "say_vbox"
            if who:
                text who id "who"
            text what id "what"
    else:
        vbox:
            style "say_two_window_vbox"
            if who:
                window:
                    style "say_who_window"
                    text who:
                        id "who"
            window:
                id "window"
                has vbox:
                    style "say_vbox"
                text what id "what"
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0
    use quick_menu

screen choice(items):
    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        has vbox:
            style "menu"
            spacing 10

        for caption, action, chosen in items:

            if action:
                if caption[0:2] == '<>':
                    button:
                        style "menu_choice_button"
                        text caption[2:] style "inactive_menu_choice"

                else:
                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

            else:
                text caption style "menu_caption"

screen input(prompt):
    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            style "nvl_vbox"
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10
                if who is not None:
                    text who id who_id
                text what id what_id
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                    else:
                        text caption style "nvl_dialogue"
    add SideImage() xalign 0.0 yalign 1.0
    use quick_menu

screen popup(disp):
    modal True
    zorder 100
    add disp align .5, .5
    imagebutton idle Fixed() action Hide('popup')

screen route_warning():
    add "backgrounds/blank.jpg"
    add "boxes/popup_warning.png" at truecenter
    imagebutton:
        focus_mask True
        pos (298,378)
        idle "buttons/menu_goback.png"
        hover HoverImage("buttons/menu_goback.png")
        action Hide("route_warning"), Function(player.location.call_screen, new_context = True)

    imagebutton:
        focus_mask True
        pos (612,377)
        idle "buttons/menu_continue.png"
        hover HoverImage("buttons/menu_continue.png")
        action Return()

screen gui_tooltip():
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

screen quick_menu():
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Hide") action HideInterface()
        textbutton _("Save") action ShowMenu("save")
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu("preferences")

screen popup_unfinished():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_unfinished")

    key "K_SPACE" action Hide("popup_unfinished")

    imagebutton:
        focus_mask True
        align (0.5,0.5)
        idle "boxes/popup_unfinished.png"
        action Hide("popup_unfinished")

screen button(Image, Label):
    imagebutton:
        align (0.5,0.97)
        idle str(Image) + ".png"
        hover HoverImage(str(Image)+".png")
        action Hide("button"), Jump(Label)

screen sex_anim_buttons():
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
                [SetVariable("anim_toggle", False),SetVariable("animated", False)] ,
                SetVariable("anim_toggle", True)
            ),
            Return
        ]

screen sex_xray_anim_buttons():
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

    imagebutton:
        pos (940,600)
        if xray:
            idle "buttons/anim_03.png"
            hover HoverImage("buttons/anim_03.png")
        else:
            idle "buttons/anim_04.png"
            hover HoverImage("buttons/anim_04.png")
        action [
            If(
                xray, 
                SetVariable("xray", False), 
                SetVariable("xray", True)
            )
        ]

screen money_popup(amount=100, type=""):
    $ amount = amount
    $ x = 550
    $ y = 390
    $ x -= len(str(amount)) * 30
    $ img = "boxes/popup_money{}.png"
    if not type:
        $ img = img.format("")
    else:
        $ img = img.format("_"+type)
    imagebutton:
        idle img
        align (0.5, 0.5)
        action Hide("money_popup")

    text "{}".format(amount):
        bold True
        size 30
        pos (x, y)

    imagebutton:
        idle "backgrounds/menu_ground.png"
        pos 0,0
        action Play("audio", "coins1"), Hide("money_popup"), Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
