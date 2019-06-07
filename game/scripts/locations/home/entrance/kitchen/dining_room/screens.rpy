screen dining_room():
    use mods_screens_hook("dining_room")

    add player.location.background

    if L_home_diningroom.is_here(M_jenny) and not M_jenny.pregnancy.gave_birth:
        imagebutton:
            focus_mask True
            pos (159,416)
            idle "characters/jenny/buttons/character_jenny_05[M_jenny.pregnancy.to_string].png"
            hover HoverImage("characters/jenny/buttons/character_jenny_05{}.png".format(M_jenny.pregnancy.to_string))
            action TalkTo(M_jenny)

    else:
        imagebutton:
            focus_mask True
            pos (158,484)
            idle game.timer.image("objects/object_table_02{}.png")
            hover HoverImage(game.timer.image("objects/object_table_02{}.png"))
            action Hide("dining_room"), Function(renpy.call, "home_lock_check", "Dining Room Table", "dining_room_table_dialogue")

    imagebutton:
        focus_mask True
        pos (952,288)
        idle game.timer.image("objects/object_door_45{}.png")
        hover HoverImage(game.timer.image("objects/object_door_45{}.png"))
        action Hide("dining_room"), Function(renpy.call, "home_lock_check", "Kitchen", "home_kitchen_dialogue")

    imagebutton:
        focus_mask True
        pos (27,293)
        idle game.timer.image("objects/object_door_46{}.png")
        hover HoverImage(game.timer.image("objects/object_door_46{}.png"))
        action Hide("dining_room"), Function(renpy.call, "home_lock_check", "Backyard", "backyard_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
