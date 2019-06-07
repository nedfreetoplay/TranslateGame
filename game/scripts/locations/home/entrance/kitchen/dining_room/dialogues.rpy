label dining_room_jenny_have_breakfast_4:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_magic_sit_stand_worried zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show jenny f_breakfast_upset_talk
    jen "About time..."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "What is your problem?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "We've got a big show today."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Big show?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "That's right so eat up."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "What do you-"
    show player f_diningroom_table_surprised_left
    deb "Good morning, sweetheart!"
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal
    show player f_diningroom_table_normal_talk
    player_name "Morning, {b}[deb_name]{/b}."
    show player f_diningroom_table_normal
    show debbie f_breakfast_standing_normal_talk
    deb "I hope you're hungry."
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_eyeroll
    show player f_diningroom_table_normal_talk
    player_name "Starving."
    show player f_diningroom_table_normal
    show jenny f_breakfast_normal_talk
    jen "{b}[deb_name]{/b}, do you know where my uniform is?"
    show jenny f_breakfast_normal
    show debbie f_breakfast_standing_normal_talk
    deb "What uniform, dear?"
    show debbie f_breakfast_standing_normal
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    show jenny f_breakfast_normal_talk
    jen "You know, from college..."
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting with dissolve
    show jenny f_breakfast_normal
    show debbie f_breakfast_standing_normal_talk
    deb "You mean, your cheerleading costume?"
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_upset_talk
    jen "{b}[deb_name]{/b}, it's a uniform!"
    show jenny f_breakfast_upset
    show debbie f_breakfast_standing_normal_talk
    deb "Okay, okay, uniform."
    show debbie f_breakfast_standing_sorry
    deb "Umm..."
    show debbie f_breakfast_standing_normal_talk
    deb "It's probably stored away in the attic with the rest of our old clothes..."
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_surprised
    jen "In the attic?!"
    show jenny f_breakfast_angry_talk
    show player f_diningroom_table_surprised_left_food
    jen "Damnit, {b}[deb_name]{/b}!"
    show debbie f_breakfast_standing_surprised
    jen "It's going to be covered in dust and cobwebs!"
    show jenny f_breakfast_angry_pouting
    show debbie f_breakfast_standing_sad_talk
    deb "Well, I'm sorry dear..."
    show player f_diningroom_table_surprised_high_food
    deb "I dunno-"
    show debbie f_breakfast_standing_sad
    pause
    show debbie f_breakfast_standing_sorry_talk
    deb "What do you need that old thing for anyways?"
    deb "It probably won't even fit you now."
    show debbie f_breakfast_standing_sorry
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_upset_talk
    jen "Yeah, I know but my fans-"
    show jenny f_breakfast_surprised
    jen "Err... I mean, I-"
    show jenny f_breakfast_surprised_back
    pause
    show jenny f_breakfast_upset_talk
    jen "{b}*Sigh*{/b} It's not important, just nevermind."
    show jenny f_breakfast_upset
    show debbie f_breakfast_standing_normal_talk
    show player f_diningroom_table_surprised_high_food
    deb "Would you like me to get it down and wash it for you?"
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_upset_talk
    show player f_diningroom_table_surprised_left_food
    jen "Ugh, I said forget it, {b}[deb_name]{/b}!!"
    show debbie f_breakfast_standing_sad
    show jenny f_breakfast_upset
    menu:
        "Remain Silent {color=7ff7}[[Submissive]{/color}":
            show player f_diningroom_table_surprised_teeth_down
            player_name "..."
            show debbie f_breakfast_standing_sad_talk
            deb "O-okay, dear."
            hide debbie with dissolve
            pause
            show jenny f_breakfast_upset_talk
            jen "Why does nothing ever go right in this house?!"
            show jenny f_breakfast_upset
            show player f_magic_sit_stand_worried_talk
            player_name "I don't know."
            show player f_magic_sit_stand_worried
            $ M_jenny.decrement("dominance")
        "Say Something {color=f77b}[[Dominant]{/color}":
            show player f_diningroom_table_grumpy_food_left_talk
            player_name "Hey, don't talk to {b}[deb_name]{/b} like that!"
            show player f_diningroom_table_grumpy_food_left
            show debbie f_breakfast_standing_surprised
            deb "!!!"
            $ M_jenny.increment("dominance")
            if M_jenny.get("dominance") <= 0:
                show jenny f_breakfast_angry_talk
                jen "What did you say?!"
                show jenny f_breakfast_angry
                show debbie f_breakfast_standing_sad
                show player f_diningroom_table_grumpy_food_left_talk
                player_name "She's just trying to help!"
                show player f_diningroom_table_grumpy_food_left
                pause
                show jenny f_breakfast_angry_talk
                jen "Well, I didn't ask for her help, did I?!"
                show jenny f_breakfast_angry
                show player f_diningroom_table_grumpy_food_left_talk
                player_name "I wasn't-"
                show player f_diningroom_table_surprised_talk_food
                player_name "I didn't mean to-"
                show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting
                show jenny f_breakfast_angry_talk
                jen "Mind your own business, loser!"
                show jenny f_breakfast_angry
                show player f_diningroom_table_shy_down with dissolve
                player_name "..."
                show debbie f_breakfast_standing_sad_talk
                deb "Would you two please not fight at the breakfast table?!"
                hide debbie with dissolve
                deb "I just don't understand where she gets that temper from..."
            else:
                show jenny f_breakfast_angry
                show player f_diningroom_table_grumpy_food_left_talk
                player_name "She's just trying to help!"
                show debbie f_breakfast_standing_sad
                player_name "You know, kinda like I WAS going to help you with your new job..."
                player_name "... But now I'm thinking I won't bother."
                show player f_diningroom_table_grumpy_food_left
                show jenny f_breakfast_surprised
                jen "That's not-"
                show jenny f_breakfast_surprised_down
                jen "I didn't mean to-"
                show player f_diningroom_table_worried_talk_high with dissolve
                player_name "{b}[jen_name]{/b} is sorry."
                show player f_magic_sit_stand_worried_talk
                player_name "Aren't you?!"
                show player f_magic_sit_stand_worried
                show jenny f_breakfast_angry
                pause
                show player f_magic_sit_stand_worried_talk zorder 1
                player_name "Well?!"
                show player f_magic_sit_stand_worried
                show jenny f_breakfast_upset_down_talk
                jen "S-sorry, {b}[deb_name]{/b}..."
                show jenny f_breakfast_upset_talk
                jen "... I'm just, having a bad day."
                show jenny f_breakfast_upset
                show player f_diningroom_table_normal
                show debbie f_breakfast_standing_sad_talk
                deb "It's alright, dear. I understand."
                show debbie f_breakfast_standing_sad
                show jenny f_breakfast_upset_down
                pause
                show debbie f_breakfast_kiss_normal_talk b_breakfast_kiss zorder 0 with dissolve
                deb "Thank you, sweetie."
                show debbie f_breakfast_kiss_kiss
                show player f_diningroom_table_surprised_left_low
                player_name "!!!"
                show player f_diningroom_table_normal of_diningroom_table_blush
                show jenny f_breakfast_eyeroll
                hide debbie with dissolve
                pause
                show jenny f_breakfast_upset_talk
                jen "You know, I liked you better before you grew a backbone..."
                show jenny f_breakfast_upset
                show player f_magic_sit_stand_worried_talk of_empty
                player_name "No, you didn't."
                show player f_magic_sit_stand_worried
                show jenny f_breakfast_eyeroll
                jen "W-whatever..."
    show jenny f_breakfast_upset_talk
    jen "Before you {b}come to my room this afternoon{/b}, {b}pop up in the attic and grab my cheer uniform{/b}."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Why?!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Because I'm going to wear it for the show today."
    show jenny f_breakfast_upset
    show player f_diningroom_table_surprised_left
    player_name "!!!"
    show player f_magic_sit_stand_normal_talk
    player_name "R-really?!"
    show player f_magic_sit_stand_laugh
    pause
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_eyeroll
    jen "Yes, perv..."
    show jenny b_breakfast_gettingup a_empty f_breakfast_getup_upset_talk with dissolve
    jen "Don't forget."
    hide jenny with dissolve
    pause
    show player f_magic_sit_stand_laugh
    player_name "( Hmm, I wonder what we're going to do while she's wearing her old cheerleading outfit? )"
    return

