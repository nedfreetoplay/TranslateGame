screen hill():
    use mods_screens_hook("hill")

    add game.timer.image("backgrounds/location_hill_day{}.jpg")

    if M_mia.get_state() == S_mia_find_harold:
        imagebutton:
            focus_mask True
            pos (389,398)
            idle "objects/character_harold_02.png"
            hover HoverImage("objects/character_harold_02.png")
            action Hide("hill"), Jump("hill_harolds_car")

    imagebutton:
        focus_mask True
        pos (18,497)
        if not game.timer.is_dark():
            idle "objects/object_treehole_01.png"
            hover HoverImage("objects/object_treehole_01.png")
        else:
            idle "objects/object_treehole_01_night.png"
            hover HoverImage("objects/object_treehole_01_night.png")
        action Hide("hill"), Jump("hill_tree")

    if not player.has_picked_up_item("stick") and M_dewitt.is_state(S_dewitt_make_new_flute):
        imagebutton:
            focus_mask True
            pos (100,700)
            idle game.timer.image("objects/object_stick_01{}.png")
            hover HoverImage(game.timer.image("objects/object_stick_01{}.png"))
            action Hide("hill"), Jump("hill_dewitt_stick")

screen hill_tree():
    imagebutton:
        focus_mask True
        align (0.45,0.65)
        if not game.timer.is_dark():
            idle "objects/object_scroll_01.png"
            hover HoverImage("objects/object_scroll_01.png")
        else:
            idle "objects/object_scroll_01_night.png"
            hover HoverImage("objects/object_scroll_01_night.png")
        action Hide("hill_tree"), Jump("hill_tree_get_scroll")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
