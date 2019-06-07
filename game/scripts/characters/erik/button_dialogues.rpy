label button_erik_master_blaster:
    show player 2
    player_name "You remember that {b}Master Blaster{/b} game {b}Mrs. Johnson{/b} bought you for Christmas a few years ago?"
    show player 1
    show erik 4
    eri "Of course, man! We spent the entire summer playing on that thing!"
    show player 2
    show erik 1
    player_name "Do you still have it?"
    show player 1
    show erik 5
    eri "Yeah, I think so. Haven't used it in a long time..."
    show erik 4
    eri "In fact, {b}I think it's just collecting dust in our old tree house{/b}."
    show player 2
    show erik 1
    player_name "Would you mind if I take it?"
    show player 1
    show erik 4
    eri "Sure, no problem."
    show player 2
    show erik 1
    player_name "Thanks, {b}Erik{/b}!"
    return

label button_erik_master_blaster_again:
    show player 2
    player_name "Where did you say that controller was again?"
    show player 1
    show erik 5
    eri "I think I left it in our old tree house."
    show player 2
    show erik 1
    player_name "Ah, that's right. Thanks, {b}Erik{/b}!"
    show player 1
    show erik 4
    eri "No problem, dude!"
    return

label button_erik_make_flute:
    show player 12
    player_name "What do I need to make a flute?"
    show player 5
    show erik 5
    eri "All you need is an appropriate sized {b}branch off a tree and a drill{/b}."
    show erik 52
    show player 12
    player_name "{b}A branch off a tree{/b}? Can't I just use the lumber at our tree house?"
    show player 5
    show erik 5
    eri "Well you might do but I remember in the game they specifically said to {b}look for a fallen branch{/b}."
    eri "Something about the instrument needing the spirit energy of the forest to play true."
    show erik 52
    show player 14
    player_name "That sounds like video game nonsense to me!"
    show player 13
    show erik 5
    eri "Hmm, it could be but do you really want to chance it?"
    show erik 52
    show player 10
    player_name "... No, I guess not."
    player_name "So, I should {b}look for a fallen branch off a tree{/b}."
    show player 12
    player_name "Then what?"
    show player 5
    show erik 5
    eri "Just drill out the center and then make some holes on one side."
    show erik 52
    show player 14
    player_name "Oh yeah!"
    player_name "You know, I think {b}I've seen a drill in our garage{/b}."
    show player 13
    show erik 4
    eri "Sounds like you've got it all figured out then!"
    return

label button_erik_talent_show:
    show player 14
    player_name "You play guitar, right?"
    show player 13
    show erik 3b
    eri "Huh?"
    eri "No. What gave you that idea?"
    show erik 51
    show player 10
    player_name "Well, aren't those your guitars hanging up in your basement..."
    player_name "I just assumed-"
    show player 5
    show erik 4
    eri "Oh, right! Yeah, those are {b}Mr. Johnson's{/b} old guitars."
    show erik 3
    eri "He never allowed me near them."
    eri "Didn't want me to break them, he said."
    eri "..."
    show erik 3b
    eri "Sometimes, I think he loved those guitars more than {b}Mrs. Johnson{/b}."
    show erik 3c
    show player 25
    player_name "Yikes."
    show player 5
    show erik 4
    eri "Tell me about it."
    eri "Anyways, I have much better hobbies than music!"
    show erik 1
    show player 14
    player_name "You mean your video games?"
    show player 13
    show erik 4
    eri "Heck yeah, dude!"
    return

