style menu_button:
    align (.5, .5)
    hover_background 'menu_btn_over'
    idle_background 'menu_btn_idle'
    insensitive_background 'menu_btn_noop'
    padding (23, 10, 20, 15)
    selected_background 'menu_btn_live'
    selected_hover_background 'menu_btn_over'
    xysize (200, 55)

style menu_button_text:
    align (.5, .5)
    color 'eee'
    hover_color 'fff'
    insensitive_color '999'
    selected_bold True
    size 18

style menu_frame is default:

    background 'menu_frame'
    padding (60, 25)

style menu_vbox:
    spacing 14

style text_input_frame:
    background '#000'
    padding (10, 10)
    xfill True

style text_input_input:
    color '5d9aff'
    size 18

style warn_button is menu_button:

    hover_background 'warn_btn_over'
    idle_background 'warn_btn_idle'
    insensitive_background 'warn_btn_noop'
    selected_background 'warn_btn_live'
    selected_hover_background 'warn_btn_over'

style warn_button_text is menu_button_text
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
