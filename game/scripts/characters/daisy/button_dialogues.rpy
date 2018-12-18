label daisy_button_baby_leave:
    show player 14b
    player_name "I'll leave you guys be."
    show player 1b
    show daisy f_normal_talk
    daisy "Alright."
    show daisy f_down_talk
    daisy "Say, bye bye daddy."
    show daisy f_down
    show player 17
    player_name "Hehe."
    show player 14b
    player_name "Goodbye, little one."
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_get_anything_baby:
    show player 14b
    player_name "Can I get you anything?"
    show player 1b
    show daisy f_normal_talk
    daisy "No, I'm okay."
    daisy "Thanks, {b}[firstname]{/b}."
    show daisy f_normal
    show player 14b
    player_name "You're welcome."
    show player 1b
    return

label daisy_button_hows_baby_doing_boy:
    show player 14b
    player_name "How's he doing?"
    show player 1b
    show daisy f_normal_talk
    daisy "He sleeps alot..."
    daisy "... And when he's not sleeping, he's eating!"
    show daisy f_normal
    show player 14b
    player_name "Heh, so he takes after his mommy then?"
    show player 1b
    show daisy f_laugh
    daisy "Nu uh!"
    show daisy f_normal
    show player 17
    player_name "Hehehe."
    show player 1b
    return

label daisy_button_hows_baby_doing_girl:
    show player 14b
    player_name "How's she doing?"
    show player 1b
    show daisy f_normal_talk
    daisy "She sleeps alot..."
    daisy "... And when she's not sleeping, she's eating!"
    show daisy f_normal
    show player 14b
    player_name "Heh, so she takes after her mommy then?"
    show player 1b
    show daisy f_laugh
    daisy "Nu uh!"
    show daisy f_normal
    show player 17
    player_name "Hehehe."
    show player 1b
    return

label daisy_button_gave_birth_intro:
    scene expression player.location.background_blur with None
    show player 14b at left
    show daisy a_naked_baby f_down
    with dissolve
    player_name "Hey, {b}Daisy{/b}."
    show player 1b
    show daisy f_down_talk
    if M_daisy.pregnancy.baby_gender == "boy":
        daisy "Isn't he wonderful, {b}[firstname]{/b}?"
        show daisy f_down
        show player 14b
        player_name "He sure is!"
        show player 1b
        show daisy f_normal_talk
        daisy "He has your eyes."
    else:
        daisy "Isn't she wonderful, {b}[firstname]{/b}?"
        show daisy f_down
        show player 14b
        player_name "She sure is!"
        show player 1b
        show daisy f_normal_talk
        daisy "She has your eyes."
    show daisy f_normal
    pause
    show daisy f_down_talk
    daisy "And my horns!"
    show daisy f_laugh
    daisy "Hehehe!"
    show daisy f_normal
    return

label daisy_button_hows_the_baby_1:
    show player 14b at left
    show daisy
    player_name "How's the baby?"
    show player 1b
    show daisy f_normal_talk
    daisy "Umm, I dunno."
    daisy "It makes me sick in the mornings but otherwise I feel the same as always."
    show daisy f_normal
    show player 14b
    player_name "Well that's good."
    player_name "You make sure and tell {b}Diane{/b} or me if you ever feel like something is wrong, okay?"
    show player 1b
    show daisy f_normal_talk
    daisy "Y-yeah, okay {b}[firstname]{/b}."
    show daisy f_normal
    return

label daisy_button_hows_the_baby_2:
    show player 1b at left
    show daisy f_normal_talk
    daisy "Hehe, look {b}[firstname]{/b}!"
    show daisy f_down_talk
    daisy "My boobies are getting bigger!"
    show daisy f_down
    show player 14b
    player_name "Yeah, you're producing more milk in preparation for the baby."
    show player 1b
    show daisy f_normal_talk
    daisy "Oh, that will make {b}Diane{/b} happy, won't it?"
    show daisy f_normal
    show player 14b
    player_name "Yeah, it sure will."
    show player 1b
    pause
    show daisy f_down_talk a_naked_touch with dissolve
    daisy "Did you see my tummy?"
    show daisy f_normal
    show player 14b
    player_name "Yeah."
    show player 1b
    show daisy f_sad_talk
    daisy "Do you think it's ugly?"
    show daisy f_sad
    show player 14b
    player_name "No, not at all!"
    player_name "I think it's kinda cute, actually..."
    show player 1b
    show daisy f_laugh
    daisy "Really?!"
    daisy "Hehe, you're weird {b}[firstname]{/b}!"
    show daisy f_normal a_naked_sides with dissolve
    show player 17
    player_name "Hehe!"
    show player 1b
    return

label daisy_button_hows_the_baby_3:
    show player 1b at left
    show daisy a_naked_touch f_sad_talk
    daisy "{b}*Sigh*{/b}"
    daisy "This baby business is a real hassle, you know?!"
    show daisy f_sad
    show player 10b
    player_name "Oh?"
    show player 5b
    show daisy f_sad_talk
    daisy "I have to pee like every five minutes!"
    show daisy f_sad
    show player 14b
    player_name "Heh, yeah that does sound like a hassle!"
    show player 1b
    show daisy f_down_talk
    daisy "... And the baby is dancing all the time!"
    show daisy f_down
    show player 14b
    player_name "Dancing?"
    show player 1b
    show daisy f_normal_talk
    daisy "Yeah, {b}Diane{/b} says it's kicking but I don't know why it would kick me..."
    daisy "I'm it's mommy afterall."
    show daisy f_normal
    show player 14b
    player_name "Heh, I'm sure you're right."
    player_name "It's probably just excited to come out."
    show player 1b
    show daisy f_laugh
    daisy "Yeah!"
    daisy "I mean, I dance when I'm excited."
    show daisy f_normal a_naked_sides with dissolve
    show player 14b
    player_name "Heh, you sure do."
    show player 1b
    return

