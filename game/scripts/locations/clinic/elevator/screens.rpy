screen hospital_elevator():
    use mods_screens_hook("hospital_elevator")

    add "backgrounds/location_hospital_elevator.jpg"

    imagebutton:
        focus_mask True
        pos (454,356)
        idle "buttons/elevator_01.png"
        hover HoverImage("buttons/elevator_01.png")
        action Hide("hospital_elevator"), Jump("hospital_dialogue")

    imagebutton:
        focus_mask True
        pos (454,235)
        idle "buttons/elevator_02.png"
        hover HoverImage("buttons/elevator_02.png")
        action Hide("hospital_elevator"), Jump("hospital_second_floor_dialogue")

    imagebutton:
        focus_mask True
        pos (454,120)
        idle "buttons/elevator_03.png"
        hover HoverImage("buttons/elevator_03.png")
        action Hide("hospital_elevator"), If(L_hospital_floor3.locked, Jump("hospital_floor3_locked"), Jump("hospital_third_floor_dialogue"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
