screen science_classroom():
    use mods_screens_hook("science_classroom")


    add game.timer.image("backgrounds/location_school_science_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (407,272)
        idle game.timer.image("objects/object_door_59{}.png")
        hover HoverImage(game.timer.image("objects/object_door_59{}.png"))
        action Hide("science_classroom"), Play("audio", sfxDoor()), Jump("school_dialogue")

    imagebutton:
        focus_mask True
        pos (183,508)
        idle game.timer.image("objects/object_microscope01{}.png")
        hover HoverImage(game.timer.image("objects/object_microscope01{}.png"))
        action Hide("science_classroom"), Jump("science_classroom_microscope_dialogue")

    if player.location.is_here(M_okita):
        imagebutton:
            focus_mask True
            pos (506,338)
            idle game.timer.image("objects/character_okita_01{}.png")
            hover HoverImage(game.timer.image("objects/character_okita_01{}.png"))
            action Hide("science_classroom"), Jump("okita_button_dialogue")

    if player.location.is_here(M_mia):
        imagebutton:
            focus_mask True
            pos (717,389)
            idle "objects/character_mia_03.png"
            hover HoverImage("objects/character_mia_03.png")
            action Hide("science_classroom"), Jump("mia_button_dialogue")

    if player.location.is_here(M_erik):
        imagebutton:
            focus_mask True
            pos (912,390)
            idle "objects/character_erik_03.png"
            hover HoverImage("objects/character_erik_03.png")
            action Hide("science_classroom"), Jump("erik_button_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
