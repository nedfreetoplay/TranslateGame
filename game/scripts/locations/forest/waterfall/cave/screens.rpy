screen cave():
    use mods_screens_hook("cave")

    add game.timer.image("backgrounds/location_forest_cave_day{}.jpg")

    if M_okita.is_state(S_okita_get_ingredients) and not player.has_picked_up_item("caveflower") and game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (618,470)
            idle "objects/object_flower_01.png"
            hover HoverImage("objects/object_flower_01.png")
            action Hide("cave"), Jump("take_caveflower")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("cave"), Jump("waterfall_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
