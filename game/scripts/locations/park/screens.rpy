screen park():
    use mods_screens_hook("park")

    add game.timer.image("backgrounds/location_park_day{}.jpg")

    if player.location.is_here(M_anna):
        imagebutton:
            focus_mask True
            pos (710,400)
            idle "objects/character_anna_01.png"
            hover HoverImage("objects/character_anna_01.png")
            action Hide("park"), Jump("anna_button_dialogue")

    if game.timer.is_dark() and not M_roxxy.is_state(S_roxxy_meeting_buyer):
        imagebutton:
            focus_mask True
            pos (724,407)
            idle "objects/object_bench_03_night.png"
            hover HoverImage("objects/object_bench_03_night.png")
            action Show("bench03_options")

    if erik.known(erik_father_treasure) or M_mia.is_state(S_mia_stolen_goods):
        imagebutton:
            focus_mask True
            pos (261,291)
            idle game.timer.image("objects/object_tree_01{}.png")
            hover HoverImage(game.timer.image("objects/object_tree_01{}.png"))
            action Hide("park"), Jump("park_bushes_dialogue")

    imagebutton:
        focus_mask True
        pos (104,464)
        idle game.timer.image("objects/object_bench_02{}.png")
        hover HoverImage(game.timer.image("objects/object_bench_02{}.png"))
        action Show("popup_unfinished")

    if game.timer.is_afternoon() and M_okita.is_state(S_okita_take_picture_judith) and player.location.is_here(M_judith):
        imagebutton:
            focus_mask True
            pos (104,430)
            idle game.timer.image("objects/character_judith_03{}.png")
            hover HoverImage(game.timer.image("objects/character_judith_03{}.png"))
            action Hide("park"), Jump("park_take_picture_judith")

    imagebutton:
        focus_mask True
        pos (318,377)
        idle game.timer.image("objects/object_fountain_01{}.png")
        hover HoverImage(game.timer.image("objects/object_fountain_01{}.png"))
        action MoveTo(L_park_fountain)

    if M_ross.is_state(S_ross_find_eve_backpack) and not player.has_picked_up_item("eve_backpack") and not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (883,499)
            idle "objects/object_backpack_01.png"
            hover HoverImage("objects/object_backpack_01.png")
            action Hide("park"), Jump("backpack_pickup_dialogue")

    if M_roxxy.is_state(S_roxxy_meeting_buyer) and game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (104,389)
            idle "objects/character_pilly_01.png"
            hover HoverImage("objects/character_pilly_01.png")
            action Hide("park"), Jump("park_pilly_button")

screen bench03_options():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("bench03_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/bench03_option_01.png"
        hover HoverImage("boxes/bench03_option_01.png")
        action If(
            not game.timer.is_evening(),
            [Hide("park"), Hide("bench03_options"), Jump("park_night_closed")],
            [Hide("park"), Hide("bench03_options"), Jump("park_rap_battle")]
        )

screen park_fountain():
    use mods_screens_hook("park_fountain")

    if not player.has_item("weird_coin"):
        imagebutton:
            focus_mask True
            align (0.44,0.81)
            if not game.timer.is_dark():
                idle "objects/object_coin_01.png"
                hover HoverImage("objects/object_coin_01.png")
            else:
                idle Composite((35,37), (0,0), "objects/object_coin_01_night.png", (10,-10), PulseImage(Crop((0,0,30,30), "map/map_sparkle01_alpha.png"), "map/map_sparkle03.png", delay1 = 5, delay2 = 0.2))
                hover HoverImage("objects/object_coin_01_night.png")
            action Hide("park_fountain"), Jump("coin_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("park_fountain"), Jump("park_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