label dining_room_jenny_pissed_at_blowjob:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_magic_sit_stand_worried zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    jen "..."
    show player f_magic_sit_stand_worried_talk
    player_name "Good morning."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "Yeah, morning."
    show jenny f_breakfast_upset_down
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "Are you going to pay me for yesterday?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "Oh, you wanna get paid to cum down my throat, huh?"
    show jenny f_breakfast_angry
    if M_jenny.get("dominance")<= 0:
        show player f_magic_sit_stand_worried_talk
        player_name "I said, I was sorry..."
        show player f_magic_sit_stand_worried
        show jenny f_breakfast_upset_down
        pause
        show player f_magic_sit_stand_worried_talk
        player_name "You know, you came in my mouth too!"
        show player f_magic_sit_stand_worried
        show jenny f_breakfast_upset_down_talk
        jen "Haha, oh yeah!"
        jen "I forgot about that..."
        show jenny f_breakfast_upset_down
        show player f_magic_sit_stand_worried_talk
        player_name "You practically waterboarded me!"
        show player f_magic_sit_stand_worried
        show jenny f_breakfast_laugh
        jen "HAHAHAAH!"
    else:
        show player f_magic_sit_stand_worried_talk
        player_name "{b}[jen_name]{/b}, I warned you!"
        show jenny f_breakfast_angry_talk
        jen "Yeah, well it's hard to concentrate on what you're saying!"
        jen "You're really good at-"
        show jenny f_breakfast_upset_down_talk
        jen "Nevermind."
        show jenny f_breakfast_upset_down
        show player f_magic_sit_stand_worried_talk
        player_name "Really good at what?"
        player_name "... Eating your pussy?"
        show player f_magic_sit_stand_worried
        show jenny f_breakfast_upset_down_talk
        jen "I didn't say that..."
        show jenny f_breakfast_upset_down
        show player f_magic_sit_stand_normal_talk
        player_name "Mmm, you kinda did..."
        show player f_magic_sit_stand_normal
        show jenny f_breakfast_upset_down_talk
        jen "Shut up."
        show jenny f_breakfast_upset_down
        pause
        show player f_magic_sit_stand_worried_talk
        player_name "So are you going to pay me or what?"
    show jenny f_breakfast_upset_down_talk
    show player f_magic_sit_stand_worried
    jen "{b}*Sigh*{/b} Fine."
    show jenny a_breakfast_dressed_money f_breakfast_upset_talk with dissolve
    jen "I guess, you earned it."
    show jenny a_breakfast_dressed_phone f_breakfast_upset_down with dissolve
    show player f_magic_sit_stand_normal_talk
    player_name "Thanks."
    show player f_diningroom_table_shy_down
    pause
    show jenny f_breakfast_upset_down_talk
    jen "You know, my fans really did like that show."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_normal_talk
    player_name "Yeah?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_upset_down_talk
    jen "It's got more than double the views that our handjob video has."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_normal_talk
    player_name "That's great!"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_grin_talk
    jen "Yeah, it means you're going to be eating a lot more pussy."
    show jenny f_breakfast_grin
    if M_jenny.get("dominance") <= 0:
        show player f_diningroom_table_surprised_left
        player_name "!!!"
        show player f_magic_sit_stand_normal_talk
        player_name "O-okay."
        show player f_magic_sit_stand_normal
        show jenny f_breakfast_grin_talk
        jen "Lucky little loser..."
    else:
        show player f_magic_sit_stand_normal_talk
        player_name "... And you'll be sucking a lot more dick."
        show player f_magic_sit_stand_normal
        show jenny f_breakfast_grin_down_talk
        jen "Tch, yeah... Maybe."
        show jenny f_breakfast_grin_down
        show player f_magic_sit_stand_normal_talk
        player_name "Haha!"
        show player f_magic_sit_stand_normal
        show jenny f_breakfast_upset_talk
    jen "Just don't go thinking I enjoy-"
    show jenny f_breakfast_surprised
    show player f_diningroom_table_worried_high
    deb "What are you kids talking about?"
    player_name "!!!" with hpunch
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal_talk
    show jenny f_breakfast_surprised_down
    deb "Has {b}[firstname]{/b} been eating something?"
    show debbie f_breakfast_standing_normal
    show player f_diningroom_table_worried_talk_high
    player_name "I..."
    show jenny f_breakfast_surprised_back
    show player f_magic_sit_stand_worried_talk
    player_name "W-we aren't..."
    show player f_magic_sit_stand_worried
    jen "Peaches!"
    show player f_magic_sit_stand_worried_talk
    player_name "Huh?!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_surprised
    jen "I bought some peaches the other day..."
    show jenny f_breakfast_normal_talk
    jen "... {b}[firstname]{/b} was eating my peaches."
    show jenny f_breakfast_normal
    show player f_diningroom_table_worried_high
    show debbie f_breakfast_standing_normal_talk
    deb "Oh, I love peaches!"
    deb "They're so juicy!"
    show debbie f_breakfast_standing_normal
    show player f_magic_sit_stand_laugh
    player_name "{b}*Snort*{/b}"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_grin_talk
    jen "Heh, you should have seen him when he finished."
    jen "{b}[firstname]{/b} is a real sloppy eater."
    show jenny f_breakfast_grin
    show player f_diningroom_table_normal_high
    show debbie f_breakfast_standing_normal_talk
    deb "Hehe, was his face all messy?"
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_laugh
    jen "He even had some in his hair!"
    show jenny f_breakfast_grin
    show debbie f_breakfast_standing_laugh
    deb "Haha!"
    show debbie f_breakfast_standing_normal
    pause
    show debbie f_breakfast_standing_normal_talk
    deb "It's nice you're sharing with {b}[firstname]{/b}."
    deb "One day, you kids are going to realize how fortunate you are to have one another."
    show debbie f_breakfast_standing_normal
    show player f_diningroom_table_normal_talk_high
    player_name "Heh, you think?"
    show player f_diningroom_table_normal_high
    show jenny f_breakfast_grin_talk
    jen "Yeah, right."
    show jenny f_breakfast_grin
    show debbie f_breakfast_standing_laugh
    deb "Now, who wants bacon?!"
    show debbie f_breakfast_standing_normal
    show player f_diningroom_table_normal_talk_high
    player_name "Oh, me!"
    show player f_diningroom_table_normal_high
    show debbie f_empty b_breakfast_potatoes3 with dissolve
    show jenny f_breakfast_eyeroll
    pause
    scene black with fade
    return

