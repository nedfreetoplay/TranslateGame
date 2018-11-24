label judith_dialogue_start:
    scene lefthall_c
    show player 1 at left
    show judith 5 at right
    with dissolve
    jud "Hey {b}[firstname]{/b}!"
    show player 2 at left
    show judith 4 at right
    player_name "Hey {b}Judith{/b}, how's it going?"
    show player 1 at left
    show judith 5 at right
    jud "Oh, I'm great!"
    show judith 2 at right
    jud "I... I just wanted to thank you."
    show judith 4 at right
    show player 21 at left
    player_name "Oh. For what?"
    show judith 3 at right
    show player 13 at left
    jud "In the locker room... You made me feel... safe."
    show judith 4 at right
    show player 11 at left
    player_name "Oh..."
    show judith 5 at right
    jud "And, you know... you stood up to {b}Annie{/b}. I think that was very brave."
    show judith 4 at right
    show player 29 at left
    player_name "It's fine, {b}Judith{/b}. I was just trying to do the right thing."
    player_name "I should be the sorry one... for showing you my... you know..."
    show judith 5 at right
    show player 11 at left
    jud "Oh that's fine!! I enjoyed-"
    show judith 3 at right
    jud "I mean... I didn't mind, at all."
    show judith 5 at right
    jud "We just got to... know each other a little better!"
    show judith 4 at right
    show player 21 at left
    player_name "Haha. Yeah. I suppose so..."
    show judith 5 at right
    show player 1 at left
    jud "I have to go! I'll see you in class then!"
    show player 14 at left
    show judith 4 at right
    player_name "See you later!"
    return

label judith_dialogue_left_hallway_intro:
    scene lefthall_c
    show judith 1 at right
    show player 14 at left
    with dissolve
    player_name "Hey, {b}Judith{/b}!"
    show player 13
    show judith 5
    jud "Oh, hey, {b}[firstname]{/b}."
    jud "How are you doing?"
    show judith 4
    show player 14
    player_name "Pretty good. How are you?"
    show player 13
    show judith 6
    jud "..."
    show judith 2
    jud "Alright I guess."
    show judith 1
    return

label judith_dialogue_art_classroom_intro:
    scene art_classroom_c
    show judith 1 at right
    show player 14 at left
    show xtra 22 as table zorder 0
    show xtra 23 as basket zorder 0 at Position (ypos = 635)
    show xtra 24 as fruit zorder 0 at Position (ypos = 565)
    with dissolve
    player_name "Enjoying art, {b}Judith{/b}?"
    show player 13
    show judith 5
    jud "Yeah!"
    jud "It's one of my favorite subjects."
    show judith 4
    show player 14
    player_name "Yeah, mine too!"
    show player 13
    show judith 5
    jud "I like it because no matter how bad my drawings are, it's still considered art!"
    show judith 4
    show player 17
    player_name "Heh, good one."
    show judith 1
    return

label judith_dialogue_bathroom_fun:
    show player 2
    player_name "Say, would you like to sneak into the girls locker for a little... You know?"
    show player 1
    show judith 5
    jud "... You really want to..."
    jud "... W-with me?"
    show player 2
    show judith 4
    player_name "I mean, yeah!"
    player_name "If that's okay?"
    show player 1
    show judith 5
    jud "Oh, definitely!"
    jud "Let's go!"
    return

label judith_dialogue_dictionary_return:
    show player 14
    player_name "Hey, {b}Judith{/b}! Here's your book back."
    show player 239_240 with dissolve
    pause
    show player 522 with dissolve
    player_name "Thanks again!"
    show player 13
    show judith 43
    with dissolve
    jud "Oh good, I was starting to worry..."
    show judith 4 with dissolve
    show player 14
    player_name "No need to worry. It's in tip top shape... See."
    show player 13
    show judith 5
    jud "Thanks for being careful with it, {b}[firstname]{/b}."
    jud "I dunno why I worry so much..."
    show judith 4
    show player 14
    player_name "Thanks for letting me borrow it!"
    show player 13
    show judith 5
    jud "Anything for yo-"
    show judith 3
    jud "I mean... A-anytime!"
    show judith 1
    show player 10
    player_name "Okay, well I'll see ya around."
    show player 5
    show judith 3
    jud "Bye, {b}[firstname]{/b}."
    return

