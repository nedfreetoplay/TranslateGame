screen popup_generic():
    style_prefix 'popup'
    frame:
        transclude
    imagebutton idle Fixed() action Hide('popup')


style popup_frame:
    align (.5, .5)
    background 'menu_frame'
    padding (30, 30)
    xmaximum 500
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
