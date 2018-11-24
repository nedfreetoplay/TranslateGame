label elevator_dialogue:
    $ player.go_to(L_hospital_elevator)
    if M_priya.is_state(S_priya_roz_camera_check):
        call expression game.dialog_select("elevator_priya_check_pregnax")
        $ player.go_to(L_hospital_floor3)
        $ M_priya.trigger(T_priya_helped_roz_with_camera)
        $ game.main()
    $ player.location.call_screen(False)

label elevator_priya_check_pregnax:
    scene expression "backgrounds/location_hospital_elevator_interior.jpg"
    show roz 21 at left
    show player 13f at right
    with dissolve
    roz "Here you go."
    show roz 20
    pause
    show roz 7
    show player 696 at Position (xoffset=-9)
    with dissolve
    roz "It's supposed to take a picture when I press the button but nothing happens."
    roz "Stupid thing is broken!"
    show roz 6
    show player 700 at Position (xoffset=-2) with dissolve
    player_name "Hmm."
    player_name "Oh, here we go!"
    show player 701 at Position (xoffset=-36) with dissolve
    pause
    show player 700 at Position (xoffset=-2) with dissolve
    player_name "You just need to open up the flashbar here to turn the camera on."
    player_name "I think that should-"
    show player 702
    player_name "!!!" with flash
    show player 703 at Position (xoffset=-36) with dissolve
    player_name "Ack!"
    player_name "Yeah, it's definitely working now..."
    pause
    show roz 23 with vpunch
    show player 10f with dissolve
    player_name "Whoa, did you just stop the elevator?"
    show player 5f
    show roz 7 with dissolve
    roz "I'm just making sure we won't be disturbed."
    show roz 6
    show player 12f
    player_name "Huh?"
    player_name "Why would-"
    show roz 10 with dissolve
    pause
    show roz 8
    show player 6f
    player_name "!!!" with hpunch
    player_name "Agh, what are you doing?!?!"
    show roz 9
    roz "Gettin' ready for my close up."
    show roz 8
    player_name "Yeah, I don't know what that means..."
    show roz 9
    roz "Well, now that you got it workin' I want you to snap a few photos of me."
    roz "For the fellas down at the home."
    show roz 8
    show player 113f with dissolve
    player_name "Why me?!"
    show player 114f
    show roz 9
    roz "You wanna go to the third floor don'tcha, kiddo?"
    show roz 8
    show player 113f
    player_name "Y-yeah..."
    show player 114f
    show roz 9
    roz "Well then, I suggest you quit yappin' and start snappin'."
    show roz 8
    show player 24f
    player_name "..."
    show roz 9
    roz "You gotta scratch my back if you want me to scratch yours."
    show roz 8
    show player 37f with dissolve
    player_name "Ugh, damnit."
    show player 24f with dissolve
    show roz 9
    roz "Make sure you get my good side!"

    if is_halloween():
        scene expression "backgrounds/location_hospital_cutscene01_halloween.jpg"
    else:
        scene expression "backgrounds/location_hospital_cutscene01.jpg"
    show expression FilteredText("... And here I thought this was going to be easy.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("How am I constantly getting myself into these situations?!") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show expression FilteredText("These pills had better be worth it.") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    scene expression "backgrounds/location_hospital_elevator_interior.jpg"
    show roz 22 at left
    show player 24f at right
    with dissolve
    roz "Oh, yeah!"
    roz "This is gonna drive the fellas wild!"
    show roz 20 with dissolve
    show player 10f
    player_name "Are we done?"
    show player 5f
    roz "Hmm?"
    show player 10f
    player_name "I really need to speak with {b}Doctor Singh{/b}."
    show player 5f
    show roz 23 with dissolve
    roz "Oh, right."
    show roz 7
    roz "Sheesh, you kids these days have no patience!" with vpunch
    show roz 6
    player_name "..."
    show roz 7
    roz "... And don't go tellin' nobody it was me who brought you up here!"
    show roz 6
    show player 10f
    player_name "Uh huh. I won't tell a soul about any... of this."
    show player 5f
    show roz 7
    roz "Good."
    roz "Now scram!"
    hide player with dissolve
    scene expression "backgrounds/location_hospital_third_blur.jpg"
    show player 24 with dissolve
    player_name "( Ugh, what a day! )"
    player_name "( At least it got me up to the {b}third floor{/b}. )"
    player_name "( I should {b}take a look around{/b} and see if I can find this {b}Doctor Singh{/b} guy. )"
    player_name "( Maybe I can find some bleach for my eyes, while I'm at it... )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
