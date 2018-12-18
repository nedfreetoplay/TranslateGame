screen home_front:
    add player.location.background

    imagebutton:
        if game.mail["player"] != "" or (erik.completed(erik_orcette) and not player.has_item("orcette") and not erik.known(erik_orcette_2) and orcette_mail_lock):
            pos (880,480)
            idle game.timer.image("objects/object_mailbox_home01{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_home01{}.png"))
        else:
            pos (880,500)
            idle game.timer.image("objects/object_mailbox_home02{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_home02{}.png"))
        action Hide("home_front"), Function(renpy.call, "home_lock_check", "Mailbox", "player_mailbox")

    imagebutton:
        focus_mask True
        pos (557,454)
        idle game.timer.image("objects/object_door_34{}.png")
        hover HoverImage(game.timer.image("objects/object_door_34{}.png"))
        action Hide("home_front"), Function(renpy.call, "home_lock_check", "Entrance", "home_entrance")

    imagebutton:
        focus_mask True
        pos (172,403)
        idle game.timer.image("objects/object_door_36{}.png")
        hover HoverImage(game.timer.image("objects/object_door_36{}.png"))
        action Hide("home_front"), Function(renpy.call, "home_lock_check", "Garage", "home_garage")

screen mailbox:
    if game.timer.is_dark():
        add "backgrounds/location_player_mailbox_night.jpg"
    else:
        add "backgrounds/location_player_mailbox_day.jpg"

    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("mailbox"), Jump("home_front")

    if erik.completed(erik_orcette) and not player.has_item("orcette") and not erik.known(erik_orcette_2) and orcette_mail_lock:
        imagebutton:
            focus_mask True
            pos (300,345)
            idle game.timer.image("mailbox_package{}")
            hover HoverImage(game.timer.image("mailbox_package{}"))
            action Hide("mailbox"), Jump("player_mailbox_dialogue")

    elif game.mail["player"] == "m_pizza_pamphlet":
        imagebutton:
            focus_mask True
            pos (240,480)
            idle game.timer.image("objects/object_mailbox_item02{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item02{}.png"))
            action Hide("mailbox"), Jump("player_mailbox_dialogue")

    elif game.mail["player"] == "m_newspaper":
        imagebutton:
            focus_mask True
            pos (250,575)
            idle game.timer.image("objects/object_mailbox_item05{}.png")
            hover HoverImage(game.timer.image("objects/object_mailbox_item05{}.png"))
            action Hide("mailbox"), Jump("player_mailbox_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
