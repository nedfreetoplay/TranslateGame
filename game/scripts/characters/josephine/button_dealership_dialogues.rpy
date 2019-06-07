label josephine_button_dealership_dialogue_pre:
    scene expression player.location.background_closeup with None
    show joe 1 at Position(xpos=0.5474,ypos=0.7630)
    show xtra3 at right
    show player 24 at left
    with dissolve
    return

label josephine_button_dealership_dialogue_intro:
    player_name "Good morning."
    show player 109f
    pause
    pause
    show player 108f
    player_name "Hello?"
    show player 109f
    pause
    Josephine "{b}*Sigh*{/b}"
    pause
    show sato 2 behind xtra3 at Position(xpos=.7630,ypos=0.7299) with dissolve
    show player 11
    Mr. Sato "{b}Josephine{/b}!"
    show sato 1
    show joe 3 at Position(xpos=0.4976,ypos=1.0000) with fastdissolve
    Josephine "What?!"
    show joe 2
    show sato 2
    Mr. Sato "Did you file those TPS reports like I asked you?"
    show sato 1
    show joe 3
    Josephine "Ugh, no..."
    show player 5
    Josephine "You know I hate doing paperwork!"
    show joe 2
    show sato 2
    Mr. Sato "I didn't give you this job for you to sit around all day texting on your phone."
    show sato 1
    show joe 3
    Josephine "First of all."
    Josephine "I'm not texting."
    Josephine "I'm shopping for shoes."
    show joe 2
    show sato 2
    Mr. Sato "... {b}Josephine{/b}, this isn't a joke!"
    Mr. Sato "Don't you have any pride?"
    Mr. Sato "How can you sit there doing nothing with all the other employees working so hard?"
    show sato 1
    Josephine "..."
    show kim 2 behind xtra3 at Position (xpos=950) with dissolve
    kim "You rang, {b}Mr. Sato{/b}?"
    show kim 1
    show sato 2
    Mr. Sato "Hmm?"
    Mr. Sato "Oh, hello {b}Kim{/b}."
    show sato 1
    show joe 1 at Position(xpos=0.5474,ypos=0.7630) with dissolve
    show kim 2
    kim "I praced my ratest sales numbers on your desk."
    show kim 1
    show player 9 with dissolve
    show sato 2
    Mr. Sato "Ah, very good!"
    Mr. Sato "See there, {b}Josephine{/b}..."
    Mr. Sato "Why can't you act more like {b}Kim{/b} here?"
    show sato 1
    show joe 3 at Position(xpos=0.4976,ypos=1.0000) with dissolve
    Josephine "Psh, we can't all have our noses buried in your ass, {b}Dad{/b}."
    show joe 2
    show sato 2
    Mr. Sato "{b}Josephine{/b}!"
    show sato 1
    show kim 2
    kim "Would you rike me to fetch you coffee, {b}Mr. Sato{/b}?"
    show kim 1
    show sato 2
    Mr. Sato "Oh, that would be lovely, {b}Kim{/b}."
    Mr. Sato "Just bring it to my office, would you?"
    Mr. Sato "Get your act together, {b}Josephine{/b}!"
    show sato 1
    show kim 3
    show player 11
    show joe 2c
    with dissolve
    Josephine "... Do you think I could pull these shoes off?"
    show joe 2
    show sato 2
    Mr. Sato "Argh! Just, tend to your customer!"
    show sato 1
    player_name "..."
    hide sato with dissolve
    pause
    show kim 4f at right with dissolve
    pause
    show kim 5 with dissolve
    kim "Hue hue hue hue!"
    show joe 2b
    kim "Such a derusional fool!"
    show kim 4
    show joe 3
    Josephine "What's so funny, fat boi?"
    show joe 2b
    show kim 2 with dissolve
    kim "FAT BOY?!"
    kim "How dare you speak to me rike that!"
    show kim 1
    show player 9 with dissolve
    show joe 3
    Josephine "You are so fucking gross..."
    show joe 2
    show kim 2
    kim "Grr, Raugh while you can!"
    kim "You just made my shit rist!"
    show kim 6 with dissolve
    kim "Your day of reckoning is fast approaching!"
    kim "Soon I will usurp that incompetant father of yours..."
    kim "... And then you will crean my toirets with your tongue!"
    show kim 1 with dissolve
    show joe 5
    Josephine "{b}*Snort*{/b} Hahahaha!"
    show joe 3
    Josephine "Yeah, whatever bitch..."
    Josephine "Don't you have some coffee to fetch?"
    show joe 2b
    show kim 2
    kim "Grr..."
    hide kim with dissolve
    player_name "..."
    show joe 7 at Position (yoffset=-20) with dissolve
    Josephine "..."
    show player 108f with dissolve
    player_name "{b}*Ahem*{/b}"
    show player 109f
    Josephine "Yeah, yeah! I hear you..."
    Josephine "{b}*Sigh*{/b}"
    Josephine "What do you want?"
    show player 108f
    player_name "You work for your {b}Dad{/b}?"
    show player 5
    show joe 5 at Position (xpos=0.8294,ypos=1.0000) with dissolve
    Josephine "Oh, great observation skills..."
    Josephine "What are you, like Sherlock Holmes's retarded nephew or something?"
    show joe 4
    player_name "..."
    show joe 5
    Josephine "Look, I don't want to work here. He just makes me do it so he can keep an eye on me."
    show joe 4
    show player 10
    player_name "That really sucks."
    show player 5
    show joe 5
    Josephine "Right?!"
    Josephine "He's such a control freak, it's ridiculous!"
    show joe 4
    pause
    show joe 5
    Josephine "Anyway, what can I help you with?"
    show joe 4
    return

