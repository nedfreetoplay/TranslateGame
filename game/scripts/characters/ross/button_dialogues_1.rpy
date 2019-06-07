label button_ross_grab_clay:
    scene location_school_art_closeup
    show player 1f at right
    show ross 2 at left
    with dissolve
    ross "Go grab a slab of clay, {b}[firstname]{/b}, so we can get started."
    show player 2f
    show ross 1
    player_name "Yes, Ma'am."

    return

label button_ross_find_partner:
    scene location_school_art_closeup
    show player 2f at right
    show ross 1 at left
    with dissolve
    player_name "Hey, {b}Miss Ross{/b}. You ready to get started?"
    show player 1f
    show ross 2
    ross "Hey there, {b}[firstname]{/b}! Just about..."
    show ross 11 with dissolve
    ross "I actually wanted to discuss something with you first."
    show player 2f
    show ross 10
    player_name "Oh?"
    show ross 11
    show player 1f
    ross "I think we should get you a partner for these sessions, what do you think?"
    show ross 10
    show player 10f
    player_name "A partner?"
    show ross 11
    show player 11f
    ross "Yeah, somebody to work along side you and bounce idea's back and forth!"
    show ross 10
    show player 2f
    player_name "Sure, okay."
    player_name "Did you have anyone in mind?"
    show player 1f
    show ross 10b with dissolve
    ross "Hmm..."
    show ross 11 with dissolve
    ross "Well my initial thought is {b}Eve{/b}. She's a talented artist just like yourself..."
    ross "... But I doubt she'd have time with all her musical studies."
    show ross 10b with dissolve
    pause
    show ross 11 with dissolve
    ross "Do you think {b}Mia{/b} would be interested?"
    ross "She's just such a cutie pie, isn't she!?"
    show ross 10
    show player 2f
    player_name "Err, yeah. I suppose."
    show player 1f
    show ross 11
    ross "Great! Well why don't you go talk to her?"
    ross "Tell her I said to get her cute butt in here!"
    show player 11f
    show ross 10
    player_name "..."

    return

label button_ross_ask_mia_partner:
    scene location_school_art_closeup
    show player 1f at right
    show ross 2 at left
    with dissolve
    ross "{b}[firstname]{/b}, you're back!"
    ross "Where's {b}Mia{/b}?"
    show player 10f
    show ross 1
    player_name "Oh, uhh... I haven't convinced her yet."
    show player 11f
    show ross 2
    ross "Well get a move on, {b}[firstname]{/b}!"
    ross "We need her enthusiasm if we're gonna win this thing!"
    return

label button_ross_mia_is_partner:
    scene location_school_art_closeup
    show player 1f zorder 1 at right
    show ross 2 at left
    show mia 7 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    ross "Hey there, Cutie Pie!"
    show ross 1
    show mia 56 at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "... Oh, umm. H-hello."
    show ross 2
    show mia 55
    ross "I'm so glad, {b}[firstname]{/b} convinced you to join us!"
    show ross 1
    show mia 56
    mia "Hehe, yeah... He said you guys really needed my help?"
    show ross 2
    show mia 55
    ross "We surely do!"
    show ross 1
    show player 2f
    show mia 8b at Position(xpos=0.65, ypos=1.0) with dissolve
    player_name "So are we ready to start now?"
    show player 1f
    show ross 11 with dissolve
    ross "Yup! Why don't you both get out your art pads and have a seat opposite each other."
    show player 2f
    show ross 10
    player_name "Okay."
    show mia 8
    show player 596f with dissolve
    mia "..."
    show mia 12
    mia "Umm, question..."
    show mia 8
    show ross 11
    ross "Yes, Dear?"
    show mia 12
    show ross 10
    mia "What if I don't have an art pad?"
    show mia 8
    show ross 25
    ross "Oh, right."
    show ross 25b
    ross "Well usually I'd provide you with one of those..."
    show ross 25
    ross "... But I'm afraid we've exhausted our stores."
    show ross 24
    show player 598f
    player_name "That sucks!"
    show player 596f
    show mia 12b
    mia "Oh well, it's no big deal. I'm not very good at drawing anyways..."
    show mia 10
    mia "I'll just watch."
    show mia 7
    show ross 11
    ross "Nonsense!"
    ross "We'll get you one!"
    show ross 27 with dissolve
    ross "{b}[firstname]{/b}, why don't you go ask {b}Eve{/b} if we can borrow one of hers."
    show ross 26
    show player 598f
    player_name "... Y-yeah, okay!"
    show ross 27
    show player 596f
    ross "See, {b}[firstname]{/b} to the rescue!"
    show player 1f
    show ross 11
    with dissolve
    ross "We'll just stay here and have some girl talk."
    show ross 13
    ross "Right, Cutie Pie?"
    show ross 12
    show mia 56 at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "Heh, okay..."
    show mia 55
    show player 2f
    player_name "Be right back."
    return

