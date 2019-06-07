screen beach():
    use mods_screens_hook("beach")

    add game.timer.image("backgrounds/location_beach_day{}.jpg")

    if not game.timer.is_dark() and M_aqua.is_set("treasure search"):
        imagebutton:
            focus_mask True
            pos (666,569)
            idle "objects/object_island_01.png"
            hover HoverImage("objects/object_island_01.png")
            action MoveTo(L_beach_island)

    imagebutton:
        focus_mask True
        pos (442,317)
        idle game.timer.image("objects/object_tower_01{}.png")
        hover HoverImage(game.timer.image("objects/object_tower_01{}.png"))
        action MoveTo(L_beach_tower)

    imagebutton:
        focus_mask True
        pos (52,527)
        idle game.timer.image("objects/object_umbrella_01{}.png")
        hover HoverImage(game.timer.image("objects/object_umbrella_01{}.png"))
        action MoveTo(L_beach_water)

screen beach_water():
    use mods_screens_hook("beach_water")

    if M_roxxy.is_state(S_roxxy_invite_to_bikini_contest,S_roxxy_check_on_roxxy, S_roxxy_go_see_contest, S_roxxy_in_cabin, S_roxxy_get_new_bikini, S_roxxy_get_oil) and game.timer == Date("afternoon", "saturday"):
        add game.timer.image("backgrounds/location_beach_water_contest{}.jpg")
        if not M_roxxy.is_state(S_roxxy_check_on_roxxy ,S_roxxy_in_cabin, S_roxxy_get_new_bikini, S_roxxy_get_oil):
            imagebutton:
                focus_mask True
                pos (201,297)
                idle "objects/character_terry_07.png"
                hover HoverImage("objects/character_terry_07.png")
                action Hide("beach_water"), Jump("terry_button_contest_dialogue")
        if not player.has_picked_up_item("sara_bikini") and M_roxxy.is_state(S_roxxy_check_on_roxxy, S_roxxy_in_cabin, S_roxxy_get_new_bikini):
            imagebutton:
                focus_mask True
                pos (388,494)
                idle "objects/object_bikini_01.png"
                hover HoverImage("objects/object_bikini_01.png")
                action Hide("beach_water"), Jump("sara_bikini_picked_up")
        if M_roxxy.is_state(S_roxxy_check_on_roxxy):
            imagebutton:
                focus_mask True
                pos (491,434)
                idle "objects/character_roxxy_06.png"
                hover HoverImage("objects/character_roxxy_06.png")
                action Hide("beach_water"), Jump("roxxy_button_showers_dialogue")
        elif not M_roxxy.is_state(S_roxxy_invite_to_bikini_contest, S_roxxy_go_see_contest):
            imagebutton:
                focus_mask True
                pos (491,434)
                idle "objects/character_roxxy_07.png"
                hover HoverImage("objects/character_roxxy_07.png")
                action Hide("beach_water"), Jump("roxxy_button_showers_dialogue")
    else:
        add L_beach_water.background
    imagebutton:
        focus_mask True
        pos (716,380)
        idle game.timer.image("objects/object_cabin_01{}.png")
        hover HoverImage(game.timer.image("objects/object_cabin_01{}.png"))
        action MoveTo(L_beach_cabin)

    if L_beach_water.is_here(M_roxxy) and game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (394,487)
            idle 'objects/character_roxxy_05.png'
            hover HoverImage('objects/character_roxxy_05.png')
            action Hide("beach_water"), Jump("roxxy_beach_button_dialogue")

    imagebutton:
        focus_mask True
        align 0.5,0.97
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_beach)


screen beach_showers():
    use mods_screens_hook("beach_showers")

    add L_beach_showers.background
    imagebutton:
        focus_mask True
        align 0.5,0.97
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_beach_water)


screen beach_cabin():
    use mods_screens_hook("beach_cabin")

    add L_beach_cabin.background
    imagebutton:
        focus_mask True
        align 0.5,0.97
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_beach_water)


screen beach_tower():
    use mods_screens_hook("beach_tower")

    add L_beach_tower.background
    imagebutton:
        focus_mask True
        pos (438,443)
        idle game.timer.image("objects/object_ladder_01{}.png")
        hover HoverImage(game.timer.image("objects/object_ladder_01{}.png"))
        action MoveTo(L_beach)

    if M_roxxy.is_state(S_roxxy_get_oil) and not player.has_item("massage_oil"):
        imagebutton:
            focus_mask True
            pos (292,578)
            idle game.timer.image("objects/object_bottle_01{}.png")
            hover HoverImage(game.timer.image("objects/object_bottle_01{}.png"))
            action Hide("beach_tower"), Jump("beach_tower_oil_pickup")

