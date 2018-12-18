label hospital_jizz_checkup:
    scene hospital_desk
    show roz 1 at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 13f at right
    show diane b_casual a_casual_sides f_normal_talk at Position (xpos=400)
    with dissolve
    dia "H-hello."
    show diane f_normal
    show roz 2
    roz "Yeah?"
    show roz 1
    show diane f_normal_talk
    dia "I have an appointment for a check up."
    show diane f_normal
    show roz 11b at Position (xoffset=-40) with dissolve
    roz "Hmm."
    pause
    show roz 2 with dissolve
    roz "{b}Diane{/b}?"
    show roz 1
    show diane f_normal_talk
    dia "That's right."
    show diane f_normal
    show roz 2
    roz "Go on up to the second floor exam room and change into a gown."
    roz "The nurse will be up to see you momentarily."
    show roz 1
    show diane f_normal_talk
    dia "O-okay."
    show diane at flip
    show diane at Position (xpos=850)
    with dissolve
    dia "C'mon, {b}[firstname]{/b}."
    hide player
    hide diane
    with dissolve
    return

label hospital_diane_seen_in_labor:
    scene expression "backgrounds/location_hospital_bed.jpg"
    show diane a_gown_bed_baby b_gown_bed f_gurney_normal_talk at Position (xpos=578,ypos=850)
    show player 5 at left
    with dissolve
    dia "There he is!"
    show diane f_gurney_normal
    pause
    show diane f_gurney_teasing_look
    dia "There's your daddy!"
    show diane f_gurney_down_front
    show player 3 with dissolve
    player_name "{b}*Gulp*{/b}"
    show diane f_gurney_normal_talk
    dia "Come on, handsome."
    if M_diane.pregnancy.baby_gender == "boy":
        dia "I want you to meet {b}your new son{/b}."
        show diane f_gurney_down_front
        show player 10 with dissolve
        player_name "{b}M-my son{/b}?"
    else:
        dia "I want you to meet {b}your new daughter{/b}."
        show diane f_gurney_down_front
        show player 10 with dissolve
        player_name "{b}M-my daughter{/b}?"
    show player 13
    dia "Mmhmmm."
    show player 426 at center with dissolve
    pause
    show player 14
    player_name "Wow..."
    if M_diane.pregnancy.baby_gender == "boy":
        player_name "... He's so cute!"
    else:
        player_name "... She's so beautiful!"
    show player 426
    show diane f_gurney_laugh
    dia "Hehe, yup."
    if M_diane.pregnancy.baby_gender == "boy":
        dia "Just like his daddy."
        show diane f_gurney_cheese
        if M_diane.pregnancy.number_of_babies == 1:
            show player 17
            player_name "I can't believe I actually have a son!"
    else:
        dia "Just like his mommy."
        show diane f_gurney_cheese
        if M_diane.pregnancy.number_of_babies == 1:
            show player 17
            player_name "I can't believe I actually have a daughter!"
    if M_diane.pregnancy.number_of_babies == 1:
        show player 18
        show diane f_gurney_teasing_look
        dia "I know, me neither."
        show player 426
        dia "I never thought I'd have a child..."
    show diane f_gurney_down_front
    pause
    show player 14
    player_name "So when are you two coming home?"
    show player 13
    show diane f_gurney_normal_talk
    dia "Oh, they wanna keep us here for couple more days."
    dia "We'll be home soon though."
    show diane f_gurney_normal
    pause
    show diane f_gurney_normal_talk
    dia "Make sure my garden doesn't wilt away!"
    show diane f_gurney_normal
    show player 14
    player_name "Don't worry, I'll take care of everything."
    show player 13
    show diane f_gurney_normal_talk
    dia "Thanks, {b}[firstname]{/b}."
    show diane f_gurney_laugh
    dia "Say bye to Daddy!"
    show diane f_gurney_cheese
    pause
    show player 429
    show diane f_gurney_normal
    player_name "I'll see you soon, little one."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
