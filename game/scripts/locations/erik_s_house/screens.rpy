screen eriks_house() tag eriks_house:


    add game.timer.image("backgrounds/location_erik_house_day{}.jpg")

    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    imagebutton:
        focus_mask True
        pos (350,417)
        idle game.timer.image("objects/object_door_18{}.png")
        hover HoverImage(game.timer.image("objects/object_door_18{}.png"))
        action If(
            not erik.over(erik_intro),
            [Hide("eriks_house"), Jump("door18_locked_dialogue")],
            [Hide("eriks_house"),
             If(
                mrsj.known(mrsj_intro),
                If(
                    not game.timer.is_dark(),
                    [Play("audio", sfxDoor()),
                     If(
                        erik.in_progress(erik_gf_stolen),
                        Jump("erik_gf_stolen"),
                        Jump("erik_indoors")
                     )
                    ],
                    If(
                        erik.in_progress(erik_thief),
                        [Jump("erik_thief_block")],
                        [Function(playSound), Play("audio", sfxDoor()),
                         If(
                            erik.in_progress(erik_gf_stolen),
                            Jump("erik_gf_stolen"),
                            Jump("erik_indoors")
                         )
                        ],
                    )
                ),
                If(
                   M_dewitt.is_state(S_dewitt_eve_karaoke),
                   Jump("erik_indoors"),
                   Jump("closed_erik")
                )
             )
            ]
        )

    imagebutton:
        focus_mask True
        pos (846,410)
        idle game.timer.image("objects/object_door_67{}.png")
        hover HoverImage(game.timer.image("objects/object_door_67{}.png"))
        action [Hide("eriks_house"), Jump("erik_backyard_dialogue")]

    imagebutton:
        focus_mask True
        if game.mail["erik"] != "":
            pos (735,480)
            idle game.timer.image("objects/object_mailbox_erik01{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_erik01{}.png"))
        else:
            pos (735,500)
            idle game.timer.image("objects/object_mailbox_erik02{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_erik02{}.png"))
        action Hide("eriks_house"), Function(game.lock_ui), Show("eriks_mailbox")

screen eriks_mailbox():
    if game.timer.is_dark():
        add "backgrounds/location_erik_mailbox_night.jpg"
    else:
        add "backgrounds/location_erik_mailbox_day.jpg"

    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide('eriks_mailbox'), Function(game.unlock_ui), MoveTo(L_erikhouse)

    if game.mail["erik"] == "m_magazine":
        imagebutton:
            focus_mask True
            pos (310,455)
            idle game.timer.image("objects/object_mailbox_item01{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item01{}.png"))
            action MoveTo(L_erikhouse_mailbox)

    elif game.mail["erik"] == "m_dad_letter":
        imagebutton:
            focus_mask True
            pos (510,345)
            idle game.timer.image("objects/object_mailbox_item03{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item03{}.png"))
            action MoveTo(L_erikhouse_mailbox)

    elif game.mail["erik"] == "m_pizza_pamphlet":
        imagebutton:
            focus_mask True
            pos (240,480)
            idle game.timer.image("objects/object_mailbox_item02{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item02{}.png"))
            action MoveTo(L_erikhouse_mailbox)

    elif game.mail["erik"] == "m_newspaper":
        imagebutton:
            focus_mask True
            pos (250,575)
            idle game.timer.image("objects/object_mailbox_item05{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item05{}.png"))
            action MoveTo(L_erikhouse_mailbox)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
