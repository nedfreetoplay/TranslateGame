screen mall_toilets():
    use mods_screens_hook("mall_toilets")

    if game.rump_n_cunt:
        add "backgrounds/location_mall_washroom_event.jpg"

    else:
        add "backgrounds/location_mall_washroom.jpg"

    imagebutton:
        focus_mask True
        pos (184,189)
        idle "objects/object_door_54.png"
        hover HoverImage("objects/object_door_54.png")
        action Hide("mall_toilets"), If(game.rump_n_cunt, Jump("rump_toilets_stall"), Jump("mall_toilets_stall"))

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_10.png"
        hover HoverImage("boxes/auto_option_10.png")
        action Hide("mall_toilets"), Jump("mall_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
