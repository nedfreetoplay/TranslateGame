label dewitt_dialogue_office_dewitt_eve_meet_up:
    scene expression game.timer.image("dewitt_office_c{}")
    show player 10 with dissolve
    player_name "I should give her some space for the time being."
    player_name "And I should also visit {b}Eve{/b} in the {b}park at night{/b}."
    return

label dewitt_dialogue_office_dewitt_end_intro:
    scene expression game.timer.image("dewitt_office_c{}")
    show dewitt 18 at left
    show player 14f at right
    with dissolve
    player_name "Hey there, {b}Melody{/b}!"
    show player 13f
    show dewitt 19
    dewitt "Mmm, hey {b}[firstname]{/b}!"
    dewitt "I was hoping you'd come visit me tonight..."
    show dewitt 18
    show player 14f
    player_name "Heh, you in the mood for a bit of fun?"
    show player 13f
    show dewitt 19
    dewitt "I'm always in the mood for you, {b}[firstname]{/b}."
    dewitt "You wanna get right to it or should I dance for you first?"
    show dewitt 18
    return

label dewitt_dialogue_office_dewitt_end_dance:
    show dewitt 19
    dewitt "Have a seat then, sugar."
    scene expression game.timer.image("dewitt_office_sex{}"):
    $ M_dewitt.set("sex speed", 0.125)
    show dewitts 1
    show dewitt cloths 1b
    show player dewitts 1 zorder 2 at left
    with dissolve
    pause
    hide dewitts
    hide dewitt
    show expression AnimatedImage("dewitt_twerk", [1,2,3,4,5,6,7,8,9,10], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve
    dewitt "Mmm..."
    dewitt "You like that, Baby?"
    player_name "Oh yeah!"
    show player dewitts 1b with hpunch
    show player dewitts 1 with dissolve
    dewitt "Oh!"
    dewitt "I love it when you do that!"
    pause
    dewitt "I think I should lose some of these clothes!"
    dewitt "What do you think, sugar?"
    player_name "Y-yeah!"
    hide dewitts
    hide dewitt_twerk
    hide dewitt
    hide player
    with dissolve

    scene expression game.timer.image("dewitt_office_c{}")
    show dewitt 20 zorder 1 with dissolve
    pause
    show dewitt 31b with dissolve
    pause
    show dewitt 32b with dissolve
    pause
    show dewitt 29 with dissolve
    dewitt "Let's change up the music too!"
    show dewitt 35b at Position (xoffset=354) with dissolve
    pause

    show player 626 zorder 0 at Position (xpos=550) with dissolve
    pause
    show dewitt 36 at Position (xoffset=354)
    dewitt "And just what are you doing back there?"
    dewitt "Haven't you heard you're not supposed to touch the dancers?"
    show dewitt 35 at Position (xoffset=354)

    show player 629
    show player_hand 629b_629c zorder 2 at Position (xpos=550)
    with dissolve
    player_name "Whoops..."
    show player 628
    show dewitt 36 at Position (xoffset=354)
    dewitt "Naughty bo-"

    show player_hand 629d
    show dewitt 37 at Position (xoffset=290) with hpunch
    show player 626
    hide player_hand
    with dissolve
    dewitt "Hey there!"
    show dewitt 38 at Position (xoffset=290)
    show player 627
    with dissolve
    dewitt "Get back on that couch, naughty!"

    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_sex{}"):
    show dewitts 1
    show dewitt cloths 1c
    show player dewitts 1 zorder 2 at left
    with dissolve
    dewitt "Mmm, how's it looking now?"
    hide dewitts
    hide dewitt
    show expression AnimatedImage("dewitt_twerk", ["1c","2c","3c","4c","5c","6c","7c","8c","9c","10c"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve
    player_name "You're so sexy, {b}Melody{/b}!"
    dewitt "Heh, thanks, sugar!"
    pause
    show player dewitts 1b with hpunch
    show player dewitts 1 with dissolve
    dewitt "Mmm!"
    dewitt "You naughty boy!"
    dewitt "You're getting me so wet!"
    pause
    dewitt "You ready for the finale?"
    player_name "Yes, Ma'am!"
    dewitt "Hehe, watch closely..."
    scene black with fade
    pause 0.25
    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_sex{}"):
    show dewitts 1
    show player dewitts 1 zorder 2 at left
    with dissolve
    dewitt "Mmm, watch me work this pussy, Baby!"
    hide dewitts
    show expression AnimatedImage("dewitt_twerk", ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve
    pause
    show player dewitts 1b with hpunch
    show player dewitts 1 with dissolve
    dewitt "Fuck!"
    dewitt "I can't take it much longer, sugar!"
    dewitt "I need that big dick!"
    pause
    return


label dewitt_dialogue_office_dewitt_end_bj:
    show player 14f
    player_name "Would you be able to give me a BJ again?"
    show player 13f
    show dewitt 19 with dissolve
    dewitt "I'd love to!"
    dewitt "You know I've played a few flutes before."
    dewitt "But your skin flute is the best I've ever had the pleasure of wrapping my lips around."
    dewitt "But enough talk let me give you another private performance."
    scene black with fade

    $ M_dewitt.set("sex speed", 0.175)
    scene expression game.timer.image("dewitt_office_bj{}")
    show dewitt bj 1 at left
    with dissolve
    pause
    show dewitt bj 2
    pause
    show dewitt bj 3
    pause
    show dewitt bj 4
    pause
    hide dewitt
    show expression AnimatedImage("dewitts_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_dewitt) as dewitts_bj
    return

label dewitt_dialogue_office_dewitt_end_sex:
    show dewitt 19
    dewitt "I was hoping you wanted to jump right in!"
    dewitt "Let's see who can get out of their clothes the quickest!"
    show dewitt 20 with dissolve
    show player 26f
    player_name "What no count down?"
    show dewitt 31f with dissolve
    show player 8f with dissolve
    dewitt "Nope!"
    show dewitt 32f with dissolve
    show player 261 with dissolve
    pause
    show dewitt 18b with dissolve

    show player 263 with dissolve
    pause
    show dewitt 19b
    dewitt "Looks like I won!"
    dewitt "Now make me cum!"
    show player 262
    player_name "Yes, Ma'am!"
    label dewitt_twerk_end:
        scene black with fade
        pause 0.25
        scene expression game.timer.image("dewitt_office_sex{}"):
        show dewitts 1
        show player dewitts 2 zorder 2 at left
        with dissolve
        dewitt "Give it to me, {b}[firstname]{/b}!"
        hide player
        show dewitts 3 at left
        with dissolve
        dewitt "Stop playing back there! I can't wait!"
        show dewitts 4
        dewitt "Right here, sugar..."
        show dewitts 5 with dissolve
        pause
        $ M_dewitt.set("sex speed", 0.125)
        show expression AnimatedImage("dewitts", [5,6,7,8,9,10,11,12,13,14], M_dewitt) as dewitts
        $ anim_toggle = True
    jump expression game.dialog_select("dewitt_sex_loop")

label dewitt_dialogue_office_intro:
    scene expression game.timer.image("dewitt_office_c{}"):
    show dewitt 1b at left
    show player 14f at right
    with dissolve
    player_name "Hello, {b}Miss Dewitt{/b}."
    show player 13f
    show dewitt 2b
    dewitt "Hey there, {b}[firstname]{/b}!"
    dewitt "Did you need something?"
    show dewitt 1b
    return

label dewitt_dialogue_office_flute_lessons:
    show player 26f
    player_name "I was hoping you could help teach me how to master my flute."
    show player 13f
    show dewitt 19 with dissolve
    dewitt "I was hoping you were going ask!"
    dewitt "Meet me here tonight and we can play together!"
    hide player
    show dewitt 6 at right
    with dissolve
    dewitt "And don't be late or I'll just have to play solo."
    return

label dewitt_dialogue_office_leave:
    show player 14f
    player_name "Not at the moment."
    show player 13f
    show dewitt 2b
    dewitt "Alright. Well, have an awesome day!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
