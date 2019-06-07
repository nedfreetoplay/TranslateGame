screen tattoo_parlor():
    use mods_screens_hook("tattoo_parlor")

    add game.timer.image("backgrounds/location_tattoo_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (419,357)
        idle game.timer.image("objects/object_door_89{}.png")
        hover HoverImage(game.timer.image("objects/object_door_89{}.png"))
        action Hide("tattoo_parlor"), If(game.timer.is_dark, Function(playSound), NullAction()), Jump("tattoo_parlor_interior_dialogue")

    imagebutton:
        focus_mask True
        pos (643,138)
        idle game.timer.image("objects/object_stairs_04{}.png")
        hover HoverImage(game.timer.image("objects/object_stairs_04{}.png"))
        action Show("popup_unfinished")

screen tattoo_parlor_interior():
    use mods_screens_hook("tattoo_parlor_interior")

    add game.timer.image("backgrounds/location_tattoo_indoor_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (9,280)
        idle game.timer.image("objects/object_door_90{}.png")
        hover HoverImage(game.timer.image("objects/object_door_90{}.png"))
        action Hide("tattoo_parlor_interior"), Jump("tattoo_parlor_dialogue")

    if player.location.is_here(M_grace):
        imagebutton:
            focus_mask True
            pos (905,343)
            idle "objects/character_grace_01.png"
            hover HoverImage("objects/character_grace_01.png")
            action Hide("tattoo_parlor_interior"), Jump("grace_dialogue")

    if M_ross.is_state(S_ross_get_paint_grace) and not player.has_item("paint"):
        imagebutton:
            focus_mask True
            pos (627,563)
            idle "objects/object_boxes_01.png"
            hover HoverImage("objects/object_boxes_01.png")
            action If(M_ross.get("talked to grace") and not player.has_item("paint"), [Hide("tattoo_parlor_interior"), Jump("tattoo_pick_up_boxes")])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
