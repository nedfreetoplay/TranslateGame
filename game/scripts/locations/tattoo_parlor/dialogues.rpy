label tattooparlor_first_visit:
    scene tattoo_indoor_b
    show player 13 with dissolve
    player_name "( I've never been in a tattoo shop before. )"
    show player 34
    player_name "( Maybe I should get a tattoo one day... )"
    hide player with dissolve
    return

label tattooparlor_mia_get_tattoo:
    scene tattoo_indoor_b
    show mia 7f at Position (xpos=400)
    show player 13 at left
    show grace f_normal_talk at right
    with dissolve
    grace "Hey guys!"
    show grace f_normal
    show player 14
    player_name "Hey."
    show player 13
    show mia 10f
    mia "Hi!"
    show mia 7f
    show grace f_laugh
    grace "Welcome to {b}Sugar Tats{/b}."
    show grace f_normal_talk
    grace "Have a look around the shop for cool tats..."
    grace "...And come see me if you have any questions!"
    hide grace with dissolve
    pause(.25)
    hide mia
    show mia 12 at right
    with dissolve
    mia "She seems busy, maybe we should come back another time?"
    show mia 8
    show player 12
    player_name "Oh, come on."
    show player 10
    player_name "You're going to stop now?!"
    show player 5
    show mia 12
    mia "*Sigh*"
    mia "You're right."
    mia "I said I would, so let's do it!"
    hide mia with dissolve
    show player 17
    player_name "That's the spirit!"
    hide player with dissolve
    return

label tattoo_pick_up_boxes:
    scene location_tattoo_indoor_closeup
    show xtra 26 at Position(xpos=0.65, ypos=1.0)
    if M_ross.get("failed pick up boxes"):
        call expression game.dialog_select("tattoo_boxes_try_again")
    else:

        call expression game.dialog_select("tattoo_boxes_intro")

    if player.has_required_str(6):
        call expression game.dialog_select("tattoo_boxes_str_pass")
        $ player.get_item("paint")
    else:

        call expression game.dialog_select("tattoo_boxes_str_fail")
        $ M_ross.set("failed pick up boxes", True)
    $ game.main()

label tattoo_boxes_try_again:
    show grace f_normal_talk at flip
    show player 1f at Position(xpos=0.5, ypos=1.0)
    with dissolve
    grace "Ready to move these boxes for me?"
    show grace f_normal
    show player 2f
    player_name "Yup, I'm doing it now."
    return

label tattoo_boxes_intro:
    show grace f_normal_talk at flip
    show player 1f at Position(xpos=0.5, ypos=1.0)
    with dissolve
    grace "Yup, that's the ones."
    grace "Just move them to the back for me and the paint is yours."
    show grace f_normal
    show player 2f
    player_name "Not a problem!"
    return

label tattoo_boxes_str_pass:
    show player 580 at Position(xpos=0.65, ypos=1.0) with dissolve
    pause
    player_name "..."
    show player 581f at Position(xpos=0.5, ypos=1.0) with dissolve
    player_name "Where do you want them again?"
    show player 580f
    show grace f_normal_talk at flip
    grace "The back room, if you don't mind."
    show player 581 at Position(xpos=0.65, ypos=1.0) with dissolve
    show grace f_normal
    player_name "No problem."
    show player 580 at Position(xpos=0.75, ypos=1.0) with dissolve
    show grace f_normal_talk
    grace "Thanks, {b}[firstname]{/b}!"
    scene location_tattoo_cutscene02
    with fade
    show text "... Who knew that tattoo equipment could be so heavy?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I understand now why {b}Eve{/b} didn't want to move these." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene location_tattoo_indoor_closeup
    show xtra 26 at Position(xpos=0.65, ypos=1.0)
    show player 10 at Position(xpos=0.55, ypos=1.0)
    with dissolve
    player_name "Phew!"
    player_name "That was a lot of boxes!"
    show player 1
    pause
    show grace f_normal_talk a_dressed_paint at flip with dissolve
    grace "All done?"
    show player 2f with dissolve
    show grace f_normal
    player_name "Yup. They're all stacked up in the back where you showed me."
    show player 1f
    show grace f_normal_talk
    grace "Awesome job, {b}[firstname]{/b}!"
    grace "Sheesh... Sweet, handsome, and strong!"
    grace "{b}Eve{/b} really hit the jackpot with you!"
    show grace f_normal
    show player 21f
    player_name "Whaaat?"
    player_name "I'm not... I mean, we aren't..."
    show grace f_normal_talk
    show player 1f
    grace "Here's that paint you wanted."
    grace "You should be able to mix everything you need with these."
    show grace f_normal a_dressed_hip
    show player 590f
    with dissolve
    player_name "Sweet! Thanks, {b}Grace{/b}!"
    show player 589f
    show grace f_laugh
    grace "My pleasure, stud!"
    show grace f_normal
    pause
    show grace f_normal_talk
    grace "Just promise me you'll take good care of {b}Eve{/b}."
    show grace f_laugh
    show player 589bf
    grace "It would be a real shame if I had to whoop that cute butt of yours..."
    show grace f_normal
    show player 590bf
    player_name "Heh, seriously... We aren't..."
    show player 589bf
    show grace f_laugh
    grace "Welp, I hope I see you again real soon, {b}[firstname]{/b}!"
    hide grace
    with dissolve
    pause
    show player 590bf
    player_name "... Together."
    show player 589bf
    pause
    show player 590bf
    player_name "... Okay."
    show player 590f
    player_name "I should get this paint back to {b}Miss Ross{/b} in the {b}art class{/b}."
    return

label tattoo_boxes_str_fail:
    show player 581b at Position(xpos=0.55, ypos=1.0) with dissolve
    player_name "[str_warn]HNNGGG!"
    player_name "[str_warn]..."
    show player 10f with dissolve
    player_name "[str_warn]What heck is in these boxes? Anvils?!"
    show player 11f
    show grace f_normal_talk at flip
    grace "[str_warn]... Too heavy?"
    show player 10f
    show grace f_normal
    player_name "[str_warn]Err, N-no..."
    show player 11f
    pause
    show player 10f
    player_name "[str_warn]... I'm just wearing the wrong shoes for this..."
    player_name "[str_warn]... Yeah, that's it!"
    show player 2f
    player_name "[str_warn]I'll be back later with the right shoes."
    show player 1f
    show grace f_laugh
    grace "[str_warn]Heh, okay."
    show grace f_normal_talk
    grace "[str_warn]... Just don't take too long."
    hide grace
    show player 35 with dissolve
    player_name "[str_warn]Hmm, I'd better hit the gym and get my strength up before coming back."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
