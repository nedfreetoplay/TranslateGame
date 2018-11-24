label eriksroom_erik_breastfeeding_started:
    scene expression game.timer.image("erik_house_bedroom{}_b")
    show player 12 with dissolve
    player_name "( No one here? )"
    show player 14
    player_name "( He must be in the basement... )"
    show player 11
    pause
    show player 10
    player_name "Huh?"
    player_name "( I think I can hear some voices coming from {b}Mrs. Johnson{/b}'s room. )"
    show player 12
    player_name "( I should ask her where {b}Erik{/b} is... )"
    hide player with dissolve
    return

label eriksroom_erik_bullying_3_completed:
    scene expression game.timer.image("erik_house_bedroom{}_b")
    show player 30 with dissolve
    player_name "Huh?"
    player_name "( {b}Erik{/b} is usually at his computer. )"
    show player 12
    player_name "( He must be in the basement... )"
    hide player with dissolve
    return

label june_intro:
    scene expression game.timer.image("erik_house_bedroom{}_b")
    show player 1 at left
    show erik 4 at right
    with dissolve
    eri "Hey, man."
    eri "Did you end up talking to {b}Mrs. Johnson{/b}?"
    show player 14
    show erik 1
    player_name "Yeah, she thinks it might be a good idea to meet other girls..."
    show player 1
    show erik 5
    eri "Oh, really?"
    show player 14
    show erik 1
    player_name "Yeah, I agree with her!"
    show erik 3c
    player_name "I can try and help you..."
    show player 11
    show erik 3b
    eri "I don't know, {b}[firstname]{/b}."
    show erik 3
    eri "I don't think I'll ever find someone who's right for me..."
    show player 10
    show erik 2
    player_name "What?"
    show player 11
    show erik 3b
    eri "Someone who's like me!"
    show player 10
    show erik 3c
    player_name "What do you mean?"
    show erik 3b
    show player 11
    eri "I'm out of shape, I'm not good at talking to people..."
    show player 5
    eri "... Face it, man, I'm just a klutz..."
    show erik 3
    eri "... The only thing I'm good at is playing games!"
    show player 10
    show erik 3c
    player_name "So?"
    show player 14
    player_name "What if we found you a gamer girl?"
    show player 1
    show erik 5
    eri "A gamer girl..."
    show erik 4
    eri "I... I guess so?"
    show player 4
    show erik 1
    player_name "Hmm..."
    show player 14
    player_name "Do you know a girl at school who likes video games?"
    show player 11
    show erik 4
    eri "Well... There's this one girl from another class... She's kind of cute."
    show player 14
    show erik 1
    player_name "There's a girl at school that you like?"
    show player 1
    show erik 5
    eri "I don't know... she just seems... nice!"
    show player 14
    show erik 1
    player_name "What's her name?"
    show player 1
    show erik 4
    eri "I think her name is {b}June{/b}."
    show player 14
    show erik 1
    player_name "Have you ever talked to her?"
    show player 1
    show erik 14
    eri "Well this one time..."
    eri "... We, uh, I asked her about..."
    show player 11
    show erik 3
    eri "No, not really."
    show erik 3b
    eri "I think she borrowed one of my pencils, once..."
    show player 14
    show erik 3c
    player_name "Why don't you speak to her more?!"
    show player 11
    show erik 3
    eri "I can't!"
    show erik 3b
    eri "I'm WAY too shy..."
    eri "... and I don't even know what I would say to her."
    show player 35
    show erik 3c
    player_name "Okay, well, this might just be harder than I thought."
    show player 11
    show erik 3
    eri "Maybe we should just give up..."
    show erik 2
    eri "*Sigh*"
    show player 10
    player_name "What?!"
    show player 14
    show erik 3c
    player_name "Come on, {b}Erik{/b}!"
    player_name "You'll see! I think she might like you..."
    player_name "Where does she usually hang out?"
    show player 1
    show erik 1
    eri "Hmm..."
    show erik 5
    eri "I've seen her in the computer room many times before."
    show player 14
    show erik 1
    player_name "The {b}computer room{/b} at {b}school{/b}?"
    show player 1
    show erik 4
    eri "Yeah. It's on the second floor..."
    show player 14
    show erik 1
    player_name "I'll go see her, maybe I can try and set something up for you."
    show player 1
    show erik 4
    eri "Okay, thanks, man."
    show erik 1
    return

