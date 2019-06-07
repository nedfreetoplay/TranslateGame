screen school_left_hallway():
    use mods_screens_hook("school_left_hallway")

    add game.timer.image("backgrounds/location_school_lefthall_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (757,297)
        idle game.timer.image("objects/object_door_14{}.png")
        hover HoverImage(game.timer.image("objects/object_door_14{}.png"))
        action [Hide("school_left_hallway"), Function(renpy.call, "school_lock_check", "Utility Closet", "door14_locked_dialogue")]

    imagebutton:
        focus_mask True
        pos (661,281)
        idle game.timer.image("objects/object_door_15{}.png")
        hover HoverImage(game.timer.image("objects/object_door_15{}.png"))
        action [Hide("school_left_hallway"), Function(renpy.call, "school_lock_check", "Boy's Lockerroom", "locker_room_dialogue")]

    imagebutton:
        focus_mask True
        pos (872,172)
        idle game.timer.image("objects/object_door_64{}.png")
        hover HoverImage(game.timer.image("objects/object_door_64{}.png"))
        action [Hide("school_left_hallway"), Function(renpy.call, "school_lock_check", "Art Classroom", "art_classroom_dialogue")]

    imagebutton:
        focus_mask True
        pos (195,281)
        idle game.timer.image("objects/object_door_16{}.png")
        hover HoverImage(game.timer.image("objects/object_door_16{}.png"))
        action [Hide("school_left_hallway"), Function(renpy.call, "school_lock_check", "School Girl's Lockerroom", "girl_lockerroom_dialogue")]

    if player.location.is_here(M_judith):
        imagebutton:
            focus_mask True
            pos (490,370)
            idle "objects/character_judith_01.png"
            hover HoverImage("objects/character_judith_01.png")
            action Hide("school_left_hallway"), Jump("judith_button_dialogue")

    imagebutton:
        focus_mask True
        pos (37,233)
        idle game.timer.image("objects/object_locker_09{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_09{}.png"))
        action MoveTo(L_school_locker_roxxy)

    imagebutton:
        focus_mask True
        pos (133,281)
        idle game.timer.image("objects/object_locker_10{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_10{}.png"))
        action MoveTo(L_school_locker_judith)


    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/door07_option_01.png"
        hover HoverImage("boxes/door07_option_01.png")
        action [Hide("school_left_hallway"), Function(renpy.call, "school_lock_check", "School Hall", "school_dialogue")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