label button_erik_borrow_guitar:
    show player
    player_name "Hey man, I need a favor!"
    show player 13
    show erik 4
    eri "Sure, what's up, dude?"
    show erik 1
    show player 14
    player_name "You know those guitars in your basement?"
    show player 13
    show erik 5
    eri "Yeah."
    show erik 1
    show player 10
    player_name "You think I could borrow one for the talent show?"
    show player 5
    show erik 5
    eri "... You wanna borrow one of {b}Mr. Johnson's{/b} guitars?"
    show erik 52
    show player 14
    player_name "Yeah, if it's alright?"
    player_name "I'll bring it back after the talent show."
    show player 13
    show erik 50
    eri "Hmm."
    show erik 5
    eri "Well I don't mind but I'm not sure {b}Mrs. Johnson{/b} would like the idea of me loaning out {b}Mr. Johnson's{/b} old stuff."
    show erik 52
    show player 10
    player_name "Really?"
    show player 5
    show erik 5
    eri "Yeah, especially his guitars. They were his babies."
    show erik 52
    show player 34
    player_name "Hmm..."
    show player 12
    player_name "What if she didn't know?"
    show player 5
    show erik 4
    eri "I'm pretty sure she'll notice if one is missing off the wall, {b}[firstname]{/b}. She isn't blind."
    show erik 52
    show player 33
    player_name "Not if I replace it with a fake."
    show player 13
    eri "..."
    show erik 5
    eri "Seriously?"
    eri "Where are you gonna get a fake guitar?"
    show erik 52
    show player 14
    player_name "... I'll make one!"
    show player 13
    show erik 5
    eri "Dude, have you lost your mind?"
    show erik 52
    show player 14
    player_name "No, trust me this will work."
    player_name "She won't even notice it's gone, I promise!"
    show player 13
    show erik 5
    eri "... If you say so. Just make sure nothing happens to the real guitar!"
    eri "{b}Mrs. Johnson{/b} would kill me!"
    show erik 52
    show player 14
    player_name "I'll be careful, {b}Erik{/b}. I promise."
    show player 13
    hide erikl
    hide erik
    with dissolve
    show player 4
    if not L_diane_shed.locked:
        player_name "( Hmm, I should be able to make a fake guitar using the {b}lumber near the treehouse{/b} and some {b}paint from Diane's shed.{/b} )"
    else:
        player_name "( Hmm, I should be able to make a fake guitar using the {b}lumber near the treehouse{/b} and some {b}paint from the garage at home.{/b} )"
    return

label button_erik_make_guitar:
    show player 13
    eri "How's that replacement guitar coming along?"
    show erik 1
    show player 14
    player_name "Still a work in progress."
    show player 13
    show erik 5
    eri "Well just be careful with the real guitar, please."
    show erik 1
    show player 14
    player_name "Will do!"
    show player 13
    hide erikl
    hide erik
    with dissolve
    show player 4
    if not L_diane_shed.locked:
        player_name "( Hmm, I should be able to make a fake guitar using the {b}lumber near the treehouse{/b} and some {b}paint from Diane's shed.{/b} )"
    else:
        player_name "( Hmm, I should be able to make a fake guitar using the {b}lumber near the treehouse{/b} and some {b}paint from the garage at home.{/b} )"
    return

label button_erik_ask_beer:
    show player 10
    player_name "Hey man, could I take a case of {b}Mr. Johnson's beer{/b}?"
    show player 5
    show erik 5
    eri "Eh, yeah I guess."
    show player 13
    eri "What's it for?"
    show erik 52
    show player 14
    player_name "It's a bribe for {b}Eve's{/b} friends. They are gonna help us clean the graffiti off the auditorium walls."
    show player 13
    show erik 5
    eri "Oh, for {b}Miss Dewitt's{/b} talent show?"
    show erik 52
    show player 14
    player_name "Yup."
    show player 13
    show erik 4
    eri "Cool!"
    eri "Take as much as you need, dude."
    show erik 1
    show player 17
    player_name "Thanks {b}Erik{/b}! You're a good friend!"
    return

label button_erik_school_sneak_mission_help:
    show player 10
    player_name "I really need your help with something big tonight, {b}Erik{/b}."
    show player 5
    show erik 5
    eri "Something big?"
    show erik 52
    show player 33
    player_name "Yeah, Man. I'm talking like uber secret mission kinda stuff."
    show player 13
    show erik 4
    eri "That sounds awesome! You really want my help!?"
    show erik 1
    show player 14
    player_name "Sure!"
    show player 12
    player_name "Everyone else chickened out on me, so... I'm kinda counting on you here."
    show player 5
    show erik 4
    eri "Don't worry, {b}[firstname]{/b}. I won't let you down!"
    show erik 1
    show player 17
    player_name "Thanks, dude!"
    show player 14
    player_name "Meet me in {b}front of the school tonight{/b}, after the sun sets."
    show player 13
    show erik 5
    eri "Whoa, wait a second..."
    show player 5
    eri "You wanna break into the school after dark?!"
    show erik 3b
    eri "I dunno about this..."
    show erik 52
    show player 10
    player_name "... I have to, man."
    player_name "If I don't, {b}Principal Smith{/b} is going to cancel the {b}Talent Show{/b} and I won't be able to get my grades up!"
    show player 5
    show erik 3
    eri "..."
    eri "A-alright, {b}[firstname]{/b}. I'll help you."
    show erik 3c
    show player 14
    player_name "Yes! Thank you, {b}Erik{/b}!"
    show erik 1
    player_name "You're a good friend!"
    show player 13
    show erik 4
    eri "Heh, no worries, dude."
    show erik 5
    eri "I'll meet you {b}tonight in front of the school{/b}."
    return