label dining_room_jenny_pissed_at_handjob:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_magic_sit_stand_worried zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause 
    jen "..."
    show player f_magic_sit_stand_worried_talk
    player_name "You still pissed at me?"
    show player f_magic_sit_stand_worried
    jen "Hmm?"
    show jenny f_breakfast_upset_down_talk
    jen "Oh."
    jen "Morning, asshole!"
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_worried_talk
    player_name "Heh, you're still mad..."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "Of course, I'm mad!"
    jen "You're disgusting!"
    show jenny f_breakfast_angry
    show player f_magic_sit_stand_worried_talk
    player_name "Look, I didn't mean to cum on you! It was just-"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Shhh!!!"
    jen "Not so loud dummy, {b}[deb_name]{/b} will hear you!"
    show jenny f_breakfast_upset
    show player f_diningroom_table_worried_talk_high
    player_name "Right, sorry."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "I had to do laundry because of you!"
    jen "You know I hate doing laundry!"
    show jenny f_breakfast_angry
    show player f_magic_sit_stand_worried_talk
    player_name "I thought {b}[deb_name]{/b} still did your laundry?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "Well, I can't exactly just hand her a bunch of cum stained bedsheets to wash, now can I?!"
    show jenny f_breakfast_angry
    show player f_magic_sit_stand_worried_talk
    player_name "No, I guess not..."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_eyeroll
    jen "Moron."
    show jenny f_breakfast_upset
    if M_jenny.get("dominance") <= 0:
        player_name "..."
        show player f_magic_sit_stand_worried_talk
        player_name "Seriously, I'm sorry!"
        show player f_magic_sit_stand_worried
    else:
        show player f_magic_sit_stand_worried_talk
        player_name "Don't be a bitch."
        show player f_magic_sit_stand_worried
        show jenny f_breakfast_upset_talk
        jen "Ugh."
    show jenny f_breakfast_upset_talk
    jen "Whatever."
    jen "Next time it happens, YOU'RE washing my sheets!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "N-next time?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Well, yeah..."
    show jenny f_breakfast_normal_talk
    jen "We made mad bank yesterday!"
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_worried_talk
    player_name "Really?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_normal_talk
    jen "Here."
    show jenny a_breakfast_dressed_money with dissolve
    jen "Your cut."
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_normal_talk
    player_name "Whoa, thanks!"
    show player f_magic_sit_stand_normal
    show jenny a_breakfast_dressed_spoon f_breakfast_normal with dissolve
    pause
    show player f_magic_sit_stand_normal_talk
    player_name "So when is our next show?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_normal_talk
    jen "Anytime {b}in the afternoon{/b} works for me."
    jen "Just {b}come to my room{/b}."
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_normal_talk
    player_name "Awesome!"
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal_talk with dissolve
    show player f_diningroom_table_normal_high
    show jenny f_breakfast_normal_low
    deb "Who's hungry?"
    show debbie f_breakfast_standing_normal
    show player f_diningroom_table_normal_talk_high
    player_name "Me!"
    show player f_diningroom_table_normal_high
    show debbie f_breakfast_standing_normal_talk
    deb "Hehe!"
    deb "Here you go, sweetie."
    show debbie b_breakfast_potatoes3 f_empty with dissolve
    show player f_diningroom_table_normal
    pause
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal_talk with dissolve
    deb "Are you kids getting along okay?"
    show debbie f_breakfast_standing_normal
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_sad
    pause
    show player f_diningroom_table_normal_talk
    player_name "Y-yes?"
    show jenny f_breakfast_normal_low
    show player f_diningroom_table_normal_high
    show debbie f_breakfast_standing_normal_talk
    deb "Good."
    deb "It warms my heart, you two spending time together."
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_eyeroll
    show player f_diningroom_table_normal_talk_high
    player_name "T-thanks, {b}[deb_name]{/b}."
    show jenny f_breakfast_normal_low
    show player f_diningroom_table_normal_high
    deb "Mmhmm."
    show player f_diningroom_table_shy_down
    hide debbie with dissolve
    pause
    call screen money_popup(100)
    $ player.get_money(100)
    scene black with fade
    return

