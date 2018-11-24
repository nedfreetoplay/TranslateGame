label smith_bedroom_sneaking:
    scene expression "backgrounds/location_smith_bedroom_night_blur.jpg"
    show player 14 with dissolve
    player_name "Phew, I guess nobody is home."
    show player 10
    player_name "{b}I should definitely look around in here.{/b}"
    show player 35b
    pause
    show player 35
    player_name "Is that a goat’s head above the bed?"
    player_name "It feels like the eyes follow me no matter where I go..."
    show player 35b
    player_name "..."
    show player 10
    player_name "The creepyness level just went up one hundred and ten percent!"
    player_name "I should {b}find that exam and bounce outta here{/b}."
    player_name "This room looks like the best bet for where she would keep them."
    hide player with dissolve
    return

label smith_painting:
    if not player.has_item("smith_painting_key") and game.timer.is_dark():
        call expression game.dialog_select("smith_painting_dialogue")
        $ player.get_item("smith_painting_key")
    $ game.main()

label smith_painting_dialogue:
    scene expression "backgrounds/location_smith_bedroom_frame.jpg"
    show expression "objects/object_key_04.png" at Position (xoffset=-245,yoffset=-320)
    player_name "Hmm, this key looks useful"
    player_name "{b}I should search this room for a place to use it.{/b}"
    return

label smith_exams:
    call expression game.dialog_select("smith_exams_dialogue")
    $ player.get_item("smith_exams")
    $ player.remove_item("smith_painting_key")
    $ game.main()

label smith_exams_dialogue:
    scene expression "backgrounds/location_smith_bedroom_night_blur.jpg"
    show player 14 with dissolve
    player_name "This is them!"
    player_name "I can't believe {b}Missy{/b} and {b}Becca{/b} were right!"
    show player 13
    "Creak..."
    show player 10
    player_name "... What the hell was that?!"
    show player 23
    player_name "Somebody is here!" with hpunch
    player_name "{b}Principal Smith{/b}! I have to get out of here!"
    player_name "... Crap! Where do I go now?!"
    hide player with dissolve
    return

label smith_window_exit_dialogue:
    if M_roxxy.is_state(S_roxxy_sneak_into_smith) and player.has_item("smith_exams"):
        call expression game.dialog_select("smith_window_exit_roxxy_sneak_into_smith")
        $ game.sleep_lock = False
        $ player.go_to(L_map)
        $ M_roxxy.trigger(T_roxxy_escaped_smith)
        $ game.main()
    jump expression game.dialog_select("smiths_frontyard_dialogue")

label smith_window_exit_roxxy_sneak_into_smith:
    scene expression "backgrounds/location_smith_frontyard_cutscene01.jpg"
    with fade
    show text "As I heard someone coming down the hallway towards the bedroom…\n... I flung the window open and leaped out onto the roof below!\nThe thought of getting caught in {b}Principal Smith{/b}’s bedroom still gives me nightmares to this day!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene expression "backgrounds/location_smith_frontyard_night_blur.jpg"
    show player 10
    player_name "Phew! That was too close!"
    player_name "I'll bring these exams to {b}Roxxy{/b} at school tomorrow!"
    player_name "For now I should head home and get some rest."
    show player 24
    pause
    show player 25
    player_name "... And change my shorts!"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