label erik_book_return:
    show player 10 at left
    show erik 1 at right
    if player.location == L_school_scienceclassroom:
        show erikl 1f at right
    player_name "I'm trying to check out a book for school but the librarian has me running errands."
    player_name "She said you had a book that's overdue and I was hoping I could get it from you."
    show player 5
    show erik 3b
    eri "I do?"
    show erik 3
    eri "I don't remember-"
    show erik 4
    eri "Ohhh wait, that's right!"
    eri "I did check one out..."
    show erik 3b
    eri "I have no idea where it could be though. Crap!"
    show erik 2
    if player.location == L_school_scienceclassroom:
        show erikl 2 at right
    with dissolve
    pause
    show erik 3b
    if player.location == L_school_scienceclassroom:
        show erikl 1f at right
    with dissolve
    eri "I remember {b}reading it in my room{/b}..."
    show erik 3
    eri "Urrgh, but I have no idea where it could have gotten to..."
    show erik 3b
    eri "Sorry, {b}[firstname]{/b}."
    show erik 52
    show player 14
    player_name "It's alright, I'll look around for it."
    show player 13
    show erik 4
    eri "Okay, good luck, dude!"
    hide erik
    hide erikl
    hide player
    with dissolve
    return

label button_erik_sex_ed:
    show erik 1 at right
    show player 12 at left
    player_name "What did {b}Mrs. Johnson{/b} want us to get again?"
    show player 5
    show erik 5
    eri "Hmm... I think she wants us to get {b}pills so she won't get pregnant{/b}."
    eri "And that book? The one about sex positions..."
    show erik 1
    show player 35
    player_name "Yeah, something about {b}Kama Sutra{/b}?"
    show player 34
    show erik 5
    eri "I think so."
    show erik 1
    show player 14
    player_name "Alright."
    hide player
    hide erik
    hide erikl
    with dissolve
    return

label button_erik_girlfriend:
    show player 14
    player_name "Dude, I got some great news for you!"
    show player 1
    show erik 5
    eri "Huh?"
    show player 14
    show erik 1
    player_name "So, I spoke to {b}June{/b}..."
    show erik 4
    eri "Oh yeah?"
    show player 14
    show erik 1
    player_name "Apparently, she likes to play this game called Orc Bork..."
    player_name "... and she's been looking to play it with someone!"
    show player 1
    show erik 4
    eri "Really?"
    show player 17
    show erik 1
    player_name "Yup!"
    show player 14
    player_name "I even told her about you!"
    player_name "I mentioned your name and how you could help her beat the game she's been playing."
    show player 1
    show erik 4
    eri "Woah..."
    show erik 1
    show player 17
    player_name "You should talk to her next time you have a chance!"
    show player 1
    show erik 4
    eri "Yeah... I should!"
    show player 14
    show erik 1
    player_name "Anyway, It's going to be great, you'll see!"
    show player 1
    show erik 4
    eri "Thanks, {b}[firstname]{/b}."
    show player 14
    show erik 1
    player_name "I'll talk to you later, then."
    hide player
    hide erik
    hide erikl
    return

label button_erik_girlfriend_stolen:
    show erik 1 at right
    show player 10 at left
    player_name "{b}Erik{/b}, about {b}June{/b}..."
    show player 5
    show erik 5
    eri "Yeah?"
    show player 10
    show erik 2
    if player.location == L_school_scienceclassroom:
        show erikl 2 at right
    with dissolve
    player_name "Well, I don't think it's going to work out..."
    show player 5
    show erik 3b
    if player.location == L_school_scienceclassroom:
        show erikl 1f at right
    with dissolve
    eri "Why? What happened?"
    show player 10
    show erik 3c
    player_name "Well, we spoke for a while..."
    show player 5
    show erik 3
    eri "And?"
    show player 10
    show erik 3c
    player_name "I just don't think she's that interested..."
    show player 5
    show erik 3
    eri "Oh..."
    show erik 3b
    eri "It's alright."
    eri "I knew she wouldn't want to anyway..."
    show player 10
    show erik 3b
    player_name "She, uh... she might be coming over to my house later."
    show player 5
    show erik 5
    eri "What?!"
    show player 10
    show erik 3c
    player_name "I'm sorry!"
    player_name "While I was talking to her, one thing led to another..."
    player_name "We're just going to hang out..."
    show player 5
    eri "..."
    player_name "..."
    show player 10
    player_name "I'll, uh, talk to you later, then."
    hide player
    hide erik
    hide erikl
    with dissolve
    return

