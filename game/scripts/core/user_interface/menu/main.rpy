screen main_menu() tag menu:


    for event in ('show', 'replace'):
        on event action Play('music', 'audio/music_title01.ogg',
                             fadein=.7, fadeout=.7, if_changed=True)

    use fancy_menu():
        style_prefix 'main'

        use core_menu

        textbutton _('[config.version] changelog') action ShowMenu('changelog')

        python:
            try:
                menu_tip = GetTooltip()
                menu_focus = renpy.display.focus.get_focused().child.text[0]
            except:
                menu_tip = menu_focus = None

        if menu_tip and menu_focus:
            vbox:
                style_prefix 'tooltip'
                add 'buttons/menu_tooltip_divider.png'
                null height 5
                text '{b}[menu_focus]{/b}'
                text menu_tip
                null height 15

        if renpy.variant('mobile') and not persistent.seen_swiftkey_hint:
            button:
                style_prefix 'hint'
                action SetField(persistent, 'seen_swiftkey_hint', True)
                text _('For an optimal experience,\nplease install the SwiftKey keyboard.')


style main_button:
    anchor (1., 0.)
    pos (.9, .83)

style main_core:
    anchor (.5, .5)
    pos (818, 410)

style tooltip_text:
    color '8b94aa'
    xpos .05

style tooltip_vbox:
    align (0., 1.)
    spacing 10
    ysize .2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
