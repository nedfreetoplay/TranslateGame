screen park_bushes:
    add game.timer.image("backgrounds/location_park_bushes_day{}.jpg")

    if not player.has_picked_up_item("stolen_goods"):
        imagebutton:
            focus_mask True
            pos (32,508)
            idle game.timer.image("objects/object_bag_02{}.png")
            hover HoverImage(game.timer.image("objects/object_bag_02{}.png"))
            action Hide("park_bushes"), Jump("park_bushes_bag_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("park_bushes"), Jump("park_dialogue")

screen park_bushes_bag:
    add "backgrounds/location_park_bag.jpg"

    if not player.has_item("treasure_key"):
        imagebutton:
            focus_mask True
            pos (540,280)
            idle "objects/object_key_02.png"
            hover HoverImage("objects/object_key_02.png")
            action Function(player.get_item, "treasure_key"), Show("popup", Image = "boxes/popup_item_key1.png")

    if player.has_picked_up_item("treasure_key"):
        imagebutton:
            focus_mask True
            pos (350,700)
            idle "boxes/auto_option_generic_01.png"
            hover HoverImage("boxes/auto_option_generic_01.png")
            action Hide("park_bushes_bag"), If(player.has_item("treasure_key"), [Function(player.get_item, "stolen_goods"), Show("popup", Image = "boxes/popup_item_goods.png")], NullAction()), Jump("park_bushes_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
