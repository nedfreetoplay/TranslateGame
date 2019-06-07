screen police_basement():
    use mods_screens_hook("police_basement")

    add "backgrounds/location_police_basement.jpg"

    imagebutton:
        focus_mask True
        pos (841,224)
        idle "images/objects/object_door_51.png"
        hover HoverImage("images/objects/object_door_51.png")
        action Hide("police_basement"), If(M_mia.get_state() == S_mia_inmate_status, Jump("inmate_transfer_block"), Jump("police_lobby_dialogue"))

    if player.location.is_here(M_yumi):
        imagebutton:
            focus_mask True
            pos (536,418)
            idle "images/objects/character_yumi_01.png"
            hover HoverImage("images/objects/character_yumi_01.png")
            action Hide("police_basement"), Jump("police_yumi_dialogue")

    if M_roxxy.get("trailer foreclosed") and M_roxxy.finished_state(S_roxxy_check_trailer):
        imagebutton:
            focus_mask True
            pos (318,291)
            idle "images/objects/object_cell_04.png"
            hover HoverImage("images/objects/object_cell_04.png")
            action Hide("police_basement"), Jump("crystal_cell_button")

    elif erik.over(erik_thief):
        imagebutton:
            focus_mask True
            pos (318,291)
            idle "images/objects/object_cell_03.png"
            hover HoverImage("images/objects/object_cell_03.png")
            action Hide("police_basement"), Jump("police_cell_larry_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (314,286)
            idle "images/objects/object_cell_01.png"
            hover HoverImage("images/objects/object_cell_01.png")
            action Hide("police_basement"), Jump("police_cell_dialogue")

    imagebutton:
        focus_mask True
        pos (31,237)
        idle "images/objects/object_cell_02.png"
        hover HoverImage("images/objects/object_cell_02.png")
        action Hide("police_basement"), Jump("police_cell_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
