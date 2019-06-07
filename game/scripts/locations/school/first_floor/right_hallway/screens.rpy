screen school_right_hallway():
    use mods_screens_hook("school_right_hallway")

    add game.timer.image("backgrounds/location_school_right_hall_day{}.jpg")

    if M_dewitt.is_state(S_dewitt_paint_trail):
        add "paint_trail_01" at center

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/door07_option_01.png"
        hover HoverImage("boxes/door07_option_01.png")
        action Hide("school_right_hallway"), Jump("school_dialogue")

    imagebutton:
        focus_mask True
        pos (14,205)
        idle game.timer.image("objects/object_locker_02{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_02{}.png"))
        action MoveTo(L_school_locker_eve)

    imagebutton:
        focus_mask True
        pos (127,274)
        idle game.timer.image("objects/object_locker_03{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_03{}.png"))
        action MoveTo(L_school_locker_mia)
    imagebutton:
        focus_mask True
        pos (210,328)
        idle game.timer.image("objects/object_locker_04{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_04{}.png"))
        action MoveTo(L_school_locker_erik)

    imagebutton:
        focus_mask True
        pos (275,370)
        idle game.timer.image("objects/object_locker_05{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_05{}.png"))
        action MoveTo(L_school_locker_ronda)

    imagebutton:
        focus_mask True
        pos (312,387)
        idle game.timer.image("objects/object_door_109{}.png")
        hover HoverImage(game.timer.image("objects/object_door_109{}.png"))
        action Hide("school_right_hallway"), Function(renpy.call, "school_lock_check", "Bridget's Office", "coach_office_dialogue")

    if player.location.is_here(M_eve):
        imagebutton:
            focus_mask True
            pos (498,421)
            idle "objects/character_eve_02.png"
            hover HoverImage("objects/character_eve_02.png")
            action Hide("school_right_hallway"), Function(renpy.call, "school_lock_check", "Eve", "right_hall_eve_button")

    imagebutton:
        focus_mask True
        pos (619,436)
        idle game.timer.image("objects/object_posters_02{}.png")
        hover HoverImage(game.timer.image("objects/object_posters_02{}.png"))
        action Hide("school_right_hallway"), Jump("prom_poster")

    imagebutton:
        focus_mask True
        pos (683,364)
        idle game.timer.image("objects/object_door_110{}.png")
        hover HoverImage(game.timer.image("objects/object_door_110{}.png"))
        action Hide("school_right_hallway"), Function(renpy.call, "school_lock_check", "Assembly Hall", "assembly_hall_dialogue")

    imagebutton:
        focus_mask True
        pos (766,325)
        idle game.timer.image("objects/object_locker_08{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_08{}.png"))
        action MoveTo(L_school_locker_dexter)

    imagebutton:
        focus_mask True
        pos (847,279)
        idle game.timer.image("objects/object_locker_07{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_07{}.png"))
        action MoveTo(L_school_locker_kevin)

    imagebutton:
        focus_mask True
        pos (952,219)
        idle game.timer.image("objects/object_locker_06{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_06{}.png"))
        action MoveTo(L_school_locker_annie)

    if player.location.is_here(M_chad):
        imagebutton:
            focus_mask True
            pos (400,422)
            idle "objects/character_chad_01.png"
            hover HoverImage("objects/character_chad_01.png")
            action Hide("school_right_hallway"), Function(renpy.call, "school_lock_check", "Chad", "chad_button_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
