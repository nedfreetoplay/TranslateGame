screen item_desc(Item):
    $ description = Item.description
    text description pos 205, 555

screen item_name(Item):
    $ name = Item.name
    text name pos 205, 530

screen backpack():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("item_desc"), Hide("item_name"), Hide("backpack"), Play("audio", "audio/sfx_backpack_close.ogg")]

    imagebutton idle "buttons/backpack.png" xalign 0.5 yalign 1.0 action [Hide("backpack"), Play("audio", "audio/sfx_backpack_close.ogg")] focus_mask True

    imagebutton idle "buttons/backpack_preloop.png" xpos 190 ypos 134 action NullAction() focus_mask True

    default backback_page = 1
    default items_per_page = 15
    default current_item = 0
    default start_item = 0
    default total_items = len(player.inventory.items)
    default Inv = player.inventory.items

    for current_item in xrange(start_item, (backback_page * items_per_page)):
        if current_item < total_items:
            $ start_xpos = 191
            $ start_ypos = 134
            $ row_ypos = math.trunc(current_item / 5)
            $ row_xpos = current_item - (row_ypos * 5)
            $ row_ypos -= math.trunc(start_item / 5)
            $ start_xpos += 130 * row_xpos
            $ start_ypos += 130 * row_ypos

            vbox:
                area (start_xpos,start_ypos,130,130)
                imagebutton:
                    idle Item(Inv[current_item]).image
                    if Item(Inv[current_item]).transform == None:
                        hover HoverImage(Item(Inv[current_item]).image)
                    else:
                        hover HoverImage(Item(Inv[current_item]).transform)
                    xalign 0.5
                    yalign 0.5
                    action (If(Item(Inv[current_item]).dialogue,
                               (Function(renpy.call_in_new_context,
                                         Item(Inv[current_item]).dialogue,
                                         item=Item(Inv[current_item])),
                                Play("audio", "audio/sfx_backpack_select2.ogg")),
                               NullAction()))
                    hovered (Show("item_name", Item=Item(Inv[current_item])),
                             Show("item_desc", Item=Item(Inv[current_item])))
                    unhovered Hide("item_desc"), Hide("item_name")

    if backback_page > 1:
        imagebutton:
            focus_mask True
            pos (43,261)
            idle "buttons/backpack_left.png"
            action SetScreenVariable("backback_page", backback_page - 1), SetScreenVariable("start_item", start_item - 15)

    if current_item + 1 < total_items:
        imagebutton:
            focus_mask True
            pos (874,264)
            idle "buttons/backpack_right.png"
            action SetScreenVariable("backback_page", backback_page + 1), SetScreenVariable("start_item", start_item + 15)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
