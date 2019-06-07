screen church_cloister_bell():
    use mods_screens_hook("church_cloister_bell")

    add game.timer.image("backgrounds/location_church_bell_day{}.jpg")

    if M_aqua.is_set("bell search"):
        imagebutton:
            focus_mask True
            pos (322,51)
            idle game.timer.image("objects/object_bell_01{}.png")
            hover HoverImage(game.timer.image("objects/object_bell_01{}.png"))
            action Hide("church_cloister_bell"), Jump("church_bell")

    imagebutton:
        focus_mask True
        pos (0,305)
        idle game.timer.image("objects/object_door_96{}.png")
        hover HoverImage(game.timer.image("objects/object_door_96{}.png"))
        action Hide("church_cloister_bell"), Jump("church_stairs_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
