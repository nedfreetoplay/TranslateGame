screen entrance:
    add L_home_entrance.background


    if (M_mom.is_state(S_mom_diane_visit) or (M_diane.is_state(S_diane_debbie_evening_visit))) and game.timer.is_evening():
        imagebutton:
            focus_mask True
            pos (699,236)
            idle "objects/object_door_35_evening.png"
            hover HoverImage("objects/object_door_35_evening.png")
            action Hide("entrance"), Function(playSound), Jump("home_kitchen_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (699,236)
            if not game.timer.is_dark():
                idle "objects/object_door_35.png"
                hover HoverImage("objects/object_door_35.png")
            else:
                idle "objects/object_door_35_night.png"
                hover HoverImage("objects/object_door_35_night.png")
            action Hide("entrance"), Function(renpy.call, "home_lock_check", "Kitchen", "home_kitchen_dialogue")

        imagebutton:
            focus_mask True
            pos (141,165)
            idle game.timer.image("objects/object_stairs_02{}.png")
            hover HoverImage(game.timer.image("objects/object_stairs_02{}.png"))
            action Hide("entrance"), Function(renpy.call, "home_lock_check", "Hallway", "hallway_dialogue")

        imagebutton:
            focus_mask True
            pos (0,243)
            if not game.timer.is_dark():
                idle "objects/object_door_39.png"
                hover HoverImage("objects/object_door_39.png")
            else:
                idle "objects/object_door_39_night.png"
                hover HoverImage("objects/object_door_39_night.png")
            action Hide("entrance"), Function(renpy.call, "home_lock_check", "Living Room", "home_livingroom_dialogue")

        if player.location.is_here(M_mom) and M_mom.is_set("chores"):
            imagebutton:
                focus_mask True
                pos (550,350)
                idle "objects/character_debbie_04.png"
                hover HoverImage("objects/character_debbie_04.png")
                action Hide("entrance"), Jump("vacuum_dialogue")

        imagebutton:
            focus_mask True
            pos (350,700)
            idle "boxes/auto_option_08.png"
            hover HoverImage("boxes/auto_option_08.png")
            action Hide("entrance"), Function(renpy.call, "home_lock_check", "Home Front", "home_front")

        if not player.has_picked_up_item("attic_key"):
            imagebutton:
                focus_mask True
                pos (982,356)
                idle game.timer.image("objects/object_key_01{}.png")
                hover HoverImage(game.timer.image("objects/object_key_01{}.png"))
                action Function(player.get_item, "attic_key"), Hide("entrance"), Jump("attic_key")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
