screen church_stairs():
    use mods_screens_hook("church_stairs")

    add game.timer.image("backgrounds/location_church_stairs{}.jpg")

    imagebutton:
        focus_mask True
        pos (775,503)
        idle game.timer.image("objects/object_door_72{}.png")
        hover HoverImage(game.timer.image("objects/object_door_72{}.png"))
        action Hide("church_stairs"), Play("audio", sfxDoor()), Jump("church_dialogue")

    imagebutton:
        focus_mask True
        pos (18,235)
        idle game.timer.image("objects/object_door_73{}.png")
        hover HoverImage(game.timer.image("objects/object_door_73{}.png"))
        action Hide("church_stairs"), Play("audio", sfxDoor()), Jump("church_angelicas_room_dialogue")

    imagebutton:
        focus_mask True
        pos (315,210)
        idle game.timer.image("objects/object_door_74{}.png")
        hover HoverImage(game.timer.image("objects/object_door_74{}.png"))
        action Hide("church_stairs"), Play("audio", sfxDoor()), Jump("church_bell_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
