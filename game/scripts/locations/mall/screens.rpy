screen mall():
    use mods_screens_hook("mall")

    add "backgrounds/location_mall_day.jpg"

    imagebutton:
        focus_mask True
        pos (612,364)
        idle "objects/object_stairs_06.png"
        hover HoverImage("objects/object_stairs_06.png")
        action Hide("mall"), Jump("mall_second_floor")

    imagebutton:
        focus_mask True
        pos (761,234)
        idle "objects/object_door_22.png"
        hover HoverImage("objects/object_door_22.png")
        action Hide("mall"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump(game.dialog_select("consumr"))]
        )

    imagebutton:
        focus_mask True
        pos (42,156)
        idle "objects/object_door_23.png"
        hover HoverImage("objects/object_door_23.png")
        action Hide("mall"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump("movie_theatre_dialogue")]
        )

    if M_jenny.is_state(S_jenny_get_a_mask) and game.timer.is_day():
        imagebutton:
            focus_mask True
            pos (439, 321)
            idle "objects/object_door_53b.png"
            hover HoverImage("objects/object_door_53b.png")
            action Hide("mall"), Jump("cupid_store_waiting_line")
    else:
        imagebutton:
            focus_mask True
            pos (541,321)
            idle "objects/object_door_53.png"
            hover HoverImage("objects/object_door_53.png")
            action Hide("mall"), If(
                                    M_mom.get_state() == S_mom_cupid_store,
                                    Jump("mom_mall_outing_block"),
                                    [Function(playSound), Jump("comic_store_dialogue")]
        )

        if L_mall.is_here(M_rump) and M_rump.get("can see speech mall"):
            imagebutton:
                focus_mask True
                pos (354,308)
                idle "objects/object_podium_01.png"
                hover HoverImage("objects/object_podium_01.png")
                action Hide("mall"), Jump("rump_mall_dialogue")

    imagebutton:
        focus_mask True
        pos (285,317)
        idle "objects/object_door_52.png"
        hover HoverImage("objects/object_door_52.png")
        action Hide("mall"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump("mall_toilets")]
        )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
