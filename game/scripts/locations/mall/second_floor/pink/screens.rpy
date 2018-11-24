screen pink:
    add "backgrounds/location_pink.jpg"

    imagebutton:
        focus_mask True
        idle "objects/object_toy_01.png"
        hover HoverImage("objects/object_toy_01.png")
        action Show("popup_buttplug")
        pos 89,167

    imagebutton:
        focus_mask True
        idle "objects/object_toy_02.png"
        hover HoverImage("objects/object_toy_02.png")
        action Show("popup_drilldo")
        pos 209,246

    imagebutton:
        idle "objects/object_toy_03.png"
        hover HoverImage("objects/object_toy_03.png")
        action Show("pink_ui")
        pos 11,422

    imagebutton:
        focus_mask True
        idle "objects/object_toy_04.png"
        hover HoverImage("objects/object_toy_04.png")
        action Show("popup_electroclit")
        pos 162,517

    imagebutton:
        focus_mask True
        idle "objects/object_toy_05.png"
        hover HoverImage("objects/object_toy_05.png")
        action Show("popup_strapon")
        pos 301,422

    imagebutton:
        focus_mask True
        idle "objects/object_toy_06.png"
        hover HoverImage("objects/object_toy_06.png")
        action Show("popup_badmonster")
        pos 315,306

    imagebutton:
        focus_mask True
        idle "objects/object_toy_07.png"
        hover HoverImage("objects/object_toy_07.png")
        action Show("popup_darthmoan")
        pos 284,182

    imagebutton:
        focus_mask True
        idle "objects/object_toy_08.png"
        hover HoverImage("objects/object_toy_08.png")
        action Show("popup_sybian")
        pos 334,532

    imagebutton:
        focus_mask True
        idle "objects/object_toy_09.png"
        hover HoverImage("objects/object_toy_09.png")
        action Show("popup_fleshtube")
        pos 439,486

    imagebutton:
        focus_mask True
        idle "objects/object_toy_10.png"
        hover HoverImage("objects/object_toy_10.png")
        action Show("popup_doomdong")
        pos 477,309

    imagebutton:
        focus_mask True
        idle "objects/object_toy_11.png"
        hover HoverImage("objects/object_toy_11.png")
        action Show("popup_ultravibrato")
        pos 530, 231

    imagebutton:
        focus_mask True
        idle "objects/object_toy_12.png"
        hover HoverImage("objects/object_toy_12.png")
        action Show("popup_sexdoll")
        pos 551,371

    imagebutton:
        focus_mask True
        idle "objects/object_toy_13.png"
        hover HoverImage("objects/object_toy_13.png")
        action Show("popup_whip")
        pos 292,491

    imagebutton:
        focus_mask True
        idle "objects/object_toy_14.png"
        hover HoverImage("objects/object_toy_14.png")
        action Show("popup_handcuffs")
        pos 147,468
    if L_pink.is_here(M_ivy):
        imagebutton:
            focus_mask True
            idle "objects/character_ivy_01.png"
            hover HoverImage("objects/character_ivy_01.png")
            action Hide("pink"), Jump("ivy_button_dialogue")
            pos 910,350

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("pink"), Jump("mall_second_floor")

screen popup_buttplug:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_buttplug")]
    add "boxes/pink_item_01.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_100.png"
        hover HoverImage("buttons/shop_button_100.png")
        action [
            Function(player.get_item, "buttplug"),
            If(
                not player.has_money(100),
                Show("popup_fail01"),
                If(
                   player.has_item("buttplug"),
                   Show("popup_fail02"),
                   Show("popup_buttplug")
                )
            ),
            Hide("popup_buttplug")
        ]
        xpos 410
        ypos 421