label josephine_button_dealership_dialogue_after:
    Josephine "What do you want again?"
    show joe 4 at Position(xpos=0.8294,ypos=1.0000)
    return

label josephine_button_dealership_dialogue_buy_vehicle:
    Josephine "Sure! Which one would you like to buy?"
    return

label josephine_button_dealership_dialogue_buy_vehicle_no_money:
    show player 24
    pause
    show player 29
    player_name "Hmmm... I don't have enough money right now."
    return

label josephine_button_dealership_dialogue_insurance_claim_pre:
    show player 14
    player_name "Well, I need to speak with someone regarding an insurance claim"
    show player 11
    show joe 5
    Josephine "Alright. What's the license plate number on the vehicle?"
    show joe 4
    show player 4
    return

label josephine_button_dealership_dialogue_insurance_claim_plate_menu_dialogue:
    player_name "What was {b}[deb_name]'s{/b} vanity plate again?"
    return

label josephine_button_dealership_dialogue_insurance_claim_right_plate:
    show player 11
    show joe 6
    Josephine "Yup, looks like we've got that in our system."
    show joe 5
    Josephine "Do you still live at 240 Cookie Street?"
    show joe 4
    show player 17
    player_name "Yep!"
    show player 11
    show joe 5
    Josephine "Okay. What's the problem with the vehicle?"
    show joe 4
    show player 10
    player_name "The engine is all smashed up!"
    show player 11
    show joe 6
    Josephine "One sec..."
    pause
    Josephine "..."
    pause
    show joe 5
    Josephine "I'm sorry. It seems that the insurance policy on that vehicle was cancelled do to a lack of payment."
    show joe 4
    show player 23
    player_name "What!?"
    show player 22
    show joe 6
    Josephine "I see an outstanding balance of {b}$4,000{/b}."
    Josephine "... And your deductible is set at {b}$5,000{/b}."
    show joe 4
    show player 23
    player_name "( !!! )" with hpunch
    show joe 5
    Josephine "So you're in for at least $9,000 before we'll cover anything..."
    Josephine "How bad is the damage?"
    show joe 4
    show player 22
    player_name "Uhh... Yeah. It's pretty extreme."
    show joe 5
    Josephine "That's a shame. It sounds like you're out of luck, Pal."
    show joe 4
    pause
    show player 10
    player_name "Damn..."
    show player 24
    player_name "What should I do now?"
    return

label josephine_button_dealership_dialogue_insurance_claim_stat_fail:
    show player 24
    player_name "[chr_warn]I... Uhm... Could you?"
    show joe 5
    Josephine "Could I... What?"
    show joe 4
    show player 37
    player_name "[chr_warn]Um... Nevermind."
    pause
    show player 24
    player_name "[chr_warn]I'm sorry I bothered you."
    show joe 5
    Josephine "Well, I hope you get your car fixed."
    show joe 4
    show player 25
    player_name "Yeah, thanks..."
    show player 24
    player_name "( Come on {b}[firstname]{/b}! All you had to do was ask for some help. )"
    player_name "{b}*Sigh*{/b}"
    player_name "( I'm way too nervous... )"
    return