label judith_dialogue_bissette_find_full_dictionary:
    show player 14
    player_name "Hey there, {b}Judith{/b}! Got a minute?"
    show player 13
    show judith 5
    jud "Sure, {b}[firstname]{/b}."
    show judith 4
    show player 14
    player_name "I was hoping I could borrow your French dictionary."
    player_name "I need to make a quick copy of some pages and I'll return it."
    show player 13
    show judith 3
    jud "My French dictionary?"
    show judith 5
    jud "Absolutely! So long as you promise to be careful with it?"
    show judith 4
    show player 11
    player_name "( What is with women and their French dictionaries? )"
    show player 10
    player_name "Yeah, I'll be really careful and you won't even notice it's gone."
    show player 13
    show judith 5
    jud "Okay, I trust you, {b}[firstname]{/b}."
    pause
    show judith 43 with dissolve
    jud "Here it is..."
    show judith 4
    show player 522
    with dissolve
    player_name "Thanks {b}Judith{/b}! I totally owe you one!"
    hide judith with dissolve
    show player 13
    player_name "( Alright, now to {b}head to the computer lab{/b} and copy these missing pages. )"
    return

label judith_dialogue_dewitt_find_flute:
    show player 10
    player_name "Do you still have the school's flute?"
    player_name "I need it for the talent show."
    show player 5
    show judith 2
    jud "Oh, umm..."
    show judith 1
    show player 10
    player_name "The instrument sign-out sheet had your name next to the flute."
    show player 5
    show judith 2
    jud "*Sigh*"
    show judith 3
    jud "I do have it. It's in my locker."
    show judith 1
    show player 12
    player_name "I have a feeling there is a \"but\" coming?"
    show player 5
    show judith 3
    jud "BUT, I kinda broke it..."
    show judith 1
    show player 1
    player_name "You broke it!?"
    player_name "How did that happen?!"
    show player 5
    show judith 5
    jud "Heh, well I accidentally kinda..."
    show judith 6
    show player 11
    player_name "..."
    show judith 2
    jud "... Sat on it."
    show judith 1
    show player 10
    player_name "You sat on it?"
    show player 11
    show judith 3
    jud "... Yeah."
    show judith 5
    jud "Which sucks cause I was really enjoying it!"
    show judith 4
    show player 10
    player_name "I didn't know you could play the flute?"
    show player 5
    show judith 5
    jud "Oh, I can't play it."
    show judith 4
    show player 12
    player_name "Well then I don't understand how you were enjoying it?"
    show player 5
    jud "..."
    show judith 5
    jud "Heh, nevermind."
    show judith 2
    jud "I was hoping no one would ask about it..."
    show judith 1
    show player 10
    player_name "Maybe I can fix it?"
    show player 5
    show judith 4
    jud "..."
    show judith 5
    jud "You can try."
    show judith 4
    show player 12
    player_name "Is it still in your locker?"
    show player 5
    show judith 5
    jud "Yup."
    show judith 4
    show player 10
    player_name "Alright, thanks, {b}Judith{/b}."
    return

label judith_dialogue_talent_show_help:
    show player 10
    player_name "I was wondering if you wanted to participate in the upcoming talent show?"
    show player 5
    show judith 3
    jud "No thanks, {b}[firstname]{/b}. I don't really know how to play an instrument."
    show judith 2
    jud "... And I'm way too embarrassed to get up on stage in front of the entire school."
    show judith 1
    show player 10
    player_name "Well what if we played together?"
    show player 5
    show judith 5
    jud "You and me?"
    show judith 4
    show player 14
    player_name "Sure, why not?"
    show player 13
    show judith 6
    jud "Hmm..."
    show judith 2
    jud "No, I'm sorry, {b}[firstname]{/b}."
    show judith 3
    jud "As much as I'd enjoy playing with you; Just the thought of being in the spotlight like that..."
    show judith 8f at Position (xoffset=2) with dissolve
    show player 11
    jud "..."
    show judith 9f at Position (xoffset=-4) with dissolve
    jud "Excuse me, I need to go use the restroom!"
    hide judith with dissolve
    show player 12
    player_name "Dang, I thought for a second she was going to agree."
    show player 10
    player_name "Guess I'd better keep looking..."
    return

