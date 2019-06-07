screen mall_second_floor():
    use mods_screens_hook("mall_second_floor")

    add "backgrounds/location_mall_upstairs_day.jpg"

    imagebutton:
        focus_mask True
        pos (358,236)
        idle "objects/object_door_21.png"
        hover HoverImage("objects/object_door_21.png")
        action Hide("mall_second_floor"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump("pink_dialogue")]
        )

    imagebutton:
        focus_mask True
        pos (45,164)
        idle "objects/object_door_103.png"
        hover HoverImage("objects/object_door_103.png")
        action Hide("mall_second_floor"), Function(playSound), Jump("cupid_dialogue")

    imagebutton:
        focus_mask True
        pos (-2,527)
        idle "objects/object_stairs_07.png"
        hover HoverImage("objects/object_stairs_07.png")
        action Hide("mall_second_floor"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump("mall_dialogue")]
        )
    imagebutton:
        focus_mask True
        pos (488,335)
        idle "objects/object_booth_01.png"
        hover HoverImage("objects/object_booth_01.png")
        action Hide("mall_second_floor"), Jump("photo_booth_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
