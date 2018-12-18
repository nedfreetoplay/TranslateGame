screen treehouse:
    add game.timer.image("backgrounds/location_treehouse_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (309,71)
        idle game.timer.image("objects/object_treehouse_01{}.png")
        hover HoverImage(game.timer.image("objects/object_treehouse_01{}.png"))
        action Hide("treehouse"), Jump("treehouse_closeup_dialogue")

    if not player.has_item("wood_pile") and (M_ross.is_state(S_ross_get_easels) or M_dewitt.is_state([S_dewitt_garage_find_paint, S_dewitt_ask_deb_paint, S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint, S_dewitt_make_replacement_guitar])):
        imagebutton:
            focus_mask True
            pos (145,684)
            idle game.timer.image("objects/object_pile_01{}.png")
            hover HoverImage(game.timer.image("objects/object_pile_01{}.png"))
            action Hide("treehouse"), Jump("treehouse_got_wood_pile")

screen treehouse_closeup:
    add game.timer.image("backgrounds/location_treehouse_closeup_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (502,39)
        idle game.timer.image("objects/object_door_83{}.png")
        hover HoverImage(game.timer.image("objects/object_door_83{}.png"))
        action Hide("treehouse_closeup"), Jump("treehouse_interior_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("treehouse_closeup"), Jump("treehouse_dialogue")

screen treehouse_interior:
    add game.timer.image("backgrounds/location_treehouse_inside_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (467,661)
        idle game.timer.image("objects/object_door_84{}.png")
        hover HoverImage(game.timer.image("objects/object_door_84{}.png"))
        action Hide("treehouse_interior"), Jump("treehouse_closeup_dialogue")

    if M_okita.is_state((S_okita_get_controller, S_okita_get_controller_info)) and not player.has_picked_up_item("controller"):
        imagebutton:
            focus_mask True
            pos (536,539)
            idle game.timer.image("objects/object_controller_01{}.png")
            hover HoverImage(game.timer.image("objects/object_controller_01{}.png"))
            action Hide("treehouse_interior"), Jump("treehouse_got_controller")

    imagebutton:
        focus_mask True
        pos (20,676)
        idle game.timer.image("objects/object_box_03{}.png")
        hover HoverImage(game.timer.image("objects/object_box_03{}.png"))
        action Hide("treehouse_interior"), Hide("ui"), Show("treehouse_box")

screen treehouse_box:
    add "backgrounds/location_treehouse_box.jpg"

    if not player.has_item("lure01"):
        imagebutton:
            focus_mask True
            pos (450,390)
            idle "objects/object_lure_01.png"
            hover HoverImage("objects/object_lure_01.png")
            action Hide("treehouse_box"), Jump("lure_02")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("treehouse_box"), Jump("treehouse_interior_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