label dining_room_jenny_cedric_upset:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_normal_low zorder 1
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show player 323e zorder 0 at Position(xpos=610,ypos=770) with dissolve
    player_name "Good morning."
    hide player
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating b_dinner_sitting zorder 0 at Position(align=(0,0))
    with dissolve
    jen "..."
    pause
    show jenny f_breakfast_upset_down_talk
    show player f_diningroom_table_surprised_left_food a_dinner_sitting_resting
    jen "Asshole!!!" with hpunch
    jen "Grr!"
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "What's your problem?"
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_angry_talk
    jen "Fucking {b}Cedric{/b}!"
    show jenny f_breakfast_angry
    show player f_diningroom_table_surprised_talk_food
    player_name "{b}Cedric{/b}, your ex-boyfriend?"
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_angry_talk
    jen "Tch, do you know any other people named {b}Cedric{/b}?!"
    show jenny f_breakfast_angry
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "No."
    show player f_diningroom_table_grumpy_food_left_talk
    pause
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_eyeroll
    jen "... Moron."
    show jenny f_breakfast_upset
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Why are you always such a bitch towards me?"
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_upset_talk
    jen "Umm, I dunno... Why are you always such a perv towards me?"
    show jenny f_breakfast_upset
    show player f_diningroom_table_surprised_left_food
    deb "What's going on in here?" with hpunch
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_sad with dissolve
    show player f_diningroom_table_surprised_high_food
    player_name "..."
    show jenny f_breakfast_upset_talk
    jen "Nothing, {b}[deb_name]{/b}."
    show jenny f_breakfast_upset
    show debbie f_breakfast_standing_sad_talk
    deb "I heard yelling."
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_talk_high_food
    player_name "She's just yelling at her phone like a crazy person."
    show player f_diningroom_table_surprised_high_food
    show jenny f_breakfast_angry_talk
    jen "Screw you, {b}[firstname]{/b}!"
    show jenny f_breakfast_angry
    show debbie f_breakfast_standing_sad_talk
    deb "Hey, cut it out, both of you!"
    show debbie f_breakfast_standing_sad
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_surprised_talk_high_food
    player_name "Sorry, {b}[deb_name]{/b}."
    show player f_diningroom_table_surprised_high_food
    jen "..."
    show debbie f_breakfast_standing_sad_talk
    deb "Why are you yelling at your phone, {b}[jen_name]{/b}?"
    show debbie f_breakfast_standing_sad
    show jenny f_breakfast_upset_down_talk
    jen "{b}*Sigh*{/b} It's nothing..."
    jen "... {b}Cedric{/b} is just refusing to answer my texts."
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "I don't blame him."
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_angry
    show debbie f_breakfast_standing_sad_talk
    deb "{b}[firstname]{/b}!"
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_high_food
    player_name "..."
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    show debbie f_breakfast_standing_sad_talk
    deb "I thought you broke up with {b}Cedric{/b}?"
    show debbie f_breakfast_standing_sad
    show jenny f_breakfast_upset_talk
    jen "I did."
    show jenny f_breakfast_upset
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    show debbie f_breakfast_standing_sad_talk
    deb "So why are you texting him?"
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting with dissolve
    show jenny f_breakfast_upset_talk
    jen "I need him for-"
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_sad_talk
    pause
    show jenny f_breakfast_upset_talk
    jen "{b}*Ahem*{/b} I uhh, need his help... With work."
    show jenny f_breakfast_upset
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    show debbie f_breakfast_standing_normal_talk
    deb "Oh."
    show debbie f_breakfast_standing_normal
    show player f_magic_sit_stand_normal_talk with dissolve
    player_name "{b}Cedric{/b} is going to help you with transcribing?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_angry
    pause
    show player f_magic_sit_stand_normal_talk
    player_name "You're still doing that, right?"
    show player f_magic_sit_stand_normal
    jen "..."
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    show debbie f_breakfast_standing_normal_talk
    deb "Why don't you just call him, sweetie?"
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_upset_talk
    jen "I've been trying, he won't answer."
    show jenny f_breakfast_upset
    show debbie f_breakfast_standing_normal_talk
    deb "Well, why don't yo-"
    show debbie f_breakfast_standing_normal
    "{b}*Sizzle*{/b}"
    show debbie f_breakfast_standing_sad
    pause
    show player f_diningroom_table_worried_high
    show debbie f_breakfast_standing_sad_talk
    deb "Oh, shoot!"
    hide debbie with dissolve
    deb "I forgot about breakfast!"
    show player f_diningroom_table_shy_down
    show jenny f_breakfast_grin
    pause
    show jenny f_breakfast_grin_talk
    jen "Sounds like you're getting burnt bacon today, loser."
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "It's still better than that cereal you're eating."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "Whatever."
    show jenny f_breakfast_upset_down
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    pause
    pause
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    show jenny f_breakfast_angry_talk
    jen "Motherfucker!"
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting with dissolve
    jen "Will you go down to {b}the gym{/b} and tell that asshole to call me?"
    show jenny f_breakfast_angry
    show player f_diningroom_table_surprised_talk_food
    player_name "Huh?"
    player_name "No way!"
    show player f_diningroom_table_surprised_left_food
    show player f_magic_sit_stand_normal_talk
    show jenny f_breakfast_upset_talk
    jen "Oh, c'mon {b}[firstname]{/b}."
    show jenny f_breakfast_upset
    show player f_diningroom_table_surprised_talk_food
    player_name "I hate that guy!"
    player_name "He always treats me like a little kid."
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_grin_talk
    jen "Well, compared to him, you are a little kid."
    show jenny f_breakfast_grin
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Absolutely not."
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_angry_talk
    jen "COME ON!"
    show jenny f_breakfast_angry
    pause
    show jenny f_breakfast_upset_talk
    jen "What if, I get naked for you again?"
    show jenny f_breakfast_upset
    show player f_diningroom_table_surprised_talk_food
    player_name "Completely naked?"
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_eyeroll
    jen "That's what I said, dummy."
    show jenny f_breakfast_upset
    show player f_diningroom_table_surprised_talk_food
    player_name "Can I touch?"
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_upset_talk
    jen "{b}*Sigh*{/b} I suppose..."
    jen "... But just my tits."
    show jenny f_breakfast_upset
    if M_jenny.get("dominance") <= 0:
        show player f_magic_sit_stand_laugh od_dinner_sitting_boner
        player_name "Sweet!"
    else:
        show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
        pause
        show player f_diningroom_table_grumpy_food_left_talk with dissolve
        player_name "Forget it, I've got better things to do."
        show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting
        show jenny f_breakfast_angry
        pause
        jen "Grr!!"
        show jenny f_breakfast_angry_talk
        jen "Fine, okay?!"
        show jenny f_breakfast_upset_talk
        jen "You can touch whatever you want, just..."
    show player f_magic_sit_stand_normal
    show jenny b_breakfast_gettingup f_breakfast_getup_upset_talk a_empty with dissolve
    jen "C'mon, let’s go!"
    show jenny f_breakfast_getup_upset
    show player f_magic_sit_stand_normal_talk
    player_name "Just as soon as I finish breakfast."
    show jenny b_breakfast_pulling f_empty
    hide player
    hide player_dick
    with dissolve
    player_name "!!!"
    hide jenny with dissolve
    jen "No, right now!"
    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_closeup with None
    show jenny b_dressed_pulling2 a_empty f_upset at flip
    show jenny at Position (xpos=-150)
    show debbie
    with dissolve
    player_name "Hey, stop pulling me!"
    show jenny b_dressed_pulling1
    show debbie f_normal_talk
    deb "Breakfast is almost ready if you two wanna-"
    show debbie f_surprised
    pause
    show debbie f_normal_talk
    deb "Are you kids going somewhere?"
    show debbie f_normal
    show jenny f_normal_talk
    jen "{b}[firstname]{/b} is going to talk to {b}Cedric{/b} for me."
    show jenny f_normal
    show debbie f_normal_talk
    deb "Well, that's nice of him."
    show debbie f_normal
    pause
    show jenny b_dressed_pulling2
    player_name "Hold on a second, I want my breakfas-"
    show jenny b_dressed_pulling1 f_upset_talk
    jen "Shut up!"
    show jenny f_upset
    pause
    show debbie f_laugh
    deb "I'm happy you two are finally spending time together!"
    hide jenny
    hide player
    with dissolve
    show debbie f_normal
    pause
    show debbie f_normal_talk
    deb "It's about time they bonded a little..."
    hide debbie with dissolve
    pause
    $ player.go_to(L_home_sisbedroom)
    scene expression player.location.background_closeup with None
    show jenny b_dressed_pulling2 a_empty f_upset
    player_name "Ack!"
    show player 12 at left
    show jenny b_dressed a_dressed_hips f_upset
    with dissolve
    player_name "What is the rush?!"
    player_name "I promise, I'll go and talk to-"
    show player 11
    show jenny b_pull1 a_empty f_grin_down with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    show player 10
    player_name "... to..."
    show player 11
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_naked a_naked_panties_remove f_grin_down with dissolve
    player_name "..."
    show jenny b_naked_panties_remove_down f_empty a_empty with dissolve
    pause
    show jenny b_naked f_upset_talk a_naked_hips with dissolve
    jen "I need {b}Cedric{/b} to call me ASAP!"
    show jenny f_eyeroll
    jen "So let's hurry up and get this over with..."
    show jenny f_gross
    if M_jenny.get("dominance") <= 0:
        player_name "..."
        show jenny f_upset_talk
        jen "Are you going to touch them or what?!"
        show jenny f_gross
        player_name "Hmm?"
        show jenny f_eyeroll a_naked_breasts with dissolve
        pause
        show jenny f_gross a_naked_hips with dissolve
        show player 22
        player_name "OH!"
        show player 14
        player_name "Right."
        hide player
        show jenny b_groping_naked_touch_talk a_groping_naked_hips f_upset
        with dissolve
        player_name "Wow!"
        show jenny b_groping_naked_touch with dissolve
        pause
        player_name "They're really nice!"
        show jenny f_upset_talk
        jen "Tell me something I don't know..."
        show jenny f_upset
        pause
        show jenny f_upset_talk b_groping_naked_suck_pre with dissolve
        jen "Guys always lov-"
        show jenny f_nipple1 b_groping_naked_suck a_groping_naked_up_clench
        jen "!!!" with hpunch
        jen "What are you-"
        pause
        show jenny f_nipple2
        jen "Ahh..."
        pause
        jen "I didn't-"
        pause
        jen "Ffffuuu-"
        pause
        jen "Ngghhh!!"
        show jenny f_upset_talk b_groping_naked_cover
        show player 24 at left
        with dissolve
        jen "Alright, stop!!"
        show jenny f_upset
        show player 10
        player_name "What's the problem?"
        show player 5
        show jenny f_upset_talk
        jen "That's plenty for today!"
        jen "Go talk to {b}Cedric{/b}."
        show jenny f_upset
        show player 12
        player_name "Ugh, alright."
        player_name "Where did you say I could find him?"
        show player 5
        show jenny f_upset_talk
        jen "He'll probably be at {b}the Gym{/b}."
        jen "That meathead is always at {b}the Gym{/b}."
        show jenny f_upset
        show player 17
        player_name "On it."
        hide player with dissolve
        pause
        show jenny b_groping_naked_orgasm a_empty f_orgasm_nipple3 at Position (yoffset=66) with dissolve
        jen "( Hmm, not bad for a little virgin loser... )"
        pause
        scene black with fade
    else:

        show player 14
        player_name "O-okay."
        hide player
        show jenny f_nipple1 b_groping_naked_suck a_groping_naked_up_clench
        jen "!!!" with hpunch
        pause
        show jenny f_nipple2
        jen "Jesus, you're just jumping right into-"
        jen "Ahh!"
        pause
        show jenny f_nipple3
        jen "Mmm."
        pause
        show jenny f_nipple1 b_groping_naked_finger
        jen "Oh, shit!"
        show jenny f_nipple2
        pause
        jen "Ffffuuu-"
        pause
        jen "I'm gonna!"
        show player 11 at Position (xpos=300)
        show jenny b_groping_naked_orgasm a_empty f_orgasm_nipple2 at Position (yoffset=66)
        jen "Ngghhh!!!" with flash
        pause
        pause
        show jenny b_groping_naked_cover a_groping_naked_up_clench f_upset_talk
        jen "Haah... Fuck!"
        show jenny f_upset
        show player 10
        player_name "Did you just cum?"
        show player 5
        show jenny f_angry_talk
        jen "What? NO!"
        show jenny f_angry
        show player 17
        player_name "Yes, you did! Look at my fingers!"
        show player 734 with dissolve
        show jenny f_angry_talk
        jen "Shut up!"
        show jenny f_angry
        show player 13
        pause
        show jenny f_angry_talk
        jen "That's plenty for today!"
        show jenny f_angry
        show player 14
        player_name "Heh, you just squirted in my hand!"
        show player 13
        show jenny f_angry_talk
        jen "I said shut up!!!"
        jen "Go talk to {b}Cedric{/b}."
        show jenny f_angry
        show player 10
        player_name "Ugh, alright."
        show player 12
        player_name "Where did you say I could find him?"
        show player 5
        show jenny f_upset_talk
        jen "He'll probably be at {b}the Gym{/b}."
        jen "That meathead is always at {b}the Gym{/b}."
        show jenny f_upset
        show player 12
        player_name "On it."
        hide player with dissolve
        pause
        show jenny b_groping_naked_orgasm a_empty f_orgasm_nipple3 at Position (yoffset=66) with dissolve
        jen "( Where the hell did that come from?! )"
        scene black with fade
    return

