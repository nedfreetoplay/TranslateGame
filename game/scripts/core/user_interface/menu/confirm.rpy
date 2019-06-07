screen confirm(message, yes_action, no_action, background=None, yes_text=_('Yes'), no_text=_('No')):

    modal True

    use common_menu():
        style_prefix 'confirm'

        vbox:

            fixed:
                if message == gui.QUIT:
                    text _('You\'ve spent [playtime] eating cookies...')

                python:
                    bgmap = {gui.DELETE_SAVE: 'menu_trash',
                         gui.OVERWRITE_SAVE: 'menu_trash'}
                    background = bgmap.get(message, background or 'menu_tissue')

                add background xalign .5 ypos .8

            label message

            hbox:
                textbutton yes_text action yes_action selected False
                textbutton no_text action no_action selected False:
                    keysym 'game_menu'

            vbox:
                style_prefix 'support'

                add 'backgrounds/menu_patreon.png' xalign .5

                text _('To support the continued development of this game you can go to:')
                text '{a=http://www.patreon.com/summertimesaga}http://www.patreon.com/summertimesaga{/a}'
                text _('Thank you!')


style confirm_button is menu_button


style confirm_button_text is menu_button_text


style confirm_fixed:
    ysize 310

style confirm_hbox:
    spacing 50
    xalign .5

style confirm_label:
    xalign .5

style confirm_label_text:
    bold True
    text_align .5

style confirm_text:
    align (.5, .15)
    text_align .5

style confirm_vbox:
    align (.5, .5)
    spacing 30

style support_text:
    color '515151'
    xalign .5

style support_vbox:
    spacing 10
    xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