label button_ross_find_art_pad:
    scene location_school_art_closeup
    show ross 13 at left
    show mia 55 at Position(xpos=0.435, ypos=1.0)
    show player 1f at right
    with dissolve
    ross "... You know, {b}Mia{/b}. I used to be friends with a girl who looked just like you!"
    show ross 12
    show mia 56
    mia "Really?"
    show ross 13
    show mia 55
    ross "Absolutely! Her name was Starchild and we used to follow our favorite band all over the country."
    show ross 12
    show mia 12b at Position(xpos=0.45, ypos=1.0) with dissolve
    mia "Well that sounds pretty neat!"
    show ross 13
    show mia 8b
    ross "Oh, it was!"
    ross "That girl always had the best drugs!"
    show ross 11
    ross "... And what a kisser! She could do things with her tongue that woul-"
    show player 10f
    show ross 10
    show mia 55 at Position(xpos=0.435, ypos=1.0) with dissolve
    player_name "*Ahem* Am I interrupting something?"
    show player 11f
    show mia 12f with dissolve
    mia "{b}[firstname]{/b}, you're back!"
    show mia 12bf
    mia "Thank goodness!"
    show mia 8bf
    show ross 11
    ross "Did you manage to get {b}Eve's artpad{/b}?"
    show player 10f
    show ross 10
    player_name "No, sorry. I'm still working on it."
    show player 11f
    show ross 11
    ross "Tsk, well shoo then! We're having girl talk here..."
    show ross 10
    show player 10f
    player_name "... A-alright. I'll be back."
    hide player with dissolve
    show mia 12f at Position(xpos=0.55, ypos=1.0) with dissolve

    mia "No! Wait! Hold up!"
    show mia 8f
    pause
    show ross 13 at Position(xpos=0.15, ypos=1.0) with dissolve
    ross "Now where was I?"
    show ross 12
    show mia 8b with dissolve
    mia "..."
    show ross 13
    ross "Oh, right! She could do things with her tongue that would make a whore blush!"
    show ross 12
    show mia 56 at Position(xpos=0.535, ypos=1.0) with dissolve
    mia "... Oh my."
    return

