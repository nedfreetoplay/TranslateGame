screen trailer():
    use mods_screens_hook("trailer")

    add game.timer.image("backgrounds/location_trailer{}.jpg")

    if player.location.is_here(M_clyde):
        imagebutton:
            focus_mask True
            pos (347,373)
            idle game.timer.image("objects/character_clyde_02{}.png")
            hover HoverImage(game.timer.image("objects/character_clyde_02{}.png"))
            action Hide("trailer"), Jump("clyde_button_dialogue")

    if player.location.is_here(M_roxxy):
        imagebutton:
            focus_mask True
            pos (622,412)
            idle "objects/character_roxxy_01.png"
            hover HoverImage("objects/character_roxxy_01.png")
            action Hide("trailer"), Function(renpy.call, "trailer_lock_check", "roxxy_trailer_button")

    if M_roxxy.get("trailer foreclosed"):
        imagebutton:
            focus_mask True
            pos (771,319)
            idle game.timer.image("objects/object_door_85b{}.png")
            hover HoverImage(game.timer.image("objects/object_door_85b{}.png"))
            action Hide("trailer"), Jump("trailer_foreclosed_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (787,320)
            idle game.timer.image("objects/object_door_85{}.png")
            hover HoverImage(game.timer.image("objects/object_door_85{}.png"))
            action Hide("trailer"), If(game.timer.is_dark, Function(playSound), NullAction()), Function(renpy.call, "trailer_lock_check", "trailer_interior")

    imagebutton:
        focus_mask True
        align 0.5,0.97
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("trailer"), Function(renpy.call, "trailer_lock_check", "trailer_park")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
