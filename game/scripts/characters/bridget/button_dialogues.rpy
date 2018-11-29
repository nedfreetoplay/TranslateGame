label coach_bridget_dialogue_office_intro:
    scene expression game.timer.image("coach_office{}_b")
    show player 11 at left
    show coach 3 at right
    with dissolve
    bri "{b}[firstname]{/b}!"
    bri "What are you doing in here?"
    show player 32
    show coach 7
    player_name "Sorry, Ma'am!!!"
    player_name "I just had some questions!"
    show player 31
    show coach 3
    bri "Questions?!"
    bri "Like what?"
    show coach 7
    return

label coach_bridget_dialogue_courtyard_intro:
    scene expression game.timer.image("backgrounds/location_school_gym{}.jpg")
    show player 11 at left
    show coach 3 at right
    with dissolve
    bri "{b}[firstname]{/b}!"
    bri "You better be training your ass off at the {b}Gym{/b}, or I'm going to shove my foot up your ass!!"
    show player 32
    show coach 7
    player_name "Yes, Ma'am!!!"
    show player 31
    show coach 3
    bri "Got any questions?!"
    show coach 7
    return

label coach_bridget_dialogue_training_advice:
    show player 10
    show coach 1
    player_name "I... Well, where should I train?"
    show coach 7
    show player 5
    bri "..."
    show player 22
    show coach 3
    bri "I just told you!"
    show coach 4
    bri "At the {b}GYM{/b}!!!"
    show player 10
    show coach 7
    player_name "But... What should I train?"
    show player 11
    show coach 3
    bri "You have to work on your {b}strength{/b} and {b}dexterity{/b} if you want to make it!"
    bri "You'll be competing in the {b}110m hurdle{/b} race to qualify this {b}school{/b} and your team into the {b}state championship{/b}!"
    show player 10
    show coach 7
    player_name "That's... A lot of pressure."
    show player 23
    show coach 3
    bri "...And you better NOT fail me!"
    show player 32
    show coach 7
    player_name "Yes, Ma'am!!!"
    hide coach
    hide player
    with dissolve
    return

label coach_bridget_dialogue_leave:
    show player 10
    show coach 1
    player_name "I... I forgot."
    show player 11
    show coach 3
    bri "Forgot? Boy you are the saddest piece of meat I've ever seen!"
    show player 22
    show coach 4
    bri "Now get out of here and get to {b}WORK{/b}!!"
    show player 32
    show coach 7
    player_name "Yes, Ma'am!!!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
