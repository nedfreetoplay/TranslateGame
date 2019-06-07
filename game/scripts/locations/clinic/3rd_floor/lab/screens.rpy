screen hospital_laboratory():
    use mods_screens_hook("hospital_laboratory")

    add L_hospital_lab.background

    imagebutton:
        focus_mask True
        pos (497,320)
        idle "objects/object_door_137.png"
        hover HoverImage("objects/object_door_137.png")
        action Hide("hospital_laboratory"), Jump("hospital_third_floor_dialogue")

    if L_hospital_lab.is_here(M_priya):
        imagebutton:
            focus_mask True
            pos (47,367)
            idle "objects/character_priya_01.png"
            hover HoverImage("objects/character_priya_01.png")
            action Hide("hospital_laboratory"), Jump("priya_button_dialogue")

    if not player.has_picked_up_item("fertility_pills"):
        imagebutton:
            focus_mask True
            pos (657,545)
            idle "objects/object_pills_01.png"
            hover HoverImage("objects/object_pills_01.png")
            action Hide("hospital_laboratory"), Jump("hospital_laboratory_take_pills_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
