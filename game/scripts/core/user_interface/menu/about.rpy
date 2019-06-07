screen about() tag menu:


    use common_menu():
        style_prefix 'about'

        textbutton _('Back') action Return()

        vbox:
            add im.FactorScale('backgrounds/menu_logo.png', .75):
                xalign .5
                yoffset 50

            text _("v[config.version]") style_suffix 'version_text'

            null height 30

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
            text _("Various fonts are also used under license, including both proprietary and the {a=http://scripts.sil.org/OFL}SIL Open Font License{/a}. Details can be found in the game/legal directory of the game files.")


style about_button is menu_button:

    align (0., 1.)

style about_button_text is menu_button_text


style about_text:
    color '9098a3'

style about_vbox:
    anchor (.5, 1.)
    pos (.5, .85)
    spacing 10
    xsize 750

style about_version_text:
    xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