label josephine_button_dealership_dialogue_insurance_claim_pay:
    show player 14
    player_name "I should have enough to cover the cost."
    show player 12
    player_name "Do you accept cash?"
    show player 5
    show joe 5
    Josephine "Yes."
    show joe 4
    show player 14
    player_name "Here."
    show player 41 at Position (xoffset=38) with dissolve
    show joe 5
    Josephine "Thanks."
    show player 5
    show joe 6
    Josephine "Did you bring the car in today?"
    show joe 4
    show player 12
    player_name "No... It's broken."
    player_name "It's still at our house."
    show player 5
    show joe 6
    Josephine "Oh... Well we can send a mechanic out."
    show joe 5
    Josephine "When would you like us to fix it?"
    show joe 4
    show player 14
    player_name "Today would be ideal."
    show player 12
    player_name "It's our only car and it took me forever to get here."
    show player 5
    show joe 5
    Josephine "Umm... Usually, we are booked for a week..."
    show joe 6
    Josephine "Let me look."
    Josephine "You're in luck."
    show joe 5
    Josephine "I should be able to send a mechanic out this afternoon."
    show joe 4
    show player 14
    player_name "Great!"
    player_name "Thank you very much."
    show player 13
    show joe 5
    Josephine "You're welcome."
    show joe 4
    show player 10
    player_name "Anything else?"
    show player 5
    show joe 5
    Josephine "No, you should be all set."
    show joe 4
    show player 14
    player_name "Thanks again!"
    show player 106
    show joe 1 at Position(xpos=0.5474,ypos=0.7630) with dissolve
    Josephine "Uh huh."
    return

label josephine_button_dealership_dialogue_insurance_claim_pay_convince:
    show player 12
    player_name "Would it be possible to make the payments later?"
    show player 10
    player_name "We're kinda going through a rough patch at the moment."
    player_name "The woman I'm living with only has the one car and it's pretty important to us..."
    show player 11
    show joe 5
    Josephine "I don't think I can-"
    show joe 4
    show player 24
    player_name "... And my {b}Father{/b} just passed away a little over a month ago..."
    show player 25
    player_name "So we've been struggling to make ends meet!"
    pause
    show joe 6
    Josephine "{b}*Sigh*{/b} Listen..."
    show joe 5
    Josephine "I'll help you out this {b}ONE{/b} time!"
    show joe 6
    Josephine "My {b}Dad{/b} would kill me if he found out, so keep it on the down-low."
    show joe 4
    show player 14
    player_name "That would be wonderful! Thank you so much!"
    show player 13
    show joe 5
    Josephine "Don't mention it. I kinda like the idea of screwing him over on this."
    show joe 6
    Josephine "I'll just make your debt disappear and reduce your deductible at the same time."
    Josephine "I'll schedule a technician out to your house to repair the vehicle. It should be fixed by the end of the day."
    show joe 4
    show player 10
    player_name "This is amazing, thank you so much!"
    Josephine "... Uh huh."
    show player 14
    player_name "Really, you're a wonderful person!"
    show player 13
    show joe 5
    Josephine "Pffft!!! Yeah... Okay. You {b}owe me one{/b}!"
    show joe 4
    show player 17
    player_name "... Oh, of course. Anything you want!"
    return

label josephine_button_dealership_dialogue_insurance_claim_give_up:
    show player 10
    player_name "I should probably talk to {b}[deb_name]{/b} about this."
    show player 2
    player_name "Thanks!"
    show player 1
    show joe 5
    Josephine "Sure, whatever."
    return

label josephine_button_dealership_dialogue_insurance_claim_proctologist_plate:
    show player 11
    show joe 5
    Josephine "You are definitely not the {b}ASSMAN{/b}. The local proctologist has that license."
    show joe 4
    show player 26
    player_name "Oh. Yeah..."
    show player 4
    return

label josephine_button_dealership_dialogue_insurance_claim_wrong_plate:
    show player 11
    show joe 6
    pause
    show joe 5
    if randomizer() < 50:
        Josephine "I'm not seeing an account that matches that license plate."
    else:
        Josephine "That would be a neat plate, but unfortunately it's not in the system."
    Josephine "Any other license plate you can think of?"
    show joe 4
    show player 4
    return

label josephine_button_dealership_dialogue_kim:
    show player 10
    player_name "What's up with that tubby guy?"
    show player 5
    show joe 5
    Josephine "Hmm?"
    Josephine "Oh, {b}Kim{/b}?"
    Josephine "... Yeah, he's a douchebag."
    Josephine "He spends all day brown nosing my {b}Dad{/b} and then plotting behind his back."
    show joe 4
    show player 12
    player_name "Shouldn't you like, warn your {b}Dad{/b} or something?"
    show player 5
    show joe 5
    Josephine "Psh, hell no!"
    Josephine "If he's too stupid to see what that evil little munchkin is up to, then he deserves to lose his job."
    Josephine "At least then, I could get out of this shit hole..."
    show joe 4
    player_name "..."
    Josephine "..."
    show joe 3
    Josephine "ohmygodthisissoboring!"
    show joe 4
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
