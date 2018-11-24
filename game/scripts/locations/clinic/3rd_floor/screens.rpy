screen hospital_3rd_floor:
    add L_hospital_floor3.background

    imagebutton:
        focus_mask True
        pos (466,458)
        idle "objects/object_elevator_01.png"
        hover HoverImage("objects/object_elevator_01.png")
        action Hide("hospital_3rd_floor"), Jump("elevator_dialogue")

    imagebutton:
        focus_mask True
        pos (371,412)
        idle "objects/object_door_136.png"
        hover HoverImage("objects/object_door_136.png")
        action Hide("hospital_3rd_floor"), Jump("hospital_lab_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