label daisy_button_intro_end:
    scene expression player.location.background_blur with None
    show daisy f_normal_talk
    show player 1b at left
    with dissolve
    daisy "{b}*Gasp* [firstname]{/b}!!!"
    show daisy f_normal
    show player 14b
    player_name "Hey {b}Daisy{/b}."
    hide player
    show daisy b_naked_hug f_empty a_empty
    with dissolve
    daisy "I missed you!"
    pause
    show daisy b_naked a_naked_sides f_normal
    show player 14b at left
    player_name "Y-yeah, I missed you too."
    show player 1b
    return

label daisy_button_have_sex_first:
    show player 14b at left
    show daisy
    player_name "You still want to have sex?"
    show player 1b
    show daisy f_normal_talk
    daisy "Oh, yes!"
    daisy "Very much!"
    show daisy f_normal
    pause
    show player 14b
    player_name "Alright, let's do it."
    show player 1b
    show daisy f_normal_talk
    daisy "{b}*Gasp*{/b} Really?!"
    show daisy f_laugh
    daisy "Yay!!!"
    show daisy f_normal
    show player 14b
    player_name "C'mon, let's go to one of the milking machines."
    show player 1b
    show daisy f_laugh
    daisy "Okay!"
    hide player
    hide daisy
    with dissolve
    pause
    return

label daisy_button_have_sex_repeat:
    show player 10b at left
    show daisy
    player_name "You wanna... You know?"
    show player 5b
    show daisy f_normal_talk
    daisy "{b}*Gasp*{/b} Have sex?!"
    show daisy f_normal
    show player 14b
    player_name "Y-yeah."
    show player 1b
    show daisy f_normal_talk
    daisy "Of course!"
    daisy "I love it when we have sex!"
    show daisy f_normal
    show player 14b
    player_name "Heh, let's head over to the milking machines then."
    show player 1b
    show daisy f_laugh
    daisy "Okay!"
    hide player
    hide daisy
    with dissolve
    pause
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show daisy_sex_breed pre_talk
    show daisy_sex_breed_mc
    with dissolve
    daisy "Alright, weasel... Come on in!"
    daisy "Hehehe!"
    hide daisy_sex_breed_mc
    show daisy_sex_breed insert_and_pullout
    with dissolve
    pause
    show daisy_sex_breed creampie_pullout with dissolve
    pause 1
    show daisy_sex_breed creampie
    daisy "!!!" with hpunch
    $ animated = False
    return

