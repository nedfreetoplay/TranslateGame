screen hospital():
    use mods_screens_hook("hospital")

    add game.timer.image("backgrounds/location_hospital_first{}.jpg")

    imagebutton:
        focus_mask True
        pos (0,0)
        if L_hospital.is_here(M_roz):
            if datetime.date.today().month == 12 and (datetime.date.today().day >= 15 and datetime.date.today().day <= 30):
                idle "objects/object_desk_09_hat.png"
                hover HoverImage("objects/object_desk_09_hat.png")
            else:
                idle "objects/object_desk_09.png"
                hover HoverImage("objects/object_desk_09.png")
            action Hide("hospital"), Jump("roz_dialogue")

        else:
            idle "objects/object_desk_09_empty.png"
            hover HoverImage("objects/object_desk_09_empty.png")
            action Hide("hospital"), Show("hospital_front_desk")

    imagebutton:
        focus_mask True
        pos (466,458)
        idle "objects/object_elevator_01.png"
        hover HoverImage("objects/object_elevator_01.png")
        action Hide("hospital"), Jump("elevator_dialogue")

screen hospital_front_desk():
    add "backgrounds/location_hospital_desk.jpg"

    imagebutton:
        focus_mask True
        pos (338,183)
        idle "objects/object_box_01.png"
        hover HoverImage("objects/object_box_01.png")
        action Hide("hospital_front_desk"), Show("roz_locker")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("hospital_front_desk"), Jump("hospital_dialogue")

screen roz_locker():
    add "backgrounds/location_hospital_box.jpg"

    if not player.has_item("hospital_access_card"):
        imagebutton:
            focus_mask True
            pos (580,50)
            idle "objects/object_card_01.png"
            hover HoverImage("objects/object_card_01.png")
            action Function(player.get_item, "hospital_access_card"), Show('popup', None, "boxes/popup_item_card4.png")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("roz_locker"), Show("hospital_front_desk")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
