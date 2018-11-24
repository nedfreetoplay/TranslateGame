label harold_police_office_dialogue_mia_route:
    show harold 1 at right
    show player 14 at left
    with dissolve
    player_name "Hey, {b}Harold{/b}!"
    show player 13
    show harold 2
    harold "There's my man!"
    show harold 1
    show player 14
    player_name "How are things going lately?"
    show player 13
    show harold 2
    harold "Never been better! Our family is the happiest it's ever been!"
    harold "{b}Helen{/b} has really changed. Really... changed."
    harold "Things are red hot in the bedr-"
    show harold 4
    harold "Anyway, you know what I mean."
    show harold 1
    show player 21
    player_name "Heh heh... Yeah, I suppose..."
    show player 13
    show harold 2
    harold "I should get back to work."
    harold "Feel free to stop by the house anytime, kiddo!"
    show harold 1
    show player 14
    player_name "Thanks, {b}Harold{/b}!"
    player_name "See you later."
    return

label harold_police_office_dialogue_helen_route_split:
    show player 22f at right
    show harold 51 at left
    with dissolve
    pause
    show harold 52
    show yum 12f at Position (xpos=395)
    with dissolve
    yum "!!!"
    show player 5f
    yum "Oh! I didn't see you there..."
    show yum 14f at Position (xpos=382) with dissolve
    show harold 53
    harold "Don't worry, {b}Yumi{/b}, it's just my daughter's little buddy."
    show harold 52
    show player 10f
    player_name "Hello..."
    show player 5f
    show yum 13f
    yum "Hi... Oh! I forgot I have something I... need to take care of in my office."
    hide yum
    show harold 54
    with dissolve
    harold "..."
    show harold 55
    harold "Sorry you had to see that, kiddo."
    harold "{b}Yumi{/b} is more of a hands on partner..."
    harold "Thought I'd try and teach her a couple things..."
    show harold 54
    show player 11f
    player_name "..."
    show player 10f
    player_name "So you and {b}Helen{/b}..."
    show player 5f
    show harold 55
    harold "Look. That ship has sailed, kiddo. {b}Helen{/b} seems to have accepted our separation."
    harold "I figured I'd better move on too."
    harold "To tell you the truth."
    harold "I've never been happier, and I've started seeing someone else."
    show harold 54
    show player 12f
    player_name "I wonder who..."
    show player 10f
    player_name "At least you're happy..."
    show player 5f
    pause
    show player 10f
    player_name "But how is {b}Mia{/b} handling this? Is she going to be alright?"
    show player 5f
    show harold 55
    harold "I'm not giving up on {b}Mia{/b}."
    harold "I visit her every day. She's my tough little girl."
    harold "She always has been after having to put up with {b}Helen{/b} and I."
    harold "She'll be alright."
    show harold 54
    show player 12f
    player_name "Good."
    show player 5f
    show harold 55
    harold "You're a good kid, {b}[firstname]{/b}. Thanks again for caring about my daughter."
    harold "I appreciate you and her trying to get me back with {b}Helen{/b}..."
    harold "It's just some things just don't work out..."
    show harold 54
    show player 21f
    player_name "Heh heh..."
    player_name "You're welcome."
    show player 5f
    show harold 55
    harold "Don’t be afraid to visit me if there is anything you need help with."
    show harold 54
    show player 36f with dissolve
    player_name "Will do. Goodbye, {b}Harold{/b}."
    return

label harold_police_office_dialogue_mia_harold_backup:
    show harold 1 at Position (xpos=762)
    show player 23 at left
    with dissolve
    player_name "{b}Harold{/b}!!"
    show player 22
    show harold 6
    harold "What's going on?? Did you find {b}Yumi{/b}?"
    show harold 1
    show player 38 with dissolve
    player_name "Yes! But she needs your help, now!!"
    show player 3 with dissolve
    show harold 3
    harold "What?!"
    show harold 1
    show player 10 with dissolve
    player_name "In the cell! {b}Yumi{/b}... She's struggling with an inmate!!"
    show player 5
    show harold 29
    harold "!!!"
    show harold 30 at right with dissolve
    harold "I... I should call for more backup. Maybe I should tell {b}Earl{/b} first-"
    show player 12
    player_name "{b}Harold{/b}! There's no time!"
    hide harold
    show harold 25 at Position (xpos=762)
    with dissolve
    player_name "You have to take control of the situation."
    show player 11
    show harold 26
    harold "But I should tell {b}Earl{/b} first..."
    harold "...I haven't dealt with inmates in a long time and-"
    show harold 25
    show player 15
    player_name "{b}Yumi{/b}'s your partner and needs your help!"
    player_name "You have to go! NOW!!!"
    show player 16
    show harold 24
    harold "..."
    show harold 6
    harold "You're right. I should take action."
    harold "Let's go."
    return

