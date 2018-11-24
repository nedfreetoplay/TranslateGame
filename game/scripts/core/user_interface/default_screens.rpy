screen say(who, what, side_image=None, two_window=False):
    if not two_window:
        window:
            id "window"
            has vbox:
                style "say_vbox"
            if who:
                text who id "who"
            text what id "what"
    else:
        vbox:
            style "say_two_window_vbox"
            if who:
                window:
                    style "say_who_window"
                    text who:
                        id "who"
            window:
                id "window"
                has vbox:
                    style "say_vbox"
                text what id "what"
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0
    use quick_menu

screen choice(items):
    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        has vbox:
            style "menu"
            spacing 10

        for caption, action, chosen in items:

            if action:
                if caption[0:2] == '<>':
                    button:
                        style "menu_choice_button"
                        text caption[2:] style "inactive_menu_choice"

                else:
                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

            else:
                text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True
    style inactive_menu_choice:
        color "#777777"
        drop_shadow [(1,1)]
        size 16
        text_align 0.5
        xalign 0.5
        yalign 0.5

    style menu_window is default

    style menu_choice is button_text clear


    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.30)
        xmaximum int(config.screen_width * 0.30)
        xpadding 3
        ypadding 3

screen input(prompt):
    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            style "nvl_vbox"
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10
                if who is not None:
                    text who id who_id
                text what id what_id
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                    else:
                        text caption style "nvl_dialogue"
    add SideImage() xalign 0.0 yalign 1.0
    use quick_menu

