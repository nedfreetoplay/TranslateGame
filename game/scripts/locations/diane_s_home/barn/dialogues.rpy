label barn_daisy_pregnancy_anouncement_repeat:
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_naked a_naked_sides f_normal at Position (xpos=600)
    show daisy f_normal at Position (xpos=300)
    with dissolve
    player_name "Hey, I got your text."
    show player 5
    show diane f_normal_talk
    dia "{b}Hey, {b}[firstname]{/b}."
    dia "You uhh, might want to sit down for this..."
    show diane f_normal
    player_name "Hmm?"
    show player 10b
    player_name "What's going on?"
    show player 5
    show diane f_normal_talk
    dia "{b}Daisy{/b} is pregnant again."
    show diane f_normal
    show player 10b
    player_name "Again?!"
    player_name "That's-"
    show player 5
    pause
    show player 30
    player_name "Are you sure?"
    show player 5
    show diane f_normal_talk
    dia "Well, the poor thing has been sick every morning for the past 3 days and she missed her... Umm..."
    show diane f_normal
    pause
    show diane f_shamed_talk_fardown
    dia "{b}*Ahem*{/b} I'm pretty sure."
    show diane f_shamed_fardown
    show player 10b
    player_name "{b}*Phew*{/b} Okay..."
    show player 5b
    show diane f_normal_talk
    dia "Oh, don't you worry. Everything is going to be fine."
    show diane f_laugh
    dia "A child is a blessing!"
    show diane f_normal
    show player 10b
    player_name "How are you taking all this {b}Daisy{/b}?"
    show player 5b
    show daisy f_normal_talk
    daisy "I'm gonna be a mommy again!"
    show daisy f_normal
    show diane f_laugh
    dia "Hehe, you certainly are sweetie."
    show diane f_smirk_talk_fardown
    dia "C'mon, let's go and get you some food."
    dia "You're eating for two now."
    show diane f_smirk
    hide daisy with dissolve
    pause
    show diane f_smirk_talk
    dia "Chin up, {b}[firstname]{/b}!"
    show diane f_smirk
    show player 5
    player_name "Hmm?"
    show diane f_smirk_talk
    dia "You're gonna be a father again."
    dia "It's good news."
    show diane f_smirk
    show player 14
    player_name "Yeah, I know."
    show player 13
    show diane f_laugh
    dia "Congratulations!"
    show diane f_smirk
    show player 14
    player_name "Thanks, {b}Diane{/b}."
    hide diane with dissolve
    pause
    show player 24
    player_name "( Holy crap. )"
    player_name "( {b}Daisy{/b} is going to have another kid... )"
    player_name "{b}*Gulp*{/b} I hope I'm ready for this."
    hide player with dissolve
    return

label barn_daisy_pregnancy_seen_in_labor:
    scene expression player.location.background_blur with None
    show player 5 at left
    show diane b_naked a_naked_sides f_normal_talk at Position (xpos=600)
    show daisy a_naked_baby f_down at Position (xpos=300)
    with dissolve
    dia "There he is!"
    show diane f_normal
    pause
    show diane f_teasing_look
    show daisy f_normal
    dia "There's your daddy!"
    show diane f_normal
    show player 3 with dissolve
    player_name "{b}*Gulp*{/b}"
    show diane f_normal_talk
    dia "Come on, handsome."
    if M_daisy.pregnancy.baby_gender == "boy":
        dia "You have to meet {b}your new son{/b}."
        show diane f_smirk_fardown
        show player 10 with dissolve
        player_name "{b}M-my son{/b}?"
    else:
        dia "You have to meet {b}your new daughter{/b}."
        show diane f_smirk_fardown
        show player 10 with dissolve
        player_name "{b}M-my daughter{/b}?"
    show player 13
    dia "Mmhmmm."
    show player 426
    show daisy f_down
    with dissolve
    pause
    show player 14
    player_name "Wow..."
    if M_daisy.pregnancy.baby_gender == "boy":
        player_name "... He's so cute!"
    else:
        player_name "... She's so cute!"
    show player 426
    show diane f_laugh
    dia "Hehe, yup."
    if M_daisy.pregnancy.baby_gender == "boy":
        dia "Just like his daddy."
    else:
        dia "Just like her mommy."
    show diane f_cheese
    show player 14b
    player_name "How are you feeling {b}Daisy{/b}?"
    show player 1b
    show diane f_smirk_fardown
    show daisy f_sad_talk
    daisy "Tired."
    show daisy f_sad
    show diane f_normal_talk
    if M_daisy.pregnancy.baby_gender == "boy":
        dia "She was up all night pushing this little guy out."
    else:
        dia "She was up all night pushing this little gal out."
    dia "It took a lot out of her."
    show diane f_smirk_fardown
    pause
    show daisy f_down
    show player 10
    player_name "Everything went okay though, right?"
    show player 5
    show diane f_normal_talk
    dia "Oh, yeah."
    dia "You'll be back on your feet in no time, won't you sweetie?"
    show diane f_smirk_fardown
    show daisy f_down_talk
    daisy "Yeah!"
    show daisy f_laugh
    daisy "We have a baby, {b}[firstname]{/b}!"
    show daisy f_normal
    show player 14b
    player_name "Y-yeah, I know."
    player_name "Don't worry, I'll take care of you guys."
    show player 1b
    show diane f_laugh
    dia "Aww, you're so sweet, {b}[firstname]{/b}."
    show diane f_smirk_talk_fardown
    dia "C'mon, we should let them rest."
    dia "Say bye to Daddy!"
    show diane f_normal
    pause
    show player 429
    player_name "I'll see you both soon, okay."
    show player 1b
    show daisy f_normal_talk
    daisy "okay, {b}[firstname]{/b}."
    hide daisy
    hide player
    hide diane
    with dissolve
    return

label barn_daisy_pregnancy_anouncement_first:
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_naked a_naked_sides f_sad at Position (xpos=600)
    show daisy f_sad at Position (xpos=300)
    with dissolve
    player_name "Hey, I got your text."
    show player 5
    show diane f_sad_talk
    dia "{b}Hey, {b}[firstname]{/b}."
    dia "You uhh, might want to sit down for this..."
    show diane f_sad
    player_name "Hmm?"
    show player 10b
    player_name "What's going on?"
    show player 5
    show diane f_sad_talk
    dia "I think {b}Daisy{/b} is pregnant."
    show diane f_sad
    show player 23
    player_name "What?!"
    player_name "I didn't think-"
    player_name "I mean, are you sure?!"
    show player 5
    show diane f_sad_talk
    dia "Well, the poor thing has been sick every morning for the past 3 days and she missed her... Umm..."
    show diane f_sad
    pause
    show diane f_sad_talk
    dia "{b}*Ahem*{/b} I'm pretty sure."
    show diane f_sad
    show player 10
    player_name "Wow, umm... Okay."
    player_name "I didn't think she could get pregnant."
    show player 5
    show diane f_sad_talk
    dia "Yeah, I didn't think so either..."
    show diane f_sad
    show player 10
    player_name "What are we going to do?"
    show player 5
    show diane f_normal_talk
    dia "Oh, don't you worry. Everything is going to be fine."
    show diane f_laugh
    dia "A child is a blessing!"
    show diane f_normal
    show player 10b
    player_name "How are you taking all this {b}Daisy{/b}?"
    show player 5b
    show daisy f_sad_talk
    daisy "I-"
    show daisy f_sad
    pause
    show daisy f_sad_talk
    daisy "I don't know..."
    daisy "Do you think I'll be a good mommy?"
    show daisy f_sad
    show diane f_normal_talk
    dia "Of course you will, sweetie!"
    dia "Besides, {b}[firstname]{/b} and I will be here to help you, every step of the way."
    show diane f_normal_talk
    dia "Won't we, {b}[firstname]{/b}?"
    show diane f_normal
    show player 14
    player_name "Y-yeah, of course!"
    show player 13
    show diane f_normal_talk
    dia "In fact, why don't you come with me. I've got some books on the subject you can look at."
    show diane f_normal
    show daisy f_sad_talk
    daisy "O-okay, {b}Diane{/b}."
    hide daisy
    hide diane
    with dissolve
    pause
    show player 24
    player_name "Holy crap."
    player_name "{b}Daisy{/b} is going to have my child..."
    player_name "{b}*Gulp*{/b} I hope I'm ready for this."
    hide player with dissolve
    return

