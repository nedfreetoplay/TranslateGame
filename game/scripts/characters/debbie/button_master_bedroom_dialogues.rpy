label debbie_dialogue_master_room_pre:
    scene debbie_bedroom_closeup2
    show debbie 55 at left
    show player 110 at right
    with dissolve
    deb "Hi, sweetie..."
    deb "Were you looking for me?"
    show debbie 54
    show player 111
    player_name "Yeah..."
    show player 110
    show debbie 55
    deb "Is there something you wanted from me?"
    show debbie 54
    return

label debbie_dialogue_master_room_after_kiss_dialogue:
    deb "Now, is there anything else you wanted?"
    show debbie 54
    return

label debbie_dialogue_master_room_kiss:
    show player 111 at right
    show debbie 54 at left
    player_name "Can I have a kiss?"
    show player 110
    show debbie 55
    deb "Of course, sweetie! Come here."
    scene debbie_bedroom
    show debbie 79
    with fade
    deb "Mmmm..."
    show debbie 80_79
    pause 3
    show debbie 75 at Position(xpos=750)
    show player 227 at Position(xpos=200)
    with fastdissolve
    deb "You're getting better at this!"
    scene debbie_bedroom_closeup2
    show debbie 55 at left
    show player 110 at right
    with fade
    return

label debbie_dialogue_master_room_shower:
    show player 111
    player_name "Hey, {b}[deb_name]{/b}!"
    player_name "Want to take a shower with me?"
    show player 110
    show debbie 55
    deb "It is getting pretty hot in the house..."
    deb "Sure! A shower sounds lovely right now."
    deb "You go ahead, sweetie. I'll be there in a minute."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    deb "Sorry to keep you waiting, sweetie..."
    return

label debbie_dialogue_master_room_sex_random_true:
    show debbie 54 at left
    show player 111 at right
    player_name "I feel like... Doing it with you again."
    show player 110
    show debbie 55
    deb "That's okay!"
    deb "I was hoping you'd want to..."
    show player 111
    show debbie 54
    player_name "Really?"
    show player 110
    show debbie 58 with dissolve
    deb "Of course! You're my man, after all."
    show debbie 57
    player_name "!!!"
    show debbie 58
    deb "Take your clothes off, sweetie."
    show debbie 57
    show player 8f
    pause
    show player 261
    pause
    show player 263
    pause
    show debbie 103
    deb "Mmm, come get me, sweetie!"
    show player 262 at right
    show debbie 102 at left
    player_name "Don't have to tell me twice..."
    return

label debbie_dialogue_master_room_sex_random_false:
    show debbie 54 at left
    show player 111 at right
    player_name "{b}[deb_name]{/b}, want to have some fun?"
    show player 110
    show debbie 54
    deb "Oh?"
    show debbie 56 with dissolve
    deb "Like...this kinda fun?"
    show debbie 57
    show player 111
    player_name "Of course..."
    show player 110
    show debbie 58
    deb "Let me see that cock of yours..."
    show debbie 57
    show player 8f with dissolve
    pause
    show debbie 101
    show player 261 with dissolve
    pause
    show player 263 with dissolve
    pause
    show debbie 58
    deb "It looks like you are ready!"
    show debbie 57
    show player 262
    player_name "I've been looking forward to this since I woke up this morning."
    show player 263
    show debbie 58
    deb "Me too."
    show debbie 102 with dissolve
    pause
    show debbie 103
    deb "Come and get it, sweetie."
    return

label debbie_dialogue_master_room_sex_after:
    hide player
    show debbie 104 at left
    with dissolve
    pause
    hide debbie
    hide player
    with dissolve
    scene debbie_bedroom_closeup_sex
    return

label debbie_dialogue_master_room_laundry_sex:
    show debbie 54
    show player 111
    player_name "I was wondering if you wanted some help in the basement."
    show player 110
    show debbie 55
    deb "In the basement? What for?"
    show player 111
    show debbie 54
    player_name "Maybe I can help you with laundry... Like we did last time?"
    show player 110
    show debbie 55
    deb "Oh, I see... I know exactly what you want!"
    deb "Give me a minute to get ready."
    deb "I'll meet you down there..."
    hide debbie
    hide player
    with dissolve
    return

label debbie_dialogue_master_room_watch_movie:
    show player 111
    player_name "I was thinking, we should watch another movie tonight. Interested?"
    show player 110
    show debbie 55
    deb "Mmm, a movie night, huh?"
    deb "That sounds like a great idea, Sweetheart!"
    show player 111
    show debbie 54
    player_name "Awesome!"
    player_name "I'll see you tonight in the living room then?"
    show player 110
    show debbie 55
    deb "I can't wait..."
    return

label debbie_dialogue_master_room_leave:
    show debbie 54
    show player 111
    player_name "Nothing, {b}[deb_name]{/b}."
    player_name "Just wanted to say hi."
    show player 110
    show debbie 55
    deb "Oh, okay..."
    deb "Well, come back if you'd like... I'm a bit bored..."
    deb "We can have fun whenever you'd like."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