label button_erik_girlfriend_intro:
    show player 14 at left
    show erik 1 at right
    player_name "Hey, who's that girl you said you like again?"
    show erik 4
    show player 1
    eri "{b}June{/b}?"
    show player 14
    show erik 1
    player_name "Yeah, where does she hang around?"
    show player 1
    show erik 4
    eri "She usually spends her time at {b}school{/b} in the {b}computer room{/b} on the second floor..."
    show player 14
    show erik 1
    player_name "Ah, okay!"
    player_name "I'll see what I can do."
    show player 1
    return

label button_erik_message_from_dad:
    show erik 52 at right
    show player 10 at left
    player_name "I was at the Police station not too long ago..."
    show player 5
    show erik 5
    eri "Oh yeah?"
    show erik 52
    show player 10
    player_name "I saw that {b}Larry{/b} guy. You know, {b}Mrs. Johnson's ex-husband{/b}?"
    show player 11
    show erik 3b
    eri "Ugh. I don't really want to think about him..."
    show erik 52
    show player 10
    player_name "Well, he's locked up and he asked me to apologize to {b}Mrs. Johnson{/b} for him."
    show player 5
    show erik 53
    eri "For real?"
    show erik 52
    show player 10
    player_name "Yeah. He just wants to say he's sorry and he hopes that one day she'll forgive him."
    player_name "... I don't know if I should even bother telling her. What do you think?"
    show player 11
    show erik 2
    if player.location == L_school_scienceclassroom:
        show erikl 2 at right
    with dissolve
    eri "..."
    show erik 3
    if player.location == L_school_scienceclassroom:
        show erikl 1f at right
    with dissolve
    show player 5
    eri "Yeah, I dunno either. I don't think it will do much good, she really hates him..."
    show erik 3b
    show player 13
    eri "I'll let her know, dude."
    show erik 52
    show player 14
    player_name "That works for me. Thanks, {b}Erik{/b}!"
    hide player
    hide erik
    hide erikl
    with dissolve
    return


label button_erik_mrsj_poker_lost:
    show player 14 at left
    show erik 1 at right
    player_name "Hey, you know that thing we did with {b}Mrs. Johnson{/b} after the poker game?"
    show erik 3
    show player 11
    eri "Oh, yeah..."
    show erik 3b
    eri "I hope you don't think she is crazy or anything..."
    show erik 1
    show player 14
    player_name "No, of course not!"
    show player 17
    player_name "I think she's awesome!"
    show player 14
    player_name "But... I just wanted to be sure that you were okay with it, you know?"
    show erik 7
    if player.location == L_school_scienceclassroom:
        show erikl 6 at right
    with dissolve
    show player 1
    eri "It's fine, really."
    show erik 5
    if player.location == L_school_scienceclassroom:
        show erikl 1f at right
    with dissolve
    eri "She's always been very touchy with me."
    eri "I've never been close to other girls."
    show player 4
    eri "I think she does it because she feels bad about me being alone all the time..."
    show erik 1
    show player 14
    player_name "How about a girlfriend?"
    show erik 3
    show player 11
    eri "Who would want to hook up with me?"
    show erik 3b
    eri "I'm terrible at talking to girls..."
    show erik 2
    if player.location == L_school_scienceclassroom:
        show erikl 2 at right
    show player 5
    eri "*Sigh*"
    show player 14
    player_name "Maybe someone from school you have things in common with?"
    show erik 3b
    if player.location == L_school_scienceclassroom:
        show erikl 1f at right
    show player 1
    eri "I guess..."
    show erik 1
    show player 14
    player_name "Would you prefer to do stuff with {b}Mrs. Johnson{/b}?"
    show erik 5
    show player 1
    eri "Like what?"
    show erik 1
    show player 14
    player_name "Like... sex? Have you thought about it?"
    show erik 5
    show player 1
    eri "Seems easier... she already gives me lots of attention."
    show erik 1
    show player 14
    player_name "Oh, yeah? What do you mean?"
    show erik 5
    show player 11
    eri "Like touching me... letting me play with her..."
    eri "Something like what we did after the poker game."
    show erik 1
    show player 10
    player_name "I knew you were breastfeeding, but I didn't know you were going that far."
    show erik 4
    show player 11
    eri "I think she likes it."
    show erik 1
    show player 14
    player_name "Do you think she would do more with us?"
    show erik 5
    show player 4
    eri "I don't know... Maybe?"
    show erik 1
    show player 14
    player_name "We could always talk to {b}Mrs. Johnson{/b} about it?"
    show erik 5
    show player 1
    eri "I don't know if we should..."
    show erik 1
    show player 14
    player_name "Why not?"
    player_name "Maybe she wants to..."
    show erik 5
    show player 1
    eri "Maybe?"
    show erik 1
    show player 4
    player_name "Hmm..."
    show erik 4
    show player 1
    eri "Do you think you could ask her?"
    show erik 1
    show player 23
    player_name "Me?!"
    show erik 4
    show player 11
    eri "Yeah!"
    eri "It's pretty awkward for me to ask, you know?"
    show erik 1
    show player 29
    player_name "I'll' try to bring it up and see what she says..."
    show player 1
    return

