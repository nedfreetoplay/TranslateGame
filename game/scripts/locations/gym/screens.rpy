screen gym_front():
    use mods_screens_hook("gym_front")

    add game.timer.image("backgrounds/location_gym_front_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (520,259)
        idle game.timer.image("objects/object_door_113{}.png")
        hover HoverImage(game.timer.image("objects/object_door_113{}.png"))
        action Hide("gym_front"), Function(playSound), Jump("training_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
