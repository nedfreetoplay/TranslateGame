screen computer_lab():
    use mods_screens_hook("computer_lab")

    add game.timer.image("backgrounds/location_school_computer_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (15,288)
        idle game.timer.image("objects/object_door_76{}.png")
        hover HoverImage(game.timer.image("objects/object_door_76{}.png"))
        action Hide("computer_lab"), Play("audio", sfxDoor()), Jump("stairs_dialogue")

    imagebutton:
        focus_mask True
        pos (415,445)
        idle game.timer.image("objects/object_printer01{}.png")
        hover HoverImage(game.timer.image("objects/object_printer01{}.png"))
        action If(game.timer.is_morning() or game.timer.is_afternoon(), [Hide("computer_lab"), Jump("printer_dialogue")])

    if player.location.is_here(M_june):
        if player.location.is_here(M_erik) and not M_bissette.is_state(S_bissette_fix_printer) and not M_okita.is_state(S_okita_get_controller, S_okita_get_controller_info, S_okita_faptic_engine):
            imagebutton:
                focus_mask True
                pos (678,343)
                idle "objects/character_june_03.png"
                hover HoverImage("objects/character_june_03.png")
                action Hide("computer_lab"), Jump("erik_dialogue")

        else:
            imagebutton:
                focus_mask True
                pos (675,395)
                idle "objects/character_june_01.png"
                hover HoverImage("objects/character_june_01.png")
                action Hide("computer_lab"), Jump("june_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
