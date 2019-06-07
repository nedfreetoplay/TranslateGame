screen preferences() tag menu:


    use common_menu():
        style_prefix 'settings'

        vbox:

            textbutton _('Back') action Return()

            hbox:
                vbox:
                    style_suffix 'column'
                    frame:
                        has vbox
                        label _('Display')
                        textbutton _('Window') action Preference('display', 'window')
                        textbutton _('Fullscreen') action Preference('display', 'fullscreen')
                    frame:
                        has vbox
                        label _('Text Speed')
                        bar value Preference("text speed")
                    frame:
                        has vbox
                        label _('Skip')
                        textbutton _('Unseen Text') action Preference('skip', 'toggle')
                        textbutton _('After Choices') action Preference('after choices', 'toggle')
                        textbutton _('Transitions') action InvertSelected(Preference('transitions', 'toggle'))

                vbox:
                    style_suffix 'column'
                    frame:
                        has vbox
                        label _('Music Volume')
                        bar value Preference("music volume")
                    frame:
                        has vbox
                        label _('Sound Volume')
                        bar value Preference("sound volume")
                    frame:
                        has vbox
                        label _('Internet')
                        textbutton _('Allow Access'):
                            action ToggleField(preferences, 'internet_access')
                            alt _('internet [text]')
                        text _('Used solely for fetching latest Patreon Rewards')
                    frame:
                        has vbox
                        label _('Other')
                        textbutton _('Clear Persistent'):
                            action Confirm(_('Are you sure you want to reset persistent data?'),
                                       
                                       
                                       

                                       ClearPersistent())
                            sensitive any(not k.startswith('_')
                                      for k in persistent.__dict__.keys())
                            style_suffix 'warn_button'


style settings_button is menu_button


style settings_button_text is menu_button_text


style settings_column:
    spacing -5

style settings_frame is menu_frame


style settings_hbox:
    spacing 30

style settings_label:
    align (.5, .5)
    bottom_padding 5

style settings_label_text:
    color '8b94aa'
    size 16

style settings_slider:
    left_bar 'menu_bar_full'
    right_bar 'menu_bar_empty'
    thumb 'menu_bar_thumb'
    xsize 200
    ysize 15

style settings_text:
    color '8b94aa'
    size 12
    text_align .5
    xalign .5
    xsize 200

style settings_vbox:
    align (.5, .5)
    spacing 10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