label harold_police_office_dialogue_mia_harolds_thoughts:
    show harold 1 at right
    show player 36 at left
    with dissolve
    player_name "Hi, {b}Harold{/b}."
    show player 13 with dissolve
    show harold 2
    harold "Hello again, kiddo."
    show harold 1
    show player 14
    player_name "Thought I'd stop by and see how dinner was with {b}Mia{/b} and {b}Helen{/b}."
    show player 13
    show harold 6
    harold "Oh... Umm... It was alright I guess. The food was really good."
    show harold 1
    show player 10
    player_name "Do you think things have...gotten better between {b}Helen{/b}...and you?"
    show player 5
    show harold 4
    harold "..."
    show harold 6
    harold "I know {b}Mia{/b} is trying to get {b}Helen{/b} and I back together."
    harold "You've been helping her too. You're a good kid."
    show harold 1
    harold "..."
    show harold 6
    harold "I suppose things between {b}Helen{/b} and I are better than when you saw us erupt at each other."
    show harold 4
    pause
    harold "I... just don't know though..."
    show harold 1
    pause
    show player 10
    player_name "Why don't you know?"
    show player 5
    show harold 26
    harold "Oh, kiddo."
    harold "We may be on good terms now, but we could be at each other's throats again."
    harold "For once, I'm thinking I might be happier on my own."
    harold "My marriage might be better left behind me."
    harold "Maybe... if {b}Helen{/b} really changed for good."
    harold "It might be possible for us to get back together."
    show harold 1
    show player 14
    player_name "I... I understand."
    show player 13
    show harold 6
    harold "I'd better get back to work. I just had another breakthrough on a case."
    show harold 2
    harold "See you later, {b}[firstname]{/b}."
    show harold 1
    show player 14
    player_name "Bye, {b}Harold{/b}."
    show player 13
    hide harold with dissolve
    pause
    show player 14
    player_name "( Sounds like {b}Harold's{/b} telling me there's a chance he'd get back with {b}Helen{/b}. )"
    show player 35
    player_name "( Maybe {b}Sister Angelica{/b}'s training is actually helping her and {b}Harold{/b}. )"
    show player 10
    player_name "( But... he sure seems happy right now without {b}Helen{/b}... )"
    player_name "( {b}Mia{/b} would be devastated if he didn't get back with {b}Helen{/b}. )"
    show player 5
    player_name "..."
    show player 12
    player_name "( I guess it's not really up to me at this point... )"
    player_name "( Might as well finish helping {b}Sister Angelica{/b}. )"
    show player 35
    player_name "( What did she want again? )"
    hide player with dissolve
    return

label harold_police_office_dialogue_roxxy_ask_earl_release:
    scene police_c_2
    show harold 1 at right
    show roxxy 1of at Position (xpos=400)
    show player 10 at left
    with dissolve
    player_name "Hey, umm..."
    player_name "My {b}friend's mother{/b} was taken into custody earlier today and we need to find out what's going on."
    show player 5
    show harold 2
    harold "Hmm?"
    show harold 2
    harold "Oh, you must be {b}Crystal's{/b} daughter!"
    show harold 1
    show roxxy 33f
    rox "... Yes."
    show roxxy 32f
    show harold 2
    harold "Sheesh, you're the spitting image of her in her younger days!"
    show harold 1
    rox "..."
    show player 10
    player_name "Uhh, could you tell us why you're holding her?"
    show player 5
    show harold 2
    harold "Sorry, kiddos."
    harold "A drug bust this big is way above my pay grade."
    harold "You'll have to speak with the chief if you want the details."
    show harold 1
    show player 10
    player_name "... Oh."
    player_name "Alright, thanks."
    show player 5
    hide harold with dissolve
    pause
    show roxxy 2c at center
    show roxxy 2c at Position (xoffset=-33)
    with dissolve
    rox "Oh my God... They must have found {b}Clyde's{/b} entire stash!"
    show roxxy 2b at Position (xoffset=-33)
    show player 12
    player_name "Just how much meth does your cousin have anyways?!"
    show player 5
    show roxxy 1j with dissolve
    rox "..."
    show roxxy 1l
    rox "I... Uhh..."
    rox "... I'm not sure."
    show roxxy 1j
    show player 12
    player_name "Well I guess we'd best go speak with {b}the chief{/b}."
    hide player
    hide roxxy
    with dissolve
    return

label harold_police_office_dialogue_pre:
    show player 1 at left
    show harold 2 at right
    with dissolve
    harold "Oh, hey, it's you again. Need something?"
    show harold 1
    show player 14
    player_name "Hi, I just had some questions."
    show player 1
    return

label harold_police_office_dialogue_wheres_mia:
    show player 14
    player_name "I was just wondering: do you know where {b}Mia{/b} is?"
    show player 11
    show harold 2
    harold "I'm sorry, I can't help you right now; we're busy with a new case..."
    harold "But, she should be at school or at home."
    show harold 1
    show player 14
    player_name "Okay. Thanks, Sir!"
    return

