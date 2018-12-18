screen cupid:
    add "backgrounds/location_mall_cupid_day.jpg"

    imagebutton:
        focus_mask True
        pos (685,232)
        idle "objects/object_door_104.png"
        hover HoverImage("objects/object_door_104.png")
        action Hide("cupid"), If(
                                M_mom.get_state() in [S_mom_choose_gift, S_mom_show_necklace],
                                Jump("mom_cupid_outing_block"),
                                [Function(playSound), Jump("cupid_dressroom")]
        )

    imagebutton:
        focus_mask True
        pos (167,328)
        idle "objects/character_kass_01.png"
        hover HoverImage("objects/character_kass_01.png")
        action Hide("cupid"), Jump("kass_dialogue")

    if player.location.is_here(M_mom):
        imagebutton:
            focus_mask True
            pos (580,320)
            idle "objects/character_debbie_08.png"
            hover HoverImage("objects/character_debbie_08.png")
            action Hide("cupid"), Jump("mom_cupid_outing")

    imagebutton:
        focus_mask True
        pos (463,280)
        idle "objects/object_jewelery_01.png"
        hover HoverImage("objects/object_jewelery_01.png")
        action Hide("cupid"), If(
                                M_mom.get_state() in [S_mom_show_necklace, S_mom_dressing_room],
                                Jump("mom_cupid_outing_block"),
                                Jump("necklace_display")
        )

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("cupid"), If(
                                M_mom.get_state() in [S_mom_choose_gift, S_mom_show_necklace, S_mom_dressing_room],
                                Jump("mom_cupid_outing_block"),
                                Jump("mall_second_floor")
        )

    imagebutton:
        focus_mask True
        pos (802,415)
        idle "objects/object_cupid_stand_01.png"
        hover HoverImage("objects/object_cupid_stand_01.png")
        action Show("cupid_ui", interface = "Plushes")

    imagebutton:
        focus_mask True
        pos (0,302)
        idle "objects/object_cupid_stand_02.png"
        hover HoverImage("objects/object_cupid_stand_02.png")
        action Show("cupid_ui", interface = "Flowers")

screen cupid_item_info(item):
    text "{color=#8995AD}[item.category]:{/color}\n\n{color=#5E6C8F}[item.name]{/color}" pos 130, 93
    imagebutton:
        idle "buttons/shop_button_" + str(item.price) + ".png"
        hover HoverImage("buttons/shop_button_" + str(item.price) + ".png")
        action If(not player.has_money(item.price), Show("popup_fail01"), If(player.has_item(item.item), Show("popup_fail02"), [Function(player.get_item, item.item), Show("popup", Image = item.popup)])) pos 685, 93

screen cupid_ui(interface):
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("cupid_item_info"), Hide("cupid_ui")]

    imagebutton idle "buttons/comic_ui_01.png" action NullAction() focus_mask True at truecenter

    $ items = []

    for item in cupidstore.items:
        if item.category == interface and not item.purchased:
            $ items.append(item)

    $ a = 0
    $ b = 0
    $ c = 0
    $ c2 = 0
    $ c3 = 0
    for item in items:
        $ c2 = math.trunc(c / 6)
        if c3 == 6:
            $ c3 = 0
        $ a = 123
        $ b = 163 + (c2 * 133)
        $ a += c3 * 130
        imagebutton:
            idle item.idle
            hover item.hover
            xpos a
            ypos b
            action Show("cupid_item_info", item = item)
        $ c += 1
        $ c3 += 1

screen cupid_necklace_display:
    add "backgrounds/location_mall_cupid_closeup_stall.jpg"

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("cupid_necklace_display"), Jump("cupid_dialogue")

screen cupid_dressingroom:
    add "backgrounds/location_mall_cupid_closeup_stall.jpg"

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("cupid_dressingroom"), Jump("cupid_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
