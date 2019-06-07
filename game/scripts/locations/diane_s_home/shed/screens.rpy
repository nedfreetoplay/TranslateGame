screen dianes_shed():
    use mods_screens_hook("dianes_shed")

    add game.timer.image("backgrounds/location_diane_shed01_day{}.jpg")

    if player.location.is_here(M_diane)and not M_dewitt.is_state(S_dewitt_shed_get_paint):
        imagebutton:
            focus_mask True
            pos (670,280)
            idle "objects/character_diane_04.png"
            hover HoverImage("objects/character_diane_04.png")
            action Hide("dianes_shed"), Jump(game.dialog_select("aunt_button_dialogue"))

    if M_diane.is_state(S_diane_delivery_3_fetch_goods):
        imagebutton:
            focus_mask True
            pos (20,580)
            idle "objects/object_milk_01.png"
            hover HoverImage("objects/object_milk_01.png")
            action Hide("dianes_shed"), Jump("dianes_shed_got_milk_delivery_3")

    if M_diane.is_state(S_diane_delivery_2_fetch_goods):
        imagebutton:
            focus_mask True
            pos (588,598)
            idle "objects/object_milk_02.png"
            hover HoverImage("objects/object_milk_02.png")
            action Hide("dianes_shed"), Function(player.get_item, "milk_carton"), Function(M_diane.trigger, T_diane_found_delivery_2_goods), Jump("dianes_shed_pick_up_milk_delivery_02")

    if M_dewitt.is_state(S_dewitt_shed_get_paint):
        imagebutton:
            focus_mask True
            pos (58,608)
            idle "objects/object_paint_01.png"
            hover HoverImage("objects/object_paint_01.png")
            action Hide("dianes_shed"), Jump(game.dialog_select("dianes_shed_dewitt_paint"))

    if M_diane.is_state(S_diane_dump_pump):
        if not M_diane.get("acquired milk"):
            imagebutton:
                focus_mask True
                pos (98,602)
                idle "objects/object_jug_01.png"
                hover HoverImage("objects/object_jug_01.png")
                action Hide("dianes_shed"), Jump(game.dialog_select("dianes_shed_get_milk_to_dump"))

        imagebutton:
            focus_mask True
            pos (35,568)
            idle "objects/object_jug_02.png"
            hover HoverImage("objects/object_jug_02.png")
            action Hide("dianes_shed"), Jump(game.dialog_select("dianes_shed_dump_milk"))

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_07.png"
        hover HoverImage("boxes/auto_option_07.png")
        action Hide("dianes_shed"), If(M_diane.finished_state(S_diane_barn_news), Jump("barn_garden_dialogue"), Jump("dianes_garden_dialogue"))

screen pump_popup():
    imagebutton:
        idle "boxes/popup_item_pump.png"
        action Hide("pump_popup")

screen milk_popup():
    imagebutton:
        idle "boxes/popup_item_milk.png"
        action Hide("milk_popup")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
