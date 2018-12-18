screen debug_menu(current_screen):
    if not renpy.variant("pc"):
        key "K_AC_BACK" action Hide("debug_menu")
    else:
        key "K_ESCAPE" action Hide("debug_menu")
        key "mouseup_3" action Hide("debug_menu")
    imagebutton:
        focus_mask True
        idle "backgrounds/menu_ground.png"
        action NullAction()

    frame:
        xpadding 10
        ypadding 40
        xalign 0.5
        yalign 0.5
        xysize (1024-140, 768-140)
        has hbox
        vbox:
            textbutton "General" action Show("debug_menu", current_screen = "general")
            textbutton "Machines" action Show("debug_menu", current_screen = "machines")
            textbutton "Locations" action Show("debug_menu", current_screen = "locations")
            textbutton "Player" action Show("debug_menu", current_screen = "player")
            textbutton "Machines info" action Show("debug_menu", current_screen="machines_info")
        vbox:
            xfill True
            if current_screen == "general":
                textbutton "Tick Timer" action Function(game.timer.tick)
                hbox:
                    textbutton "Unlock UI" action Function(game.unlock_ui)
                    textbutton "Lock UI" action Function(game.lock_ui)
                    if game.ui_locked:
                        text "UI is locked" color "#c61f1d" size 16
                    else:
                        text "UI is unlocked" color "#28701d" size 16
                textbutton "Unlock Cookie Jar Scenes" action Function(unlock_all_scenes)
                textbutton "Set Rump Scene" action Function(game.set_rump_n_cunt)
                textbutton "Skip First Day" action Function(game.skip_first_day)
                textbutton "Print items list to console" action Function (print_item_list)
                textbutton "Unlock All locations" action Function (unlock_all_locations)
                hbox:
                    textbutton "Force Unlock Map" action Function(game.force_unlock_ui)
                    textbutton "Unforce Unlock Map" action Function(game.force_lock_ui)
                    if game.force_unlock_map:
                        text "Map is unlocked" color "#28701d" size 16
                    else:
                        text "Map is locked" color "#c61f1d" size 16
                text "Set day to:"
                hbox:
                    textbutton "Mon." action Function(game.timer.set_time, 1, 0)
                    textbutton "Tue." action Function(game.timer.set_time, 1, 1)
                    textbutton "Wed." action Function(game.timer.set_time, 1, 2)
                    textbutton "Thur." action Function(game.timer.set_time, 1, 3)
                    textbutton "Fri." action Function(game.timer.set_time, 1, 4)
                    textbutton "Sat." action Function(game.timer.set_time, 1, 5)
                    textbutton "Sun." action Function(game.timer.set_time, 1, 6)
                text "Set time to:"
                hbox:
                    textbutton "Morning" action Function(game.timer.set_time, 0)
                    textbutton "Afternoon" action Function(game.timer.set_time, 1)
                    textbutton "Evening" action Function(game.timer.set_time, 2)
                    textbutton "Night" action Function(game.timer.set_time, 3)
                hbox:
                    textbutton "Lock Sleep" action Function (game.lock_sleep)
                    textbutton "Unlock Sleep" action Function (game.unlock_sleep)
                    if game.sleep_lock:
                        text "Sleep is locked" color "#c61f1d" size 16
                    else:
                        text "Sleep is unlocked" color "#28701d" size 16
                hbox:
                    textbutton "Cheat Mode Toggle" action Function (game.toggle_cheat_mode)
                    if game.cheat_mode:
                        text "Cheat Mode is ON" color "#c61f1d" size 16
                    else:
                        text "Cheat Mode is OFF" color "#28701d" size 16
                hbox:
                    xfill True
                    add Input(size=20, color="#fefefe", default="", changed=setDebugMenuPythonToWatch, length=60, allow = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789./*-+'{}[]()_&|\"\\=%,;:#")
                    textbutton "Watch" action Function(renpy.watch, store.debugMenuPythonToWatch)
                    textbutton "Unwatch" action Function(renpy.unwatch, store.debugMenuPythonToWatch)
                hbox:
                    xfill True
                    textbutton "Toggle Debug Period" action Function(Game.toggle_debug_period)
                    text "[game.get_period_str]" color "#c61f1d" size 16
                hbox:
                    xfill True
                    textbutton "Toggle Label Name Notification" action ToggleField(persistent, "notify_label_name")
                    if persistent.notify_label_name:
                        text "Label name notifications are ON" color "#c61f1d" size 16
                    else:
                        text "Label name notifications are OFF" color "#28701d" size 16

            elif current_screen == "player":
                hbox:
                    xfill True
                    textbutton "Increase STR" action Function(player.increase_str)
                    textbutton "Increase INT" action Function(player.increase_int)
                    textbutton "Increase CHR" action Function(player.increase_chr)
                    textbutton "Increase DEX" action Function(player.increase_dex)
                hbox:
                    xfill True
                    add Input(size=20, color="#fefefe", default="1000", changed=setDebugMenuMoney, length=6, allow = "0123456789")
                    textbutton "Add" action Function(player.get_money, int(store.debugMenuMoney))
                    textbutton "Remove" action Function(player.spend_money, int(store.debugMenuMoney))

            elif current_screen == "machines":
                $ machines = filter(lambda m:len(m._states.keys())>2, store.machines.values())
                hbox:
                    python:
                        for machine in machines[:5]:
                            ui.textbutton("Adv {}".format(machine._name.capitalize()), clicked=Function(machine.advance), text_style="style_textbutton_debug")
                hbox:
                    python:
                        for machine in machines[5:10]:
                            ui.textbutton("Adv {}".format(machine._name.capitalize()), clicked=Function(machine.advance), text_style="style_textbutton_debug")
                hbox:
                    python:
                        for machine in machines[10:15]:
                            ui.textbutton("Adv {}".format(machine._name.capitalize()), clicked=Function(machine.advance), text_style="style_textbutton_debug")
                hbox:
                    python:
                        for machine in machines[15:20]:
                            ui.textbutton("Adv {}".format(machine._name.capitalize()), clicked=Function(machine.advance), text_style="style_textbutton_debug")
                hbox:
                    python:
                        for machine in machines[20:24]:
                            ui.textbutton("Adv {}".format(machine._name.capitalize()), clicked=Function(machine.advance), text_style="style_textbutton_debug")

            elif current_screen == "locations":
                $ locations = []
                for loc in store.locations:
                    $ locations.append(store.locations[loc])
                $ locations = filter(lambda x:L_map in x.parents, locations)
                hbox:
                    python:
                        for loc in locations[:4]:
                            ui.textbutton("Unlock {}".format(loc.name.capitalize()), clicked=Function(loc.unlock, True, False), text_style="style_textbutton_debug")
                hbox:
                    python:
                        for loc in locations[4:8]:
                            ui.textbutton("Unlock {}".format(loc.name.capitalize()), clicked=Function(loc.unlock, True, False), text_style="style_textbutton_debug")
                hbox:
                    python:
                        for loc in locations[8:12]:
                            ui.textbutton("Unlock {}".format(loc.name.capitalize()), clicked=Function(loc.unlock, True, False), text_style="style_textbutton_debug")
                hbox:
                    python:
                        for loc in locations[12:16]:
                            ui.textbutton("Unlock {}".format(loc.name.capitalize()), clicked=Function(loc.unlock, True, False), text_style="style_textbutton_debug")
                hbox:
                    python:
                        for loc in locations[16:20]:
                            ui.textbutton("Unlock {}".format(loc.name.capitalize()), clicked=Function(loc.unlock, True, False), text_style="style_textbutton_debug")
                hbox:
                    python:
                        for loc in locations[20:24]:
                            ui.textbutton("Unlock {}".format(loc.name.capitalize()), clicked=Function(loc.unlock, True, False), text_style="style_textbutton_debug")
                hbox:
                    python:
                        for loc in locations[24:28]:
                            ui.textbutton("Unlock {}".format(loc.name.capitalize()), clicked=Function(loc.unlock, True, False), text_style="style_textbutton_debug")
                hbox:
                    python:
                        for loc in locations[28:31]:
                            ui.textbutton("Unlock {}".format(loc.name.capitalize()), clicked=Function(loc.unlock, True, False), text_style="style_textbutton_debug")

            elif current_screen == "machines_info":
                $ machines = filter(lambda m:m.priority>0, store.machines.values())
                python:
                    for machine in machines:
                        ui.text(repr(machine), style="style_machine_info_debug")
    imagebutton:
        focus_mask True
        pos (905, 80)
        idle "buttons/computer_button_03.png"
        hover HoverImage("buttons/computer_button_03.png")
        action Hide("debug_menu")
    imagebutton:
        focus_mask True
        pos (860, 80)
        idle "buttons/computer_button_05.png"
        hover HoverImage("buttons/computer_button_05.png")
        action Hide("debug_menu"), Call("_console")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
