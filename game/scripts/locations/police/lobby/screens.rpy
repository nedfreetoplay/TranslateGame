screen police_lobby():
    use mods_screens_hook("police_lobby")

    add "backgrounds/location_police_lobby.jpg"

    imagebutton:
        focus_mask True
        pos (151,360)
        idle "images/objects/object_door_49.png"
        hover HoverImage("images/objects/object_door_49.png")
        action Hide("police_lobby"), Jump("police_basement_dialogue")

    imagebutton:
        focus_mask True
        pos (586,376)
        idle "images/objects/object_door_50.png"
        hover HoverImage("images/objects/object_door_50.png")
        action Hide("police_lobby"), Jump("police_office_dialogue")

    imagebutton:
        focus_mask True
        pos (12,338)
        idle "images/objects/object_board_03.png"
        hover HoverImage("images/objects/object_board_03.png")
        action Hide("police_lobby"), Jump("police_board")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