label dining_room_jenny_have_breakfast_3:
    scene expression game.timer.image("dining_room{}")
    show debbie b_breakfast_sitting a_breakfast_rest f_breakfast_sitting_normal zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_diningroom_table_normal_talk zorder 0 at Position(align=(0,0)) with dissolve
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    player_name "Mmm, that was so good {b}[deb_name]{/b}!"
    player_name "You're the best cook in the whole world!"
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_laugh
    deb "Aww, hehe!"
    show debbie f_breakfast_sitting_normal_talk
    deb "Thanks, sweetie."
    show debbie f_breakfast_sitting_normal
    show player f_diningroom_table_normal_talk
    player_name "You want help with the dishes?"
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "Oh, no..."
    deb "I can handle it just fine. Don't you worry!"
    deb "I'm in such a good mood, now that {b}[jen_name]{/b} found herself a job."
    deb "I was so worried about her!"
    show debbie f_breakfast_sitting_normal
    show player f_magic_sit_stand_laugh
    player_name "Heh, yeah."
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "Transcribing..."
    deb "I didn't know she had it in her!"
    show debbie f_breakfast_sitting_normal
    show player f_magic_sit_stand_worried_talk
    player_name "Uh huh..."
    show player f_diningroom_table_shy_down
    show debbie f_breakfast_sitting_normal_talk
    deb "Oh, listen to me blathering on."
    deb "I'm sure you have a million things you'd rather do than listen to me."
    show debbie f_breakfast_sitting_normal
    show player f_magic_sit_stand_worried_talk
    player_name "No, not at all!"
    show player f_diningroom_table_normal_talk
    player_name "I enjo-"
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "You just run along now and have a good day, alright?"
    show debbie f_breakfast_sitting_normal
    pause
    show player f_diningroom_table_normal_talk
    player_name "Okay."
    show player f_diningroom_table_normal
    pause
    show player f_diningroom_table_normal_talk
    player_name "Thanks again for breakfast."
    show player f_diningroom_table_normal
    show debbie f_breakfast_sitting_normal_talk
    deb "My pleasure, sweetie."
    hide player with dissolve
    $ player.go_to(L_home_entrance)
    scene expression player.location.background_blur
    show player f_worried
    with dissolve
    player_name "( I can't believe {b}[deb_name]{/b} bought that transcribing story... )"
    pause
    show player a_dressed_thinking f_thinking with dissolve
    player_name "( Hmm, I wonder what {b}[jen_name]{/b} is really up to? )"
    hide player with dissolve
    return