label harold_police_office_dialogue_the_chief:
    show player 12
    player_name "Who's {b}the chief{/b}?"
    show player 5
    show harold 2
    harold "Oh, you want {b}Earl{/b}."
    show player 13
    harold "He's right over there on the other side of the office."
    show harold 1
    show player 14
    player_name "Gotcha, thanks!"
    return

label harold_police_office_dialogue_larry:
    show player 10
    player_name "What did you need me to ask {b}Larry{/b}?"
    show player 5
    show harold 6
    harold "{b}Larry{/b} isn't giving up the location of the goods."
    show harold 1
    show player 33
    player_name "Oh yeah!"
    show player 12
    player_name "I'll talk with him. I know his wife."
    player_name "If I can't get the location out of him, maybe I can get {b}Mrs. Johnson{/b} to help us."
    show player 5
    show harold 2
    harold "Thanks, {b}[firstname]{/b}."
    return

label harold_police_office_dialogue_thief:
    show player 10
    player_name "What did you need me to do if I see the thief again?"
    show player 5
    show harold 6
    harold "If you notice him, give me a call directly."
    show harold 1
    show player 12
    player_name "Of course! I'll keep an eye out for him."
    player_name "He is always sneaking into my neighbor's, {b}Mrs. Johnson's{/b}, yard at night."
    show player 5
    show harold 6
    harold "There have also been reports of him near the park as well. If you happen to notice him there, keep me in the loop."
    show harold 1
    show player 12
    player_name "Okay, I'll check there for clues as well."
    show player 5
    show harold 2
    harold "Thanks, {b}[firstname]{/b}."
    return

label harold_police_office_dialogue_donuts:
    show player 14
    player_name "What kiiind of... donuts, err... do you like?"
    show player 11
    show harold 3
    harold "Excuse me?"
    show player 14
    show harold 1
    player_name "Just wondering!"
    show player 11
    show harold 2
    harold "Look, I don't have time to chat right now, I'm swamped with work..."
    harold "... Why don't you run off to school, okay?"
    show player 10
    show harold 1
    player_name "But-"
    show player 5
    show harold 2
    harold "I have to go, sorry."
    return

label harold_police_office_dialogue_donuts_wrong:
    show player 437 at left with fastdissolve
    player_name "I err, got you something."
    show player 1
    show player 436
    harold "..."
    show player 437
    player_name "It's for you!"
    show harold 8
    show player 1
    with fastdissolve
    harold "You brought me a box of... donuts?!"
    show player 14
    show harold 7
    player_name "Yeah! I thought maybe you'd like to snack on them at work..."
    show player 1
    show harold 9
    harold "Oh..."
    harold "I'm not a big fan of that kind, to be honest."
    show player 11
    show harold 10
    player_name "..."
    show harold 11
    harold "But I err... I appreciate the thought!"
    harold "I'm sure that {b}Earl{/b} will be more than happy to have them..."
    show player 10
    show harold 10
    player_name "Alright."

    show player 5
    hide harold with dissolve
    pause
    show player 10
    player_name "( Damn! )"
    player_name "( I must've bought the wrong kind. )"
    player_name "( I have to make sure I get the right ingredients... )"
    return

label harold_police_office_dialogue_donuts_correct:
    show player 437 at left with fastdissolve
    player_name "I err, got you something."
    show player 1
    show player 436
    harold "..."
    show player 437
    player_name "It's for you!"
    show harold 8
    show player 1
    with fastdissolve
    harold "You brought me a box of... donuts?!"
    show player 14
    show harold 7
    player_name "Yeah! I thought maybe you'd like to snack on them at work..."
    show player 1
    show harold 9
    harold "Let me see..."
    harold "Holy... [harold_glaze]... with... [harold_topping]?!"
    show player 14
    show harold 7
    player_name "I thought you'd like those!"
    show player 1
    show harold 8
    harold "These are my favourite... How did you..."
    show player 17
    show harold 44
    player_name "I got lucky, I suppose."
    show player 1
    show harold 45
    harold "*Nom nom*"
    show harold 46
    harold "Well, kid, you did well."
    show player 17
    show harold 45
    player_name "Glad you like them!"
    show player 1
    harold "..."
    show player 11
    show harold 46
    harold "Wait, before you go..."
    show player 1
    harold "I know that you and {b}Mia{/b} like to... hang out, and all that stuff."
    harold "You seem like a good kid, so I'll talk to my wife and see if she can lay off a bit."
    show player 14
    show harold 45
    player_name "You mean, I can visit her now?"
    show player 1
    show harold 46
    harold "Not too fast!"
    harold "I didn't say that... but... You could probably sneak in like before and I'll try and keep my wife distracted, alright?"
    show player 14
    show harold 45
    player_name "Really?"
    show player 1
    show harold 46
    harold "I said I'll try, I can't promise you anything."
    show player 14
    show harold 45
    player_name "Thanks, {b}Harold{/b}."
    show player 1
    show harold 46
    harold "Alright, now get out of here before my boss sees us with these donuts!"
    show player 17
    show harold 45
    player_name "Ha ha."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
