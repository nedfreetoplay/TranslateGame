screen game_menu() tag menu:


    use common_menu():
        style_prefix 'game_menu'

        vbox:
            textbutton _('Back') action Return()
            use core_menu


style game_menu_core is menu_frame:

    align (.5, .5)
    top_margin 10

style game_menu_vbox:
    align (.5, .5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
