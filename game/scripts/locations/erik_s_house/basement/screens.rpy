screen eriks_basement() tag eriks_house:


    add "backgrounds/location_erik_basement01.jpg"

    imagebutton:
        focus_mask True
        pos (37,475)
        idle "objects/object_cabinet_01.png"
        hover HoverImage("objects/object_cabinet_01.png")
        action Show("cabinet01_options")

    if player.location.is_here(M_erik, M_mrsj):
        imagebutton:
            focus_mask True
            pos (393,353)
            idle "objects/object_poker_02.png"
            hover HoverImage("objects/object_poker_02.png")
            action Hide("eriks_basement"), Jump("mrsj_poker")

    else:
        imagebutton:
            focus_mask True
            pos (394,505)
            idle "objects/object_poker_01.png"
            hover HoverImage("objects/object_poker_01.png")
            action Show("poker01_options")

    imagebutton:
        focus_mask True
        pos (137,308)
        idle "objects/object_stairs_01.png"
        hover HoverImage("objects/object_stairs_01.png")
        action If(
            M_mrsj.is_set("afterpoker fun"),
            [Hide("eriks_basement"), Jump("mrsj_afterpoker_fun_block")],
            [Hide("eriks_basement"), Jump("erik_indoors")]
        )

    if M_dewitt.is_state(S_dewitt_clean_graffiti) and not player.has_item("beer"):
        imagebutton:
            focus_mask True
            pos (72,621)
            idle "objects/object_beer_01.png"
            hover HoverImage("objects/object_beer_01.png")
            action Hide("eriks_basement"), Jump("eriks_basement_dewitt_get_beer")

    if M_dewitt.is_state(S_dewitt_replace_guitar) and player.has_item("fake_guitar"):
        imagebutton:
            focus_mask True
            pos (635,338)
            idle "objects/object_guitar_01.png"
            hover HoverImage("objects/object_guitar_01.png")
            action Hide("eriks_basement"), Jump("eriks_basement_dewitt_replace_guitar")

    imagebutton:
        focus_mask True
        pos (879,310)
        idle "objects/object_door_81.png"
        hover HoverImage("objects/object_door_81.png")
        action Hide("eriks_basement"), Jump("erik_basement_backroom_dialogue")

    if player.location.is_here(M_erik) and not player.location.is_here(M_mrsj) and not erik_drunk:
        imagebutton:
            focus_mask True
            pos (855,410)
            idle "objects/character_erik_01.png"
            hover HoverImage("objects/character_erik_01.png")
            action Hide("eriks_basement"), Jump("erik_button_dialogue")

screen cabinet01_options():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("cabinet01_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/cabinet01_option_01.png"
        hover HoverImage("boxes/cabinet01_option_01.png")
        action Hide("cabinet01_options"), Hide("eriks_basement"), Jump("cabinet")

screen poker01_options():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("poker01_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/poker01_option01.png"
        hover HoverImage("boxes/poker01_option01.png")
        action Hide("poker01_options"), Hide("eriks_basement"), Jump("poker_table")

screen eriks_basement_backroom():
    use mods_screens_hook("eriks_basement_backroom")

    add "backgrounds/location_erik_basement_back.jpg"

    imagebutton:
        focus_mask True
        pos (733,231)
        idle "objects/object_door_82.png"
        hover HoverImage("objects/object_door_82.png")
        action Hide("eriks_basement_backroom"), Jump("erik_basement")

    if player.location.is_here(M_erik, M_mrsj):
        imagebutton:
            focus_mask True
            pos (0,315)
            idle "images/objects/character_mrsj_02.png"
            hover HoverImage("images/objects/character_mrsj_02.png")
            action Hide("eriks_basement_backroom"), Jump("mrsj_afterpoker_fun")

    else:
        imagebutton:
            focus_mask True
            pos (0,385)
            idle "objects/object_couch_01.png"
            hover HoverImage("objects/object_couch_01.png")
            action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (888,539)
        idle "objects/object_aquarium_01.png"
        hover HoverImage("objects/object_aquarium_01.png")
        action Hide("eriks_basement_backroom"), Hide("ui"), Show("backroom_aquarium")

screen backroom_aquarium():
    add "backgrounds/location_erik_basement_aquarium.jpg"

    if erik.started(erik_card_hunt) and not player.has_item("eriks_cards"):
        imagebutton:
            focus_mask True
            pos (350,450)
            idle "objects/object_box_02.png"
            hover HoverImage("objects/object_box_02.png")
            action Hide("backroom_aquarium"), Jump("backroom_aquarium")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("backroom_aquarium"), Show("eriks_basement_backroom"), Show("ui")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