label button_erik_breastfeeding_in_person:
    show erik 1 at right
    show player 10 at left
    player_name "I didn't know you and {b}Mrs. Johnson{/b} were... so close."
    show player 5
    show erik 3
    eri "It's weird, I know..."
    show erik 2
    if player.location == L_school_scienceclassroom:
        show erikl 2 at right
    with dissolve
    show player 12
    player_name "No, not at all!"
    show player 10
    player_name "I...I think it's cool!"
    show player 13
    show erik 3b
    if player.location == L_school_scienceclassroom:
        show erikl 1f at right
    with dissolve
    eri "..."
    show player 29 with dissolve
    player_name "I mean, {b}Mrs. Johnson{/b} is like... really hot!"
    player_name "I think you're kind of lucky..."
    show player 13 with dissolve
    show erik 3
    eri "I guess so."
    show player 12
    player_name "You guys do... anything else together?"
    show player 11
    show erik 5
    eri "...NO!!"
    show erik 3
    eri "She just, you know, let's me touch her a lot..."
    show erik 3b
    show player 23
    player_name "Really?!"
    player_name "Like... her whole body?"
    show player 14
    show erik 5
    eri "Well, sort of."
    show erik 50
    show player 12
    player_name "Don't you like it?"
    show player 13
    show erik 5
    eri "Of course!"
    show erik 50
    show player 33
    player_name "I know I would!"
    show player 13
    show erik 5
    eri "Just...please don't tell anyone alright?"
    show erik 50
    show player 14
    player_name "{b}Erik{/b}, you're my best friend."
    player_name "I'll keep this between us."
    player_name "I was just... surprised, you know?"
    show player 13
    show erik 5
    eri "Thanks, {b}[firstname]{/b}. You're a good friend."
    hide player
    hide erik
    hide erikl
    with dissolve
    return

label button_erik_favor_completed:
    show erik 1 at right
    show player 17 at left
    player_name "I have it!"
    show erik 4 at right
    show player 1 at left
    eri "Oh yeah?"
    show erik 1 at right
    show player 33 at left
    player_name "A brand new copy of {b}Sea Dogs SAGA{/b}!"
    show player 239_240
    pause
    show erik 4 at right
    show player 72 at left
    eri "No way!"
    show erik 8 at right
    if player.location == L_school_scienceclassroom:
        show erikl 8 at right
    with dissolve
    show player 1 at left
    eri "Thanks, {b}[firstname]{/b}!"
    show erik 9 at right
    show player 14 at left
    player_name "Sooo... Are you gonna talk to {b}Kevin{/b}?"
    show erik 10 at right
    show player 1 at left
    eri "Yeah. I'll take over his cafeteria duties."
    show erik 9 at right
    show player 36 at left
    player_name "Great! Thanks {b}Erik{/b}!"
    return