label barn_daisy_caught_breeding_aftermath:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh at Position (xpos=300)
    show diane b_naked a_naked_sides f_smirk at Position (xpos=580)
    with dissolve
    daisy "Hi, {b}[firstname]{/b}!"
    show daisy f_normal
    show player 14b
    player_name "Hey, {b}Daisy{/b}. {b}Diane{/b}."
    show player 1
    show diane f_smirk_talk
    dia "Hello."
    show diane f_smirk
    pause
    show diane a_nudge f_smirk_talk_fardown with dissolve
    dia "{b}*Ahem*{/b}"
    show diane a_naked_sides f_smirk_fardown with dissolve
    show daisy f_shy_talk
    daisy "S-so, {b}Diane{/b}'s been telling me all about sex..."
    show daisy f_shy
    show player 11
    player_name "!!!"
    show daisy f_shy_talk
    daisy "... And how it's something that two consenting adults should only do when they love each other very much."
    show daisy f_shy
    show player 10b
    player_name "O-okay?"
    show player 5b
    show diane f_smirk_talk_fardown
    dia "Aaand?"
    show diane f_smirk_fardown
    show daisy f_shy_talk
    daisy "... And that my master was lying and taking advantage of me, which is wrong..."
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "That's right."
    show diane f_smirk_fardown
    show daisy f_laugh
    daisy "Oh!"
    show daisy f_shy_talk
    daisy "... And that they're not called a weasel or a hidey-hole."
    daisy "You have a penis and I have a floogina!"
    show daisy f_shy
    player_name "..."
    show diane f_smirk_talk_fardown
    dia "VA-gina, dear."
    show diane f_smirk_fardown
    show daisy f_laugh
    daisy "Oops, sorry!"
    daisy "Vagina. I have a vagina."
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "Very good, sweetie."
    show diane f_smirk_fardown with None
    show daisy f_normal_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    daisy "So can {b}[firstname]{/b} and I have sex now?!"
    show daisy f_normal
    show player 11
    show diane f_surprised
    player_name "!!!" with hpunch
    show diane f_shamed_talk_smile
    dia "{b}*Sigh*{/b}"
    show player 5
    show diane f_shamed_talk_fardown
    dia "{b}Daisy{/b}, I told you why {b}[firstname]{/b} and I are having sex, didn't I?"
    show diane f_shamed_fardown
    show daisy f_normal_talk
    daisy "Yes, because you're consenting adults that love each other very much..."
    daisy "... And it increases your milk production."
    show daisy f_normal
    show diane f_shamed_talk_fardown
    dia "That's right, it's for my business."
    show diane f_shamed_fardown
    show daisy f_laugh
    daisy "I'm part of the business too!"
    show daisy f_normal
    show diane f_shamed_talk_fardown
    dia "I know that, but-"
    show diane f_shamed_fardown
    show daisy f_normal_talk
    daisy "... And I'm an adult and I love {b}[firstname]{/b}..."
    daisy "... And I wanna have sex too!"
    show daisy f_normal
    show diane f_shamed_talk_fardown
    dia "{b}*Sigh*{/b}"
    dia "Well, that's between you and {b}[firstname]{/b} then."
    show daisy at unflip
    show daisy at Position (xpos=300)
    with dissolve
    show diane f_shamed
    show player 10
    player_name "Huh?!"
    show player 5
    pause
    show player 10
    player_name "Y-you're serious?!"
    show player 5
    show diane f_shamed_talk_smile
    dia "She's right."
    dia "You're both adults and if you two wanna have sex, I can't stop you."
    dia "I'd rather we keep this all out in the open instead of you two doing it behind my back."
    show diane f_shamed
    show player 10
    player_name "I wasn't-"
    player_name "I mean, I wouldn't have-"
    show player 5
    show diane f_shamed_talk_smile
    dia "It's alright, {b}[firstname]{/b}."
    dia "{b}Daisy{/b} is a sweet girl and she really likes you."
    dia "If you like her too, then there's nothing wrong with you two having sex."
    dia "Just promise me you'll be careful."
    show diane f_shamed
    show player 24
    player_name "..."
    show player 5b
    show daisy f_normal_talk
    daisy "I'll be careful!"
    show daisy f_normal
    show diane f_laugh
    dia "Hehe, good girl {b}Daisy{/b}."
    show diane f_smirk
    pause
    show diane f_smirk_talk
    dia "Alright, you two have a lot to talk about and I should get back to work."
    dia "Let me know if you need anything."
    show diane f_smirk with None
    show daisy f_laugh at flip
    show daisy at Position (xpos=750)
    with dissolve
    show diane f_smirk_fardown
    daisy "Thanks, {b}Diane{/b}!"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "You're welcome, sweetie."
    hide diane with dissolve
    pause
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=300)
    with dissolve
    daisy "Are you okay, {b}[firstname]{/b}?"
    daisy "You look funny."
    show daisy f_shy
    show player 10b
    player_name "I don't-"
    show player 5b
    pause
    show player 10b
    player_name "This is all really sudden."
    show player 5b
    show daisy f_sad_talk
    daisy "Oh."
    daisy "You mean, you don't want to have sex with me?"
    show daisy f_sad
    show player 10b
    player_name "I'm not saying that, it's just... Are you sure this is what you want?"
    show player 5b
    show daisy f_normal_talk
    daisy "Oh, yes!"
    daisy "You take care of me and bring me pizza and pretty flowers!"
    daisy "You're like the bestest man in the whole world!"
    daisy "I'd much rather have sex with you than with master..."
    show daisy f_normal
    show player 10b
    player_name "Yeah but you don't have to have sex with anybody, {b}Daisy{/b}..."
    show player 5b
    show daisy f_normal_talk
    daisy "I want to!"
    show daisy f_sexy_talk
    daisy "I think it will be fun to put your weasel in my hidey-hole!"
    show daisy f_sexy
    player_name "..."
    show daisy f_sexy_talk
    daisy "Sorry, I meant your penis... In my floogina."
    show daisy f_sexy
    show player 10b
    player_name "Vagina."
    show player 5b
    show daisy f_shy_talk
    daisy "Oh, right!"
    show daisy f_shy
    pause
    show daisy f_normal_talk
    daisy "So, do you wanna have sex?!"
    show daisy f_sexy
    return

label barn_daisy_caught_breeding_aftermath_yes:
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
    hide daisy
    hide player
    with dissolve
    pause
    return

label barn_daisy_caught_breeding_aftermath_no:
    show player 10b
    player_name "{b}Daisy{/b}, I don't think this is a good idea."
    show player 5b
    show daisy f_sad_talk
    daisy "It's not?"
    show daisy f_sad
    show player 10b
    player_name "We shouldn't rush into this without giving it more thought."
    show player 5b
    show daisy f_sad_talk
    daisy "More thought?"
    daisy "I've been thinking about having sex with you for a long time!"
    show daisy f_sad
    show player 10b
    player_name "Y-you have?"
    show player 5b
    show daisy f_sad_talk
    daisy "Uh huh."
    show daisy f_sad
    pause
    show player 10b
    player_name "Still, I think... I need some time to process all of this..."
    show player 5b
    show daisy f_sad_talk
    daisy "Oh, okay."
    show daisy f_sad
    pause
    show daisy f_sad_talk
    daisy "You'll let me know when you're ready though, right?"
    show daisy f_sad
    show player 10b
    player_name "Yeah, I will."
    show player 5b
    pause
    show player 10b
    player_name "Thanks for understanding, {b}Daisy{/b}."
    show player 5b
    show daisy f_sad_talk
    daisy "You're welcome."
    show daisy f_sad
    pause
    show player 10b
    player_name "I should-"
    player_name "{b}*Ahem*{/b} I should get back to work."
    show player 5b
    show daisy f_sad_talk
    daisy "Okay."
    hide player
    hide daisy
    with dissolve
    return

label barn_dialogue_daisy_caught_breeding:
    scene expression player.location.background_blur with None
    show player 12 with dissolve
    player_name "No, {b}Diane{/b} wanted some alone time with {b}Daisy{/b} to sort out that whole, \"weasel\" situation..."
    player_name "I shouldn't interfere."
    hide player with dissolve
    return

label barn_daisy_dead_flowers:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy b_naked_behind_sad f_empty a_empty zorder 1
    with dissolve
    daisy "Oh no!!!"
    show player 5b
    player_name "Hmm?"
    daisy "No, no, no, no!!"
    show player 10b
    player_name "{b}Daisy{/b}?"
    show player 5b
    show daisy b_naked a_naked_cover f_sad_talk with dissolve
    daisy "{b}[firstname]{/b}, it's terrible!"
    daisy "{b}*Sniff*{/b} Something's wrong!"
    show daisy f_sad
    show player 10b
    player_name "Huh?"
    show player 5b
    show daisy f_sad_talk
    daisy "I think they're sick!"
    show daisy f_sad
    show player 10b
    player_name "{b}Daisy{/b}, I don't-"
    player_name "Who's sick?"
    show player 5b
    show daisy f_sad_talk a_naked_vase_wilted at Position (xpos=300) with dissolve
    daisy "My flowers!!!"
    show daisy f_sad
    show player 10b
    player_name "All of them?!"
    show player 5b
    show daisy f_sad_talk
    daisy "{b}*Sniff*{/b} Y-yes..."
    show daisy f_sad
    show player 10b
    player_name "How did that happen?"
    show player 5b
    show daisy f_sad_talk
    daisy "I don't know! {b}*Sniff*{/b}"
    daisy "They were pretty yesterday..."
    show daisy f_sad
    show player 10b
    player_name "I'm so sorry, {b}Daisy{/b}..."
    show player 5b
    show diane f_sad_talk b_shirtless a_shirtless_sides at Position (xpos=600) with dissolve
    show player 5
    dia "Is {b}Daisy{/b} crying?!"
    show diane f_sad with None
    show daisy f_sad_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    daisy "{b}Diane{/b}, something's wrong with my pretty flowers!!"
    show daisy f_sad

    pause
    show diane f_shamed_talk_fardown
    dia "Aww, sweetie..."
    dia "That's just how it goes with flowers..."
    dia "... They aren't meant to live forever."
    dia "It'll be okay."
    show diane f_shamed_fardown
    show daisy f_sad_talk
    daisy "{b}*Sniff*{/b} But... But..."
    daisy "How do we fix them?"
    show daisy f_sad
    show diane f_shamed_talk_fardown
    dia "I'm afraid, some things, just can't be fixed dear..."
    show diane f_shamed_fardown
    show daisy f_sad_talk
    daisy "... No..."
    hide daisy
    hide diane
    show daisy b_naked_diane_comfort f_empty a_empty
    show diane b_empty a_empty f_shamed_talk_look
    with dissolve
    dia "There, there."
    dia "Shhh."
    show diane f_shamed_talk_look_closed
    show daisy b_naked_diane_comfort2
    daisy "{b}*Sniff*{/b} What are we gonna do?"
    show daisy b_naked_diane_comfort
    show diane f_shamed_talk_look
    dia "Well, why don't we add them to the compost pile out back?"
    dia "That way, they can help us make new flowers one day."
    show daisy b_naked_diane_comfort2
    show diane f_shamed_talk_look_closed
    daisy "R-really?"
    show daisy b_naked_diane_comfort
    dia "Mmhmm."
    show diane f_shamed_talk_look
    dia "C'mon, sweetie. I'll show you."
    show diane f_shamed_talk_look_closed
    show daisy b_naked_diane_comfort2
    daisy "{b}*Sniff*{/b} O-okay."
    hide daisy
    show diane f_shamed b_shirtless a_shirtless_sides at fliplright
    with dissolve
    pause
    hide diane
    show diane b_shirtless a_shirtless_sides f_normal_talk at Position (xpos=600)
    with dissolve
    dia "{b}[firstname]{/b}?"
    show diane f_normal
    show player 13
    player_name "Hmm?"
    show diane f_normal_talk
    dia "Why don't you run over to {b}the Mall{/b} and get her some new flowers?"
    show diane f_normal
    show player 10
    player_name "Right now?"
    show player 5
    show diane f_normal_talk
    dia "Yeah, it'll be a nice surprise for her."
    show diane f_normal
    show player 14
    player_name "Yeah, okay."
    show player 13
    show diane f_normal_talk
    dia "Try to get her something big and colorful."
    show diane f_laugh
    dia "{b}Sunflowers{/b} would be perfect!"
    show diane f_normal
    show player 14
    player_name "Okay, I'll look for {b}Sunflowers{/b}."
    show player 13
    daisy "{b}Diane{/b}?!"
    show diane f_normal_talk at fliplright with dissolve
    dia "Coming, sweetie!"
    hide diane
    show diane b_shirtless a_shirtless_sides f_normal_talk at Position (xpos=600)
    with dissolve
    dia "Thanks, {b}[firstname]{/b}."
    hide diane with dissolve
    pause
    show player 4 with dissolve
    player_name "( Hmm, I think that new store {b}Cupid{/b} at {b}the Mall{/b} sells flowers. )"
    player_name "( {b}I should start there{/b}. )"
    hide player with dissolve
    return

