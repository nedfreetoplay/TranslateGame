screen kitchen:
    if M_mom.is_set("revealing") or (M_mom.is_set("sleep together") and not M_mom.is_set("revealing")):
        $ mom_idle = "objects/character_debbie_02.png"
        $ mom_hover = HoverImage("objects/character_debbie_02.png")
        $ mom_x = 420
        $ mom_y = 276

    else:
        $ mom_idle = "objects/character_debbie_01.png"
        $ mom_hover = HoverImage("objects/character_debbie_01.png")
        $ mom_x = 682
        $ mom_y = 197

    add game.timer.image("backgrounds/location_home_kitchen_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (41,97)
        idle game.timer.image("objects/object_door_20{}.png")
        hover HoverImage(game.timer.image("objects/object_door_20{}.png"))
        action Hide("kitchen"), Function(renpy.call, "home_lock_check", "Dining Room", "dining_room_dialogue")

    if player.location.is_here(M_mom):
        if M_mom.get_state() == S_mom_dishes_help and M_mom.is_set("chores"):
            imagebutton:
                focus_mask True
                pos (722,196)
                idle "images/objects/character_debbie_05.png"
                hover HoverImage("images/objects/character_debbie_05.png")
                action Hide("kitchen"), Function(renpy.call, "home_lock_check", "Mom", "dishes_dialogue")

        else:
            imagebutton:
                focus_mask True
                pos (mom_x, mom_y)
                idle mom_idle
                hover mom_hover
                action Hide("kitchen"), Function(renpy.call, "home_lock_check", "Mom", "mom_button_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_01.png"
        hover HoverImage("boxes/auto_option_01.png")
        action Hide("kitchen"), Function(renpy.call, "home_lock_check", "Entrance", "home_entrance")

screen deb_name_input:
    add NameInputText("boxes/popup_name_debbie.png", deb_name, "b96dff")
    add Input(size = 24, color = "#b96dff", default = "", changed = debbie_name, length = 12, xpos = 313, ypos = 329, allow = " абвгдеёжзийклмнопрстуфхцчшъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    key "K_RETURN" action Return
    imagebutton idle "buttons/menu_skip_01.png" hover HoverImage("buttons/menu_skip_01.png") action Return pos 320,430

screen mom_kitchen_fuck_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("mom_kitchen_fuck_options"), Jump("mom_kitchen_fuck_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("mom_kitchen_fuck_options"), Jump("mom_kitchen_fuck_cum")

    if M_mom.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("mom_kitchen_fuck_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") + 0.05), Jump("mom_kitchen_fuck_loop")

    if M_mom.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("mom_kitchen_fuck_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") - 0.05), Jump("mom_kitchen_fuck_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
