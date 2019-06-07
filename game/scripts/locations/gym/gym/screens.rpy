screen gym():
    use mods_screens_hook("gym")

    add game.timer.image("backgrounds/location_gym_day{}.jpg")

    if player.location.is_here(M_kevin):
        imagebutton:
            focus_mask True
            pos (136,378)
            idle "objects/object_bench_01c.png"
            hover HoverImage("objects/object_bench_01c.png")
            action Hide("gym"), Jump("kevin_button_dialogue_gym")
    else:
        imagebutton:
            focus_mask True
            pos (136,458)
            idle "objects/object_bench_01.png"
            hover HoverImage("objects/object_bench_01.png")
            action Hide("gym"), Jump("cant_solo_lift")

    imagebutton:
        pos (32,380)
        focus_mask True
        idle "images/objects/character_cedric_01.png"
        hover HoverImage("images/objects/character_cedric_01.png")
        action Hide("gym"), Jump("cedric_button_dialogue")

    imagebutton:
        focus_mask True
        pos (414,383)
        idle "objects/object_door_10.png"
        hover HoverImage("objects/object_door_10.png")
        action Hide("gym"), Jump("yoga_room")

    if player.location.is_here(M_somrak):
        if not M_somrak.finished_state(S_somrak_waiting_a) or game.timer.is_morning():
            imagebutton:
                focus_mask True
                pos (498,0)
                idle "objects/object_bag_01_morning.png"
                hover HoverImage("objects/object_bag_01_morning.png")
                action TalkTo(M_somrak)
        else:
            imagebutton:
                focus_mask True
                pos (498,0)
                idle "objects/object_bag_01.png"
                hover HoverImage("objects/object_bag_01.png")
                action TalkTo(M_somrak)

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("gym"), Jump("gym_front")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
