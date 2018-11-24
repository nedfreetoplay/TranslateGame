screen dianes_bedroom:
    add game.timer.image("backgrounds/location_diane_bedroom_day{}.jpg")

    if False:
        imagebutton:
            focus_mask True
            pos (228,141)
            idle "images/objects/object_bed_06.png"
            hover HoverImage("images/objects/object_bed_06.png")
            action Hide("dianes_bedroom"), Jump(game.dialog_select("diane_bedroom_dialogue"))

    if M_diane.is_state(S_diane_drunken_splur, S_diane_get_cold_towel, S_diane_bring_cold_towel, S_diane_drunken_splur_aftermath):
        imagebutton:
            focus_mask True
            pos (228,141)
            idle "images/objects/object_bed_07.png"
            hover HoverImage("images/objects/object_bed_07.png")
            action Hide("dianes_bedroom"), Jump(game.dialog_select("diane_bedroom_dialogue"))

    if M_diane.is_state(S_diane_delivery_2_done, S_diane_delivery_2_resting) and not M_diane.is_state(S_diane_debbie_drop_off_request):
        imagebutton:
            focus_mask True
            pos (228,141)
            idle "images/objects/object_bed_07.png"
            hover HoverImage("images/objects/object_bed_07.png")
            action Hide("dianes_bedroom"), Jump(game.dialog_select("diane_bedroom_diane_delivery_2_done"))

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/door19_option_01.png"
        hover HoverImage("boxes/door19_option_01.png")
        action Hide("dianes_bedroom"), Jump(game.dialog_select("dianelobby_dialogue"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
