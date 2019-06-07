screen boys_lockerroom():
    use mods_screens_hook("boys_lockerroom")


    if not game.timer.is_dark():
        if L_school_shower.is_here(M_roxxy):
            add "backgrounds/location_school_locker_room_empty_day.jpg"
        else:
            add "backgrounds/location_school_locker_room_day.jpg"
    else:
        add "backgrounds/location_school_locker_room_night.jpg"

    if L_school_shower.is_here(M_roxxy):
        imagebutton:
            focus_mask True
            pos (25,274)
            idle "images/objects/object_door_17_girls.png"
            hover HoverImage("images/objects/object_door_17_girls.png")
            action Hide("boys_lockerroom"), Jump("roxxy_shower_dialogue")

    elif M_bissette.is_set("martinez book search") and not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (4,274)
            idle "images/objects/object_door_17_backpack.png"
            hover HoverImage("images/objects/object_door_17_backpack.png")
            action Hide("boys_lockerroom"), Jump("latinas_shower_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (25,274)
            idle game.timer.image("objects/object_door_17{}.png")
            hover HoverImage(game.timer.image("objects/object_door_17{}.png"))
            action If(
                shower_door_count == 0,
                [Hide("boys_lockerroom"), Jump("door17_locked_dialogue")],
                [Hide("boys_lockerroom"), Jump("lockershowers_dialogue")]
            )

    if False:
        imagebutton:
            focus_mask True
            pos (520,160)
            idle "objects/object_airvent_01.png"
            hover HoverImage("objects/object_airvent_01.png")
            action Hide("boys_lockerroom"), Jump("airvent_webcam_quest")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_02.png"
        hover HoverImage("boxes/auto_option_02.png")
        action Hide("boys_lockerroom"), Jump("left_hall_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
