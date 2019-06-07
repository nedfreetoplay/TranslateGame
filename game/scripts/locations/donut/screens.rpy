screen donut_shop():
    use mods_screens_hook("donut_shop")

    add game.timer.image("backgrounds/location_donut_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (591,443)
        idle game.timer.image("objects/object_door_91{}.png")
        hover HoverImage(game.timer.image("objects/object_door_91{}.png"))
        action Hide("donut_shop"), If(game.timer.is_dark(), Jump("donut_locked"), [Function(playSound), Jump("donut_interior_dialogue")])

screen donut_shop_interior():
    use mods_screens_hook("donut_shop_interior")

    add "backgrounds/location_donut_inside_day.jpg"

    imagebutton:
        focus_mask True
        pos (660,325)
        idle "objects/character_beth_01.png"
        hover HoverImage("objects/character_beth_01.png")
        action Hide("donut_shop_interior"), Jump("beth_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("donut_shop_interior"), Jump("donut_shop_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
