screen judith_stage01():
    add "backgrounds/location_school_locker_room_broken_stall_01.jpg"

    imagebutton:
        pos (380,700)
        idle "buttons/judith_stage01_01.png"
        hover HoverImage("buttons/judith_stage01_01.png")
        action Hide("judith_stage01"), Jump("judith_kiss")

screen judith_stage02():
    add "backgrounds/location_school_locker_room_broken_stall_02.jpg"

    imagebutton:
        pos (350,700)
        idle "buttons/judith_stage01_02.png"
        hover HoverImage("buttons/judith_stage01_02.png")
        action Hide("judith_stage01"), Jump("judith_handjob")

screen judith_stage03():
    add "backgrounds/location_school_locker_room_broken_stall_03.jpg"

    imagebutton:
        pos (80,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("judith_stage02"), Jump("judith_keepgoing")

    imagebutton:
        pos (280,700)
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("judith_stage02"), Jump("judith_cum")

    imagebutton:
        pos (480,700)
        idle "buttons/judith_stage01_03.png"
        hover HoverImage("buttons/judith_stage01_03.png")
        action Hide("judith_stage01"), Jump("judith_playwithtits")

    imagebutton:
        pos (680,700)
        idle "buttons/judith_stage01_04.png"
        hover HoverImage("buttons/judith_stage01_04.png")
        action Hide("judith_stage02"), Jump("judith_pullpants")

screen judith_stage04():
    add "backgrounds/location_school_locker_room_broken_stall_04.jpg"

    imagebutton:
        pos (180,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("judith_stage02"), Jump("judith_keepgoing")

    imagebutton:
        pos (380,700)
        idle "buttons/judith_stage01_02.png"
        hover HoverImage("buttons/judith_stage01_02.png")
        action Hide("judith_stage01"), Jump("judith_handjob")


screen school_girls_lockerroom():
    use mods_screens_hook("school_girls_lockerroom")

    add game.timer.image("backgrounds/location_school_locker_room_broken{}.jpg")

    imagebutton:
        focus_mask True
        pos (348,314)
        idle game.timer.image("objects/object_door_32{}.png")
        hover HoverImage(game.timer.image("objects/object_door_32{}.png"))
        action Show("door32_options")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_02.png"
        hover HoverImage("boxes/auto_option_02.png")
        action Hide("school_girls_lockerroom"), Jump("left_hall_dialogue")

screen door32_options():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("door32_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/door32_option_01.png"
        hover HoverImage("boxes/door32_option_01.png")
        action Hide("door32_options"), Hide("school_girls_lockerroom"), Jump("judith_toilet")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
