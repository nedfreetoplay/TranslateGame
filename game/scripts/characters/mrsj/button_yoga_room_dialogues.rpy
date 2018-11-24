label mrsj_button_yoga_room_dialogue_pre_first:
    show player 1 at left
    show mrsj 10 at right
    with dissolve
    player_name "Umm-"
    show player 11 at left
    window hide
    pause
    player_name "..."
    show mrsj 11 at right
    window hide
    pause
    show mrsj 12 at right
    window hide
    pause
    show mrsj 13 at right with hpunch
    mrsjo "Oh!"
    show player 18 at left
    mrsjo "...{b}[firstname]{/b}?"
    show mrsj 14 at right
    show player 17 at left
    player_name "Hi, {b}Mrs. Johnson{/b}!"
    show mrsj 17 at right
    show player 1 at left
    mrsjo "What are you doing here?"
    show mrsj 14 at right
    show player 29 at left
    player_name "I... saw you from the main {b}Gym{/b}!"
    player_name "I just came to say hi!"
    show player 13 at left
    show mrsj 18 at right
    mrsjo "That's so sweet!"
    show mrsj 17 at right
    mrsjo "So you're working out now, huh?"
    show mrsj 14 at right
    show player 21 at left
    player_name "Haha. Yeah..."
    player_name "...Just started to train to get fit!"
    show mrsj 19 at right
    show player 11 at left
    mrsjo "And I bet you'll get nice and {b}hard{/b}-"
    mrsjo "..."
    show player 13 at left
    show mrsj 18 at right
    mrsjo "I mean, {b}strong{/b}!"
    show mrsj 14 at right
    show player 17 at left
    player_name "I hope so..."
    show mrsj 17 at right
    show player 1 at left
    mrsjo "Anyway, is there anything you wanted to talk about?"
    return

label mrsj_button_yoga_room_dialogue_pre_repeat:
    show player 14 at left
    show mrsj 14 at right
    with dissolve
    player_name "Hi, {b}Mrs. Johnson{/b}!"
    show player 1 at left
    show mrsj 17 at right
    mrsjo "Hi, {b}[firstname]{/b}!"
    show player 11 at left
    show mrsj 18 at right
    mrsjo "You're starting to look fit, young man!"
    show player 29 at left
    show mrsj 14 at right
    player_name "Oh. Thanks..."
    player_name "So are you..."
    show player 1 at left
    show mrsj 17 at right
    mrsjo "Is there anything you wanted to talk about?"
    return

label mrsj_button_yoga_room_dialogue_hows_erik:
    show player 10 at left
    show mrsj 14 at right
    player_name "How's {b}Erik{/b} these days?"
    player_name "I hardly see him."
    show mrsj 18 at right
    show player 5 at left
    mrsjo "Well... You know how he is!"
    mrsjo "He just loves his video games..."
    show player 10 at left
    show mrsj 14 at right
    player_name "Yeah, but it's been even worse lately."
    player_name "I don't even get text messages from him..."
    show mrsj 19 at right
    show player 5 at left
    mrsjo "..."
    show mrsj 20 at right
    show player 11 at left
    mrsjo "You know, I think he's having problems adjusting to life out on his own."
    mrsjo "I worry about him."
    show mrsj 19 at right
    show player 12 at left
    player_name "I had no idea."
    show mrsj 20 at right
    show player 11 at left
    mrsjo "He's not used to being the man of the house."
    mrsjo "... And he has such a hard time with girls."
    show mrsj 19 at right
    mrsjo "The poor thing has to be lonely."
    show mrsj 14 at right
    show player 21 at left
    player_name "...Yeah. I think I understand."
    show mrsj 18 at right
    show player 13 at left
    mrsjo "It's a good thing he has a loyal friend like you, {b}[firstname]{/b}!"
    mrsjo "He needs you."
    show mrsj 14 at right
    show player 17 at left
    player_name "Well, we've always been friends so..."
    show mrsj 18 at right
    show player 1 at left
    mrsjo "I'll tell him to text you more often!"
    show mrsj 14 at right
    show player 14 at left
    player_name "It's alright, I just wanted to make sure he's okay."
    show mrsj 17 at right
    show player 1 at left
    mrsjo "Is there anything else you wanted to talk about?"
    return

label mrsj_button_yoga_room_dialogue_what_was_that:
    call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_pre")
    if M_anna.is_state(S_anna_start):
        call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_anna_intro")
        $ M_anna.trigger(T_anna_intro)
    call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_after")
    return

