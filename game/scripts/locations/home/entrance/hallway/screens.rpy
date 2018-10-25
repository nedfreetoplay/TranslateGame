screen hallway:
    add game.timer.image("backgrounds/location_home_hallway_day{}.jpg")


    imagebutton:
        focus_mask True
        pos (175,280)
        idle game.timer.image("objects/object_door_02{}.png")
        hover HoverImage(game.timer.image("objects/object_door_02{}.png"))
        action Hide("hallway"), Function(renpy.call, "home_lock_check", "Bedroom", "bedroom_dialogue")


    imagebutton:
        focus_mask True
        pos (387,225)
        idle game.timer.image("objects/object_door_03{}.png")
        hover HoverImage(game.timer.image("objects/object_door_03{}.png"))
        action Hide("hallway"), Function(renpy.call, "home_lock_check", "Upstairs Bedroom", "sis_bedroom_dialogue")


    imagebutton:
        focus_mask True
        if game.in_shower is not None:
            pos (526,108)
            idle "objects/object_door_04_busy.png"
            hover HoverImage("objects/object_door_04_busy.png")
        else:
            pos (580,108)
            idle game.timer.image("objects/object_door_04{}.png")
            hover HoverImage(game.timer.image("objects/object_door_04{}.png"))
        action Hide("hallway"), Function(renpy.call, "home_lock_check", "Shower", "shower_dialogue")


    imagebutton:
        focus_mask True
        pos (830,0)
        idle game.timer.image("objects/object_door_19{}.png")
        hover HoverImage(game.timer.image("objects/object_door_19{}.png"))
        action Hide("hallway"), Function(renpy.call, "home_lock_check", "Entrance", "home_entrance")


    imagebutton:
        focus_mask True
        pos (360,40)
        idle game.timer.image("objects/object_door_40{}.png")
        hover HoverImage(game.timer.image("objects/object_door_40{}.png"))
        action Hide("hallway"), Function(renpy.call, "home_lock_check", "Attic", "attic_entry_dialogue")

screen jen_name_input:
    add NameInputText("boxes/popup_name_jenny.png", jen_name, "ff6df0")
    add Input(size = 24, color = "#ff6df0", default = "", changed = jenny_name, length = 12, xpos = 313, ypos = 329, allow = " абвгдеёжзийклмнопрстуфхцчшъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    key "K_RETURN" action Return
    imagebutton idle "buttons/menu_skip_01.png" hover HoverImage("buttons/menu_skip_01.png") action Return pos 320,430
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