screen popup_drilldo:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_drilldo")]
    add "boxes/pink_item_02.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_400.png"
        hover HoverImage("buttons/shop_button_400.png")
        action [
            Function(player.get_item, "drilldo"),
            If(
                not player.has_money(400),
                Show("popup_fail01"),
                If(
                   player.has_item("drilldo"),
                   Show("popup_fail02"),
                   Show("popup_drilldo")
                )
            ),
            Hide("popup_drilldo")
        ]
        xpos 410
        ypos 421

screen popup_darthmoan:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_darthmoan")]
    add "boxes/pink_item_03.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_300.png"
        hover HoverImage("buttons/shop_button_300.png")
        action [
            Function(player.get_item, "darthmoan"),
            If(
                not player.has_money(300),
                Show("popup_fail01"),
                    If(
                       player.has_item("darthmoan"),
                       Show("popup_fail02"),
                       Show("popup_darthmoan")
                    )
            ),
            Hide("popup_darthmoan")
        ]
        xpos 410
        ypos 421

screen popup_badmonster:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_badmonster")]
    add "boxes/pink_item_04.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_500.png"
        hover HoverImage("buttons/shop_button_500.png")
        action [
            Function(player.get_item, "badmonster"),
            If(
                not player.has_money(500),
                Show("popup_fail01"),
                If(
                   player.has_item("badmonster"),
                   Show("popup_fail02"),
                   Show("popup_badmonster")
                )
            ),
            Hide("popup_badmonster")
        ]
        xpos 410
        ypos 421

screen popup_sybian:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_sybian")]
    add "boxes/pink_item_05.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_500.png"
        hover HoverImage("buttons/shop_button_500.png")
        action [
            Function(player.get_item, "sybian"),
            If(
                not player.has_money(500),
                Show("popup_fail01"),
                If(
                   player.has_item("sybian"),
                   Show("popup_fail02"),
                   Show("popup_sybian")
                )
            ),
            Hide("popup_sybian")
        ]
        xpos 410
        ypos 421

screen popup_strapon:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_strapon")]
    add "boxes/pink_item_06.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_500.png"
        hover HoverImage("buttons/shop_button_500.png")
        action [
            Function(player.get_item, "strapon"),
            If(
                not player.has_money(500),
                Show("popup_fail01"),
                If(
                   player.has_item("strapon"),
                   Show("popup_fail02"),
                   Show("popup_strapon")
                )
            ),
            Hide("popup_strapon")
        ]
        xpos 410
        ypos 421

screen popup_fleshtube:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_fleshtube")]
    add "boxes/pink_item_07.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_100.png"
        hover HoverImage("buttons/shop_button_100.png")
        action [
            Function(player.get_item, "fleshtube"),
            If(
                not player.has_money(100),
                Show("popup_fail01"),
                If(
                   player.has_item("fleshtube"),
                   Show("popup_fail02"),
                   Show("popup_fleshtube")
                )
            ),
            Hide("popup_fleshtube")
        ]
        xpos 410
        ypos 421

screen popup_electroclit:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_electroclit")]
    add "boxes/pink_item_08.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_100.png"
        hover HoverImage("buttons/shop_button_100.png")
        action [
            Function(player.get_item, "electroclit"),
            If(
                not player.has_money(100),
                Show("popup_fail01"),
                If(
                   player.has_item("electroclit"),
                   Show("popup_fail02"),
                   Show("popup_electroclit")
                )
            ),
            Hide("popup_electroclit")
        ]
        xpos 410
        ypos 421

screen popup_ultravibrato:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_ultravibrato")]
    add "boxes/pink_item_09.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_200.png"
        hover HoverImage("buttons/shop_button_200.png")
        action [
            Function(player.get_item, "ultravibrato"),
            If(
                not player.has_money(200),
                Show("popup_fail01"),
                If(
                   player.has_item("ultravibrato"),
                   Show("popup_fail02"),
                   Show("popup_ultravibrato")
                )
            ),
            Hide("popup_ultravibrato")
        ]
        xpos 410
        ypos 421

