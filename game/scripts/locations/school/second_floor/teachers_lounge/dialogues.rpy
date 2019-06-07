label teachers_lounge_first_visit:
    scene expression game.timer.image("backgrounds/location_school_lounge{}_blur.jpg") with fade
    show player 14 with dissolve
    player_name "This must be the teachers lounge."
    player_name "Their private little getaway from my classmates."
    hide player with dissolve
    return

label teachers_lounge_okita_dose_smith:
    scene location_school_lounge_day_blur
    show player 11
    player_name "( There she is! Drinking coffee just like I thought. )"
    player_name "( I just need to dose the coffee pot! )"
    return

label coffee_pot_dialogue_wrong_time:
    scene location_school_lounge_day_blur
    show player 11
    player_name "( I can't do it while she's sitting there... )"
    return

label coffee_pot_dialogue_right_time:
    scene expression "backgrounds/location_school_lounge_cutscene01.jpg"
    with fade
    show text "This seemed like the best course of action." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I knew {b}Principal Smith{/b} drank coffee from this pot every afternoon." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "And since it was synthesized using her DNA, it shouldn't affect anybody else." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "At least, that's what I hoped." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    return

label coffee_pot_dialogue:
    if M_okita.is_state(S_okita_dose_smith):
        if game.timer.is_afternoon():
            call expression game.dialog_select("coffee_pot_dialogue_wrong_time")

        elif game.timer.is_morning():
            call expression game.dialog_select("coffee_pot_dialogue_right_time")
            $ M_okita.trigger(T_okita_dosed_smith)
    $ player.go_to(L_school_teacherslounge)
    $ game.main()

label smith_lounge_dialogue:
    scene expression game.timer.image("backgrounds/location_school_lounge_day{}_blur.jpg")
    show player 22 at left
    show principal 33 at right
    with dissolve
    player_name "( Oh crap! Principal Smith is in here! )"
    show player 11
    show principal 31 with dissolve
    player_name "( ... )"
    show principal 32
    smi "{b}[firstname]{/b}?"
    smi "What in the world are you doing in the teacher's lounge?!"
    show player 10
    show principal 31
    player_name "I was just-"
    show player 11
    show principal 32
    smi "Students are not allowed to be in here!"
    smi "Get back to your class immediately or I'll have you expelled!"
    show player 10
    show principal 31
    player_name "Y-yes, Ma'am!"
    $ player.go_to(L_school_floor2)
    $ game.main()

label microwave_dialogue:
    scene expression game.timer.image("backgrounds/location_school_lounge_microwave{}.jpg")
    player_name "An apple?!" with hpunch
    player_name "Why would anyone cook apples in microwaves..."
    $ A_apple.unlock()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
