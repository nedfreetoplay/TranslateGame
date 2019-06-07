label dianes_dialogue_daisy:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "How's {b}Daisy{/b} getting on?"
    show player 13
    show diane f_normal_talk
    dia "Oh, she's settling in great!"
    dia "Kinda funny that a dairy farmer would find a magical cow girl, isn't it?"
    dia "It's a good thing I built that barn..."
    show diane f_normal
    pause
    show diane f_laugh
    dia "She's a sweet girl."
    show diane f_normal
    show player 14
    player_name "Yeah, she is."
    show player 13
    show diane f_normal_talk
    dia "I'm so glad we found her."
    show diane f_normal
    return

label dianes_dialogue_cow_girl:
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_naked a_naked_sides
    with dissolve
    player_name "Any progress with our new friend?"
    show player 5
    show diane f_shamed_talk_smile
    dia "{b}*Sigh*{/b} That poor thing."
    dia "She's still half convinced her master is gonna pop up and punish her for letting us see her."
    dia "Whatever that awful man did to her, she's not ready to talk about it."
    show diane f_shamed
    show player 10
    player_name "Has she at least given you her name?"
    show player 5
    show diane f_shamed_talk_smile
    dia "No, not yet."
    dia "She's coming around though."
    dia "I imagine it won't be long till she's ready to speak with you."
    show diane f_shamed
    show player 10
    player_name "Okay."
    show player 5
    return

label dianes_dialogue_milk_sample:
    scene expression player.location.background_blur with None
    show diane b_naked a_naked_sides
    show player 14 at left
    player_name "Could I have a small sample of your milk?"
    show player 13
    show diane f_smirk_talk
    dia "Hehe, feeling thirsty, are we?"
    show diane f_smirk
    show player 29 with dissolve
    player_name "N-no, I really do just need a sample."
    show player 13 with dissolve
    show diane f_surprised
    pause
    show diane f_shamed_talk
    dia "Oh."
    dia "Uhh, sure. Just give me a second."
    if M_diane.outfit.get == "shirtless":
        show diane b_topless
    show diane a_squeeze3 f_down_front
    with dissolve
    pause
    show diane f_normal_talk a_bottle1 with dissolve
    dia "Will this work?"
    show diane b_naked f_normal a_naked_sides with dissolve
    show player 713
    with dissolve
    player_name "Yeah, this is perfect!"
    player_name "Thanks, {b}Diane{/b}!"
    show diane f_normal_talk
    hide player with dissolve
    dia "No pro-"
    show diane f_surprised
    pause
    show diane f_shamed_front
    dia "( What is he up to? )"
    hide diane with dissolve

    return

label dianes_dialogue_hows_baby_doing_boy:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "How's he doing?"
    show player 13
    show diane f_normal_talk
    dia "Oh, he's just wonderful!"
    dia "I never want to put him down."
    show diane f_normal
    show player 14
    player_name "Well, you'll have to put him down eventually..."
    show player 13
    show diane f_laugh
    dia "Nah uh!"
    show diane f_cheese
    show player 17
    player_name "Hehehe."
    show player 13
    return

label dianes_dialogue_hows_baby_doing_twins:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "How are they doing?"
    show player 13
    show diane f_normal_talk
    dia "Oh, they're just wonderful!"
    dia "I never want to put them down."
    show diane f_normal
    show player 14
    player_name "Well, you'll have to put them down eventually..."
    show player 13
    show diane f_laugh
    dia "Nah uh!"
    show diane f_cheese
    show player 17
    player_name "Hehehe."
    show player 13
    return

label dianes_dialogue_hows_baby_doing_girl:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "How's she doing?"
    show player 13
    show diane f_normal_talk
    dia "Oh, she's just wonderful!"
    dia "I never want to put her down."
    show diane f_normal
    show player 14
    player_name "Well, you'll have to put her down eventually..."
    show player 13
    show diane f_laugh
    dia "Nah uh!"
    show diane f_cheese
    show player 17
    player_name "Hehehe."
    show player 13
    return

label dianes_dialogue_get_anything_baby:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "Can I get you anything?"
    show player 13
    show diane f_normal_talk
    dia "No, I'm okay."
    dia "Thanks, stud."
    show diane f_normal
    show player 14
    player_name "You're welcome."
    show player 13
    show diane f_shamed_talk_smile
    dia "No really, thank you, {b}[firstname]{/b}."
    dia "For everything."
    show diane f_shamed
    show player 14
    player_name "It's my pleasure, {b}Diane{/b}."
    show player 13
    return

label dianes_dialogue_baby_leave:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "I'll leave you guys be."
    show player 13
    show diane f_normal_talk
    dia "Alright."
    show diane f_laugh
    dia "Say, bye bye, Daddy."
    show diane f_cheese
    show player 17
    player_name "Hehe."
    show player 36 with dissolve
    if M_diane.pregnancy.baby_gender == "twins":
        player_name "Goodbye, little ones."
    else:
        player_name "Goodbye, little one."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_gave_birth_intro:
    show player 14 at left
    show diane b_casual a_casual_baby
    with dissolve
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    if M_diane.pregnancy.baby_gender == "boy":
        dia "Shh, he's sleeping."
    elif M_diane.pregnancy.baby_gender == "twins":
        dia "Shh, they're sleeping."
    else:
        dia "Shh, she's sleeping."
    show diane f_normal
    show player 14
    player_name "Oh, sorry."
    show player 13
    return