label erik_sex_ed:
    scene expression game.timer.image("eriks_room{}_c")
    show player 13 at left
    show erik 5 at right
    with dissolve
    eri "Hey, {b}[firstname]{/b}!"
    eri "Did you end up talking to {b}Mrs. Johnson{/b}?"
    show erik 1
    show player 14
    player_name "Yeah, she said she needed to think about it..."
    show player 13
    show erik 5
    eri "Maybe we shouldn't have said-"
    show erik 1b
    show player 11
    mrsjo "Boys?"
    mrsjo "Can you come over here, please?"
    show erik 1
    show player 10
    player_name "Was that {b}Mrs. Johnson{/b}?"
    show player 5
    show erik 5
    eri "Yeah... I think she's in her room."
    show erik 1
    show player 14
    player_name "She wants us to come over..."
    show player 13
    show erik 5
    eri "Why?"
    show erik 1
    show player 14
    player_name "We'll have to see..."
    hide player
    hide erikl
    hide erik
    with dissolve
    return

label erik_bullying:
    scene expression game.timer.image("eriks_room{}_c")
    show player 13 at left with dissolve
    show erik 5 at right with dissolve
    eri "Hey, {b}[firstname]{/b}."
    eri "How've you been?"
    show erik 1
    show player 14
    player_name "I've been doing pretty good."
    show player 12
    player_name "How about you?"
    player_name "Have you been missing classes lately or something?"
    show player 5
    show erik 2 with dissolve
    eri "..."
    show player 10
    player_name "Is everything alright?"
    show player 5
    show erik 5 with dissolve
    eri "{b}Mrs. Johnson{/b} sent you up here, huh?"
    show erik 3b
    show player 10
    player_name "Just checking up on you, that's all."
    show player 5
    show erik 5
    eri "Well... {b}Dexter{/b} has been on my case ever since you left..."
    eri "It's just been hard to attend school knowing he'll be there too. Waiting..."
    show erik 3b
    show player 12
    player_name "What happened while I was away?"
    show player 5
    show erik 5
    eri "A few weeks ago, I was sitting in the cafeteria and he came up to me..."
    show erik 3
    eri "...He said he wanted a copy of my homework for {b}Miss Bissette{/b}'s class."
    show player 12
    player_name "What did you do?"
    show player 11
    show erik 5
    eri "I told him no!"
    eri "But, he said he'd stick me into a locker If I didn't do what he asked..."
    show erik 3b
    player_name "..."
    show erik 5
    eri "Anyway, I ended up giving him my homework and have been until recently."
    show erik 3b
    show player 38 with dissolve
    player_name "What happened?"
    show player 11 with dissolve
    show erik 5
    eri "I told him he can't push me around all the time."
    eri "And then... He hit me in front of everyone..."
    show erik 2 with dissolve
    show player 16
    pause
    show player 12
    player_name "Hey, {b}Erik{/b}..."
    show erik 3 with dissolve
    show player 10
    player_name "I'm glad you told me."
    show player 30
    player_name "Let me know if he bothers you again."
    player_name "And hopefully he can focus his attention on someone else!"
    show player 13
    show erik 5
    eri "Alright, thanks {b}[firstname]{/b}."
    show erik 3b
    show player 14
    player_name "You gonna be OK?"
    show player 13
    show erik 5
    eri "Yeah, I guess..."
    eri "But, can you please not tell {b}Mrs. Johnson{/b} I'm being bullied at school?"
    eri "I don't want her to worry so much..."
    show erik 3b
    show player 2
    player_name "Okay."
    hide player
    hide erikl
    hide erik
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
