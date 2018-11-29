label dianes_garden_diane_find_carpenter:
    scene garden
    show player 14 at left
    show diane b_shirtless a_shirtless_sides at lright
    with dissolve
    player_name "Hey, {b}Diane{/b}!"
    show player 13
    show diane f_normal_talk
    dia "Hey, {b}[firstname]{/b}!"
    show diane f_normal
    show player 14
    player_name "Have you spoken with {b}Annie's Dad{/b} yet?"
    player_name "You know, about building your barn?"
    show player 13
    show diane f_normal_talk
    dia "Oh, yes."
    dia "I spoke with him over the phone this morning."
    dia "He'll do it and for a good price too."
    show diane f_normal
    show player 17
    player_name "That's great news!"
    show player 14
    player_name "When's he gonna start?"
    show player 13
    show diane f_sad_talk
    dia "Well, that's the problem."
    show player 5
    dia "He was very non-committal over the phone."
    show diane f_sad
    show player 10
    player_name "Oh?"
    show player 5
    show diane f_sad_talk
    dia "I told him I needed it completed ASAP but he needed to take care of a few odd jobs around his house first."
    dia "I was kinda hoping you could-"
    show diane f_sad
    pause
    show diane f_normal_talk
    dia "Oh, nevermind. It's silly."
    show diane f_normal
    show player 14
    player_name "No, go ahead."
    show player 13
    show diane f_normal_talk
    dia "Well... Do you think you could go over there and give him a hand?"
    show diane f_normal
    show player 12
    player_name "Really?"
    show player 5
    show diane f_normal_talk
    dia "Yeah."
    dia "Just see if there's anything you can do to help him out, you know?"
    dia "Anything to get him over here and building a soon as possible."
    show diane f_normal
    show player 10
    player_name "Hmm, I guess it couldn't hurt to check it out..."
    show player 5
    show diane f_normal_talk
    dia "I would really appreciate it, handsome."
    hide player
    show diane kiss_shirtless
    with dissolve
    pause
    hide diane
    show player 29 at left
    show diane at lright
    with dissolve
    player_name "Heh, no problem!"
    show player 13 with dissolve
    show diane f_normal_talk
    dia "I'll be in the shed pumping if you need me."
    hide diane with dissolve
    pause
    show player 12
    player_name "Hmm, I guess I should head over to {b}Annie's house{/b} and {b}speak with her father.{/b}"
    hide player with dissolve
    return

label garden_diane_drunken_splur_aftermath:
    scene garden
    show player 35 with dissolve
    player_name "No use working on the garden today..."
    player_name "I'll have to come back another time."
    hide player with dissolve
    $ game.main()
    return

label garden_diane_gardening_help:
    scene expression "backgrounds/location_diane_garden_closeup.jpg"
    show player 684
    player_name "( Phew, it's really cooking outside today... )"
    pause
    show player 685
    player_name "( I hope {b}Diane{/b} is doing alright in the shed. )"
    player_name "( She's been keeping her distance these past couple- )"
    dia "OOOWWWW!!!" with hpunch
    show player 23 with dissolve
    player_name "*Gasp* {b}Diane?!{/b}"
    show player 22
    dia "OW! OW! OW!"
    show player 12
    player_name "I'm coming!!!"
    hide player with dissolve
    return

label dianes_garden_diane_drunk_like_a_sailor:
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show diane_chair up zorder 1
    show diane b_laying_back_shirtless a_wave f_laying_laugh zorder 2 at Position (ypos=982)
    with dissolve
    dia "Yoo hoo, {b}[firstname]{/b}!!!"
    show diane f_laying_smirk_talk
    dia "Could you come here for a second?"
    show diane f_laying_smirk
    player_name "Coming!"
    show diane a_drink_sip f_laying_drinking with dissolve
    pause
    show diane a_drink f_laying_smirk_up
    show player 429 zorder 0 at Position (xpos=175,ypos=648)
    with dissolve
    player_name "What's up, {b}Diane{/b}?"
    player_name "You need something?"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "I'm just worried I'm gonna burn sitting out here in the sun like this..."
    show diane f_laying_smirk_up_talk a_wave with dissolve
    dia "You think you could help me out?"
    show diane f_laying_smirk_up
    show player 435
    player_name "You want me to put sun screen on you?"
    show player 434
    show diane f_laying_laugh a_single_bottle with dissolve
    dia "Oh yes, very much!"
    show diane f_laying_smirk_up
    show player 435
    player_name "{b}*Gulp*{/b} Y-yeah, okay."
    show player 434
    hide diane
    show diane f_laying_sitting_smirk_up_talk b_laying_sitting_topless a_empty zorder 2 at Position (yoffset=92)
    with dissolve
    dia "Just give me one second here..."
    show diane_chair down
    show diane laying1 zorder 2
    with dissolve
    pause
    show player 426 at Position (xpos=387,ypos=648) with dissolve
    pause
    show player 427
    player_name "Do you want the sun screen rubbed underneath these straps?"
    show player 426
    dia "Of course!"
    dia "And if it makes it easier, just pull them back..."
    show player 429g
    player_name "!!!"
    hide player
    show diane laying_remove1
    with dissolve
    pause
    show diane laying_remove2 with dissolve
    pause
    show player 429 zorder 0 at Position (xpos=560,ypos=798)
    show diane laying2
    with dissolve
    player_name "Like this?"
    show player 426
    dia "There we go."
    dia "Have at it, stud!"
    player_name "..."
    show player massage 2 with dissolve
    pause
    show player massage 3 with dissolve
    pause
    hide player
    show diane laying_massage_back
    with dissolve
    dia "Mmm, that feels wonderful!"
    dia "Make sure you don't miss a spot."
    show player 429b zorder 0 at Position (xpos=560,ypos=798)
    show diane laying2
    with dissolve
    player_name "Mmmhmm."
    hide player
    show diane laying_massage_back
    with dissolve
    pause
    pause
    show player massage 3 zorder 0 at Position (xpos=560,ypos=798)
    show diane laying2
    with dissolve
    dia "Oh, that's really nice..."
    pause
    show player massage 5
    show diane laying3
    with dissolve
    pause
    show diane laying4 with dissolve
    pause
    show player massage 4
    show diane laying5
    with dissolve
    player_name "!!!"
    player_name "( Does she really want me to rub lotion down there too? )"
    pause
    show player massage 5
    dia "Don't stop, {b}[firstname]{/b}!"
    show player 429h with dissolve
    player_name "Heh, O-okay."
    hide player
    show diane laying_massage_naked_back
    with dissolve
    pause
    pause
    player_name "Here goes..."
    show diane laying_massage_butt with dissolve
    pause
    dia "Oh, god..."
    pause
    show player 429h zorder 0 at Position (xpos=560,ypos=798)
    show diane laying5
    with dissolve
    player_name "I umm... Think I got it all, {b}Diane{/b}."
    show player 429d
    dia "Hmm?"
    dia "Are you sure you didn't miss a spot?"
    show player 429g
    player_name "..."
    dia "Hehehe, I'm just teasing you, handsome."
    show player 429b
    player_name "I should get back to work."
    show player 429g
    show diane laying_getup with dissolve
    dia "I don't think so!"
    player_name "!!!"
    show diane laying_kick
    show diane_chair up
    with dissolve
    dia "You've still gotta get this side!"
    show diane b_laying_back_naked a_laydown f_laying_smirk_up at Position (ypos=982)
    show player 429b at Position (xpos=355,ypos=648)
    with dissolve
    player_name "{b}*Gulp*{/b} R-really?"
    show player 429c
    show diane f_laying_smirk_up_talk
    dia "Mmmhmm."
    dia "You don't want me to burn, now do you?"
    show diane f_laying_smirk_up
    show player 429b
    player_name "N-no..."
    show player 429c
    show diane f_laying_smirk_up_talk
    dia "Start with my chest."
    show diane f_laying_smirk_up a_cream with dissolve
    show player 429b
    player_name "Are you sure?"
    show player 429c
    show diane f_laying_smirk_up_talk
    dia "Yes!"
    dia "... Let me help."
    show diane a_laydown
    show player 429i at Position (xpos=387,ypos=648)
    with dissolve
    dia "Just put your hand..."
    hide player
    show diane b_laying_grope1 f_laying_smirk_up_talk
    with dissolve
    dia "... Right here..."
    with dissolve
    show diane b_laying_grope f_laying_explain_close with dissolve
    pause
    show diane f_laying_explain
    dia "Oooh, this is just what I needed {b}[firstname]{/b}!"
    show diane f_laying_explain_close
    pause
    show diane f_laying_explain
    dia "My breasts are so sore from all this milking..."
    show diane f_laying_explain_close
    player_name "Mmmhmm."
    pause
    show diane f_laying_explain
    dia "Nngghh!"
    dia "Be careful with my nipples, they're very tender right now..."
    show diane f_laying_explain_close
    pause
    show diane b_laying_back_naked
    show player 81 at Position (xpos=403,ypos=648)
    with dissolve
    player_name "( Oh no, not again! )"
    show player 78
    show diane f_laying_explain
    dia "Hmm?"
    show diane f_laying_smirk_up_talk
    dia "Why did you stop-"
    show diane f_laying_surprised_down
    dia "!!!" with hpunch
    show player 426e with dissolve
    player_name "Sorry, {b}Diane{/b}!"
    player_name "I didn't mean-"
    show diane f_laying_smirk_up_talk
    dia "Shh!"
    dia "It's alright, {b}[firstname]{/b}..."
    dia "You just got a little excited helping me out."
    dia "Perfectly natural."
    show diane f_laying_smirk_up
    show player 427b with dissolve
    player_name "Yeah, but..."
    show player 78 with dissolve
    show diane f_laying_smirk_up_talk
    dia "May I return the favor?"
    show diane f_laying_smirk_up
    show player 427b with dissolve
    player_name "What are you gonna-"
    show player 427c
    player_name "!!!" with hpunch
    show player 427d_e
    pause
    show diane f_laying_smirk_up_talk
    dia "That feels good, doesn't it?"
    show diane f_laying_smirk_up
    player_name "Y-yeah..."
    player_name "That feels really good!"
    show diane f_laying_laugh
    dia "Hehe, see?"
    show diane f_laying_smirk_up_talk
    dia "There's nothing to be embarrassed about."
    show diane f_laying_smirk_up
    pause
    show diane f_laying_smirk_up_talk
    dia "I haven't felt one of these in a very loooong time."
    show diane f_laying_smirk_up
    player_name "..."
    pause
    show diane f_laying_laugh
    dia "I can't believe you're so big!"
    show diane f_laying_smirk_up
    player_name "I..."
    player_name "... Thanks."
    show diane f_laying_laugh
    dia "Hehehe."
    show diane f_laying_smirk_up
    pause
    player_name "{b}Diane{/b}, I'm gonna..."
    show diane f_laying_smirk_up_talk
    dia "Let it out, stud."
    show diane f_laying_smirk_up
    pause
    show player 426b
    player_name "HNNGGG!!!" with flash
    pause
    player_name "Haaah... Haaah..."
    player_name "!!!"
    show player 426g
    player_name "Oh my gosh, {b}Diane{/b}, I'm sorry!"
    player_name "I didn't mean to-"
    show player 426h
    show diane f_laying_smirk_up_talk
    dia "Hehe, you didn't do anything to be sorry about, {b}[firstname]{/b}!"
    dia "C'mon, let's go inside and get you cleaned up..."
    show diane f_laying_smirk_up
    show player 426g
    player_name "O-okay."
    hide player
    hide diane
    hide diane_chair
    with dissolve
    scene expression "backgrounds/location_diane_kitchen_closeup.jpg"
    show player 139 at left
    show diane b_shirtless f_smirk a_shirtless_sides at lright
    with dissolve
    player_name "..."
    show diane f_smirk_talk
    dia "Mmm, see? Just a quick- *hic*"
    dia "Just a quick clean up and you're good as new!"
    show diane f_smirk
    show player 140
    player_name "Y-yeah..."
    show player 139
    show diane f_smirk_talk
    dia "Ooh, I think I drank too much again."
    dia "I should go lie down."
    dia "Thanks so much for my day off, {b}[firstname]{/b}!"
    show diane f_laugh
    dia "It was just what the doctor ordered."
    show diane f_smirk
    show player 140
    player_name "I'm glad you enjoyed it."
    show player 139
    show diane f_laugh
    dia "Hehe, very much!"
    hide player
    show diane kiss_mouth
    with dissolve
    player_name "!!!"
    show player 3 at left
    show diane b_shirtless f_smirk_talk a_shirtless_sides at lright
    with dissolve
    dia "Goodnight, stud!"
    hide diane with dissolve
    show player 29
    player_name "G-goodnight..."
    $ renpy.end_replay()
    show player 3
    player_name "..."
    player_name "( I can't believe that just happened! )"
    player_name "( {b}Diane{/b} just... )"
    show player 18 with dissolve
    player_name "( ... )"
    player_name "( ... Wow! )"
    show player 13
    player_name "( I hope she's alright. )"
    player_name "( I should get home. )"
    hide player with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["02_unlocked"] = True
    return