label daisy_button_diane_breeding:
    scene expression player.location.background_blur with None
    show player 13 at left
    show diane b_naked a_naked_sides f_shamed_talk_smile
    with dissolve
    dia "Psst, {b}[firstname]{/b}."
    show diane f_shamed
    show player 5
    player_name "Hmm?"
    show player 10
    player_name "{b}Diane{/b}, what's going on?"
    show player 5
    show diane f_shamed_talk_smile
    dia "Were you on your way to see {b}Daisy{/b}?"
    show diane f_shamed
    show player 14
    player_name "Yeah, I was just on my way to milk her."
    show player 13
    show diane f_smirk_talk
    dia "Mmm, watching you milk her gets me so-"
    show diane f_smirk
    pause
    hide player
    show diane b_pull_mc_naked f_empty a_empty at flip
    dia "Come with me!" with hpunch
    dia "{b}Daisy{/b} can wait a little longer."
    dia "I need you inside me, right now!"
    hide diane with dissolve
    player_name "O-okay-"
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed pre_talk
    show diane_sex_breed_mc
    with dissolve
    dia "C'mon stud, give it to me!"
    hide diane_sex_breed_mc
    show diane_sex_breed insert_and_pullout
    with dissolve
    pause
    show diane_sex_breed creampie_pullout with dissolve
    pause 1
    show diane_sex_breed creampie
    dia "Oh, yeaaaah!!" with hpunch
    $ M_diane.set('sex speed', 0.09)
    show expression AnimatedImage("diane_sex_back", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
    pause
    dia "Ahh!"
    pause
    dia "Thank you, {b}[firstname]{/b}."
    dia "It's wrong of me to steal you away from {b}Daisy{/b} while she's still adjusting but..."
    dia "... I really nee-"
    dia "Ah, shit!"
    dia "... Really needed this today!"
    pause
    player_name "Heh, it's no problem {b}Diane{/b}."
    pause
    scene location_diane_garden_cutscene12
    with fade
    player_name "I think {b}Daisy's{/b} been adjusting really well."
    player_name "She seems really happy living here."
    dia "I think so too."
    dia "We really lucked out finding her."
    dia "She's so adorable!"
    player_name "Plus, she's helping you out with your business now, right?"
    dia "Definitely!"
    dia "She produces more than I do and she's not even-"
    scene location_diane_garden_cutscene12b with fade
    "{b}*Clink*{/b}{p=1}{nw}"
    "{b}*Smash*{/b} !!!" with hpunch
    player_name "What the-"
    pause
    dia "{b}Daisy{/b}?!"
    scene expression player.location.background_blur with None
    show player 368f at Position (xpos=650)
    show diane b_naked a_naked_sides f_smirk at Position (xpos=600)
    show daisy b_naked_shy a_naked_shy_front f_shy_sad_talk at flip
    with dissolve
    daisy "I didn't-"
    daisy "I, I, I wasn't-"
    show daisy f_shy_sad
    show diane f_smirk_talk
    dia "Were you watching us?"
    show diane f_smirk
    pause
    show daisy f_shy_sad_talk
    daisy "I'm sorry, please don't be mad!"
    show daisy f_shy_sad
    show diane f_laugh
    dia "Hehe, it's alright, sweetie!"
    hide daisy
    show daisy b_naked_diane_comfort a_empty f_empty at Position (xpos=200)
    show diane b_empty a_empty f_smirk_talk_fardown zorder 1 at Position (xpos=200)
    with dissolve
    dia "Shh, we're not mad."
    show diane f_smirk_fardown
    show daisy b_naked_diane_comfort2
    daisy "{b}*Sniff*{/b} Y-you're not mad?"
    show daisy b_naked_diane_comfort
    show diane f_smirk_talk_fardown
    dia "Of course not!"
    dia "You were just curious, weren't you?"
    show diane f_smirk_fardown
    show daisy b_naked_diane_comfort2
    daisy "Y-yeah..."
    show diane b_naked a_naked_sides f_smirk at Position (xpos=600)
    hide daisy
    show daisy b_naked a_naked_sides f_normal_talk at flip
    with dissolve
    daisy "I've never seen anyone else play {b}hide the weasel{/b} before..."
    show daisy f_normal
    show player 367f
    player_name "{b}Hide the weasel{/b}?"
    show player 368f
    show daisy f_normal_talk
    daisy "Master and I used to play it too!"
    show daisy f_normal
    pause
    show daisy f_normal_talk
    daisy "His weasel wasn't as large as {b}[firstname]'s{/b} though..."
    show daisy f_normal
    show player 367f
    player_name "You mean, {b}Jebadiah{/b} was having sex with you?!"
    show player 368f
    show diane f_shamed_talk_smile
    dia "{b}*Sigh*{/b} Of course he was..."
    dia "... The dirty old bastard."
    show diane f_shamed_talk
    show daisy f_normal_talk
    daisy "Don't be upset {b}Diane{/b}..."
    show daisy f_laugh
    daisy "Master just needed my help!"
    daisy "I didn't want his weasel to get sick and die!"
    show daisy f_normal
    show player 367f
    player_name "Okay, I'm confused."
    show player 368f
    show daisy f_normal_talk
    daisy "That's why you play with {b}[firstname]{/b}, right?"
    show daisy f_normal
    pause
    show diane f_shamed_talk_smile
    dia "Sweetie, exactly what did that old man tell you?"
    show diane f_shamed
    show daisy f_normal_talk
    daisy "Umm, that sometimes a man's weasel gets sick and becomes hard all over..."
    show daisy f_normal
    player_name "..."
    show daisy f_normal_talk
    daisy "... And when that happens, he needs to put it inside a woman's hidey-hole."
    daisy "Otherwise it turns blue and falls off."
    show daisy f_normal
    pause
    show diane f_shamed_talk_smile
    dia "Well, he was a creative old bastard... I'll give him that."
    show diane f_shamed
    show player 367f
    player_name "... Hidey-hole?"
    show player 368f
    show daisy f_normal_talk
    daisy "Yeah!"
    hide daisy
    show daisy b_naked_behind f_empty a_empty at Position (xpos=100)
    with dissolve
    show diane f_surprised_front
    daisy "Master said his weasel liked my hidey-hole the best!"
    show player 430f
    with hpunch
    pause
    show player 66f
    daisy "{b}*Gasp*{/b}"
    hide daisy
    show daisy b_naked a_naked_sides f_sad_talk at flip
    with dissolve
    show diane f_surprised
    daisy "Look {b}Diane{/b}!"
    daisy "{b}[firstname]{/b}'s weasel is getting sick again!"
    show diane f_surprised_front
    show daisy f_sad
    show player 67f
    pause
    hide daisy
    show daisy b_naked_behind f_empty a_empty at Position (xpos=100)
    with dissolve
    daisy "Do you want to use my hidey-hole this time?!"
    show player 430bf
    player_name "Uhh."
    show player 430f
    show diane f_shamed_talk_smile
    dia "No, no, no..."
    dia "{b}[firstname]{/b}'s {b}*Ahem*{/b} weasel... Will be just fine."
    show diane f_shamed
    hide daisy
    show daisy b_naked a_naked_sides f_normal at flip
    with dissolve
    show diane f_shamed_talk_smile
    dia "Right now, I think you and I need to have a talk."
    show diane f_shamed
    show daisy f_normal_talk
    daisy "Oh, okay."
    show daisy f_normal
    show diane f_smirk_talk
    dia "I'm sure {b}[firstname]{/b} can take care of that on his own, can't you {b}[firstname]{/b}?"
    show diane f_smirk
    show player 432f
    player_name "Y-yeah..."
    show player 431f
    show diane f_smirk_talk
    dia "Why don't you head on home for the day and give us some girl time."
    show diane f_smirk
    show player 432f
    player_name "Sure thing."
    show player 431f
    show daisy f_laugh
    daisy "Byeeee, {b}[firstname]{/b}!"
    show daisy f_normal
    show player 432f
    player_name "Heh, bye {b}Daisy{/b}."
    hide player
    hide daisy
    hide diane
    with dissolve
    return

label daisy_button_more_jebadiah_delmont_2:
    show player 10b
    player_name "There's something I still don't understand, {b}Daisy{/b}."
    show player 5b
    show daisy f_normal
    daisy "Hmm?"
    show player 10b
    player_name "Why were you so frightened of me when you first appeared?"
    show player 5b
    show daisy f_sad_talk
    daisy "Oh."
    show daisy f_surprised_after_appear
    daisy "Umm..."
    pause
    show player 10b
    player_name "You don't have to tell me if you don't want to."
    show player 5b
    show daisy f_sad_talk
    daisy "No, I-"
    daisy "I want to."
    show daisy f_sad_talk_closed
    daisy "I just..."
    pause
    show daisy a_naked_cover with dissolve
    daisy "I was a bad girl, {b}[firstname]{/b}!"
    show player 10b
    player_name "Huh?!"
    player_name "I find that hard to imagine."
    show player 5b
    show daisy f_sad_talk
    daisy "No, I was!"
    show daisy a_naked_sides
    daisy "You see, master forgot to lock the shack one night and I-"
    show daisy f_sad_talk_closed
    daisy "I-"
    show daisy f_sad
    pause
    show daisy f_sad_talk
    daisy "I just wanted to go for a walk!"
    show daisy f_sad
    pause
    show daisy f_sad_talk
    daisy "But I got lost..."
    show daisy f_sad
    show player 10b
    player_name "You did?"
    show player 5b
    show daisy f_sad_talk
    daisy "Uh huh."
    daisy "It was so scary!"
    daisy "I was lost for days with no food or water..."
    daisy "... But then, they saved me."
    show daisy f_sad
    show player 10b
    player_name "Who saved you?"
    show player 5b
    show daisy f_sad_talk
    daisy "Bernice and Jethro."
    daisy "They brought me back to their house and gave me food."
    show daisy f_sad
    show player 10b
    player_name "Well that was lucky."
    show player 5b
    show daisy f_sad_talk
    daisy "It was... "
    show daisy a_naked_wiping_tears with dissolve
    daisy "{b}*Sniff*{/b}"
    show daisy a_naked_sides with dissolve
    daisy "They were very nice people."
    daisy "Master didn't think so though..."
    show daisy f_sad
    player_name "Hmm?"
    show daisy f_sad_talk
    daisy "He was so mad at me!"
    daisy "I told him I didn't mean to but he grabbed me by the arm really hard and pulled me out of the house."
    daisy "Jethro yelled at him to take it easy and Master hit him."
    daisy "Over and over and over again."
    daisy "It was awful!"
    show daisy f_sad
    show player 10b
    player_name "What an asshole..."
    player_name "Why was he so mad?!"
    show player 5b
    show daisy f_sad_talk
    daisy "He said other people couldn't be trusted, especially men."
    daisy "That they would hand me over to the Gophermant for a pat on the head."
    show daisy f_sad
    show player 10b
    player_name "Gophermant?!"
    show player 5b
    pause
    show player 10b
    player_name "Do you mean Government?"
    show player 5b
    show daisy f_sad_talk
    daisy "Yeah, that's the one."
    show daisy f_sad
    player_name "..."
    show player 10b
    player_name "So then what happened?"
    show player 5b
    show daisy f_sad_talk
    daisy "After that, master started to chain me up in the shack at night."
    show daisy f_sad
    show player 10b
    player_name "He chained you up?!"
    show player 5b
    show daisy f_sad_talk
    daisy "Yeah, he said it was for my own good..."
    daisy "... That I was a bad girl."
    show daisy f_sad
    show player 10b
    player_name "You're not a bad girl, {b}Daisy{/b}."
    player_name "It sounds to me, like he was a bad master."
    show player 5b
    show daisy f_sad_talk
    daisy "{b}*Sniff*{/b} R-really?"
    show daisy f_sad
    show player 10b
    player_name "Yes."
    player_name "You definitely didn't deserve to be treated like that!"
    show player 5b
    show daisy f_sad_talk_closed
    daisy "It's hard to sleep when you're chained up."
    show daisy f_sad
    show player 10b
    player_name "I bet."
    player_name "I'd like to chain him up and show him how it feels!"
    show player 5b
    daisy "..."
    show player 10b
    player_name "So that's why you were scared when you saw us?"
    show player 5b
    show daisy f_sad_talk
    daisy "Uh huh."
    daisy "I was worried master would find out."
    show daisy f_sad
    show player 10b
    player_name "Well, there's no need to worry about that."
    player_name "{b}Diane{/b} and I won't let anybody hurt you, ever again."
    show player 5b
    return

label daisy_button_how_are_your_flowers_3:
    show player 14b
    player_name "How are your flowers?"
    show daisy f_normal_talk
    daisy "Oh, the {b}Sunflowers{/b} you got me are so pretty!"
    daisy "I love them!"
    show daisy f_normal
    show player 14b
    player_name "That's great!"
    player_name "I had a feeling they would cheer you up."
    show player 1b

    daisy "Mmhmm!"
    return

label daisy_button_you_seem_happy:
    show player 14b
    player_name "You seem really happy today."
    show player 1b
    show daisy f_normal_talk
    daisy "I am!"
    daisy "Very, very happy!"
    daisy "I get to live here in the nice barn and {b}Diane{/b} takes care of me and you bring me yummy pizza..."
    show daisy f_normal
    pause

    show daisy f_normal_talk
    daisy "I'm glad you were the one who found me {b}[firstname]{/b}."
    show daisy f_normal
    show player 14b
    player_name "Yeah, me too."
    player_name "I like seeing you happy, {b}Daisy{/b}!"
    show player 1b
    show daisy f_surprised_after_appear
    daisy "!!!"
    show daisy a_naked_touch with dissolve
    pause
    show player 10b
    player_name "You okay?"
    show player 5b
    show daisy f_normal_talk
    daisy "Y-yeah."
    show daisy a_naked_sides with dissolve
    daisy "Sometimes, I feel funny in my tummy when you're around..."
    show daisy f_normal
    player_name "Hmm?"
    show player 10b
    player_name "Does it hurt?"
    show player 5b
    show daisy f_down_talk
    daisy "N-no, it feels... All tingly."
    show daisy f_down
    show player 10b
    player_name "Huh, weird."
    show player 5b
    return

label daisy_button_want_me_to_milk_you:
    show daisy f_normal_talk
    show player 1b at left
    daisy "Umm, {b}[firstname]{/b}?"
    show daisy f_normal
    show player 14b
    player_name "Yeah?"
    show player 1b
    show daisy f_normal_talk
    daisy "C-could you milk me?"
    show daisy f_down_talk b_naked_boob a_empty with dissolve
    daisy "Cause my boobies are all full again."
    show daisy f_down
    pause
    show player 14b
    player_name "{b}*Gulp*{/b} S-sure."
    hide player
    show daisy b_player_milking a_empty f_down
    with dissolve
    daisy "!!!"
    player_name "Does that feel alright?"
    show daisy f_down_talk
    daisy "Y-yes."
    show daisy f_down
    player_name "Just relax and enjoy, {b}Daisy{/b}."
    return

label daisy_button_finished_milking_intro:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh a_naked_up
    with dissolve
    daisy "{b}*Gasp* [firstname]{/b}!!!"
    show daisy f_normal a_naked_sides with dissolve
    show player 14b
    player_name "Hey, {b}Daisy{/b}."
    show player 1b
    show daisy f_normal_talk
    daisy "What are we gonna do today?!"
    show daisy f_normal
    show player 14b
    player_name "Heh, I don't know yet."
    show player 1b
    return

label daisy_button_daisy_need_milking:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh
    with dissolve
    daisy "Okay, I'm ready!"
    show daisy f_normal
    show player 10b
    player_name "C-can I ask you something?"
    show player 5b
    daisy "Hmm?"
    show player 10b
    player_name "How come you want me to-"
    player_name "{b}*Ahem*{/b} M-milk you?"
    show player 5b
    show daisy f_normal_talk
    daisy "Well, {b}Diane{/b} says you're better at it than she is and..."
    show daisy f_down_talk
    daisy "... And I..."
    show daisy f_down
    pause

    show daisy f_down_talk
    daisy "... Y-you make me..."
    daisy "... I dunno."
    show daisy f_laugh
    show player 14b
    player_name "Umm, okay."
    show daisy f_normal
    player_name "I guess, we should get started, huh?"
    show player 1b
    pause
    hide player
    show daisy b_player_milking a_empty f_down
    with dissolve
    daisy "!!!"
    player_name "Does that feel alright?"
    show daisy f_down_talk
    daisy "Y-yes."
    show daisy f_down
    player_name "Let me know if I do anything that doesn't, okay?"
    show daisy f_normal_smelling
    daisy "Mmmhmm."
    pause
    show daisy f_down_talk
    daisy "{b}Diane{/b} was right, you are really good at this!"
    show daisy f_down
    player_name "Heh, thanks."
    show daisy f_down_talk
    daisy "Ahh!"
    show daisy f_down
    player_name "Just relax and enjoy, {b}Daisy{/b}."
    return

label daisy_button_get_new_flowers_has_flowers:
    scene expression player.location.background_blur with None
    show player 14b at left
    show daisy a_naked_shy_front b_naked_shy f_shy_sad at Position (yoffset=10)
    with dissolve
    player_name "Hey, {b}Daisy{/b}."
    show player 1b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Hi, {b}[firstname]{/b}."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 14b
    player_name "I've got something for you."
    show player 1b
    daisy "Hmm?"
    show player 239_240 with dissolve
    pause
    show player 722 with dissolve
    pause
    show daisy f_normal_talk b_naked a_naked_cover with dissolve
    daisy "{b}*Gasp*{/b} Wowzers!!!"
    show player 1b
    show daisy a_naked_sunflower1 f_down_talk
    with dissolve
    daisy "Look how big and pretty they are!"
    pause
    show daisy a_naked_sunflower2 f_normal_smelling with dissolve
    daisy "Mmm!"
    show daisy b_naked_hug f_empty a_empty
    hide player
    with dissolve
    daisy "Thank you, thank you, thank you!!!"
    show player 14b at left
    show daisy a_naked_sunflower1 b_naked f_down zorder 1 at Position (xpos=300)
    with dissolve
    player_name "Heh, you're welcome."
    show player 1b
    show daisy f_down_talk
    daisy "What are these flowers called?"
    show daisy f_down
    show player 14b
    player_name "Those are called {b}Sunflowers{/b}."
    show player 1b
    show daisy f_normal_talk
    daisy "Why do they call them that?"
    show daisy f_normal
    show player 14b
    player_name "Hmm, probably because of their yellow color."
    show player 1b
    show daisy f_normal_talk
    daisy "Oh, I get it."
    show daisy f_laugh
    daisy "Like the sun!"
    show daisy f_down
    show player 14b
    player_name "Heh, that's right."
    show player 1b
    show daisy f_laugh
    daisy "Hehe!"
    show daisy f_normal
    show diane b_shirtless a_shirtless_sides f_shamed_talk_fardown at Position (xpos=600) with dissolve
    show player 13
    dia "Oh, did you get new flowers?"
    show diane f_shamed_fardown with None
    show daisy f_laugh at flip
    show daisy at Position (xpos=750)
    with dissolve
    daisy "{b}[firstname]{/b} brought me some!"
    show daisy f_down
    show diane f_smirk_talk
    dia "Well, wasn't that nice of him..."
    show diane f_smirk
    show daisy f_normal_talk
    daisy "Uh huh!"
    daisy "{b}[firstname]{/b} is the nicest man ever!"
    show daisy f_down
    show diane f_smirk_talk
    dia "He certainly is."
    show diane f_smirk
    pause
    show diane f_shamed_talk_fardown
    dia "Alright, we should get those flowers in some water so I can get you milked, sweetie."
    dia "Lots of work to be done today."
    show diane f_shamed_fardown with None
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=300)
    with dissolve
    daisy "I want {b}[firstname]{/b} to do it."
    show player 11
    player_name "!!!" with hpunch
    show player 10b
    player_name "W-what?"
    show player 5b
    show daisy f_normal_talk
    daisy "Is it okay if {b}[firstname]{/b} milks me, {b}Diane{/b}?"
    show daisy f_normal
    show diane f_shamed_talk_fardown
    dia "It's fine with me."
    show diane f_shamed_fardown with None
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=300)
    with dissolve
    show diane f_smirk
    daisy "Will you milk me, {b}[firstname]{/b}?"
    show daisy f_normal
    show player 14b
    player_name "Uhh, sure... If that's what you want."
    show player 1b
    show daisy f_laugh
    daisy "Yay!!"
    show daisy f_normal
    show diane f_smirk_talk
    dia "Just be careful with her, okay?"
    show diane f_smirk
    show player 14
    player_name "Y-yeah, I will."
    show player 13
    show diane f_shamed_talk_fardown
    dia "Alright, let's go take care of those flowers."
    show diane f_shamed_fardown
    show daisy f_shy_talk_back
    daisy "Okay."
    show daisy f_normal_talk
    daisy "I'll be right back, {b}[firstname]{/b}."
    show daisy f_normal
    show player 14b
    player_name "O-okay."
    hide player
    hide daisy
    hide diane
    with dissolve
    return

