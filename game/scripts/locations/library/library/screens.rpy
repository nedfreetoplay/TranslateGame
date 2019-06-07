screen library():
    use mods_screens_hook("library")

    add "backgrounds/location_library_day.jpg"

    imagebutton:
        focus_mask True
        pos (513,354)
        idle "objects/object_shelf_03.png"
        hover HoverImage("objects/object_shelf_03.png")
        action Hide("library"), Jump("library_bookshelf")

    if player.location.is_here(M_mia):
        imagebutton:
            focus_mask True
            pos (24,402)
            idle "objects/character_mia_05.png"
            hover HoverImage("objects/character_mia_05.png")
            action Hide("library"), If(
                                       M_bissette.get_state() == S_bissette_reference_book_search,
                                       Jump("poem_assignment_lock"),
                                       Jump("mia_library_dialogue")
            )

    imagebutton:
        focus_mask True
        pos (104,378)
        idle "objects/object_desk_05.png"
        hover HoverImage("objects/object_desk_05.png")
        action Show("desk05_options")

    imagebutton:
        focus_mask True
        pos (636,349)
        idle "objects/object_door_29.png"
        hover HoverImage("objects/object_door_29.png")
        action Hide("library"), If(
                                   M_bissette.get_state() == S_bissette_get_dictionary and player.has_item("french_dictionary"),
                                   Jump("check_out_lock"),
                                   If(
                                      M_bissette.get_state() == S_bissette_find_poem_reference_book and player.location.is_here(M_mia),
                                      Jump("poem_assignment_lock"),
                                      Jump("backroom_dialogue")
                                   )
        )

    imagebutton:
        focus_mask True
        pos (803,324)
        idle "objects/object_door_55.png"
        hover HoverImage("objects/object_door_55.png")
        action Hide("library"), If(
                                   M_bissette.get_state() == S_bissette_get_dictionary and player.has_item("french_dictionary"),
                                   Jump("check_out_lock"),
                                   If(
                                      M_bissette.get_state() in [S_bissette_find_poem_reference_book, S_bissette_reference_book_search] and player.location.is_here(M_mia),
                                      Jump("poem_assignment_lock"),
                                      Jump("meeting_room_dialogue")
                                   )
        )

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("library"), If(
                                   M_bissette.get_state() == S_bissette_get_dictionary and player.has_item("french_dictionary"),
                                   Jump("check_out_lock"),
                                   If(
                                      M_bissette.get_state() in [S_bissette_find_poem_reference_book, S_bissette_reference_book_search] and player.location.is_here(M_mia),
                                      Jump("poem_assignment_lock"),
                                      Jump("library_front")
                                   )
        )

screen library_bookshelf():
    use mods_screens_hook("library_bookshelf")

    add "library_shelf"

    imagebutton:
        focus_mask True
        pos (742,416)
        idle "buttons/book_01.png"

        action NullAction()

    if M_bissette.get_state() == S_bissette_get_dictionary and not player.has_item("french_dictionary"):
        imagebutton:
            focus_mask True
            pos (190,453)
            idle "buttons/book_04.png"
            hover HoverImage("buttons/book_04.png")
            action Hide("library_bookshelf"), Jump("french_dictionary")

    if M_diane.is_state(S_diane_check_bookshelf):
        imagebutton:
            focus_mask True
            pos (234,110)
            idle "buttons/book_02.png"
            hover HoverImage("buttons/book_02.png")
            action Hide("library_bookshelf"), Jump(game.dialog_select("breeding_guide"))

    if mrsj.started(mrsj_sex_ed) and not player.has_item("kamasutra"):
        imagebutton:
            focus_mask True
            pos (406,440)
            idle "buttons/book_03.png"
            hover HoverImage("buttons/book_03.png")
            action Hide("library_bookshelf"), Jump("kamasutra")

    if not player.has_item("old_book"):
        imagebutton:
            focus_mask True
            pos (836,108)
            idle "buttons/book_05.png"
            hover HoverImage("buttons/book_05.png")
            action Hide("library_bookshelf"), Jump("library_old_book")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_04.png"
        hover HoverImage("boxes/auto_option_04.png")
        action Hide("library_bookshelf"), Jump("library_dialogue")

screen desk05_options():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("desk05_options")]

    imagebutton:
        focus_mask True
        align (0.5,0.82)
        idle "boxes/desk05_option_01.png"
        hover HoverImage("boxes/desk05_option_01.png")
        action Hide("desk05_options"), Hide("library"), Jump("library_desk_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
