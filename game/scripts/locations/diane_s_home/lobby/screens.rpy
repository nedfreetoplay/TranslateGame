screen dianes_lobby():
    use mods_screens_hook("dianes_lobby")

    add "backgrounds/location_diane_entrance_day.jpg"

    imagebutton:
        focus_mask True
        pos (700,431)
        idle "objects/object_door_56.png"
        hover HoverImage("objects/object_door_56.png")
        action Hide("dianes_lobby"), Call("diane_house_lock_check", L_diane_yard)

    imagebutton:
        focus_mask True
        pos (26,193)
        idle "objects/object_door_57.png"
        hover HoverImage("objects/object_door_57.png")
        action Hide("dianes_lobby"), Call("diane_house_lock_check", L_diane_kitchen)

    imagebutton:
        focus_mask True
        pos (369,93)
        idle "objects/object_door_58.png"
        hover HoverImage("objects/object_door_58.png")
        action Hide("dianes_lobby"), Play("audio", sfxDoor()), Jump("dianebedroom_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