label button_erik_ask_favor:
    show erik 1 at right
    show player 29 at left
    player_name "I need a favor, actually!"
    show erik 5 at right
    show player 13 at left
    eri "Oh yeah?"
    eri "What is it?"
    show erik 1 at right
    show player 14 at left
    player_name "Well, you know {b}Kevin{/b} from {b}school{/b}?"
    show erik 5 at right
    show player 1 at left
    eri "Sort of..."
    show erik 1 at right
    show player 17 at left
    player_name "Ok, well. He's on cafeteria duty for another two months..."
    player_name "...And he really needs a replacement."
    show erik 2 at right
    show player 11 at left
    if player.location == L_school_scienceclassroom:
        show erikl 2 at right
    with dissolve
    eri "Ugh. I {b}HATE{/b} cafeteria duty..."
    show erik 3 at right
    if player.location == L_school_scienceclassroom:
        show erikl 1f at right
    with dissolve
    show player 10 at left
    player_name "Look, you don't have to do it..."
    show player 14 at left
    player_name "...But if you do, I'll get you whatever you want!"
    player_name "Is there anything at all?"
    show erik 1 at right
    show player 1 at left
    eri "Hmm..."
    show erik 4 at right
    show player 11 at left
    eri "Well, you could get me this new game that just came out I guess..."
    show erik 1 at right
    show player 2 at left
    player_name "What's it called?"
    show erik 4 at right
    show player 1 at left
    eri "It's called: {b}Sea Dogs SAGA{/b}"
    eri "...it's in store at {b}COSMIC CUMICS{/b} already..."
    show erik 1 at right
    show player 18 at left
    player_name "Ok! So if I get it, you'll do it?"
    show erik 3 at right
    show player 2 at left
    eri "Yeah... I guess."
    show erik 1 at right
    show player 14 at left
    player_name "Awesome!!!"
    return

label button_erik_where_is_mrsj:
    if player.location == L_school_scienceclassroom:
        show erik 1 at right
        show erikl 1f at right
        with dissolve
    else:
        show erik 1 at right
    show player 35 at left
    player_name "Where's {b}Mrs. Johnson{/b}?"
    show erik 5 at right
    show player 34 at left
    eri "... Eh, she's normally around the house somewhere. Except in the {b}afternoons{/b} when she's teaching yoga at the {b}Gym{/b}."
    show player 1 at left
    show erik 1 at right
    show player 14 at left
    player_name "Ah, I see."
    return

label button_erik_not_much:
    if player.location == L_school_scienceclassroom:
        show erik 1 at right
        show erikl 1f at right
        with dissolve
    else:
        show erik 1 at right
    show player 2 at left
    player_name "Oh, not much."
    show player 17 at left
    player_name "Just dropping by to say hi!"
    show erik 5 at right
    show player 1 at left
    eri "Is everyone alright at your new place?"
    show erik 1 at right
    show player 10 at left
    player_name "{b}[deb_name]'s{/b} been getting {b}weird phone calls{/b} but she say's everything's fine so..."
    show player 24 at left
    player_name "I think we'll be alright..."
    show erik 5 at right
    show player 13 at left
    eri "That's odd..."
    show erik 5 at right
    show player 24 at left
    player_name "Yeah, I know..."
    show player 36 at left
    player_name "Anyway, I'd better get going."
    show erik 7 at right
    if player.location == L_school_scienceclassroom:
        show erikl 6 at right
    with dissolve
    eri "Alright, then. See ya!"
    hide player
    hide erikl
    hide erik
    with dissolve
    return

label button_erik_webcam_help:
    show player 29 at left
    show erik 1 at right
    player_name "By the way... I need help with something tonight..."
    show erik 5
    eri "Oh yeah? What is it?"
    show player 21
    show erik 1
    player_name "It's gonna sound a bit crazy, but I need help sneak into school tonight..."
    show player 13
    show erik 5
    eri "What?"
    eri "...But why?"
    show player 10
    show erik 1
    player_name "All you need to know is this will help me catch up with school..."
    show player 108f
    player_name "...And I can't afford to fail, I really need to do it."
    show player 5
    show erik 3
    eri "Hmm..."
    eri "I don't know about this... Sounds like trouble."
    show player 10
    show erik 1
    player_name "Please?"
    show player 13
    show erik 5
    eri "I guess I can help..."
    show player 17
    show erik 1
    player_name "Sweet!!!"
    show player 14
    player_name "Alright, meet me at school tonight!"
    show player 1
    show erik 4
    eri "Okay."
    hide erik
    hide erikl
    hide player
    return