label dianes_dialogue_intro_kitchen:
    scene expression player.location.background_blur
    show player 14 at left
    show diane b_nightgown a_nightgown_water
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Hey, {b}[firstname]{/b}."
    show diane f_normal
    show player 10
    player_name "You alright?"
    show player 5
    dia "Hmm?"
    show diane f_normal_talk
    dia "Yeah, I'm okay."
    show player 13
    dia "I was just thirsty so I came in here for a glass of water."
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "Now I'm just thinking..."
    show diane f_normal
    show player 14
    player_name "Thinking about what?"
    show player 13
    show diane f_laugh
    dia "Hehe, I dunno, work stuff I guess..."
    show diane f_normal
    show player 14
    player_name "O-okay."
    show player 13
    return

label dianes_dialogue_hows_business:
    show player 14 at left
    show diane b_naked a_naked_sides
    player_name "Have you had an easier time keeping up with all your orders now?"
    show player 13
    show diane f_laugh
    dia "Oh my, yes!"
    show diane f_normal_talk
    dia "I think my milk supply has more than doubled since the birth!"
    dia "Production is going very smoothly now."
    if M_diane.pregnancy.number_of_babies == 1:
        dia "I just have to make sure I leave some milk for the little one."
        show diane f_laugh
        dia "That child of ours is so hungry!"
    else:
        dia "I just have to make sure I leave some milk for the little ones."
        show diane f_laugh
        dia "Those children of ours are so hungry!"
    show diane f_normal
    show player 17
    player_name "Haha."
    show player 14
    player_name "Well, that milk of yours is so delicious... I can't blame them!"
    show player 13
    return

label dianes_dialogue_goodnight_1:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "I was just heading to bed."
    player_name "You need anything?"
    show player 13
    dia "Hmm?"
    show diane f_normal_talk
    dia "Oh, I'm fine stud."
    dia "Thanks for asking."
    show diane f_normal
    show player 14
    player_name "Alright then, goodnight."
    show player 13
    show diane f_normal_talk
    dia "Goodnight."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_goodnight_2:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Yeah, everything's fine."
    player_name "Sorry to wake you."
    show player 13
    show diane f_normal_talk
    dia "That's okay."
    show diane f_normal
    show player 14
    player_name "Goodnight."
    show player 13
    show diane f_normal_talk
    dia "Goodnight, stud."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_what_up_to:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "What are you up to?"
    show player 13
    show diane f_normal_talk
    dia "Oh, I'm just sitting here bored."
    dia "Late night TV sucks."
    show diane f_normal
    show player 14
    player_name "Heh, that's too true!"
    show player 13
    show diane f_smirk_talk
    dia "You wanna do something fun?"
    show diane f_smirk
    show player 10
    player_name "What did you have in mind?"
    show player 13
    show diane f_smirk_talk
    dia "Mmm, I can think of a few things..."
    show diane f_smirk
    return

label dianes_dialogue_on_my_way_debbie:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "I was on my way to see {b}[deb_name]{/b}."
    show player 13
    show diane f_normal_talk
    dia "Ahh, okay."
    dia "She's in her room."
    show diane f_normal
    show player 14
    player_name "I'll talk to you later, okay?"
    show player 13
    show diane f_normal_talk
    dia "Alright."
    show diane f_normal
    hide player with dissolve
    pause
    show diane f_smirk_talk
    dia "You two have fun."
    show diane f_laugh
    dia "Hehehe."
    hide diane with dissolve
    return

label dianes_dialogue_leave_d19_d20_day:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "I should check on the garden."
    show player 13
    show diane f_normal_talk
    dia "Okay."
    dia "Just don't forget that I need your help pumping too!"
    show diane f_normal
    show player 14
    player_name "I won't."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_hows_the_business:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    dia "Business is booming!"
    dia "I can barely keep up with all the orders!"
    show diane f_normal
    show player 14
    player_name "That's good, right?"
    show player 13
    show diane f_normal_talk
    dia "It's very good."
    show diane f_laugh
    dia "I'll have to start hiring more boobs soon."
    show diane f_cheese
    return

label dianes_dialogue_call_veronica:
    show player 10 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Have you talked with {b}Veronica{/b} yet?"
    show player 13
    show diane f_sad_talk
    dia "No, not yet."
    show diane f_normal_talk
    dia "I will though."
    show diane f_normal
    show player 14
    player_name "She'd really like to work for you."
    show player 13
    show diane f_laugh
    dia "Yeah, we'll see."
    show diane f_cheese
    return

label dianes_dialogue_what_are_you_up_to:
    show player 14 at left
    show diane f_normal b_nightgown a_nightgown_sides
    player_name "What are you doing?"
    show player 13
    show diane f_normal_talk
    dia "Oh, just watching some TV and sipping some of {b}[deb_name]'s{/b} delicious wine."
    dia "It's so nice having roommates again."
    show diane f_normal
    show player 14
    player_name "Is it?"
    show player 13
    show diane f_normal_talk
    dia "Of course!"
    dia "I was so lonely over there in that big house by myself."
    show diane f_normal
    show player 14
    player_name "Yeah, I can imagine."
    show player 13
    show diane f_normal_talk
    dia "Now I feel like I'm part of a family again."
    show diane f_normal
    show player 14
    player_name "You are part of our family {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Aww, thanks handsome."
    show diane f_normal
    return

