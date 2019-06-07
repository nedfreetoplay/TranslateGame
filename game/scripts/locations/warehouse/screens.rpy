screen warehouse():
    use mods_screens_hook("warehouse")

    add game.timer.image("Backgrounds/location_warehouse_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (341,486)
        idle game.timer.image("objects/object_door_108{}.png")
        hover HoverImage(game.timer.image("objects/object_door_108{}.png"))
        action Show("popup_unfinished")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
