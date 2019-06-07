screen beach_house_front():
    use mods_screens_hook("beach_house_front")

    add player.location.background
    if not player.has_picked_up_item("beach_house_key"):
        imagebutton:
            focus_mask True
            pos (134,498)
            idle game.timer.image("objects/object_sign_05{}.png")
            hover HoverImage(game.timer.image("objects/object_sign_05{}.png"))
            action Show("popup_buy_beach_house")
    imagebutton:
        focus_mask True
        pos (773,420)
        idle game.timer.image("objects/object_door_114{}.png")
        hover HoverImage(game.timer.image("objects/object_door_114{}.png"))
        action Hide("beach_house_front"), If(player.has_picked_up_item("beach_house_key"), Jump("beach_house_entrance_dialogue"), Jump("beach_house_not_bought_dialogue"))

screen popup_buy_beach_house():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_buy_beach_house")

    add "boxes/shop_item_beach_house01.png" at truecenter

    imagebutton:
        focus_mask True
        align (0.5,0.72)
        idle "buttons/shop_button_5000.png"
        hover HoverImage("buttons/shop_button_5000.png")
        action [Function(player.get_item, "beach_house_key"),
            If(
                not player.has_money(5000),
                Show("popup_fail01"),
                [Hide("popup_buy_beach_house"), Show('popup', None, "boxes/popup_key4.png"), Function(A_home_sweet_home.unlock)]
            ),
            Hide("popup_buy_beach_house")
        ]

screen beach_house_entrance():
    use mods_screens_hook("beach_house_entrance")

    add player.location.background
    imagebutton:
        focus_mask True
        pos (184,274)
        idle game.timer.image("objects/object_door_117{}.png")
        hover HoverImage(game.timer.image("objects/object_door_117{}.png"))
        action Hide("beach_house_entrance"), Jump("beach_house_front_dialogue")
    imagebutton:
        focus_mask True
        pos (632,25)
        idle game.timer.image("objects/object_stairs_08{}.png")
        hover HoverImage(game.timer.image("objects/object_stairs_08{}.png"))
        action Hide("beach_house_entrance"), Jump("beach_house_bedroom_dialogue")
    if L_beachhouse_entrance.is_here(M_consuela):
        imagebutton:
            focus_mask True
            pos (464,383)
            idle "objects/character_consuela_01.png"
            hover HoverImage("objects/character_consuela_01.png")
            action Hide("beach_house_entrance"), Jump("consuela_button_dialogue")

screen beach_house_bedroom():
    use mods_screens_hook("beach_house_bedroom")

    add player.location.background
    imagebutton:
        focus_mask True
        pos (0,290)
        idle game.timer.image("objects/object_door_118{}.png")
        hover HoverImage(game.timer.image("objects/object_door_118{}.png"))
        action Hide("beach_house_bedroom"), Jump("beach_house_patio_dialogue")
    imagebutton:
        focus_mask True
        pos (0,690)
        idle game.timer.image("objects/object_stairs_09{}.png")
        hover HoverImage(game.timer.image("objects/object_stairs_09{}.png"))
        action Hide("beach_house_bedroom"), Jump("beach_house_entrance_dialogue")
    imagebutton:
        focus_mask True
        pos (265,475)
        idle game.timer.image("objects/object_bed_12{}.png")
        hover HoverImage(game.timer.image("objects/object_bed_12{}.png"))
        action Hide("beach_house_bedroom"), Jump("beach_house_sleeping")

screen beach_house_patio():
    use mods_screens_hook("beach_house_patio")

    add player.location.background
    imagebutton:
        focus_mask True
        pos (797,194)
        idle game.timer.image("objects/object_door_116{}.png")
        hover HoverImage(game.timer.image("objects/object_door_116{}.png"))
        action Hide("beach_house_patio"), Jump("beach_house_bedroom_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
