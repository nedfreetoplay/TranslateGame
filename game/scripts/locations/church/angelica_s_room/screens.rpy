screen angelicas_room():
    use mods_screens_hook("angelicas_room")

    add game.timer.image("backgrounds/location_church_nun_day{}.jpg")

    if M_mia.get_state() == S_mia_church_plan and game.timer.is_weekend() and game.timer.is_morning():
        imagebutton:
            focus_mask True
            pos (52,205)
            idle "objects/object_robe_01.png"
            hover HoverImage("objects/object_robe_01.png")
            action Hide("angelicas_room"), Jump("priest_outfit")

    if player.location.is_here(M_angelica, M_helen):
        imagebutton:
            focus_mask True
            pos (225,270)
            if M_mia.get_state() in [S_mia_angelicas_order, S_mia_angelicas_whip]:
                idle "objects/character_angelica_05.png"
                hover HoverImage("objects/character_angelica_05.png")

            else:
                idle "objects/character_angelica_04.png"
                hover HoverImage("objects/character_angelica_04.png")
            action Hide("angelicas_room"), Jump("angelicas_room_dialogue")

    elif player.location.is_here(M_angelica):
        imagebutton:
            focus_mask True
            pos (225,270)
            idle "objects/character_angelica_02.png"
            hover HoverImage("objects/character_angelica_02.png")
            action Hide("angelicas_room"), Jump("angelicas_room_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/door11_option_01.png"
        hover HoverImage("boxes/door11_option_01.png")
        action Hide("angelicas_room"), Jump("church_stairs_dialogue")

screen final_sacrament_watch_angelica_options():
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("final_sacrament_watch_angelica_options"), Jump("helen_final_sacrament_watch_angelica_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("final_sacrament_watch_angelica_options"), Jump("helen_final_sacrament_watch_angelica_cum")

    if M_helen.get("sex speed") < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("final_sacrament_watch_angelica_options"), Function(M_helen.set, "sex speed", M_helen.get("sex speed") + 0.05), Jump("helen_final_sacrament_watch_angelica_loop")

    if M_helen.get("sex speed") > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("final_sacrament_watch_angelica_options"), Function(M_helen.set, "sex speed", M_helen.get("sex speed") - 0.05), Jump("helen_final_sacrament_watch_angelica_loop")

screen final_sacrament_fuck_helen_options():
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("final_sacrament_fuck_helen_options"), Jump("helen_final_sacrament_fuck_helen_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("final_sacrament_fuck_helen_options"), Jump("helen_final_sacrament_fuck_helen_cum")

    if M_helen.get("sex speed") < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("final_sacrament_fuck_helen_options"), Function(M_helen.set, "sex speed", M_helen.get("sex speed") + 0.05), Jump("helen_final_sacrament_fuck_helen_loop")

    if M_helen.get("sex speed") > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("final_sacrament_fuck_helen_options"), Function(M_helen.set, "sex speed", M_helen.get("sex speed") - 0.05), Jump("helen_final_sacrament_fuck_helen_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