label button_ross_found_art_pad:
    scene location_school_art_closeup
    show ross 46 at left
    show mia 55 at Position(xpos=0.435, ypos=1.0)
    show player 11f zorder 1 at right
    with dissolve
    ross "... Hmm, I think my favorite one is the {b}Praia do Abricó{/b}"
    show ross 11 with dissolve
    ross "It's back home in Rio de Janeiro."
    show ross 10
    show mia 56
    mia "Oh, I dunno..."
    mia "... I don't think I'm brave enough for a nude beach."
    show ross 13
    show mia 55
    ross "Oh, sure you are, Cutie Pie!"
    ross "Nobody should be ashamed of their body. The human form is a work of art after all..."
    show ross 13
    ross "... Especially yours."
    ross "You're just absolutely gorgeous, {b}Mia{/b}!"
    show ross 12
    show mia 56
    mia "Wow, I... Uhh..."
    show player 10f

    player_name "{b}*Ahem*{/b}"
    show player 11f
    show mia 12bf with dissolve
    mia "Oh, {b}[firstname]{/b}, thank goodness you're back!"
    show mia 8b zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve
    show player 2f
    player_name "You guys having fun?"
    show player 1f
    show ross 11
    ross "We're having a blast!"
    ross "I assume you got the {b}Art Pad{/b}?"
    show ross 10
    show player 598f with dissolve
    player_name "Yup, I got it right here."
    show player 596f
    show ross 11 with dissolve
    ross "Good work, {b}[firstname]{/b}!"
    ross "We should get started now."
    ross "I want both of you to take a seat opposite one another."
    show ross 58 with dissolve
    ross "... Because today you're going to be drawing portaits of each other using pencil and paper."
    show player 598f
    show ross 10 with dissolve
    player_name "So you want me to draw {b}Mia{/b}?"
    show player 596f
    show ross 11
    ross "That's right and {b}Mia{/b}, I want you to draw {b}[firstname]{/b}."
    show ross 10
    show mia 12b
    mia "I'll try..."
    show ross 13
    show mia 8b
    ross "You're just too adorable aren't you?"
    show ross 12
    show mia 55 at Position(xpos=0.635, ypos=1.0) with dissolve
    ross "Don't worry, there's no such thing as bad art!"
    show mia 56
    mia "... If you say so."
    show mia 55
    show ross 11
    ross "Now let's get started."


    scene location_school_art_cutscene06
    with fade
    show text "I always did enjoy art but drawing a live model was a totally different experience..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... I'm glad {b}Miss Ross{/b} had chosen {b}Mia{/b} as my partner for this." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "She really was cute!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_school_art_closeup
    show player 1 zorder 1 at left
    show mia 8b at right
    show ross 11f zorder 0 at Position(xpos=0.535, ypos=1.0)
    with dissolve
    ross "Well done, both of you!"
    ross "It's such a beautiful drawing, {b}[firstname]{/b}!"

    show ross 28f at Position(xpos=0.435, ypos=1.0) with dissolve
    ross "I'm feeling very good about our chances in this art contest..."
    ross "You should show {b}Mia{/b}."
    show ross 12 at Position(xpos=0.35, ypos=1.0)
    show player 560
    with dissolve

    pause
    show mia 69
    mia "*gasp*"
    show mia 10
    mia "Wow! It's so good!"
    show mia 7
    show ross 11
    ross "Isn't it!?"
    show ross 13
    ross "It's almost as beautiful as the real thing!"
    show ross 13c
    ross "Don't you think, {b}[firstname]{/b}?"
    show player 561
    show ross 12b
    player_name "Y-yeah, almost..."

    show player 560
    show ross 12
    show mia 56 with dissolve
    mia "Aww, thanks {b}[firstname]{/b}."
    show mia 55
    show ross 13
    ross "Alright then, let's see how you did {b}Mia{/b}?"
    show mia 59b with dissolve
    mia "Mmm, no. That's okay. I'd rather not."
    show ross 11
    show mia 59d
    ross "Oh, pish posh! Don't play so hard to get!"
    ross "Remember, there's no such thing as bad art..."
    show ross 10
    show mia 59e
    mia "... Okay."
    show mia 59c
    show ross 24

    ross "..."
    show mia 59
    mia "I told you, I'm not very good..."
    show mia 59c
    show ross 25
    ross "Well no, it's -- Interesting..."
    show ross 11
    ross "There's definitely room for improvement."
    show player 561
    show ross 10
    player_name "I like it, {b}Mia{/b}!"
    show player 560
    show mia 57
    mia "You do?"
    show player 561
    show mia 58
    player_name "Yeah, it's really cute!"

    show player 560
    show ross 11
    ross "There, now see, {b}Mia{/b}. {b}[firstname]{/b} likes it!"
    show ross 10
    mia "..."
    show ross 11
    ross "Well, I think we had better call it there for today."
    ross "We made some really good progress, you two!"
    show ross 58 at Position(xpos=0.41, ypos=1.0) with dissolve
    ross "Make sure you both get lots of rest and don't forget to do those meditations I taught you!"
    show ross 10 at Position(xpos=0.35, ypos=1.0) with dissolve
    show player 2
    with dissolve
    player_name "Alright, I'll try, {b}Miss Ross{/b}."
    player_name "See ya, {b}Mia{/b}!"
    show player 1
    show mia 56 with dissolve
    mia "Bye, {b}[firstname]{/b}."
    return