screen beach_island():
    use mods_screens_hook("beach_island")

    add "backgrounds/location_beach_island_day.jpg"

    imagebutton:
        focus_mask True
        if M_aqua.get_state() == S_aqua_treasure_search:
            pos (409,124)
            idle "objects/object_statue_02.png"
            hover HoverImage("objects/object_statue_02.png")

        else:
            pos (311,124)
            idle "objects/object_statue_03.png"
            hover HoverImage("objects/object_statue_03.png")
        action Hide("beach_island"), With(fade), Jump("beach_statue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action MoveTo(L_beach)

screen treasure_lock():
    default lock01 = 0
    default lock02 = 0
    default lock03 = 0
    default lock04 = 0
    default open_lock = False

    imagemap:
        ground "backgrounds/location_beach_lock.jpg"

        imagebutton:
            focus_mask True
            align (0.99,0.99)
            idle "boxes/auto_option_generic_02.png"
            hover HoverImage("boxes/auto_option_generic_02.png")
            action Hide("treasure_lock"), With(fade), Jump("beach_island_dialogue")

        if lock01 == 1 and lock02 == 5 and lock03 == 1 and lock04 == 3:
            imagebutton:
                focus_mask True
                if not open_lock:
                    pos (460,125)
                    idle PulseHoverImage("objects/object_keyhole_01.png", delay = 2)
                    hover HoverImage("objects/object_keyhole_01.png")
                else:
                    pos (460,74)
                    idle "objects/object_keyhole_02.png"
                action If(player.has_item("treasure_key"), SetScreenVariable("open_lock", True), NullAction()), Hide("treasure_lock"), With(fade), Jump("treasure_open")

        if lock01 > 0:
            imagebutton:
                focus_mask True
                pos (110,407)
                idle "buttons/lock_icon_" + str(lock01).zfill(2) + ".png"
                hover HoverImage("buttons/lock_icon_" + str(lock01).zfill(2) + ".png")
                action If(lock01 < 10, SetScreenVariable("lock01", lock01 + 1), SetScreenVariable("lock01", 0))
        else:
            hotspot (110,407,188,186) background "backgrounds/location_beach_lock.jpg" action SetScreenVariable("lock01", 1)

        if lock02 > 0:
            imagebutton:
                focus_mask True
                pos (317,407)
                idle "buttons/lock_icon_" + str(lock02).zfill(2) + ".png"
                hover HoverImage("buttons/lock_icon_" + str(lock02).zfill(2) + ".png")
                action If(lock02 < 10, SetScreenVariable("lock02", lock02 + 1), SetScreenVariable("lock02", 0))
        else:
            hotspot (317,407,188,186) background "backgrounds/location_beach_lock.jpg" action SetScreenVariable("lock02", 1)

        if lock03 > 0:
            imagebutton:
                focus_mask True
                pos (522,407)
                idle "buttons/lock_icon_" + str(lock03).zfill(2) + ".png"
                hover HoverImage("buttons/lock_icon_" + str(lock03).zfill(2) + ".png")
                action If(lock03 < 10, SetScreenVariable("lock03", lock03 + 1), SetScreenVariable("lock03", 0))
        else:
            hotspot (522,407,188,186) background "backgrounds/location_beach_lock.jpg" action SetScreenVariable("lock03", 1)

        if lock04 > 0:
            imagebutton:
                focus_mask True
                pos (728,407)
                idle "buttons/lock_icon_" + str(lock04).zfill(2) + ".png"
                hover HoverImage("buttons/lock_icon_" + str(lock04).zfill(2) + ".png")
                action If(lock04 < 10, SetScreenVariable("lock04", lock04 + 1), SetScreenVariable("lock04", 0))
        else:
            hotspot (728,407,188,186) background "backgrounds/location_beach_lock.jpg" action SetScreenVariable("lock04", 1)

screen treasure_chest():
    use mods_screens_hook("treasure_chest")

    imagebutton:
        focus_mask True
        pos (440,275)
        idle "objects/object_compass_01.png"
        hover HoverImage("objects/object_compass_01.png")
        action Return()

screen roxxy_massage(massage):
    imagebutton:
        focus_mask True
        align 0.3,0.95
        idle "buttons/johnson_01.png"
        hover HoverImage("buttons/johnson_01.png")
        action Hide("roxxy_massage"), Return()

    imagebutton:
        focus_mask True
        align 0.6,0.95
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("roxxy_massage"), Jump(massage)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
