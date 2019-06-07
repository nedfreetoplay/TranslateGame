screen dealership():
    use mods_screens_hook("dealership")

    add L_dealership.background

    imagebutton:
        focus_mask True
        pos (321,441)
        idle "objects/character_josephine_01.png"
        hover HoverImage("objects/character_josephine_01.png")
        action Hide("dealership"), Jump("josephine_button_dealership_dialogue")

    imagebutton:
        focus_mask True
        pos (730,441)
        idle "objects/character_kim_01.png"
        hover HoverImage("objects/character_kim_01.png")
        action Hide("dealership"), Jump("kim_button_dialogue")

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("dealership"), Jump("dealership_front_dialogue")

screen dealership_front():
    use mods_screens_hook("dealership_front")

    add L_dealership_front.background

    imagebutton:
        focus_mask True
        pos (643,431)
        idle game.timer.image("objects/object_door_38{}.png")
        hover HoverImage(game.timer.image("objects/object_door_38{}.png"))
        action Hide("dealership_front"), Jump("dealership_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