label daisy_button_get_new_flowers_no_flowers:
    scene expression player.location.background_blur with None
    show player 10b at left
    show daisy a_naked_cover f_sad_talk_closed
    with dissolve
    player_name "You okay?"
    show player 5b
    show daisy a_naked_wiping_tears with dissolve
    daisy "Yeah."
    show daisy a_naked_shy_front b_naked_shy f_shy_sad_talk at Position (yoffset=10) with dissolve
    daisy "I just miss my flowers..."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "I'm sorry, {b}Daisy{/b}."
    player_name "Can I get you anything?"
    player_name "I don't like seeing you sad like this..."
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "No, it's alright."
    show daisy f_shy_sad at Position (yoffset=10)
    pause
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Thanks, {b}[firstname]{/b}."
    hide daisy with dissolve
    show player 5
    player_name "( Hmm, I should go to {b}Cupid{/b} and {b}the Mall{/b} and {b}get her some new flowers{/b}. )"
    show player 13
    player_name "( I bet that will cheer her up. )"
    pause
    player_name "( {b}Diane{/b} said I should look for {b}Sunflowers{/b}. )"
    hide player with dissolve
    return

label daisy_button_sleeping:
    show player 434 with dissolve
    player_name "( Aww, look how cute she is when she's sleeping! )"
    player_name "( I should leave her be. )"
    hide player with dissolve
    return