label button_ross_collage:
    scene location_school_art_closeup
    show player 2f zorder 1 at right
    show mia 2f zorder 0 at Position(xpos=0.55, ypos=1.0)
    with dissolve
    player_name "You ready for another session with {b}Miss Ross{/b}?"
    show player 1f
    show mia 6f
    mia "Yeah, I guess..."
    show player 10f
    show mia 2f
    player_name "You don't seem very excited about it."
    player_name "I thought you loved art?"
    show player 11f
    show mia 6f
    mia "I do love art."
    mia "... And I really like watching you and {b}Miss Ross{/b} work."
    show mia 6bf
    mia "It's just..."
    show mia 6f
    mia "{b}Miss Ross{/b} makes me feel a little self-conscious."
    show player 10f
    show mia 2f
    player_name "She does?"
    show player 11f
    show mia 6f
    mia "She's being very forward with me, don't you think?"
    show player 2f
    show mia 2f
    player_name "Yeah but she's like that with everyone."
    show player 1f
    show mia 6f
    mia "Is she?"
    mia "I dunno, she's lived such an adventurous life and she's so full of experience..."
    show mia 6bf
    mia "She makes me feel so boring."
    show player 2f
    show mia 2f
    player_name "I don't think you're boring, {b}Mia{/b}."
    show player 1f
    show mia 4f
    mia "You don't?"
    show mia 1f
    show player 2f
    player_name "Not at all."
    player_name "I think you just need to relax and keep an open mind."
    player_name "I betcha {b}Miss Ross{/b} can teach us a lot of cool stuff!"
    show mia 5f
    show player 1f
    mia "..."
    show mia 3f
    mia "Yeah, maybe you're right, {b}[firstname]{/b}!"
    show mia 4f
    mia "I coul-"
    show mia 1f
    show player 11f
    show ross 11 at left with dissolve

    ross "There's my favorite students!"
    show mia 8b at Position(xpos=0.65, ypos=1.0) with dissolve
    ross "What are you two love-birds talking about?"
    show mia 55 at Position(xpos=0.635, ypos=1.0) with dissolve
    show player 10f
    player_name "Love-birds?"
    show mia 56
    show player 11f
    mia "We were just wondering what todays session would be about?"
    show mia 55
    show ross 13
    ross "Straight to business, huh?"
    ross "You little firecracker, I love it!"
    show ross 12
    mia "..."
    show ross 58 with dissolve
    ross "Today you're each going to make a collage!"
    show ross 10 with dissolve
    show mia 12b at Position(xpos=0.65, ypos=1.0) with dissolve
    mia "Collage? I don't even know what that means..."
    show mia 8b
    show ross 27 with dissolve
    ross "Oh, they are so much fun! You're going to love them {b}Mia{/b}!"
    ross "We're going to cut pictures out of magazines and glue them together to make art."
    show ross 26
    show player 2f
    show mia 7
    player_name "Sounds like fun to me."
    show player 1f
    show mia 10
    mia "Yeah, it really does."
    show mia 7
    show ross 11 with dissolve
    ross "Alright, well I've got just about everything we need right here. We're just missing {b}rubber cement{/b} and {b}a big stack of magazines.{/b}"
    ross "Why don't you two go find us some?"
    show ross 10
    show player 2f
    player_name "We can do that, right {b}Mia{/b}?"
    show player 1f
    show mia 10b
    mia "Absolutely. In fact, I think my {b}Dad{/b} has some rubber cement at home."
    show mia 10
    mia "I'll go get it!"
    hide mia with dissolve

    show ross 11
    ross "... And away she goes!"
    ross "I guess that means you're in charge of finding the {b}magazines, [firstname]{/b}."
    ross "If you can find {b}three BIG stacks of magazines{/b}, I think that should be enough."
    show player 2f
    show ross 10
    player_name "Any idea where I could find some?"
    show player 1f
    show ross 10b with dissolve
    ross "Hmm..."
    show ross 11
    ross "... I'd start at the {b}Library{/b}. They should have a huge selection to choose from!"
    show player 2f
    show ross 10
    player_name "Alright, I'll go check it out."
    return

label button_ross_find_magazines:
    scene location_school_art_closeup
    show player 2f zorder 1 at right
    show ross 10 at left
    with dissolve
    player_name "Where did you say I should look again?"
    show player 1f
    show ross 11
    ross "For the {b}magazines{/b}?"
    ross "Try the {b}Library{/b}."
    ross "And see if you can find {b}three BIG stacks of magazines{/b}, alright?"
    if M_ross.get("talked with jane"):
        hide ross with dissolve
        show player 10 with dissolve
        player_name "{b}*Sigh*{/b}"
        player_name "The library doesn't have any magazines though."
        if M_ross.get("magazines remaining") == 3:
            player_name "And I still need to find 3 more magazines."
        elif M_ross.get("magazines remaining") == 2:
            player_name "And I still need to find 2 more magazines."
        elif M_ross.get("magazines remaining") == 1:
            player_name "And I still need to find 1 more magazine."
        player_name "I guess I should {b}look around here at school.{/b}"
    else:
        show ross 10
        show player 2f
        player_name "{b}Library{/b}, got it!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