label barn_front_daisy_pizza_craving:
    scene expression player.location.background_blur with None
    show player 684 with dissolve
    player_name "( Ugh, it's so freaking hot out today! )"
    pause
    show player 24 with dissolve
    player_name "{b}*Sigh*{/b} I should take a break for awhile..."
    show player 11
    daisy "{b}Diane{/b}!"
    daisy "That tickles!!!"
    show player 30
    player_name "Hmm?"
    show player 5
    dia "Well, we want to make sure we got it all, don't we?"
    daisy "Yes..."
    show player 10
    player_name "What are they up to in there?"
    hide player with dissolve
    pause
    $ player.go_to(L_diane_barn_interior)
    scene expression player.location.background_blur with None

    show daisy b_diane_milking a_empty f_laugh with dissolve
    daisy "Hehehe!"
    dia "Heh, you have to stop squirming, sweetie."
    daisy "I can't help it!"
    show player 10 at left with dissolve
    player_name "What's going on in-"
    show player 11
    pause
    show player 29 with dissolve
    player_name "Whoa."
    show player 3
    show daisy f_normal_talk
    daisy "H-hi, {b}[firstname]{/b}."
    show daisy f_normal b_naked a_naked_sides at Position (xpos=300)
    show diane b_naked a_naked_sides f_normal_talk at Position (xpos=600)
    with dissolve
    dia "Hey, {b}[firstname]{/b}."
    dia "I'm just milking our new friend here."
    show diane f_normal
    show player 14 with dissolve
    player_name "Y-yeah, I can see that."
    player_name "Sorry, I'll leave you two alone."
    show player 13
    show diane f_laugh
    dia "Oh, nonsense!"
    show diane f_normal_talk
    dia "It's nothing you haven't seen before."
    show diane f_smirk_talk_fardown
    show daisy f_shy_back
    dia "You don't mind if {b}[firstname]{/b} stays, do you sweetie?"
    show diane f_smirk_fardown
    show daisy f_shy_talk_back
    daisy "No, it's okay."
    show daisy f_shy_talk
    daisy "{b}[firstname]{/b} is nice, right?"
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "Heh, yes. {b}[firstname]{/b} is very nice."
    show diane f_smirk
    show daisy f_normal
    show player 14
    player_name "How long has this been going on?"
    show player 13
    show diane f_smirk_talk
    dia "Mmm, just a couple of days."
    dia "The poor thing started acting strange and I couldn't figure out what the problem was."
    dia "It turns out her \"boobies\" were hurting."
    show diane f_cheese
    pause
    show diane f_laugh
    dia "Haha, her words, not mine."
    show diane f_smirk_fardown
    show daisy f_sad_talk
    daisy "Well, Master used to milk me everyday..."
    daisy "... But he's not around to do it anymore."
    show daisy f_sad
    show diane f_smirk_talk_fardown
    dia "Thank goodness for that."
    dia "You're much better off without that creepy old man!"
    show diane f_smirk_fardown
    pause
    show daisy f_normal_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    daisy "... Yeah."
    daisy "I like when {b}Diane{/b} does it better."
    show daisy f_normal
    show diane f_laugh
    dia "Heh."
    show diane f_smirk_talk_fardown
    dia "Well, if you think I'm good at it, you should see {b}[firstname]{/b}!"
    show diane f_smirk_fardown
    show daisy f_shy_talk
    daisy "Really?!"
    show daisy f_shy
    dia "Mmmhmm."
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=300)
    with dissolve
    daisy "{b}Diane{/b} says that you milk her sometimes too?"
    show daisy f_shy
    show diane f_smirk
    show player 14b
    player_name "Y-yeah, sometimes..."
    show player 1b
    show daisy f_normal_talk
    daisy "I've never met anyone else that needs to be milked like me."
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Perhaps {b}[firstname]{/b} can tell you more about what we do here and take your mind off all the tickling, huh?"
    hide diane
    hide daisy
    show daisy b_diane_milking a_empty f_normal_talk
    with dissolve
    daisy "Y-yeah, okay."
    show daisy f_normal
    show player 10
    player_name "Uhh, sure..."
    show player 14
    player_name "{b}*Ahem*{/b} You see, {b}Diane{/b} sells her milk to people who need it."
    show player 1
    show daisy f_shy_talk
    daisy "People need it?"
    show daisy f_shy
    show player 14
    player_name "Yeah."
    player_name "Some of her customers drink it and others cook with it."
    player_name "Heh, I even heard some of my friends say they are mixing it into their protein shakes..."
    show player 1
    show daisy f_laugh
    daisy "Wowzers, {b}Diane{/b} must have yummy milk!"
    show daisy f_normal
    show player 14
    player_name "Yeah, it's really tasty!"
    show player 1
    show daisy f_shy_back
    daisy "{b}Diane{/b}, you should sell my milk too!"
    show daisy b_naked a_naked_sides f_normal_talk at flip
    show daisy at Position (xpos=750)
    show diane b_naked a_naked_sides f_smirk_fardown at Position (xpos=600)
    with dissolve
    daisy "Master says it's the best in the whole world!"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "You'd be okay with me selling some?"
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "Of course!"
    daisy "I wanna help people too!"
    show daisy f_normal
    show diane f_laugh
    dia "Haha, you're such a good girl, {b}Daisy{/b}."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "Uh huh!"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "I think we're about done for today..."
    dia "Feeling better?"
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "Yes, much better."
    daisy "Thank you, {b}Diane{/b}!"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "No problem, sweetie."
    show diane f_smirk_fardown
    pause
    show diane f_smirk_talk_fardown
    dia "We should probably get some food in you now, don't you think?"
    show diane f_smirk_fardown
    show daisy f_laugh
    daisy "{b}*Gasp*{/b} Oats?!"
    show daisy f_normal
    show diane f_laugh
    dia "Heh, oats again?"
    show diane f_smirk_talk_fardown
    dia "{b}*Sigh*{/b} Don't you get tired of eating oats all the time?"
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "Nope!"
    daisy "Master always feeds me oats, they're yummy!"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Okay, but your old master doesn't control what you eat anymore..."
    dia "Wouldn't you rather try something else?"
    show diane f_smirk_fardown
    show daisy f_normal_smelling
    daisy "Mmm"
    show daisy f_normal_talk
    daisy "I dunno..."
    daisy "What's better than oats?"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Hehe, lots of things!"
    dia "You could try some more things out of my garden?"
    show diane f_smirk_fardown
    show daisy f_normal_smelling
    daisy "Hmm..."
    show daisy f_normal_talk at unflip
    show daisy at Position (xpos=300)
    with dissolve
    daisy "What do you like to eat, {b}[firstname]{/b}?"
    show daisy f_normal
    show diane f_normal
    show player 10b
    player_name "Me?"
    show player 17
    player_name "Cheese burgers!"
    show player 1b
    show diane f_sad_talk
    dia "{b}[firstname]{/b}, are you crazy?!"
    show player 5
    dia "We cannot feed her a cheese burger!!"
    show diane f_sad
    show player 10
    player_name "Hmm, why not?"
    show player 5
    pause
    show player 11
    pause
    show player 29 with dissolve
    player_name "Oh, right..."
    show diane f_smirk
    player_name "... Because that's beef and she's-"
    show player 3
    pause
    show player 14b
    player_name "Sorry."
    show player 1b
    show daisy f_normal_talk
    daisy "What's a cheese burger?"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Nevermind that, dear."
    show diane f_normal
    show player 14b
    player_name "Pizza then!"
    show player 1b
    show daisy f_shy_talk
    daisy "Pizza?"
    show daisy f_shy
    pause
    show daisy f_laugh
    daisy "Hehe, that's a funny word!"
    show daisy f_normal
    show diane f_thinking
    dia "That could work, I guess..."
    show diane f_normal_talk
    show player 13
    dia "You wanna run over to {b}Tony's Pizzeria{/b} and grab a pizza for her to try?"
    show diane f_normal
    show player 14
    player_name "Yeah, I can do that."
    show player 13
    show daisy f_normal_talk
    daisy "Pizza!"
    show daisy f_laugh
    daisy "Hehehe!"
    show daisy f_normal
    show diane f_normal_talk
    dia "Just remember she's a herbavore, okay?"
    dia "I don't know if she'd be able to handle meat."
    show diane f_normal
    show player 14
    player_name "Got it!"
    player_name "{b}One veggie pizza, coming up{/b}!"
    hide player with dissolve
    show daisy f_normal_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    show diane f_smirk_fardown
    daisy "PIZZA!!!"
    show daisy f_normal
    show diane f_laugh
    dia "Hehe!"
    hide diane
    hide daisy
    with dissolve
    return

