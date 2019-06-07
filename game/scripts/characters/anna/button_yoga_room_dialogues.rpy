label anna_button_yoga_room_dialogue_pre:
    scene yoga_room_night
    show anna 2 at right
    show player 13 at left
    with dissolve
    anna "Hello, {b}[firstname]{/b}."
    show anna 1
    show player 14
    player_name "Hi, {b}Anna{/b}."
    show player 13
    show anna 2
    anna "What's up?"
    show anna 1
    return

label anna_button_yoga_room_dialogue_wheres_mrsj:
    show player 14
    player_name "I'm looking for {b}Mrs. Johnson{/b}."
    show player 30
    player_name "Do you know where I could find her?"
    show player 5
    show anna 2
    anna "She usually teaches during the day."
    anna "She must be home by now..."
    show anna 1
    show player 14
    player_name "Oh. I see. Thanks!"
    show player 13
    show anna 3
    anna "No problem!"
    return

label anna_button_yoga_room_dialogue_yoga:
    show player 10
    player_name "Do you want to practice some yoga poses with me?"
    show player 5
    show anna 3
    anna "Of course!!"
    show anna 2
    anna "I like when someone can help me reach those... hard postures..."
    show anna 1
    show player 33
    player_name "Right, you're quite flexible as I remember."
    show player 13
    show anna 2
    anna "Alright, let's find a yoga mat..."
    hide anna
    scene location_gym_yoga_front
    with fade
    show player 413 at left
    show anna 13
    with dissolve
    anna "Which position should we practice?"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
