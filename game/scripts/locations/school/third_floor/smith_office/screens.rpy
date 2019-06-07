screen principal_smiths_office():
    use mods_screens_hook("principal_smiths_office")

    if not M_ross.is_set('smith office painting'):
        add game.timer.image("backgrounds/location_school_office_day{}.jpg")

    else:
        add game.timer.image("backgrounds/location_school_office_painting_day{}.jpg")

    if M_diane.is_state(S_diane_delivery_3_fetch_invoice, S_diane_delivery_3_drop_off_goods):
        imagebutton:
            focus_mask True
            pos (449,310)
            idle "principal 24f"
            hover HoverImage("principal 24f")
            action Hide("principal_smiths_office"), Jump("smith_office_smith_delivery_3_dialogue")

        imagebutton:
            focus_mask True
            pos (55,359)
            idle "objects/character_ronda_03.png"
            hover HoverImage("objects/character_ronda_03.png")
            action Hide("principal_smiths_office"), Jump("smith_office_ronda_delivery_3_dialogue")

    else:
        if M_smith.is_state(S_smith_intro):
            imagebutton:
                focus_mask True
                pos (238,227)
                idle "objects/object_desk_03_annie.png"
                hover HoverImage("objects/object_desk_03_annie.png")
                action Hide("principal_smiths_office"), Jump("principals_office_smith_intro")

        elif M_smith.is_state(S_smith_go_to_locker):
            imagebutton:
                focus_mask True
                pos (238,227)
                idle "objects/object_desk_03_annie.png"
                hover HoverImage("objects/object_desk_03_annie.png")
                action Hide("principal_smiths_office"), Jump("principals_office_smith_go_to_locker")

        elif player.location.is_here(M_smith):
            imagebutton:
                focus_mask True
                pos (238,227)
                idle "objects/object_desk_03c.png"
                hover HoverImage("objects/object_desk_03c.png")
                action Hide("principal_smiths_office"), Jump("principals_office_smith_no_desk")

        else:
            imagebutton:
                focus_mask True
                pos (238,387)
                idle game.timer.image("objects/object_desk_03{}.png")
                hover HoverImage(game.timer.image("objects/object_desk_03{}.png"))
                action Show("desk03_options")

        if not (M_okita.is_state(S_okita_get_ingredients) and game.timer.is_afternoon() and game.ui_locked and not player.has_item('tissue')):
            imagebutton:
                focus_mask True
                pos (350,700)
                idle "boxes/auto_option_01.png"
                hover HoverImage("boxes/auto_option_01.png")
                action Hide("principal_smiths_office"), Jump("third_floor_dialogue")

    imagebutton:
        focus_mask True
        pos (847,387)
        idle game.timer.image("objects/object_desk_04{}.png")
        hover HoverImage(game.timer.image("objects/object_desk_04{}.png"))
        action Show("desk04_options")

    if not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (758,553)
            idle game.timer.image("objects/object_garbage_01{}.png")
            hover HoverImage(game.timer.image("objects/object_garbage_01{}.png"))
            action Hide("principal_smiths_office"), Jump("principal_trash")

screen principle_garbage():
    add "backgrounds/location_school_office_garbage.jpg"

    if M_okita.is_state(S_okita_get_ingredients) and not player.has_picked_up_item("tissue"):
        imagebutton:
            focus_mask True
            pos (722,125)
            idle "objects/object_tissue_01.png"
            hover HoverImage("objects/object_tissue_01.png")
            action Hide("principle_garbage"), Jump("tissue_taken")

screen principle_drawer():
    add game.timer.image("backgrounds/location_school_office_drawer_day{}.jpg")

    if False:
        imagebutton:
            focus_mask True
            pos (110,25)
            idle "objects/object_papers_01.png"
            hover HoverImage("objects/object_papers_01.png")
            action Hide("principle_drawer"), Jump("principle_drawer_diane_delivery_3_fetch_invoice")

    else:
        imagebutton:
            focus_mask None
            pos (110,25)
            idle "objects/object_papers_01.png"
            action NullAction()

        imagebutton:
            focus_mask True
            align 0.5, 0.97
            idle "boxes/auto_option_generic_01.png"
            hover HoverImage("boxes/auto_option_generic_01.png")
            action Hide("principle_drawer"), Jump("office_dialogue")

screen desk03_options():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("desk03_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/desk03_option_01.png"
        hover HoverImage("boxes/desk03_option_01.png")
        action Hide("desk03_options"), Hide("principal_smiths_office"), Jump("desk_open")

screen desk04_options():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("desk04_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/desk04_option_01.png"
        hover HoverImage("boxes/desk04_option_01.png")
        if not player.location.is_here(M_smith):
            action Hide("desk04_options"), Hide("principal_smiths_office"), Jump("principle_drawer")

        else:
            action Hide("desk04_options"), Hide("principal_smiths_office"), Jump("desk03_locked_dialogue")

screen desk_drawer():
    add "backgrounds/location_school_office_desk.jpg"

    if not player.has_picked_up_item("master_key"):
        imagebutton:
            focus_mask True
            pos (505,166)
            idle "objects/object_key_03.png"
            hover HoverImage("objects/object_key_03.png")
            action Jump("masterkey_taken")

    if not player.has_item("keycode_note") and M_okita.is_state(S_okita_get_keycode):

        imagebutton:
            focus_mask True
            pos (339, 394)
            idle "objects/object_note_02.png"
            hover HoverImage("objects/object_note_02.png")
            action Jump("keycode_note_taken")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("desk_drawer"), Jump("office_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