label barn_front_daisy_picking_flowers:
    scene expression player.location.background_blur with None
    show player 14 at left
    $ M_diane.outfit = "shirtless"
    show diane b_naked a_naked_sides
    with dissolve
    player_name "Hey {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Hey there, stud."
    dia "How are you today?"
    show diane f_normal
    show player 14
    player_name "I'm alright."
    player_name "What are you doing out here in the garden?"
    player_name "Shouldn't you be inside with our new friend?"
    show player 13
    show diane f_normal_talk
    dia "Actually, it was her idea."
    show diane f_normal
    show player 5
    player_name "Hmm?"
    show diane f_normal_talk
    dia "See for yourself."
    show diane f_normal
    show player 5f with dissolve
    pause
    scene expression "backgrounds/location_diane_garden_cutscene11.jpg" with fade
    player_name "Wow, look at her..."
    player_name "... She's smiling!"
    dia "I know, isn't it adorable?!"
    dia "You should have seen how timid she was when she asked to leave the barn."
    dia "It about broke my heart."
    player_name "I can imagine."
    player_name "Why is she naked?"
    dia "Well, I gave her some clothes but she said she didn't like wearing them."
    dia "I didn't wanna force her."
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_naked a_naked_sides at Position (xpos=600)
    with dissolve
    player_name "So..."
    player_name "What are you gonna do with her?"
    show player 5
    dia "Hmm?"
    show player 10
    player_name "I mean, shouldn't we call somebody or something?"
    show player 5
    show diane f_normal_talk
    dia "Heh, who in the world would we call for something like this?"
    show diane f_normal
    show player 10
    player_name "I dunno? Animal control?"
    show player 5
    show diane f_normal_talk
    dia "No, we'll let her decide what she wants to do."
    dia "For now, it's probably best if she stays here in the barn."
    dia "Who knows what would happen if anybody saw her."
    show diane f_normal
    show player 10
    player_name "Y-yeah, I guess that makes sense."
    show player 5
    cow "{b}Diane{/b}!"
    cow "{b}Diane{/b} did you see all the flowers?!"
    show daisy a_naked_bouquet f_down_talk at Position (xpos=300) with dissolve
    show player 1b
    cow "They're so pret-"
    show daisy f_scared
    pause
    show daisy f_sad_talk
    show player 5b
    cow "Eep!"
    show daisy f_sad
    show diane f_shamed_talk_smile
    dia "Shh, it's alright sweetie."
    dia "Remember, what we talked about?"
    dia "This is {b}[firstname]{/b} and he's a nice man."
    dia "He won't hurt you."
    show diane f_shamed
    cow "..."
    show daisy f_shy_back
    show diane f_shamed_talk_smile
    dia "You're not going to hurt her right, {b}[firstname]{/b}?"
    show diane f_shamed
    show player 29 with dissolve
    show daisy f_sad
    player_name "Not at all."
    show player 4
    cow "..."
    show player 14b with dissolve
    player_name "I like your flowers."
    show player 1b
    show daisy f_sad_talk
    cow "Y-you do?"
    show daisy f_sad
    show diane f_normal
    show player 14b
    player_name "Yes, they're very pretty."
    show player 1b
    pause
    show daisy f_sad_talk
    cow "{b}Diane{/b} says you're the one who woke me up."
    show daisy f_sad
    show player 14b
    player_name "Oh, umm... Yeah, I suppose I was."
    show player 1b
    show daisy f_sad_talk_closed
    cow "T-thank you, for that."
    show daisy f_shy
    show player 17
    player_name "Heh, you don't have to thank me."
    show player 14b
    player_name "I'm just happy you're here now."
    show player 1b
    show daisy f_shy_talk
    cow "Me too."
    show daisy f_normal_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    cow "C-can I keep these, {b}Diane{/b}?"
    show daisy f_normal
    show diane f_normal_talk
    show player 13
    dia "You wanna keep the flowers?"
    show diane f_normal
    show daisy f_shy_talk
    cow "If that's okay?"
    show daisy f_shy
    show diane f_laugh
    dia "Heh, well of course it's okay sweetie!"
    show diane f_normal_talk
    dia "Let's go and put them in some water so they have something to drink, okay?"
    show diane f_normal
    show daisy f_laugh
    cow "Y-yeah, okay!"
    show daisy f_normal
    show diane f_normal_talk
    dia "Follow me, both of you."
    hide diane with dissolve
    show player 1b
    pause
    show daisy f_shy at unflip
    show daisy at Position (xpos=300)
    with dissolve
    show player 18
    pause
    show daisy f_sad_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    cow "W-wait for me!"
    hide daisy with dissolve
    show player 11
    pause
    show player 5
    player_name "( Well, at least she isn't recoiling in fear anymore. )"
    player_name "( That's a step in the right direction. )"
    $ player.go_to(L_diane_barn_interior)
    scene expression player.location.background_blur with None
    show player 1 at left
    show diane b_naked a_naked_sides f_smirk_fardown at Position (xpos=600)
    show daisy a_naked_bouquet f_shy_talk at flip
    show daisy at Position (xpos=250)
    with dissolve
    cow "S-so they drink the water?"
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "Mmhmm, they need water to produce food for themselves."
    show diane f_smirk_fardown
    show daisy f_shy_talk
    cow "... But where is the mouth on a flower?"
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "Hehe, no dear."
    dia "They drink water using their roots."
    dia "It flows right up the stem and into the petals."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    cow "Really?!"
    show daisy f_normal
    show diane f_smirk_talk_fardown a_shirtless_vase1 with dissolve
    dia "Lemme show you."
    show diane f_smirk_fardown
    pause
    show daisy a_naked_sides
    show diane f_laugh a_shirtless_vase2
    with dissolve
    dia "Just like that, see?"
    show diane f_smirk_talk_fardown a_shirtless_sides
    show daisy a_naked_vase
    with dissolve
    dia "Now, you check in on them throughout the day and you'll see the water level goes down as they drink."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    cow "O-okay, {b}Diane{/b}."
    show daisy f_normal
    show diane f_smirk
    show player 14b
    player_name "You gotta make sure they get sunlight too."
    show player 1b
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=-200)
    with dissolve
    cow "Sunlight?"
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "He's right."
    show daisy at flip
    show daisy at Position (xpos=250)
    with dissolve
    dia "Flowers need sunlight too, otherwise they'll wilt and die."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    cow "O-okay."
    cow "Will you show me how to catch sunlight?"
    show daisy f_normal
    show player 17
    player_name "Haha!"
    show player 1b
    show diane f_laugh
    show daisy f_sad
    dia "You don't catch it, sweetie."
    show diane f_smirk_talk_fardown
    dia "All you need to do is place them in a spot where they can see the sun for a few hours a day."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    cow "Oh, I can do that!"
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=-200)
    with dissolve
    cow "T-thanks, {b}[firstname]{/b}!"
    show daisy f_shy
    show diane f_smirk
    show player 14b
    player_name "You're welcome, eh..."
    player_name "What do I call you?"
    show player 1b
    cow "Hmm?"
    show player 14b
    player_name "Do you have a name?"
    show player 1b
    show daisy f_sad_talk_closed
    cow "Umm..."
    show daisy f_shy_talk
    cow "{b}Diane{/b} calls me sweetie?"
    show daisy f_shy
    show diane f_normal_talk
    dia "Hehe, that's more of a term of endearment then a real name, dear."
    show diane f_normal
    show daisy f_shy_talk
    cow "Oh, I umm..."
    show daisy f_shy
    show player 10b
    player_name "Didn't your... Uhh, master, give you a name?"
    show player 433
    show daisy f_shy_talk
    cow "He called me little pet..."
    cow "... Or sometimes..."
    show daisy f_sad_talk_closed
    cow "N-naughty girl."
    show daisy f_sad
    show diane f_laugh
    dia "Well, those won't do!"
    show diane f_normal
    show player 10b
    player_name "Definitely not."
    show player 5b
    show daisy f_shy
    pause
    show player 14b
    player_name "You should pick your own name."
    show player 1b
    show daisy f_shy_talk
    cow "I can pick it?"
    show daisy f_shy
    show diane f_normal_talk
    dia "That's a great idea, {b}[firstname]{/b}!"
    show diane f_normal
    show daisy f_shy_talk
    cow "B-but, I don't know any names..."
    show daisy f_shy
    show player 14b
    player_name "That's alright, we'll help you!"
    show player 1b
    show daisy f_shy_talk
    cow "O-okay."
    show daisy f_shy
    show diane f_normal_talk
    dia "Dorothy!"
    show diane f_normal
    show daisy f_scared
    cow "Mmm..."
    show player 10
    player_name "Bessie?"
    show player 5
    show diane f_shamed_talk_smile
    show daisy f_shy_back
    dia "Eww, no."
    show diane f_normal_talk
    dia "How about Molly?"
    show diane f_normal
    show daisy f_shy
    cow "Mmm..."
    show player 17
    player_name "Clarabelle!"
    show player 13
    show daisy f_down
    show diane f_laugh
    dia "Hah, why do you keep saying cow names?"
    show diane f_normal
    show player 14
    player_name "Umm, because she's a {b}cow girl{/b}?"
    show player 13
    show diane f_smirk_talk
    dia "Yeah, but she's definitely more girl than cow!"
    show diane f_smirk
    show player 14
    player_name "C'mon, it's not like I'm trying to name her Buttercup or something..."
    show player 1b
    show daisy f_down_talk
    cow "What is this called?"
    show daisy f_down
    show diane f_normal
    dia "Hmm?"
    show daisy f_shy_talk a_naked_flower with dissolve
    cow "The flower, what is it called?"
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "That flower is called {b}Daisy{/b}."
    show diane f_smirk_fardown
    show daisy f_down_talk
    cow "{b}Daisy{/b}..."
    show daisy f_laugh
    cow "I like that!"
    show daisy f_normal_talk
    cow "Can I be {b}Daisy{/b}?"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Hehe, of course sweetie."
    show diane f_smirk_fardown
    show player 17
    player_name "That's a beautiful name and it suits you!"
    show player 1b
    show daisy f_normal_talk
    cow "It does?"
    show daisy f_normal
    show diane f_normal_talk
    dia "I agree."
    show diane f_smirk_fardown
    show daisy f_laugh at flip
    show daisy at Position (xpos=250)
    with dissolve
    cow "O-okay!"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "So it's decided then."
    dia "Your name is {b}Daisy{/b}."
    show diane f_smirk_fardown
    show daisy f_laugh at unflip
    show daisy at Position (xpos=-200)
    with dissolve
    daisy "My name is {b}Daisy{/b}."
    show daisy f_normal
    show player 14b
    player_name "Nice to meet you, {b}Daisy{/b}!"
    show player 1b
    show daisy f_laugh
    daisy "Hehe!"
    show daisy f_normal_talk a_naked_sides with dissolve
    daisy "Nice to meet you, {b}[firstname]{/b}!"
    show daisy f_normal
    show diane f_normal_talk
    dia "Aww, my heart could just melt right now."
    show diane f_smirk_fardown
    show daisy f_sad_talk at flip
    show daisy at Position (xpos=250)
    with dissolve
    daisy "{b}*Gasp*{/b} They can do that?!"
    show daisy f_sad
    show player 17
    player_name "Pfft, hahaha!"
    show player 1b
    show diane f_smirk_talk_fardown
    dia "Heh, no sweetie."
    show daisy f_normal
    dia "That's just an expression."
    dia "It means I'm really happy."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "Oh."
    show daisy f_laugh a_naked_up with dissolve
    daisy "Then, my heart could melt too!"
    show daisy f_normal a_naked_sides with dissolve
    show player 17
    show diane f_laugh
    dia "Hahaha!"
    player_name "Hahaha!"
    show player 1b
    pause
    show diane f_smirk_talk_fardown
    dia "Alright, well..."
    show diane f_smirk_talk
    dia "{b}[firstname]{/b} and I should really get some work done before we run out of daylight."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "Oh."
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "You just take care of your flowers for now and let us know if you need anything, okay?"
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "Y-yeah."
    show daisy f_normal
    show diane f_normal_talk
    dia "Alright, c'mon {b}[firstname]{/b}."
    hide diane with dissolve
    show player 14b
    player_name "Goodbye, {b}Daisy{/b}."
    show player 1b
    show daisy f_laugh at unflip
    show daisy at Position (xpos=-200)
    with dissolve
    daisy "Bye!"
    hide player
    hide daisy
    with dissolve
    return