label judith_dialogue_okita_get_bifocal_lenses:
    show player 2
    player_name "Judith, are you farsighted or nearsighted?"
    show player 1
    show judith 2
    jud "Uhh, well."
    show judith 3
    jud "Both..."
    show player 2
    show judith 1
    player_name "Really?!"
    show player 1
    show judith 2
    jud "Yeah. I'm blind without my glasses..."
    show judith 3
    jud "Pretty dorky. I know..."
    show player 2
    show judith 1
    player_name "No, it's great!"
    show player 1
    show judith 3
    jud "It is?"
    show player 29 with dissolve
    show judith 1
    player_name "Well I mean, no. It sucks that you can't see without them."
    show player 2 with dissolve
    player_name "... But it's also a good thing, cause I'm looking for a pair of Varifocal lenses."
    show player 1
    show judith 5
    jud "Oh. Well, you found some."
    show player 2
    show judith 4
    player_name "You wouldn't happen to have a spare set would you?"
    show player 1
    show judith 5
    jud "Sure."
    show player 2
    show judith 4
    player_name "Awesome! Could I have them?"
    show player 1
    show judith 2
    jud "Hmm, you want me to just give you my spare set?"
    show player 10
    show judith 1
    player_name "... Yes?"
    show player 11
    show judith 3
    jud "How about a trade?"
    show player 2
    show judith 1
    player_name "Yeah, okay. What do you want?"
    show player 1
    show judith 2
    jud "Umm, it's kinda embarrassing..."
    show judith 1
    player_name "..."
    show judith 2
    jud "Well, you see, some of the other girls have been giving me a hard time..."
    show judith 3
    jud "... because I've never had a boyfriend."
    show player 10
    show judith 1
    player_name "That sucks."
    show player 11
    show judith 2
    jud "Yeah."
    jud "I was kinda wondering..."
    show judith 3
    jud "... Well, I was hoping you would pretend to be my boyfriend."
    show player 23
    show judith 1
    player_name "( !!! )" with hpunch
    show player 10
    player_name "You want me to pretend to be your boyfriend?"
    show player 11
    show judith 3
    jud "Just long enough to take a couple pictures!"
    show player 10
    show judith 1
    player_name "Pictures?!"
    show player 11
    show judith 2
    jud "Yeah."
    show judith 3
    jud "You meet me in the park, we take a couple pictures like we're boyfriend and girlfriend, and then I'll give you my spare set."
    jud "Deal?"
    show player 10
    show judith 1
    player_name "I uhh..."
    show player 11
    show judith 3
    jud "Pleeeease? It would be such a huge help!"
    show player 2
    show judith 1
    player_name "Yeah, alright, I suppose I can do that."
    show player 1
    show judith 5
    jud "You will?!"
    jud "Okay, meet me at the park! I'll be there in the {b}afternoons{/b}."
    show player 2
    show judith 4
    player_name "{b}The park, in the afternoon.{/b} Got it!"
    show player 1
    show judith 5
    jud "Great! See you there!"
    return

label judith_dialogue_okita_take_picture_judith:
    show player 2
    player_name "Where did you want to take that picture again?"
    show player 1
    show judith 3
    jud "Oh umm, at the park."
    show player 2
    show judith 1
    player_name "Alright."
    show player 1
    show judith 3
    jud "You aren't having second thoughts, are you?"
    show judith 2
    jud "Cause it's okay, we don't hav-"
    show player 2
    show judith 1
    player_name "No, {b}Judith{/b}. It's fine, really!"
    show judith 4
    player_name "I'll meet you there!"
    show player 1
    show judith 5
    jud "... Thanks, {b}[firstname]{/b}."
    return

label judith_dialogue_ross_ask_model:
    show player 2
    player_name "I'm working on a project for {b}Miss Ross{/b} and it requires a live model."
    player_name "Would you be interested?"
    show player 1
    show judith 5
    jud "You want me to model for you?"
    show player 2
    show judith 4
    player_name "Yeah, that would be awesome!"
    show player 10
    player_name "It's nude modeling though..."
    show player 11
    show judith 3
    jud "... Oh."
    show judith 1
    jud "..."
    show judith 3
    jud "... You really want me to?"
    show player 10
    show judith 1
    player_name "Of course!"
    show player 11
    show judith 5
    jud "Then I'll do it! For you, {b}[firstname]{/b}!"
    show player 2
    show judith 4
    player_name "Thanks {b}Judith{/b}! That's really awesome of you!"
    player_name "Just meet me in the Art class."
    show player 1
    show judith 5
    jud "Alright."
    return

label judith_dialogue_left_hallway_leave:
    show player 5
    player_name "..."
    show judith 6
    jud "..."
    show player 29 with dissolve
    player_name "Well... I'd better get going!"
    show player 3
    show judith 5
    jud "See you later, {b}[firstname]{/b}."
    return

label judith_dialogue_art_classroom_leave:
    show player 14
    player_name "See you later, {b}Judith{/b}."
    show player 13
    show judith 5
    jud "Bye, {b}[firstname]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