label dining_room_jenny_have_breakfast_2:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_normal_low zorder 1
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show player 323e zorder 0 at Position(xpos=610,ypos=770) with dissolve
    player_name "Morning."
    hide player
    show player b_dinner_sitting a_dinner_sitting_bowl f_diningroom_table_shy_down zorder 0 at Position(align=(0,0))
    with dissolve
    pause
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_resting with dissolve
    pause
    show player f_diningroom_table_grumpy_food_left_talk with dissolve
    player_name "Hello?!"
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_upset_down_talk
    jen "Hmm, what?!"
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "What's your problem?"
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_upset_down_talk
    jen "Nothing, leave me alone."
    show jenny f_breakfast_upset_down
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    player_name "..."
    pause
    show jenny f_breakfast_eyeroll
    jen "Ugh, this stupid {b}Sluttygram{/b} thing is a waste of time!"
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_worried_talk with dissolve
    player_name "Those pictures didn't help?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "They did but it's just not making me enough money..."
    show jenny f_breakfast_upset_down
    show player f_magic_sit_stand_worried_talk
    player_name "Yeah, well {b}Sluttygram{/b} is pretty small potatoes compared to what's out there..."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "What do you mean?"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "You do realize that porn exists, right?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Yeah, so?"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Why would anyone pay good money to look at sexy photos with no nudity when they can watch hardcore porn, for free?!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_eyeroll
    jen "Umm, I dunno... How about because I'm hot and those porno skanks aren't?!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_laugh
    player_name "You're joking, right?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "No, shut up!"
    show jenny b_breakfast_gettingup f_breakfast_getup_upset_talk a_empty with dissolve
    jen "Don't pretend like you don't think I'm hot!"
    show jenny f_breakfast_getup_upset
    show player f_diningroom_table_surprised_forward
    player_name "..."
    show jenny f_breakfast_getup_angry_talk
    jen "Say it!"
    show jenny f_breakfast_getup_angry
    return

