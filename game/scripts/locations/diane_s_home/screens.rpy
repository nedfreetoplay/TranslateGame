screen dianes_front_yard():
    use mods_screens_hook("dianes_front_yard")

    add game.timer.image("backgrounds/location_diane_front_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (289,382)
        idle game.timer.image("objects/object_door_106{}.png")
        hover HoverImage(game.timer.image("objects/object_door_106{}.png"))
        action Hide("dianes_front_yard"), Call("diane_house_lock_check", L_diane_home)

    imagebutton:
        focus_mask True
        pos (563,482)
        idle game.timer.image("objects/object_door_107{}.png")
        hover HoverImage(game.timer.image("objects/object_door_107{}.png"))
        action Hide("dianes_front_yard"), Call("diane_house_lock_check", L_diane_garden)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
