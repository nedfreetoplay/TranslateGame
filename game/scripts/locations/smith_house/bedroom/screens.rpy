screen smiths_bedroom():
    use mods_screens_hook("smiths_bedroom")

    add L_smith_bedroom.background

    if not player.has_item("smith_exams"):
        imagebutton:
            focus_mask True
            pos (0,229)
            idle game.timer.image("objects/object_door_124{}.png")
            hover HoverImage(game.timer.image("objects/object_door_124{}.png"))
            action Hide("smiths_bedroom"), Jump("smiths_hallway_dialogue")

    if M_roxxy.is_state(S_roxxy_sneak_into_smith) and not player.has_picked_up_item("smith_painting_key"):
        imagebutton:
            focus_mask True
            pos (138,238)
            idle game.timer.image("objects/object_painting_03{}.png")
            hover HoverImage(game.timer.image("objects/object_painting_03{}.png"))
            action Hide("smiths_bedroom"), Jump("smith_painting")

    if M_roxxy.is_state(S_roxxy_sneak_into_smith) and player.has_item("smith_painting_key"):
        imagebutton:
            focus_mask True
            pos (164,406)
            idle game.timer.image("objects/object_cabinet_04{}.png")
            hover HoverImage(game.timer.image("objects/object_cabinet_04{}.png"))
            action Hide("smiths_bedroom"), Show("smiths_bedroom_cabinet")

    if player.has_item("smith_exams"):
        imagebutton:
            focus_mask True
            pos (332,250)
            idle game.timer.image("objects/object_window_01{}.png")
            hover HoverImage(game.timer.image("objects/object_window_01{}.png"))
            action Hide("smiths_bedroom"), Jump("smith_window_exit_dialogue")

screen smiths_bedroom_cabinet():
    add "backgrounds/location_smith_bedroom_cabinet.jpg"

    if not player.has_picked_up_item("smith_exams"):
        imagebutton:
            focus_mask True
            pos (353,528)
            idle "objects/object_exams_01.png"
            hover HoverImage("objects/object_exams_01.png")
            action Hide("smiths_bedroom_cabinet"), Jump("smith_exams")

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("smiths_bedroom_cabinet"), Jump("smiths_bedroom_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
