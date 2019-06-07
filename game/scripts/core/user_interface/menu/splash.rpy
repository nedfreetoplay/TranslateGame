screen splash() tag menu:


    use common_menu():
        style_prefix 'splash'

        add 'backgrounds/menu_logo.png':
            align .5, -.35

        frame:
            has side 'c r':
                style_prefix 'age_check'

            frame:
                style_prefix 'rating'

                has vbox

                frame:
                    style_prefix 'rating_limit'
                    text '1{k=4}8{/k}+'

                text _('MATURE CONTENT')

            fixed:
                label _('I am 18 years of age or older.')

                hbox:
                    textbutton 'Yes' action Return()
                    textbutton 'No' action Quit(confirm=False)

        vbox:
            text _('All characters represented are fictitious and 18+ years of age.')
            text _('© 2016-2019 Summertime Saga. All rights reserved.')


style age_check_button is menu_button:

    xysize (120, 48)

style age_check_button_text is menu_button_text


style age_check_fixed:
    xsize 300

style age_check_hbox:
    align (.5, .9375)
    spacing 20

style age_check_label:
    align (.5, .15)

style rating_frame:
    background '#fff'
    padding (1, 1)

style rating_limit_frame:
    background '#871618'
    xysize (80, 70)

style rating_limit_text:
    align (.5, .5)
    font 'fonts/Arial.ttf'
    outlines ((1, 'fff', 0, 0),)
    size 40

style rating_text:
    color '000'
    font 'fonts/NotoSansJP-Regular.otf'
    outlines ((1, '00000033', 0, 0),)
    size 7
    xalign .5

style rating_vbox:
    spacing 1

style splash_frame:
    align (.5, .925)
    background 'menu_frame_fade'
    padding (4, 4)

style splash_text:
    color '515151'
    xalign .5

style splash_vbox:
    align (.5, 1.)
    spacing 5
    yanchor .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
