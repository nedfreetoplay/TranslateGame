screen attic():
    use mods_screens_hook("attic")

    add game.timer.image("backgrounds/location_home_attic_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (214,640)
        idle game.timer.image("objects/object_door_41{}.png")
        hover HoverImage(game.timer.image("objects/object_door_41{}.png"))
        action Hide("attic"), Jump("hallway_dialogue")

    if not player.has_picked_up_item("fishing_rod"):
        imagebutton:
            focus_mask True
            pos (220,365)
            idle game.timer.image("objects/object_rod_01{}.png")
            hover HoverImage(game.timer.image("objects/object_rod_01{}.png"))
            action Function(player.get_item, "fishing_rod"), Hide("attic"), Jump("fishing_rod")

    if not player.has_picked_up_item("ring"):
        imagebutton:
            focus_mask True
            pos (262,198)
            idle game.timer.image("objects/object_ring_01{}.png")
            hover HoverImage(game.timer.image("objects/object_ring_01{}.png"))
            action Function(player.get_item, "ring"), Hide("attic"), Jump("ring")

    imagebutton:
        focus_mask True
        pos (287,500)
        idle game.timer.image("objects/object_safe_01{}.png")
        hover HoverImage(game.timer.image("objects/object_safe_01{}.png"))
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (450,390)
        idle game.timer.image("objects/object_dress_01{}.png")
        hover HoverImage(game.timer.image("objects/object_dress_01{}.png"))
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (807,398)
        idle game.timer.image("objects/object_globe_01{}.png")
        hover HoverImage(game.timer.image("objects/object_globe_01{}.png"))
        action Hide("attic"), With(fade), Jump("globe")

    imagebutton:
        focus_mask True
        pos (128, 638)
        idle game.timer.image("objects/object_picture_01{}.png")
        hover HoverImage(game.timer.image("objects/object_picture_01{}.png"))
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (888,289)
        idle game.timer.image("objects/object_painting_01{}.png")
        hover HoverImage(game.timer.image("objects/object_painting_01{}.png"))
        action Hide("attic"), With(fade), Jump("painting")

    imagebutton:
        focus_mask True
        pos (178,548)
        idle game.timer.image("objects/object_discs_01{}.png")
        hover HoverImage(game.timer.image("objects/object_discs_01{}.png"))
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (739, 618)
        idle game.timer.image("objects/object_carpet_01{}.png")
        hover HoverImage(game.timer.image("objects/object_carpet_01{}.png"))
        action Hide("attic"), Jump("peep_hole_dialogue")

    if not player.has_picked_up_item("cheerleader_outfit"):
        imagebutton:
            focus_mask True
            pos (345,375)
            idle game.timer.image("objects/object_outfit_01{}.png")
            hover HoverImage(game.timer.image("objects/object_outfit_01{}.png"))
            action Hide("attic"), Jump("cheerleader_outfit")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
