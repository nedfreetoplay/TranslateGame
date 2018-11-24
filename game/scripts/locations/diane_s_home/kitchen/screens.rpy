screen dianes_kitchen:
    add "backgrounds/location_diane_kitchen_empty_day.jpg"

    if M_diane.is_state(S_diane_make_drink):
        imagebutton:
            focus_mask True
            pos (527,255)
            idle "objects/object_note_03.png"
            hover HoverImage("objects/object_note_03.png")
            action Show("object_note_03_closeup")

        imagebutton:
            focus_mask True
            pos (370,408)
            idle "objects/object_drinks_01.png"
            hover HoverImage("objects/object_drinks_01.png")
            action Hide("dianes_kitchen"), Jump(game.dialog_select("kitchen_drink"))

    if L_diane_kitchen.is_here(M_diane):
        imagebutton:
            focus_mask True
            pos (345,219)
            idle "objects/character_diane_02.png"
            hover HoverImage("objects/character_diane_02.png")
            action Hide("dianes_kitchen"), Jump(game.dialog_select("aunt_button_dialogue"))

    if M_diane.is_state(S_diane_fetch_pump) and not player.has_item("pump"):
        imagebutton:
            focus_mask True
            pos (520,390)
            idle "objects/object_pump_01.png"
            hover HoverImage("objects/object_pump_01.png")
            action Hide("dianes_kitchen"), Jump("dianes_kitchen_get_pump")

    if not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (0,260)
            idle "objects/object_door_66.png"
            hover HoverImage("objects/object_door_66.png")
            action [Hide("dianes_kitchen"),  Function(playSound), Jump("dianelobby_dialogue")]

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_07.png"
        hover HoverImage("boxes/auto_option_07.png")
        action [Hide("dianes_kitchen"), Jump(game.dialog_select("dianes_garden_dialogue"))]

    if M_diane.is_state(S_diane_get_cold_towel):
        imagebutton:
            focus_mask True
            pos 878, 373
            idle "objects/object_sink_01.png"
            hover HoverImage("objects/object_sink_01.png")
            action Hide("dianes_kitchen"), Jump(game.dialog_select("dianes_kitchen_get_water"))

screen object_note_03_closeup:
    imagebutton:
        focus_mask None
        pos (0,0)
        idle "objects/closeup_note03.png"
        action Hide("object_note_03_closeup")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
