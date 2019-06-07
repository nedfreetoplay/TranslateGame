screen school_second_floor():
    use mods_screens_hook("school_second_floor")

    add game.timer.image("backgrounds/location_school_second_day{}.jpg")

    if M_dewitt.is_state(S_dewitt_paint_trail):
        add "paint_trail_04" at center

    imagebutton:
        focus_mask True
        pos (134,327)
        idle game.timer.image("objects/object_sign_03{}.png")
        hover HoverImage(game.timer.image("objects/object_sign_03{}.png"))
        action Hide("school_second_floor"), Function(renpy.call, "school_lock_check", "School Hall", "school_dialogue")

    imagebutton:
        focus_mask True
        pos (16,420)
        idle game.timer.image("objects/object_door_11{}.png")
        hover HoverImage(game.timer.image("objects/object_door_11{}.png"))
        action Hide("school_second_floor"), Function(renpy.call, "school_lock_check", "School Third Floor", "third_floor_dialogue")

    imagebutton:
        focus_mask True
        pos (610,366)
        idle game.timer.image("objects/object_door_12{}.png")
        hover HoverImage(game.timer.image("objects/object_door_12{}.png"))
        action Hide("school_second_floor"), Function(renpy.call, "school_lock_check", "Cafeteria", "cafeteria_dialogue")

    imagebutton:
        focus_mask True
        pos (471,332)
        idle game.timer.image("objects/object_door_75{}.png")
        hover HoverImage(game.timer.image("objects/object_door_75{}.png"))
        action Hide("school_second_floor"), Function(renpy.call, "school_lock_check", "Computer Lab", "computer_lab_dialogue")

    imagebutton:
        focus_mask True
        pos (864,408)
        idle game.timer.image("objects/object_door_97{}.png")
        hover HoverImage(game.timer.image("objects/object_door_97{}.png"))
        action MoveTo(L_school_teacherslounge)

    if player.location.is_here(M_annie):
        imagebutton:
            focus_mask True
            pos (320,370)
            idle "objects/character_annie_01.png"
            hover HoverImage("objects/character_annie_01.png")
            action Hide("school_second_floor"), Function(renpy.call, "school_lock_check", "Annie", "annie_button_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