label daisy_button_no_veggie_pizza:
    show player 1b
    show daisy f_normal_talk
    daisy "Did you bring me another {b}veggie pizza{/b}?"
    show daisy f_normal
    show player 10b
    player_name "No, not today."
    show player 5b
    show daisy f_sad_talk
    daisy "Aww..."
    show daisy f_sad
    show player 10b
    player_name "Sorry, {b}Daisy{/b}..."
    player_name "... Maybe tomorrow, okay?"
    show player 5b
    show daisy f_sad_talk
    daisy "Okay."
    show daisy f_sad
    return

label daisy_button_has_veggie_pizza:
    show player 14b
    player_name "I brought you something!"
    show player 1b
    show daisy f_normal_talk
    daisy "{b}*Gasp*{/b} A present?!"
    show daisy f_normal
    player_name "Mmmhmm."
    show player 239_240 with dissolve
    pause
    show player 719c with dissolve
    show daisy f_normal_talk
    daisy "{b}Veggie pizza{/b}?!"
    show daisy f_normal
    show player 719d
    player_name "Hehe, that's right!"
    show player 719c
    show daisy f_laugh
    daisy "Yay!!"
    show daisy f_normal
    show player 721 with dissolve
    pause
    show player 18
    show daisy a_naked_pizza_slice
    with dissolve
    pause
    show daisy f_laugh a_naked_up with dissolve
    daisy "I love pizza!!"
    show player 17
    player_name "Me too!"
    show player 1b
    show daisy a_naked_pizza_eat with dissolve
    pause
    daisy "Mmm!"
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_more_jebadiah_delmont:
    show player 10b
    player_name "So, do you think you're ready to tell me more about your old Master?"
    show player 5b
    show daisy f_shy_sad_talk a_naked_shy_front b_naked_shy at Position (yoffset=10) with dissolve
    daisy "Mmm, maybe..."
    daisy "What do you want to know?"
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "What was he like?"
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Hmm, Master was..."
    daisy "... Different, than you and {b}Diane{/b}."
    daisy "He didn't get along with other people very well but he didn't want to be alone either."
    daisy "So he made me."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "He made you?"
    show player 5b
    daisy "Mmhmm."
    show player 10b
    player_name "How did he do that?"
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "I don't know..."
    show daisy f_normal_talk b_naked a_naked_sides with dissolve
    daisy "... Maybe he used his magics?"
    show daisy f_normal
    pause
    show player 14b
    player_name "So you really saw him do magic then?"
    show player 1b
    show daisy f_laugh
    daisy "Oh yes, wonderful magics!"
    show daisy f_normal
    pause
    show daisy f_normal_talk
    daisy "He could remove his thumb or pull money out from behind my ear whenever he wanted!"
    show daisy f_normal
    show player 5b
    player_name "..."
    show daisy f_normal_talk
    daisy "He had a storm cloud that he trapped inside a stick!"
    show daisy f_normal
    show player 10b
    player_name "Huh?"
    show player 5b
    show daisy f_normal_talk
    daisy "Yeah, if you turned it upside down, you could hear it raining inside!"
    show daisy f_normal
    player_name "..."
    show daisy f_laugh
    daisy "Oh, oh, oh, and he had a glass ball full of snow from the north pole!"
    show daisy f_normal
    show player 10b
    player_name "Let me guess, you had to shake it and then the snow would fall?"
    show player 5b
    show daisy f_normal_talk
    daisy "Yeah!"
    show daisy f_shy_talk
    daisy "How did you know that?!"
    show daisy f_shy
    show player 14b
    player_name "They're called snow globes."
    show player 1b
    show daisy f_sad_talk
    daisy "{b}*Gasp*{/b} Do you know magics too?!"
    show daisy f_sad
    show player 10b
    player_name "{b}Daisy{/b}, I don't think any of that was magic..."
    show player 5b
    show daisy f_normal_talk
    daisy "What about his wand then?!"
    show daisy f_normal
    show player 10b
    player_name "Wand?"
    show player 5b
    show daisy f_normal_talk
    daisy "Yeah, it would make a clicky sound and then fire would spurt from the tip!"
    show daisy f_laugh
    daisy "It was definitely magics!"
    show daisy f_normal_talk
    daisy "I saw it."
    show daisy f_normal
    player_name "..."
    return

