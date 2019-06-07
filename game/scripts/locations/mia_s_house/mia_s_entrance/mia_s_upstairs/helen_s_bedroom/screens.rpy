screen helens_bedroom():
    use mods_screens_hook("helens_bedroom")

    if M_helen.get_state() == S_helen_master_servant_fun:
        add "backgrounds/location_mia_house_helen_closed.jpg"

    else:
        add game.timer.image("backgrounds/location_mia_house_helen_day{}.jpg")

    if M_mia.get_state() == S_mia_midnight_help:
        imagebutton:
            focus_mask True
            pos (864,436)
            idle "objects/object_statue_01.png"
            hover HoverImage("objects/object_statue_01.png")
            action Hide("helens_bedroom"), Jump("helens_mary_statue")

    if player.location.is_here(M_helen):
        imagebutton:
            focus_mask True
            if not M_mia.is_set('helen button change'):
                pos (170,400)
                if M_helen.get_state() in [S_helen_master_servant_fun, S_helen_end]:
                    idle "objects/character_helen_02.png"
                    hover HoverImage("objects/character_helen_02.png")

                else:
                    idle game.timer.image("objects/character_helen_01{}.png")
                    hover HoverImage(game.timer.image("objects/character_helen_01{}.png"))

            else:
                pos (340,470)
                idle game.timer.image("objects/character_helen_03{}.png")
                hover HoverImage(game.timer.image("objects/character_helen_03{}.png"))
            action Hide("helens_bedroom"), Jump("helen_button_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("helens_bedroom"), Jump("mias_upstairs")

screen helen_bedroom_sex_options():
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("helens_bedroom"), Jump("helen_bedroom_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("helens_bedroom"), Jump("helen_bedroom_sex_cum")

    if M_helen.get("sex speed") < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("helens_bedroom"), Function(M_helen.set, "sex speed", M_helen.get("sex speed") + 0.05), Jump("helen_bedroom_sex_loop")

    if M_helen.get("sex speed") > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("helens_bedroom"), Function(M_helen.set, "sex speed", M_helen.get("sex speed") - 0.05), Jump("helen_bedroom_sex_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
