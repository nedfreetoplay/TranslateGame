screen hospital_2nd_floor():
    use mods_screens_hook("hospital_2nd_floor")

    add game.timer.image("backgrounds/location_hospital_second{}.jpg")

    imagebutton:
        focus_mask True
        pos (466,458)
        idle "objects/object_elevator_01.png"
        hover HoverImage("objects/object_elevator_01.png")
        action Hide("hospital_2nd_floor"), Jump("elevator_dialogue")

    imagebutton:
        focus_mask True
        pos (50,168)
        idle "objects/object_door_77.png"
        hover HoverImage("objects/object_door_77.png")
        action Hide("hospital_2nd_floor"), Jump("hospital_second_floor_room_dialogue")

    imagebutton:
        focus_mask True
        pos (260,405)
        idle "objects/object_phone_01.png"
        hover HoverImage("objects/object_phone_01.png")
        action Hide("hospital_2nd_floor"), Jump("hospital_second_floor_phone_dialogue")

    imagebutton:
        focus_mask True
        pos (843,168)
        idle "objects/object_door_78.png"
        hover HoverImage("objects/object_door_78.png")
        action Hide("hospital_2nd_floor"), Jump("hospital_storage_room_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