label dianes_dialogue_wheres_debname:
    show player 10 at left
    show diane f_normal b_nightgown a_nightgown_sides
    player_name "Doesn't she usually sit out here with you?"
    show player 13
    show diane f_normal_talk
    dia "She went to bed early tonight..."
    dia "... Said she was tired."
    show diane f_normal
    show player 14
    player_name "Oh, I see."
    show player 13
    show diane f_normal_talk
    dia "You can still go and see her if you'd like, I'm sure she wouldn't mind."
    show diane f_normal
    show player 14
    player_name "Y-yeah, maybe..."
    show player 13
    return

label dianes_dialogue_love_that_nightgown:
    show player 14 at left
    show diane f_normal b_nightgown a_nightgown_sides
    player_name "It looks amazing on you!"
    show player 13
    show diane f_laugh a_nightgown_hip with dissolve
    dia "Hehe, thanks!"
    show diane f_reading_intrigued
    dia "I was worried it might be a little innapropriate but given what {b}[deb_name]{/b} and {b}[jen_name]{/b} prance around in..."
    show diane f_normal
    show player 14
    player_name "Heh, y-yeah."
    show player 426
    pause
    show diane f_smirk_talk
    dia "Hehe, you still with me handsome?"
    show diane f_smirk
    player_name "Hmm?"
    show player 29 with dissolve
    player_name "Oh, s-sorry!"
    show player 3
    show diane f_smirk_talk
    dia "Haha, it's alright."
    dia "You can look."
    show diane f_smirk
    show player 426 with dissolve
    pause
    pause
    show player 403
    show diane a_nightgown_sides with dissolve
    return

label dianes_dialogue_goodnight:
    show player 14 at left
    show diane f_normal b_nightgown a_nightgown_sides
    player_name "I should probably get to bed."
    show player 13
    show diane f_normal_talk
    dia "Yeah, me too."
    show diane f_normal
    show player 14
    player_name "Goodnight, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Goodnight, handsome."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_hows_the_couch:
    show player 14 at left
    show diane f_normal b_shirtless a_shirtless_sides
    player_name "You sleeping alright?"
    show player 13
    show diane f_normal_talk
    dia "Oh, it's fine."
    dia "A little lumpy but I'll manage."
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "You wanna hear something weird?"
    show diane f_normal
    show player 14
    player_name "Sure."
    show player 13
    show diane f_normal_talk
    dia "{b}[jen_name]{/b} keeps coming down in the middle of the night and huffing when she finds me laying there."
    dia "Then when I ask her what she needs, she rolls her eyes and storms off muttering something about wasting money."
    dia "Any idea what that's about?"
    show diane f_normal
    show player 29 with dissolve
    player_name "I uhh-"
    show player 3
    show diane f_normal_talk
    dia "What could she possibly want in the living room in the middle of the night?"
    show diane f_normal
    pause
    show player 10 with dissolve
    player_name "No idea."
    show player 5
    show diane f_thinking
    dia "{b}*Sigh*{/b} Probably just her way of trying to get under my skin."
    show diane f_normal
    show player 14
    player_name "Heh yeah, probably..."
    show player 13
    show diane f_annoyed_talk
    dia "She's such a bitch."
    show diane f_cheese
    return

label dianes_dialogue_feeling_better:
    show player 14 at left
    show diane f_normal
    player_name "How are you feeling?"
    show player 13
    show diane f_laugh
    dia "Oh, much better now that you're helping me pump!"
    show diane f_smirk_talk
    dia "Thank you for that, {b}[firstname]{/b}."
    show diane f_smirk
    show player 14
    player_name "You're welcome."
    player_name "Just make sure you get lots of rest, okay?"
    show player 13
    show diane f_laugh
    dia "Haha, okay, Dad!"
    show diane f_cheese
    show player 17
    player_name "Haha!"
    show player 13
    show diane f_smirk
    return

label dianes_dialogue_like_working_for_you:
    show player 14 at left
    show diane f_normal
    player_name "You know, I really enjoy this work {b}Diane{/b}."
    show player 13
    show diane f_laugh
    dia "Hah, I bet you do!"
    if M_diane.outfit.get == "dressed":
        show diane f_smirk_talk a_dressed_finger with dissolve
    else:
        show diane f_smirk_talk
    dia "What young man wouldn't enjoy handling breasts all day?"
    if M_diane.outfit.get == "dressed":
        show diane f_smirk a_dressed_shovel with dissolve
    else:
        show diane f_smirk
    show player 14
    player_name "That's not what I-"
    player_name "Heh, I mean... That part is pretty awesome."
    show player 401
    player_name "You have great boobs."
    show player 403
    show diane f_smirk_talk
    dia "Uh huh."
    show diane f_smirk
    show player 14
    player_name "... But it's not just that!"
    player_name "It feels nice taking care of you."
    player_name "I like it."
    show player 13
    if M_diane.outfit.get == "dressed":
        show diane f_smirk_talk a_dressed_blush with dissolve
    else:
        show diane f_smirk_talk
    dia "Aww."
    dia "I like it too, {b}[firstname]{/b}."
    if M_diane.outfit.get == "dressed":
        show diane f_smirk a_dressed_shovel with dissolve
    else:
        show diane f_smirk
    pause
    show diane f_smirk_talk
    dia "Just don't tell {b}[deb_name]{/b}!"
    show diane f_smirk
    show player 14
    player_name "Don't worry, I won't."
    show player 403
    return