label barn_daisy_awakened_statue:
    scene expression player.location.background_blur with None
    $ M_diane.outfit = "shirtless"
    show diane b_naked f_shamed_talk_fardown a_shirtless_blanket at Position (xpos=600)
    show daisy b_naked_shy a_naked_shy_front f_shy_sad at flip
    show daisy at Position (xpos=200,yoffset=10)
    with dissolve
    dia "Here you go, sweetie."
    hide diane
    hide daisy
    show daisy b_naked_blanket_cover1 a_empty f_blanket_shy_back zorder 0 at Position (yoffset=10)
    show diane f_down_front b_empty a_empty zorder 1
    with dissolve
    pause
    show daisy b_naked_blanket_cover2 f_blanket_shy_talk_back at Position (yoffset=10)
    cow "Uhh, t-thank you."
    show daisy b_naked_shy a_naked_shy_blanket f_shy_sad zorder 2 at flip
    show daisy at Position (xpos=700,yoffset=10)
    show diane b_naked a_naked_sides f_shamed_talk_fardown at Position (xpos=600)
    with dissolve
    dia "You're welcome."
    show diane f_shamed_fardown
    show player 5 at left with dissolve
    pause
    show diane f_shamed_talk_fardown
    dia "Now tell me about how you ended up in my garden, dear."
    show diane f_shamed_fardown
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    cow "I-"
    cow "I'm not sure."
    cow "Master was worried about something and said I had to go back to sleep."
    show daisy f_shy_sad at Position (yoffset=10)
    pause
    show daisy f_shy_sad_talk at Position (yoffset=10)
    cow "I begged him not to!"
    cow "I hate it when he makes me sleep."
    show daisy f_shy_sad at Position (yoffset=10)
    show diane f_shamed_talk_fardown
    dia "I'm not sure I understand..."
    show diane f_shamed
    show player 10
    player_name "He turned her into a statue."
    show player 5b
    show daisy b_jump_scared a_empty f_empty
    cow "EEEEP!" with hpunch
    show diane b_empty a_empty f_thinking_back zorder 1 at Position (xpos=414)
    show daisy b_naked_cower f_cower_sad a_empty at unflip
    show daisy zorder 0 at Position (xpos=600,yoffset=26)
    with dissolve
    pause
    show diane f_shamed_talk
    dia "What?"
    show diane f_shamed
    show player 10
    player_name "{b}Jebadiah Delmont{/b} was supposedly some kind of hillbilly wizard."
    player_name "I think he must have been keeping her a secret by turning her into a statue."
    player_name "That way nobody would see her."
    show player 5
    show diane f_smirk_talk
    dia "Hillbilly wizard?!"
    dia "That's silly!"
    show diane f_smirk
    show player 10
    player_name "I know, but-"
    show player 5
    show diane f_laugh
    dia "Hahaha, you can't be serious!"
    show diane f_smirk
    show player 12
    player_name "I didn't believe it either but... I mean..."
    show diane f_thinking
    show player 469 with dissolve
    player_name "How else do you explain her?"
    show player 5b with dissolve
    show daisy f_cower_sad_talk at Position (yoffset=26)
    cow "Please, I didn't mean to-!"
    show daisy b_naked_shy a_naked_shy_cover f_shy_sad at Position (yoffset=10)
    show diane b_naked a_naked_sides f_shamed_talk_fardown at flip
    show diane at Position (xpos=750)
    with dissolve
    show player 5
    dia "Aww, sweetie..."
    dia "Nobody is gonna hurt you, okay?"
    dia "{b}[firstname]{/b} here is the nicest guy you'll ever meet."
    show diane f_shamed_fardown
    pause
    show diane f_shamed_talk_smile at unflip
    show diane at Position (xpos=300)
    with dissolve
    dia "I think she's a little frightened of you, {b}[firstname]{/b}..."
    show diane f_shamed
    pause
    show diane f_shamed_talk_smile
    dia "Why don't you head on home for the day and give me some time to calm her down, okay?"
    show diane f_shamed
    show player 10
    player_name "Uhh, yeah. Okay."
    player_name "If you're sure you'll be alright?"
    show player 5
    show diane f_shamed_talk_smile
    dia "Oh, I'll be fine."
    dia "Go on, {b}we can talk about this later{/b}, okay?"
    show diane f_shamed
    hide player with dissolve
    return

