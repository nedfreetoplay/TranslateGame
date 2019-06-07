screen popup_warning():
    use popup_generic():
        style_prefix 'warn_popup'

        side 'l c':

            add 'boxes/popup_generic_warning.png'
            vbox:
                label _('WARNING!')
                transclude


style warn_popup_label_text:
    bold True
    size 20

style warn_popup_side:
    spacing 15

style warn_popup_vbox:
    spacing 10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
