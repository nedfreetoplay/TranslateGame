screen pool():
    use mods_screens_hook("pool")

    add game.timer.image("backgrounds/location_pool_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (129,382)
        idle game.timer.image("objects/object_diving_01{}.png")
        hover HoverImage(game.timer.image("objects/object_diving_01{}.png"))
        action Show("diving_options")

    imagebutton:
        focus_mask True
        pos (706,375)
        idle game.timer.image("objects/object_door_25{}.png")
        hover HoverImage(game.timer.image("objects/object_door_25{}.png"))
        action Hide("pool"), If(
                                game.timer.is_dark(),
                                Jump("pool_dialogue"),
                                If(
                                   M_cassie.is_state(S_cassie_medic_room, S_cassie_end),
                                   Jump("medic_room_dialogue"),
                                   Jump("poolrules03_dialogue")
                                )
        )

    imagebutton:
        focus_mask True
        pos (774,367)
        idle game.timer.image("objects/object_door_26{}.png")
        hover HoverImage(game.timer.image("objects/object_door_26{}.png"))
        action Hide("pool"), If(
                                game.timer.is_dark(),
                                Jump("pool_dialogue"),
                                If(
                                   player.has_item("swimsuit"),
                                   Jump("changing_dialogue"),
                                   Jump("locked_door26_dialogue")
                                )
        )

    imagebutton:
        focus_mask True
        pos (849,358)
        idle game.timer.image("objects/object_door_27{}.png")
        hover HoverImage(game.timer.image("objects/object_door_27{}.png"))
        action Hide("pool"), If(
                                game.timer.is_dark(),
                                Jump("pool_dialogue"),
                                If(
                                   player.has_item("swimsuit"),
                                   Jump("changing_dialogue"),
                                   Jump("locked_door26_dialogue")
                                )
        )

    imagebutton:
        focus_mask True
        pos (932,348)
        idle game.timer.image("objects/object_door_28{}.png")
        hover HoverImage(game.timer.image("objects/object_door_28{}.png"))
        action Hide("pool"), If(
                                game.timer.is_dark(),
                                Jump("pool_dialogue"),
                                If(
                                   player.has_item("swimsuit"),
                                   Jump("changing_dialogue"),
                                   Jump("locked_door26_dialogue")
                                )
        )

    if not game.timer.is_dark():
        if player.location.is_here(M_ronda):
            imagebutton:
                focus_mask True
                pos (630,386)
                idle "objects/character_ronda_01.png"
                hover HoverImage("objects/character_ronda_01.png")
                action Hide("pool"), Jump("ronda_pool_button_dialogue")

        imagebutton:
            focus_mask True
            pos (489,307)
            idle "objects/character_cassie_01.png"
            hover HoverImage("objects/character_cassie_01.png")
            action Hide("pool"), Jump("cassie_button_dialogue")

screen diving_options():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("diving_options")]

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/diving_option_01.png"
        hover HoverImage("boxes/diving_option_01.png")
        action Hide("diving_options"), Hide("pool"), If(
                                                        game.timer.is_dark(),
                                                        Jump("pool_dialogue"),
                                                        Jump("poolrules_dialogue")
        )

screen gloryhole_stage01():
    add "backgrounds/location_pool_changeroom03b.jpg"

    imagebutton:
        focus_mask True
        pos (180,700)
        idle "buttons/gloryhole_stage01_01.png"
        hover HoverImage("buttons/gloryhole_stage01_01.png")
        action Hide ("gloryhole_stage01"), Jump("gloryhole_medic_bj")

    imagebutton:
        focus_mask True
        pos (380,700)
        idle "buttons/gloryhole_stage01_02.png"
        hover HoverImage("buttons/gloryhole_stage01_02.png")
        action Hide ("gloryhole_stage01"), Jump("gloryhole_medic_fuck_fail")

    imagebutton:
        focus_mask True
        pos (580,700)
        idle "buttons/gloryhole_stage01_03.png"
        hover HoverImage("buttons/gloryhole_stage01_03.png")
        action Hide ("gloryhole_stage01"), Jump("gloryhole_medic_fuckraw_fail")

screen gloryhole_stage02():
    add "backgrounds/location_pool_changeroom03b.jpg"

    imagebutton:
        focus_mask True
        pos (90,700)
        idle "buttons/gloryhole_stage02_01.png"
        hover HoverImage("buttons/gloryhole_stage02_01.png")
        action Hide ("gloryhole_stage02"), Jump("gloryhole_medic_bj")

    imagebutton:
        focus_mask True
        pos (290,700)
        idle "buttons/gloryhole_stage02_02.png"
        hover HoverImage("buttons/gloryhole_stage02_02.png")
        action Hide ("gloryhole_stage02"), Jump("gloryhole_medic_bjtitsfinal")

    imagebutton:
        focus_mask True
        pos (490,700)
        idle "buttons/gloryhole_stage02_03.png"
        hover HoverImage("buttons/gloryhole_stage02_03.png")
        action Hide ("gloryhole_stage02"), Jump("gloryhole_medic_bjfacefinal")

    if store._in_replay == None:
        imagebutton:
            focus_mask True
            pos (690,700)
            idle "buttons/gloryhole_stage02_04.png"
            hover HoverImage("buttons/gloryhole_stage02_04.png")
            action Hide ("gloryhole_stage02"), Jump("gloryhole_medic_swallow_fail")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
