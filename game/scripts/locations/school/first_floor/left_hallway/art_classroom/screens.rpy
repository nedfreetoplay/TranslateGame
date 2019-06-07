screen art_classroom():
    use mods_screens_hook("art_classroom")

    add game.timer.image("backgrounds/location_school_art_day{}.jpg")

    if player.location.is_here(M_judith):
        imagebutton:
            focus_mask True
            pos (571,399)
            idle "objects/character_judith_02.png"
            hover HoverImage("objects/character_judith_02.png")
            action NullAction()

    imagebutton:
        focus_mask True
        pos (431,277)
        idle game.timer.image("objects/object_door_60{}.png")
        hover HoverImage(game.timer.image("objects/object_door_60{}.png"))
        action Hide("art_classroom"), Play("audio", sfxDoor()), Jump("leave_art_classroom")

    if not game.timer.is_dark():
        if player.location.is_here(M_ross):
            imagebutton:
                focus_mask True
                pos (135,315)
                idle "objects/character_ross_01.png"
                hover HoverImage("objects/character_ross_01.png")
                action Hide("art_classroom"), Jump("ross_button_dialogue")

        if M_mia.get_state() in [S_mia_draw_tattoo, S_mia_show_tattoo]:
            imagebutton:
                focus_mask True
                pos (833,277)
                idle "objects/object_painting_02.png"
                hover HoverImage("objects/object_painting_02.png")
                action Hide("art_classroom"), Jump("easel_dialogue")

        imagebutton:
            focus_mask True
            pos (249,367)
            idle "objects/object_fruits_01.png"
            hover HoverImage("objects/object_fruits_01.png")
            action Show("popup_unfinished")

        if M_ross.is_state(S_ross_grab_clay):
            imagebutton:
                focus_mask True
                pos (592,320)
                idle "objects/object_clay_01.png"
                hover HoverImage("objects/object_clay_01.png")
                action Hide("art_classroom"), Jump("art_classroom_ross_molding_clay_cutscene")


screen tattoos():
    imagebutton:
        focus_mask True
        pos (88,113)
        idle "buttons/tattoo_drawing_01.png"
        hover HoverImage("buttons/tattoo_drawing_01.png")
        action Hide("tattoos"), SetVariable("drawn_tattoo", "tattoo_butterfly"), Return()

    imagebutton:
        focus_mask True
        pos (399,135)
        idle "buttons/tattoo_drawing_02.png"
        hover HoverImage("buttons/tattoo_drawing_02.png")
        action Hide("tattoos"), SetVariable("drawn_tattoo", "tattoo_dolphin"), Return()

    imagebutton:
        focus_mask True
        pos (675,113)
        idle "buttons/tattoo_drawing_03.png"
        hover HoverImage("buttons/tattoo_drawing_03.png")
        action Hide("tattoos"), SetVariable("drawn_tattoo", "tattoo_stars"), Return()

    imagebutton:
        focus_mask True
        pos (98,415)
        idle "buttons/tattoo_drawing_04.png"
        hover HoverImage("buttons/tattoo_drawing_04.png")
        action Hide("tattoos"), SetVariable("drawn_tattoo", "tattoo_flowers"), Return()

    imagebutton:
        focus_mask True
        pos (411,411)
        idle "buttons/tattoo_drawing_05.png"
        hover HoverImage("buttons/tattoo_drawing_05.png")
        action Hide("tattoos"), SetVariable("drawn_tattoo", "tattoo_skull"), Return()

    imagebutton:
        focus_mask True
        pos (702,447)
        idle "buttons/tattoo_drawing_06.png"
        hover HoverImage("buttons/tattoo_drawing_06.png")
        action Hide("tattoos"), SetVariable("drawn_tattoo", "tattoo_cookie"), Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