label dining_room_jenny_have_breakfast_2_youre_hot:
    show player f_magic_sit_stand_worried_talk
    player_name "You're hot."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_getup_angry_talk
    jen "Damn right!"
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down with dissolve
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    pause
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    pause
    show player f_diningroom_table_grumpy_food_left_talk with dissolve
    player_name "But it's still small potatoes."
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting
    show jenny f_breakfast_upset_down_talk
    jen "Yeah, yeah..."
    show jenny f_breakfast_upset_down
    pause
    show jenny f_breakfast_eyeroll
    jen "Grr, I need more money!!!"
    show jenny f_breakfast_upset_down
    pause
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    show jenny f_breakfast_upset
    pause
    show jenny f_breakfast_upset_talk
    jen "Come with me."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk with dissolve
    player_name "Huh, where?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "To my room, dummy."
    jen "I've got a proposition for you."
    hide jenny with dissolve
    show player f_magic_sit_stand_worried_talk
    player_name "Uhh, okay."
    show player f_magic_sit_stand_worried
    player_name "( I hope I didn't piss her off... )"
    hide player with dissolve
    return

label dining_room_jenny_have_breakfast_2_no:
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    pause
    show player f_diningroom_table_grumpy_food_left_talk a_dinner_sitting_resting with dissolve
    player_name "Wow, are you that desperate for attention?"
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_getup_upset_talk
    jen "What?!"
    jen "That's not-"
    show jenny f_breakfast_getup_angry
    pause
    show jenny f_breakfast_getup_angry_talk
    jen "SHUT UP!"
    show jenny f_breakfast_getup_angry
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Heh and you call me pathetic..."
    show player f_diningroom_table_grumpy_food_left
    jen "Grrr!!"
    hide jenny with dissolve
    show player f_diningroom_table_looking_down_food
    pause
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_sad_talk with dissolve
    deb "What's gotten into her this morning?"
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_talk_high_food
    player_name "Who knows?"
    show player f_diningroom_table_surprised_high_food
    show debbie f_breakfast_standing_sad_talk
    deb "This whole job business must really be stressing her out."
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_talk_high_food
    player_name "Yeah, maybe."
    show player f_diningroom_table_surprised_high_food
    show debbie f_breakfast_standing_sad_talk
    deb "Poor thing."
    deb "Here's some more breakfast, sweetie."
    show debbie b_breakfast_potatoes3 f_empty with dissolve
    pause
    show debbie b_breakfast_potatoes f_breakfast_standing_normal with dissolve
    show player f_diningroom_table_surprised_talk_high_food
    player_name "Thanks, {b}[deb_name]{/b}!"
    show player b_dinner_sitting a_dinner_sitting_bowl f_diningroom_table_shy_down with dissolve
    hide debbie with dissolve
    pause
    player_name "( I should probably go and check on {b}[jen_name]{/b}... )"
    player_name "( I wasn't trying to be mean, she just really knows how to push my buttons. )"
    player_name "( Not until after I eat this delicious breakfast though! )"
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    return

label dining_room_sis_breakfast_started:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_normal_low zorder 1
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    show player 323d zorder 0 at Position(xpos=610,ypos=770)
    with fade
    player_name "( Huh. {b}[jen_name]{/b} is awake already? )"
    player_name "( She usually sleeps in. )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
