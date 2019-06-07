screen credits() tag menu:


    default scroll = credits.adjustment()

    on 'replace' action Play('music', '<loop 241.5>audio/music_credits.ogg',
                             fadein=.7, fadeout=.7, if_changed=True)

    use common_menu():
        style_prefix 'credits'

        vbox:
            grid 2 1:
                style_prefix 'creator_credit'
                label _('Owner & Creator')
                text 'DarkCookie'

            null height 20

            grid 2 1:
                for column in credits.team:
                    grid 2 len(column):
                        style_prefix 'credit'
                        for name, role in column:
                            label role
                            text name

            null height 30

            label _('Special thanks to all our key pledging contributors!')

            null height 10

            side 'c b':
                fixed:
                    style_prefix 'pledge'
                    viewport:
                        draggable True
                        mousewheel True
                        edgescroll (20, 20, credits.sign)
                        yadjustment scroll
                        text credits.pledgers
                    if scroll.value > 0:
                        textbutton '\u25b2':
                            action Function(scroll.pgup)
                    if scroll.value < scroll.range:
                        textbutton '\u25bc':
                            action Function(scroll.pgdn)
                            yalign 1.


                side 'l r':
                    textbutton _('Back') action Return()
                    textbutton _('About') action ShowMenu('about')


style creator_credit_label_text:
    size 18

style creator_credit_text take creator_credit_label_text


style credit_grid:
    xalign .5
    xspacing 10
    yspacing 5

style credit_label:
    xalign 1.

style credit_label_text is credits_label_text


style credit_text:
    bold True
    color '4091fc'

style credits_button is menu_button


style credits_button_text is menu_button_text


style credits_grid:
    spacing 30
    xalign .5

style credits_label:
    xalign .5

style credits_label_text:
    color '9098a3'
    italic True

style credits_side:
    spacing 20
    xfill True

style pledge_button:
    hover_background '#54555c77'
    idle_background '#3b3d4577'
    xfill True
    ysize 20

style pledge_button_text:
    align (.5, .5)

style pledge_text:
    font credits.font
    language 'western'
    line_spacing 1
    text_align .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
