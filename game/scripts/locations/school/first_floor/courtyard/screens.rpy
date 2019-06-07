screen school_courtyard():
    use mods_screens_hook("school_courtyard")

    add game.timer.image("backgrounds/location_school_gym{}.jpg")
    if player.location.is_here(M_ronda):
        imagebutton:
            focus_mask True
            pos (131,402)
            idle "objects/character_ronda_02.png"
            hover HoverImage("objects/character_ronda_02.png")
            action Hide("school_courtyard"), Jump("ronda_button_dialogue")


    if player.location.is_here(M_bridget):
        imagebutton:
            focus_mask True
            pos (600,380)
            idle "objects/character_coach_01.png"
            hover HoverImage("objects/character_coach_01.png")
            action Hide("school_courtyard"), Jump("coach_button_dialogue")

    if player.location.is_here(M_dexter):
        imagebutton:
            focus_mask True
            pos (881,432)
            idle "objects/character_dexter_01.png"
            hover HoverImage("objects/character_dexter_01.png")
            action Hide("school_courtyard"), Jump("dexter_court_dialogue")

    imagebutton:
        align (0.5,0.97)
        idle "boxes/door07_option_01.png"
        hover HoverImage("boxes/door07_option_01.png")
        action Hide("school_courtyard"), Jump("school_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