label mrsj_button_yoga_room_dialogue_what_was_that_pre:
    show mrsj 14 at right
    show player 14 at left
    player_name "What was that {b}yoga pose{/b} you were doing earlier?"
    show mrsj 13 at right
    show player 13 at left
    show player 1 at left
    mrsjo "Oh, I'll show you!"
    show mrsj 12 at right
    show player 11 at left
    mrsjo "You start like this!"
    show mrsj 11 at right
    window hide
    pause
    show player 21 at left
    show mrsj 10 at right
    window hide
    pause
    mrsjo "All the way down on your knees!"
    window hide
    pause
    show player 21 at left
    player_name "Uhhh..."
    player_name "...Yeah..."
    show player 11 at left
    mrsjo "It's called the {b}Cat Cow{/b}!"
    show mrsj 11 at right
    window hide
    pause
    show mrsj 12 at right
    window hide
    pause
    show mrsj 13 at right
    show player 18 at left
    mrsjo "Not bad, right?"
    return

label mrsj_button_yoga_room_dialogue_what_was_that_anna_intro:
    show anna 12f at Position (xpos=600)
    show mrsj 13 at right
    show player 13
    with dissolve
    anna "Hello, {b}Tammy{/b}."
    show anna 5f
    anna "Don't tell me you started without me."
    show anna 4f
    show mrsj 18
    mrsjo "Of course not! I'm just chatting with a friend of my tenant, {b}Erik{/b}!"
    show anna 11 at Position (xpos=700) with dissolve
    show mrsj 17b
    mrsjo "{b}Anna{/b}, this is {b}[firstname]{/b}. {b}[firstname]{/b}, this is my friend, {b}Anna{/b}."
    show mrsj 14
    show player 36 with dissolve
    player_name "Hi!"
    show player 13 with dissolve
    show mrsj 14b
    show anna 12
    anna "You're a friend of {b}Erik{/b}?"
    show anna 11
    show player 14
    show mrsj 14
    player_name "Yeah. We've been friends for a long time."
    show player 12
    player_name "Are you a trainer here too?"
    show player 5
    show anna 2 with dissolve
    show mrsj 14b
    anna "Oh, no. I'm just a student."
    show anna 1
    show player 13
    show mrsj 17
    mrsjo "{b}Anna{/b} is one of my best. She could teach here if she wanted to!"
    show mrsj 14b
    show anna 3
    anna "Oh, I don't think so! Ha ha!"
    show anna 2
    anna "She's a great teacher and I'm just a novice."
    show anna 1
    show mrsj 17
    mrsjo "{b}Anna{/b}, is just being humble."
    show mrsj 17b
    mrsjo "She might be a beginner, but she is very talented... and extremely flexible."
    show mrsj 14b
    show anna 3
    anna "Ha ha."
    show anna 2
    anna "I've gotta go now and get ready for my next lesson."
    show anna 3
    anna "Goodbye, {b}Tammy{/b}!"
    show anna 1
    show mrsj 17b
    mrsjo "See you soon."
    show mrsj 14b
    show anna 2
    anna "It was a pleasure meeting you, {b}[firstname]{/b}."
    show anna 1
    show player 14
    show mrsj 14
    player_name "Bye!"
    hide anna with dissolve
    return

label mrsj_button_yoga_room_dialogue_what_was_that_after:
    show mrsj 17 at right
    show player 1 at left
    mrsjo "Is there anything else you wanted to talk about?"
    return

label mrsj_button_yoga_room_dialogue_youre_so_fit:
    show mrsj 14 at right
    show player 29 at left
    player_name "I have to say, {b}Mrs. Johnson{/b}, you are really fit!"
    player_name "Do you exercise a lot?"
    show mrsj 18 at right
    show player 13 at left
    mrsjo "Aw... You're so nice!"
    show mrsj 17 at right
    mrsjo "Well, I come here as often as I can and try to use the Gym..."
    mrsjo "...I also go jogging! And I do yoga in my room at night as well..."
    show mrsj 19 at right
    show player 21 at left
    player_name "Well, it's working!"
    show player 13 at left
    mrsjo "You think?"
    show mrsj 15 at right
    show player 11 at left
    mrsjo "My {b}butt{/b} is still a bit big..."
    show mrsj 16 at right
    show player 23 at left
    mrsjo "...And my {b}boobs{/b} are not like they used to be..."
    player_name "..."
    show player 28 at left
    show mrsj 19 at right
    player_name "*gulp*"
    show player 1 at left
    show mrsj 18 at right
    mrsjo "Is there anything else you wanted to talk about?"
    return

label mrsj_button_yoga_room_dialogue_have_to_train:
    show mrsj 14 at right
    show player 14 at left
    player_name "I should get back to my training!"
    show mrsj 18 at right
    show player 1 at left
    mrsjo "Okay, then!"
    show mrsj 14 at right
    show player 17 at left
    player_name "Bye, {b}Mrs. Johnson{/b}!"
    hide player 17 at left with dissolve
    hide mrsj 14 at right with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
