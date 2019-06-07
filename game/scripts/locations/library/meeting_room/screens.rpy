screen library_meeting_room():
    use mods_screens_hook("library_meeting_room")

    add "backgrounds/location_library_meeting_day.jpg"

    imagebutton:
        focus_mask True
        pos (418,491)
        idle "objects/object_table_03.png"
        hover HoverImage("objects/object_table_03.png")
        action Hide("library_meeting_room"), Jump("meeting_room_table_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_04.png"
        hover HoverImage("boxes/auto_option_04.png")
        action Hide("library_meeting_room"), Jump("library_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
