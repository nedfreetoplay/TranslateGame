screen consumr:
    add "backgrounds/location_mall_consumr_day.jpg"

    imagebutton:
        focus_mask True
        pos (174,281)
        idle "objects/object_shop_01.png"
        hover HoverImage("objects/object_shop_01.png")
        action Show("popup_parts")

    imagebutton:
        focus_mask True
        pos (454,584)
        idle "objects/object_shop_03.png"
        hover HoverImage("objects/object_shop_03.png")
        action Show("popup_swimsuit")

    imagebutton:
        focus_mask True
        pos (88,261)
        idle "objects/object_shop_02.png"
        hover HoverImage("objects/object_shop_02.png")
        action Show("popup_webcam")

    imagebutton:
        focus_mask True
        pos (820,524)
        idle "objects/object_shop_05.png"
        hover HoverImage("objects/object_shop_05.png")
        action Show("popup_bike")

    imagebutton:
        focus_mask True
        pos (60,606)
        idle "objects/object_shop_06.png"
        hover HoverImage("objects/object_shop_06.png")
        action Show("popup_milkjug")

    imagebutton:
        focus_mask True
        pos (170,620)
        idle "objects/object_shop_07.png"
        hover HoverImage("objects/object_shop_07.png")
        action Show("popup_exterminator")

    imagebutton:
        focus_mask True
        pos (230,618)
        idle "objects/object_shop_08.png"
        hover HoverImage("objects/object_shop_08.png")
        action Show("popup_eradicator")

    imagebutton:
        focus_mask True
        pos (290,616)
        idle "objects/object_shop_09.png"
        hover HoverImage("objects/object_shop_09.png")
        action Show("popup_annihilator")

    imagebutton:
        focus_mask True
        pos (350,608)
        idle "objects/object_shop_10.png"
        hover HoverImage("objects/object_shop_10.png")
        action Show("popup_gas_can")

    imagebutton:
        focus_mask True
        pos (536,515)
        idle "objects/object_shop_11.png"
        hover HoverImage("objects/object_shop_11.png")
        action Show("popup_wrench")

    imagebutton:
        focus_mask True
        pos (380,388)
        idle "objects/object_shop_12.png"
        hover HoverImage("objects/object_shop_12.png")
        action Show("popup_cat_food")

    imagebutton:
        focus_mask True
        pos (326,381)
        idle "objects/object_shop_chickenstock01.png"
        hover HoverImage("objects/object_shop_chickenstock01.png")
        action If(M_okita.is_set("talked with veronica"), Show("popup_chicken_stock"), Jump("consumr_chicken_stock_dialogue"))

    imagebutton:
        focus_mask True
        pos (700,400)
        idle "objects/character_vero_01.png"
        hover HoverImage("objects/character_vero_01.png")
        action Hide("consumr"), Jump("veronica_button_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_03.png"
        hover HoverImage("boxes/auto_option_03.png")
        action Hide("consumr"), Jump("mall_dialogue")

screen popup_parts:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_parts")

    add "boxes/shop_item_parts01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_200.png"
        hover HoverImage("buttons/shop_button_200.png")
        action [Function(player.get_item, "parts"),
            If(
               not player.has_money(200),
               Show("popup_fail01"),
               If(
                  player.has_item("parts"),
                  Show("popup_fail02"),
                  [Function(quest_complete, quest05),
                   Show("popup_parts")
                  ]
               )
            ),
            Hide("popup_parts")
        ]

screen popup_swimsuit:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_swimsuit")

    add "boxes/shop_item_swimsuit01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_100.png"
        hover HoverImage("buttons/shop_button_100.png")
        action [Function(player.get_item, "swimsuit"),
            If(
               not player.has_money(100),
               Show("popup_fail01"),
               If(
                  player.has_item("swimsuit"),
                  Show("popup_fail02"),
                  Show("popup_swimsuit")
               )
            ),
            Hide("popup_swimsuit")
        ]

screen popup_webcam:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_webcam")

    add "boxes/shop_item_camera01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_300.png"
        hover HoverImage("buttons/shop_button_300.png")
        action [Function(player.get_item, "supersaga_webcam"),
            If(
               not player.has_money(300),
               Show("popup_fail01"),
               If(
                  player.has_item("supersaga_webcam"),
                  Show("popup_fail02"),
                  Show("popup_webcam")
               )
            ),
            Hide("popup_webcam")
        ]

screen popup_bike:
    $ player.transport_level = max(player.transport_level, 1)
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_bike")

    add "boxes/shop_item_bike01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_500.png"
        hover HoverImage("buttons/shop_button_500.png")
        action [Function(player.get_item, "bike"),
            If(
               not player.has_money(500),
               Show("popup_fail01"),
               If(
                  player.has_item("bike"),
                  Show("popup_fail02"),
                  Show("popup_bike")
               )
            ),
            Hide("popup_bike")
        ]

screen popup_milkjug:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide ("popup_milkjug")

    add "boxes/shop_item_jug01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_300.png"
        hover HoverImage("buttons/shop_button_300.png")
        action [Function(player.get_item, "milkjug"),
            If(
               not player.has_money(300),
               Show("popup_fail01"),
               If(
                  player.has_item("milkjug"),
                  Show("popup_fail02"),
                  Show("popup_milkjug")
               )
            ),
            Hide("popup_milkjug")
        ]

screen popup_exterminator:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_exterminator")

    add "boxes/shop_item_spray01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_100.png"
        hover HoverImage("buttons/shop_button_100.png")
        action [Function(player.get_item, "exterminator"),
            If(
               not player.has_money(100),
               Show("popup_fail01"),
               If(
                  player.has_item("exterminator"),
                  Show("popup_fail02"),
                  Show("popup_exterminator")
               )
            ),
            Hide("popup_exterminator")
        ]

screen popup_eradicator:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_eradicator")

    add "boxes/shop_item_spray02.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_100.png"
        hover HoverImage("buttons/shop_button_100.png")
        action [Function(player.get_item, "eradicator"),
            If(
               not player.has_money(100),
               Show("popup_fail01"),
               If(
                  player.has_item("eradicator"),
                  Show("popup_fail02"),
                  Show("popup_eradicator")
               )
            ),
            Hide("popup_eradicator")
        ]

screen popup_annihilator:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_annihilator")

    add "boxes/shop_item_spray03.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_100.png"
        hover HoverImage("buttons/shop_button_100.png")
        action [Function(player.get_item, "annihilator"),
            If(
               not player.has_money(100),
               Show("popup_fail01"),
               If(
                  player.has_item("annihilator"),
                  Show("popup_fail02"),
                  Show("popup_annihilator")
               )
            ),
            Hide("popup_annihilator")
        ]

screen popup_gas_can:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_gas_can")

    add "boxes/shop_item_gas01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_100.png"
        hover HoverImage("buttons/shop_button_100.png")
        action [Function(player.get_item, "gas_can"),
            If(
               not player.has_money(100),
               Show("popup_fail01"),
               If(
                  player.has_item("gas_can"),
                  Show("popup_fail02"),
                  Show("popup_gas_can")
               )
            ),
            Hide("popup_gas_can")
        ]

screen popup_wrench:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_wrench")

    add "boxes/shop_item_wrench01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_50.png"
        hover HoverImage("buttons/shop_button_50.png")
        action [Function(player.get_item, "wrench"),
            If(
               not player.has_money(50),
               Show("popup_fail01"),
               If(
                  player.has_item("wrench"),
                  Show("popup_fail02"),
                  Show("popup_wrench")
               )
             ),
             Hide("popup_wrench")
        ]

screen popup_cat_food:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_cat_food")

    add "boxes/shop_item_catfood01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_100.png"
        hover HoverImage("buttons/shop_button_100.png")
        action [Function(player.get_item, "cat_food"),
            If(
               not player.has_money(100),
               Show("popup_fail01"),
               If(
                  player.has_item("cat_food"),
                  Show("popup_fail02"),
                  Show("popup_cat_food")
               )
            ),
            Hide("popup_cat_food")
        ]

screen popup_chicken_stock:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_chicken_stock")

    add "boxes/shop_item_chickenstock01.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_50.png"
        hover HoverImage("buttons/shop_button_50.png")
        action [Function(player.get_item, "chicken_stock"),
            If(
               not player.has_money(50),
               Show("popup_fail01"),
               If(
                  player.has_item("chicken_stock"),
                  Show("popup_fail02"),
                  Show("popup_chicken_stock")
               )
            ),
            Hide("popup_chicken_stock")
        ]

label consumr_chicken_stock_dialogue:
    scene location_mall_consumr_day_blur
    show player 4
    with dissolve
    if M_okita.is_state(S_okita_get_ingredients):
        player_name "Хм, Окита сказала {b}Овощной Бульон{/b}, но у них есть только Куриный..."
        player_name "Может, продавец сможет мне помочь?"
    else:
        player_name "Не понимаю, зачем мне сейчас куриный бульон..."
    $ game.main()

screen popup_fail01:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_fail01")

    add "boxes/popup_shopping_fail01.png"

screen popup_fail02:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_fail02")

    add "boxes/popup_shopping_fail02.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
