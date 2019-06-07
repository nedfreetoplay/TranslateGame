screen comic_store():
    use mods_screens_hook("comic_store")

    if M_jenny.between_states(S_jenny_get_a_mask, S_jenny_come_back_camshow) and game.timer.is_day():
        add "backgrounds/location_mall_comic_lucha_day.jpg"
    else:
        add "backgrounds/location_mall_comic_day.jpg"

    imagebutton:
        focus_mask True
        pos (675,318)
        idle "objects/character_lily_01.png"
        hover HoverImage("objects/character_lily_01.png")
        action Hide("comic_store"), Jump("tatiana_dialogue")

    imagebutton:
        focus_mask True
        pos (9,333)
        idle "objects/object_bookshelf_01.png"
        hover HoverImage("objects/object_bookshelf_01.png")
        action Show("comic_ui", interface = "Video Games")

    imagebutton:
        focus_mask True
        pos (159,355)
        idle "objects/object_comicstand_01.png"
        hover HoverImage("objects/object_comicstand_01.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (564,175)
        idle "objects/object_costumes_01.png"
        hover HoverImage("objects/object_costumes_01.png")
        action Show("comic_ui", interface = "Cosplay")

    imagebutton:
        focus_mask True
        pos (328,392)
        idle "objects/object_figurines_01.png"
        hover HoverImage("objects/object_figurines_01.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (905,409)
        idle "objects/object_posters_01.png"
        hover HoverImage("objects/object_posters_01.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (297,509)
        idle "objects/object_shelf_01.png"
        hover HoverImage("objects/object_shelf_01.png")
        action Show("comic_ui", interface = "Collectible")

    imagebutton:
        focus_mask True
        pos (583,500)
        idle "objects/object_shelf_02.png"
        hover HoverImage("objects/object_shelf_02.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (440,293)
        idle "objects/object_vr_01.png"
        hover HoverImage("objects/object_vr_01.png")
        action Show("popup_virtualsaga")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_10.png"
        hover HoverImage("boxes/auto_option_10.png")
        action Hide("comic_store"), Jump("mall_dialogue")

screen popup_virtualsaga():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_virtualsaga")

    add "boxes/pink_item_11.png" pos 276,281

    imagebutton:
        focus_mask True
        pos (410,421)
        idle "buttons/shop_button_600.png"
        hover HoverImage("buttons/shop_button_600.png")
        action [
            Function(player.get_item, "virtualsaga"),
            If(
                not player.has_money(600),
                Show("popup_fail01"),
                If(
                    player.has_item("virtualsaga"),
                    Show("popup_fail02"),
                    Show("popup_virtualsaga")
                )
            ),
            Hide("popup_virtualsaga")
        ]

screen comic_item_info(Item):
    text "{color=#8995AD}[Item.category]:{/color}\n\n{color=#5E6C8F}[Item.name]{/color}" pos 130, 93
    imagebutton:
        idle "buttons/shop_button_" + str(Item.price) + ".png"
        hover HoverImage("buttons/shop_button_" + str(Item.price) + ".png")
        action BuyItem(Item.item, buy_action=Item.callback and Function(Item.callback)) pos 685, 93

screen comic_item_preview(Item):
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("comic_item_preview")

    imagebutton idle "buttons/comic_ui_02.png" action Hide("comic_item_preview") focus_mask True at truecenter

    imagebutton idle Item.image action NullAction() focus_mask True at truecenter

screen comic_ui(interface):
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("comic_item_info"), Hide("comic_ui")]

    imagebutton idle "buttons/comic_ui_01.png" action NullAction() focus_mask True at truecenter

    $ items = []

    for Item in comicstore.items:
        if Item.category == interface and Item.purchased == False and (
                not Item.availability or eval(Item.availability)):
            $ items += [Item]

    $ a = 0
    $ b = 0
    $ c = 0
    $ c2 = 0
    $ c3 = 0
    for Item in items:
        $ c2 = math.trunc(c / 6)
        if c3 == 6:
            $ c3 = 0
        $ a = 123
        $ b = 163 + (c2 * 133)
        $ a += c3 * 130
        imagebutton:
            idle Item.idle
            hover Item.hover
            xpos a
            ypos b
            action [Show("comic_item_info", Item = Item), If(Item.image == "", NullAction(), Show("comic_item_preview", Item = Item))]
        $ c += 1
        $ c3 += 1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