label button_erik_ask_model:
    show player 10 at left
    show erik 1 at right
    player_name "I'm working on a project for {b}Miss Ross{/b} and it requires a live model."
    player_name "Would you be interested?"
    show player 11
    show erik 5
    eri "Uhh, You really think I would make a good model?"
    show player 10
    show erik 1
    player_name "Hmm, no... Probably not."
    show player 2
    player_name "I'll look elsewhere."
    show player 1
    show erik 4
    eri "Good luck, dude."
    return

label button_erik_path_split:
    show player 14 at left
    show erik 1 at right
    player_name "What should I ask {b}Mrs. Johnson{/b} again?"
    show erik 5
    show player 1
    eri "Find out if she wants to do more stuff with us?"
    show player 14 at left
    show erik 1
    player_name "Oh, right."
    player_name "I'll let you know once I talk to her."
    show player 1
    show erik 1
    return

label erik_funky_block:
    scene expression game.timer.image("erik_inside{}_b")
    show player 10 with dissolve
    player_name "Well... I guess I should leave {b}Erik{/b} alone for a while."
    hide player with dissolve
    $ game.main()

label button_erik_talked_to_roxxy_booze:
    show erik 1 at right
    if player.location == L_school_scienceclassroom:
        show erikl 1f at right
    show player 10 at left
    player_name "{b}Roxxy{/b} asked me to get some drinks for her and her friends."
    player_name "You wouldn't mind if I took some of {b}Mr. Johnson's{/b} beer out of the basement, would you?"
    show player 5
    show erik 5
    eri "You want me to provide {b}Roxxy{/b} and her friends with alcohol?!"
    show erik 52
    show player 10
    player_name "Err... Yeah?"
    show player 5
    show erik 5
    eri "No way, dude!"
    eri "Do you realize how much grief they give me at school?!"
    show erik 52
    show player 24
    player_name "Yeah I know, man..."
    show player 14
    player_name "Think of this as a chance to get on their good side!"
    show player 13
    show erik 5
    eri "Hmm, no thanks!"
    show player 5
    eri "I'm pretty sure all their sides are equally bad."
    show erik 52
    player_name "..."
    show player 10
    player_name "Alright, I understand. Thanks anyways."
    show player 5
    show erik 5
    eri "I'm sorry, {b}[firstname]{/b}."
    eri "You know I'll do anything for you, dude."
    eri "Just... I don't wanna get involved with {b}Roxxy{/b}."
    show erik 52
    show player 14
    player_name "No worries."
    player_name "I'll figure something else out."
    show player 5f with dissolve
    if player.location == L_school_scienceclassroom:
        show erikl 2 at right
    show erik 2
    with dissolve
    eri "..."
    if player.location == L_school_scienceclassroom:
        show erikl 1f at right
    show erik 5
    with dissolve
    eri "Oh, wait!"
    show erik 52
    show player 5 with dissolve
    player_name "Hmm?"
    show erik 5
    eri "What about a fake ID?"
    show erik 52
    show player 10
    player_name "A fake ID?!"
    player_name "What do you know about fake ID's, {b}Erik{/b}?!"
    show player 5
    show erik 3
    eri "Oh, uhh..."
    eri "I kinda..."
    show erik 3b
    eri "... Sorta, looked into it a few years ago..."
    show erik 52
    show player 12
    player_name "Why in the heck would you need a fake ID?"
    show player 5
    show erik 3
    eri "... For this video game I wanted."
    if player.location == L_school_scienceclassroom:
        show erikl 2
    show erik 2
    with dissolve
    show player 11
    player_name "..."
    if player.location == L_school_scienceclassroom:
        show erikl 1f at right
    show erik 3
    with dissolve
    eri "An adult game."
    show erik 52
    show player 14
    player_name "Are you telling me you have a fake ID?"
    show player 13
    show erik 5
    eri "No!"
    show player 5
    eri "Heh, I uhh.. Couldn't afford it."
    show erik 4
    eri "... But I know where you can get one!"
    show erik 1
    show player 14
    player_name "Alright, where?"
    show player 13
    show erik 5
    eri "I read about it online."
    eri "There's a guy down at {b}the pier{/b} that makes them for $400."
    show erik 52
    show player 35
    player_name "Hmm, down at {b}the pier{/b}, huh?"
    show player 14
    player_name "Alright, I'll look into it."
    show player 13
    show erik 4
    eri "Good luck, dude!"
    hide erik
    hide erikl
    with dissolve
    show player 14
    player_name "I should {b}head back to Roxxy{/b} and see what she thinks about all this."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
