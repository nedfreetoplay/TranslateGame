label coach_bridget_dialogue_office_intro:
    scene expression game.timer.image("coach_office{}_b")
    show player 11 at left
    show bridget f_angry_talk at right
    with dissolve
    bri "{b}[firstname]{/b}!"
    bri "What are you doing in here?"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Sorry, Ma'am!!!"
    player_name "I just had some questions!"
    show player 31
    show bridget f_angry_talk
    bri "Questions?!"
    bri "Like what?"
    show bridget a_dressed_crossed f_angry
    return

label coach_bridget_dialogue_courtyard_intro:
    scene expression game.timer.image("backgrounds/location_school_gym{}.jpg")
    show player 11 at left
    show bridget f_angry_talk at right
    with dissolve
    bri "{b}[firstname]{/b}!"
    bri "You better be training your ass off at the {b}Gym{/b}, or I'm going to shove my foot up your ass!!"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Yes, Ma'am!!!"
    show player 31
    show bridget f_angry_talk
    bri "Got any questions?!"
    show bridget a_dressed_crossed f_angry
    return

label coach_bridget_dialogue_training_advice:
    show player 10
    show bridget a_dressed_crossed f_normal
    player_name "I... Well, where should I train?"
    show bridget a_dressed_crossed f_angry
    show player 5
    bri "..."
    show player 22
    show bridget f_angry_talk
    bri "I just told you!"
    show bridget a_dressed_crossed f_angry_yell
    bri "At the {b}GYM{/b}!!!"
    show player 10
    show bridget a_dressed_crossed f_angry
    player_name "But... What should I train?"
    show player 11
    show bridget f_angry_talk
    bri "You have to work on your {b}strength{/b} and {b}dexterity{/b} if you want to make it!"
    bri "You'll be competing in the {b}110m hurdle{/b} race to qualify this {b}school{/b} and your team into the {b}state championship{/b}!"
    show player 10
    show bridget a_dressed_crossed f_angry
    player_name "That's... A lot of pressure."
    show player 23
    show bridget f_angry_talk
    bri "...And you better NOT fail me!"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Yes, Ma'am!!!"
    hide bridget
    hide player
    with dissolve
    return

label coach_bridget_dialogue_leave:
    show player 10
    show bridget a_dressed_crossed f_normal
    player_name "I... I forgot."
    show player 11
    show bridget f_angry_talk
    bri "Forgot? Boy you are the saddest piece of meat I've ever seen!"
    show player 22
    show bridget a_dressed_crossed f_angry_yell
    bri "Now get out of here and get to {b}WORK{/b}!!"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Yes, Ma'am!!!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