label garden_diane_check_up:
    scene garden
    show player 14 with dissolve
    player_name "I should look for {b}Diane{/b}."
    show player 35
    player_name "{b}... Maybe she's inside?{/b}"
    hide player with dissolve
    return

label dianes_garden_diane_clear_bug_infested_garden:
    scene garden_dead
    show player 14 at left
    show diane b_casual a_casual_sides
    with dissolve
    player_name "Hmm, looks like I missed a few of the nests..."
    show player 13
    show diane f_normal_talk
    dia "Don't worry, the {b}pesticide{/b} will take care of them."
    dia "You go ahead and start spraying while I get changed."
    dia "When I get back, we can start replanting."
    show diane f_normal
    show player 14
    player_name "Sounds good."
    hide player
    hide diane with dissolve
    return

label diane_garden_first_time:
    show expression "backgrounds/location_diane_garden_cutscene05.jpg"
    show expression FilteredText("I didn't know the first thing about gardening but it was nice to see {b}Diane{/b}.\nI always liked her when I was a kid.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause    
    hide cutscene
    show expression FilteredText("She was just a fun person to be around!\nKind hearted and supportive.\nA great sense of humour and full of warmth.") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide cutscene
    show expression FilteredText("I really hope I don't disappoint her...") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with fade

    scene garden
    show player 1 at left
    show diane f_normal_talk at right
    with dissolve
    dia "Well, there's a handsome young man..."
    show diane f_laugh
    show player 13
    dia "You've grown so much, I hardly recognized you at the funeral."
    show diane f_normal
    show player 17
    player_name "Heh, Hi {b}Diane{/b}."
    show diane f_surprised
    show player 2
    player_name "Wow! You look so much like {b}[deb_name]{/b}..."
    show diane f_thinking
    show player 1
    dia "Oh, come now. I'm not nearly as pretty as {b}[deb_name]{/b}..."
    show diane f_surprised
    show player 33
    player_name "Well, I think you look great, {b}Diane{/b}!"
    show diane a_dressed_blush f_laugh_blush with dissolve
    show player 1
    dia "Aww, aren't you just a little charmer?!"
    show diane f_surprised
    show player 11
    dia "..."
    show diane f_laugh_blush with dissolve
    dia "You here to do some work for me?"
    show diane f_normal_talk
    show player 1
    dia "I'm guessing {b}[deb_name]{/b} told you I'm looking for someone to help me this summer?"
    show diane f_normal
    show player 2
    player_name "Yeah, she told me to come see you. I could definitely use the money for tuition."
    show diane f_normal_talk
    show player 5
    dia "Wonderful!"
    dia "I was hoping to get you started today but I'm afraid I ran into a problem..."
    show diane f_shamed_talk_look a_dressed_broken with dissolve
    dia "My old shovel finally quit on me."
    show diane f_shamed
    show player 10
    player_name "Oh! Yeah, that looks pretty bad."
    show diane f_shamed_talk_smile
    show player 1
    dia "We may have to wait until I can replace it..."
    dia "I'm sorry, {b}[firstname]{/b}."
    show diane f_shamed
    show player 2
    player_name "It's okay, {b}Diane{/b}."
    show player 2 at left
    show diane f_normal at right with dissolve
    player_name "Is there any way we can continue the work without it?"
    show diane f_normal_talk
    show player 1
    dia "Well, we can't really dig up a garden without a shovel, can we?"
    dia "I'll just have to pick up a new one next time I'm at the store."
    show diane f_teasing
    show player 11
    dia "Unless..."
    show player 10
    show diane f_normal
    player_name "Unless?"
    show player 11
    show diane f_normal_talk
    dia "... You wouldn't happen to have one at home?"
    show player 4
    show diane f_normal
    player_name "Hmm..."
    show player 2
    player_name "We might have a {b}shovel{/b} in our garage!"
    player_name "I'll go check and come back if I find something."
    show player 203
    show diane f_laugh
    dia "That would be great!"
    show diane f_normal_talk
    dia "Come on back if you find one and we'll get started."
    hide diane
    hide player
    with dissolve
    return

label diane_garden_need_shovel_has_shovel:
    scene garden
    show player 239_240 at left
    show diane a_dressed_sides at lright
    with dissolve
    player_name "Hmm..."
    show player 241 with dissolve
    pause
    show player 242 with dissolve
    pause
    show player 244 with dissolve
    player_name "Here it is!"
    show player 243
    show diane f_laugh
    dia "Ohh! Wonderful!"
    show diane f_normal_talk
    dia "See, you've been a big help already!"
    dia "Alright, before you start, I'll have to show you what to do..."
    show diane a_dressed_finger f_explain with dissolve
    show player 11
    with dissolve
    dia "Make sure you {b}only{/b} keep the vegetables that are {b}long{/b} and {b}hard{/b}!"
    dia "Take out everything else... Especially those pesky rats and bugs, got it?"
    show diane a_dressed_shovel f_normal with dissolve
    show player 14
    player_name "Got it!!"
    show diane f_normal_talk
    show player 1
    dia "You should really take all the money I'm playing you to the {b}Bank{/b} too, when you're done!"
    dia "That's your decision though."
    show diane f_normal
    show player 4
    player_name "Umm, sure. I guess I could do that..."
    show diane f_laugh
    show player 1
    dia "Alright handsome, let's get to work!"
    hide player
    show diane kiss
    with dissolve
    player_name "..."
    hide diane with dissolve
    show expression "boxes/popup_garden.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_garden.png" with dissolve
    return

label diane_garden_need_shovel_no_shovel:
    scene expression player.location.background_blur with None
    show player 2 at left
    show diane f_normal at right
    with dissolve
    player_name "I still haven't found that {b}shovel{/b}."
    player_name "Is there any way we can continue the work without it?"
    show diane f_normal_talk
    show player 1
    dia "Well, we can't really dig up a garden without a shovel, can we?"
    dia "I'll just have to pick up a new one next time I'm at the store."
    show diane f_teasing
    show player 11
    dia "Unless..."
    show player 10
    show diane f_normal
    player_name "Unless?"
    show player 11
    show diane f_normal_talk
    dia "... You wouldn't happen to have one at home?"
    show player 4
    show diane f_normal
    player_name "Hmm..."
    show player 2
    player_name "We might have a {b}shovel{/b} in our garage!"
    player_name "I'll go check and come back if I find something."
    show player 203
    show diane f_laugh
    dia "That would be great!"
    show diane f_normal_talk
    dia "Come on back if you find one and we'll get started."
    hide diane
    hide player
    with dissolve
    return

label diane_garden_delivery_1_task:
    scene garden
    show player 13 at left
    show diane f_normal_talk at lright
    with dissolve
    dia "Oh, {b}[firstname]{/b}, I'm so glad you came by today!"
    show diane f_normal
    show player 10
    player_name "Uh oh, another garden emergency?"
    show player 5
    show diane f_laugh
    dia "Heh, not exactly..."
    show diane f_normal_talk
    dia "I haven't told you about my side business yet, have I?"
    show diane f_normal
    show player 12
    player_name "Side business? I thought you just lived off the money you got in your divorce?"
    show player 5
    show diane f_smirk_talk
    dia "Heh, well I do for the most part. My little startup is more of a pet project than an actual money making endeavor..."
    show diane f_smirk
    show player 14
    player_name "Alright, so what is it?"
    show player 13
    show diane f_normal_talk
    dia "I've been packaging and selling milk."
    show diane f_normal
    show player 14
    player_name "Milk?! I didn't know you had a cow! That's awesome!"
    show player 13
    dia "..."
    show player 32 with dissolve
    player_name "Where is she? Can I pet her?"
    show player 31
    show diane f_laugh
    dia "Hahaha!"
    show diane f_smirk_talk
    dia "Sorry, handsome. My cow is... Well... Let's just say she isn't fond of visitors."
    show diane f_smirk
    show player 10 with dissolve
    player_name "Aww, okay..."
    player_name "So what do you need my help with?"
    show player 13
    show diane f_normal_talk
    dia "Well, a local pizza business placed an order and I need someone to deliver it for me."
    show diane f_normal
    show player 14
    player_name "I can do that!"
    show player 13
    show diane f_normal_talk
    dia "You don't mind?"
    dia "It would be a huge help."
    show diane f_normal
    show player 14
    player_name "No, I don't mind at all."
    show player 13
    show diane f_laugh
    dia "Oh, wonderful!"
    hide player
    show diane kiss
    with dissolve
    pause
    show player 5 at left
    show xtra 21 at left
    show diane f_normal_talk
    with dissolve
    dia "I dunno what I'd do without you, {b}[firstname]{/b}!"
    show diane f_normal
    hide xtra 21
    show player 21
    player_name "Heh, it's no problem. I love to help!"
    show player 13
    show diane f_normal_talk
    dia "Let me grab the package for you..."
    hide diane with dissolve
    pause
    show player 18
    player_name "( Wow, this is so cool! )"
    player_name "( {b}Diane{/b} really is like a farm girl at heart. )"
    show player 33
    player_name "( I hope she lets me meet her cow some day... )"
    show player 13
    show diane f_normal_talk a_dressed_milk_package with dissolve
    dia "Here we are."
    show diane f_normal
    show player 427
    player_name "Whoa, it has your face on it and everything!"
    show player 426
    show diane f_smirk_talk
    dia "Yup."
    show diane f_smirk
    show player 427
    player_name "Hmm, {b}\"Auntie Diane's Original.\"{/b}"
    show player 426
    show diane f_smirk_talk
    dia "Hehehe, you like that?"
    show diane f_smirk
    show player 14
    player_name "Yeah, it's got a nice ring to it!"
    show player 13
    show diane f_smirk_talk
    dia "I thought so too."
    show diane f_cheese a_dressed_shovel
    show player 163e
    with dissolve
    player_name "So, where am I taking it?"
    show player 163d
    show diane f_normal_talk
    dia "Just down the road to a little restaurant called, {b}\"Tony's Pizza.\"{/b}"
    show diane f_normal
    show player 163e
    player_name "I've heard of that place!"
    player_name "We've been getting {b}flyers{/b} from them in our {b}mailbox{/b}."
    show player 163d
    show diane f_normal_talk
    dia "Yeah, I hear they're pretty good."
    dia "Say hi to {b}Tony{/b} for me, won't you?"
    dia "Oh, and don't forget to collect the payment."
    show diane f_normal
    show player 163e
    player_name "Sure thing."
    player_name "I'll be back in a flash!"
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_drunken_splur:
    scene location_diane_garden_close_day_blur with None
    show player 11 at left
    show diane b_shirtless a_shirtless_drink f_drunk_talk at lright
    with dissolve
    dia "Yoo-hooo! There you are, handsome!"
    show player 5
    dia "How are you-*hic* doing today?"
    dia "You here to give me another sh-*hic*"
    dia "... Another show?!"
    show diane a_shirtless_drink_sip with dissolve
    show player 12
    player_name "{b}Diane{/b}? Are you drunk?"
    show player 11
    show diane a_shirtless_drink with dissolve
    dia "Hehehe, yeeeaaah..."
    dia "Just a little though!"
    dia "It's so hot out here, you know?!"
    dia "I just-*hic*"
    dia "I just needed a little something to cool myself off..."
    dia "... And I thought to myself, \"Self,\" {b}*Hic*{/b} \"your side business is really starting to take of!\""
    dia "If that's not a cause for celebration, I don't know what is!"
    show diane a_shirtless_drink_sip with dissolve
    pause
    show diane b_shirtless_pull a_shirtless_drink_pull f_drunk with dissolve
    player_name "!!!"
    show diane f_drunk_talk
    dia "You wanna celebrate with me, {b}[firstname]{/b}?"
    show diane f_drunk
    show player 22
    pause
    show player 10
    player_name "{b}Diane{/b}, your clothes... They um... Slipped."
    show player 11
    show diane f_drunk_talk
    dia "Huh? What are you..."
    show diane a_shirtless_drink_hand_pull with dissolve
    dia "Oh!!"
    show diane a_shirtless_reach_pull f_laugh_blush with dissolve
    dia "Hahaha!"
    show player 21
    show diane f_shamed
    player_name "Heh..."
    show player 13
    show diane f_shamed_talk
    dia "I guess I shouldn't have taken my shirt off, huh?"
    dia "It doesn't help having these... Massive udders flopping around!!"
    show diane f_laugh_blush
    dia "Haha!"
    show diane b_shirtless a_shirtless_reach f_shamed with dissolve
    pause
    show player 11
    show diane b_shirtless_pull a_shirtless_drink_hand_pull with dissolve
    dia "Oops! They keep trying to escape!"
    show diane a_shirtless_reach_pull f_laugh_blush with dissolve
    dia "Haha!"
    show player 1
    show diane b_shirtless a_shirtless_drink f_drunk_talk at right with fastdissolve
    dia "There."
    dia "Have I ever told you how much I dislike {b}[deb_name]'s{/b} other tenant?"
    show player 10
    show diane f_drunk
    player_name "Uh, no. You mean, {b}[jen_name]{/b}?"
    show player 5
    show diane f_laugh_blush
    dia "Yes! *hic* That's the one!"
    show diane f_drunk_talk
    dia "She's such a biiiitch!"
    show diane f_drunk
    show player 11
    pause
    show diane f_drunk_talk
    dia "I wish I had nice young tits like her though..."
    show diane a_shirtless_drink_sip with dissolve
    pause
    show diane a_shirtless_drink with dissolve
    dia "What's the matter?"
    dia "You don't like her tits?"
    show diane f_drunk
    show player 24
    player_name "I... Uh..."
    show diane a_shirtless_drink_hand with dissolve
    dia "You're telling me you haven't noticed them?"
    show diane a_shirtless_drink with dissolve
    show player 10
    player_name "Well... I don't know."
    show diane f_drunk_talk
    show player 11
    dia "Here."
    show diane b_shirtless_pull a_shirtless_pull f_drunk with fastdissolve
    show player 22
    pause
    show diane f_drunk_talk
    show player 11
    dia "I mean, don't you think they look better than these old things?"
    show diane f_drunk
    show player 21
    player_name "No, I think your breasts look great, {b}Diane{/b}."
    show diane f_drunk_talk
    show player 13
    dia "Awww!"
    dia "You're so-*hic*"
    dia "... So sweet!"
    show diane f_drunk
    pause
    show diane a_shirtless_reach_pull f_shamed_talk with dissolve
    show player 11
    dia "Hmm..."
    dia "I don't feel so good all of a sudden."
    dia "I think I need to-*hic*"
    dia "I need to lie down for a bit..."
    show diane sitting_drunk with dissolve
    show player 427
    player_name "Whoa, whoa, whoa!"
    player_name "{b}Diane{/b}, you can't just lie down in the garden..."
    show player 13
    show diane b_shirtless_pull a_shirtless_reach_pull f_shamed_talk
    with dissolve
    dia "Hmm?"
    show diane f_shamed
    show player 14
    player_name "Lemme help you upstairs to your bed!"
    show player 13
    show diane f_drunk_talk
    dia "Aww, would you do that for-*hic*"
    dia "... Do that for me?"
    show diane f_drunk
    show player 14
    player_name "Of course, here..."
    hide player
    show diane hold_talk
    with dissolve
    dia "Mmm, such a helpful young man..."
    show diane hold_peek
    pause
    show diane hold_talk
    dia "You're so much sweeter than all the other worthless men in this town!"
    show diane hold_peek
    player_name "..."
    dia "..."
    show diane hold_talk
    dia "Hehehe, it's on the top floor, stud."
    show diane hold
    player_name "!!!"
    player_name "Right, sorry."
    hide diane with dissolve
    scene expression "backgrounds/location_diane_garden_cutscene07.jpg"
    show expression FilteredText("I'd never seen {b}Diane{/b} this drunk before!\nI helped her up the stairs to her room, doing my best to listen as she drunkenly poured her heart out.") as cutscene at Position (xpos= 512, ypos = 700)
    with fade
    pause
    hide cutscene
    show expression FilteredText("She went on and on about her no good ex-husband and the men she'd seen since they'd divorced.\nI was beginning to suspect there was more to this drunken episode\nthan a simple celebration. ") as cutscene at Position (xpos= 512, ypos = 700) with dissolve
    pause
    scene black
    hide cutscene
    with fade
    scene expression "backgrounds/location_diane_bedroom_closeup.jpg"
    show diane hold_tired_talk
    dia "... He wouldn't even talk with me about children, the worthless prick."
    dia "What kinda man doesn't want to settle down and start a family?!"
    show diane hold_tired
    player_name "..."
    show diane hold_tired_talk
    dia "... Now he's probably off gambling his money away and banging cheap whores!"
    show diane hold_tired
    player_name "Okay {b}Diane{/b}, here we are..."
    player_name "Let's get you in bed, okay?"
    show diane hold_talk
    dia "Pfft, hahaha!"
    dia "You're the first person to who's said that to me in a loooooong time!"
    show diane hold
    player_name "!!!"
    show diane hold_talk
    dia "Hahaha!"
    dia "Oh, I'm just-*hic*"
    dia "I'm just teasing you, stud..."
    dia "I think I can take it from here."
    show diane b_shirtless_pull a_shirtless_tired f_drunk_talk
    show player 13 at left
    with dissolve
    dia "Why don't you go and fetch me a glass of water from the kitchen?"
    show diane f_drunk
    show player 14
    player_name "Y-yeah, okay."
    show player 13
    show diane f_drunk_talk
    dia "Good boy."
    hide diane
    hide player
    with dissolve
    return

label dianes_garden_diane_mouse_attack_not_known:
    scene garden with None
    show player 1f with dissolve
    pause
    show player 32f at Position(xoffset=-69)
    player_name "Huh. Where's {b}Diane{/b}?"
    player_name "She's usually out here working on her garden..."
    show player 31 at Position(xoffset=68)
    pause
    show player 30
    player_name "It doesn't look like she's in her shed either."
    show player 12
    player_name "She must be inside. It's really hot outside today."
    show player 5
    player_name "..."
    show player 10
    player_name "Maybe I should check up on her before I start working."
    hide player with dissolve
    return

label dianes_garden_diane_need_shovel_remove_waste:
    scene expression player.location.background_blur with None
    show player 203 at left
    show diane f_normal_talk
    with dissolve
    dia "Oh, there you are. Thank goodness!"
    dia "I was starting to think you weren't coming by today."
    show player 2
    show diane f_normal
    player_name "Hi, {b}Diane{/b}!"
    player_name "Is everything alright?"
    show diane f_normal_talk
    show player 203
    dia "Everything's fine. You've been doing a great job with my garden, {b}[firstname]{/b}!"
    dia "In fact, you're doing so well, that we have a ton of leftover waste!"
    show diane f_normal
    show player 17
    player_name "Sorry about that. Haha."
    show diane f_normal_talk
    show player 203
    dia "No need to be sorry, handsome!"
    dia "I just need help moving it."
    dia "I loaded it all up in this {b}wheelbarrow{/b}..."
    dia "... But I'm afraid it's too much for my poor back."
    dia "Do you think you could help me out?"
    show player 14
    show diane f_normal
    player_name "Of course!"
    player_name "That's why I'm here!"
    show player 13
    show diane f_normal_talk
    dia "Just be careful, it's really heavy!"
    show player 2
    show diane f_normal
    player_name "No problem!"
    player_name "I'll take care of it!"
    return

label dianes_garden_diane_need_shovel_remove_waste_repeat:
    scene expression player.location.background_blur with None
    show player 203 at left
    show diane f_normal_talk
    with dissolve
    dia "I was starting to think you weren't coming by today."
    show player 2
    show diane f_normal
    player_name "Hi, {b}Diane{/b}!"
    player_name "Is everything alright?"
    show diane f_normal_talk
    show player 203
    dia "Everything's fine. I just need help moving this {b}wheelbarrow{/b}..."
    dia "... I'm afraid it's too much for my poor back."
    dia "Do you think you could help me out?"
    show player 14
    show diane f_normal
    player_name "Of course!"
    player_name "That's why I'm here!"
    show player 13
    show diane f_normal_talk
    dia "Just be careful, it's really heavy!"
    show player 2
    show diane f_normal
    player_name "No problem!"
    player_name "I'll take care of it!"
    return

label dianes_garden_diane_need_shovel_remove_waste_pass:
    scene expression player.location.background_blur with None
    show player 255 at left
    show diane f_normal
    with dissolve
    player_name "There we go."
    player_name "See, I can handle it!"
    show player 254
    show diane f_laugh_blush
    dia "!!!" with hpunch
    dia "Wow... You lifted it like it was nothing!"
    show diane f_smirk
    pause
    show player 254
    show diane f_smirk_talk
    dia "Strong and handsome..."
    dia "I bet you have to fight those young girls at school off with a stick, don't you?!"
    show diane f_smirk
    show player 255
    player_name "Hah, no... Not really."
    show player 254
    show diane f_laugh
    dia "Oh, come now! I don't believe that for one second!"
    show diane f_smirk_talk
    dia "In my younger years, I'd have been all over you in an instant!"
    show diane f_smirk
    show player 255
    show xtra 21 at Position (xpos=88) with dissolve
    player_name "Hehe."
    player_name "I uhh..."
    player_name "... Where would you like me to dump this?"
    show player 254
    show diane f_smirk_talk
    dia "Hmm?"
    show diane f_lookup
    dia "Oh, right!"
    show diane f_normal_talk
    dia "Just follow me, handsome."
    dia "I keep a compost heap just over here, behind the house."
    show diane f_normal
    show player 255
    hide xtra with dissolve
    player_name "Compost?"
    player_name "Like, garbage?"
    show player 254
    show diane f_laugh
    dia "What? Hehe, no!"
    show diane f_normal_talk
    dia "Compost is a valuable resource for a gardener, {b}[firstname]{/b}!"
    dia "All that organic matter decomposes and creates a nutrient rich fertilizer for the soil."
    show diane f_normal
    show player 255
    player_name "Really? So it helps the plants grow?"
    show player 254
    show diane f_normal_talk
    dia "That's right!"
    dia "It's what makes my vegetables so..."
    show diane f_smirk_talk
    dia "Girthy."
    show diane f_smirk
    show player 255
    player_name "Awesome!"
    player_name "I'm learning so much from you, {b}Diane{/b}!"
    hide location_diane_garden_day_blur
    hide player
    hide diane
    with dissolve
    scene expression "backgrounds/location_diane_garden_cutscene04.jpg"
    show expression FilteredText("The compost pile behind her house was so far!\n I barely made it; the wheelbarrow kept slipping out of my hands.") as cutscene at Position (xpos= 512, ypos = 700)
    with fade
    pause
    hide cutscene
    show expression FilteredText("It felt good though, moving all that waste for {b}Diane{/b}.\n... And I was learning a lot about gardening!") as cutscene at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide cutscene
    scene black
    with fade
    scene location_diane_garden_day_blur
    show player 18 at left
    show diane f_laugh_blush at lright
    with dissolve
    dia "I can't believe you did it with such ease!"
    show diane f_normal
    show player 17
    player_name "It was pretty hard, actually. Haha!"
    show player 203
    show diane f_normal_talk
    dia "Well, I sure am glad you were here..."
    dia "I don't know what I would have done without you!"
    show diane f_normal
    show player 2
    player_name "It's no big deal."
    player_name "I like the exercise!"
    show player 203
    show diane f_teasing
    dia "I bet you do..."
    dia "... You must excercise all the time."
    show diane f_smirk
    show player 11
    player_name "..."
    show player 21
    player_name "What do you mean?"
    show player 13
    show diane f_laugh
    dia "C'mon, What's your secret? You're so lean and fit!"
    show diane f_thinking
    show player 11
    dia "I try to stay active as often as possible but I can't seem to get rid of all this fat."
    show diane f_normal
    show player 10
    player_name "Fat?! What fat?"
    show diane f_surprised
    show player 29 with dissolve
    player_name "You look great, {b}Diane{/b}."
    show diane a_dressed_blush f_laugh_blush with dissolve
    show player 13 with dissolve
    dia "Aww. You say that now. But if you saw me without clothes on, you'd be singing a different tune!"
    show diane f_surprised
    show player 11
    player_name "..."
    show diane a_dressed_shovel f_laugh_blush with dissolve
    dia "Err... Anyway!"
    show diane f_teasing
    dia "... You gonna tell me your trick or not?"
    dia "Have you been working out?"
    show diane f_smirk
    show player 21
    player_name "A little."
    show player 35
    player_name "I try going to the gym sometimes."
    show player 13
    show diane f_normal_talk
    dia "Really?!"
    dia "That's great!"
    show diane a_dressed_finger f_explain with dissolve
    dia "You know, there are many good advantages to staying in shape."
    show diane a_dressed_shovel f_teasing with dissolve
    show player 11
    dia "Women love guys who are lean, strong, and full of vigor."
    show diane f_smirk
    player_name "..."
    show diane f_smirk_talk
    dia "Let's see that six pack!"
    show diane f_smirk
    show player 22
    player_name "!!!" with hpunch
    show player 21
    player_name "You want to see my..."
    show player 11
    show diane f_smirk_talk
    dia "Your abs! Yes."
    dia "Give this old lady a show!"
    show diane f_smirk
    show player 10
    player_name "O-okay..."
    show diane f_surprised
    show player 249 with dissolve
    show diane a_dressed_blush f_laugh_blush with dissolve
    dia "Whooo!"
    show diane a_dressed_shovel f_smirk_talk with dissolve
    dia "Look at that sexy body!"
    show diane f_teasing
    dia "How can you not be popular with the girls at school?"
    show diane f_smirk
    show player 250
    player_name "Heh, I dunno..."
    show diane f_surprised
    show player 108f with dissolve
    player_name "There are guys much bigger than me at school."
    player_name "I'm definitely not one of the cool guys..."
    show player 109f
    show diane f_teasing
    dia "Aww, well that's okay, {b}[firstname]{/b}."
    show diane f_thinking
    show player 13
    dia "The girls will grow out of that phase sooner than you think..."
    show diane f_laugh_blush
    dia "... Just give it some time!"
    show diane f_eyes_closed
    show player 17
    player_name "Thanks, {b}Diane{/b}."
    show diane f_smirk_talk
    show player 203
    dia "No problem, stud!"
    show diane f_smirk
    show xtra 21 at left with dissolve
    player_name "..."
    show diane f_normal
    dia "..."
    show diane f_thinking a_dressed_blush with dissolve
    dia "Boy, it sure is hot out here, isn't it?"
    show diane f_normal
    show player 14
    hide xtra with dissolve
    player_name "Heh, yeah. I'm sweating like crazy!"
    show player 13
    show diane f_normal_talk a_dressed_finger with dissolve
    dia "Well, I bet I can come up with a solution to that..."
    show diane hose with dissolve
    show player 10
    player_name "Oh?"
    show player 12
    player_name "What are you-"
    show diane a_dressed_hose f_cheese with dissolve
    show player 11
    player_name "..."
    show player 10
    player_name "You aren't gonna-"
    show diane a_dressed_hose_shoot
    show player 668
    player_name "!!!" with hpunch
    pause
    player_name "Whoa! That's freezing!"
    show player 669f with dissolve
    show diane f_laugh
    dia "Oh, no you don't! You aren't getting away that easily!"
    hide player with dissolve
    show diane hose_chase with dissolve
    dia "Hahaha!"
    hide diane with dissolve
    scene expression "backgrounds/location_diane_garden_cutscene06.jpg"
    show expression FilteredText("{b}Diane{/b} and I wrestled with that hose, spraying one another and giggling like school children.") as cutscene at Position (xpos= 512, ypos = 700)
    with fade
    pause
    hide cutscene
    show expression FilteredText("We didn't get a lot accomplished in the garden that day but we did have a lot of fun!") as cutscene at Position (xpos= 512, ypos = 700) with dissolve
    pause
    scene black
    hide cutscene
    with fade
    scene location_diane_garden_night_blur
    show player 677 at left
    show diane b_dressed_wet f_laugh a_dressed_blush at lright
    with dissolve
    dia "Okay, okay! I submit!"
    show diane f_normal_talk
    dia "I can't keep up with you..."
    show diane f_cheese a_dressed_shovel with dissolve
    show player 678
    player_name "I win?!"
    show player 677
    show diane f_normal_talk
    dia "Yeah, yeah... You win!"
    show diane f_normal
    show player 679 with dissolve
    player_name "Hahaha! Victory!"
    show diane f_laugh
    dia "Hehehe!"
    show player 677 with dissolve
    show diane f_lookup
    pause
    dia "Sheesh, is it getting dark already?"
    show diane f_normal_talk
    dia "You should get on home, {b}[firstname]{/b}."
    dia "I have some other work to do tonight."
    show diane f_normal
    show player 678
    player_name "Anything I can help with?"
    show player 677
    show diane f_surprised
    dia "Hmm?"
    show diane f_smirk_talk
    dia "Nah, I think not. I appreciate the offer, but this is work I'm better off doing alone..."
    show diane f_smirk
    show player 678
    player_name "O-okay..."
    show player 677
    show diane f_normal_talk
    dia "Thanks again for all your help today, stud!"
    dia "Tell {b}[deb_name]{/b} I said, \"Hi.\""
    show diane f_normal
    show player 678
    player_name "Alright."
    player_name "See ya soon, {b}Diane{/b}."
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_need_shovel_remove_waste_fail:
    scene location_diane_garden_day_blur
    show player 253 at left with dissolve
    pause
    show player 256 at Position(xpos=0.0322,ypos=1.0000)
    show diane f_normal
    with dissolve
    player_name "[str_warn]Ughhh!!..."
    player_name "[str_warn]...Ghhh..."
    show player 27 with dissolve
    player_name "[str_warn]I... I can't do it..."
    player_name "[str_warn]I'm sorry..."
    show player 3
    show diane f_normal_talk
    dia "Oh..."
    dia "It's... okay. I really did pack it way too full..."
    dia "I'll just take some out and we can do it little by little."
    show player 23
    player_name "No, wait... I can do it!"
    show player 256 with dissolve
    dia "..."
    show player 10 with dissolve
    player_name "I'm just tired today, that's all..."
    player_name "Let me rest and get some {b}strength{/b}. I'll come back and do it another day, I promise."
    show diane f_normal
    show player 3
    dia "..."
    show diane f_laugh
    show player 5
    dia "Oh? Well, if you say so..."
    show diane f_normal_talk
    dia "I'll see you again soon?"
    show player 2
    show diane f_normal
    player_name "Yeah, I'll be back real soon."
    player_name "Thanks, {b}Diane{/b}!"
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_delivery_3_task_week:
    scene garden
    show player 13 at left
    show diane f_normal_talk b_shirtless a_shirtless_sides at lright
    with dissolve
    dia "Hey there, stud!"
    dia "You ready to make another delivery?"
    show diane f_normal
    show player 17
    player_name "Oh, so that's the big job you were talking about!"
    show player 13
    show diane f_normal_talk
    dia "Well, of course."
    dia "What did you think it was?"
    show diane f_normal
    show player 29 with dissolve
    player_name "I..."
    player_name "I dunno."
    show player 3
    show diane f_smirk
    dia "Mmhmm."
    show diane f_smirk_talk
    dia "Naughty boy..."
    dia "This is my biggest customer yet, {b}[firstname]{/b}."
    dia "Do a good job and you can help me with my pumping when you get back, deal?"
    show diane f_smirk
    show player 17 with dissolve
    player_name "deal!"
    show player 13
    show diane f_laugh
    dia "Hehe."
    show diane f_smirk
    show player 14
    player_name "So where is the package going this time?"
    show player 13
    show diane f_normal_talk
    dia "Just deliver it to the cafeteria at your school."
    show diane f_normal
    show player 22
    player_name "!!!"
    show player 10
    player_name "My school?"
    show player 11
    show diane f_normal_talk
    dia "That's right!"
    show diane f_normal
    show player 10
    player_name "You mean the students at school will be drinking-"
    show player 11
    show diane f_normal_talk
    dia "You'd better hurry, handsome."
    dia "I told your principal to expect delivery ASAP."
    show diane f_normal
    player_name "..."
    show player 10
    player_name "Okay."
    show player 5
    show diane f_normal_talk
    dia "{b}The package is in the shed.{/b}"
    show diane f_normal
    show player 10
    player_name "Got it."
    return

label dianes_garden_diane_delivery_3_task_weekend:
    scene expression player.location.background_blur
    show diane f_normal_talk
    dia "The {b}Package{/b} has to be dropped off at the {b}School{/b}, so come back during the school week."
    show player 1 at left
    player_name "Okay."
    return

label dianes_garden_diane_delivery_3_done:
    scene garden
    show player 640e at left
    show diane b_shirtless a_shirtless_sides at lright
    with dissolve
    player_name "Hey, {b}Diane{/b}."
    player_name "I delivered that package to my school for you."
    show player 13
    show diane a_shirtless_money f_shamed_talk_smile
    with dissolve
    dia "Yeah, I just got off the phone with the cafeteria guy."
    show diane a_shirtless_sides with dissolve
    dia "He's already placed another order."
    dia "Even bigger than the last."
    show diane f_shamed
    show player 14
    player_name "That's a good thing, right?"
    show player 13
    show diane f_shamed_talk_smile
    dia "{b}*Sigh*{/b} Yeah, I'm just worried about meeting the demand is all."
    dia "I need to find a better work place soon!"
    dia "Otherwise, I might lose customers..."
    show diane f_shamed
    show player 10
    player_name "Anything I can do to help?"
    show player 5
    show diane f_shamed_talk_smile
    dia "Hmm, I'm afraid not."
    dia "I just have to hope a vacant barn becomes available."
    show diane f_shamed
    show player 10
    player_name "It's a shame you don't have more land here. You could just build a new barn."
    show player 5
    show diane f_normal_talk
    dia "Yeah, that would be nice wouldn't it?"
    dia "I could design it to fit my business perfectly!"
    show diane f_thinking
    dia "... You know what?!"
    dia "You might actually be on to something {b}[firstname]{/b}..."
    show player 14
    player_name "Really?"
    show player 13
    show diane f_normal_talk
    dia "Yeah!"
    dia "Why don't you get started on the gardening and let me think on this for awhile."
    show diane f_normal
    show player 14
    player_name "Sure thing!"
    show player 13
    show diane f_smirk_talk
    dia "Come and see me when you're done."
    dia "We can have some fun."
    show diane f_smirk
    show player 29 with dissolve
    player_name "O-okay."
    show player 3
    show diane f_laugh
    dia "Hehehe, thanks stud!"
    hide player
    show diane kiss_shirtless
    with dissolve
    pause
    hide diane with dissolve
    return

label garden_diane_clean_garden:
    scene expression "backgrounds/location_diane_garden_closeup.jpg"
    show player 10 with dissolve
    player_name "Oh, man..."
    player_name "How did this happen?"
    show player 184 at right with dissolve
    player_name "..."
    show player 672 with dissolve
    player_name "Yuck!"
    player_name "Everything is ruined..."
    show diane at flip with dissolve
    player_name "How did this happen-"
    show diane f_sad_talk
    dia "Hi, {b}[firstname]{/b}..."
    show diane f_sad
    show player 22 at Position (xoffset=-131) with dissolve
    player_name "!!!"
    show player 10f with dissolve
    player_name "{b}Diane{/b}, look!"
    show player 671f with dissolve
    show diane f_scared
    dia "..."
    show player 672f
    player_name "What happened to the garden?"
    player_name "Did I screw something up?"
    show player 5f with dissolve
    show diane a_dressed_blush f_shamed_talk_smile with dissolve
    dia "Oh no, handsome..."
    dia "This is all my fault."
    show diane a_dressed_shovel with dissolve
    dia "I went with an all natural pesticide this year and it wasn't as effective as I was hoping."
    show diane f_shamed
    show player 12f
    player_name "Pesticide?"
    show player 5f
    show diane f_shamed_talk_smile
    dia "Yeah, you see those critters crawling all over the garden?"
    show diane f_shamed
    show player 10f
    player_name "Yeah..."
    show player 5f
    show diane f_shamed_talk_smile a_dressed_finger with dissolve
    dia "Those are {b}earwigs{/b}."
    show diane f_shamed a_dressed_shovel with dissolve
    player_name "..."
    show player 12f
    player_name "Why do they call them earwigs?"
    show player 5f
    show diane f_laugh
    dia "Hehe, it's from an old wives tale... People used to believe earwigs would crawl into your ear and lay eggs in your brains."
    show diane f_normal
    show player 11f
    player_name "!!!"
    show player 10f
    player_name "That's not... I mean, they don't really-"
    show player 5f
    show diane f_laugh a_dressed_blush with dissolve
    dia "Hahaha! No, of course not!"
    show diane f_normal_talk a_dressed_shovel with dissolve
    dia "They prefer moist rich soil, which is why they ended up in our garden here."
    dia "I betcha there are dozens of nests in that soil right now..."
    show diane f_normal
    show player 12f
    player_name "... Gross!!!"
    player_name "So how do we fix it?"
    show player 5f
    show diane f_normal_talk a_dressed_finger with dissolve
    dia "Hmm, well for starters, we're gonna have to throw out all these infested crops and destroy as many nests as we can."
    dia "Then we'll need to till the soil and replant."
    dia "Making sure we use a more effective pesticide this time."
    show diane f_normal a_dressed_shovel with dissolve
    show player 14f
    player_name "Alright."
    player_name "Let's get started!"
    show player 13f
    show diane f_normal_talk
    dia "Hehe, so eager..."
    dia "I can't believe you're enjoying gardening so much!"
    show diane f_normal
    show player 14f
    player_name "It's a lot of fun!"
    show player 13f
    show diane f_normal_talk
    dia "Alright, well dig in!"
    hide player
    hide diane
    with dissolve
    jump garden_listing
    return

label dianes_garden_diane_bug_infestation:
    scene garden
    show player 10 at left with dissolve
    player_name "{b}Diane{/b}?"
    show player 4 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "That's weird."
    player_name "She's usually waiting here to greet me."
    show player 31 with dissolve
    player_name "!!!"
    show player 32
    player_name "Oh, no!"
    player_name "What's wrong with the garden?!"
    hide player with dissolve
    return

label dianes_garden_diane_check_up_on_garden:
    scene garden
    show player 14 with dissolve
    player_name "Hey, {b}Diane{/b}!"
    player_name "How's the-"
    show player 32 at Position (xoffset=68) with dissolve
    player_name "Wow!!!"
    show player 17 with dissolve
    player_name "The garden looks great!"
    show player 14
    player_name "I can't believe everything is growing back so quickly."
    show player 30
    player_name "Hmm..."
    show player 32f with dissolve
    player_name "{b}Diane{/b} is missing again..."
    player_name "I wonder where she's hiding?"
    hide player with dissolve
    return

label dianes_garden_diane_pump_request:
    scene garden
    show player 5 at left
    show diane f_normal_talk at lright
    with dissolve
    dia "Hey, there he is!"
    show diane f_normal
    show player 29 with dissolve
    player_name "Hi, {b}Diane{/b}."
    show player 3
    show diane f_laugh
    dia "I'm so glad you're here!"
    show diane f_normal_talk
    dia "Did {b}[deb_name]{/b} tell you about my new client?"
    show diane f_normal
    show player 29
    player_name "Yeah, she said you landed a big one."
    show player 3
    show diane f_laugh
    dia "You better believe it!"
    show diane f_normal_talk
    dia "I've got a lot of work to do before we can make the delivery."
    dia "I'm afraid I won't really have time to tend the garden..."
    show diane f_normal
    show player 5 with dissolve
    player_name "..."
    show diane f_normal_talk
    dia "Think you can handle it by yourself?"
    show diane f_explain
    dia "I'll give you a bump in pay..."
    show diane f_cheese
    show player 10
    player_name "Yeah, that's fine."
    show player 5
    show diane f_normal
    dia "..."
    show diane f_shamed_talk_smile
    dia "What's the matter, handsome?"
    dia "You still thinking about the other day?"
    show diane f_shamed
    show player 12
    player_name "Yeah, I'm really sorry about the whole-"
    show player 11
    show diane f_laugh a_dressed_finger with dissolve
    dia "Oh, don't be silly, handsome."
    show diane f_normal_talk
    dia "You're a young man!"
    dia "You can't always control those things!"
    show diane f_normal a_dressed_shovel with dissolve
    show player 29 with dissolve
    player_name "Yeah, I guess..."
    show player 3
    show diane f_normal_talk
    dia "Don't give it another thought, {b}[firstname]{/b}!"
    show diane f_normal
    show player 13 with dissolve
    player_name "..."
    show diane f_normal_talk
    dia "Alright, well I'd best get started."
    dia "Lots of work to do!"
    dia "I'll be in the shed getting everything ready if you need me, okay?"
    show diane f_normal
    show player 23
    player_name "{b}*Gasp*{/b} Is the cow in there now?"
    show player 14
    player_name "Can I pet it?!"
    show player 13
    show diane f_normal_talk
    dia "Huh?"
    show diane f_lookup
    dia "Oh, the cow... Uhh, no."
    show diane f_smirk
    dia "..."
    show diane f_smirk_talk
    dia "I'll go and visit the cow later tonight."
    show diane f_smirk
    show player 12
    player_name "So, what are you doing in the shed now?"
    show player 5
    show diane f_surprised_down a_dressed_blush with dissolve
    dia "I uhh..."
    show diane f_shamed_talk_smile a_dressed_finger with dissolve
    dia "... Cleaning!"
    dia "Yeah, I have to get all the equipment sterilized and make sure all the packaging is ready."
    show diane f_shamed a_dressed_shovel with dissolve
    show player 17
    player_name "I see."
    show player 14
    player_name "Do you need any help?"
    show player 13
    show diane f_laugh
    dia "No thanks, handsome."
    dia "You just focus on the gardening for now and I'll-"
    show diane f_explain a_dressed_finger with dissolve
    dia "!!!"
    show diane f_normal_talk
    dia "Actually, there is something you can do for me!"
    show diane f_normal a_dressed_shovel with dissolve
    show player 14
    player_name "Sure, anything."
    show player 13
    show diane f_smirk_talk
    dia "{b}I left one of my tools on the kitchen counter.{/b}"
    dia "Could you run and fetch it for me?"
    show diane f_smirk
    show player 14
    player_name "Of course."
    player_name "I'll be right back."
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_delivery_2_task:
    scene garden
    show diane b_shirtless a_shirtless_tired f_tired_down at lright
    show player 14 at left
    with dissolve
    player_name "Hello, {b}Diane{/b}."
    player_name "How are you-"
    show player 11
    player_name "!!!"
    show player 10
    player_name "Are you okay?"
    player_name "You look exhausted!"
    show player 5
    show diane f_tired_talk
    dia "Oh, yeah. I'm alright."
    dia "I just haven't gotten much sleep these past few days..."
    dia "This latest delivery is killing me!"
    show diane f_tired
    show player 10
    player_name "That's not good."
    player_name "Are you sure I can't help you milk the cow?"
    show player 12
    player_name "I really wouldn't mind."
    show player 5
    show diane f_tired_talk
    dia "I bet you wouldn't!"
    show diane f_laugh
    dia "Hahahaha!"
    show diane f_tired
    show player 11
    player_name "..."
    show diane f_tired_talk
    dia "Sorry, I'm a little loopy right now."
    show player 5
    dia "There's no need, stud."
    dia "I finished the order last night."
    show diane f_tired
    show player 12
    player_name "Oh."
    show player 14
    player_name "Well, that's good!"
    show player 13
    show diane f_tired_talk
    dia "You wouldn't mind delivering it for me again, would you?"
    show diane f_tired
    show player 14
    player_name "Of course not!"
    player_name "I'd love to deliver it for you."
    show player 13
    show diane f_tired_talk
    dia "Oh, you're a lifesaver, handsome!"
    hide player
    show diane kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane b_shirtless a_shirtless_tired f_tired_talk
    with dissolve
    dia "You won't have far to go; It's for the daycare next door."
    show diane f_tired
    show player 10
    player_name "Next door?"
    player_name "I think {b}Anne{/b} lives next door..."
    show player 5
    show diane f_tired_down
    dia "Hmm?"
    show player 12
    player_name "She's a girl from my class."
    show player 5
    show diane f_tired_talk
    dia "Oh, that must be {b}Lucy's daughter{/b}."
    show diane f_tired
    show player 12
    player_name "{b}Lucy{/b}? I dunno, maybe..."
    show player 5
    show diane f_tired_talk
    dia "Well, if she's anything like her mother, I'm sure she's delightful!"
    show diane f_tired
    show player 12
    player_name "... Yeah. I dunno about that."
    show player 5
    show diane f_tired_talk
    dia "Give them my regards, will you?"
    dia "I've gotta get some sleep."
    dia "... Just bring me the money when you're finished, okay?"
    show diane f_tired
    show player 14
    player_name "Sure thing, {b}Diane.{/b}"
    show player 13
    show diane f_tired_talk
    dia "Thanks, stud."
    show diane f_tired at Position (xpos=450) with dissolve
    show player 10
    player_name "Wait!!"
    show player 5
    dia "Hmm?"
    show player 12
    player_name "Where's the delivery?"
    show player 5
    show diane f_tired_down
    dia "..."
    show diane f_laugh
    dia "Oh! Hahahahaha!!"
    dia "Yeah, you'll probably need that, huh?"
    show diane f_tired_talk
    dia "It's in the shed."
    dia "I left it unlocked for you, handsome."
    show diane f_tired
    show player 17
    player_name "Okay, I'm on it."
    show player 13
    show diane f_tired_talk
    dia "Thanks again, handsome."
    hide diane
    hide player
    with dissolve
    return

label dianes_garden_diane_d9_intro:
    scene garden
    show player 10 at left
    show diane b_shirtless a_shirtless_tired f_tired
    with dissolve
    player_name "Hey, {b}Diane{/b}."
    player_name "Feeling better today?"
    show player 5
    show diane f_tired_talk
    dia "Hey, handsome."
    dia "I feel fine. Thanks for asking."
    show diane f_tired
    show player 10
    player_name "... You sure? You still look really tired."
    show player 5
    show diane f_tired_talk
    dia "Heh, do I?"
    show diane f_tired
    show player 10
    player_name "How much sleep did you get yesterday?"
    show player 5
    show diane f_tired_talk
    dia "I'm not sure."
    dia "I saw that note you left me about {b}Lucy's{/b} next order and I've been trying to get a head start on production."
    dia "It's strenuous but I'm just going to have to get used to it, I guess..."
    show diane f_tired
    show player 10
    player_name "What do you mean?"
    show player 5
    show diane f_tired_talk
    dia "Well, my orders aren't slowing down anytime soon."
    dia "As a matter of fact, they're getting bigger."
    show diane f_tired
    show player 10
    player_name "Yeah, but-"
    show player 5
    show diane f_tired_talk
    dia "I've even got a line on another new client."
    dia "My biggest yet."
    show diane f_tired
    show player 10
    player_name "{b}Diane{/b}..."
    player_name "You have to take care of yourself first..."
    player_name "Are you sure you aren't taking on too much, too quickly?"
    player_name "I worry about you."
    show player 5
    show diane f_tired_talk
    dia "Aww."
    dia "I appreciate your concern, {b}[firstname]{/b}, but you don't need to worry about me."
    dia "This business has been a dream of mine for a long time."
    dia "It'll take a lot more than a few sleepless nights to stop me from seeing it through."
    show diane f_tired
    show player 10
    player_name "... Alright, just..."
    show player 14
    player_name "... Remember I'm here to help if you need it."
    show player 13
    show diane f_tired_talk
    dia "Thanks, {b}[firstname]{/b}."
    hide player
    show diane kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane b_shirtless a_shirtless_tired f_tired_talk
    with dissolve
    dia "Well, I should get back to it."
    dia "Take good care of my garden, won't you?"
    show diane f_tired
    show player 14
    player_name "Of course."
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_shed_light_on:
    scene expression player.location.background_blur
    show player 4 with dissolve
    player_name "( Hmm? )"
    player_name "( {b}The door is open and the light is on!{/b} )"
    player_name "( She can't seriously still be working, can she? )"
    hide player with dissolve
    return

label dianes_garden_diane_missing:
    scene garden
    show player 127 with dissolve
    player_name "Where's {b}Diane{/b}?"
    show player 12
    player_name "She's usually outside around this time..."
    show player 56
    player_name "She must be somewhere."
    hide player 56 with dissolve
    return

label dianes_garden_diane_daylight_drinking:
    return

label dianes_garden_diane_ready_for_day_off:
    scene garden
    show player 14 at left
    show diane b_shirtless a_shirtless_sides at lright
    with dissolve
    player_name "Hey {b}Diane{/b}!"
    player_name "You ready for your day off?"
    show player 13
    show diane f_normal_talk
    dia "Hi, {b}[firstname]{/b}."
    dia "Hehe, yeah I guess..."
    dia "I just need to finish up this last batch I was working on this morning and-"
    show diane f_normal
    show player 33
    player_name "No, no, no..."
    show player 14
    player_name "You're done working today!"
    show player 13
    show diane f_normal_talk
    dia "... But I have to make sure everything is stored away correctly."
    show diane f_normal
    show player 14
    player_name "Just tell me what to do and I'll handle it."
    show player 17
    player_name "The rest of your day is all about relaxation!"
    show player 13
    show diane f_laugh a_shirtless_shock with dissolve
    dia "Hahaha. Okay, okay..."
    show diane f_normal_talk a_shirtless_sides with dissolve
    dia "{b}Just head into the shed and dump what's in the pump into a storage jug.{/b}"
    show diane f_normal
    show player 14
    player_name "That sounds easy enough."
    show player 13
    show diane f_normal_talk
    dia "... But you have to make sure you get the cap on tight!"
    show diane f_normal
    show player 14
    player_name "You just take a seat and I'll handle it, okay?"
    $ M_diane.is_naked = 0
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_return_drink:
    return

label dianes_garden_diane_drunken_shenanigans_apology:
    scene expression "backgrounds/location_diane_garden_closeup.jpg"
    show diane at flip
    show diane at Position (xpos=250)
    show vero f_normal_talk b_casual a_casual_front at Position (xpos=600)
    with dissolve
    vero "I just can't get over how good your garden is looking nowadays!"
    vero "I remember when it was just a sad little patch of tomatoes..."
    show vero f_normal
    show diane f_laugh
    dia "Haha, thanks {b}Vee{/b}!"
    show diane f_normal_talk
    dia "It certainly has come a long way..."
    show diane f_normal
    show vero f_normal_talk
    vero "It's really gorgeous, {b}Diane{/b}!"
    vero "Wow!!!"
    show vero bending at flip
    show vero at Position (xoffset=100)
    show diane f_down_front
    with dissolve
    pause
    hide vero
    show vero f_normal_talk b_casual a_cucumber1 at Position (xpos=600)
    show diane f_normal
    with dissolve
    vero "Look at the size of this one!"
    show vero f_normal
    show diane f_normal_talk
    dia "Yeah, I know!"
    show diane f_smirk_talk
    dia "He's a monster."
    show diane f_smirk
    show vero f_normal_talk a_cucumber2 with dissolve
    vero "I'll say..."
    show vero f_normal
    show diane f_normal_talk
    dia "You wanna take him home with you?"
    show diane f_wink
    show vero f_rolleyes a_cucumber1 with dissolve
    vero "Oh my gosh, I should never have told you about that..."
    show vero f_sexy
    show diane f_laugh a_dressed_finger with dissolve
    dia "Hey, I'm not one to judge."
    show diane f_normal a_dressed_shovel with dissolve
    show vero f_sexy_down
    vero "..."
    show vero f_sexy_talk_down
    vero "No, it's way too big for me!"
    show vero f_sexy_down
    show diane f_laugh
    dia "Haha, yeah. Me too."
    show diane f_smirk
    show vero f_surprised_down
    vero "Ahaha, I knew you'd try it!"
    show vero f_sexy a_casual_front with dissolve
    show diane f_smirk_talk
    dia "Yeah, yeah..."
    show diane f_smirk
    show vero f_sexy_talk
    vero "So what's your secret?"
    vero "You aren't using hormones on them or anything are you?"
    show vero f_sexy
    show diane f_normal_talk
    dia "Psh, of course not!"
    dia "I remember our discussion about that."
    show diane f_normal
    show vero f_sexy_talk
    vero "Good."
    show vero f_sexy
    show diane f_normal_talk
    dia "To be honest, I've left most of the gardening to my friend this year."
    show diane f_normal
    show vero f_normal_talk
    vero "Oh, you mean that cute one you brought into the store the other day?!"
    show vero f_normal
    show diane f_normal_talk
    dia "Don't get any ideas, {b}Vee{/b}!"
    dia "He's a good kid."
    show diane f_normal
    show vero f_normal_talk
    vero "Yeah, so?"
    show vero f_sexy_talk
    vero "I'm a nice girl..."
    show vero f_sexy
    show diane f_normal_talk
    dia "Uh huh."
    show diane f_normal
    show vero f_laugh
    vero "Hehehe!"
    show vero f_sexy
    show diane f_normal_talk
    dia "His guardian would kill me if I let you get your claws on him."
    show diane f_normal
    show vero f_sexy_talk
    vero "Aww, c'mon."
    show vero f_sexy
    show diane f_normal_talk a_dressed_finger with dissolve
    dia "Absolutely not, {b}Vee{/b}."
    show diane f_normal a_dressed_shovel with dissolve
    show vero f_sexy_talk
    vero "Tsk, you're no fun."
    show vero f_sexy
    pause
    show vero f_thinking
    vero "... Arrghh..."
    vero "Sometimes I really regret moving to this town."
    vero "The men here suck!"
    show vero f_normal
    show diane f_normal_talk
    dia "You don't have to tell me."
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "You're not thinking about moving back to the farm are you?"
    show diane f_normal
    show vero f_laugh
    vero "Oh, heck no!"
    show vero f_normal_talk
    vero "If I went back there with my tail between my legs, I'd never hear the end of it.!"
    vero "{b}*Sigh*{/b}"
    vero "I can't believe I've been working at {b}Consum-R{/b} for five years!"
    vero "It's so depressing..."
    show vero f_normal
    pause
    show vero f_normal_talk
    vero "Oh, that reminds me!"
    vero "I wanted to ask you how the new business is going?"
    show vero f_normal
    show diane f_normal_talk a_dressed_blush with dissolve
    dia "Oh, uhh..."
    show diane a_dressed_shovel with dissolve
    dia "It's going well, so far."
    show diane f_normal
    show vero f_normal_talk
    vero "You're still not ready to give me the details?"
    show vero f_normal
    show diane f_normal_talk
    dia "Mmm, not quite yet..."
    show diane f_normal
    show vero f_rolleyes
    vero "Ugh, fiiiine."
    show vero f_normal_talk
    vero "Just don't forget about me when you start making the big bucks!"
    vero "I'm a quick learner and I'll work hard for you {b}Diane{/b}."
    show vero f_normal
    show diane f_normal_talk
    dia "Heh, I know that {b}Vee{/b}..."
    dia "I just don't have enough work to warrant hiring an extra hand at the moment."
    dia "I promise, I'll call you as soon as I do."
    show diane f_normal
    show player 13 at left with dissolve
    show vero f_normal_talk
    vero "You had better."
    show vero f_normal
    show player 14
    player_name "Hello ladies."
    show player 13
    show vero f_sexy_talk
    vero "Uh oh, your boyfriend is here..."
    show vero f_sexy
    show diane f_normal_talk
    dia "Tch, shuddup {b}Vee{/b}!"
    show diane at unflip
    show diane at lcenter
    with dissolve
    dia "Ignore her, {b}[firstname]{/b}."
    show diane f_normal
    show vero f_sexy_talk
    vero "Oh, he knows I'm only teasing..."
    show vero f_normal_talk
    vero "We were just talking about this beautiful garden you've been working on."
    show vero f_normal
    show player 17
    player_name "It looks pretty good, huh?"
    show player 18
    show vero f_normal_talk
    vero "It looks better than good."
    vero "What's your secret?"
    show vero f_normal
    show player 10
    player_name "Huh?"
    show player 5
    show vero f_normal_talk
    vero "You've gotta be doing something special to get results like this."
    show vero f_normal
    show player 35
    player_name "Hmm, not really."
    show player 14
    player_name "I just till it, sow it, and water it."
    player_name "Like {b}Diane{/b} taught me."
    show player 13
    show vero f_normal_talk
    vero "That's it?"
    show vero f_normal
    show player 14
    player_name "Yup."
    show player 13
    pause
    show player 35
    player_name "Oh!"
    show player 14
    player_name "I have been fertilizing it with compost..."
    show player 10
    player_name "... Maybe that's my secret?"
    show player 13
    show diane f_laugh
    dia "Hahaha!"
    show vero f_laugh
    vero "Hehe, maybe..."
    show diane f_normal
    show vero f_normal
    pause
    show vero f_normal_talk
    vero "Well, I should probably get going..."
    show vero f_normal
    hide diane
    show diane f_normal_talk at flip
    show diane at Position (xpos=250)
    with dissolve
    dia "So soon?"
    show diane f_normal
    show vero f_normal_talk
    vero "Heh, Yeah. Those groceries at {b}Consum-R{/b} aren't going to sell themselves you know?!"
    show vero f_normal
    show diane f_normal_talk
    dia "Hah, I suppose not."
    hide vero
    show diane hug_vero_talk at Position (xoffset=200)
    with dissolve
    dia "Swing by anytime, alright?"
    show diane f_normal
    show vero f_normal_talk b_casual a_casual_front at Position (xpos=600)
    vero "Will do."
    show vero f_normal
    show player 14
    player_name "Bye {b}Veronica{/b}."
    player_name "Nice seeing you again."
    show player 13
    show vero f_normal_talk
    vero "Yeah, you too handsome."
    show vero f_sexy
    pause
    show vero f_sexy_talk
    vero "You know what?"
    vero "I think I'll take that cucumber afterall..."
    show vero bending at Position (xoffset=370)
    show diane f_down_front
    with dissolve
    pause
    show player 426
    vero "Hmm, now where did I put it..."
    show diane f_lookup
    dia "Oh, good grief!"
    show diane f_laugh
    dia "Haha, would you get out of here already!"
    show diane f_normal
    show vero f_sexy_talk b_casual a_cucumber1 at Position (xpos=600) with dissolve
    show player 13
    vero "Hehe, thanks again, {b}Diane{/b}!"
    hide vero with dissolve
    player_name "..."
    hide diane
    show diane f_normal_talk
    with dissolve
    dia "You ready to get to work, {b}stud{/b}?"
    show diane f_normal
    show player 10
    player_name "Hmm?"
    show player 14
    player_name "Oh!"
    player_name "Yup, I'm ready."
    show player 13
    show diane f_normal_talk
    dia "Glad to hear it."
    show diane f_shamed_talk_smile
    dia "... But uhh, before you get started..."
    show diane f_shamed
    show player 14
    player_name "Yeah?"
    show player 13
    show diane f_shamed_talk_smile a_dressed_blush with dissolve
    dia "I think I should apologize."
    show diane f_shamed a_dressed_shovel with dissolve
    show player 10
    player_name "Apologize?"
    show player 5
    show diane f_shamed_talk_smile
    dia "You know, the other day..."
    dia "... With the uhh-"
    dia "{b}*Ahem*{/b} I just had too much to drink and things got a little... Umm, inappropriate."
    show diane f_shamed
    player_name "..."
    show diane f_shamed_talk_smile
    dia "It's just been a long while since anyone has shown me that kind of attention and I've been lonely a lot recently and-"
    dia "Ugh, no. Damnit, that's no excuse... I-"
    show diane f_sad_talk
    dia "Look, I took advantage of you, {b}[firstname]{/b} and I'm really sorry... I-"
    show diane f_sad
    show player 14
    player_name "You didn't take advantage of me!"
    show player 13
    show diane f_sad_talk
    dia "Huh?"
    show diane f_sad
    show player 17
    player_name "It was awesome!"
    player_name "I was kinda hoping we could do it again sometime?"
    show player 13
    show diane f_shamed_talk_smile a_dressed_blush with dissolve
    dia "You wanna do it again?!"
    show diane f_shamed
    show player 26
    player_name "Of course. You're a beautiful woman, {b}Diane{/b}!"
    show player 13
    show diane f_shamed_talk_smile a_dressed_shovel with dissolve
    dia "O-okay, but-"
    dia "{b}[deb_name]{/b} trusted me to look after you and it wasn't right of me to-"
    show diane f_shamed
    show player 14
    player_name "I'm not a child, {b}Diane{/b}. And besides, it was fun!"
    show player 13
    show diane f_shamed_talk_smile
    dia "... And {b}[deb_name]{/b} would kill me if she found out."
    show diane f_shamed
    show player 14
    player_name "She doesn't have to know."
    show player 13
    dia "..."
    show player 14
    player_name "I mean, we're just having a little fun."
    player_name "I don't see the harm in it."
    show player 13
    show diane f_shamed_talk_smile
    dia "Hmm."
    dia "Wouldn't you rather do that stuff with girls your own age?"
    show diane f_shamed
    show player 14
    player_name "Are you kidding?!"
    player_name "You're like a million times hotter than the girls at my school, {b}Diane{/b}!"
    show player 13
    show diane f_laugh a_dressed_blush with dissolve
    dia "Oh, I am not!"
    show player 17
    player_name "Heh, it's true."
    show player 18
    show diane f_smirk a_dressed_shovel with dissolve
    pause
    show diane f_lookup
    dia "Alright, Mr. Charmer..."
    show diane f_smirk_talk
    dia "We're clearly not in the right mindset to have this conversation."
    dia "So, let's just focus on work, shall we?"
    show diane f_smirk
    show player 12
    player_name "Seriously?"
    show player 5
    show diane f_smirk_talk
    dia "Yes, seriously!"
    show diane f_normal_talk
    dia "I'll be in the shed if you need something."
    show diane f_normal
    show player 26
    player_name "You sure I can't give you a hand?"
    show player 13
    show diane f_laugh
    dia "Haha, no. I don't need a hand..."
    show diane f_smirk_talk
    dia "Nice try."
    show diane f_smirk
    show player 14
    player_name "What?!"
    show player 13
    show diane f_smirk_talk
    dia "Just get started on your garden work."
    show diane f_smirk
    show player 14
    player_name "Alright."
    show player 13
    hide diane with dissolve
    pause
    show player 5
    player_name "( Hmm, I hope I didn't upset her... )"
    player_name "{b}( I should probably leave her be for now and just focus on my work in the garden. ){/b}"
    hide player with dissolve
    return

label dianes_garden_diane_do_not_disturb:
    scene townmap
    player_name "I should visit {b}Diane{/b} another time..."
    return

label dianes_garden_diane_shed_still_open:
    show player 12 with dissolve
    player_name "That's strange..."
    show player 30
    player_name "{b}Diane's{/b} shed is {b}still open{/b}..."
    hide player 30 with dissolve
    return

label drink_offered:
    scene garden
    if M_diane.get("aunt_drink_made"):
        show player 137 with dissolve
    else:

        show player 12 with dissolve
    player_name "I should give {b}Diane{/b} her {b}drink{/b} before I get back to work..."
    $ game.main()

label aunt_masturbate_not_seen:
    show diane_masturbate 1_2
    player_name "!!!"
    player_name "( ... What is she... )"
    window hide
    pause 2
    player_name "( WOW... )"
    player_name "( She's playing with her vegetables... )"
    player_name "( A whole cucumber! )"
    player_name "( ... )"
    player_name "( ...I should leave before I get caught. )"
    scene garden
    with dissolve
    show player 113 with dissolve
    player_name "I can't believe I caught her masturbating!"
    show player 114
    player_name "... or that she's horny enough to do it with veggies!"
    show player 113
    player_name "Is that why she only wants {b}long{/b} and {b}hard{/b} ones?"
    show player 109f
    player_name "Hmm..."
    show player 108f
    player_name "I guess she has been lonely lately..."
    player_name "I should get back to work and pretend I didn't see anything..."
    hide player 108f with dissolve
    $ renpy.end_replay()
    return

label find_shovel:
    scene expression game.timer.image("garden{}")
    show player 12 with dissolve
    if player.has_item("shovel"):
        player_name "I should let {b}Diane{/b} know that I'm ready to start working."
    else:
        player_name "I need to find a {b}shovel{/b} before I can help with the garden..."
    hide player with dissolve
    $ game.main()


label before_masturbation:
    scene expression game.timer.image("garden{}")
    show player 34 with dissolve
    player_name "Hmmm..."
    show player 12
    player_name "I should find out if {b}Diane{/b} is home first."
    $ game.main()

label after_masturbation:
    scene expression game.timer.image("garden{}")
    show player 34 with dissolve
    player_name "Hmmm..."
    show player 12
    player_name "Maybe not right now."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