label barn_player_completed_mysterious_statue:
    scene expression player.location.background_blur with None
    show diane b_naked a_naked_sides f_normal_talk
    show player 13 at left
    with dissolve
    dia "Hey, {b}[firstname]{/b}."
    dia "Ready to get to work?"
    show diane f_normal
    show player 14
    player_name "Actually, I wanted to show you something."
    show player 13
    show diane f_normal_talk
    dia "Oh?"
    show diane f_normal
    show player 14
    player_name "You remember that broken statue {b}Richard{/b} found buried under your house?"
    show player 13
    show diane f_normal_talk
    dia "Yeah, with those creepy legs, right?"
    show diane f_normal
    show player 17
    player_name "Heh, yeah..."
    show player 14
    player_name "Well, I think I found all the pieces."
    show player 13
    show diane f_normal_talk
    dia "Really?"
    show diane f_normal
    show player 14
    player_name "Check it out."
    show player 239_240 with dissolve
    pause
    show player 717 with dissolve
    show diane f_smirk_talk_fardown
    dia "Oh, wow!"
    dia "It's a woman!"
    show diane f_smirk_fardown
    show player 717b
    player_name "Yeah, with really weird legs..."
    player_name "... And horns."
    show player 717
    show diane f_smirk_talk_fardown
    dia "Aww, look at her cute little ears!"
    dia "She reminds me of those silly goat men in the old myths!"
    dia "You know, the ones with the pan flutes?"
    show diane f_smirk_fardown
    show player 717b
    player_name "Satyrs."
    show player 717
    show diane f_laugh
    dia "Is that what they were called?"
    show diane f_normal
    player_name "Mmhmmm."
    show diane f_normal_talk
    dia "She's so cool!"
    show diane f_smirk_fardown
    pause
    show diane f_smirk_talk_fardown
    dia "I wonder why she's holding a bucket?"
    show diane f_smirk_fardown
    show player 717b
    player_name "I think it's a {b}milk pail{/b}."
    show player 717
    show diane f_normal_talk
    dia "What makes you think that?"
    show diane f_normal
    show player 717b
    player_name "I dunno, just a feeling, I guess..."
    show player 717
    show diane f_normal_talk
    dia "So, she's like a little milk maid?"
    show diane f_normal
    show player 717b
    player_name "Hehe, Yeah."
    player_name "A {b}cow girl{/b} milk maid."
    show player 717
    show diane f_laugh
    dia "Oh my gosh, I love it!"
    show diane f_normal
    show player 717b
    player_name "Hehe, I thought you might."
    show player 717c
    pause
    show player 717b
    player_name "Why don't you keep it?"
    show player 717
    show diane f_smirk_talk_fardown
    dia "Really?"
    show diane f_smirk_fardown
    show player 717b
    player_name "Yeah."
    player_name "I don't have anywhere to put it at my house."
    show player 717
    show diane f_thinking
    dia "Hmm."
    show diane f_normal_talk
    dia "It would look great in my garden, don't you think?"
    show diane f_normal
    show player 717b
    player_name "Definitely!"
    show player 13
    show diane a_statue_full f_down_front
    with dissolve
    pause
    show diane f_reading_intrigued
    dia "I can't believe this thing turned out to be such a beautiful creature!"
    pause
    show diane f_laugh
    dia "Thanks, {b}[firstname]{/b}!"
    show diane f_normal
    show player 14
    player_name "No problem!"
    show player 13
    show diane f_normal_talk
    dia "I'm gonna go and find a place for it {b}out in the garden{/b}, right now!"
    hide diane with dissolve
    pause
    show player 18
    player_name "( Well, that certainly made {b}Diane{/b} happy. )"
    show player 4 with dissolve
    player_name "( I wonder if Clyde's grandfather made it? )"
    player_name "( ... And why? )"
    pause
    show player 34 with dissolve
    player_name "( Hmm, maybe {b}I should take a closer look at that statue{/b} sometime... )"
    hide player with dissolve
    return

label barn_diane_pregnancy_anouncement:
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 13 at left
    show diane b_naked a_naked_sides f_laugh
    with dissolve
    dia "{b}[firstname]{/b}!!"
    show player 10
    show diane f_cheese
    player_name "What's the big emergency?!"
    show player 5
    show diane f_laugh
    dia "We did it!"
    dia "I'm pregnant!"
    show diane f_cheese
    show player 14
    player_name "You are?!"
    player_name "Are you sure?!"
    show player 13
    show diane f_laugh
    dia "I'm positive!"
    dia "You're gonna be a daddy!"
    show diane f_cheese
    show player 14
    player_name "I'm gonna-"
    show player 18
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "You alright?"
    show diane f_normal
    show player 14
    player_name "Hmm?"
    player_name "Y-yeah!"
    player_name "This is great news, {b}Diane{/b}!"
    player_name "I'm so happy!"
    hide player
    show diane kiss_naked
    with dissolve
    pause
    show player 13 at left
    show diane b_naked a_naked_sides f_laugh
    with dissolve
    dia "Mmm, me too!"
    dia "Oh, this is so exciting!"
    show diane f_normal_talk
    dia "I never thought I would have this opportunity!"
    show diane f_normal
    pause
    show diane f_laugh
    dia "Oh, thank you {b}[firstname]{/b}!"
    dia "Thank you, thank you, thank you!!!"
    hide player
    show diane kiss_naked
    with dissolve
    pause
    show player 14 at left
    show diane b_naked a_naked_sides f_cheese
    with dissolve
    player_name "Heh, you're welcome..."
    show player 13
    show diane f_normal
    pause
    show player 14
    player_name "So what should I..."
    player_name "{b}*Ahem*{/b} Is there anything I can do for you?"
    show player 13




    show diane f_normal_talk
    dia "Hmm?"
    dia "Oh, no!"
    dia "Just keep doing everything you've been doing."
    dia "Keep being wonderful, {b}[firstname]{/b}!"
    show diane f_normal
    show player 14
    player_name "That, I can definitely do!"
    show player 13
    show diane f_laugh
    dia "Hehe!"
    hide player
    hide diane
    with dissolve
    return

label barn_diane_return_outfit_package:
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 14 at left
    show diane b_shirtless a_shirtless_sides
    with dissolve
    player_name "Hey {b}Diane{/b}, I'm back!"
    show player 13
    show diane f_normal_talk
    dia "There you are."
    dia "I was starting to worry you'd gotten lost!"
    show diane f_normal
    show player 14
    player_name "Heh, yeah... I ran into {b}Veronica{/b} again..."
    show player 13
    show diane f_laugh
    dia "Again?!"
    show diane f_normal_talk
    dia "Is that girl stalking you or something?"
    show diane f_normal
    show player 10
    player_name "N-no, I don't think so."
    player_name "She was at {b}Pink{/b}..."
    show player 13
    show diane f_smirk_talk
    dia "Oh, was she shopping for something naughty?"
    show diane f_smirk
    show player 14
    player_name "Eh, she was in the back room, actually."
    player_name "Blowing off steam, she said."
    show player 13
    show diane f_shamed_talk_smile
    dia "Oh, goodness..."
    dia "The poor dear must really be stressed out."
    show diane f_shamed
    show player 14
    player_name "Yeah, I think she is."
    player_name "She wants you to call her."
    show player 13
    show diane f_normal_talk
    dia "Yeah, I'll have to do that."
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "Umm, did you get the package I ordered?"
    show diane f_normal
    show player 17
    player_name "I did!"
    show player 239_240 with dissolve
    pause
    show player 170 with dissolve
    player_name "What's in it?"
    show player 13
    show diane f_laugh a_shirtless_box
    with dissolve
    dia "Hehe, you'll find out..."
    show diane f_smirk_talk
    dia "This is so exciting!"
    show diane f_smirk
    show player 29 with dissolve
    player_name "A-are we really gonna have sex, {b}Diane{/b}?"
    show player 3
    show diane f_smirk_talk
    dia "Oh, you better believe it!"
    dia "I just need to get everything ready."
    dia "Would you mind stepping outside for a moment?"
    show diane f_smirk
    show player 29
    player_name "O-okay, sure."
    hide player with dissolve
    scene expression "backgrounds/location_barn_garden_day_blur.jpg"
    show player 18 with dissolve
    player_name "( I can't believe this is really about to happen! )"
    player_name "( I'm gonna have sex with {b}Diane{/b}... )"
    show player 13
    dia "Okay, {b}[firstname]{/b}!"
    dia "I'm ready!"
    show player 14
    player_name "C-coming!"
    show player 33
    player_name "( Phew. Alright, {b}[firstname]{/b}! This is it! )"
    hide player with dissolve
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 10f with dissolve
    player_name "{b}D-diane{/b}?"
    show player 13f
    $ M_diane.is_naked = 0
    $ M_diane.outfit = "cow"
    show diane f_smirk_talk b_naked a_naked_sides
    dia "I'm here."
    show diane f_smirk
    show player 11 at left
    player_name "!!!" with hpunch
    show player 23
    player_name "..."
    show diane f_smirk_talk
    dia "Well, what do you think?"
    show player 428
    show diane a_naked_cow_check f_smirk_down with dissolve
    pause
    show player 426
    show diane a_naked_sides with dissolve
    show player 429
    player_name "Y-you look..."
    show player 29 with dissolve
    show diane f_cheese
    player_name "Wow!"
    show player 3
    show diane f_smirk_talk
    dia "Is it too much?"
    show diane f_smirk
    show player 12 with dissolve
    player_name "NO!"
    show player 26
    player_name "It's really, really sexy!"
    show player 426
    show diane f_smirk_talk
    dia "You think so?!"
    show diane f_smirk
    show player 26
    player_name "I do!"
    show player 426
    show diane f_smirk_talk
    dia "Oh, good!"
    dia "I was worried you'd think it's silly..."
    show diane f_smirk
    show player 29 with dissolve
    player_name "So how do you wanna-"
    hide player
    show diane kiss_naked at Position (xoffset=-172)
    with dissolve
    player_name "!!!"
    pause
    show diane b_pull_mc_naked f_empty a_empty with dissolve
    dia "Mmm, I can't wait another second!"
    dia "We'll use the milking station."
    dia "It's perfect!"
    pause 
    hide diane with dissolve
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed pre_talk
    show diane_sex_breed_mc
    with dissolve
    dia "Give it to me, stud!"
    dia "I want you to breed me like an animal!"
    player_name "O-okay..."
    hide diane_sex_breed_mc
    show diane_sex_breed insert_and_pullout
    with dissolve
    pause
    show diane_sex_breed creampie_pullout with dissolve
    pause 1
    show diane_sex_breed creampie
    dia "Oh my god!" with hpunch
    return

