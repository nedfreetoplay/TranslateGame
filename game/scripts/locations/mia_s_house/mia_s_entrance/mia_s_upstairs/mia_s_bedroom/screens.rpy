screen mias_bedroom():
    use mods_screens_hook("mias_bedroom")

    add game.timer.image("backgrounds/location_mia_bedroom{}.jpg")

    imagebutton:
        focus_mask True
        pos (245,474)
        idle game.timer.image("objects/object_laundry_02{}.png")
        hover HoverImage(game.timer.image("objects/object_laundry_02{}.png"))
        action Hide("mias_bedroom"), Show("mia_bedroom_laundry_basket")

    if player.location.is_here(M_mia):
        imagebutton:
            focus_mask True
            pos (300,300)
            idle "objects/character_mia_01c.png"
            hover HoverImage("objects/character_mia_01c.png")
            action Hide("mias_bedroom"), Jump("mia_button_dialogue")

    imagebutton:
        focus_mask True
        pos (3,492)
        idle "objects/object_teddy_01.png"
        hover HoverImage("objects/object_teddy_01.png")
        action Hide("mias_bedroom"), Jump("mia_bedroom_teddy")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("mias_bedroom"), Jump("mias_upstairs")

screen mia_bedroom_laundry_basket():
    add game.timer.image("backgrounds/location_mia_bedroom_basket{}_closeup.jpg")

    if not player.has_picked_up_item("mia_panties"):
        imagebutton:
            focus_mask True
            pos (395,191)
            idle game.timer.image("objects/object_panties_04{}.png")
            hover HoverImage(game.timer.image("objects/object_panties_04{}.png"))
            action Hide("mia_bedroom_laundry_basket"), Jump("mia_bedroom_panties")

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("mia_bedroom_laundry_basket"), Jump("mias_bedroom_screen")

screen mia_bedroom_sex_options():
    imagebutton:
        focus_mask True
        pos (150,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("mia_bedroom_sex_options"), Jump("mia_bedroom_sex_loop")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("mia_bedroom_sex_options"), Jump("mia_bedroom_sex_cum_outside")

    imagebutton:
        focus_mask True
        pos (550,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("mia_bedroom_sex_options"), Jump("mia_bedroom_sex_cum_inside")

    if anim_toggle:
        if M_mia.get("sex speed") < .175:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("mia_bedroom_sex_options"), Function(M_mia.set, "sex speed", M_mia.get("sex speed") + 0.05), Jump("mia_bedroom_sex_loop")

        if (M_mia.get("sex speed") > .076 and M_mia.is_set("vaginal sex")) or (M_mia.get("sex speed") > .126 and M_mia.get("butt speed") == 1) or (M_mia.get("sex speed") > .076 and M_mia.get("butt speed") > 1):
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("mia_bedroom_sex_options"), If(not M_mia.is_set("vaginal sex"), If(M_mia.get("butt speed") == 1, Function(M_mia.set, "sex speed", .125), Function(M_mia.set, "sex speed", M_mia.get("sex speed") - 0.05)), Function(M_mia.set, "sex speed", M_mia.get("sex speed") - 0.05)), Jump("mia_bedroom_sex_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