screen popup_doomdong:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_doomdong")]
    add "boxes/pink_item_10.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_300.png"
        hover HoverImage("buttons/shop_button_300.png")
        action [
            Function(player.get_item, "doomdong"),
            If(
                not player.has_money(300),
                Show("popup_fail01"),
                If(
                   player.has_item("doomdong"),
                   Show("popup_fail02"),
                   Show("popup_doomdong")
                )
            ),
            Hide("popup_doomdong")
        ]
        xpos 410
        ypos 421

screen popup_sexdoll:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_sexdoll")]
    add "boxes/pink_item_12.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_800.png"
        hover HoverImage("buttons/shop_button_800.png")
        action [
            Function(player.get_item, "sexdoll"),
            If(
               not player.has_money(800),
               Show("popup_fail01"),
               If(
                  player.has_item("sexdoll"),
                  Show("popup_fail02"),
                  Show("popup_sexdoll")
               )
            ),
            Hide("popup_sexdoll")
        ]
        xpos 410
        ypos 421

screen popup_whip:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_whip")]
    add "boxes/pink_item_13.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_500.png"
        hover HoverImage("buttons/shop_button_500.png")
        action [
            Function(player.get_item, "whip"),
            If(
               not player.has_money(500),
               Show("popup_fail01"),
               If(
                  player.has_item("whip"),
                  Show("popup_fail02"),
                  Show("popup_whip")
               )
            ),
            Hide("popup_whip")
        ]
        xpos 410
        ypos 421

screen popup_handcuffs:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_handcuffs")]
    add "boxes/pink_item_14.png" pos 276,281
    imagebutton:
        idle "buttons/shop_button_50.png"
        hover HoverImage("buttons/shop_button_50.png")
        action [
            Function(player.get_item, "handcuffs"),
            If(not player.has_money(50),
               Show("popup_fail01"), 
               If(
                  player.has_item("handcuffs"),
                  Show("popup_fail02"),
                  Show("popup_handcuffs")
               )
            ),
            Hide("popup_handcuffs")
        ]
        xpos 410
        ypos 421

screen popup_fail01:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_fail01")]
    add "boxes/popup_shopping_fail01.png"

screen popup_fail02:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("popup_fail02")]
    add "boxes/popup_shopping_fail02.png"

screen pamphlet:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("pamphlet"), Show("pink")]

    imagebutton:
        focus_mask True
        pos (180,30)
        idle "buttons/massage_01.png"
        hover HoverImage("buttons/massage_01.png")
        action Hide("pamphlet"), If(
                                    player.has_money(100),
                                    [Function(player.spend_money, 100), Function(game.timer.tick), Jump("ivy_paizuri")],
                                    Jump("ivy_no_money")
        )

    imagebutton:
        focus_mask True
        pos (176,203)
        idle "buttons/massage_02.png"
        hover HoverImage("buttons/massage_02.png")
        action Hide("pamphlet"), If(
                                    player.has_money(200),
                                    [Function(player.spend_money, 200), Function(game.timer.tick), Jump("ivy_blowjob")],
                                    Jump("ivy_no_money")
        )

    imagebutton:
        focus_mask True
        pos (177,363)
        idle "buttons/massage_03.png"
        hover HoverImage("buttons/massage_03.png")
        action Hide("pamphlet"), If(
                                    player.has_money(400),
                                    [Function(player.spend_money, 400), Function(game.timer.tick), Jump("ivy_reverse_cowgirl")],
                                    Jump("ivy_no_money")
        )

    imagebutton:
        focus_mask True
        pos (183,545)
        idle "buttons/massage_04.png"
        hover HoverImage("buttons/massage_04.png")
        action Hide("pamphlet"), If(
                                    player.has_money(600),
                                    [Function(player.spend_money, 600), Function(game.timer.tick), Jump("ivy_cowgirl")],
                                    Jump("ivy_no_money")
        )