label barn_diane_outfit_package:
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 29 at left
    show diane b_shirtless a_shirtless_sides f_smirk
    with dissolve
    player_name "H-hey, {b}Diane{/b}."
    show player 3
    show diane f_smirk_talk
    dia "Hi, handsome."
    dia "You look anxious to get started!"
    show diane f_smirk
    show player 29
    player_name "Heh, y-yeah."
    show player 3
    show diane f_smirk_talk
    dia "Mmm, me too..."
    dia "... But there's one last thing I want you to do for me."
    show diane f_smirk
    show player 14 with dissolve
    player_name "A-anything!"
    show player 13
    show diane f_smirk_talk
    dia "I need you to go and pick up a special package at the mall for me."
    show diane f_smirk
    show player 14
    player_name "I can do that!"
    show player 14f with dissolve
    player_name "I'll be back before you-"
    show diane f_laugh
    show player 11 with dissolve
    dia "Hold on just a second!"
    show player 13
    show diane f_smirk_talk
    dia "I haven't even told you what store that package is in!"
    show diane f_smirk
    show player 14
    player_name "S-sorry."
    show player 13
    show diane f_laugh
    dia "Haha, it's alright."
    show diane f_smirk_talk
    dia "You'll need to look around {b}on the second floor{/b} for a store called, {b}\"Pink.\"{/b}"
    show diane f_smirk
    show player 17
    player_name "{b}\"Pink\"{/b}, got it!"
    show player 13
    show diane f_smirk_talk
    dia "Tell the lady at the front desk that you're there to collect a package under the name {b}Diane{/b}."
    show diane f_normal_talk
    dia "... And don't look inside!"
    show diane f_normal
    show player 14
    player_name "O-okay."
    show player 13
    show diane f_normal_talk
    dia "It's very important that you don't look inside the package, {b}[firstname]{/b}!"
    show diane f_smirk_talk
    dia "I don't want you to spoil the surprise."
    show diane f_smirk
    show player 14
    player_name "I promise, I won't look."
    show player 13
    show diane f_smirk_talk
    dia "Good boy."
    hide player
    show diane kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane b_shirtless a_shirtless_sides f_smirk_talk
    with dissolve
    dia "Hurry back to me, stud."
    show diane f_smirk
    show player 14
    player_name "Yes, ma'am!"
    hide player
    hide diane
    with dissolve
    return

label barn_diane_barn_checkup:
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 14 at left
    show diane b_casual a_casual_sides
    with dissolve
    player_name "Hey, {b}Diane{/b}!"
    player_name "I'm ready to-"
    show player 11
    pause
    show player 14
    player_name "Where's your overalls?"
    show player 13
    show diane f_normal_talk
    dia "Hey, {b}[firstname]{/b}."
    dia "I was just about to walk out the door."
    show diane f_normal
    show player 10
    player_name "Oh?"
    player_name "Where are you going?"
    show player 5
    show diane f_normal_talk
    dia "I made an appointment to see a doctor this morning."
    dia "If we're gonna... You know."
    show diane f_wink
    pause
    show diane f_normal_talk
    dia "I wanna get checked out and make sure everything's in tip top shape."
    show diane f_normal
    show player 14
    player_name "Ah, I see."
    player_name "Well, can I come with you?"
    show player 13
    show diane f_normal_talk
    dia "You wanna come with me to see the doctor?"
    show diane f_normal
    show player 17
    player_name "Sure!"
    show player 13
    show diane f_normal_talk
    dia "Alright."
    dia "I would definitely appreciate the company."
    show diane f_laugh
    dia "Doctors kinda freak me out."
    show diane f_normal
    show player 14
    player_name "Hehe, really?"
    show player 13
    show diane f_normal_talk
    dia "Yeah."
    dia "All that poking and prodding, you know?"
    show diane f_normal
    show player 14
    player_name "Hah, yeah. I know what you mean."
    show player 13
    show diane f_normal_talk
    dia "Well come on then, stud."
    dia "Let's get moving!"
    show diane f_normal
    show player 14
    player_name "Y-yes, ma'am!"
    hide player
    hide diane
    with dissolve
    return

label barn_diane_return_production_book:
    scene expression player.location.background_blur
    show diane b_shirtless a_shirtless_sides f_normal_talk
    show player 13 at left
    with dissolve
    dia "Finally, you're back!"
    dia "I was starting to think you got lost or something."
    show diane f_normal
    show player 14
    player_name "Yeah, sorry."
    player_name "I stopped off at the library."
    show player 13
    show diane f_normal_talk
    dia "Oh?"
    show diane f_normal
    show player 14
    player_name "Yeah, I ran into {b}Veronica{/b} at {b}Consum-R{/b} and we started talking."
    player_name "She says hi by the way."
    show player 13
    show diane f_laugh
    dia "Oh, I love her! She's such a sweetie!"
    show diane f_normal
    show player 14
    player_name "I asked her about increasing milk production."
    show player 11
    show diane f_sad_talk
    dia "WHAT?!" with hpunch
    show diane f_scared
    pause
    show diane f_sad_talk
    dia "You didn't tell her I'm milking myself did you?!"
    show diane f_sad
    show player 10
    player_name "N-no, of course not."
    show player 5
    show diane f_lookup
    dia "Phew! I was really worried there for a sec!"
    show diane f_normal
    show player 10
    player_name "There's no need to worry."
    player_name "She was asking how the business was going and she was very pushy..."
    player_name "She wants to work for you, you know?"
    show player 5
    show diane f_normal_talk
    dia "Yeah, I know."
    show diane f_normal
    show player 10
    player_name "She seems pretty knowledgeable."
    show player 5
    show diane f_normal_talk
    dia "She is!"
    dia "Her parents owned a huge dairy farm out west and she grew up working it."
    show diane f_normal
    show player 12
    player_name "So when I said you were looking to increase milk production, she assumed I meant cows."
    show player 13
    show diane f_normal_talk
    dia "Oh, good."
    dia "I'm not ready to tell her yet."
    show diane f_normal
    show player 14
    player_name "Anyways, she sent me down a path to find this."
    show player 239_240 with dissolve
    pause
    show player 369 with dissolve
    player_name "I hope it helps..."
    show player 13
    show diane a_shirtless_book_cover f_reading_intrigued
    with dissolve
    dia "Hmm, \"Breeder's Guide?\""
    show diane f_normal
    show player 14
    player_name "Yeah, it turns out, there's a fairly easy answer to your milk production problems..."
    show player 13
    show diane a_shirtless_book f_down_front with dissolve
    pause
    show diane f_surprised_down
    dia "!!!" with hpunch
    dia "I..."
    show diane f_reading_intrigued
    dia "This is-"
    dia "I mean... I can't-"
    show diane f_laugh
    dia "Hahaha!"
    show diane f_normal_talk
    dia "Could you imagine me pregnant?"
    show diane f_normal
    show player 14
    player_name "Sure, why not?"
    show player 13
    show diane f_thinking
    dia "..."
    show diane f_laugh
    dia "Nobody would want to have a baby with me!"
    show diane f_normal
    show player 14
    player_name "I don't know about that..."
    player_name "You're beautiful, and smart, and driven, and so much fun to be around!"
    player_name "I bet, there are tons of guys out there who would be thrilled to have a baby with you, {b}Diane{/b}."
    show player 13
    show diane f_shamed_talk_smile
    dia "... Yeah, right."
    show diane f_shamed
    show player 14
    player_name "I mean, I would."
    show player 13
    show diane f_laugh
    dia "Haha, now you're just being ridiculous..."
    show diane f_shamed
    show player 12
    player_name "Hmm?"
    show player 14
    player_name "I'm serious."
    show player 13
    show diane f_shamed_talk_smile
    dia "Look, I know we have a little fun sometimes but we can't do that!"
    show diane f_shamed
    show player 10
    player_name "Why not?"
    show player 5
    show diane f_shamed_talk_smile
    dia "It isn't right!"
    show diane f_shamed_talk_smile_back
    dia "... And what would {b}[deb_name]{/b} say?!"
    dia "She'd probably never talk to me again!"
    show diane f_shamed
    show player 14
    player_name "Oh, she wouldn't do that."
    player_name "You're like, her favorite person in the entire world, {b}Diane{/b}."
    show player 13
    show diane f_shamed_talk_smile
    dia "You really think it's a good idea for you and I to have a baby?!"
    show diane f_shamed
    show player 14
    player_name "Well, I dunno... Maybe?"
    show player 13
    show diane f_shamed_talk_smile_back
    dia "Tch, I don't think you've really thought this through..."
    show diane f_shamed
    show player 12
    player_name "I just want to help you, {b}Diane{/b}!"
    show player 5
    show diane f_shamed_talk_smile
    dia "Oh, stop it!"
    show diane f_shamed
    player_name "..."
    show diane f_shamed_talk_smile
    dia "I appreciate what you're saying {b}[firstname]{/b} but it's just out of the question, alright?"
    show diane f_shamed
    show player 24
    player_name "{b}*Sigh*{/b} If you say so..."
    show diane f_shamed_talk_smile
    dia "Now, why don't you go tend to the garden while I finish up in here."
    show diane f_shamed
    show player 25
    player_name "Alright."
    hide player with dissolve
    pause
    show diane f_down_front
    pause
    dia "( Oh my... )"
    dia "( Just imagine being bred like a animal! )"
    dia "( Mmm, it's so hot! )"
    show diane f_reading_blushing
    dia "( I can't believe {b}[firstname]{/b} really wants to do that with me! )"
    show diane f_reading_lip_bite
    dia "( ... Maybe... )"
    pause
    show diane a_shirtless_book_close f_explain_close with dissolve
    dia "( No! Stop it, {b}Diane{/b}! )"
    dia "( Get those naughty thoughts out of your head right now! )"
    show diane a_shirtless_book_throw with dissolve
    dia "( Even I'm not perverted enough to do something like that! )"
    show diane a_shirtless_sides with dissolve
    pause
    show diane f_smirk_talk
    dia "Phew, I need some air..."
    hide diane with dissolve
    return


