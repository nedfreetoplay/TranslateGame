screen boys_locker_shower():
    use mods_screens_hook("boys_locker_shower")

    add game.timer.image("backgrounds/location_school_lockershowers_day{}.jpg")

    if game.timer.game_day() >= 1 and not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (530,300)
            idle "objects/character_latinas_01.png"
            hover HoverImage("objects/character_latinas_01.png")
            action Hide("boys_locker_shower"), Jump("latinas_button_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_02.png"
        hover HoverImage("boxes/auto_option_02.png")
        action Hide("boys_locker_shower"), Jump("locker_room_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