label daisy_button_milking_business:
    show player 14b
    player_name "So you like it when {b}Diane{/b} milks you?"
    show player 1b
    show daisy f_normal_talk
    daisy "Oh, yes!"
    show daisy f_laugh a_naked_up with dissolve
    daisy "Milking makes my boobies feel good!"
    show daisy f_normal_talk a_naked_sides with dissolve
    daisy "Plus, she's much gentler than Master was..."
    show daisy f_normal
    pause
    show daisy f_normal_talk
    daisy "... I just wish it didn't tickle me so!"
    show daisy f_normal
    show player 14b
    player_name "I'm sure she'll figure out a way to do it without tickling you."
    show player 1b
    show daisy f_normal_talk
    daisy "I hope so."
    daisy "I want {b}Diane{/b} to sell my milk too and make people happy!"
    show daisy f_normal
    return

label daisy_button_how_are_your_flowers_2:
    show player 14b
    player_name "How are your flowers?"
    show player 1b
    show daisy f_normal_talk
    daisy "They're still doing good."
    daisy "I give them water and sunlight everyday, just like you told me."
    show daisy f_normal
    show player 14b
    player_name "That's wonderful, {b}Daisy{/b}."
    show player 1b
    daisy "Mmhmm."
    show daisy f_normal_talk
    daisy "{b}Diane{/b} says there's lots of flowers in the world and they come in all sorts of different colors too!"
    daisy "Is that true?"
    show daisy f_normal
    show player 14b
    player_name "Yup, it's true."
    show player 1b
    show daisy f_laugh a_naked_cover with dissolve
    daisy "Wowzers!"
    show daisy f_normal_talk a_naked_sides with dissolve
    daisy "I hope I get to see them all someday..."
    show daisy f_normal
    return

