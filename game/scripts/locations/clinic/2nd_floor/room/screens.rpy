screen hospital_2nd_floor_room:
    add game.timer.image("backgrounds/location_hospital_room{}.jpg")

    imagebutton:
        focus_mask True
        pos (69,274)
        idle "objects/object_door_79.png"
        hover HoverImage("objects/object_door_79.png")
        action Hide("hospital_2nd_floor_room"), Jump("hospital_2nd_floor_room_bathroom_dialogue")

    if L_hospital_room.is_here(M_micoe):
        imagebutton:
            focus_mask True
            pos (300,390)
            idle "objects/character_micoe.png"
            hover HoverImage("objects/character_micoe.png")
            action Hide("hospital_2nd_floor_room"), Jump("micoe_button_dialogue")

    if M_diane.pregnancy.character_bedridden:
        imagebutton:
            focus_mask True
            pos (431, 426)
            idle "objects/character_diane_hospital_"+M_diane.pregnancy.baby_gender+".png"
            hover HoverImage("objects/character_diane_hospital_"+M_diane.pregnancy.baby_gender+".png")
            action Hide("hospital_2nd_floor_room"), Jump("diane_hospital_bed_dialogue")
    else:
        imagebutton:
            focus_mask True
            pos (433,428)
            idle "objects/object_bed_09.png"
            hover HoverImage("objects/object_bed_09.png")
            action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("hospital_2nd_floor_room"), Jump("hospital_second_floor_dialogue")

screen hospital_2nd_floor_bathroom:
    add L_hospital_room_bathroom.background

    imagebutton:
        focus_mask True
        pos (882,10)
        idle "objects/object_door_139.png"
        hover HoverImage("objects/object_door_139.png")
        action Hide("hospital_2nd_floor_bathroom"), Jump("hospital_second_floor_room_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
