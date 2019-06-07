screen trailer_interior():
    use mods_screens_hook("trailer_interior")

    add game.timer.image("backgrounds/location_trailer_interior_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (0,0)
        idle game.timer.image("objects/object_door_86{}.png")
        hover HoverImage(game.timer.image("objects/object_door_86{}.png"))
        action Hide("trailer_interior"), Function(renpy.call, "trailer_lock_check", "trailer")

    imagebutton:
        focus_mask True
        pos (411,312)
        idle game.timer.image("objects/object_door_87{}.png")
        hover HoverImage(game.timer.image("objects/object_door_87{}.png"))
        action Hide("trailer_interior"), Function(playSound), Function(renpy.call, "trailer_lock_check", "trailer_bedroom")

    if player.location.is_here(M_crystal):
        imagebutton:
            focus_mask True
            pos (690,288)
            idle "objects/character_crystal_01.png"
            hover HoverImage("objects/character_crystal_01.png")
            action Hide("trailer_interior"), Jump("roxmom_dialogue")

screen crystal_sex_options():
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("crystal_sex_options"), Jump("trailer_interior_crystal_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("crystal_sex_options"), Jump("trailer_interior_crystal_sex_cum")

    if anim_toggle:
        if M_crystal.get("sex speed") < .175:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("crystal_sex_options"), Function(M_crystal.set, "sex speed", M_crystal.get("sex speed") + 0.05), Jump("trailer_interior_crystal_sex_loop")

        if M_crystal.get("sex speed") > .076:
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("crystal_sex_options"), Function(M_crystal.set, "sex speed", M_crystal.get("sex speed") - 0.05), Jump("trailer_interior_crystal_sex_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