label dianes_dialogue_leave_d12b:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "I'd better get back to it."
    show player 13
    show diane f_normal_talk
    dia "Alright."
    dia "If you need anything, you know where to find me."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_have_you_spoken_with_debname:
    show player 14 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    player_name "You talked with {b}[deb_name]{/b} lately?"
    show player 13
    show diane f_tired_talk
    dia "Oh, all the time!"
    dia "We're back to daily phone calls again."
    show diane f_tired
    show player 14
    player_name "That's nice."
    show player 13
    show diane f_tired_talk
    dia "It's been wonderful!"
    dia "I missed her so much!"
    show diane f_tired
    show player 14
    player_name "Well, she missed you too."
    player_name "We all did, really."
    show player 13
    show diane f_tired_talk
    dia "Aww."
    hide player
    if M_diane.outfit.get == "dressed":
        show diane kiss
    else:
        show diane kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    with dissolve
    return

label dianes_dialogue_about_veronica:
    show player 12 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    player_name "So how did you meet that girl {b}Veronica{/b}?"
    show player 13
    show diane f_tired_talk
    dia "You mean {b}Vee{/b}?"
    dia "Oh, I love that girl!"
    dia "We met in the gardening section of {b}Consum-R{/b}, a couple years ago."
    dia "She had just moved up here from the country and didn't know anybody."
    show diane f_tired
    show player 14
    player_name "I bet that was rough."
    show player 13
    show diane f_tired_talk
    dia "Oh, it certainly was."
    dia "She was a mess!"
    dia "I offered to show the poor dear around town in exchange for some gardening advice and we just sorta hit it off."
    show diane f_tired
    show player 14
    player_name "That was nice of you."
    show player 13
    show diane f_tired_talk
    dia "Yeah, I guess."
    dia "Truthfully, I was in need of a friend too."
    dia "What with {b}[deb_name]{/b} being so wrapped up with {b}your Dad{/b} and all."
    show diane f_tired
    show player 5
    player_name "..."
    pause
    show diane f_tired_talk
    dia "Oh, I'm sorry handsome!"
    dia "I didn't mean that to sound like a bad thing."
    show diane f_tired
    show player 10
    player_name "Yeah, I know you didn't."
    show player 5
    show diane f_tired_talk
    dia "Your {b}Father{/b} was a good man, I always liked him."
    show diane f_tired
    show player 10
    player_name "Thanks."
    show player 5
    return

label dianes_dialogue_hows_the_garden_2:
    show player 14 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    player_name "So I'm really doing okay with the garden?"
    show player 13
    show diane f_tired_talk
    dia "You're doing better than okay!"
    dia "I've never see my garden looking this good!"
    dia "I might have the finest cucumbers in all the land!"
    show diane f_tired
    show player 14
    player_name "Hah, I dunno about that..."
    player_name "I'm glad it turning out so well though."
    show player 13
    return

label dianes_dialogue_take_it_easy:
    show player 14 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    player_name "Alright, I guess I should get back to work."
    show player 10
    player_name "Take it easy, okay?"
    player_name "I worry about you working yourself too hard."
    show player 5
    show diane f_tired_talk
    dia "Psh, you sound just like {b}[deb_name]{/b}..."
    dia "I'll be fine."
    show diane f_tired
    show player 10
    player_name "Okay..."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_about_debname:
    show player 14 at left
    show diane f_normal
    player_name "I'm glad you're spending time with {b}[deb_name]{/b} again."
    player_name "I know she's been missing your company."
    show player 13
    show diane f_normal_talk a_dressed_blush with dissolve
    dia "Aww and I missed hers!"
    show diane a_dressed_shovel with dissolve
    dia "We were inseperable in our younger years, you know?"
    show diane f_normal
    show player 14
    player_name "Yeah, I've heard the stories."
    show player 13
    show diane f_laugh
    dia "Hah!"
    show diane f_smirk_talk a_dressed_finger with dissolve
    dia "Well, I hope she hasn't told you all the stories!"
    show diane f_smirk a_dressed_shovel with dissolve
    show player 10
    player_name "Huh?"
    show player 13
    show diane f_laugh
    dia "Hehe, nevermind."
    show diane f_normal
    show player 14
    player_name "I still can't get over how much you two look alike..."
    show player 13
    show diane f_normal_talk
    dia "Yeah, we used to get that all the time."
    dia "They called us twins in college."
    show diane f_normal
    show player 14
    player_name "I can see that."
    show player 13
    show diane f_normal_talk
    dia "I was the wild one and she was the pretty one!"
    show diane f_normal
    show player 29 with dissolve
    player_name "I think you're both pretty, {b}Diane{/b}."
    show player 3
    show diane f_shamed_talk_smile a_dressed_blush with dissolve
    dia "Aww, thanks handsome."
    show diane f_normal a_dressed_shovel with dissolve
    show player 13 with dissolve
    return

label dianes_dialogue_hows_the_garden:
    show player 14 at left
    show diane f_normal
    player_name "So how's your garden doing?"
    show player 13
    show diane f_sad_talk
    dia "It's definitely seen better days..."
    dia "I've been so pre-occupied with side work lately, I'm afraid my garden just doesn't get the attention it deserves."
    show diane f_normal_talk
    dia "That's why I was so excited when {b}[deb_name]{/b} said you might be able to help me this summer."
    show diane f_normal
    show player 14
    player_name "I'm happy to help, {b}Diane{/b}!"
    show player 13
    return

