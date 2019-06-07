screen waterfall():
    use mods_screens_hook("waterfall")

    add game.timer.image("backgrounds/location_forest_waterfall_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (360,400)
        idle game.timer.image("objects/object_cave_01{}.png")
        hover HoverImage(game.timer.image("objects/object_cave_01{}.png"))
        action Hide("waterfall"), Jump("cave_dialogue")

    if M_okita.is_state(S_okita_get_ingredients) and not player.has_picked_up_item("toad"):
        imagebutton:
            focus_mask True
            pos (481,650)
            idle game.timer.image("objects/object_toad_01{}.png")
            hover HoverImage(game.timer.image("objects/object_toad_01{}.png"))
            action Hide("waterfall"), Jump("take_toad")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("waterfall"), Jump("forest_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
