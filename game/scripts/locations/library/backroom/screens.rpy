screen library_backroom():
    use mods_screens_hook("library_backroom")

    add "backgrounds/location_library_backroom01.jpg"

    if M_bissette.is_state(S_bissette_reference_book_search):
        imagebutton:
            focus_mask True
            pos (376,426)
            idle "objects/object_book_01.png"
            hover HoverImage("objects/object_book_01.png")
            action Hide("library_backroom"), Jump("poem_assignment_book")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_04.png"
        hover HoverImage("boxes/auto_option_04.png")
        action Hide("library_backroom"), Jump("library_dialogue")

screen backroom_couple_sex():
    imagebutton:
        pos (350,700)
        idle "buttons/backroom_stage01_01.png"
        hover HoverImage("buttons/backroom_stage01_01.png")
        action Hide("backroom_couple_sex"), Jump("backroom_couple_finish")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
