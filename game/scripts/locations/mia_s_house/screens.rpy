screen mias_house():
    use mods_screens_hook("mias_house")

    add game.timer.image("backgrounds/location_mia_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (571,442)
        idle game.timer.image("objects/object_door_24{}.png")
        hover HoverImage(game.timer.image("objects/object_door_24{}.png"))
        action If(
            game.timer.is_weekend() and game.timer.is_morning(),
            [Hide("mias_house"), Jump("closed_mia")],
            If(
                M_mia.get_state() == S_mia_need_space,
                [Hide("mias_house"), Jump("mia_banned")],
                If(
                    game.timer.is_morning(),
                    [Hide("mias_house"), Jump("closed_mia")],
                    If(
                        game.timer.is_afternoon(),
                        If(
                            not M_mia.is_set('front door locked'),
                            [Hide("mias_house"), Function(playSound), Jump("mias_entrance")],
                            [Hide("mias_house"), Jump("closed_mia")]
                        ),
                        If(
                            game.timer.is_evening(),
                            If(
                                not M_mia.is_set('front door locked'),
                                [Hide("mias_house"), Jump("mias_house_sneak")],
                                [Hide("mias_house"), Jump("night_closed_mia")]
                            ),
                            If(
                                M_mia.get_state() in [S_mia_midnight_help, S_mia_locked_room],
                                [Hide("mias_house"), Jump("mias_house_sneak")],
                                [Hide("mias_house"), Jump("night_closed_mia")]
                            )
                        )
                    )
                )
            )
        )

    if player.location.is_here(M_mia):
        imagebutton:
            focus_mask True
            pos (270,480)
            idle "objects/character_mia_02.png"
            hover HoverImage("objects/character_mia_02.png")
            action Hide("mias_house"), Jump("mia_dialogue_mias_house_front")

    imagebutton:
        focus_mask True
        if game.has_mail("mia"):
            pos (830,480)
            idle game.timer.image("objects/object_mailbox_mia01{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_mia01{}.png"))

        else:
            pos (830,500)
            idle game.timer.image("objects/object_mailbox_mia02{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_mia02{}.png"))
        action Hide("mias_house"), Function(game.lock_ui), Show("mias_mailbox")

screen mias_mailbox():
    add game.timer.image("backgrounds/location_mia_mailbox_day{}.jpg")

    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide('mias_mailbox'), Function(game.unlock_ui), MoveTo(L_miahouse)

    if game.mail["mia"] == "m_pizza_pamphlet":
        imagebutton:
            focus_mask True
            pos (240,480)
            idle game.timer.image("objects/object_mailbox_item02{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item02{}.png"))
            action MoveTo(L_miahouse_mailbox)

    elif game.mail["mia"] == "m_newspaper":
        imagebutton:
            focus_mask True
            pos (250,575)
            idle game.timer.image("objects/object_mailbox_item05{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item05{}.png"))
            action MoveTo(L_miahouse_mailbox)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
