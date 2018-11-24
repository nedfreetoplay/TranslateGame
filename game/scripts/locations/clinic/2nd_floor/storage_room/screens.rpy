screen hospital_storage_room:
    add "backgrounds/location_hospital_storage.jpg"

    imagebutton:
        focus_mask True
        pos (247,282)
        idle "objects/object_door_80.png"
        hover HoverImage("objects/object_door_80.png")
        action Hide("hospital_storage_room"), Jump("hospital_storage_cabinet_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("hospital_storage_room"), Jump("hospital_second_floor_dialogue")

screen hospital_storage_cabinet:
    add "backgrounds/location_hospital_cabinet.jpg"

    imagebutton:
        focus_mask True
        pos (98,173)
        idle "objects/object_pharmacy_01.png"
        hover HoverImage("objects/object_pharmacy_01.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (486,207)
        idle "objects/object_pharmacy_02.png"
        hover HoverImage("objects/object_pharmacy_02.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (770,226)
        idle "objects/object_pharmacy_03.png"
        hover HoverImage("objects/object_pharmacy_03.png")
        action Show("popup_unfinished")

    if not player.has_item("birth_control_pills"):
        imagebutton:
            focus_mask True
            pos (148,469)
            idle "objects/object_pharmacy_04.png"
            hover HoverImage("objects/object_pharmacy_04.png")
            action Function(player.get_item, "birth_control_pills"), Show("popup", Image = "boxes/popup_item_pills1.png")

    imagebutton:
        focus_mask True
        pos (331,502)
        idle "objects/object_pharmacy_05.png"
        hover HoverImage("objects/object_pharmacy_05.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (596,466)
        idle "objects/object_pharmacy_06.png"
        hover HoverImage("objects/object_pharmacy_06.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (732,457)
        idle "objects/object_pharmacy_07.png"
        hover HoverImage("objects/object_pharmacy_07.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("hospital_storage_cabinet"), Jump("hospital_storage_room_dialogue")

screen roz_storage_sex_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("roz_storage_sex_options"), Jump("roz_storage_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("roz_storage_sex_options"), Jump("roz_storage_sex_cum")

    if M_roz.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("roz_storage_sex_options"), Function(M_roz.set, "sex speed", M_roz.get("sex speed") + 0.05), Jump("roz_storage_sex_loop")

    if M_roz.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("roz_storage_sex_options"), Function(M_roz.set, "sex speed", M_roz.get("sex speed") - 0.05), Jump("roz_storage_sex_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