label daisy_button_finished_pizza_intro:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_normal_talk
    daisy "Hi, {b}[firstname]{/b}!"
    show daisy f_normal
    show player 14b
    player_name "Hey, {b}Daisy{/b}."
    player_name "How are you today?"
    show player 1b
    show daisy f_sad_talk
    daisy "Mmm, I'm bored."
    show daisy f_normal_talk
    daisy "What are you doing?"
    show daisy f_normal
    return

label daisy_button_get_pizza_has_not_pizza:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh
    with dissolve
    daisy "Pizza!"
    daisy "Hehehe!"
    show daisy f_normal
    show player 14b
    player_name "Heh, she's so excited."
    player_name "I should head to {b}Tony's Pizzeria{/b} and get her a {b}veggie pizza{/b}."
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_get_pizza_has_pizza:
    scene expression player.location.background_blur with None
    show player 719d at left
    show daisy
    with dissolve
    player_name "{b}Daisy{/b}?"
    player_name "Look what I've brought for you!"
    show player 719c
    show daisy f_laugh
    daisy "Pizza?!"
    show daisy f_normal
    show player 720 with dissolve
    player_name "Mmmhmm!"
    show daisy f_normal_talk
    daisy "Oh, it smells really good!"
    show daisy f_normal
    pause
    show daisy f_sad_talk
    daisy "How do I eat it?"
    show daisy f_sad
    show player 720b
    player_name "Hehe, lemme show you."
    show daisy f_normal
    show player 721 with dissolve
    player_name "You just hold it like this and start eating from this end here."
    show player 719d with dissolve
    player_name "Mmm, so good!!"
    show player 719c
    pause
    show player 719d
    player_name "Now you try."
    show daisy a_naked_pizza_hold f_normal_talk
    show player 1b
    with dissolve
    daisy "O-okay."
    show daisy a_naked_pizza_slice f_sad_talk with dissolve
    daisy "Like this?"
    show daisy f_normal
    show player 14b
    player_name "Yup, just like that."
    show player 1b
    show daisy f_normal_talk
    daisy "{b}*Gasp*{/b} Wowzers!!! My first pizza!"
    show daisy f_normal
    show player 17 with dissolve
    player_name "Hehe!"
    show player 1b
    show daisy a_naked_pizza_eat f_empty with dissolve
    daisy "Mmmhmm!!!"
    show player 11
    player_name "!!!" with hpunch
    pause
    daisy "More!"
    show player 10b
    player_name "Yeah, eat as much as you'd like..."
    hide player
    hide daisy
    with dissolve
    scene expression "backgrounds/location_diane_garden_cutscene13.jpg"
    show expression FilteredText("The pizza went over even better than I had expected.\nTo this day I have never seen anyone throw down food like {b}Daisy{/b}.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("{b}Daisy{/b} went through eight pieces in the time it took me to eat two!") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy o_sauce f_burp
    with dissolve
    daisy "{b}*Buuuuurp*{/b}"
    show daisy f_normal
    show player 14b
    player_name "Heh, you alright over there?"
    show player 1b
    show daisy f_laugh
    daisy "That was so delicious!!"
    show daisy f_normal_talk
    daisy "Can I eat pizza everyday?!"
    show daisy f_normal
    show player 17
    player_name "Haha, I don't think that would be a good idea..."
    show player 1b
    show daisy f_sad_talk
    daisy "Oh."
    show daisy f_sad
    show player 14b
    player_name "... but I can bring you some every now and then."
    show player 1b
    show daisy f_laugh a_naked_up with dissolve
    daisy "Yay!"
    daisy "I like pizza!"
    show daisy f_normal a_naked_sides with dissolve
    show player 14b
    player_name "Hehe, me too!"
    show player 433
    show daisy f_normal_talk
    daisy "Thank you, {b}[firstname]{/b}!"
    hide player
    show daisy b_naked_hug f_empty a_empty o_empty
    with dissolve
    player_name "Y-you're welcome, {b}Daisy{/b}."
    show daisy f_normal_talk o_sauce b_naked a_naked_sides
    show player 1b at left
    with dissolve
    daisy "I'm gonna go see if {b}Diane{/b} wants some pizza too!"
    hide daisy with dissolve
    show player 13
    pause
    show player 14
    player_name "You better tell her to hurry, there's only a few slices left!"
    show player 13
    pause
    show player 18
    player_name "( I'm really glad I did this. )"
    player_name "( {b}Daisy{/b} is so cute when she's happy. )"
    show player 13
    pause
    show player 426
    player_name "( Alright, I'd better finish up here and get to work on the garden before I run out of daylight. )"
    hide player with dissolve
    return

label daisy_button_leave:
    show player 14b at left
    if not M_daisy.finished_state(S_daisy_get_pizza):
        show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    else:
        show daisy f_normal
    player_name "I should get back to work."
    player_name "Let me know if you need anything, okay?"
    show player 1b
    if not M_daisy.finished_state(S_daisy_get_pizza):
        show daisy f_shy_shy_talk at Position (yoffset=10)
    else:
        show daisy f_normal_talk
    daisy "O-okay."
    daisy "Bye, {b}[firstname]{/b}."
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_jebadiah_delmont:
    show player 10b at left
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    player_name "So your old master doesn't sound like a very nice guy, huh?"
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Mmm, he {i}could{/i} be nice... Sometimes."
    daisy "When I was a good girl."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "Oh?"
    show player 5b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "He would bring me presents and teach me songs."
    show daisy f_shy_shy at Position (yoffset=10)
    show player 10b
    player_name "Well, that doesn't sound so bad..."
    show player 5b
    show daisy f_shy_sad_talk a_naked_shy_cover at Position (yoffset=10) with dissolve
    daisy "As long as I stayed quiet in the shack and didn't touch his things, I was a good girl."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "What happened if you left the shack?"
    show player 5b
    show daisy f_shy_sad_talk_closed at Position (yoffset=10)
    daisy "I don't-"
    daisy "H-he would-"
    show daisy b_naked a_naked_cover f_sad_talk_closed with dissolve
    pause
    show player 10b
    player_name "Do you wanna talk about it?"
    show player 5b
    daisy "No, please no!"
    show player 10b
    player_name "It's okay, we don't have to-"
    show player 433
    daisy "No, no, no, no-"
    show player 10b
    player_name "{b}Daisy{/b}, it's okay..."
    player_name "We don't have to talk about him at all if you don't want to."
    show player 5b
    show daisy f_sad_talk
    daisy "{b}*Sniff*{/b} I-I'm a good girl?"
    show daisy f_sad
    show player 14b
    player_name "Of course!"
    show player 10b
    player_name "I didn't mean to upset you, I-"
    show player 5b
    pause
    show player 14b
    player_name "You don't need to worry, {b}Daisy{/b}."
    player_name "{b}Diane{/b} and I would never hurt you."
    show player 1b
    show daisy f_shy_sad_talk a_naked_shy_front b_naked_shy at Position (yoffset=10) with dissolve
    daisy "O-okay."
    show daisy f_shy_sad at Position (yoffset=10)
    return

label daisy_button_about_yourself:
    show player 14b at left
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    player_name "Tell me about yourself."
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Me?!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Yeah, I'd like to know more about you."
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "I don't-"
    daisy "There's not much-"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Is there anything you like?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Umm, flowers?"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 17
    player_name "Heh, anything besides flowers?"
    show player 1b
    show daisy f_shy_down at Position (yoffset=10)
    daisy "Hmm."
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Oats!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 10b
    player_name "Oats?"
    show player 5b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Yeah, Master used to feed me oats all the time."
    show daisy f_shy_laugh at Position (yoffset=10)
    daisy "It was yummy!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "What's {b}Diane{/b} been feeding you?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Oh, lots of stuff..."
    daisy "She says I should try other things and not just eat oats all the time."
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "She's right."
    player_name "What have you tried so far?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Mmm, I've tried lettuce, carrots, bopples, grapes-"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 10b
    player_name "Bopples?"
    player_name "What's a bopple?"
    show player 1b
    show daisy f_shy_down_talk at Position (yoffset=10)
    daisy "Umm, they are red and crunchy and they make my tongue feel funny."
    show daisy f_shy_shy at Position (yoffset=10)
    player_name "Hmm?"
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "{b}Diane{/b} says it's because they are sweet."
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Do you mean an apple?"
    show player 1b
    show daisy f_shy_laugh at Position (yoffset=10)
    daisy "Yes, that's it!"
    show daisy f_shy_down_talk at Position (yoffset=10)
    daisy "Apple."
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "It was yummy too, but oats are much better!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Heh, okay."
    show player 1b
    return

label daisy_button_how_are_your_flowers_1:
    show player 14b at left
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    player_name "How are your flowers?"
    player_name "Have you been watching them closely?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Yes, very closely!"
    daisy "{b}Diane{/b} was right, they do drink the water!"
    daisy "It's so neat!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 17
    player_name "Hehehe."
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Do you wanna watch them with me?!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Uhh, no... Sorry {b}Daisy{/b}, I have too much work to do around here."
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Oh, okay."
    show daisy f_shy_shy at Position (yoffset=10)
    return

label daisy_button_still_nervous:
    show player 14b
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    player_name "I still make you nervous, huh?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Y-yeah... A little."
    show daisy f_shy_shy at Position (yoffset=10)
    pause
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "S-sorry."
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Heh, you don't need to be sorry."
    player_name "It's okay, I understand."
    show player 1b
    pause
    show player 14b
    player_name "There's no rush."
    show player 1b
    return

label daisy_button_intro_scared:
    scene expression player.location.background_blur with None
    show player 10b at left
    show daisy b_naked_behind_sad f_empty a_empty
    with dissolve
    player_name "Hi there, uhh-"
    show player 11
    show daisy b_jump_scared
    cow "EEEEP!!!" with hpunch
    show daisy b_naked a_naked_cover f_sad_talk_closed
    pause
    show player 24
    dia "{b}[firstname]{/b}!"
    show diane b_naked a_naked_sides f_shamed_talk_smile at Position (xpos=600)
    dia "She's still frightened of you!"
    show diane f_shamed
    show player 25
    player_name "I'm sorry, I didn't mean to scare her."
    show player 24
    show diane f_shamed_talk_smile
    dia "It's alright."
    dia "Just give me a little more time with her, okay?"
    show diane f_shamed
    pause
    show diane f_shamed_talk_smile
    dia "{b}I'll let you know when she's ready to speak with you.{/b}"
    show diane f_shamed
    show player 25
    player_name "O-okay."
    hide player with dissolve
    return

label daisy_button_intro:
    scene expression player.location.background_blur with None
    show player 14b at left
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    with dissolve
    player_name "Hey, {b}Daisy{/b}."
    show player 1b
    daisy "..."
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "H-hi."
    show daisy f_shy_shy at Position (yoffset=10)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
