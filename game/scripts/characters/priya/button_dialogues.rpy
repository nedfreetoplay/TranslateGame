label priya_button_intro:
    scene expression "backgrounds/location_hospital_lab_blur.jpg"
    show player 5 at left
    show priya f_angry a_dressed_point
    with dissolve
    priya "You again?!"
    priya "What are you doing here?!"
    show priya f_stern a_dressed_crossed with dissolve
    pause
    show priya f_angry
    priya "Do you have some results to report?"
    show priya f_stern
    return

label priya_button_menu_no:
    show priya f_stern a_dressed_crossed
    show player 24 at left
    player_name "No, sorry."
    player_name "I was just-"
    show player 5
    show priya f_angry a_dressed_point with dissolve
    priya "This is a restricted area for a reason!"
    priya "You can't just come and go as you please..."
    show priya f_stern a_dressed_crossed with dissolve
    show player 10
    player_name "I'm sorry, {b}Priya{/b}."
    show player 24
    player_name "I-"
    player_name "I'll go..."
    show player 5
    show priya f_facepalm_talk a_dressed_facepalm with dissolve
    priya "{b}*Sigh*{/b}"
    priya "No, I'm sorry... I'm sorry."
    show priya f_hopeful_talk a_dressed_sides with dissolve
    priya "I don't mean to yell at you."
    show priya f_normal_talk
    priya "It's just... It's dangerous for you to be up here."
    priya "So please, don't come back unless you have something to report."
    show priya f_normal
    show player 10
    player_name "O-okay."
    hide player
    hide priya
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