label dianes_dialogue_what_have_you_been_up_to:
    show player 14 at left
    show diane f_normal
    player_name "So what have you been doing with yourself these past few years?"
    show player 13
    show diane f_normal_talk
    dia "Oh, not much really..."
    show diane f_normal
    show player 14
    player_name "Not much?!"
    player_name "I thought you were out there partying like crazy and getting chased by rich men?"
    show player 13
    show diane f_laugh a_dressed_blush with dissolve
    dia "Haha, goodness no!"
    dia "Whatever gave you that idea?"
    show diane f_normal a_dressed_shovel with dissolve
    show player 14
    player_name "Well, {b}[deb_name]{/b} always says you're the wild one."
    show player 13
    show diane f_smirk_talk a_dressed_finger with dissolve
    dia "Well, perhaps in my younger days..."
    show diane f_normal_talk a_dressed_shovel with dissolve
    dia "Honestly, since the divorce, I spend most of my time right here in this garden."
    show diane f_normal
    show player 14
    player_name "You mean, you don't go out at all anymore?"
    show player 13
    show diane f_normal_talk
    dia "Occasionally I'll go out for a drink with my friend {b}Veronica{/b}."
    dia "Nothing too exciting."
    show diane f_normal
    show player 14
    player_name "Don't you miss it?"
    show player 13
    show diane f_normal_talk
    dia "Hmm, sometimes."
    dia "I'm too old for that kind of life now."
    show diane f_smirk_talk
    dia "Besides, there's no good men left in this town."
    show diane f_smirk
    show player 12
    player_name "Really?!"
    show player 13
    show diane f_laugh
    dia "Heh, trust me."
    show diane f_smirk_talk
    dia "At my age, the only thing left is the dregs."
    show diane f_smirk
    show player 10
    player_name "Bummer."
    show player 5
    return

label dianes_dialogue_intro_d1_d6:
    show player 13 at left
    show diane f_normal_talk
    with dissolve
    dia "Hey there, {b}[firstname]{/b}!"
    dia "I'm so glad you decided to come and help me."
    show diane f_normal
    show player 14
    player_name "Yeah, it's no problem {b}Diane{/b}."
    player_name "Thanks for paying me!"
    show player 13
    show diane f_laugh
    dia "Hehe, my pleasure handsome."
    show diane f_normal
    return

label dianes_dialogue_intro_d7_d12:
    show player 5 at left
    show diane f_tired_talk b_naked a_magic_dressed_shovel_shirtless_sides
    with dissolve
    dia "Hey, {b}[firstname]{/b}."
    dia "My garden is looking really-"
    dia "*Yawn*"
    dia "... Really nice."
    show diane f_tired
    show player 10
    player_name "You alright, {b}Diane{/b}?"
    show player 5
    show diane f_tired_talk
    dia "Yeah, I'm okay."
    dia "Just tired."
    show diane f_tired
    return

label dianes_dialogue_intro_d12b_d15:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    dia "Hey there, handsome!"
    show diane f_normal
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "You need something?"
    show diane f_normal
    return

label dianes_dialogue_intro_d16_d18_barn:
    show player 13 at left
    show diane f_normal_talk b_shirtless a_shirtless_sides
    with dissolve
    dia "Hey there, stud!"
    show diane f_normal
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "You ready to work?"
    show diane f_normal
    return

label dianes_dialogue_intro_d16_d18_couch:
    show player 13 at left
    show diane f_normal_talk b_nightgown a_nightgown_sides
    with dissolve
    dia "Hey there, stud!"
    show diane f_normal
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "You heading to bed?"
    show diane f_normal
    show player 14
    player_name "Yeah, in a couple minutes."
    show player 13
    return

label dianes_dialogue_intro_d19_d20_barn:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    with dissolve
    dia "Hey there, stud!"
    show diane f_normal
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "You ready to work?"
    show diane f_normal
    return

label dianes_dialogue_intro_d19_couch:
    show player 13 at left
    show diane f_smirk_talk b_nightgown a_nightgown_sides
    with dissolve
    dia "Hey there, stud!"
    show diane f_smirk
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "You looking for me or {b}[deb_name]{/b}?"
    show diane f_normal
    return

label dianes_dialogue_intro_d20_couch:
    show player 13 at left
    show diane f_normal_talk b_nightgown a_nightgown_sides
    with dissolve
    dia "Hmm, {b}[firstname]{/b}?"
    show diane f_normal
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Everything alright?"
    show diane f_normal
    return

label dianes_dialogue_ready_to_pump:
    show player 14 at left


    show diane f_normal b_naked a_naked_sides
    with dissolve
    player_name "You ready to pump?"
    show player 13
    show diane f_normal_talk
    dia "Absolutely."
    dia "Just give me one second to get set up."
    hide diane with dissolve
    show player 14
    player_name "O-okay."
    return