screen name_input:
    add "backgrounds/menu_name.jpg"
    add SnowBlossom(Animation("buttons/leaf01.png", 0.15, "buttons/leaf02.png", 0.15))
    add "backgrounds/menu_name_overlay.png"
    add Input(size=16, color="#5d9aff", default=firstname, changed=name_func, length=12, xpos= 720, ypos = 392, allow = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    key "K_RETURN" action Start()
    imagebutton:
        idle "buttons/menu_name_back01.png"
        hover HoverImage("buttons/menu_name_back01.png")
        action Hide("name_input"), Show("main_menu")
        xpos 726
        ypos 231
    imagebutton:
        idle "buttons/menu_name_start01.png"
        hover HoverImage("buttons/menu_name_start01.png")
        action Start()
        xpos 726
        ypos 506

transform credit_scroll:
    xalign 0.0 yalign 0.0
    linear 20.0 yalign 1.0

screen popup(Image):
    zorder 100
    imagebutton idle "backgrounds/menu_ground.png" action NullAction() xalign 0.0 yalign 0.0
    add Image xalign 0.5 yalign 0.5


    timer 1.0 action Hide("popup")

screen route_warning():
    add "backgrounds/blank.jpg"
    add "boxes/popup_warning.png" at truecenter
    imagebutton:
        focus_mask True
        pos (298,378)
        idle "buttons/menu_goback.png"
        hover HoverImage("buttons/menu_goback.png")
        action Hide("route_warning"), Function(player.location.call_screen, new_context = True)

    imagebutton:
        focus_mask True
        pos (612,377)
        idle "buttons/menu_continue.png"
        hover HoverImage("buttons/menu_continue.png")
        action Return()

screen adult_warning:
    imagebutton:
        focus_mask True
        pos (435,635)
        idle "buttons/menu_yes.png"
        hover HoverImage("buttons/menu_yes.png")
        action Return()

    imagebutton:
        focus_mask True
        pos (565,635)
        idle "buttons/menu_no.png"
        hover HoverImage("buttons/menu_no.png")
        action Quit(confirm=False)

screen changelog:
    add "backgrounds/menu_changelog.jpg"

    side "c b r":
        area (31, 60, 962, 550)
        viewport id "changelog":
            draggable True
            mousewheel True
            has vbox
            $ changelog = ""
            $ changelog_lines = 0
            python:

                if renpy.variant("mobile"):
                    file_ = renpy.file("changelog.txt")
                else:
                    file_ = codecs.open(sys.path[0] + "/game/changelog.txt", encoding = "utf-8")


                for line in file_:
                    line = line.replace("\r\n", "")
                    line = line.replace("\n", "")
                    changelog += "{}\n".format(line)
                    changelog_lines += 1

                file_.close()
            $ changelog_ylength = changelog_lines * 19
            imagemap:
                ground im.Composite((962, changelog_ylength), (0, 0), "backgrounds/menu_ground.png")

                vbox:
                    text "[changelog]" text_align 0.0

    imagebutton:
        pos (50,675)
        idle "buttons/menu_name_back01.png"
        hover HoverImage("buttons/menu_name_back01.png")
        action Hide("changelog"), Show("main_menu")

screen credits:
    add "backgrounds/menu_credits.jpg"

    use pledgers

    imagebutton:
        pos (50,675)
        idle "buttons/menu_name_back01.png"
        hover HoverImage("buttons/menu_name_back01.png")
        action Function(playMusic, "audio/music_title01.ogg"), Return()

screen creditsquick() tag menu:
    add "backgrounds/menu_credits.jpg"

    use pledgers

    imagebutton:
        pos (50,675)
        idle "buttons/menu_name_back01.png"
        hover HoverImage("buttons/menu_name_back01.png")
        action Function(playMusic), Return()

screen pledgers() tag menu:
    side "c b r":
        area (31, 235, 962, 358)
        viewport id "pledgers":
            draggable True
            mousewheel True
            has vbox
            $ pledgers = ""
            $ pledgers_lines = 0
            python:

                if renpy.variant("mobile"):
                    file_ = renpy.file("pledge_list.txt")
                else:
                    file_ = codecs.open(sys.path[0] + "/game/pledge_list.txt", encoding = "utf-8")


                for line in file_:
                    line = line.replace("\r\n", "")
                    line = line.replace("\n", "")
                    name,colour = line.split(",")
                    pledgers += "{{color=#{0}}}{1}{{/color}}, ".format(colour,name)
                    pledgers_lines += 1

                pledgers = pledgers[:-2]

                file_.close()
            $ ylength = (len(pledgers) / pledgers_lines) * 19
            imagemap:
                ground im.Composite((962, ylength), (0, 0), "backgrounds/menu_ground.png")

                vbox:
                    text "[pledgers]" text_align 0.5 at credit_scroll

screen main_menu() tag menu:
    $ playMusic("audio/music_title01.ogg")
    window:
        style "mm_root"
    add "backgrounds/menu_menu.jpg"
    add "cloud_animation" xpos 600 ypos 65
    add SnowBlossom(Animation("buttons/leaf01.png", 0.15, "buttons/leaf02.png", 0.15))
    imagemap:

        ground "backgrounds/menu_menu_overlay.png"
        idle "menu_idle"
        hover HoverImage("menu_idle")

        alpha False

        hotspot ( 730, 211, 175, 48) action [Hide("main_menu"), ShowMenu("name_input"), Hide("gui_tooltip")] hovered Show("gui_tooltip", my_picture = "buttons/tooltip_01.png", my_tt_xpos=0, my_tt_ypos=0) unhovered Hide("gui_tooltip")
        hotspot ( 730, 279, 175, 48) action [Hide("main_menu"), ShowMenu("load"), Hide("gui_tooltip")] hovered Show("gui_tooltip", my_picture = "buttons/tooltip_02.png", my_tt_xpos=0, my_tt_ypos=0) unhovered Hide("gui_tooltip")
        hotspot ( 730, 347, 175, 48) action [Hide("main_menu"), ShowMenu("preferences"), Hide("gui_tooltip")] hovered Show("gui_tooltip", my_picture = "buttons/tooltip_03.png", my_tt_xpos=0, my_tt_ypos=0) unhovered Hide("gui_tooltip")
        hotspot ( 730, 416, 175, 48) action [Hide("main_menu"), ShowMenu("cookie_jar"), Hide("gui_tooltip")] hovered Show("gui_tooltip", my_picture = "buttons/tooltip_06.png", my_tt_xpos=0, my_tt_ypos=0) unhovered Hide("gui_tooltip")
        hotspot ( 730, 485, 175, 48) action [Hide("main_menu"), Function(playSound), Function(playMusic, "<loop 241.5>audio/music_credits.ogg"), ShowMenu("credits"), Hide("gui_tooltip")] hovered Show("gui_tooltip", my_picture = "buttons/tooltip_04.png", my_tt_xpos=0, my_tt_ypos=0) unhovered Hide("gui_tooltip")
        hotspot ( 730, 554, 175, 48) action Quit(confirm = True) hovered Show("gui_tooltip", my_picture = "buttons/tooltip_05.png", my_tt_xpos=0, my_tt_ypos=0) unhovered Hide("gui_tooltip")
        text "[config.version] changelog" xalign 0.9 yalign 0.85
        hotspot (800, 610,175, 48) action [Hide("main_menu"), ShowMenu("changelog"), Hide("gui_tooltip")]

init -2:
    style mm_button:
        size_group "mm"

screen navigation() tag menu:
    imagemap:
        ground "backgrounds/menu_quickmenu.jpg"
        idle "backgrounds/menu_quickmenu.jpg"
        hover HoverImage("backgrounds/menu_quickmenu.jpg")
        hotspot ( 430, 139, 167, 40) action Return()
        hotspot ( 430, 256, 167, 40) action MainMenu()
        hotspot ( 430, 317, 167, 40) action Hide("navigation"), ShowMenu("save")
        hotspot ( 430, 379, 167, 40) action Hide("navigation"), ShowMenu("load")
        hotspot ( 430, 440, 167, 40) action Hide("navigation"), ShowMenu("preferences")
        hotspot ( 430, 503, 167, 40) action Hide("navigation"), Function(playSound), Function(playMusic, "<loop 241.5>audio/music_credits.ogg"), ShowMenu("creditsquick")
        hotspot ( 430, 564, 167, 40) action Quit()

    key "K_ESCAPE" action Return()

screen file_picker():
    frame:
        style "file_picker_frame"

        has vbox

        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 3
        $ rows = 2

        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"


            for i in range(1, columns * rows + 1):


                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text

screen preferences() tag menu:
    $ autosaving_enabled = persistent.autosaving_enabled
    $ allow_internet_connections = persistent.allow_internet_connections
    imagemap:
        ground "backgrounds/menu_settings.jpg"
        idle "backgrounds/menu_settings.jpg"
        hover HoverImage("backgrounds/menu_settings.jpg")
        hotspot ( 430, 80, 167, 40) action Return()
        hotspot ( 233, 210, 167, 33) action Preference("display", "window")
        hotspot ( 233, 260, 167, 33) action Preference("display", "fullscreen")
        hotspot ( 233, 360, 167, 33) action Preference("skip", "all")
        hotspot ( 233, 410, 167, 33) action Preference("skip", "seen")
        hotspot ( 567, 211, 167, 33) action If(autosaving_enabled, SetField(persistent, "autosaving_enabled", False), SetField(persistent, "autosaving_enabled", True))
        hotspot ( 567, 368, 167, 33) action If(allow_internet_connections, SetField(persistent, "allow_internet_connections", False), SetField(persistent, "allow_internet_connections", True))

        bar value Preference("text speed") at Position (xpos= 233, ypos = 505, xmaximum = 220, ymaximum = 70)
        bar value Preference("music volume") at Position (xpos= 233, ypos = 580, xmaximum = 220, ymaximum = 70)
        bar value Preference("sound volume") at Position (xpos= 233, ypos = 650, xmaximum = 220, ymaximum = 70)
        add Input(size=16, color="#fefefe", default=persistent.autosave_frequency, changed=setAutosaveFrequency, length=4, xpos= 657, ypos = 270, allow = "0123456789")

    if _preferences.fullscreen:
        add "buttons/checkbox.png" pos 432,269
    else:
        add "buttons/checkbox.png" pos 432,219

    if _preferences.skip_unseen:
        add "buttons/checkbox.png" pos 432,369
    else:
        add "buttons/checkbox.png" pos 432,419

    if persistent.autosaving_enabled:
        add "buttons/checkbox.png" pos 766,219

    if persistent.allow_internet_connections:
        add "buttons/checkbox.png" pos 766,376

screen quick_preferences tag menu:
    $ autosaving_enabled = persistent.autosaving_enabled
    $ allow_internet_connections = persistent.allow_internet_connections
    imagemap:
        ground "backgrounds/menu_settings.jpg"
        idle "backgrounds/menu_settings.jpg"
        hover HoverImage("backgrounds/menu_settings.jpg")
        hotspot (430, 139, 167, 40) action Return()
        hotspot (233, 270, 167, 33) action Preference("display", "window")
        hotspot (233, 320, 167, 33) action Preference("display", "fullscreen")
        hotspot ( 567, 211, 167, 33) action If(autosaving_enabled, SetField(persistent, "autosaving_enabled", False), SetField(persistent, "autosaving_enabled", True))
        hotspot ( 567, 368, 167, 33) action If(allow_internet_connections, SetField(persistent, "allow_internet_connections", False), SetField(persistent, "allow_internet_connections", True))

        bar value Preference("text speed") at Position (xpos= 404, ypos = 415, xmaximum = 220, ymaximum = 70)
        bar value Preference("music volume") at Position (xpos= 404, ypos = 502, xmaximum = 220, ymaximum = 70)
        bar value Preference("sound volume") at Position (xpos= 404, ypos = 575, xmaximum = 220, ymaximum = 70)
        add Input(size=16, color="#fefefe", default=persistent.autosave_frequency, changed=setAutosaveFrequency, length=4, xpos= 657, ypos = 270, allow = "0123456789")

    if _preferences.fullscreen:
        add "buttons/checkbox.png" pos 432,328
    else:
        add "buttons/checkbox.png" pos 432,278

    if persistent.autosaving_enabled:
        add "buttons/checkbox.png" pos 765,218

    if persistent.allow_internet_connections:
        add "buttons/checkbox.png" pos 766,376

screen save() tag menu:
    imagemap:
        ground "backgrounds/menu_saving01.jpg"
        idle "backgrounds/menu_saving01.jpg"
        hover HoverImage("backgrounds/menu_saving01.jpg")
        alpha False

        use load_save_page_buttons(FileCurrentPage())

        hotspot (133, 275, 225, 168) hovered Show("load_save_slot_description", slot = 1) unhovered Hide("load_save_slot_description") action Hide("load_save_slot_description"), Function(clearSaveName), Show("set_save_description", file_save = FileSave(1), slot = 1):
            use load_save_slot(1)
        hotspot (400, 275, 225, 168) hovered Show("load_save_slot_description", slot = 2) unhovered Hide("load_save_slot_description") action Hide("load_save_slot_description"), Function(clearSaveName), Show("set_save_description", file_save = FileSave(2), slot = 2):
            use load_save_slot(2)
        hotspot (668, 275, 225, 168) hovered Show("load_save_slot_description", slot = 3) unhovered Hide("load_save_slot_description") action Hide("load_save_slot_description"), Function(clearSaveName), Show("set_save_description", file_save = FileSave(3), slot = 3):
            use load_save_slot(3)
        hotspot (133, 468, 225, 168) hovered Show("load_save_slot_description", slot = 4) unhovered Hide("load_save_slot_description") action Hide("load_save_slot_description"), Function(clearSaveName), Show("set_save_description", file_save = FileSave(4), slot = 4):
            use load_save_slot(4)
        hotspot (400, 468, 225, 168) hovered Show("load_save_slot_description", slot = 5) unhovered Hide("load_save_slot_description") action Hide("load_save_slot_description"), Function(clearSaveName), Show("set_save_description", file_save = FileSave(5), slot = 5):
            use load_save_slot(5)
        hotspot (668, 468, 225, 168) hovered Show("load_save_slot_description", slot = 6) unhovered Hide("load_save_slot_description") action Hide("load_save_slot_description"), Function(clearSaveName), Show("set_save_description", file_save = FileSave(6), slot = 6):
            use load_save_slot(6)

screen set_save_description(file_save, slot) tag save:
    python:
        if FileSaveName(slot) == "":
            store.save_name = "{} - Day {}".format(store.firstname, game.timer._game_day)
        else:
            store.save_name = FileSaveName(slot)
    modal True
    key "mouseup_3" action [file_save, Hide("set_save_description")]
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action file_save, Hide("set_save_description")
    add "boxes/popup_name_save.png" at truecenter
    text "{b}Give this save a description:{/b}" xalign 0.5 yalign 0.415
    add Input(size = 20, color = "#FFFFFF", default = store.save_name, changed = save_description, length = 35, xpos = 300, ypos = 353, allow = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
    key "K_RETURN" action [file_save, Hide("set_save_description")]
    imagebutton idle "buttons/menu_ok.png" hover HoverImage("buttons/menu_ok.png") action [file_save, Hide("set_save_description")] xalign 0.5 yalign 0.57

screen load() tag menu:
    imagemap:
        ground "backgrounds/menu_loading01.jpg"
        idle "backgrounds/menu_loading01.jpg"
        hover HoverImage("backgrounds/menu_loading01.jpg")
        alpha False

        use load_save_page_buttons(FileCurrentPage())

        hotspot (133, 275, 225, 168) hovered Show("load_save_slot_description", slot = 1) unhovered Hide("load_save_slot_description") action FileLoad(1):
            use load_save_slot(1)
        hotspot (400, 275, 225, 168) hovered Show("load_save_slot_description", slot = 2) unhovered Hide("load_save_slot_description") action FileLoad(2):
            use load_save_slot(2)
        hotspot (668, 275, 225, 168) hovered Show("load_save_slot_description", slot = 3) unhovered Hide("load_save_slot_description") action FileLoad(3):
            use load_save_slot(3)
        hotspot (133, 468, 225, 168) hovered Show("load_save_slot_description", slot = 4) unhovered Hide("load_save_slot_description") action FileLoad(4):
            use load_save_slot(4)
        hotspot (400, 468, 225, 168) hovered Show("load_save_slot_description", slot = 5) unhovered Hide("load_save_slot_description") action FileLoad(5):
            use load_save_slot(5)
        hotspot (668, 468, 225, 168) hovered Show("load_save_slot_description", slot = 6) unhovered Hide("load_save_slot_description") action FileLoad(6):
            use load_save_slot(6)

screen load_save_page_buttons(load_save_page) tag save:
    if load_save_page in ["auto", "quick", "1", "2"]:
        $ load_save_page = 3
    $ load_save_page = int(load_save_page)

    hotspot (289, 208, 38, 37) clicked FilePage("auto"):
        use load_save_page_number((289, 208, 38, 37), "auto")
    hotspot (348, 208, 38, 37) clicked FilePage("quick"):
        use load_save_page_number((348, 208, 38, 37), "quick")
    hotspot (407, 208, 38, 37) clicked FilePage(load_save_page - 2):
        use load_save_page_number((407, 208, 38, 37), load_save_page - 2)
    hotspot (465, 208, 38, 37) clicked FilePage(load_save_page - 1):
        use load_save_page_number((465, 208, 38, 37), load_save_page - 1)
    hotspot (524, 208, 38, 37) clicked FilePage(load_save_page):
        use load_save_page_number((524, 208, 38, 37), load_save_page)
    hotspot (583, 208, 38, 37) clicked FilePage(load_save_page + 1):
        use load_save_page_number((583, 208, 38, 37), load_save_page + 1)
    hotspot (642, 208, 38, 37) clicked FilePage(load_save_page + 2):
        use load_save_page_number((642, 208, 38, 37), load_save_page + 2)
    hotspot (700, 208, 38, 37) clicked FilePage(load_save_page + 3):
        use load_save_page_number((700, 208, 38, 37), load_save_page + 3)

    hotspot (428, 137, 172, 44) action Return()
    hotspot (134, 208, 94, 38) clicked FilePagePrevious()
    if (load_save_page + 7) < 99:
        hotspot (800, 208, 94, 38) clicked FilePageNext()

screen load_save_page_number(load_save_page_area, load_save_page_name) tag save:
    if load_save_page_name == "auto":
        text "{b}A{/b}" xalign 0.5 yalign 0.6
    elif load_save_page_name == "quick":
        text "{b}Q{/b}" xalign 0.5 yalign 0.6
    else:
        text str("{b}" + str(load_save_page_name).zfill(2) + "{/b}") xalign 0.5 yalign 0.6

screen load_save_slot(slot) tag save:
    $ file_text = "{}. {}".format(str(FileSlotName(slot, 6)).zfill(2), FileTime(slot))
    add FileScreenshot(slot) xoffset 2 yoffset 2
    text "{b}[file_text]{/b}" yoffset -20
    if FileLoadable(slot):
        imagebutton idle "buttons/delete_button_01.png" hover HoverImage("buttons/delete_button_01.png") xalign 0.99 yalign 0.01 action FileDelete(slot)
    key "save_delete" action FileDelete(slot)

screen load_save_slot_description(slot) tag save:
    $ file_text = "{}".format(FileSaveName(slot))
    if file_text == "":
        $ file_text = "No Description"
    if not file_text.endswith("."):
        $ file_text += "."
    text "{b}[file_text]{/b}" xalign 0.5 yalign 0.92

init -2 python:
    config.thumbnail_width = 221
    config.thumbnail_height = 164

screen yesno_prompt(message, yes_action, no_action):
    modal True

    window:
        style "gm_root"

    if message in [layout.DELETE_SAVE, layout.OVERWRITE_SAVE]:
        add "backgrounds/menu_confirm.jpg"
        if message == layout.DELETE_SAVE:
            text "{b}Are you sure you want to delete this save?" xalign 0.5 yalign 0.56

        elif message == layout.OVERWRITE_SAVE:
            text "{b}Are you sure you want to overwrite this save?" xalign 0.5 yalign 0.56

    elif message == layout.LOADING:
        text "{b}Are you sure you want to load this save?" xalign 0.5 yalign 0.56

    elif message == layout.QUIT:
        text "{b}Are you sure you want to quit the game?" xalign 0.5 yalign 0.56

    elif message == layout.MAIN_MENU:
        text "{b}Are you sure you want to quit to the main menu?" xalign 0.5 yalign 0.56

    imagemap:
        ground "menu_ground"
        idle "menu_quit_idle"
        hover HoverImage("menu_quit_idle")

        alpha False


        hotspot ( 312, 463, 175, 48) action yes_action
        hotspot ( 530, 463, 175, 48) action no_action


    if message == layout.QUIT:
        $ persistent.time_spent_playing += (time() - time_spent_playing_start)
        $ time_spent_playing_start = time()
        $ time_spent_playing_string = format_seconds_to_dhm(persistent.time_spent_playing)
        text "You've spent [time_spent_playing_string] eating cookies..." xalign 0.5 yalign 0.5

    text "{a=http://www.patreon.com/summertimesaga}http://www.patreon.com/summertimesaga{/a}" xalign 0.5 yalign 0.855


    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"

screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

screen quick_menu():
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Hide") action HideInterface()
        textbutton _("Save") action ShowMenu("save")
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu("preferences")

init -2:
    style quick_button is default:
        background None
        xpadding 7
        ypadding -2

    style quick_button_text is default:
        size 20
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

screen popup_unfinished:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_unfinished")

    key "K_SPACE" action Hide("popup_unfinished")

    imagebutton:
        focus_mask True
        align (0.5,0.5)
        idle "boxes/popup_unfinished.png"
        action Hide("popup_unfinished")

screen button(Image, Label):
    imagebutton:
        align (0.5,0.97)
        idle str(Image) + ".png"
        hover HoverImage(str(Image)+".png")
        action Hide("button"), Jump(Label)

screen sex_anim_buttons:
    imagebutton:
        focus_mask True
        pos (10,600)
        if anim_toggle:
            idle "buttons/anim_02.png"
            hover HoverImage("buttons/anim_02.png")
        else:
            idle "buttons/anim_01.png"
            hover HoverImage("buttons/anim_01.png")
        action [
            If(
                anim_toggle,
                [SetVariable("anim_toggle", False),SetVariable("animated", False)] ,
                SetVariable("anim_toggle", True)
            ),
            Return
        ]

screen sex_xray_anim_buttons:
    imagebutton:
        focus_mask True
        pos (10,600)
        if anim_toggle:
            idle "buttons/anim_02.png"
            hover HoverImage("buttons/anim_02.png")
        else:
            idle "buttons/anim_01.png"
            hover HoverImage("buttons/anim_01.png")
        action [
            If(
                anim_toggle,
                SetVariable("anim_toggle", False),
                SetVariable("anim_toggle", True)
            ),
            Return
        ]

    imagebutton:
        pos (940,600)
        if xray:
            idle "buttons/anim_03.png"
            hover HoverImage("buttons/anim_03.png")
        else:
            idle "buttons/anim_04.png"
            hover HoverImage("buttons/anim_04.png")
        action [
            If(
                xray, 
                SetVariable("xray", False), 
                SetVariable("xray", True)
            )
        ]

screen escape_key:
    key "K_ESCAPE" action ShowMenu("navigation")

screen gameover:
    add "backgrounds/menu_gameover.jpg"
    imagebutton:
        focus_mask True
        pos (265,443)
        idle "buttons/menu_load.png"
        hover HoverImage("buttons/menu_load.png")
        action ShowMenu("load")
    imagebutton:
        focus_mask True
        pos (527,443)
        idle "buttons/menu_retry.png"
        hover HoverImage("buttons/menu_retry.png")
        action Hide("gameover"), Jump("dexter_fight_pre")

screen cheat_option:
    add "backgrounds/menu_cheats.jpg"
    imagebutton:
        focus_mask True
        idle "buttons/menu_cheats_01.png"
        hover HoverImage("buttons/menu_cheats_01.png")
        action Jump("intro")
        xpos 230
        ypos 240

    imagebutton:
        focus_mask True
        idle "buttons/menu_cheats_02.png"
        hover HoverImage("buttons/menu_cheats_02.png")
        action Jump("cheat_intro")
        xpos 610
        ypos 240
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
