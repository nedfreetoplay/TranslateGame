screen french_classroom():
    use mods_screens_hook("french_classroom")

    add game.timer.image("backgrounds/location_school_french{}.jpg")

    imagebutton:
        focus_mask True
        pos (384,276)
        idle game.timer.image("objects/object_door_07{}.png")
        hover HoverImage(game.timer.image("objects/object_door_07{}.png"))
        action Hide("french_classroom"), Play("audio", sfxDoor()), Jump(game.dialog_select("school_dialogue"))

    if player.location.is_here(M_eve):
        imagebutton:
            focus_mask True
            pos (209,406)
            idle "objects/character_eve_01.png"
            hover HoverImage("objects/character_eve_01.png")
            action Hide("french_classroom"), Jump("eve_classroom_dialogue")

    if player.location.is_here(M_roxxy):
        imagebutton:
            focus_mask True
            pos (886,351)
            idle "objects/character_roxxy_02.png"
            hover HoverImage("objects/character_roxxy_02.png")
            action Hide("french_classroom"), Jump("roxxy_classroom_dialogue")

    if player.location.is_here(M_bissette):
        imagebutton:
            focus_mask True
            pos (747,342)
            idle "objects/character_bissette_01.png"
            hover HoverImage("objects/character_bissette_01.png")
            action Hide("french_classroom"), Jump("bissette_button_dialogue")

    imagebutton:
        focus_mask True
        pos (0,278)
        idle game.timer.image("objects/object_map_02{}.png")
        hover HoverImage(game.timer.image("objects/object_map_02{}.png"))
        action Hide("french_classroom"), Jump("europe_map_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
