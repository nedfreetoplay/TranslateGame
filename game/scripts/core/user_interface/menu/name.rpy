screen name() tag menu:


    default name = persistent.firstname or 'Anon'

    use fancy_menu():
        style_prefix 'name'

        vbox:

            if main_menu:
                textbutton _('Back') action Return() keysym 'game_menu'
            else:
                textbutton _('Back') action MainMenu(False) keysym 'game_menu'

            frame:
                has vbox:

                    style_prefix 'name_prompt'

                label _('Choose a name for your character:')

                frame:
                    style_prefix 'text_input'
                    input:
                        allow ('abcdefghijklmnopqrstuvwxyz'
                           'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                           '0123456789 ')
                        length 12
                        value ScreenVariableInputValue('name')

            textbutton _('Start!'):
                action (SetField(persistent, 'firstname', name.strip()), 
                    ShowMenu('mode'))
                keysym 'input_enter'
                selected False
                sensitive name.strip()


style name_button is menu_button


style name_button_text is menu_button_text


style name_frame:
    background 'menu_frame_dark'
    bottom_margin 10
    padding (30, 40)
    xsize 283

style name_prompt_label:
    xalign .5

style name_prompt_label_text:
    size 18
    text_align .5

style name_prompt_vbox:
    spacing 20

style name_vbox:
    anchor (.5, .5)
    pos (818, 410)
    spacing 30
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
