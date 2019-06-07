screen changelog() tag menu:


    default scroll = ui.adjustment()
    default version = changelog.keys[0]

    use common_menu():
        style_prefix 'changelog'

        textbutton _('Back') action Return()

        vbox:

            label _('[config.name] Changelog')

            hbox:
                style_prefix 'versions'
                for v in changelog.keys:
                    textbutton v action (SetScreenVariable('version', v),
                                         Function(scroll.change , 0))

            side 'c r b':
                viewport id 'changelog':
                    draggable True
                    mousewheel True
                    yadjustment scroll

                    text changelog.notes[version].strip():
                        substitute False

                vbar value YScrollValue('changelog')
                null height 70


style changelog_button is menu_button:

    align (0., 1.)
    yanchor .925

style changelog_button_text is menu_button_text


style changelog_label_text:
    color '9098a3'
    size 18

style changelog_side:
    spacing 10

style changelog_text:
    color 'ccc'
    line_spacing 4

style changelog_vbox:
    spacing 30

style changelog_vscrollbar:
    base_bar 'menu_bar_empty'
    thumb 'menu_bar_thumb'
    unscrollable 'hide'
    xsize 15

style versions_button_text:
    selected_color '4091fc'

style versions_hbox:
    box_wrap True
    spacing 30
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