label dianes_dialogue_hows_the_baby_pregnancy_1:
    show player 13 at left
    show diane b_naked a_naked_sides f_normal_talk
    with dissolve
    dia "Oh, there's not much to report yet."
    dia "Unless you're interested in hearing about my morning sickness?"
    show diane f_normal
    show player 10
    player_name "Well, if you want to talk about it, we can?"
    show player 13
    show diane f_laugh
    dia "Haha, oh goodness no!"
    show diane f_normal_talk
    dia "I appreciate you asking though."
    dia "Thanks, {b}[firstname]{/b}."
    show diane f_normal
    return

label dianes_dialogue_hows_the_baby_pregnancy_2:
    show player 13 at left
    show diane b_naked a_naked_sides f_normal_talk
    with dissolve
    dia "Oh, there's not much to report yet."
    dia "Unless you're interested in hearing about my morning sickness?"
    show diane f_normal
    show player 10
    player_name "Well, if you want to talk about it we can?"
    show player 13
    show diane f_laugh
    dia "Haha, oh goodness no!"
    show diane f_normal_talk
    dia "I appreciate you asking though."
    dia "Thanks, {b}[firstname]{/b}."
    show diane f_normal
    return

label dianes_dialogue_hows_the_baby_pregnancy_3:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    with dissolve
    dia "Heh, my tits are so swollen!"
    dia "Do they look bigger to you?"
    show diane f_normal
    show player 26
    player_name "I dunno, they were pretty big to begin with..."
    show player 18
    show diane f_normal_talk
    dia "Oh, c'mon!"
    show player 13
    dia "They're definitely bigger!"
    show diane f_normal
    pause
    show player 14
    player_name "I just love your little baby bump!"
    show player 13
    show diane f_laugh a_touch_belly with dissolve
    dia "Hehe, I know!"
    show diane f_normal_talk
    dia "Isn't it adorable?"
    show diane f_normal
    pause
    show diane f_normal_talk a_naked_sides with dissolve
    dia "Thanks for checking in with me, {b}[firstname]{/b}."
    show diane f_normal
    show player 14
    player_name "Of course."
    player_name "I can't wait to meet our baby, {b}Diane{/b}!"
    show player 13
    show diane f_normal_talk
    dia "Aww, you're the sweetest man in the world!"
    show diane f_normal
    return

label dianes_dialogue_hows_the_baby_pregnancy_4:
    show player 13 at left
    show diane f_tired_talk b_naked a_naked_sides
    with dissolve
    dia "Ugh, I'm exhausted..."
    show player 5
    dia "My feet are killing me, I look like a whale, and my tits never stop leaking!"
    show diane f_tired
    show player 10
    player_name "... Oh."
    show player 5
    show diane f_laugh
    dia "Hehe, but it's okay."
    show diane f_normal_talk a_touch_belly with dissolve
    dia "I'm gonna be a mommy very soon!"
    show diane f_normal
    show player 14
    player_name "That's right, you are!"
    show player 13
    show diane f_normal_talk
    dia "I'm so excited, {b}[firstname]{/b}!"
    dia "I can't wait to hold our child in my arms!"
    show diane f_normal
    show player 14
    player_name "Yeah, me too."
    show player 13
    show diane a_naked_sides
    with dissolve
    return

label dianes_dialogue_breeding_session:
    show player 13 at left
    show diane b_naked a_naked_sides f_smirk_talk
    with dissolve
    dia "You ready to get started?"
    show diane f_smirk
    show player 14
    player_name "S-sure."
    show player 13
    show diane f_smirk_talk
    dia "Thank goodness!"
    dia "I'm getting so wet just thinking about that big dick of your's putting a baby inside me..."
    show diane f_smirk
    show player 10
    player_name "You are?!"
    hide player
    show diane b_pull_mc_naked f_empty a_empty
    with dissolve
    dia "Mmm, I need it so bad, {b}[firstname]{/b}!"
    hide diane
    with dissolve
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed_mc
    show diane_sex_breed pre_talk
    with dissolve
    dia "That's it, stud."
    dia "Give it to me."
    hide diane_sex_breed_mc
    show diane_sex_breed insert_and_pullout
    with dissolve
    pause
    show diane_sex_breed creampie_pullout with dissolve
    pause 1
    show diane_sex_breed creampie
    dia "Ahh!!"
    return

label dianes_dialogue_cow_suit:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "I wanted to talk to you about your cow outfit..."
    show player 13
    show diane f_normal_talk
    dia "Oh?"
    show diane f_normal
    menu:
        "Put it back on." if M_diane.outfit.get == "naked":
            show player 14 at left
            show diane f_normal
            player_name "I want you to wear it while I breed you."
            player_name "It's so sexy!"
            show player 13
            show diane f_laugh
            dia "Oh, I'm so happy you think so!"
            show diane f_normal_talk
            dia "I love it too!"
            show diane f_smirk_talk
            dia "It just feels right, you know?"
            dia "Wearing it in here."
            show diane f_smirk
            show player 14
            player_name "Yeah, totally."
            hide diane
            with dissolve
            $ M_diane.outfit.is_naked = 0
            $ M_diane.outfit.set_default_outfit_schedule([["cow","cow","nightgown","nightgown"]])

        "Could you remove it?" if not M_diane.outfit.get == "naked":
            show player 14 at left
            show diane f_normal
            player_name "I'd rather have you completely naked."
            show player 13
            show diane f_smirk_talk
            dia "You would?!"
            dia "Mmm, you naughty boy..."
            show diane f_smirk
            pause
            show diane f_smirk_talk
            dia "I can take it off, if that's what you really want."
            dia "Whatever helps you put a baby in my belly."
            hide diane
            with dissolve
            $ M_diane.outfit.set_default_outfit_schedule([["naked","naked","nightgown","nightgown"]])
    return

