screen ui:
    if not game.ui_locked:
        $ suffix = ""
        if player.location.name not in ["Town Map", "Bedroom", "Erik's House", "Mia's House"] and M_player.get_state() != S_player_start or game.timer.game_day() == 0:
            $ suffix = "_noskip"
        imagemap:
            ground "buttons/ui_ground.png"
            if renpy.get_screen("town_map"):
                idle "buttons/ui_idle_02{}.png".format(suffix)
                hover HoverImage("buttons/ui_idle_02{}.png".format(suffix))
            else:
                idle "buttons/ui_idle{}.png".format(suffix)
                hover HoverImage("buttons/ui_idle{}.png".format(suffix))
            alpha False
            if renpy.get_screen("town_map"):
                hotspot (16, 5, 71, 71) action [Hide("town_map"), Function(playMusic), Function(playSound), Jump("bedroom_dialogue")]
            elif M_mom.get_state() == S_mom_bad_guys_driveby and not game.timer.is_dark() and player.location in [L_home, L_home_bedroom]:
                hotspot (16, 5, 71, 71) action [Function(player.location.hide_screen), Function(playMusic), Function(playSound), Jump("bad_guys_driveby")]
            else:
                hotspot (16, 5, 71, 71) action [Function(player.location.hide_screen), Jump("map_dialogue")]
            hotspot (801, 5, 51, 68) action [Show("cellphone"), Play("audio", "audio/sfx_phone_notification.ogg")]
            if game.new_message:
                add "buttons/cellphone_app_alert.png" pos 835,5
            elif game.new_achievements:
                add "buttons/cellphone_achieve_alert.png" pos 835,5
            hotspot (867, 5, 60, 71) action If(renpy.get_screen("backpack"), [Hide("backpack"), Play("audio", "audio/sfx_phone_notification.ogg")], [Show("backpack"), Play("audio", "audio/sfx_backpack_open.ogg")])
            hotspot (946, 5, 68, 70) action ShowMenu("navigation")
            if suffix == "":
                hotspot (503, 44, 31, 25) action Function(game.timer.tick)

    else:
        imagemap:
            ground "buttons/ui_ground.png"
            idle "buttons/ui_idle_locked.png"
            hover HoverImage("buttons/ui_idle_locked.png")
            alpha False
            hotspot (16, 5, 71, 71) action NullAction()
            hotspot (801, 5, 51, 68) action [Show("cellphone"), Play("audio", "audio/sfx_phone_notification.ogg")]
            if game.new_message:
                add "buttons/cellphone_app_alert.png" pos 835,5
            elif game.new_achievements:
                add "buttons/cellphone_achieve_alert.png" pos 835,5
            hotspot (867, 5, 60, 71) action If(renpy.get_screen("backpack"), [Hide("backpack"), Play("audio", "audio/sfx_phone_notification.ogg")], [Show("backpack"), Play("audio", "audio/sfx_backpack_open.ogg")])
            hotspot (946, 5, 68, 70) action ShowMenu("navigation")

    text "{b}[player.inventory.money]{/b}" xpos 765 ypos 16 xalign 1.0

    $ what_location = store.locations_rus.get(player.location.name)
    text "{b}[what_location]{/b}" xpos 105 ypos 15 xalign 0.0
    if game.timer.is_morning():
        add "buttons/ui_day_cycle_bar.png" pos 444,29
        add "buttons/ui_day_cycle_bar.png" pos 499,29
        add "buttons/ui_day_cycle_bar.png" pos 554,29
    elif game.timer.is_afternoon():
        add "buttons/ui_day_cycle_bar.png" pos 499,29
        add "buttons/ui_day_cycle_bar.png" pos 554,29
    elif game.timer.is_evening():
        add "buttons/ui_day_cycle_bar.png" pos 554,29
    $ Day = game.timer.dayOfWeek(full=True)
    text "{b}[Day]{/b}" xpos 105 ypos 45 xalign 0.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
