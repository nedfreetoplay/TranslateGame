screen lair_entrance():
    add "backgrounds/location_lair_ocean.jpg"

    imagebutton:
        focus_mask True
        pos (387,433)
        idle "objects/object_lair_01.png"
        hover HoverImage("objects/object_lair_01.png")
        action Hide("lair_entrance"), Jump("maze_pre")

screen lair():
    use mods_screens_hook("lair")

    add "backgrounds/location_lair.jpg"

    if player.location.is_here(M_aqua):
        imagebutton:
            focus_mask True
            pos (291,436)
            idle "objects/object_mount_01.png"
            hover HoverImage("objects/object_mount_01.png")
            action Hide("lair"), Jump("aqua_dialogue")

    if M_aqua.is_set("seasucc available"):
        imagebutton:
            focus_mask True
            pos (5,442)
            idle "objects/object_seathrone_01.png"
            hover HoverImage("objects/object_seathrone_01.png")
            action Hide("lair"), Jump("seasucc_dialogue")

screen aqua_sex_options():
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("aqua_sex_options"), Jump("aqua_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("aqua_sex_options"), Jump("aqua_sex_cum")

    if M_aqua.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("aqua_sex_options"), Function(M_aqua.set, "sex speed", M_aqua.get("sex speed") + 0.05), Jump("aqua_sex_loop")

    if M_aqua.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("aqua_sex_options"), Function(M_aqua.set, "sex speed", M_aqua.get("sex speed") - 0.05), Jump("aqua_sex_loop")

screen seasucc_options():
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("seasucc_options"), Jump("seasucc_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/cam_stage01_02.png"
        hover HoverImage("buttons/cam_stage01_02.png")
        action Hide("seasucc_options"), Jump("seasucc_cum")

    if M_aqua.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("seasucc_options"), Function(M_aqua.set, "sex speed", M_aqua.get("sex speed") + 0.05), Jump("seasucc_loop")

    if M_aqua.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("seasucc_options"), Function(M_aqua.set, "sex speed", M_aqua.get("sex speed") - 0.05), Jump("seasucc_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
