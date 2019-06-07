screen core_menu():
    frame:
        style_suffix 'core'

        has vbox:

            style_prefix 'core_menu'

        if main_menu:
            textbutton _('New Game') action ShowMenu('name'):
                tooltip _('Start a new game from the beginning.')
            textbutton _('Load Game') action ShowMenu('load'):
                tooltip _('Continue playing from a previously saved game.')
        else:
            key 'game_menu' action Return()
            if _in_replay:
                textbutton _('End Replay') action EndReplay(confirm=True)
            else:
                textbutton _('Main Menu') action MainMenu()
            textbutton _('Save') action ShowMenu('save')
            textbutton _('Load') action ShowMenu('load')

        textbutton _('Settings') action ShowMenu('preferences'):
            tooltip _('Adjust the game options and preferences.')

        if main_menu:
            textbutton _('Cookie Jar') action ShowMenu('cookie_jar'):
                tooltip _('Select unlocked characters to replay their animated scenes!')

        textbutton _('Credits') action ShowMenu('credits'):
            tooltip _('List of contributors during the creation of [config.name!t].')
        textbutton _('Quit') action Quit(confirm=not main_menu):
            tooltip _('This will close the game ... but why would you do that?')


style core_menu:
    align (.5, .5)

style core_menu_vbox:
    spacing 14
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