label dianes_dialogue_dump_pump:
    scene garden
    show player 10 at left
    show diane b_shirtless a_shirtless_sides
    with dissolve
    player_name "What did I need to do again?"
    show player 13
    show diane f_normal_talk
    dia "Hmm?"
    dia "Oh, {b}just head into the shed and dump what's in the pump into a storage jug.{/b}"
    show diane f_normal
    show player 14
    player_name "Right!"
    player_name "I'm on it!"
    hide player
    hide diane with dissolve
    return

label dianes_dialogue_daylight_drinking:
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show player 429 zorder 0 at Position (xpos=175,ypos=648)
    show diane_chair up
    show diane b_laying_back_shirtless a_laydown f_laying_smirk_up at Position (ypos=982)
    with dissolve
    player_name "How are you doing over here?"
    show player 426
    show diane f_laying_laugh
    dia "Mmm, fantastic!"
    show diane f_laying_smirk_up
    show player 429
    player_name "Can I get you anything?"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "I wouldn't say no to a drink."
    show diane f_laying_smirk_up
    show player 429
    player_name "Your wish is my command!"
    player_name "What kind of drink do you want?"
    show player 426
    $ randomdrink = M_diane.get("random drink")
    show diane f_laying_thinking
    dia "How about a {b}[randomdrink]{/b}?"
    show diane f_laying_smirk_up
    show player 427
    player_name "{b}[randomdrink]{/b}?!"
    player_name "I've never made anything like that before..."
    show player 426
    show diane f_laying_laugh
    dia "Hehe, no worries. I'll do it."
    show diane f_laying_smirk_up
    show player 429
    player_name "No! I can figure it out."
    player_name "You just relax on your day off!"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "You're sure?"
    show diane f_laying_smirk_up
    show player 429
    player_name "Positive!"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "Okay. Well, {b}the recipe is inside on a note pad next to the mixer.{/b}"
    show diane f_laying_smirk_up
    show player 429
    player_name "Got it!"
    player_name "One {b}[randomdrink]{/b}, coming right up!"
    hide player
    hide diane
    hide diane_chair
    with dissolve
    return

label dianes_dialogue_make_drink:
    $ randomdrink = M_diane.get("random drink")
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show player 427 zorder 0 at Position (xpos=175,ypos=648)
    show diane_chair up
    show diane b_laying_back_shirtless a_laydown f_laying_smirk_up at Position (ypos=982)
    with dissolve
    player_name "What drink did you want again?"
    show player 426
    show diane f_laying_thinking
    dia "Hmm, a {b}[randomdrink]{/b} would be nice."
    show diane f_laying_smirk_up_talk
    dia "{b}The recipe is inside on a note pad next to the mixer.{/b}"
    show diane f_laying_smirk_up
    show player 429
    player_name "One {b}[randomdrink]{/b}, coming right up!"
    hide player
    hide diane
    hide diane_chair
    with dissolve
    return

label dianes_dialogue_diane_fetch_pump:
    show player 10 at left
    show diane f_normal
    with dissolve
    player_name "What did you need me to do again?"
    show player 5
    show diane f_normal_talk
    dia "Just fetch me the {b}tool{/b} I left on the {b}kitchen counter.{/b}"
    show diane f_normal
    show player 14
    player_name "Oh, right!"
    player_name "I'll be right back!"
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_diane_got_pump:
    scene garden
    show player 239_240 at left
    show diane at lright
    with dissolve
    pause
    show player 103 at Position (xoffset=38) with dissolve
    player_name "Is this what you needed?"
    show player 13
    show diane a_dressed_pump f_normal_talk
    with dissolve
    dia "Yup!"
    show diane f_normal
    show player 10
    player_name "What is this thing anyways?"
    show player 13
    show diane f_normal_talk
    dia "You've never seen a breast pump before?"
    show diane f_normal
    show player 10
    player_name "... No?"
    show player 12
    player_name "It's a pump?"
    show player 5
    dia "Mmmhmm."
    show player 10
    player_name "How does it work?"
    show player 5
    show diane f_explain
    dia "Hehe, well you put this end over the nipple and then press the lever here and it sucks the milk out of the teet and into this container."
    show diane f_normal
    show player 14
    player_name "Whoa!"
    show player 10
    player_name "... And it doesn't hurt the cow?"
    show player 13
    show diane f_laugh a_dressed_blush with dissolve
    dia "Hahaha!"
    dia "No, handsome."
    show diane f_normal_talk a_dressed_shovel with dissolve
    dia "It feels really good!"
    show diane f_shamed_talk_smile
    dia "You know, for the uhh... Cow."
    show diane f_shamed
    show player 14
    player_name "Can I try milking the cow sometime?"
    show player 13
    show diane f_laugh
    dia "Haha, I don't think that's a good idea, handsome."
    show diane f_smirk_talk a_dressed_finger with dissolve
    dia "For now you just work on the garden, okay?"
    show diane f_smirk a_dressed_shovel with dissolve
    show player 14
    player_name "... Okay."
    show player 13
    show diane f_smirk_talk
    dia "If you need me, I'll be in here."
    dia "Just knock first, got it?."
    show diane f_smirk
    show player 14
    player_name "Yeah, I've got it."
    show player 13
    show diane f_laugh
    dia "Hehe, thanks stud."
    hide player
    hide diane
    with dissolve
    return


