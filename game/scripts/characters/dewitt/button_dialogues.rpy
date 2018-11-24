label dewitt_dialogue_dewitt_eve_meet_up:
    scene music_classroom_c
    show player 10 with dissolve
    player_name "I should give her some space for the time being."
    player_name "And I should also visit {b}Eve{/b} in the {b}park at night{/b}."
    return

label dewitt_dialogue_dewitt_science_adhesive:
    scene music_classroom_c
    show player 17 with dissolve
    player_name "{b}Kevin{/b} was going to make some adhesive in {b}Miss Okita's{/b} classroom."
    player_name "I should see what he's up to."
    return

label dewitt_dialogue_dewitt_school_sneak_mission_help:
    scene music_classroom_c
    show player 10 with dissolve
    player_name "Maybe {b}Erik{/b} will help me {b}sneak into the school tonight{/b}."
    return

label dewitt_dialogue_dewitt_office_night_visit_delay:
    scene music_classroom_c
    show player 13 at left
    show dewitt 19f at right
    with dissolve
    dewitt "Remember, I have one more surprise for you."
    hide player
    show dewitt 6f at left
    with dissolve
    dewitt "You'll have to come to my office {b}tomorrow{/b} after school if you want it..."
    show player 29 at left
    show dewitt 18f at Position (xpos=300)
    with dissolve
    player_name "O-okay..."
    player_name "I'll be there."
    show player 13 with dissolve
    show dewitt 19f
    dewitt "Mmm, I can't wait!"
    dewitt "See you then, {b}[firstname]{/b}."
    hide dewitt with dissolve
    show player 18
    player_name "..."
    return

label dewitt_dialogue_dewitt_office_night_visit:
    scene music_classroom_c
    show player 13 at left
    show dewitt 19f at right
    with dissolve
    dewitt "Remember, I have one more surprise for you."
    hide player
    show dewitt 6f at left
    with dissolve
    dewitt "You'll have to come to my office after school if you want it..."
    show player 29 at left
    show dewitt 18f at Position (xpos=300)
    with dissolve
    player_name "O-okay..."
    player_name "I'll be there."
    show player 13 with dissolve
    show dewitt 19f
    dewitt "Mmm, I can't wait!"
    dewitt "See you then, {b}[firstname]{/b}."
    hide dewitt with dissolve
    show player 18
    player_name "..."
    return

label dewitt_dialogue_dewitt_end:
    scene music_classroom_c
    show player 13f at right
    show dewitt 2 at left
    with dissolve
    dewitt "Thanks again for everything, sugar!"
    show dewitt 1
    show player 14f
    player_name "My pleasure, {b}Miss Dewitt{/b}."
    show player 13f
    show dewitt 19 with dissolve
    dewitt "Remember, my door is always open for you."
    show dewitt 18
    show player 17f
    player_name "Yes, Ma'am."
    return

label dewitt_dialogue_intro:
    scene music_classroom_c
    show dewitt 1 at left
    show player 2f at right
    player_name "Hi, {b}Miss Dewitt{/b}."
    show dewitt 2
    show player 1f
    dewitt "Hello, {b}[firstname]{/b}!"
    dewitt "Ready to groove with us today?"
    show dewitt 1
    show player 33f
    player_name "Of course!"
    show dewitt 2
    show player 13f
    dewitt "Is there anything you want to talk about?"
    show dewitt 1
    show player 34f
    return

label dewitt_dialogue_dewitt_find_flute:
    show player 10f
    player_name "Where should I start looking for the flute?"
    show player 5f
    show dewitt 2
    dewitt "Did you {b}check the instrument checkout sheet in the classroom locker{/b}?"
    show dewitt 1
    show player 14f
    player_name "Oh yeah!"
    player_name "I'll look there for a clue!"
    show player 13f
    show dewitt 2
    dewitt "Bye, sugar!"
    return

label dewitt_dialogue_dewitt_make_new_flute:
    show player 10f
    player_name "About the flute-"
    show player 11f
    show dewitt 2
    dewitt "Did you find the flute yet?"
    show dewitt 1
    show player 3f at Position (xoffset=-8) with dissolve
    player_name "..."
    show player 10f with dissolve
    player_name "Not yet."
    show player 5f
    show dewitt 2
    dewitt "I hope it's not lost."
    show dewitt 1
    show player 14f
    player_name "Don't worry! I'm on it!"
    show player 13f
    show dewitt 2
    dewitt "Thanks, {b}[firstname]{/b}!"
    hide dewitt with dissolve
    show player 4f with dissolve
    player_name "( {b}Erik{/b} said I should be able to make one. )"
    return

label dewitt_dialogue_talent_show_help:
    show player 10f
    player_name "How many people do you need for the talent show again?"
    show player 5f
    show dewitt 5
    dewitt "I was hoping for at least {b}two more{/b}."
    dewitt "Any less and I'm afraid we'll have to cancel."
    show dewitt 4
    show player 14f
    player_name "Alright, no worries, {b}Ms. Dewitt{/b}! I'll find someone!"
    show player 13f
    show dewitt 5
    dewitt "Aww thanks, sugar!"
    return

label dewitt_dialogue_leave:
    show player 10f
    player_name "Not really..."
    player_name "Just hoping I can catch up."
    show dewitt 2
    show player 5f
    dewitt "Oh, honey. You'll be just fiiine!"
    show player 13f
    dewitt "Pick an instrument and take a seat!"
    dewitt "We'll get you back in the groove..."
    show dewitt 1
    show player 14f
    player_name "Thanks, {b}Miss Dewitt{/b}..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
