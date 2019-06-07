screen roxxys_locker():
    use mods_screens_hook("roxxys_locker")

    add "roxxy_locker"

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("roxxys_locker"), Jump("left_hall_dialogue")

screen judiths_locker():
    use mods_screens_hook("judiths_locker")

    add "judith_locker"

    if not player.has_picked_up_item("judith_glasses") and M_okita.is_state(S_okita_picture_taken):
        imagebutton:
            focus_mask True
            pos (394,607)
            idle "objects/object_glasses_01.png"
            hover HoverImage("objects/object_glasses_01.png")
            action Hide("judiths_locker"), Jump("take_judith_glasses")

    if not player.has_picked_up_item("broken_flute") and M_dewitt.is_state(S_dewitt_judith_locker_search):
        imagebutton:
            focus_mask True
            pos (584,406)
            idle "objects/object_flute_01.png"
            hover HoverImage("objects/object_flute_01.png")
            action Hide("judiths_locker"), Jump("take_broken_flute")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("judiths_locker"), Jump("left_hall_dialogue")

screen eves_locker():
    use mods_screens_hook("eves_locker")

    add "eve_locker"

    if M_ross.is_set("talked with chad") and not player.has_picked_up_item("eve_drawing"):
        imagebutton:
            focus_mask True
            pos (316,457)
            idle "objects/object_drawing_01.png"
            hover HoverImage("objects/object_drawing_01.png")
            action Hide("eves_locker"), Jump("eve_locker_drawing_pick_up")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("eves_locker"), Jump("right_hall_dialogue")

screen mias_locker():
    use mods_screens_hook("mias_locker")

    add "mia_locker"

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("mias_locker"), Jump("right_hall_dialogue")

screen eriks_locker():
    use mods_screens_hook("eriks_locker")

    add game.timer.image("erik_locker{}")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("eriks_locker"), Jump("right_hall_dialogue")

screen rondas_locker():
    use mods_screens_hook("rondas_locker")

    add "ronda_locker"

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("rondas_locker"), Jump("right_hall_dialogue")

screen dexters_locker():
    use mods_screens_hook("dexters_locker")

    add "dexter_locker"

    if M_bissette.is_set("dexters book search"):
        imagebutton:
            focus_mask True
            pos (725,540)
            idle game.timer.image("objects/object_book_02{}.png")
            hover HoverImage(game.timer.image("objects/object_book_02{}.png"))
            action Hide("dexters_locker"), Return()

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("dexters_locker"), Jump("right_hall_dialogue")

screen kevins_locker():
    use mods_screens_hook("kevins_locker")

    add "kevin_locker"

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("kevins_locker"), Jump("right_hall_dialogue")

screen annies_locker():
    use mods_screens_hook("annies_locker")

    add "annie_locker"

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("annies_locker"), Jump("right_hall_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