label dianes_dialogue_delivery_1_reminder:
    scene garden
    show player 10 at left
    show diane
    with dissolve
    player_name "Where am I supposed to deliver this milk again?"
    show player 5
    show diane f_normal_talk
    dia "You need to take that order to {b}Tony{/b} down at {b}Tony's Pizzeria{/b}."
    show diane f_normal
    show player 14
    player_name "Oh yeah, I know that place!"
    player_name "Alright, I'll be back in a flash."
    show player 13
    show diane f_normal_talk
    dia "Thanks, {b}[firstname]{/b}!"
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_delivery_1_done:
    scene garden
    show diane f_normal
    show player 640e at left
    with dissolve
    player_name "I made your delivery for you."
    show player 13
    show diane f_normal_talk a_dressed_money
    with dissolve
    dia "Oh, thank you so much {b}[firstname]{/b}!"
    show diane a_dressed_shovel with dissolve
    dia "Did {b}Tony{/b} say anything?"
    show diane f_normal
    show player 14
    player_name "Uh huh, he said the milk had really taken their pizzas to a whole new level!"
    show player 13
    show diane f_normal_talk
    dia "{b}*Gasp*{/b}"
    dia "So he liked it?!"
    show diane f_normal
    show player 14
    player_name "Heh, I'd say so."
    show player 17
    player_name "He wants to triple his next order!"
    show player 13
    show diane f_sad_talk
    dia "Triple?!"
    show diane f_surprised_front
    dia "Hmm..."
    show player 12
    player_name "Is that a problem?"
    show player 5
    show diane f_shamed_front_talk
    dia "Huh? Oh... Well, I'm not sure."
    dia "I've don't know if I can handle-"
    show diane f_surprised
    pause
    show diane f_smirk_talk
    dia "I mean, my cow..."
    dia "... I don't know if she can handle that much demand."
    show diane f_smirk
    show player 12
    player_name "Sounds like you might need to expand and get more cattle."
    show player 13
    show diane f_thinking
    dia "..."
    show diane f_thinking_back
    dia "I'm defintely not ready for that yet."
    dia "I'll just have to push her harder and start stockpiling..."
    show diane f_normal
    show player 14
    player_name "Can I do anything to help?"
    show player 13
    show diane f_normal_talk
    dia "Heh, no that's alright."
    dia "You've helped me plenty already."
    show diane f_normal
    player_name "..."
    show diane f_normal_talk
    dia "Why don't you get back to your garden work?"
    show diane f_normal
    show player 14
    player_name "Yeah, okay..."
    show player 13f with dissolve
    show diane f_teasing
    dia "Oh!"
    show diane f_normal
    show player 13 with dissolve
    show diane f_normal_talk
    dia "... I almost forgot."
    show diane a_dressed_money with dissolve
    dia "This is yours."
    show diane f_normal a_dressed_shovel
    show player 640c
    with dissolve
    player_name "Huh? This is the entire payment from the delivery!"
    show player 640b
    show diane f_normal_talk
    dia "Hehe, I told you, {b}[firstname]{/b}. This isn't a money making endeavor for me."
    show diane f_smirk_talk
    dia "At least not for the moment."
    show diane f_smirk
    player_name "..."
    show diane f_normal_talk
    dia "You take it and put it towards your tuition."
    show diane f_normal
    show player 14 with dissolve
    player_name "Thanks, {b}Diane{/b}!"
    show player 13
    show diane f_laugh
    dia "You're welcome, handsome!"
    hide player
    show diane kiss
    with dissolve
    pause
    hide diane with dissolve
    return

label dianes_dialogue_leave_d1:
    show player 14 at left
    show diane f_normal
    player_name "I should probably get started on the garden."
    show player 13
    show diane f_normal_talk
    dia "Alright."
    dia "Thanks again for helping!"
    show diane f_normal
    show player 14
    player_name "No problem."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_delivery_3_reminder:
    show player 10 at left
    show diane b_naked a_naked_sides at lright
    with dissolve
    player_name "What was I supposed to do again?"
    show player 13
    show diane f_normal_talk
    dia "{b}Take the package of milk from my shed and deliver it to the cafeteria at your school.{/b}"
    show diane f_normal
    show player 14
    player_name "Oh, right."
    player_name "I'm on it!"
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_pre_fun_paint:
    show player 10
    player_name "{b}[deb_name]{/b} said she gave the old paint in the garage."
    player_name "You still have it right?"
    show player 5
    if L_diane_garden.is_here(M_diane):
        show diane f_laugh
    else:
        show diane b_naked a_naked_sides f_laugh
    dia "Well, sure I do!"
    if L_diane_garden.is_here(M_diane):
        show diane f_normal
    else:
        show diane b_naked a_naked_sides f_normal
    show player 13
    if L_diane_garden.is_here(M_diane):
        show diane f_normal_talk
    else:
        show diane b_naked a_naked_sides f_normal_talk
    dia "There should be some left in the shed."
    dia "Help yourself!"
    if L_diane_garden.is_here(M_diane):
        show diane f_normal
    else:
        show diane b_naked a_naked_sides f_normal
    show player 14
    player_name "Thanks!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