label barn_building_inform_carpenter:
    scene expression player.location.background_blur with None
    show player 13 at left
    show diane b_casual a_casual_bag f_laugh at lright
    with dissolve
    dia "{b}[firstname]{/b}, there you are!"
    show diane f_normal_talk
    dia "I was just about to head to your house."
    show diane f_normal
    show player 14
    player_name "Wow, he's already started building!"
    show player 13
    show diane f_laugh
    dia "Yup!"
    dia "Isn't it exciting!"
    show diane f_cheese
    show player 14
    player_name "Yeah, it really is."
    player_name "Did he give you a time frame for when he expects to complete it?"
    show player 13
    show diane f_normal_talk
    dia "Hmm, not exactly but he'll call when it's ready."
    hide player
    show diane b_casual_bag_hug a_empty f_laugh at Position (xoffset=-414)
    with dissolve
    dia "C'mon, roomie."
    dia "We gotta get home before {b}Debbie{/b} starts worrying."
    show player 14 at left
    show diane b_casual a_casual_bag f_normal at lright
    with dissolve
    player_name "Heh, yes ma'am."
    hide player
    hide diane
    with dissolve
    return

label barn_diane_check_barn_out:
    scene expression L_diane_barn_interior.background_blur
    show diane b_shirtless a_shirtless_sides at flip
    show diane at Position (xpos=100)
    show richard f_normal_talk
    show player 13 at left
    with dissolve
    rich "Hey, you got here quick."
    show richard f_normal
    show player 17
    player_name "Heh, I could barely keep up with her."
    show player 13
    show diane f_laugh
    dia "I'm excited!"
    show diane f_cheese
    show richard f_confused_talk
    rich "Hah, I guess you're ready for the tour then?"
    show richard f_confused
    show diane f_normal_talk
    dia "Yes, please!"
    show diane f_normal
    show richard f_normal_talk
    rich "Alright then, follow me."
    hide richard
    hide diane
    hide player
    with dissolve
    scene expression L_diane_barn.background with fade
    rich "I did everything exactly to your specifications."
    rich "All the doors are thick and sturdy with custom built locking mechanisms, so you shouldn't have to worry about anyone breaking in."
    dia "Niiice!"
    scene expression L_diane_barn_garden.background with fade
    rich "I made sure to keep the grunts out of your garden so everything there should be more or less the way you left it."
    rich "... And the hay guys had some excess they didn't use, so I told them to stack it under the awning out back."
    dia "That's perfect!"
    scene expression L_diane_barn_interior.background with fade
    player_name "Whoa!"
    dia "Hehe!"
    rich "Again, everything was done to your specifications."
    rich "You've got plenty of extra storage space on the second floor and room to expand, should you ever decide to."
    dia "It's so beautiful!"
    player_name "What are those machines for?!"
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show diane b_shirtless a_shirtless_sides at flip
    show diane at Position (xpos=100)
    show richard f_confused_talk
    show player 13 at left
    with dissolve
    rich "Yeah, about those..."
    rich "A couple fellas showed up with them about three days ago, saying you ordered them."
    rich "All the paperwork checked out and they did all the installation."
    rich "I still don't have any idea what they do..."
    show richard f_confused
    show diane f_laugh
    dia "Hehe, those are, uhh... It's a secret of the trade!"
    show diane f_normal
    rich "Hmmph."
    show richard f_normal_talk
    rich "Fair enough."
    show richard f_normal
    pause
    show richard f_normal_talk
    rich "Welp, I think that about covers it."
    show richard f_normal
    show diane f_normal_talk
    dia "Thanks so much, {b}Richard{/b}."
    dia "This all looks even better than I imagined it."
    show diane f_normal
    show richard f_normal_talk
    rich "Well, I'd appreciate it if you could recommend me to anyone you know who's needing work done."
    show richard f_normal
    show diane f_normal_talk
    dia "I certainly will!"
    show diane f_normal
    show richard f_normal_talk
    rich "Alright, then I'll leave you to it."
    rich "Oh, wait!"
    rich "I nearly forgot."
    show richard f_normal
    dia "Hmm?"
    show richard f_normal_talk a_dressed_statue with dissolve
    show diane f_down_front
    show player 433
    rich "The hay delivery guys found this half buried in the corner the other day."
    show richard f_confused_talk
    rich "It's the damnedest thing..."
    show player 434
    rich "I dunno how I missed it when I was working on the foundation."
    show diane a_shirtless_statue
    show richard a_dressed_hips
    with dissolve
    rich "You know anything about it?"
    show richard f_normal
    show diane f_normal_talk
    dia "I've never seen it before..."
    dia "... Looks like some sort of statue or something."
    show diane f_normal
    show richard f_normal_talk
    rich "Yeah, that's what I was thinking."
    show richard f_normal
    show player 14
    player_name "Can I see it?"
    show diane f_down_front a_shirtless_sides at unflip
    show diane at Position (xpos=-300)
    show player 688
    with dissolve
    player_name "( Hmm, it looks like the lower half a nude woman. )"
    player_name "( What's with the tail though? )"
    show player 689
    player_name "( There's something written on the bottom of it. )"
    show expression "objects/closeup_statue_01.png"
    hide player
    hide diane
    hide richard
    with dissolve
    dia "What's that written on the bottom?"
    player_name "{b}\"Delmont.\"{/b}"
    player_name "Hmm, {b}Delmont{/b}..."
    player_name "It sounds familiar."
    hide expression "objects/closeup_statue_01.png"
    show diane b_shirtless a_shirtless_sides f_normal_talk at Position (xpos=200)
    show richard
    show player 689 at left
    with dissolve
    dia "Maybe it's a name?"
    show diane f_normal
    show richard f_confused_talk
    rich "... Or a surname?"
    show richard f_normal
    show player 12 with dissolve
    player_name "You mind if I hang on to it?"
    show player 5
    show diane f_normal_talk
    dia "Knock yourself out."
    show diane f_normal
    show player 13
    show richard f_normal_talk
    rich "Well..."
    show diane at flip
    show diane at Position (xpos=600)
    rich "Give me a call if you need anything else."
    show richard f_normal
    show diane f_normal_talk
    dia "Thanks again, {b}Richard{/b}."
    show diane f_normal
    hide richard with dissolve
    pause
    show diane f_normal_talk
    dia "Say hi to {b}Lucy{/b} for me!"
    show diane f_normal
    pause
    show diane f_laugh at unflip, lright with dissolve
    dia "Oh, this is wonderful!"
    show diane f_normal_talk
    dia "Isn't it wonderful, {b}[firstname]{/b}?!"
    show diane f_normal
    show player 14
    player_name "Heh, it does look really nice."
    player_name "So what are those machines for?!"
    show player 13
    show diane f_normal_talk
    dia "Oh, right."
    dia "Those are milking machines."
    show diane f_normal
    show player 10
    player_name "They are?"
    show player 13
    show diane f_normal_talk
    dia "You lay in them and attach the milkers to your breasts."
    dia "I had them custom built for comfort, since I have to spend so many hours milking."
    show diane f_normal
    show player 14
    player_name "I see."
    show player 13
    show diane f_smirk_talk
    dia "Gravity should make your job a lot easier with me in that position..."
    show diane f_smirk
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "My job?!"
    show player 11
    show diane f_laugh
    dia "Of course!"
    show diane f_smirk_talk
    dia "You're the one who keeps asking if you can help..."
    dia "... And with those magic hands of yours, I figured, who better?"
    show diane f_smirk
    show player 10
    player_name "So I'm going to be milking you?"
    show player 11
    show diane f_smirk_talk
    dia "Is that a problem?"
    show diane f_smirk
    show player 29 with dissolve
    player_name "N-no!"
    show player 3
    pause
    show player 10 with dissolve
    player_name "How come there are three of them though?"
    show player 5
    show diane f_laugh
    dia "Heh, well I'll have to expand and bring more ladies in eventually, right?"
    show diane f_normal
    show player 10
    player_name "M-more, ladies?"
    player_name "You mean, I'm gonna be milking more ladies?"
    show player 11
    show diane f_normal_talk
    dia "Maybe."
    show diane f_smirk_talk
    dia "That's between you and them."
    show diane f_smirk
    show player 29 with dissolve
    player_name "I uhh... Wha-"
    player_name "{b}*Ahem*{/b} W-who do you have in mind?"
    show player 3
    show diane f_laugh
    dia "Hahaha, calm down handsome."
    show diane f_normal_talk
    dia "I don't have anyone in mind right now..."
    dia "It could be a long while before I find the right fit for a job like that."
    show diane f_normal
    show player 14 with dissolve
    player_name "Heh, right. That makes sense."
    show player 13
    show diane f_normal_talk
    dia "In the meantime, I'll have to see about {b}finding a way to increase my production{/b}..."
    show diane f_normal
    show player 10
    player_name "What do you mean?"
    show player 5
    show diane f_normal_talk
    dia "Well, I'm nearing my limit on how much breast milk I can produce in a day."
    dia "There's gotta be something I can do to increase the flow..."
    show diane f_normal
    show player 10
    player_name "Increase the flow?"
    player_name "... Maybe you should speak with a doctor?"
    show player 5
    show diane f_normal_talk
    dia "Yeah, that might be a good idea."
    dia "Don't worry, {b}[firstname]{/b}, I'll figure something out."
    show diane f_normal
    show player 14
    player_name "N-no, I'll help too!"
    show player 13
    show diane f_laugh
    dia "Haha, there's something else I need you to do."
    show diane f_normal
    show player 14
    player_name "Anything!"
    show player 13
    show diane f_normal_talk
    dia "I don't think I ordered enough {b}storage containers for the milk{/b}."
    dia "Would you run over to {b}Consum-R{/b} and {b}buy me one more?{/b}"
    show diane f_normal
    show player 14
    player_name "Sure thing."
    show player 13
    show diane f_normal_talk
    dia "Thanks, {b}[firstname]{/b}."
    hide player
    hide diane
    with dissolve

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
