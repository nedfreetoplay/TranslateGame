screen assembly_hall():
    use mods_screens_hook("assembly_hall")

    if M_dewitt.is_state([S_dewitt_paint_trail, S_dewitt_check_up, S_dewitt_eve_meet_up, S_dewitt_erik_get_beer]):
        add "backgrounds/location_school_assembly_hall_paint.jpg"

    elif M_dewitt.is_state([S_dewitt_attend_talent_show, S_dewitt_talent_show]):
        add "backgrounds/location_school_assembly_hall_talentshow.jpg"

    else:
        add game.timer.image("backgrounds/location_school_assembly_hall_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (761,348)
        idle game.timer.image("objects/object_door_111{}.png")
        hover HoverImage(game.timer.image("objects/object_door_111{}.png"))
        action Hide("assembly_hall"), Function(renpy.call, "school_lock_check", "School Right Hallway", "right_hall_dialogue")

    if M_dewitt.is_state(S_dewitt_attend_talent_show):
        imagebutton:
            focus_mask True
            pos (431,262)
            idle "objects/character_dewitt_05.png"
            hover HoverImage("objects/character_dewitt_05.png")
            action Hide("assembly_hall"), Jump(game.dialog_select("assembly_hall_dewitt_attend_talent_show"))

    elif M_dewitt.is_state(S_dewitt_talent_show):
        imagebutton:
            focus_mask True
            pos (431,262)
            idle "objects/character_dewitt_05.png"
            action NullAction()

        imagebutton:
            focus_mask True
            pos (9,369)
            idle "objects/character_kevin_03.png"
            hover HoverImage("objects/character_kevin_03.png")
            action Hide("assembly_hall"), Jump(game.dialog_select("assembly_hall_dewitt_talent_show"))

screen dewitt_bj_options():
    if M_dewitt.get("sex speed") < .175:
        imagebutton:
            focus_mask True
            pos (250,615)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Function(M_dewitt.set, "sex speed", M_dewitt.get("sex speed") + 0.05)

    if M_dewitt.get("sex speed") > .076:
        imagebutton:
            focus_mask True
            pos (450,615)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Function(M_dewitt.set, "sex speed", M_dewitt.get("sex speed") - 0.05)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
