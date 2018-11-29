init -1 python:
    theme.roundrect(
        widget = "#8833ce",
        widget_hover = "#cd249b",
        widget_text = "#000000",
        widget_selected = "#b6d754",
        disabled = "#57cdff",
        disabled_text = "#717be5",
        label = "#000000",
        frame = "#04b4ff",
        mm_root = "backgrounds/menu_menu.jpg",
        gm_root = "backgrounds/menu_quit.jpg",
        rounded_window = False,
    )

    style.window.background = Frame("boxes/dialogue_chatbox.png", 12, 12)
    style.window.left_margin = 0
    style.window.right_margin = 0
    style.window.top_margin = 0
    style.window.bottom_margin = 0
    style.window.left_padding = 80
    style.window.right_padding = 80
    style.window.top_padding = 20
    style.window.bottom_padding = 20
    style.window.yminimum = 122
    style.default.size = 15
    style.default.drop_shadow = [(1, 1)]

    style.rapbattle = Style(style.button)
    style.rapbattle_text = Style(style.text)
    style.button["rapbattle"].idle_background = "buttons/rap_ui_button01.png"
    style.button["rapbattle"].hover_background = "buttons/rap_ui_button01b.png"
    style.button["rapbattle"].xsize = 277
    style.button["rapbattle"].ysize = 69

    style.text["rapbattle_text"].background = Frame("buttons/rap_ui_button01.png", 277,79)
    style.text["rapbattle_text"].size = 22
    style.text["rapbattle_text"].color = ("#ffffff")
    style.text["rapbattle_text"].pos = (50,23)

    style.time_bar.left_bar = "buttons/bar_full.png"
    style.time_bar.right_bar = "buttons/bar_empty.png"

    style.menu_choice_button.background = Frame("buttons/dialogue_choice1.png",28,9)
    style.menu_choice_button.hover_background = Frame(HoverImage("buttons/dialogue_choice1.png"),28,9)
    style.menu_choice_button.yminimum = 30
    style.menu_choice_button.xminimum = 500
    style.menu_choice.color = "#ffffff"
    style.menu_choice.size = 16
    style.menu_choice.drop_shadow = [(1, 1)]

init -2:
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

    style mm_button:
        size_group "mm"

    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text

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

    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"

style default:
    font "fonts/DejaVuSans.ttf"
    size 14
    antialias True

style style_earnings:
    size 35

style style_instructions:
    size 20
    bold True
    antialias True

style style_instructions_small:
    size 12
    bold True
    antialias True

style style_shooting_score:
    size 60
    bold True
    antialias True
    color "#bebebe"

style style_cellphone_hints:
    size 12
    bold True
    antialias True
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    color "#f7f1ed"

style style_cellphone_message:
    size 14
    antialias True
    color "#6c6e70"

style style_cellphone_message_texting:
    size 16
    antialias True
    color "#000"

style style_cellphone_message_content:
    size 18
    antialias True
    color "#000"

style style_cellphone_title:
    size 20
    font "fonts/Arial.ttf"
    antialias True
    bold True
    outlines [ (absolute(4), "#fefefe", absolute(0), absolute(0)), (absolute(2), "#000", absolute(0), absolute(0)) ]
    color "#fefefe"

style style_cellphone_achievements_header:
    size 18
    antialias True
    bold True
    color "#000"

style style_cellphone_achievements_subheader:
    size 15
    antialias True
    bold True
    color "#000"

style style_cellphone_achievements:
    size 12
    antialias True
    color "#010101"

style style_cutscene:
    size 16
    antialias True
    color "#fefefe"
    text_align 0.5

style style_textbutton_debug:
    size 14
    antialias True

style style_machine_info_debug:
    size 18
    antialias True
    bold True
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

style style_pregnancy_percentage:
    font "fonts/ArialBlack.ttf"
    size 40
    antialias True
    bold True
    color "#692560"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
