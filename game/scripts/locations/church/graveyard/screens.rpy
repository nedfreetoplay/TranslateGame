screen church_graveyard:
    if (datetime.date.today().month == 10 and datetime.date.today().day > 25) or (datetime.date.today().month == 11 and datetime.date.today().day < 2):
        add game.timer.image("backgrounds/location_church_graveyard_halloween_day{}.jpg")
    else:
        add game.timer.image("backgrounds/location_church_graveyard_day{}.jpg")

    if not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (248,507)
            idle "objects/object_tomb_01.png"
            hover HoverImage("objects/object_tomb_01.png")
            action Show("popup_unfinished")

        if M_aqua.is_set("tomb search"):
            imagebutton:
                focus_mask True
                pos (82,519)
                idle "objects/object_tomb_03.png"
                hover HoverImage("objects/object_tomb_03.png")
                action Hide("church_graveyard"), Jump("right_tombstone")

    imagebutton:
        focus_mask True
        if not game.timer.is_dark():
            pos (627,223)
        else:
            pos (626,223)
        if not M_player.is_set("pet cat") and not game.timer.is_dark():
            idle "objects/object_tomb_04.png"
            hover HoverImage("objects/object_tomb_04.png")
            action Hide("church_graveyard"), Jump("stray_cat")
        else:
            idle game.timer.image("objects/object_tomb_02{}.png")
            hover HoverImage(game.timer.image("objects/object_tomb_02{}.png"))
            action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("church_graveyard"), If(M_diane.finished_state(S_diane_couch_crashing), Jump("barn_dialogue"), Jump(game.dialog_select("dianes_garden_dialogue")))

screen cat_name_input:
    add NameInputText("boxes/popup_name_cat.png", cat_name, "c87efe")
    add Input(size = 24, color = "#c87efe", default = "", changed = stray_cat_name, length = 12, xpos = 313, ypos = 329, allow = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    key "K_RETURN" action Return
    imagebutton idle "buttons/menu_skip_01.png" hover HoverImage("buttons/menu_skip_01.png") action Return pos 320,430
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
