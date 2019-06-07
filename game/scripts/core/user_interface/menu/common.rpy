screen common_menu():
    style_prefix 'common_menu'

    frame:
        style 'common_menu_outer_frame'
        transclude

    if main_menu:
        key 'game_menu' action Show('main_menu')


style common_menu_outer_frame is empty:

    background 'menu_background'
    padding (30, 30)
    xfill True
    yfill True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
