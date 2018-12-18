screen town_map:
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
        idle game.timer.image("map/home01{}.png")
        hover HoverImage(game.timer.image("map/home01{}.png"))
        action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Home", "home_front")

    imagebutton:
        focus_mask True
        pos (728,593)
        idle game.timer.image("map/erikhouse01{}.png")
        hover HoverImage(game.timer.image("map/erikhouse01{}.png"))
        action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Erik", "erik_house_dialogue")

    if not L_school_hall.locked:
        imagebutton:
            focus_mask True
            pos (407,233)
            idle game.timer.image("map/school01{}.png")
            hover HoverImage(game.timer.image("map/school01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "School", "school_dialogue")

    if not L_basketball_court.locked:
        imagebutton:
            focus_mask True
            pos (417,220)
            idle game.timer.image("map/bball01{}.png")
            hover HoverImage(game.timer.image("map/bball01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Basketball Court", "basket_court_dialogue")

    if not L_diane_yard.locked and not M_diane.finished_state(S_diane_build_toys):
        imagebutton:
            focus_mask True
            pos (468,62)
            idle game.timer.image("map/dianehouse01{}.png")
            hover HoverImage(game.timer.image("map/dianehouse01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Diane", "dianes_front_yard_dialogue")

    elif M_diane.between_states(S_diane_build_toys, S_diane_barn_news):
        imagebutton:
            focus_mask True
            pos (468,62)
            idle game.timer.image("map/barn01{}.png")
            hover HoverImage(game.timer.image("map/barn01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Diane's Barn", "barn_build_front_dialogue")
    elif M_diane.finished_state(S_diane_barn_news) or M_diane.is_state(S_diane_barn_news):
        imagebutton:
            focus_mask True
            pos (468,62)
            idle game.timer.image("map/barn01{}.png")
            hover HoverImage(game.timer.image("map/barn01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Diane's Barn", "barn_front_dialogue")

    if not L_miahouse.locked:
        imagebutton:
            focus_mask True
            pos (621,592)
            idle game.timer.image("map/miahouse01{}.png")
            hover HoverImage(game.timer.image("map/miahouse01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Mia", "mias_house_dialogue")

    if not L_gym_front.locked:
        imagebutton:
            focus_mask True
            pos (851,320)
            idle game.timer.image("map/gym01{}.png")
            hover HoverImage(game.timer.image("map/gym01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Gym", "gym_front")

    if not L_library_front.locked:
        imagebutton:
            focus_mask True
            pos (697,323)
            idle game.timer.image("map/library01{}.png")
            hover HoverImage(game.timer.image("map/library01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Library", "library_front")

    if not L_park.locked:
        imagebutton:
            focus_mask True
            pos (310,179)
            idle game.timer.image("map/park01{}.png")
            hover HoverImage(game.timer.image("map/park01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Park", "park_dialogue")

    if not L_pool.locked:
        imagebutton:
            focus_mask True
            pos (462,578)
            idle game.timer.image("map/pool01{}.png")
            hover HoverImage(game.timer.image("map/pool01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Pool", "pool_dialogue")

    if not L_mall.locked:
        imagebutton:
            focus_mask True
            pos (791,79)
            idle game.timer.image("map/mall01{}.png")
            hover HoverImage(game.timer.image("map/mall01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Mall", "mall_dialogue")

    if not L_bank.locked:
        imagebutton:
            focus_mask True
            pos (708,198)
            idle game.timer.image("map/bank01{}.png")
            hover HoverImage(game.timer.image("map/bank01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Bank", "bank_dialogue")

    if not L_pizzeria_exterior.locked:
        imagebutton:
            focus_mask True
            pos (98,338)
            idle game.timer.image("map/pizza01{}.png")
            hover HoverImage(game.timer.image("map/pizza01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Pizzeria", "pizza_exterior_dialogue")

    if not L_dealership_front.locked:
        imagebutton:
            focus_mask True
            pos (104,176)
            idle game.timer.image("map/dealership01{}.png")
            hover HoverImage(game.timer.image("map/dealership01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Dealership", "dealership_front_dialogue")

    if not L_pier.locked:
        imagebutton:
            focus_mask True
            pos (58,529)
            idle game.timer.image("map/pier01{}.png")
            hover HoverImage(game.timer.image("map/pier01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Pier", "pier_dialogue")

    if not L_forest.locked:
        imagebutton:
            focus_mask True
            pos (0,107)
            idle game.timer.image("map/forest01{}.png")
            hover HoverImage(game.timer.image("map/forest01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Forest", "forest_dialogue")

    if not L_church_front.locked:
        imagebutton:
            focus_mask True
            pos (588,48)
            idle game.timer.image("map/church01{}.png")
            hover HoverImage(game.timer.image("map/church01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Church", "church_front_dialogue")

    if not L_police_lobby.locked:
        imagebutton:
            focus_mask True
            pos (834,227)
            idle game.timer.image("map/police01{}.png")
            hover HoverImage(game.timer.image("map/police01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Police", "police_lobby_dialogue")

    if not L_tattooparlor.locked:
        imagebutton:
            focus_mask True
            pos (259,47)
            idle game.timer.image("map/tattoo01{}.png")
            hover HoverImage(game.timer.image("map/tattoo01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Tattoo Parlor", "tattoo_parlor_dialogue")

    if not L_beach.locked:
        imagebutton:
            focus_mask True
            pos (204,570)
            idle game.timer.image("map/beach01{}.png")
            hover HoverImage(game.timer.image("map/beach01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Beach", "beach_dialogue")

    if not L_hill.locked:
        imagebutton:
            focus_mask True
            pos (692,-3)
            idle game.timer.image("map/hill01{}.png")
            hover HoverImage(game.timer.image("map/hill01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Hill", "hill_dialogue")

    if not L_hospital.locked:
        imagebutton:
            focus_mask True
            pos (342,499)
            idle game.timer.image("map/clinic01{}.png")
            hover HoverImage(game.timer.image("map/clinic01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Hospital", "hospital_dialogue")

    if not L_trailerpark.locked:
        imagebutton:
            focus_mask True
            pos (3,294)
            idle game.timer.image("map/trailer01{}.png")
            hover HoverImage(game.timer.image("map/trailer01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Trailer Park", "trailer_park_dialogue")

    if not L_treehouse.locked:
        imagebutton:
            focus_mask True
            pos (805,512)
            idle game.timer.image("map/treehouse01{}.png")
            hover HoverImage(game.timer.image("map/treehouse01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Treehouse", "treehouse_dialogue")

    if not L_donutshop.locked:
        imagebutton:
            focus_mask True
            pos (982,222)
            idle game.timer.image("map/donut01{}.png")
            hover HoverImage(game.timer.image("map/donut01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Donut Shop", "donut_shop_dialogue")

    if M_aqua.is_set("altar pass") and M_aqua.is_set("treasure pass") and M_aqua.is_set("squid pass") and M_aqua.is_set("maze pass") and not L_lair.locked:
        imagebutton:
            focus_mask True
            pos (10,675)
            idle game.timer.image("map/lair01{}.png")
            hover HoverImage(game.timer.image("map/lair01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Lair", "lair_dialogue")

    if not L_warehouse.locked:
        imagebutton:
            focus_mask True
            pos (110,58)
            idle game.timer.image("map/warehouse01{}.png")
            hover HoverImage(game.timer.image("map/warehouse01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Warehouse", "warehouse_dialogue")

    if not L_beachhouse_front.locked:
        imagebutton:
            focus_mask True
            pos (211,495)
            idle game.timer.image("map/beachhouse01{}.png")
            hover HoverImage(game.timer.image("map/beachhouse01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Beach House", "beach_house_front_dialogue")

    if not L_smith_front.locked:
        imagebutton:
            focus_mask True
            pos (344,269)
            idle game.timer.image("map/smith01{}.png")
            hover HoverImage(game.timer.image("map/smith01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Smith", "smiths_frontyard_dialogue")

    if not L_annie_front.locked:
        imagebutton:
            focus_mask True
            pos (344, 59)
            idle game.timer.image("map/annie01{}.png")
            hover HoverImage(game.timer.image("map/annie01{}.png"))
            action Hide("town_map"), Hide("ui"), Function(renpy.call, "map_lock_check", "Annie", "annies_house_front_dialogue")

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