screen ivy_paizuri_options:
    imagebutton:
        pos (300,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("ivy_paizuri_options"), Jump("ivy_paizuri_loop")

    if anim_toggle:
        imagebutton:
            pos (500,700)
            idle "buttons/ivy_stage01_01.png"
            hover HoverImage("buttons/ivy_stage01_01.png")
            action Hide("ivy_paizuri_options"), Function(M_ivy.set, "sex speed", M_ivy.get("sex speed") - 0.25), Jump ("ivy_paizuri_loop")

screen ivy_blowjob_options:
    imagebutton:
        pos (300,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("ivy_blowjob_options"), Jump("ivy_blowjob_loop")

    if anim_toggle:
        imagebutton:
            pos (500,700)
            idle "buttons/ivy_stage01_01.png"
            hover HoverImage("buttons/ivy_stage01_01.png")
            action Hide("ivy_blowjob_options"), Function(M_ivy.set, "sex speed", M_ivy.get("sex speed") - 0.25), Jump ("ivy_blowjob_loop")

screen ivy_rcowgirl_options:
    imagebutton:
        pos (200,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("ivy_rcowgirl_options"), Jump("ivy_reverse_cowgirl_loop")

    if anim_toggle:
        imagebutton:
            pos (400,700)
            idle "buttons/ivy_stage01_01.png"
            hover HoverImage("buttons/ivy_stage01_01.png")
            action Hide("ivy_rcowgirl_options"), Function(M_ivy.set, "sex speed", M_ivy.get("sex speed") - 0.25), Jump ("ivy_reverse_cowgirl_loop")

    imagebutton:
        pos (600,700)
        idle "buttons/ivy_stage01_02.png"
        hover HoverImage("buttons/ivy_stage01_02.png")
        action Hide("ivy_rcowgirl_options"), Jump("ivy_slap_ass")

screen ivy_cowgirl_options:
    imagebutton:
        pos (300,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("ivy_cowgirl_options"), Jump("ivy_cowgirl_loop")

    if anim_toggle:
        imagebutton:
            pos (500,700)
            idle "buttons/ivy_stage01_01.png"
            hover HoverImage("buttons/ivy_stage01_01.png")
            action Hide("ivy_cowgirl_options"), Function(M_ivy.set, "sex speed", M_ivy.get("sex speed") - 0.25), Jump ("ivy_cowgirl_loop")

screen pink_item_info(Item):
    text "{color=#8995AD}[Item.category]:{/color}\n\n{color=#5E6C8F}[Item.name]{/color}" pos 130, 93
    imagebutton:
        idle "buttons/shop_button_" + str(Item.price) + ".png"
        hover HoverImage("buttons/shop_button_" + str(Item.price) + ".png")
        action If(not player.has_money(Item.price), Show("popup_fail01"), If(player.has_item(Item.item), Show("popup_fail02"), [Function(player.get_item, Item.item), Show("popup", Image = Item.popup)])) pos 685, 93

screen pink_ui:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("pink_item_info"), Hide("pink_ui")]

    imagebutton idle "buttons/pink_ui_01.png" action NullAction() focus_mask True at truecenter

    $ a = 0
    $ b = 0
    $ c = 0
    $ c2 = 0
    $ c3 = 0
    for Item in pinkstore.items:
        $ c2 = math.trunc(c / 6)
        if c3 == 6:
            $ c3 = 0
        $ a = 123
        $ b = 163 + (c2 * 133)
        $ a += c3 * 130
        imagebutton idle Item.idle hover Item.hover xpos a ypos b action Show("pink_item_info", Item = Item)
        $ c += 1
        $ c3 += 1

screen ivy_cowgirl_cum_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("ivy_cowgirl_cum_options"), SetVariable("ivy_cum_inside", False), Return()

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("ivy_rcowgirl_cum_options"), SetVariable("ivy_cum_inside", True), Return()

screen ivy_rcowgirl_cum_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("ivy_rcowgirl_cum_options"), SetVariable("ivy_cum_inside", False), Return()

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("ivy_rcowgirl_cum_options"), SetVariable("ivy_cum_inside", True), Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
