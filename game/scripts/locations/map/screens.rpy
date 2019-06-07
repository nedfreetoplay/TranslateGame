screen town_map():
    use mods_screens_hook("town_map")

    if not game.timer.is_dark():
        if getPlayingMusic("<loop 0 to 66.459>audio/music_map.ogg"):
            $ playMusic("<loop 0 to 66.459>audio/music_map.ogg")
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)

    else:
        if getPlayingMusic("<loop 107 to 215>audio/music_map_night.ogg"):
            $ playMusic("<loop 107 to 215>audio/music_map_night.ogg")
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    add game.timer.image("map/map_base{}.jpg")

    imagebutton:
        focus_mask True
        pos (837,613)
        idle L_home.miniature()
        hover HoverImage(L_home.miniature())
        hovered Function(player.go_to, L_home)
        unhovered Function(player.go_to, L_map)
        action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Home", "home_front")

    imagebutton:
        focus_mask True
        pos (728,593)
        idle L_erikhouse.miniature()
        hover HoverImage(L_erikhouse.miniature())
        hovered Function(player.go_to, L_erikhouse)
        unhovered Function(player.go_to, L_map)
        action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Erik", "erik_house_dialogue")

    if not L_school_hall.locked:
        imagebutton:
            focus_mask True
            pos (407,233)
            idle L_school_hall.miniature()
            hover HoverImage(L_school_hall.miniature())
            hovered Function(player.go_to, L_school_hall)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "School", "school_dialogue")

    if not L_basketball_court.locked:
        imagebutton:
            focus_mask True
            pos (417,220)
            idle L_basketball_court.miniature()
            hover HoverImage(L_basketball_court.miniature())
            hovered Function(player.go_to, L_basketball_court)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Basketball Court", "basket_court_dialogue")

    if not L_diane_yard.locked and not M_diane.finished_state(S_diane_build_toys):
        imagebutton:
            focus_mask True
            pos (468,62)
            idle L_diane_yard.miniature()
            hover HoverImage(L_diane_yard.miniature())
            hovered Function(player.go_to, L_diane_yard)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Diane", "dianes_front_yard_dialogue")

    elif M_diane.between_states(S_diane_build_toys, S_diane_barn_news):
        imagebutton:
            focus_mask True
            pos (468,62)
            idle L_diane_barn.miniature()
            hover HoverImage(L_diane_barn.miniature())
            hovered Function(player.go_to, L_diane_barn_building)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Diane's Barn", "barn_build_front_dialogue")

    elif M_diane.finished_state(S_diane_barn_news) or M_diane.is_state(S_diane_barn_news):
        imagebutton:
            focus_mask True
            pos (468,62)
            idle L_diane_barn.miniature()
            hover HoverImage(L_diane_barn.miniature())
            hovered Function(player.go_to, L_diane_barn)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Diane's Barn", "barn_front_dialogue")

    if not L_miahouse.locked:
        imagebutton:
            focus_mask True
            pos (621,592)
            idle L_miahouse.miniature()
            hover HoverImage(L_miahouse.miniature())
            hovered Function(player.go_to, L_miahouse)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Mia", "mias_house_dialogue")

    if not L_gym_front.locked:
        imagebutton:
            focus_mask True
            pos (851,320)
            idle L_gym_front.miniature()
            hover HoverImage(L_gym_front.miniature())
            hovered Function(player.go_to, L_gym_front)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Gym", "gym_front")

    if not L_library_front.locked:
        imagebutton:
            focus_mask True
            pos (697,323)
            idle L_library_front.miniature()
            hover HoverImage(L_library_front.miniature())
            hovered Function(player.go_to, L_library_front)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Library", "library_front")

    if not L_park.locked:
        imagebutton:
            focus_mask True
            pos (310,179)
            idle L_park.miniature()
            hover HoverImage(L_park.miniature())
            hovered Function(player.go_to, L_park)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Park", "park_dialogue")

    if not L_pool.locked:
        imagebutton:
            focus_mask True
            pos (462,578)
            idle L_pool.miniature()
            hover HoverImage(L_pool.miniature())
            hovered Function(player.go_to, L_pool)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Pool", "pool_dialogue")

    if not L_mall.locked:
        imagebutton:
            focus_mask True
            pos (791,79)
            idle L_mall.miniature()
            hover HoverImage(L_mall.miniature())
            hovered Function(player.go_to, L_mall)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Mall", "mall_dialogue")

    if not L_bank.locked:
        imagebutton:
            focus_mask True
            pos (708,198)
            idle L_bank.miniature()
            hover HoverImage(L_bank.miniature())
            hovered Function(player.go_to, L_bank)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Bank", "bank_dialogue")

    if not L_pizzeria_exterior.locked:
        imagebutton:
            focus_mask True
            pos (98,338)
            idle L_pizzeria_exterior.miniature()
            hover HoverImage(L_pizzeria_exterior.miniature())
            hovered Function(player.go_to, L_pizzeria_exterior)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Pizzeria", "pizza_exterior_dialogue")

    if not L_dealership_front.locked:
        imagebutton:
            focus_mask True
            pos (104,176)
            idle L_dealership_front.miniature()
            hover HoverImage(L_dealership_front.miniature())
            hovered Function(player.go_to, L_dealership_front)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Dealership", "dealership_front_dialogue")

    if not L_pier.locked:
        imagebutton:
            focus_mask True
            pos (58,529)
            idle L_pier.miniature()
            hover HoverImage(L_pier.miniature())
            hovered Function(player.go_to, L_pier)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Pier", "pier_dialogue")

    if not L_forest.locked:
        imagebutton:
            focus_mask True
            pos (-96,108)
            idle L_forest.miniature()
            hover HoverImage(L_forest.miniature())
            hovered Function(player.go_to, L_forest)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Forest", "forest_dialogue")

    if not L_church_front.locked:
        imagebutton:
            focus_mask True
            pos (588,48)
            idle L_church_front.miniature()
            hover HoverImage(L_church_front.miniature())
            hovered Function(player.go_to, L_church_front)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Church", "church_front_dialogue")

    if not L_police_lobby.locked:
        imagebutton:
            focus_mask True
            pos (834,227)
            idle L_police_lobby.miniature()
            hover HoverImage(L_police_lobby.miniature())
            hovered Function(player.go_to, L_police_lobby)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Police", "police_lobby_dialogue")

    if not L_tattooparlor.locked:
        imagebutton:
            focus_mask True
            pos (259,47)
            idle L_tattooparlor.miniature()
            hover HoverImage(L_tattooparlor.miniature())
            hovered Function(player.go_to, L_tattooparlor)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Tattoo Parlor", "tattoo_parlor_dialogue")

    if not L_beach.locked:
        imagebutton:
            focus_mask True
            pos (204,570)
            idle L_beach.miniature()
            hover HoverImage(L_beach.miniature())
            hovered Function(player.go_to, L_beach)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Beach", "beach_dialogue")

    if not L_hill.locked:
        imagebutton:
            focus_mask True
            pos (692,-3)
            idle L_hill.miniature()
            hover HoverImage(L_hill.miniature())
            hovered Function(player.go_to, L_hill)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Hill", "hill_dialogue")

    if not L_hospital.locked:
        imagebutton:
            focus_mask True
            pos (342,499)
            idle L_hospital.miniature()
            hover HoverImage(L_hospital.miniature())
            hovered Function(player.go_to, L_hospital)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Hospital", "hospital_dialogue")

    if not L_trailerpark.locked:
        imagebutton:
            focus_mask True
            pos (3,294)
            idle L_trailerpark.miniature()
            hover HoverImage(L_trailerpark.miniature())
            hovered Function(player.go_to, L_trailerpark)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Trailer Park", "trailer_park_dialogue")

    if not L_treehouse.locked:
        imagebutton:
            focus_mask True
            pos (805,512)
            idle L_treehouse.miniature()
            hover HoverImage(L_treehouse.miniature())
            hovered Function(player.go_to, L_treehouse)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Treehouse", "treehouse_dialogue")

    if not L_donutshop.locked:
        imagebutton:
            focus_mask True
            pos (982,222)
            idle L_donutshop.miniature()
            hover HoverImage(L_donutshop.miniature())
            hovered Function(player.go_to, L_donutshop)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Donut Shop", "donut_shop_dialogue")

    if M_aqua.is_set("altar pass") and M_aqua.is_set("treasure pass") and M_aqua.is_set("squid pass") and M_aqua.is_set("maze pass") and not L_lair.locked:
        imagebutton:
            focus_mask True
            pos (10,675)
            idle L_lair.miniature()
            hover HoverImage(L_lair.miniature())
            hovered Function(player.go_to, L_lair)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Lair", "lair_dialogue")

    if not L_warehouse.locked:
        imagebutton:
            focus_mask True
            pos (110,58)
            idle L_warehouse.miniature()
            hover HoverImage(L_warehouse.miniature())
            hovered Function(player.go_to, L_warehouse)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Warehouse", "warehouse_dialogue")

    if not L_beachhouse_front.locked:
        imagebutton:
            focus_mask True
            pos (211,495)
            idle L_beachhouse_front.miniature()
            hover HoverImage(L_beachhouse_front.miniature())
            hovered Function(player.go_to, L_beachhouse_front)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Beach House", "beach_house_front_dialogue")

    if not L_smith_front.locked:
        imagebutton:
            focus_mask True
            pos (344,269)
            idle L_smith_front.miniature()
            hover HoverImage(L_smith_front.miniature())
            hovered Function(player.go_to, L_smith_front)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Smith", "smiths_frontyard_dialogue")

    if not L_annie_front.locked:
        imagebutton:
            focus_mask True
            pos (344, 59)
            idle L_annie_front.miniature()
            hover HoverImage(L_annie_front.miniature())
            hovered Function(player.go_to, L_annie_front)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Annie", "annies_house_front_dialogue")

    if not L_boat_bridge.locked:
        imagebutton:
            focus_mask True
            pos (109,702)
            idle L_boat_bridge.miniature()
            hover HoverImage(L_boat_bridge.miniature())
            hovered Function(player.go_to, L_boat_bridge)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Boat", "boat_bridge_dialogue")

    if not L_rump_front.locked:
        imagebutton:
            focus_mask True
            pos (899,473)
            idle L_rump_front.miniature()
            hover HoverImage(L_rump_front.miniature())
            hovered Function(player.go_to, L_rump_front)
            unhovered Function(player.go_to, L_map)
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Rump", "mayor_rumps_frontyard_dialogue")

    add game.timer.image("car01{}")
    add game.timer.image("car02{}")
    add game.timer.image("car03{}")
    add "sparkle01"
    add "sparkle02"
    add "sparkle03"
    add "cloud01"
    if Game.is_christmas() and random.random() >= 0.9:
        $ A_hes_real.unlock()
        add game.timer.image("santa_car{}")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
