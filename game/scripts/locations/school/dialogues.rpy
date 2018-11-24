label school_diane_delivery_3:
    scene school
    show player 166 at left with dissolve
    player_name "Phew, almost there..."
    show player 168b
    ann "HOLD IT RIGHT THERE!" with hpunch
    show player 168c
    player_name "Hmm?"
    show player 168b
    show annie 5 at right with dissolve
    ann "Where do you think you're going with all that milk?"
    show annie 6
    show player 168
    player_name "Oh, hey {b}Annie{/b}."
    player_name "I'm supposed to deliver this to the cafeteria."
    show player 167
    show annie 5
    ann "I don't think so."
    show annie 6
    show player 166
    player_name "What, why?"
    show player 165
    show annie 5
    ann "{b}Mrs. Smith{/b} didn't say anything to me about a milk delivery today."
    show annie 6
    show player 166
    player_name "... So?"
    player_name "I'm sure {b}Mrs. Smith{/b} doesn't tell you about every little thing that's going on in the school..."
    show player 165
    show annie 3
    ann "Uhh, yes she does."
    ann "I'm her second in command."
    show annie 1
    player_name "..."
    show player 166
    player_name "Look {b}Annie{/b}, this is really heavy. Can you please just get out of my way?"
    player_name "I'm positive it's supposed to go to the cafeteria."
    show player 165
    show annie 4
    ann "I said no!"
    ann "Not until I clear it with {b}Mrs. Smith{/b}."
    show annie 1
    player_name "..."
    show annie 3
    ann "C'mon, she's in her office."
    hide annie with dissolve
    show player 166
    player_name "{b}Her office on the third floor?!{/b}"
    player_name "Can you at least help me carry this?"
    show player 165
    ann "Nope!"
    pause
    show player 168c
    player_name "{b}*Sigh*{/b}"
    hide player with dissolve
    return

label school_erik_intro_started:
    scene outside_school_b
    show duo 6 at left with dissolve
    show mia 1 at right with dissolve
    player_name "Hey, {b}Mia{/b}!"
    show duo 1 at left
    show mia 4 at right
    mia "Hey, {b}[firstname]{/b}! Glad to see you're back!"
    mia "Hi, {b}Erik{/b}! How was your weekend?"
    show duo 10 at left
    show mia 1 at right
    eri "I mostly stayed in my room..."
    show duo 1 at left
    show mia 3 at right
    mia "That's cool. Sometimes I like alone time too!"
    show mia 4 at right
    mia "What about you, {b}[firstname]{/b}? What have you been up to?"
    show mia 2 at right
    show duo 9 at left
    player_name "Well, I'm not sure if you've heard or not, but my {b}Dad{/b} passed away. So I've been dealing with that..."
    show mia 6 at right
    mia "Oh yeah. I heard from my mom..."
    show duo 15 at left
    mia "I didn't mean to bring it up. I'm sorry you had to go through that. I'm just glad you're finally back!"
    show mia 2 at right
    player_name "Thanks. I'll be fine. Don't worry."
    show mia 4 at right
    mia "Listen, I was looking for someone to {b}help me get ready for the final exams{/b}, so..."
    show duo 7 at left
    mia "... If you're interested, let me know!"
    show duo 8 at left
    show mia 1 at right
    player_name "Uhh, sure... I guess?"
    player_name "Where do you want to meet? The library?"
    show duo 1
    show mia 6
    mia "Umm, I'd have to ask my parents, first."
    mia "They probably won't let me though."
    mia "I'm not really allowed to stay late after school or see friends outside of my house."
    show mia 2
    show duo 9
    player_name "Really?! That sucks!"
    show duo 7
    show mia 3
    mia "Yeah... heh, heh."
    show duo 7
    show mia 6
    mia "Anyway, It'd be easier if you just came over to my house to study..."
    show mia 3 at right
    mia "You know where I live, so just drop by whenever you want!"
    show duo 7 at left
    show mia 4 at right
    mia "I'd better get going. {b}Science class{/b} is starting soon!"
    show duo 1
    mia "{b}Professor Okita{/b} said today's {b}laboratory experiment{/b} will be challenging."
    mia "That means it's probably gonna to take the entire hour to complete."
    show mia 1
    show duo 10
    eri "Ugh. Don't remind me..."
    show duo 1
    show mia 4
    mia "Talk to you later guys!"
    hide mia with dissolve
    hide duo with dissolve
    return

label school_roxxy_shower_event:
    scene school
    show jersey 10 with dissolve
    player_name "( Woah! it's hard to breathe! )"
    player_name "( It's so damn hot outside... )"
    show jersey 33 at Position(xoffset=22) with fastdissolve
    player_name "( ... And I'm SOAKED! )"
    player_name "( I should {b}take a shower{/b} before going to my next class. )"
    return

label school_roxxy_intense_gymercise:
    scene school
    show erik 28 at right
    show player 1 at left
    with dissolve
    eri "Hey, {b}[firstname]{/b}."
    show erik 27
    show player 14
    player_name "Hey, {b}Erik{/b}."
    player_name "Why are you wearing your gym clothes?"
    show erik 28
    show player 11
    eri "{b}Coach Bridget{/b} wants to speak with you!"
    eri "She's waiting out by the track."
    show erik 27
    show player 10
    player_name "Crap, it's probably about all the training I've missed... She's gonna kill me!"
    show erik 28
    show player 5
    eri "You'd better hurry!"
    show erik 27
    show player 10
    player_name "Yeah, thanks for letting me know, man!"
    show erik 29
    show player 11
    eri "No problem, dude!"
    show erik 27
    hide player with dissolve
    pause
    show erik 28
    eri "Good luck!"
    hide erik with dissolve
    return

label school_bissette_challenge:
    scene school
    show player 34 with dissolve
    player_name "( I should probably {b}talk to Miss Bissette about that private tutoring{/b}. )"
    player_name "( I can't understand any of the material in class... )"
    player_name "( ...I think I'm too far behind to catch up on my own. )"
    player_name "( A little bit of extra help never hurt anybody... )"
    show player 4 at Position (xoffset=5) with dissolve
    player_name "( ...And I may get that reward if I do well in the final quiz! )"
    hide player with dissolve
    return

label school_mia_glasses_favor:
    scene school
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Hey, {b}[firstname]{/b}."
    show mia 7
    show player 14
    player_name "Hey, {b}Mia{/b}."
    show player 12
    player_name "How's your dad doing?"
    show player 5
    show mia 10
    mia "He's alright. I think..."
    show mia 51 with dissolve
    mia "My mom was cleaning up his office last night and found these old glasses..."
    show mia 7
    show player 446
    with dissolve
    pause
    show player 448
    player_name "Sweet, Aviators!"
    player_name "Does he still wear them?"
    show player 13
    show mia 50
    with dissolve
    mia "He used to but that was a long time ago."
    mia "I was thinking maybe he would like to use them again."
    show mia 50b
    show player 14
    player_name "That's nice."
    show player 13
    show mia 50
    mia "Actually, I was wondering if you could drop them off at his work?"
    mia "I have to be somewhere later and I won't have time to take them myself."
    show mia 50b
    show player 10
    player_name "Huh? You want {b}me{/b} to go?"
    show player 5
    show mia 50
    mia "Why not?"
    mia "You two seem to be getting along so well..."
    mia "...And he would be happy to see them again, I'm sure!"
    mia "Ever since you spoke to him, he's been doing much better."
    show mia 50b
    show player 12
    player_name "Ehh... Yeah, I suppose I could drop them off at his work."
    show player 447
    show mia 10
    with dissolve
    mia "Thanks, that's really sweet of you to do this for me."
    show mia 7
    show player 448
    player_name "It's no problem, I don't mind visiting him."
    show player 447
    show mia 10
    mia "See you later, then!"
    show mia 7
    show player 448
    player_name "Bye."
    show unlock54 at truecenter with dissolve
    pause
    hide unlock54 with dissolve
    hide player
    hide mia
    with dissolve
    return

label school_erik_bullying_2_started:
    scene school
    show dexter 9 at right with dissolve
    eri "Ugh!!"
    eri "Let... me go... {b}Dexter{/b}!"
    dex "Not a chance, chubby."
    dex "You still haven't given me your homework."
    dex "I guess you didn't get the message."
    eri "I told you! I already turned it in! I don't have it anymore!"
    dex "Well then, I guess you'll have to give me something else..."
    dex "How much money do you got on you?"
    eri "What?!"
    dex "I said, how much money are you going to give me before I shove your face into a locker!!"
    eri "!!!"
    eri "{b}Dexter{/b}! I... I..."
    show player 15 at left with dissolve
    show dexter 10
    player_name "HEY!!!"
    player_name "Leave him alone, {b}Dexter{/b}!"
    show player 16
    show dexter 9
    dex "Well, if it isn't your loser friend."
    show dexter 10
    show player 15
    player_name "{b}Dexter{/b}, stop picking on {b}Erik{/b}."
    show player 16
    show dexter 9
    dex "Why? Would you like to take his place?"
    player_name "..."
    show dexter 12 with dissolve
    dex "Step up, {b}[firstname]{/b}."
    show dexter 13
    dex "Let's see what you got!"
    return

label school_erik_bullying_2_started_dex_pass:
    show dexter 14
    show player 387 with dissolve
    player_name "I'm not scared of you, {b}Dexter{/b}!"
    show player 388
    show dexter 15
    dex "Well, you should be scared of... THIS!"
    hide player
    hide dexter
    show dexter 16 at left
    with dissolve
    pause
    show dexter 17 at right with dissolve
    player_name "Haiii!!"
    hide dexter
    show player 390 at left
    show dexter 18 at right
    with dissolve
    dex "Arghh!!"
    dex "You... Little... Shit..."
    show dexter 15 with dissolve
    show player 389
    player_name "!!!"
    show player 391
    show dexter 19 with hpunch
    pause
    hide player
    show dexter 20 at left
    with dissolve
    dex "Not so fast this time, huh?!"
    dex "I'll show you..."
    hide player
    with dissolve

    scene school_fight_cs1 with fade
    show text "Even after all my recent training at the gym,\n{b}Dexter{/b} was still too strong for me...\n...but I knew now, that I could hurt him..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    scene school_fight_cs2 with fade
    show text "...And then, everything went dark." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    scene black with fade
    pause

    scene school with None
    show mia 24 at left
    show dexter 21 at Position (xpos=713)
    with dissolve
    mia "{b}[firstname]{/b}!! Are you okay?!"
    show mia 23
    pause
    show mia 28 with dissolve
    mia "What's your problem, {b}Dexter{/b}?"
    mia "You really hurt him!"
    show mia 27
    show dexter 22
    dex "Mind your own business!"
    dex "He had it coming!!"
    show dexter 23
    show roxxy 30 at right with dissolve
    rox "{b}Dexter{/b}?"
    show roxxy 29
    show dexter 24
    dex "What?!"
    show dexter 23
    show mia 23 with dissolve
    show roxxy 27
    rox "..."
    show roxxy 28
    rox "Umm.... {b}Dexter{/b}, what's going on?"
    rox "Did you do that?"
    show roxxy 29
    show mia 27 with dissolve
    show dexter 24
    dex "Nothing's going on!!"
    show dexter 12
    dex "I just finished teaching this little shit a lesson."
    show dexter 23
    show roxxy 30
    rox "Really? You had to do this now? In the hallway?"
    show roxxy 29
    show dexter 24
    dex "Shut up, {b}Roxxy{/b}."
    dex "Come on. Lets get out of here!"
    show roxxy 27
    dex "I've got better things to do than watch a bunch of idiots standing around."
    hide dexter
    hide roxxy
    with dissolve
    hide mia
    show eve 9 at Position (xpos=75)
    show mia 23 at left
    show judith 40 at Position (xpos=600)
    show erik 50 at Position (xpos=900)
    with dissolve
    jud "Oh my gosh! What happened?!"
    show judith 41
    show eve 10
    eve "{b}Dexter{/b} is such a jerk."
    eve "He went too far this time."
    show eve 9
    hide erik
    show teacher 15 at Position (xpos=700)
    show erik 50 at Position (xpos=900)
    with dissolve
    bis "!!!"
    bis "What is happening over here?"
    bis "What is wrong with {b}[firstname]{/b}?"
    show teacher 14
    show mia 26 with dissolve
    mia "He got into a fight with {b}Dexter{/b} and {b}Dexter{/b} slammed him into the lockers."
    mia "He's still breathing. I hope he'll be alright."
    show mia 25
    bis "..."
    show teacher 15
    bis "We should be calling the ambulance!"
    $ playSound()
    scene black with fade
    hide mia
    hide eve
    hide teacher
    hide erik
    hide judith
    return

label school_erik_bullying_2_started_dex_fail:
    show dexter 14 at right with dissolve
    show player 6 at left with dissolve
    player_name "[dex_warn]I don't want to fight you, {b}Dexter{/b}!"
    show player 23 with dissolve
    player_name "[dex_warn]I just want you to leave {b}Erik{/b} alone..."
    show player 22
    show dexter 15
    dex "Really?"
    show dexter 14
    show player 10
    player_name "[dex_warn]That's all..."
    show player 22
    show dexter 12 with dissolve
    dex "Hah!"
    dex "Weak and pathetic..."
    dex "...Just like your father!"
    hide dexter
    with dissolve
    show player 24
    player_name "[dex_warn]..."
    hide player
    with dissolve
    return

label school_roxxy_intro_started:
    scene school with fade
    show duo 1 at left
    show dexter 1 at Position (xpos=700)
    show roxxy 4 at right
    with dissolve
    rox "... So then {b}Becca{/b} threw her retainer in the toilet!"
    show dexter 3
    dex "Bahahahahahah!"
    show roxxy 3d
    rox "..."
    show roxxy 3c
    rox "... Ugh, What are you two losers looking at?!"
    show dexter 2 at Position (xoffset=-2)
    show roxxy 3b
    show duo 2 at left
    eri "I think we're looking at the combined IQ of 2."
    show duo 3 at left
    player_name "Hah!!"
    show roxxy 31
    rox "Excuse me?!"
    show roxxy 3b
    show dexter 8 at Position (xoffset=-2)
    dex "... Huh, I don't get it?"
    show dexter 2 at Position (xoffset=-2)
    show duo 7 at left
    show roxxy 30
    rox "They're calling us stupid..."
    show roxxy 29
    show dexter 8 at Position (xoffset=-2)
    dex "They are?!"
    show dexter 6 at Position (xoffset=-119) with dissolve
    dex "Hey! You calling us stupid?!"
    show dexter 5 at Position (xoffset=-119)
    show duo 10
    show roxxy 3b
    eri "I... N-no, I didn't... I mean, I wouldn't..."
    show duo 11
    show dexter 4 at Position (xoffset=-20) with dissolve
    dex "Cause I'll smash your face in, you little shit!"
    show duo 4
    show dexter 2 at Position (xoffset=-2) with dissolve
    show roxxy 3
    rox "...and what are {b}YOU{/b} laughing at?"
    show roxxy 2
    rox "Didn't your deadbeat loser of a father kill himself or something?"
    show roxxy 1g
    show duo 9
    eri "..."
    show player 15 at left
    player_name "At least I {b}HAD{/b} a father growing up..."
    player_name "... And I don't live in a {b}TRAILER{/b}!!"
    show player 16
    show roxxy 3c
    rox "!!!" with hpunch
    show roxxy 3
    rox "... You're dead!"
    rox "Dexter, get 'em!!!"
    show roxxy 3d
    show player 11
    show dexter 8 at Position (xoffset=-2)
    dex "Hold up, {b}Roxxy{/b}. {b}Principal Smith{/b} is coming..."
    dex "If I get caught fighting again, {b}Coach Bridget{/b} said she'll kick me off the team."
    hide dexter with dissolve
    show roxxy 3c
    show player 16
    rox "Pfft, fine..."
    show roxxy 3
    rox "... This isn't over, {b}[firstname]{/b}!"
    rox "I'll deal with you later!"
    hide roxxy with dissolve
    pause
    hide player
    show duo 1 at left
    show principal 5 at right with dissolve
    smi "You two! Get over here, {b}RIGHT NOW{/b}!!!"
    show duo 11 at left
    smi "What are you still doing in the damn hallway??!"
    show duo 12 at left
    show principal 3 at right
    eri "Sorry, {b}Principal Smith{/b}! We were just-"
    show duo 11 at left
    show principal 4 at right
    smi "Ah, {b}[firstname]{/b}! Finally returned to us I see..."
    show duo 6
    show principal 1 at Position(xpos=0.935, ypos=1.0)
    player_name "Y-yes, Ma'am."
    show duo 7
    show principal 27
    smi "Well it's about time! Do you have any idea how far your grades have fallen?!"
    show duo 9
    show principal 1
    player_name "... They have?"
    show duo 10
    eri "That doesn't seem fair!"
    eri "Don't you know his Dad-"
    show duo 11
    show principal 2
    smi "That's quite enough, young man!"
    show principal 4 at right
    smi "I suggest you get your butt to class before you find it sitting in detention!"
    show duo 10
    show principal 1 at Position(xpos=0.935, ypos=1.0)
    eri "..."
    show duo 12
    show principal 4 at right
    smi "... And as for you, {b}[firstname]{/b}. We need to discuss your failing grades!"
    smi "I want you upstairs, in my office, right away!"
    show duo 9
    show principal 1 at Position(xpos=0.935, ypos=1.0)
    player_name "Yes, {b}Principal Smith{/b}."

    hide principal
    hide duo
    with dissolve
    show player 5 at left
    show erik 3b at right
    eri "Man, she's pure evil..."
    show player 2
    show erik 1
    player_name "Heh, yeah."
    show player 1
    show erik 5
    eri "I'm serious! She's like the Evil Ice Queen from Whorecraft!"
    show player 2
    show erik 1
    player_name "Well, {b}I'd better get up to her office{/b} before her mood worsens."
    show player 1
    show erik 5
    eri "Good luck, dude..."
    show player 2
    show erik 1
    player_name "... Thanks."
    show player 1
    show erik 4
    eri "Oh shoot, I almost forgot!"
    eri "{b}I slipped a little welcome back present into your locker{/b}!"
    show player 2
    show erik 1
    player_name "Really?"
    show player 1
    show erik 4
    eri "Glad to have you back, dude!"
    show player 2
    show erik 1
    player_name "Thanks, {b}Erik{/b}!"
    show player 34
    player_name "Hmm..."
    show player 10
    player_name "... You know, I don't remember my {b}locker combination{/b}."
    show player 11
    show erik 5
    eri "You didn't write it down?"
    show player 10
    show erik 1
    player_name "No but I guess I should have, huh?"
    show player 11
    show erik 5
    eri "You're probably going to have to {b}talk to {b}Principal Smith{/b} about it{/b}."
    show player 10
    show erik 1
    player_name "Ugh, you're probably right..."
    player_name "I'll see you later, {b}Erik{/b}."
    show player 11
    show erik 5
    eri "Yup, see ya, {b}[firstname]{/b}."
    return

label school_hallway_dewitt_talent_show_ask_annie:
    scene school
    show player 4f with dissolve
    player_name "( I wonder who I should talk to first? )"
    show player 9f at left with dissolve
    pause
    pause
    show player 22 at left
    show annie 4 at right
    with hpunch
    ann "{b}[firstname]{/b}, stop loitering in the hallway!"
    show annie 1
    show player 12
    player_name "{b}Annie{/b}, I just stepped into the hallway..."
    show player 5
    show annie 5
    ann "Whatever. Hurry to your next class before I write you up!"
    show annie 6
    show player 12
    player_name "Alright! Sheesh..."
    show player 10
    player_name "Oh, Hey! Wait a second!"
    player_name "You don't happen to play an instrument or sing do you?"
    show player 5
    show annie 3
    ann "I do. What of it?"
    show annie 1
    show player 10
    player_name "Well, you see, {b}Ms. Dewitt{/b} is looking for people to play in the talent show."
    show player 5
    show annie 5
    ann "Yes, I'm well aware."
    show annie 6
    player_name "..."
    show player 10
    player_name "Would you maybe like to be a part of it?"
    show player 5
    show annie 9
    ann "Pfft, absolutely not!"
    show annie 5
    ann "You do realize, {b}Principal Smith{/b} is trying to get that stupid show cancelled, right?"
    show annie 6
    show player 12
    player_name "Yeah, I heard."
    show player 5
    show annie 3
    ann "So there's no way I could participate in it!"
    show annie 1
    show player 12
    player_name "You don't always have to listen to {b}Principal Smith{/b}, {b}Annie{/b}."
    show player 5
    show annie 5
    ann "I am head of the disciplinary committee, official hall monitor, and {b}Principal Smith's{/b} second in command!"
    show annie 3
    ann "It's my sworn duty to follow her orders."
    show annie 1
    show player 12
    player_name "This isn't the military, {b}Annie{/b}..."
    show player 11
    show annie 7
    ann "SILENCE!"
    show annie 1
    show player 10
    player_name "But-"
    show player 11
    show annie 5
    ann "{b}Principal Smith{/b} wants that show cancelled and plans have been set in motion."
    show annie 6
    show player 12
    player_name "... Plans?"
    show player 5
    show annie 9
    ann "Grr, I've said too much."
    show annie 1
    show player 11
    player_name "..."
    show annie 5
    ann "I suggest you just give up on the talent show. It's not going to happen, I assure you."
    show annie 8
    ann "Now get out of my way so I can finish my patrol!"
    hide annie with dissolve
    show player 12
    player_name "What a whackjob..."
    hide player with dissolve
    return

label school_dewitt_school_sneak_mission:
    scene expression game.timer.image("outside_school{}")
    show player 32f with dissolve
    player_name "( Where the heck is {b}Erik{/b}? )"
    player_name "( He should have been here by now... )"
    show player 31f
    show erik 5 at right with dissolve
    eri "{b}[firstname]{/b}?"
    show erik 52
    show player 10 at left with dissolve
    player_name "There you are!"
    player_name "What took you so long?"
    show player 5
    show erik 4
    eri "Sorry, dude! I was pillaging an Orcette village and I kinda lost track of time..."
    show erik 1
    show player 12
    player_name "... Huh?"
    player_name "Is that a video game thing?!"
    show player 5
    show erik 5
    eri "... Yeah."
    show erik 1
    show player 37 with dissolve
    player_name "..."
    show player 38 with dissolve
    player_name "Let's just focus on the mission, {b}Erik{/b}."
    show player 5 with dissolve
    show erik 5
    eri "What is our mission anyways?"
    show erik 52
    show player 239_240 with dissolve
    pause
    show player 618 at Position (xoffset=35) with dissolve
    player_name "We gotta break into {b}Principal Smith's office{/b} and apply this {b}adhesive solution{/b} to her office chairs."
    show player 617 at Position (xoffset=35)
    show erik 5
    eri "Is that the same stuff we made in {b}Miss Okita's class{/b} awhile back?"
    show erik 52
    show player 618 at Position (xoffset=35)
    player_name "Yeah. {b}Kevin{/b} made it for me."
    show player 617 at Position (xoffset=35)
    show erik 5
    eri "That stuff is crazy strong!"
    eri "... And you want to put it on {b}Principal Smith's chairs{/b}?"
    eri "Won't she get stuck?"
    show erik 52
    show player 17 with dissolve
    player_name "Heh, that's kind of the point, dude."
    show player 13
    show erik 3b
    eri "Oh, right."
    show erik 3c
    pause
    show erik 3b
    eri "Well, lead the way I guess..."

    scene outside_school_night02a with dissolve
    show text "The school was locked down tight but I was determined to find an entry point somewhere.\nPerhaps one of these main floor windows would do the trick?" at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    pause 0.5

    show outside_school_night02b with dissolve
    show text "{b}Erik{/b} was not the ideal partner for a stealth mission but I was still glad to have him along.\nThere's no way I could have managed this without him." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    pause 0.5

    scene outside_school_night02c with dissolve
    show text "As {b}Erik{/b} helped me through the window I couldn't help but feel like this had all been too easy...\n... There was certainly something ominous about the school tonight." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    $ playMusic()
    hide text with dissolve

    scene black
    with dissolve
    pause 0.5

    scene school_night with dissolve
    player_name "!!!"
    player_name "Shh, I hear something."

    scene cult_event 1
    with Dissolve(0.3)
    eri "..."
    eri "!!!"
    scene cult_event 2
    with Dissolve(0.3)
    player_name "Shhh!"
    player_name "Stay quiet..."
    scene cult_event 3
    with Dissolve(0.3)
    window hide
    pause
    scene cult_event 4
    with Dissolve(0.3)
    scene school_night
    show player 22 at left
    show erik 51 at right
    with dissolve
    pause
    show player 10
    player_name "What the-"
    player_name "Who was that?"
    player_name "... And where are they going?"
    show player 5
    show erik 53
    eri "I don't like this, {b}[firstname]{/b}!"
    eri "We should get out of here!"
    show erik 52
    show player 10
    player_name "Calm down, dude."
    player_name "They don't know we're here."
    show player 5
    show erik 53
    eri "What do you think is up with the creepy outfits?"
    show erik 52
    show player 10
    player_name "I dunno."
    show player 92
    player_name "I think we should follow them."
    show player 90
    show erik 53
    eri "Are you nuts?!"
    show erik 52
    show player 92
    player_name "It'll be fine, {b}Erik{/b}!"
    player_name "Just stay behind me and keep quiet!"
    show player 90
    show erik 2 with dissolve
    eri "{b}*Sigh*{/b}"
    show erik 3 with dissolve
    eri "... Fine."
    hide player
    hide erik
    with dissolve
    return

label school_dewitt_pre_talent_show_chat:
    scene school
    show kevin 23 at Position (xpos=600)
    show eve 6 at right
    with dissolve
    show player 13 at left with dissolve
    eve "There he is!"
    show eve 5
    show kevin 22 with dissolve
    kev "Finally!"
    kev "How did everything go last night?"
    show kevin 23 with dissolve
    show eve 2b
    eve "We were starting to worry you got caught or something..."
    show eve 5
    show player 14
    player_name "Nope. Everything went smoothly."
    player_name "Have you guys seen {b}Principal Smith{/b} and {b}Annie{/b} this morning?"
    show player 13
    show kevin 9b
    kev "Not for awhile."
    kev "You think they're really stuck up in her office?!"
    show kevin 23
    show player 17
    player_name "I hope so."
    show player 13
    show eve 6
    eve "Haha! This is so awesome!"
    show eve 5
    show player 14
    player_name "Where's {b}Miss Dewitt{/b}?"
    show player 13
    show eve 6
    eve "She's in the {b}Auditorium{/b} setting up for the show."
    show eve 5
    show kevin 9b
    kev "We were just getting ready to go help her."
    show kevin 23
    show eve 6
    eve "Yeah, why don't you come with us?"
    show eve 5
    show player 14
    player_name "Hmm, I'm gonna go check on {b}Principal Smith's office{/b} first."
    player_name "I want to make certain there won't be any surprises."
    show player 13
    show kevin 9b
    kev "Yeah, that's probably a good idea."
    show kevin 23
    show eve 2b
    eve "... Just promise me you'll be careful, {b}[firstname]{/b}."
    show eve 1
    show player 17
    player_name "I will."
    show player 13
    show eve 2b
    eve "Meet us in the {b}Auditorium{/b} when you're finished."
    hide eve
    hide kevin
    hide player
    with dissolve
    return

label school_weekend_lock:
    scene expression game.timer.image("outside_school{}")
    show player 12 with dissolve
    player_name "( It's the {b}weekend{/b}. )"
    player_name "( The school is {b}closed{/b} until {b}Monday{/b}. )"
    hide player 12 with dissolve
    hide event01
    return

label night_closed_school:
    if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
        $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    scene expression game.timer.image("outside_school{}")
    if False:
        if M_erik.get("webcam help"):
            $ player.go_to(L_school_hall)
            call expression game.dialog_select("school_erik_webcam_quest")
            call expression game.dialog_select("school_erik_webcam_quest_sneak_in")

            $ game.main()
        else:

            call expression game.dialog_select("school_erik_webcam_quest_need_help")
    else:

        call expression game.dialog_select("school_closed")
    call expression game.dialog_select("map_dialogue")

label school_closed:
    show player 2 with dissolve
    player_name "( The {b}school{/b} is closed at night... I should come back tomorrow. )"
    hide player 2 with dissolve
    return

label school_hallway:
    $ player.go_to(L_school_hall)
    $ game.main()

label school_locker_smith_go_to_locker:
    scene location_school_day_blur
    show player 11f at right
    show annie 3f at Position(xpos=0.3, ypos=1.0)
    with dissolve
    ann "Alright, let's get this over with."
    show annie 17 with dissolve
    pause
    show annie 18 at Position(xpos=0.24, ypos=1.0) with dissolve

    show player 10f
    player_name "Wow, so that key opens everybody's locker?"
    show player 11f
    show annie 17 at Position(xpos=0.3, ypos=1.0) with dissolve
    pause
    show annie 3f with dissolve
    ann "Pfft, this key opens every lock and door in the school."
    show player 10f
    show annie 1f
    player_name "For real?!"
    show player 11f
    show annie 5f
    ann "Duh, that's why it's called a {b}Masterkey{/b}."
    show player 10f
    show annie 6f
    player_name "How come you get it?"
    show player 11f
    show annie 5f
    ann "Umm, because I bust my ass every day helping {b}Principal Smith{/b} keep all you kids in line!?"
    show player 12f
    show annie 6f
    player_name "Kids? We're the same age..."
    show player 16f
    show annie 3f
    ann "... Yeah, right. Everyone around here is so immature."
    show player 10f
    show annie 1f
    player_name "So you just have that {b}Masterkey{/b} with you all the time?"
    show player 11f
    show annie 3f
    ann "Of course not! {b}Principal Smith keeps it in her office{/b} but we like, never have to use it."
    show player 10f
    show annie 1f
    player_name "Never?"
    show player 11f
    show annie 4f
    ann "Nobody else is dumb enough to lose their locker combination..."
    show annie 3f
    ann "Hurry up and grab what you need."
    ann "We're gonna be late for {b}Athletics Class{/b}!"
    show player 10f
    show annie 1f
    player_name "Yeah, yeah. I'm going."
    return

label school_hallway_smith_unlocked_locker:
    scene location_school_day_blur
    show player 34
    with dissolve
    player_name "( Hmm, so {b}Principal Smith has a Masterkey in her office somewhere{/b}. )"
    player_name "( ... {b}that would be useful thing to have{/b}! )"
    player_name "( ... )"
    player_name "( Something to think about. )"
    player_name "( For now, I should head to the {b}Boys Locker Room{/b} and get changed for {b}Athletics Class{/b}. )"

    return

label school_erik_webcam_quest:
    show player 14 at left
    show erik 1 at right
    player_name "Hey!"
    show player 17
    player_name "I thought you wouldn't show up."
    show player 1
    show erik 4
    eri "I told {b}Mrs. Johnson{/b} I went to see a movie at the mall..."
    show player 17
    show erik 1
    player_name "Nice."
    show player 11
    show erik 5
    eri "But I can't be out too long: I have to be home before bedtime."
    show player 92
    show erik 1
    player_name "You have a bedtime?!"
    show player 91
    show erik 3
    eri "... I just don't like to upset {b}Mrs. Johnson{/b}, you know?"
    show player 113
    show erik 1
    player_name "Anyway, we have to be quick and quiet!"
    show player 1
    show erik 5
    eri "Is there an alarm, though?"
    show erik 1
    show player 2
    player_name "We shouldn't have to worry about that if we use the window!"
    player_name "Just follow me..."
    hide player
    hide erik
    hide event01_night
    hide ui
    scene black
    return

label school_erik_webcam_quest_sneak_in:
    with dissolve
    with Pause(0.5)
    show outside_school_night02a with dissolve
    show text "After some convincing, {b}Erik{/b} followed me to the right side of the school.\nWe quickly ran through the yard towards one of the main floor windows." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    with Pause(0.5)

    show outside_school_night02b with dissolve
    show text "I had to give {b}Erik{/b} a boost first.\n I have to say, it was a lot harder than I thought..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    with Pause(0.5)

    show outside_school_night02c with dissolve
    show text "It was then my turn, as I jumped up and snuck inside...\n We had finally made it in, and no one had seen us." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    $ playMusic()
    hide text with dissolve

    hide outside_school_night02a
    hide outside_school_night02b
    hide outside_school_night02c
    scene black
    with dissolve
    with Pause(0.5)
    scene school_night with dissolve
    player_name "!!!"
    player_name "I hear someone coming..."
    scene cult_event 1
    with Dissolve(0.3)
    eri "What the-"
    scene cult_event 2
    with Dissolve(0.3)
    player_name "Shhh!"
    player_name "Stay quiet..."
    scene cult_event 3
    with Dissolve(0.3)
    window hide
    pause
    scene cult_event 4
    with Dissolve(0.3)
    scene school_night
    show player 22 at left
    show erik 5 at right
    with dissolve
    eri "I have a bad feeling about this..."
    show player 10
    show erik 1
    player_name "Yeah, Something's going on here."
    show player 11
    show erik 5
    eri "What are they doing in the school this late?"
    eri "... And wearing those strange outfits?"
    show player 92
    show erik 1
    player_name "Let's follow them and see where they're going."
    show player 91
    show erik 5
    eri "Really? Cause I was thinking maybe we should just leave..."
    show player 26
    show erik 3
    player_name "Don't be a chicken!"
    player_name "Plus, we still haven't finished what we came here for..."
    show player 91
    show erik 2
    eri "{b}*Sigh*{/b}"
    show erik 3
    eri "Fine..."
    hide player 91 with dissolve
    hide erik 3 with dissolve
    return

label school_erik_webcam_quest_need_help:
    show player 114 with dissolve
    player_name "Hmm..."
    show player 10
    player_name "( I'm gonna need some {b}help{/b} sneaking into the school at night. )"
    hide player 10 with dissolve
    return

label school_roxxy_dexter_argument:
    scene school
    show eve 2 at right
    show kevin 23f at Position (xpos=500)
    with dissolve
    eve "Yeah, they are out there arguing right now!"
    show eve 5
    show kevin 9bf
    kev "Hah, they are the worst..."
    kev "They totally deserve each other!"
    show kevin 23f
    show eve 2
    eve "I know right..."
    eve "C'mon, we should go check it out before it's over."
    show eve 5
    show kevin 9bf
    kev "... I'm good. Their stupid drama doesn't do anything for me..."
    show kevin 23f
    show player 14 at left with dissolve
    player_name "What's going on guys?"
    show player 13
    show kevin 9b with dissolve
    kev "Heya, Bruh!"
    show kevin 23
    show eve 4 with dissolve
    eve "Hey, {b}[firstname]{/b}."
    show eve 2 with dissolve
    eve "{b}Roxxy{/b} and {b}Dexter{/b} are causing some big scene over at the {b}basketball court.{/b}"
    eve "I was just about to go check it out."
    eve "... Wanna come with?"
    show eve 5
    show player 14
    player_name "Yeah, okay."
    player_name "Let's go."
    show player 13
    show kevin 9b
    kev "See you guys later!"
    hide player
    hide kevin
    hide eve
    with dissolve
    return

label school_roxxy_dexter_confront:
    scene school
    show player 5 at left
    show dexter 1 at right
    show dexter 4
    with dissolve
    dex "{b}[firstname]{/b}!"
    show dexter 2 with dissolve
    show player 10
    player_name "Oh, man. Here we go..."
    player_name "What do you want, {b}Dexter{/b}?"
    show player 5
    show dexter 6 with dissolve
    dex "Have you been perving on {b}Roxxy{/b} in the shower?!"
    show dexter 5
    show player 12
    player_name "Who told you that?"
    show player 11
    show dexter 8 with dissolve
    dex "... {b}Becca{/b}!"
    show dexter 6 with dissolve
    dex "Is it true?"
    show dexter 2 with dissolve
    show player 10
    player_name "No!"
    player_name "I just went to take a shower after my gym class."
    player_name "It's not my fault {b}Roxxy{/b} was already in there!"
    show player 5
    dex "..."
    show dexter 6 with dissolve
    dex "So you WERE perving on her!"
    show dexter 2 with dissolve
    show player 10
    player_name "Huh?"
    show player 12
    player_name "No!"
    player_name "Weren't you listening?!"
    player_name "Look man, I wasn't in there to perv on {b}Roxxy{/b}..."
    player_name "I needed to shower!"
    player_name "I promised her I wouldn't look."
    show player 11
    dex "..."
    hide player
    show dexter 7 at left

    player_name "{b}*Gurt*{/b}" with hpunch
    show player 89 at left
    show dexter 1 at right
    show dexter 6
    with dissolve
    dex "Leave {b}Roxxy{/b} alone!"
    show dexter 5
    show player 88
    player_name "{b}*Weeze*{/b}"
    show dexter 6
    dex "She's mine!"
    dex "Understand?!"
    show dexter 5
    player_name "{b}*Gasp*{/b}"
    show player 89
    show dexter 4 with dissolve
    dex "Go near her again and I'll bash your face in!"
    show dexter 2 with dissolve
    show player 88
    player_name "{b}*Cough Cough*{/b}"
    show player 10 with dissolve
    player_name "... I thought you two were finished?"
    show player 90
    show dexter 8
    dex "... Huh?"
    dex "Who said that?"
    show dexter 2
    show player 10
    player_name "You did!"
    player_name "The other day, at the {b}basketball court{/b}."
    show player 90
    show dexter 6 with dissolve
    dex "It's not over!"
    dex "She'll apologize and we'll get back together."
    show dexter 2 with dissolve
    show player 10
    player_name "... I'm not so sure."
    show player 90
    show dexter 15 at Position (xoffset=2) with dissolve
    dex "You want another one?!"
    show dexter 14 at Position (xoffset=2)
    show player 88 with dissolve
    player_name "{b}*Cough*{/b}... Please, no."
    show player 89
    show dexter 15 at Position (xoffset=2)
    dex "Then stay away from my girl!"
    dex "Got it?!"
    show dexter 14 at Position (xoffset=2)
    show player 10 with dissolve
    player_name "... Yeah, I got it."
    show player 90
    show dexter 15 at Position (xoffset=2)
    dex "That's what I thought!"
    hide dexter with dissolve
    show player 16
    player_name "( ... )"
    player_name "( You're gonna get yours one day, {b}Dexter{/b}. )"
    hide player with dissolve
    return

label school_roxxy_assignment:
    scene school
    show teacher 18f at left
    show roxxy 33 zorder 1 at right
    with dissolve
    rox "No, {b}Miss Bissette{/b}! I'm begging you here!"
    rox "Please, don't fail me!"
    show roxxy 32
    show teacher 19f
    bis "I have been telling you, silly girl!"
    bis "Turning in other student's work is inexcusable!"
    bis "I am sick of saying these things!"
    show teacher 18f
    show roxxy 33
    rox "C'mon! There's gotta be something I can do!"
    rox "Just give me one more chance!"
    show roxxy 32
    show teacher 3f
    bis "Hah!"
    show teacher 19f
    bis "I have given you many chances already!"
    show teacher 18f
    show roxxy 33
    rox "I'll study and do the work myself this time."
    rox "I promise!"
    rox "Just one more chance!"
    show roxxy 32
    show teacher 20f
    bis "..."
    show player 13f zorder 0 at Position (xpos=650) with dissolve
    show teacher 2f
    bis "Oh, {b}[firstname]{/b}!"
    bis "This is good timing, yes?!"
    show teacher 5f
    bis "{b}Roxanne{/b} here was just caught trying to hand in {b}your homework{/b}!"
    show teacher 19f
    bis "... This, after I tell her, \"I fail you, if you do this again!\""
    bis "Now she is wanting yet another chance!"
    show teacher 5f
    bis "What say you?"
    bis "Should I to be giving her this chance?"
    show teacher 4f
    rox "..."
    show player 11f
    player_name "..."
    show player 10f
    player_name "I uhh..."
    player_name "... Yes?"
    show player 5f
    show teacher 20f
    bis "Hmm..."
    pause
    show teacher 2f
    bis "Tsk, you are too kind hearted, {b}[firstname]{/b}!"
    show teacher 12f
    bis "... But you are also too cute to refuse!"
    show roxxy 1e
    show player 13f
    bis "Very well."
    show teacher 19f
    bis "This is to be your last chance {b}Roxanne{/b}!"
    show teacher 18f
    show roxxy 1d
    rox "Phew, thank you!"
    show roxxy 1e
    show teacher 19f
    bis "... And to make sure you do things right..."
    show teacher 3f
    bis "{b}[firstname]{/b} here is going to be your study partner!"
    show player 22f
    show teacher 1f
    show roxxy 3c with dissolve
    rox "What?!"
    rox "No freaking way that is happening!"
    show roxxy 3d
    show teacher 3f
    bis "Ah ah ah!"
    show teacher 2f
    bis "What has become of your, \"I will do anything!\" Hmm?"
    show teacher 1f
    show roxxy 2
    rox "... Yeah, but..."
    show roxxy 3c
    rox "... Why him?!"
    show roxxy 14
    if M_bissette.is_state(S_bissette_end):
        show teacher 12f
        bis "{b}[firstname]{/b} here is my best student!"
        bis "Who better to help you with your studies, yes?"
        show teacher 13f
    else:
        show teacher 2f
        bis "{b}[firstname]{/b} is trying to make up work as well."
        bis "It seems fitting you should be helping one another to catch up, yes?"
        show teacher 1f
    show player 10f
    player_name "I really have to do this?"
    show player 5f
    show teacher 2f
    bis "It was your idea to be giving her another chance!"
    bis "I expect you to make sure she really does the studying!"
    show teacher 1f
    show player 24f
    player_name "{b}*Sigh*{/b}"
    player_name "Okay..."
    show teacher 3f
    bis "Tres Bien!"
    show teacher 2f
    bis "I leave you to it!"
    hide teacher with dissolve
    show player 5 at left with dissolve
    show roxxy 29
    rox "..."
    player_name "..."
    show roxxy 30
    rox "Ugh, this sucks!"
    show roxxy 29
    show player 10
    player_name "Just relax... It won't be that bad."
    player_name "I'll just swing by your place later and we'll get it over with quickly..."
    show player 5
    show roxxy 2
    rox "You want to come to my place?"
    show roxxy 3
    rox "I don't want you there!"
    show roxxy 3d
    show player 10
    player_name "Would you rather go to the library or something?"
    show player 5
    show roxxy 3c
    rox "... And be seen in public with YOU..."
    rox "Eww, no."
    show roxxy 14
    show player 12
    player_name "Well then..."
    show player 11
    dex "Hey, {b}Missy{/b}! You seen {b}Roxxy{/b} today?!"
    missy "Yeah, she was on her way to see {b}Miss Bissette{/b}..."
    show roxxy 2b
    rox "!!!" with hpunch
    show roxxy 2c
    rox "Oh shit!"
    rox "Umm..."
    rox "Hide!"
    scene expression "backgrounds/location_school_cutscene03.jpg"
    with fade
    show text "Before I knew what was happening {b}Roxxy{/b} had flung open my locker and shoved me inside." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene school
    show roxxy 7f at left
    show dexter 8 at right
    with dissolve
    dex "There you are."
    show dexter 2
    show roxxy 11f with dissolve
    rox "... Yeah, I'm here. What's up?"
    show roxxy 9f
    show dexter 8
    dex "Just thought I'd see if you were ready to apologize yet?"
    show dexter 2
    show roxxy 11f
    rox "Pfft, apologize for what?"
    show roxxy 9f
    show dexter 6 with dissolve
    dex "You know what!"
    dex "You called me names!"
    show dexter 2
    show roxxy 11f
    rox "You mean stupid?"
    dex "..."
    show roxxy 5f with dissolve
    rox "Well, don't act so stupid and I won't call you stupid... stupid."
    show roxxy 6f with dissolve
    dex "Grrr..."
    show dexter 6
    dex "STOP CALLING ME STUPID!" with hpunch
    show dexter 5
    show roxxy 10f with dissolve
    rox "... Or what?"
    show roxxy 7f with dissolve
    show dexter 2 with dissolve
    dex "..."
    show dexter 8
    dex "You're lucky you're my girlfriend!"
    dex "If anybody else talked to me like this..."
    show dexter 4
    dex "I'd smash their faces in!" with hpunch
    show dexter 2
    show roxxy 11f
    with dissolve
    rox "Uh huh."
    rox "Are you done whining?"
    show roxxy 9f
    show dexter 8
    dex "Whatever."
    dex "You'll apologize eventually."
    show dexter 6 with dissolve
    dex "Just remember. Until you do, don't ask me for nothin'!"
    show dexter 2 with dissolve
    show roxxy 10f
    rox "Like I need anything from you!"
    rox "You'd probably just screw it up, even if I did!"
    show roxxy 6f with dissolve
    dex "..."
    show dexter 4 with dissolve
    dex "Rrraaaggh!!!" with hpunch
    show dexter 6 with dissolve
    dex "You're such a bitch!"
    hide dexter with dissolve
    show roxxy 7f
    rox "..."
    show roxxy 1b at right with dissolve
    rox "Alright, come on out, {b}[firstname]{/b}."
    show roxxy 1
    pause
    show player 12 at left with dissolve
    player_name "Is it really a good idea to antagonize him like that?"
    show player 5
    show roxxy 1b
    rox "Huh?"
    show roxxy 3c
    rox "Whatever. Fuck him! He's a dick!"
    show roxxy 3d
    show player 10
    player_name "Yeah, but he's not exactly the most stable person in the world..."
    player_name "Why are you dating him anyways?"
    show player 12
    player_name "You're like, way out of his league!"
    show player 5
    show roxxy 2
    rox "Pfft, please. I'm way out of everyone's league!"
    rox "Dating {b}Dexter{/b} means nobody else messes with me."
    show roxxy 1h
    rox "It's just easier."
    show roxxy 1g
    show player 10
    player_name "Yeah, but he's so..."
    show player 5
    show roxxy 2
    rox "... Stupid?"
    show roxxy 1
    show player 17
    player_name "Haha, yeah!"
    show player 13
    show roxxy 4
    rox "Hahaha!"
    show roxxy 1
    pause
    show player 11
    player_name "..."
    rox "..."
    show player 10
    player_name "{b}*Ahem*{/b} So... I guess {b}I'll come around your place tonight{/b}?"
    show player 5
    show roxxy 30
    rox "{b}*Sigh*{/b} Fine."
    rox "Just don't expect much from me with the studying. It's not my strong suit."
    show roxxy 29
    show player 14
    player_name "No worries. I'll show you the ropes!"
    show player 13
    rox "..."
    show player 36 with dissolve
    player_name "See ya {b}tonight{/b}."
    show player 13
    show roxxy 30
    rox "... Uh huh."
    show roxxy 29
    hide player with dissolve
    rox "..."
    pause
    show roxxy 1g
    pause
    return

label school_roxxy_missing_outfit:
    scene school
    show becca 1 at Position(xpos=315)
    show missy 2b at left
    show roxxy 3c zorder 1 at right
    with dissolve
    rox "... Ugh, did you two find it?"
    show roxxy 3b
    show becca 2
    becca "Nope."
    show becca 1
    show missy 2
    missy "Are you sure you didn't leave it at home?"
    show missy 2b
    show roxxy 3c
    rox "Of course I'm sure, {b}Missy{/b}!"
    rox "What, do I look like an idiot or something?"
    show roxxy 3b
    show becca 3
    show missy 1b
    missy "I didn't say that!"
    show missy 3
    show becca 3b
    becca "You might as well have..."
    show becca 3
    show missy 2
    missy "I'm just trying to help!"
    show missy 2b
    show becca 4
    becca "Hahaha, worst help ever!"
    show becca 5
    show roxxy 30
    rox "{b}*Sigh*{/b} I don't suppose one of you brought an extra uniform?"
    show roxxy 29
    show becca 2
    becca "Nope. My back-up is in the wash."
    show becca 3
    show missy 1b
    missy "Yeah, I didn't bring mine either."
    show missy 1
    show becca 8
    becca "With {b}Missy's{/b} tiny tits, her uniform wouldn't fit you anyways..."
    show becca 7
    show missy 4
    missy "Shuddup, Skank!"
    show missy 2b
    show becca 4
    becca "Hahaha, don't worry. You'll hit puberty someday..."
    show becca 5
    show roxxy 3c
    rox "{b}*Sigh*{/b} You two are worthless, you know that?"
    show roxxy 3b
    show becca 2
    becca "Pssh, whatever."
    show becca 1
    show missy 2
    missy "It's not our fault you left your uniform at home!"
    show missy 2b
    show roxxy 30
    rox "I guess, we'll just have to go and get it."
    show roxxy 3b
    show becca 2b with dissolve
    becca "What?!"
    becca "You want us to walk to your place right now?!"
    show becca 1 with dissolve
    show missy 2
    missy "Yeah, fuck that!"
    show missy 2b
    show roxxy 3c
    rox "C'mon you dumb bitches!"
    rox "I don't wanna walk there all by myself!"
    show roxxy 3b
    show missy 2
    missy "No way!"
    missy "If I skip another French lesson, {b}Miss Bissette{/b} is going to write my parents..."
    show missy 2b
    show becca 3b
    becca "Ooh, your mom would totally whoop your ass if that happened!"
    show becca 3
    show missy 1b
    missy "I know, right?"
    show missy 1
    show roxxy 2
    rox "Fine, we'll just go without you... Right, {b}Becca{/b}?"
    show roxxy 1
    show becca 2b with dissolve
    becca "..."
    show roxxy 3b
    rox "Seriously?!"
    show roxxy 3c
    show becca 2 with dissolve
    becca "It's too hot to walk all the way to your place!"
    becca "... And besides, your cousin freaks me out."
    show becca 1
    show roxxy 31
    show missy 2b
    rox "You guys suck!"
    show roxxy 3d
    show player 14f zorder 0 at Position (xpos=600) with dissolve
    player_name "Hey, girls!"
    player_name "What's going on?"
    show player 13f
    show becca 2
    becca "... Umm, why are you talking to us?"
    show becca 1
    show player 11f
    show missy 1b
    missy "Nerd alert!"
    show missy 1
    show roxxy 27 with dissolve
    rox "..."
    show player 5 with dissolve
    show roxxy 28
    rox "I forgot my {b}Cheerleading Uniform{/b} at home."
    show roxxy 1n
    rox "... And \"my friends\" here, are too good to go with me to get it."
    show roxxy 1m
    show player 5f with dissolve
    show missy 1b
    missy "Hey, I totally would if it wasn't for {b}Miss Bissette{/b}!"
    show missy 1
    show roxxy 1n
    rox "... Whatever."
    show roxxy 1m
    show player 10 with dissolve
    player_name "I'll go with you."
    show roxxy 1k
    player_name "... You know, if you want?"
    show player 5
    show roxxy 1i
    show becca 2b with dissolve
    becca "Eww..."
    becca "Why would she want to go anywhere with you, geek boy?!"
    show becca 1 with dissolve
    show roxxy 1j
    rox "..."
    pause
    show roxxy 1l
    rox "... Fine, let's go."
    show roxxy 1k
    show player 13
    show becca 2b with dissolve
    becca "WHAT!?!"
    becca "You're seriously going with this loser?"
    show becca 1
    show roxxy 3
    with dissolve
    rox "Well, I don't wanna walk across town on my own!"
    rox "... And since you two slutbags won't come..."
    show roxxy 3c
    show player 5
    rox "... What choice to do I have?"
    show roxxy 3b
    show becca 2
    show player 5f with dissolve
    becca "Yeah but I mean... Just look at him..."
    becca "... He's so..."
    show becca 1
    show missy 8
    missy "... Losery?"
    show missy 7
    show becca 4
    becca "Haha, yeah!"
    show becca 5
    show missy 3
    show player 12f
    player_name "That's not even a word!"
    show player 90f
    show roxxy 3c
    rox "Ugh, would you two shuddup already?!"
    rox "C'mon, {b}[firstname]{/b}. Let's get this over with."
    hide roxxy with dissolve
    player_name "..."
    show player 12f
    player_name "... See ya, slutbags!"
    hide player with dissolve
    show becca 1
    becca "..."
    show becca 3
    show missy 6
    missy "Pfft, hahaha!"
    show missy 7
    show becca 2f at Position (xpos=400) with dissolve
    becca "What are you laughing at?!"
    show becca 1f
    show missy 6
    missy "... That nerd just called you a slutbag!"
    show missy 7
    show becca 2f
    becca "Umm, he called both of us slutbags, moron."
    show becca 1f
    show missy 3
    missy "..."
    show missy 5
    missy "Oh, right..."
    show missy 4
    missy "Hey, don't call me moron, you twat!"
    scene black with fade
    return

label school_roxxy_return_to_school:
    scene school
    show player 14 at Position (xpos=500)
    show roxxy 23 at right
    show roxxy_outfit cheer at right
    with dissolve
    player_name "Looks like we made it back in time."
    show player 13
    show roxxy 24
    rox "... Thanks for your help today."
    show roxxy 23
    show player 14
    player_name "Not a problem, {b}Roxxy{/b}!"
    show player 13
    show becca 5 at Position(xpos=315)
    show becca_outfit cheer at Position (xpos=315)
    show missy 1b at left
    show missy_outfit cheer at left
    with dissolve
    show player 13f at Position (xpos=600) with dissolve
    missy "Hey, you found it?!"
    show missy 1
    show becca 6
    becca "... Uhh, obviously."
    becca "She's wearing it, isn't she?"
    show becca 5
    show missy 2
    missy "Oh, shuddup!"
    show missy 2b
    show becca 8
    becca "What's the geek still doing here?"
    show becca 7
    show player 5f
    show roxxy 23b
    rox "... Don't call him names."
    show roxxy 23
    show becca 2
    becca "Huh?"
    show becca 1
    show roxxy 24
    rox "... He's a nice guy."
    show roxxy 23
    show becca 8
    becca "What, are you in love with him now or something?"
    show becca 7
    show roxxy 23c
    rox "Pfft, no!"
    show roxxy 24
    rox "He just helped me out of a jam today is all and I think you should be nicer to him."
    show roxxy 23
    show becca 4
    becca "Hah, whatever!"
    show becca 8
    becca "I think you've got a little crush on {b}[firstname]{/b}!"
    show becca 4
    becca "Haha!"
    show becca 8
    becca "What do you think, {b}Missy{/b}?"
    show becca 7
    show missy 8
    missy "... Yeah, he's kinda cute."
    show missy 7
    show becca 3
    becca "!!!" with hpunch
    show becca 3b
    show missy 3
    becca "That's not what I meant!"
    show becca 2
    becca "What's the matter with you two?!"
    show becca 1
    show missy 1
    rox "..."
    show becca 2
    becca "Ugh, I'm going to practice!"
    hide becca
    hide becca_outfit cheer
    with dissolve
    show missy 2
    missy "{b}Becca{/b}, hold up!"
    missy "... I didn't understand the question!"
    hide missy
    hide missy_outfit cheer
    with dissolve
    rox "..."
    show player 10 at Position (xpos=500) with dissolve
    player_name "... Thanks for saying that."
    show player 13
    show roxxy 23b
    rox "Huh?"
    show roxxy 24
    rox "Oh, right."
    rox "Whatever."
    rox "Don't let it go to your head!"
    show roxxy 23b
    rox "I don't like you or anything. I just appreciate your help is all."
    show roxxy 23
    show player 14
    player_name "O-okay."
    player_name "I guess I'll see you around."
    show player 13
    show roxxy 24
    rox "Yeah, we'll see..."
    hide roxxy
    hide roxxy_outfit cheer
    with dissolve
    player_name "( Well, that was a crazy day... )"
    player_name "( I think {b}Roxxy{/b} is actually starting to warm up to me! )"
    show player 18
    player_name "( I should look for more opportunities to get close with her. )"
    return

label school_roxxy_trailer_park_trouble:
    scene school
    show annie 3 at right
    show roxxy 3df zorder 1 at left
    with dissolve
    ann "The student handbook is very clear on this matter!"
    ann "Students are not allowed to have their cellphones out while on school property."
    show annie 1
    show roxxy 3f
    rox "Go away, you psychotic little brown noser!"
    show roxxy 3df
    show player 10f zorder 0 at Position (xpos=500) with dissolve
    player_name "What's going on?"
    show player 5f
    show roxxy 3f
    rox "I'm having a crisis here!"
    show roxxy 3df
    show player 5 at Position (xpos=400) with dissolve
    show annie 5
    ann "Irrelevant!"
    ann "No cell phones on school property and this is school property!"
    show annie 3
    ann "You have to put it away!"
    show annie 1
    show roxxy 3f
    rox "Back off, {b}Annie{/b} or I swear I'm going to pop you one, right in the face!"
    show roxxy 3bf
    show annie 5
    ann "Pfft, you don't frighten me..."
    show annie 6
    ann "..."
    show annie 5
    ann "... I'm getting {b}Principal Smith{/b}!"
    hide annie with dissolve
    show roxxy 3df
    show player 10f at Position (xpos=600) with dissolve
    player_name "What happened?"
    show player 5f
    show roxxy 33f
    rox "Apparently, the cops just showed up and arrested {b}my mom{/b}!"
    show roxxy 32f
    show player 10f
    player_name "What?!"
    player_name "Why would they do that?"
    show player 11f
    show roxxy 33f
    rox "I don't know!"
    rox "I've gotta get home..."
    show roxxy 32f
    player_name "..."
    show player 10f
    player_name "You want me to walk with you?"
    show player 5f
    show roxxy 32f
    rox "..."
    show roxxy 1lf
    rox "You'd really do that?"
    show roxxy 32f
    show player 10f
    player_name "... Sure, I don't mind!"
    show player 5f
    rox "..."
    show roxxy 1lf
    rox "Thanks, {b}[firstname]{/b}."
    rox "C'mon, let's get out of here before {b}Annie{/b} comes back."
    show roxxy 32f
    show player 12f
    player_name "Right behind you."
    hide roxxy
    hide player
    with dissolve
    return

label school_roxxy_selling_meth_ask_roxxy:
    scene school
    show roxxy 14f at Position (xpos=500)
    show becca 1 at Position(xpos=315)
    show missy 1 at left
    show player 14f at right
    with dissolve
    player_name "Hey {b}Roxxy{/b}, I need to speak with you!"
    show player 13f
    show becca 2
    becca "Ugh, get lost loser!"
    show becca 1
    show missy 2
    missy "Yeah, can't you see she has enough problems?!"
    show missy 2b
    show player 14f
    player_name "I think I found a way to fix all of this!"
    show player 13f
    show missy 2
    missy "Pfft, yeah right!"
    show missy 2b
    show becca 2
    becca "What's a nerd like you going to do?"
    show becca 1
    show roxxy 29f
    show player 12f
    player_name "Can I please just talk to you for a second?"
    show player 90f
    show becca 2
    becca "I said get lost!"
    show becca 1
    show missy 2
    missy "Yeah, ge-"
    show missy 3
    show roxxy 30f
    rox "Would you two shut up already!"
    show player 11f
    rox "*Sigh* Just go on to class, I wanna hear him out."
    show roxxy 29f
    show player 13f
    show becca 2b with dissolve
    becca "You're serious?"
    show becca 1
    show roxxy 3 at Position (xpos=600)
    with dissolve
    rox "Just go!"
    show roxxy 3b
    show missy 2b
    show becca 2
    becca "Tch, Fine!"
    show becca 3b
    becca "C'mon {b}Missy{/b}!"
    hide becca
    hide missy
    with dissolve
    pause
    show roxxy 3cf at Position (xpos=500) with dissolve
    rox "So how exactly are you gonna fix all this?"
    show roxxy 3df
    show player 14f
    player_name "Well, I convinced {b}Clyde{/b} to turn himself in!"
    show player 13f
    show roxxy 30f
    rox "... Great."
    show roxxy 3df
    show player 5f
    player_name "..."
    show player 10f
    player_name "That's it?"
    show player 5f
    show roxxy 3cf
    rox "Did you forget?"
    rox "Even if he confesses, {b}my mom{/b} will stay in jail until her trial."
    rox "We'll still lose the trailer."
    show roxxy 3df
    show player 14f
    player_name "Well, I've got a plan for that as well!"
    player_name "{b}Clyde{/b} says he's got more than enough Meth to make $50,000 dollars!"
    show player 13f
    show roxxy 2f
    rox "Pfft, {b}Clyde{/b} says..."
    show roxxy 3cf
    show player 5f
    rox "That moron can barely tie his shoes!"
    rox "... And you think he can really sell all that Meth?!"
    show roxxy 3df
    player_name "..."
    show player 10f
    player_name "Doesn't he do it all the time?"
    show player 5f
    show roxxy 4f
    rox "Hahaha! Are you kidding me?"
    show roxxy 3cf
    rox "He cooks it but {b}my mom{/b} does all the selling!"
    show roxxy 3df
    show player 11f
    player_name "..."
    show roxxy 2bf
    rox "!!!"
    show roxxy 3cf
    rox "I never said that! Understand!"
    show roxxy 3df
    show player 10f
    player_name "Don't worry, I'm not gonna tell anybody."
    show player 5f
    show roxxy 30f
    rox "Look, I appreciate you trying to help, {b}[firstname]{/b}."
    show roxxy 3cf
    rox "... But you're better off just forgetting about me and my problems!"
    hide roxxy with dissolve
    player_name "..."
    show player 4f
    player_name "( Well, now what? )"
    player_name "( I guess I should head {b}back to Clyde{/b}... )"
    hide player with dissolve
    return

label school_roxxy_shut_down_lab:
    scene school
    show roxxy 32f at Position (xpos=500)
    show becca 2 at Position(xpos=315)
    show missy 1 at left
    show player 13f at right
    with dissolve
    becca "Ugh, back again?"
    show becca 1
    show missy 2
    missy "What do you want now, loser?!"
    show missy 2b
    show player 5f
    show roxxy 30f at Position (xoffset=34)
    rox "Oh. My. God."
    show roxxy 3 at Position (xpos=600) with dissolve
    rox "Would you two just cut it out?"
    rox "I'm not in the mood for all of this."
    show roxxy 3d
    show missy 3
    missy "..."
    show becca 2
    becca "... So what? We're supposed to be nice to this nerd now?"
    show becca 1
    show roxxy 3c
    rox "Just let us talk."
    show roxxy 3d
    show player 13f
    show becca 2
    becca "Fine."
    show becca 3b
    becca "C'mon, {b}Missy{/b} let's leave {b}Roxxy{/b} and her nerdy little boy toy to chat."
    hide becca with dissolve
    show roxxy 3c
    rox "Ugh, quit being a bitch, {b}Becca{/b}!"
    show roxxy 3d
    show missy 1b
    missy "Hey, wait for me!"
    hide missy with dissolve
    pause
    show roxxy 3cf at Position (xpos=500) with dissolve
    rox "What do you want, {b}[firstname]{/b}."
    show roxxy 3df
    show player 14f
    player_name "I brought you something!"
    show player 239_240f with dissolve
    pause
    show player 650f with dissolve
    pause
    show roxxy 68bf
    show player 13f
    with dissolve
    rox "..."
    show roxxy 68cf
    rox "God he's dumb."
    show roxxy 1f f with dissolve
    show player 14f
    player_name "Heh, yeah..."
    show player 13f
    show roxxy 2f
    rox "I thought I told you to forget about all this?"
    show roxxy 1f f
    show player 14f
    player_name "Yeah, you did."
    show player 13f
    show roxxy 2f
    rox "So why are you still-"
    show roxxy 2bf
    show player 14f
    player_name "I brought you something else too!"
    show player 239_240f with dissolve
    pause
    show player 638bf
    rox "!!!" with hpunch
    show roxxy 80f at Position (xoffset=47)
    show player 13f
    with dissolve
    pause
    show roxxy 82f at Position (xoffset=47)
    rox "Holy shit!"
    rox "I've never seen this much money before!"
    rox "How did you..."
    show roxxy 81f at Position (xoffset=47)
    show player 14f
    player_name "Clyde and I sold the Meth last night."
    show player 13f
    show roxxy 82f at Position (xoffset=47)
    rox "Are you serious?!"
    show roxxy 81f at Position (xoffset=47)
    show player 14f
    player_name "Yeah. We made $60,000!"
    player_name "That should be plenty to bail {b}your mom{/b} out... Right?"
    show player 13f
    show roxxy 80f at Position (xoffset=47)
    rox "..."
    show roxxy 1bf with dissolve
    rox "I can't believe you did all this!"
    show roxxy 1f f
    rox "..."
    show roxxy 1bf
    rox "{b}[firstname]{/b}, why are you doing all this?!"
    rox "You don't owe me anything and I've only ever been mean to you."
    show roxxy 1f f
    show player 14f
    player_name "... Cause it's the right thing to do."
    show player 13f
    show roxxy 1if at Position (xoffset=-34) with dissolve
    rox "..."
    show roxxy 1lf at Position (xoffset=-34)
    rox "I don't know what to say..."
    show roxxy 1kf
    show player 14f
    player_name "You don't have to say anything."
    player_name "Just go and get your home back."
    show player 13f
    pause
    hide player
    show roxxy 59f at right
    player_name "!!!" with hpunch
    rox "Thank you, {b}[firstname]{/b}!"
    rox "I'm not going to forget this!"
    hide roxxy
    show roxxy 1f f at Position (xpos=500)
    show player 14f at right
    with dissolve
    player_name "... No problem!"
    show player 13f
    show roxxy 1bf
    rox "I'd better get down to the station and get {b}Mom{/b} out!"
    rox "I'll talk with you soon, okay?"
    show roxxy 1f f
    show player 14f
    player_name "Alright. Good luck!"
    show player 13f
    hide roxxy with dissolve
    pause
    hide player
    show player 17f
    with dissolve
    player_name "( Wow! )"
    player_name "( {b}Roxxy{/b} just hugged me in public! )"
    show player 13f
    player_name "( Well, sorta... Nobody was around to see it... )"
    player_name "( ... But it's still progress! )"
    player_name "( I should look for more opportunities to spend time with her once things settle down! )"
    hide player with dissolve
    return

label school_roxxy_give_exams:
    scene school
    show player 14 at left
    show roxxy 1 at right
    with dissolve
    player_name "Hey, {b}Roxxy{/b}!"
    show player 17
    player_name "I've got something for you?"
    show player 13
    show roxxy 1b
    rox "You mean..."
    rox "You have the exams?"
    show roxxy 1
    show player 14
    player_name "Heh, yeah!"
    player_name "She was keeping them in her bedroom, can you believe that?!"
    show player 239_240 with dissolve
    pause
    show player 643 with dissolve
    pause
    hide player
    show roxxy 59 at left
    with dissolve
    rox "Oh my god, you're the best {b}[firstname]{/b}!"
    player_name "!!!" with hpunch
    show roxxy 64b at right
    show player 14 at left
    with dissolve
    player_name "Err, thanks..."
    show player 13
    show roxxy 64c
    rox "You know..."
    rox "I really like a guy who isn't afraid to stick their neck out for their girl."
    show roxxy 64b
    show player 10
    player_name "... M-my girl?"
    show player 5
    show roxxy 2b with dissolve
    rox "!!!"
    show roxxy 2c
    rox "I mean, not to say... I'm your girl or anything..."
    show roxxy 1
    show player 3 with dissolve
    player_name "..."
    show roxxy 2
    rox "Heh, that would be crazy, right?"
    show roxxy 1
    show player 29
    player_name "Oh, I don't kno-"
    show player 3
    show roxxy 2
    rox "I mean, could you imagine you and I?"
    rox "... Dating?"
    show roxxy 1
    show player 24 with dissolve
    player_name "..."
    rox "..."
    show player 26
    player_name "I uhh..."
    show player 11
    show roxxy 2b
    ann "You really think one of the students is responsible?"
    smi "... Well who else would break into my house and steal only the exams?!"
    show roxxy 2c
    rox "Oh shit!"
    rox "{b}Principal Smith{/b} is coming!"
    show roxxy 2b
    show player 10
    player_name "You can't let her see those exams!"
    player_name "We gotta get out of here!"
    show roxxy 2c at left
    show player 11f at Position (xpos=400)
    with dissolve
    rox "There's no time!"
    show roxxy 2b
    show player 10f
    player_name "What are you-"
    show player 11f
    show roxxy 3c
    rox "{b}Shut up and get over here!!!{/b}"
    show roxxy 3d
    show player 22f
    player_name "!!!"
    scene black with fade
    scene expression "backgrounds/location_school_cutscene04.jpg"
    with fade
    show text "... And just like that I was dragged into my locker by {b}Roxxy{/b}!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene school
    show principal 26f at left
    show principal 26f at Position (xoffset=70)
    show annie 3 at right
    with dissolve
    ann "So what's the plan?"
    show annie 1
    show principal 4f with dissolve
    smi "We have to get those exams back! If the board finds out about this, it could mean the end of everything I've built here!"
    show principal 26f at Position (xoffset=70) with dissolve
    show annie 3
    ann "Don't worry, ma'am. That's not going to happen!"
    show annie 1
    show principal 27f at Position (xoffset=70)
    smi "Of course it's not going to happen! You're gonna find those exams and bring those responsible to me for punishment!"
    show principal 26f at Position (xoffset=70)
    show annie 3
    ann "... Yes, ma'am."
    show annie 1
    show principal 27f at Position (xoffset=70)
    smi "Start by searching these lockers."
    smi "The little shit might have stashed them in there."
    show principal 26f at Position (xoffset=70)
    show annie 3
    ann "Right away, ma'am!"
    show annie 1
    show principal 4f with dissolve
    smi "... And don't fail me, {b}Annie{/b}!"
    smi "You know what happens when I'm displeased..."
    show principal 26f at Position (xoffset=70) with dissolve
    show annie 6
    ann "..."
    show annie 5
    ann "I won't fail you, ma'am."
    show annie 6
    show principal 27f at Position (xoffset=70)
    smi "Very good."
    smi "Now get to work!"
    hide annie
    hide principal
    with dissolve
    scene expression "backgrounds/location_school_locker_inside01.jpg"
    show player locker 3
    show roxxy locker 1

    player_name "!!!"
    show player locker 1
    player_name "{b}Annie is searching the lockers!{/b}"
    player_name "We're totally screwed!"
    show player locker 2
    show roxxy locker 2
    rox "Shh!!!"
    rox "Be quiet!"
    show roxxy locker 3
    rox "... And stop squirming around!"
    show roxxy locker 1
    show player locker 1
    player_name "Sorry, I'm just freaking out!"
    player_name "We're gonna get expelled for this, you know?!"
    show player locker 2
    show roxxy locker 2
    rox "Would you just calm down!"
    show roxxy locker 1
    show player locker 4
    player_name "..."
    show player locker 7
    player_name "Sorry..."
    show player locker 2
    "Clang!"
    show player locker 3
    pause
    ann "Eugh, what are these crusty tissues?!"
    show player locker 1
    player_name "She's getting closer!"
    show player locker 8
    "Clang!"
    show player_boner locker 1 with dissolve
    pause
    show roxxy locker 2
    rox "Hey! You're poking-"
    show player locker 9
    show player_boner locker 2
    show roxxy locker 4
    rox "!!!" with hpunch
    show roxxy locker 3
    rox "What is that?!"
    rox "Don't tell me that's your-"
    show roxxy locker 4
    show player locker 5
    player_name "..."
    "Clang!"
    show player locker 3
    show roxxy locker 6
    rox "Is your dick hard right now?!"
    show roxxy locker 5
    show player locker 7
    player_name "I-I can't help it..."
    show player locker 5
    show roxxy locker 7
    rox "How can you be turned on right now?!"
    show roxxy locker 5
    show player locker 7
    player_name "I don't know! I can't exactly control it!"
    show player locker 5
    show roxxy locker 7
    rox "Well, try hard-"
    show roxxy locker 8
    hide player_boner
    rox "{b}*Gasp*{/b}"
    rox "It's touching my-"
    show roxxy locker 9
    show player locker 2
    player_name "Stop moving!"
    show player locker 1
    show roxxy locker 8
    "Clang!"
    $ M_roxxy.set('sex speed', .6)
    show roxxy locker 8_9
    show player locker 9
    player_name "You're making it worse!!"
    show player locker 8
    rox "... It's touching my Pu-"
    show player locker 9
    player_name "{b}Roxxy{/b} stop moving!"
    show player locker 3
    player_name "... Oh crap."
    player_name "I think we're the next locker..."
    show player locker 9
    player_name "You have to stop grinding on me!"
    show player locker 8
    $ M_roxxy.set('sex speed', 2)
    show roxxy locker 8_9
    rox "Ahh... Fuuu..."
    pause
    jud "{b}Annie!{/b}"
    show player locker 3
    jud "I need help opening my locker..."
    ann "Ugh, seriously?"
    ann "You are such a pain in my ass."
    jud "I know, I'm sorry..."
    ann "This is the last time!"
    jud "..."
    jud "Why are you searching everyone's locker anyways?"
    show player locker 4
    ann "Just you nevermind that!"
    pause
    ann "Alright, it's open. Get your stuff and-"
    ann "Your locker is mess!"
    show player locker 8
    jud "..."
    ann "This is disgusting..."
    ann "What's the matter with you?!"
    jud "I just-"
    ann "Keeping food in your locker is strictly forbidden!"
    show player locker 3
    ann "I'm gonna have to write you up for this..."
    jud "... But-"
    ann "No excuses, c'mon!"
    ann "I'm taking you to {b}Principal Smith{/b} right away!"
    show player locker 9
    ann "I bet punishing you will cheer her up!"
    jud "P-punishment?"
    ann "Move it!"
    jud "... What kind of punishment?!"
    pause
    $ M_roxxy.set('sex speed', .4)
    show roxxy locker 8_9
    rox "Mmm..."
    show player locker 7
    player_name "{b}*Huff*{/b} You gotta... Stop."
    player_name "I think {b}Annie{/b} is... {b}*Puff*{/b}... Annie is leaving!"
    show player locker 8
    rox "Ahh!"
    show player locker 7
    player_name "{b}Roxxy{/b}?"
    player_name "What are you doing?! We've gotta go!"
    show player locker 9
    rox "Shuddup! Shuddup! Shuddup!"
    $ M_roxxy.set('sex speed', .2)
    show roxxy locker 8_9
    player_name "What's gotten into-"
    show player locker 9
    show roxxy locker 10
    rox "Ngghhh!" with flash
    show player locker 8
    player_name "!!!" with hpunch
    rox "Haah... Haah..."
    rox "Holy shit!"
    rox "That was..."
    show player locker 5
    player_name "..."
    show player locker 6
    player_name "{b}Roxxy{/b} we gotta get out of here before {b}Annie{/b} comes back!"
    show player locker 5
    show player_boner locker 2
    show roxxy locker 2
    with dissolve
    rox "Y-yeah... Okay."
    rox "Just... Help me out. My legs are like jello right now..."
    scene black with fade
    scene school
    show roxxy 1k at right
    show player 10 at left
    with dissolve
    player_name "That was too close!"
    show player 5
    rox "..."
    show roxxy 1l
    rox "Phew, that was..."
    show roxxy 1m
    pause
    show roxxy 86 at left
    hide player with hpunch
    pause
    show roxxy 3b at right
    show player 15 at left
    with dissolve
    player_name "Ouch!"
    show player 12
    player_name "What was that for?!"
    show player 90
    show roxxy 3c
    rox "Who the hell gets a boner at a time like that?!"
    show roxxy 3d
    show player 10
    player_name "I don't know?!"
    player_name "It just happened!"
    show player 12
    player_name "You're the one who wouldn't stop grinding on it!"
    show player 90
    show roxxy 3b
    pause
    show roxxy 86 at left
    hide player
    rox "Shut up!" with hpunch
    show roxxy 3b at right
    show player 15 at left
    with dissolve
    player_name "Ouch! Stop punching me!"
    show player 16
    show roxxy 3
    rox "You had better not tell anybody what happened in that locker!"
    show roxxy 3c
    rox "Do you understand me?!"
    show roxxy 3b
    show player 12
    player_name "Yeah, I got it!"
    player_name "Just make sure you don't get caught with those exams..."
    show player 90
    show roxxy 3
    rox "I'll worry about the exams!"
    rox "You just focus on keeping your mouth shut!"
    rox "If anybody finds out I will absolutely die!"
    show roxxy 29f with dissolve
    show player 12
    player_name "{b}*Sigh*{/b} You are way to concerned about other peoples opinions... You know that?"
    show player 90
    show roxxy 30f
    rox "Just shut up, {b}[firstname]{/b}..."
    show roxxy 29f
    show player 12
    player_name "Fine. I've gotta get to my next class anyways..."
    player_name "See ya, {b}Roxxy{/b}."
    show player 90
    rox "..."
    show roxxy 30f
    rox "Bye."
    hide player
    hide roxxy
    with dissolve
    show roxxy 29f
    rox "..."
    show roxxy 32 with dissolve
    pause
    show roxxy 33
    rox "That felt amazing!"
    rox "... And it's so..."
    rox "... Big!"
    show roxxy 1g with dissolve
    rox "..."
    show roxxy 1h
    rox "Who would have thought he was packing something like that?!"
    show roxxy 32 with dissolve
    pause
    show roxxy 33
    rox "... Maybe I am too worried about other people's opinions..."
    rox "I mean, would it really be so bad if I started dating {b}[firstname]{/b}?"
    show roxxy 1i
    rox "..."
    show roxxy 1l
    rox "Oh my god, I just realized..."
    rox "{b}Missy{/b} was right about the nerds having big dicks thing."
    show roxxy 84 with dissolve
    rox "..."
    rox "Ugh, if she finds out I'll never hear the end of it..."
    hide roxxy with dissolve
    return

label school_roxxy_dexter_flirt:
    scene school
    show player 13f at right
    show dewitt 43 at left
    with dissolve
    dewitt "Oh, {b}[firstname]{/b}. Perfect timing!"
    show dewitt 42
    show player 14f
    player_name "Hey, {b}Miss Dewitt{/b}."
    player_name "Dang, that's a lot of records!"
    show player 13f
    show dewitt 41
    dewitt "Could you do me a favor and run these down to the auditorium for me?"
    dewitt "I'm doing a lecture on acoustics later today..."
    show dewitt 42
    show player 14f
    player_name "Sure, I don't mind."
    show player 13f
    show dewitt 43
    dewitt "Aww, thank you, sugar."
    hide dewitt
    show player 642f
    with dissolve
    pause
    player_name "( Hmm, {b}the auditorium{/b} is down the {b}right side hallway on the first floor{/b}. )"
    player_name "( {b}I should head there now.{/b} )"
    hide player with dissolve
    return

label school_roxxy_do_pushups_intro:
    scene school
    show player 13 at left
    show erik 4 at right
    with dissolve
    eri "{b}[firstname]{/b}!"
    show erik 1
    show player 14
    player_name "Hey, {b}Erik{/b}."
    player_name "What's up, man?"
    show player 13
    show erik 4
    eri "Oh, you know... The usual."
    eri "I got this sick new codpiece during a raid lastnight!"
    show erik 1
    show player 12
    player_name "Codpiece?"
    show player 13
    show erik 4
    eri "Yeah, dude. The green ladies love a good codpiece..."
    show erik 1
    show player 17
    player_name "... Haha, right on, man."
    show player 13
    show erik 4
    eri "How did things go at the bikini contest?"
    show erik 1
    show player 14
    player_name "It was so awesome!"
    player_name "You should have come with me..."
    show player 13
    show erik 4
    eri "So you got to see {b}Roxxy{/b} in a tight bikini?"
    show erik 1
    show player 14
    player_name "Oh, you have no idea!"
    player_name "She looked so sexy, man!"
    show player 13
    show erik 4
    eri "Cool!"
    eri "You really like her, huh?"
    show erik 1
    show player 14
    player_name "... Yeah. She's actually a pretty nice person."
    player_name "It's just buried under a layer of bitchiness..."
    show player 13
    show erik 4
    eri "Hahaha!"
    eri "She actually said Hi to me this morning..."
    show erik 1
    show player 12
    player_name "Really?"
    show player 13
    show erik 3b
    eri "I mean, she didn't know my name..."
    show erik 4
    eri "But hey, at least she didn't call me nerd or fat boy."
    show erik 1
    show player 14
    player_name "Heh, sorry."
    show player 13
    show erik 4
    eri "No, really! It was a big improvement."
    eri "She must really like you, {b}[firstname]{/b}!"
    show erik 1
    show player 14
    player_name "Yeah, I dunno."
    show player 13
    show erik 4
    eri "C'mon, dude."
    eri "Used to be, she wouldn't even talk to us."
    eri "Now she's inviting you out to party with her friends."
    show erik 1
    show player 5
    player_name "..."
    show player 10
    player_name "We're gonna be late for gym..."
    show player 5
    show erik 3b
    eri "Oh, shoot! You're right."
    show erik 4
    eri "C'mon, you can tell me all about the bikini contest on the way!"
    hide player
    hide erik
    with dissolve
    scene gym
    show player 13 at left
    show erik 3b zorder 1
    with dissolve
    eri "Her top snapped?!"
    show erik 1
    show player 14
    player_name "Heh, yeah."
    show player 13
    show erik 3b
    eri "Like... You saw her..."
    show erik 1
    show player 14
    player_name "Her breasts!"
    show player 13
    show erik 4
    eri "... Whoa!"
    show erik 1
    show player 14
    player_name "It's not that big a deal..."
    show player 13
    show erik 4
    eri "Yeah, right!"
    eri "That's so awesome, dude!"
    eri "I wish I could have-"
    show erik 1b
    show dexter 15 zorder 0 at right
    with dissolve
    show player 90
    dex "Beat it, fat boy."
    show dexter 14
    show erik 5b
    eri "Huh?"
    show erik 5b
    show player 12
    player_name "Leave us alone, {b}Dexter{/b}..."
    show player 90
    show dexter 15
    dex "I SAID BEAT IT, FAT BOY!"
    hide erik
    show dexter 21c
    with dissolve
    pause
    show dexter 21d with dissolve
    pause
    show dexter 14 with dissolve
    show player 15
    player_name "What the hell, man!"
    show player 16
    show dexter 15 with dissolve
    dex "Didn't I tell you to leave {b}Roxxy{/b} alone?!"
    show dexter 14
    show player 5
    player_name "..."
    show dexter 15
    dex "Now I hear you're bothering her at the beach?!!"
    show dexter 13 at Position (xoffset=-18) with dissolve
    dex "Do I need to bash your face in?!"
    show dexter 14 with dissolve
    show player 12
    player_name "Back off, {b}Dexter{/b}!"
    player_name "She invited me to come."
    show player 90
    show dexter 12 with dissolve
    dex "Psh, yeah right."
    dex "Why would she want to hang around a loser like you?"
    show dexter 11
    show player 12
    player_name "I'm the loser?!"
    player_name "You're the one who has to force himself on girls because he can't get any action..."
    show player 90
    show dexter 15 with dissolve
    dex "What the hell did you just say?!"
    show dexter 14
    show player 15
    player_name "... You heard me!"
    show player 12
    player_name "You're pathetic, {b}Dexter{/b}!"
    show player 90
    show dexter 21b at Position (xpos=950) with dissolve
    dex "You're dead, {b}[firstname]{/b}!"
    show dexter 14
    show coach 3f with dissolve
    bri "What in heck is going on here?!"
    show coach 1 with dissolve
    show dexter 11
    dex "!!!"
    show player 12
    player_name "N-nothing, ma'am."
    show player 90
    show coach 3
    bri "It doesn't look like nothing!"
    show coach 3f with dissolve
    bri "{b}Dexter{/b}, how many times do I have to tell you, not to start fights during class?!"
    show coach 1f
    show dexter 22
    dex "Yeah, but Coach... This cock roach has been-"
    show dexter 21
    show coach 4f
    bri "I don't want to hear it!" with hpunch
    bri "If you boys need to settle an arguement, then let's do it in a non-violent way..."
    show coach 1f
    show player 12
    player_name "... What, like talking?"
    show player 90
    show dexter 22
    dex "I don't understand-"
    show dexter 21
    show coach 4f
    bri "Push-ups!"
    show coach 1f
    show player 10
    player_name "Huh?!"
    show player 5
    show coach 4
    bri "Drop and give me fifty! Both of you!" with hpunch
    show coach 1
    show player 11
    player_name "!!!"
    dex "!!!"
    show coach 3
    bri "Last person standing wins the arguement!"
    show coach 1
    show dexter 12
    dex "This little twerp can't do fifty push-ups..."
    show dexter 11
    show player 12
    player_name "I bet I can do them faster than you."
    hide player with dissolve
    show dexter 12
    dex "Psh, yeah right."
    show dexter 11
    dex "..."
    hide dexter with dissolve
    pause
    show coach 5 with dissolve
    bri "Go!"
    return

label school_roxxy_trailer_park_romance_intro:
    scene school
    show player 13 at left
    show roxxy 1b at right
    with dissolve
    rox "{b}[firstname]{/b}!"
    show roxxy 1
    show player 14
    player_name "Hey, {b}Roxxy{/b}."
    player_name "What's up?"
    show player 13
    show roxxy 1b
    rox "I was waiting up for you."
    show roxxy 1
    show player 10
    player_name "You were waiting for me?"
    show player 5
    show roxxy 1b
    rox "Yeah, I figured we could walk to class together."
    show roxxy 1
    show player 12
    player_name "Really?"
    show player 14
    player_name "I mean, sure! I'd like that!"
    show player 13
    show roxxy 1b
    rox "Cool."
    show roxxy 1
    player_name "..."
    rox "..."
    show player 14
    player_name "So did you get your trophy home?"
    show player 13
    show roxxy 4
    rox "Yeah!"
    show roxxy 1b
    rox "I've got it in my room."
    rox "I still can't believe I won..."
    show roxxy 1
    show player 14
    player_name "Well, you did!"
    player_name "Those other girls didn't stand a chance!"
    show player 13
    show roxxy 1b
    rox "Heh, really?"
    show roxxy 1
    show player 14
    player_name "Of course."
    player_name "You are way out of their league!"
    show player 13
    rox "..."
    show roxxy 1b
    rox "... Thanks, {b}[firstname]{/b}."
    rox "Say, I was thinking..."
    rox "... If you aren't too busy..."
    show roxxy 1
    show player 5
    player_name "Hmm?"
    show roxxy 2
    rox "... Maybe you'd wanna hang out tonight?"
    show roxxy 1
    show player 10
    player_name "You wanna hang out, with me?"
    show player 5
    show roxxy 2
    rox "Only if you want to!"
    rox "... I just thought... Maybe... You'd come to my place?"
    show roxxy 1b
    rox "I can make you dinner!"
    rox "You know... As thanks for all your help!"
    show roxxy 1
    show player 10
    player_name "You can cook?"
    show player 5
    show roxxy 2
    rox "No, not really..."
    show roxxy 1b
    rox "... Sorry, I'm not very good at this stuff."
    show roxxy 1
    show player 5
    player_name "Hmm?"
    show player 10
    player_name "What do you mean?"
    show player 5
    show roxxy 2
    rox "... Nevermind."
    rox "Just forget I said anything."
    show roxxy 1
    return

label school_roxxy_trailer_park_romance_no:
    show player 10
    player_name "Well, I would {b}Roxxy{/b} but I've got other plans..."
    show player 5
    show roxxy 1l with dissolve
    rox "Oh, yeah. Totally..."
    rox "I've got tons of other stuff to do too."
    show roxxy 1k
    show player 12
    player_name "... Maybe another time?"
    show player 5
    show roxxy 1l
    rox "Yeah, maybe. We'll see..."
    hide roxxy with dissolve
    pause
    show player 12
    player_name "She's acting weird..."
    hide player with dissolve
    return

label school_roxxy_trailer_park_romance_yes:
    show player 10
    player_name "Wait, no!"
    show player 14
    player_name "I'll come!"
    show player 13
    show roxxy 1b
    rox "You will?!"
    show roxxy 1
    show player 14
    player_name "Definitely! I'm just surprised you asked me is all."
    show player 13
    show roxxy 2
    rox "Heh, yeah..."
    show roxxy 1
    player_name "..."
    rox "..."
    show roxxy 1b
    rox "So I guess I'll see you this {b}afternoon{/b} at {b}my place{/b}?"
    show roxxy 1
    show player 14
    player_name "Sounds good."
    show player 13
    show roxxy 4
    rox "Awesome! Don't forget!"
    show roxxy 1
    show player 14
    player_name "Heh, I won't."
    hide roxxy with dissolve
    pause
    show player 17
    player_name "( Wow, {b}dinner tonight at Roxxy's place{/b}! )"
    player_name "( I guess we're really friends now! )"
    show player 13
    player_name "( Hmm, I wonder why she was acting so weird about it though? )"
    hide player with dissolve
    return

label school_roxxy_dexter_basketball:
    scene school
    show player 5f with dissolve
    player_name "( Hmm, I don't see {b}Dexter{/b} around... )"
    player_name "( I really hope he didn't see {b}Roxxy{/b} and I making out. )"
    player_name "( He'll wanna fight for sure. )"
    show erik 4 at right
    eri "What's up, dud-"
    show erik 5
    show player 6f at left
    player_name "Whaaaa!!!" with hpunch
    show player 22 with dissolve
    eri "Whoa?!"
    show player 37 with dissolve
    eri "What the-"
    show erik 3b
    player_name "Phew, sorry man."
    show player 38
    player_name "You scared the crap out of me!"
    show player 5 with dissolve
    show erik 5
    eri "What's got you so jumpy?"
    show erik 3b
    show player 10
    player_name "{b}*Sigh*{/b} I think {b}Dexter{/b} saw me making out with {b}Roxxy{/b}..."
    show player 5
    show erik 5
    eri "!!!" with hpunch
    eri "You made out with {b}Roxxy{/b}?!"
    show erik 51
    show player 38 with dissolve
    player_name "Shh, keep it down man!"
    show player 3
    show erik 53
    eri "Sorry... Dude, this is epic news though!"
    show erik 4
    eri "My best friend is making out with the most popular girl in school!"
    show erik 1
    show player 5 with dissolve
    player_name "..."
    show player 12
    player_name "I guess you didn't hear the part where her steroid pumping, psycho of an ex-boyfriend saw us together?"
    show player 5
    show erik 3b
    eri "Oh, right."
    show erik 5
    eri "Yeah, that's not good. {b}Dexter{/b} is going to kill you, dude..."
    show erik 52
    show player 12
    player_name "I know! That's why I'm jumpy!"
    player_name "I'm keep expecting him to charge out at me every time I pass a classroom..."
    show player 5
    show erik 4
    eri "Well, no worries, dude. I've got your back!"
    eri "We can walk together and I'll make sure he doesn't sneak up on you."
    show erik 1
    show player 10
    player_name "Heh, thanks, {b}Erik{/b}..."
    show player 5
    show erik 5
    eri "Just be warned, if it comes down to a fight, I'm gonna be less than worthless..."
    player_name "..."
    show erik 3b
    eri "I'm serious, dude... Don't judge me too harshly if I pee my pants and pass out!"
    show erik 1
    show player 17
    player_name "Hahaha!"
    show player 13
    show erik 4
    eri "C'mon, we've got Gym out on the {b}basketball court{/b} today. No way, {b}Dexter{/b} tries to start a fight in front of {b}Coach Bridget{/b}."
    show erik 1
    show player 10
    player_name "Yeah, I hope you're right."
    hide player
    hide erik
    with dissolve
    scene basketball_b
    show kevin 23f at Position (xpos=500)
    show erik 52f at Position (xpos=300)
    show player 5 at left
    show coach 15b at right
    with dissolve
    bri "... Now I know you boys have probably seen the professionals on TV..."
    bri "... Dribbling between their legs and passing behind their backs!"
    show coach 15c
    bri "It's a bunch of nonsense!" with hpunch
    show coach 15b
    bri "Basketball is all about the fundamentals!"
    bri "Intelligent playcalling, precise execution-"
    show coach 15
    show kevin 32f
    kev "... And making it rain from the 3-point line!"
    show kevin 23f
    player_name "..."
    eri "..."
    show coach 15c
    bri "Oh, so this is all a big joke to you, huh?"
    show coach 15
    show kevin 34f with dissolve
    kev "{b}*Gulp*{/b} ... I didn't mean-"
    show kevin 23f with dissolve
    show coach 15b
    bri "No, no, no. It's my fault..."
    bri "... I didn't realize you were too good for basketball fundamentals..."
    show coach 15
    show kevin 34f with dissolve
    kev "That wasn't-"
    show kevin 34bf
    show coach 15c
    bri "Why don't you just run laps around the court for the rest of class instead?"
    show coach 15
    kev "!!!"
    show kevin 24f with dissolve
    kev "... But that's 57 minutes..."
    show kevin 24bf
    show coach 15b
    bri "Is that not enough?"
    bri "We can always meet here after school if you want more?"
    show coach 15
    show kevin 24f
    kev "{b}*Sigh*{/b} No, ma'am."
    show kevin 24bf
    show coach 15b
    bri "Good."
    show coach 15c
    bri "Get started!" with hpunch
    show coach 16
    hide kevin
    with dissolve
    pause
    show coach 15b with dissolve
    bri "Hmm, now where was I?"
    show coach 15
    show player 10
    player_name "{b}*Ahem*{/b} Fundamentals, ma'am."
    show player 5
    show coach 15b
    bri "Ahh, yes."
    bri "So basketball is all about the fund-"
    show coach 15
    show player 22
    dex "There's the nerd I've been looking for!" with hpunch
    show player 23
    player_name "Oh, shit..."
    show player 22
    show erik 5f
    eri "Uh oh..."
    show erik 51f
    show dexter 14 at right with dissolve
    show coach 15b
    bri "What in the world?!"
    show coach 15
    show dexter 15
    dex "You think I wasn't gonna find out, you little bitch?!"
    show dexter 14
    show coach 15c
    bri "Excuse me?! {b}Dext{/b}-"
    show coach 15
    show dexter 13 at Position (xoffset=-18) with dissolve
    dex "Get out of my way, fat boy or I'll punch those stupid freckles right off your face!" with hpunch
    show erik 64f with fastdissolve
    show erik 65f with fastdissolve
    show erik 66f with fastdissolve
    hide erik
    show dexter 15
    with dissolve
    dex "I saw you and that whore, ex-girlfriend of mine!"
    show dexter 14
    show player 15
    player_name "Hey, don't talk about about {b}Roxxy{/b} like that!"
    show player 16
    show dexter 15
    dex "I'll say whatever the hell I want!"
    dex "What are you gonna do about it, NERD?!"
    show dexter 14
    show player 11 at Position (xpos=-150)
    show coach 15cf at left
    bri "Alright, {b}Dexter{/b}, you better back up right this instant!" with hpunch
    bri "This isn't happening in the middle of my class, mister!"
    show coach 15f
    show dexter 15
    dex "... But {b}Coach{/b} you don't understand..."
    dex "This piece of shit-"
    show dexter 14
    show coach 15cf
    bri "I don't wanna hear it, {b}Dexter{/b}!"
    bri "You know the rules in my class!"
    bri "We settle things here without violence!"
    show coach 15f
    show dexter 15
    dex "Ugh, this won't be settled until that twerp gets the beating he has coming..."
    show dexter 14
    show coach 17f with dissolve
    player_name "..."
    show coach 1f
    show dexter 29
    with dissolve
    dex "Hmm?"
    show coach 2f
    bri "So beat him on the court."
    hide coach
    show player 16 at left
    with dissolve
    show dexter 30
    dex "I don't understand..."
    show dexter 29
    show player 12
    player_name "She's saying we should settle this with a game of basketball... moron."
    show player 16
    dex "!!!"
    show dexter 30
    dex "Oh, you're so dead..."
    show dexter 33
    show player 647
    with dissolve
    dex "Fine!"
    show dexter 15 with dissolve
    dex "You're ball, NERD!"
    hide player
    hide dexter
    with dissolve
    return

label school_roxxy_fight_dexter:
    scene expression game.timer.image("outside_school{}")
    show player 12 with dissolve
    player_name "I had better make sure I'm prepared for a fight before going back to school."
    player_name "There's no doubt, {b}Dexter{/b} will be looking for blood after what happened on the basketball court."
    show player 4 at Position (xoffset=7) with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "I'll need lots of {b}Agility{/b} to avoid his attacks and {b}Strength{/b} to put him down fast."
    player_name "Otherwise, I won't stand a chance..."
    show player 5
    player_name "..."
    show player 38 at Position (xoffset=51) with dissolve
    player_name "Am I ready for this?!"
    show player 3 at Position (xoffset=26) with dissolve

    return

label school_roxxy_locker_sex:
    scene expression "backgrounds/location_school_locker_room_backpack_day_blur.jpg"
    show becca 6 at Position (xpos=315)
    show roxxy 1g at Position (xpos=600)
    show missy 7 at left
    with dissolve
    becca "... It's that good?!"
    show becca 5
    show roxxy 1h
    rox "Fucking. Mind. Blowing!"
    show roxxy 1g
    show missy 5
    missy "Ooooh, I'm getting wet just thinking about it..."
    show missy 7
    show roxxy 1h
    rox "Like, oh my god... I can't even describe the way it feels."
    show roxxy 1g
    show becca 2
    becca "... Does it hurt?"
    show becca 1
    show roxxy 2
    rox "Yeah, a lot at first!"
    show missy 3
    show roxxy 1b
    rox "... But after awhile it hurts less..."
    show roxxy 1h
    rox "... And then later it still hurts but in a really REALLY good way!"
    show roxxy 1g
    show becca 5
    becca "Hmm..."
    show missy 8
    missy "God, that's so hot!"
    show missy 7
    show becca 3b
    becca "It does sound pretty hot..."
    show becca 5
    show roxxy 1h
    rox "You have no idea!"
    show roxxy 1g
    becca "..."
    show missy 8
    missy "So when do we get to play with him?!"
    show roxxy 2b
    show missy 7
    show becca 3b
    becca "{b}Missy{/b}!!!"
    show becca 3
    show missy 8
    missy "... What?!"
    show roxxy 3d
    missy "Don't act like you aren't thinking the same thing!"
    show missy 7
    show becca 26 with dissolve
    becca "..."
    show becca 24 with dissolve
    show roxxy 3c
    rox "... Seriously?!"
    rox "He's {b}MY{/b} fucking boyfriend! Why should I let you dumb skanks play with him?!"
    show roxxy 3d
    show missy 1b
    missy "Uhh, because we're your dumb skanks!"
    show missy 8
    missy "... And besides, we all know it turns you on..."
    show missy 7
    show roxxy 2b
    rox "!!!" with hpunch
    show roxxy 3c
    rox "What the hell are you talking about?!"
    show roxxy 3d
    show missy 8
    missy "Psh, don't lie!"
    show missy 7
    show becca 25
    becca "We've both seen you playing with yourself during our games of spin the bottle, {b}Roxxy{/b}..."
    show becca 24
    show roxxy 2c
    rox "... I do not!"
    show roxxy 2b
    show missy 1b
    missy "You do so!!!"
    show missy 7
    show becca 25
    becca "It's not very subtle..."
    show becca 24
    show roxxy 29
    rox "..."
    show roxxy 30
    rox "Tch, okay. Fine!"
    show roxxy 3c
    rox "I admit, it's kinda hot watching everybody fooling around when we play..."
    rox "That doesn't mean I'm going to let you start fucking him..."
    show roxxy 3d
    show becca 25
    becca "..."
    show missy 4
    missy "Why not?!"
    show missy 2b
    show roxxy 3
    rox "Because he's {b}my man{/b}!"
    rox "Not yours! {b}MINE{/b}!"
    show roxxy 3b
    becca "..."
    show missy 8
    missy "Yeah, but..."
    missy "Just think about this, {b}Roxxy{/b}."
    missy "{b}Becca{/b} naked... On her back... Her pale, freckled tits heaving with anticipation..."
    show missy 7
    show roxxy 1
    show becca 27 with dissolve
    becca "Anticipation?! What the hell are you on about?!"
    show becca 26
    show missy 4
    missy "Shut up! I'm trying to paint a picture here!"
    show missy 2b
    rox "..."
    show missy 8
    missy "{b}[firstname]{/b}'s huge throbbing cock, rubbing against her clit as she moans and begs you to let her have it..."
    show missy 7
    becca "..."
    show roxxy 1b
    rox "... I'm listening."
    show roxxy 1
    show missy 8
    missy "{b}*Ahem*{/b}!!!"
    show missy 7
    show becca 27
    becca "What?!"
    show becca 26
    show missy 8
    missy "{b}Becca{/b} begs you to let her have it..."
    show missy 7
    show becca 27
    becca "Seriously?!"
    show becca 26
    show missy 4
    missy "Do it, bitch! Don't fucking ruin this for me!"
    show missy 2b
    show becca 24 with dissolve
    becca "..."
    show becca 25
    becca "Please, let me have it {b}Roxxy{/b}..."
    show missy 7
    show roxxy 4
    rox "Hahaha, you would really beg me for it, {b}Becca{/b}?"
    show roxxy 1
    show becca 25
    becca "... I don't know."
    show becca 24
    show missy 8
    missy "Oh, she totally would! Look at how turned on she is, just thinking about it..."
    show missy 7
    show becca 27 with dissolve
    becca "I am not!"
    show becca 26
    show missy 8
    missy "Bitch, you're practically panting."
    show missy 7
    becca "..."
    show becca 24 with dissolve
    show roxxy 1g
    rox "Hmm."
    show roxxy 1h
    rox "... And what about you?!"
    show roxxy 1g
    show becca 26 with dissolve
    show missy 1b
    missy "Me?!"
    show missy 1
    show roxxy 1h
    rox "You gonna beg me too?"
    show roxxy 1g
    show missy 8
    missy "I'll do whatever you want me to do!"
    missy "You want me to beg? I'll beg."
    missy "I'll suck your tits or lick your pussy... Hell, I'll toss your salad if you want!"
    missy "Just as long as you let me take a ride on that huge nerd cock of his!"
    show missy 7
    show roxxy 4
    rox "Hahahaha!"
    show roxxy 1g
    show missy 8
    missy "C'mon, you have to admit. It's pretty hot."
    missy "Your own personal bitches, willing to do anything you desire, for a chance at your man's cock..."
    show missy 7
    show becca 27
    becca "I am not tossing her salad..."
    show becca 26
    show missy 2
    missy "Psh, you totally would {b}Becca{/b}. Don't lie!"
    show missy 7
    show becca 24 with dissolve
    becca "..."
    show roxxy 1h
    rox "You really put a lot of thought into this..."
    show roxxy 1h
    show missy 6
    missy "Hah, more than a lot, believe me!"
    show missy 7
    rox "..."
    show missy 8
    missy "So what do you say?!"
    show missy 7
    rox "..."
    show roxxy 1g
    rox "... Maybe."
    show roxxy 1h
    show missy 3
    show becca 2
    becca "!!!"
    show missy 1b
    missy "{b}*Gasp*{/b} Really?!"
    show missy 1
    show roxxy 1b
    rox "We would have to establish some ground rules..."
    rox "... Like you two do everything I say, no arguements."
    show roxxy 1g
    show missy 1b
    missy "I am SO totally on board with that!"
    show missy 1
    becca "..."
    show roxxy 1b
    rox "{b}Becca{/b}?"
    show roxxy 1
    show missy 7b with dissolve
    becca "!!!"
    show missy 1 with dissolve
    show becca 25
    becca "... I'll do everything you say."
    becca "No arguements..."
    show becca 24
    show roxxy 1h
    rox "... Even if I tell you to eat me out or swallow {b}[firstname]{/b}'s load?"
    show roxxy 1g
    show missy 4
    missy "Hell yes! Gladly!"
    show missy 1b
    missy "Anything you want, {b}Roxxy{/b}! I'm your bitch!"
    show missy 1
    becca "..."
    show roxxy 1b
    rox "{b}Becca{/b}?"
    show roxxy 1g
    show becca 25
    becca "... Yeah, okay."
    show becca 24
    show roxxy 1h
    rox "Okay, what?!"
    show roxxy 1g
    show becca 25
    becca "I'll be your bitch too, okay?!"
    show becca 24
    show roxxy 4
    rox "Hahaha!"
    show roxxy 1h
    rox "...Hmm, I'll think about it."
    show roxxy 1g
    show missy 7
    missy "..."
    becca "..."
    show roxxy 1b
    rox "Now, if you'll excuse me."
    show roxxy 1h
    rox "I'm gonna go find {b}my man{/b}!"
    hide roxxy with dissolve
    pause
    show becca 1f at Position (xpos=400) with dissolve
    show missy 4
    missy "Damnit, I was hoping she would agree right away..."
    show missy 2b
    show becca 2f
    becca "... Me too."
    show becca 1f
    show missy 1b
    missy "See, I fucking knew you were into it!"
    show missy 1
    show becca 2f
    becca "Shut up!"
    show becca 1f
    show missy 8
    missy "You're such a slut."
    show missy 7
    show becca 2f
    becca "Yeah, well... At least I'm not as big a slut as you!"
    show becca 1f
    show missy 5
    missy "Psh, whatever."
    show missy 2
    missy "My sluttiness might have just got us a date with {b}[firstname]'s{/b} magic cock!"
    missy "You should be thanking me right now!"
    show missy 2b
    show becca 7f
    becca "..."
    hide becca
    hide missy
    with dissolve

    scene school
    show player 13 at left
    with dissolve
    show roxxy 1b at right with dissolve
    rox "There you are!"
    show roxxy 1
    show player 14
    player_name "Hey, {b}Roxxy{/b}!"
    player_name "What are you up to?"
    show player 13
    show roxxy 1h
    rox "Heh, I was just thinking about you..."
    show roxxy 1g
    show player 14
    player_name "Oh yeah?"
    player_name "What about me?"
    show player 13
    show roxxy 1h
    rox "Oh, you know... Just how strong and manly you are..."
    rox "... And how I'd like to ride that strong, manly cock of yours right here and now."
    show roxxy 1g
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "What?! we can't do that!"
    player_name "We're at school!"
    show player 5
    show roxxy 4
    rox "Hehehe, don't worry!"
    show roxxy 1h
    rox "Nobody is gonna see us..."
    show roxxy 1g
    show player 11
    player_name "..."
    show roxxy 1h
    rox "I have a plan!"
    hide roxxy with dissolve
    show player 12
    player_name "What the-"
    hide player with fastdissolve

    scene expression "backgrounds/location_school_cutscene06.jpg"
    with fade
    show text "Again, {b}Roxxy{/b} dragged me into my locker like some rag doll!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene expression "backgrounds/location_school_locker_inside01.jpg"
    show player locker 1
    show roxxy locker 1b
    with dissolve
    player_name "Great, we're stuffed in my locker again..."
    show player locker 2
    show roxxy locker 1
    rox "Hehe, shut up and get your cock out!"
    show roxxy locker 1b
    show player locker 7
    player_name "You're serious?!"
    show player locker 5
    show roxxy locker 1
    rox "Hell yeah, I'm serious!"
    rox "I want you inside me, right now!"
    show roxxy locker 1b
    show player locker 6
    player_name "What the heck got you so worked up?!"
    show player locker 5
    show roxxy locker 1
    rox "Mmm, you'll find out soon enough."
    show roxxy locker 1b
    show player locker 11 with dissolve
    player_name "..."
    show player locker 12 with dissolve
    pause
    hide roxxy
    show player locker 13
    with dissolve
    rox "... But right now, I want you to concentrate..."
    show player locker 14 with dissolve
    pause
    rox "... On fucking me senseless!"
    player_name "O-okay..."
    show player locker 15
    rox "!!!" with hpunch
    rox "Ahhh..."
    return

label school_roxxy_locker_sex_repeat:
    scene school
    show player 12 with dissolve
    player_name "... Now where the hell is she?!"
    show player 4 with dissolve
    rox "Pssst!"
    show player 11f
    player_name "!!!" with hpunch
    hide player with fastdissolve

    scene expression "backgrounds/location_school_cutscene06.jpg"
    with fade
    show text "Again, {b}Roxxy{/b} dragged me into my locker like some rag doll!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I wasn't her boy toy was I?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene expression "backgrounds/location_school_locker_inside01.jpg"
    show player locker 8
    show roxxy locker 1
    with dissolve
    rox "Finally! I was starting to think you chickened out on me!"
    show roxxy locker 1b
    show player locker 6
    player_name "Seriously, you wanna do this again?!"
    show player locker 5
    show roxxy locker 1
    rox "Absolutely!"
    show roxxy locker 1b
    show player locker 6
    player_name "You realize what would happen? If we got caught having sex on school grounds?!"
    show player locker 5
    show roxxy locker 1
    rox "Yeah, we'd both be expelled."
    show roxxy locker 1b
    player_name "... Exactly!"
    show player locker 11 with dissolve
    pause
    show player locker 12 with dissolve
    pause
    hide roxxy
    show player locker 13
    with dissolve
    rox "So let's not get caught..."
    show player locker 14 with dissolve
    player_name "... Why aren't you worried about-"
    rox "{b}[firstname]{/b}, shut up and fuck me!"
    show player locker 15
    player_name "Fine!" with hpunch
    return

label roxxy_locker_sex_loop_pre:
    scene expression "backgrounds/location_school_locker_inside01.jpg"
    $ M_roxxy.set("sex speed", .09)
    show expression AnimatedImage("roxxys_locker", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_locker with dissolve
    return

label roxxy_locker_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("roxxys_locker", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_locker
                $ animated = True
            pause 5
            call expression game.dialog_select("roxxy_locker_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "roxxys_locker {}".format(pose_list[pose_counter]) as roxxys_locker
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("roxxy_locker_hscene_dialog")
        $ animcounter += 1
    if M_roxxy.get("roxxy locker sex first"):
        $ M_roxxy.set("roxxy locker sex first", False)
    call screen roxxy_locker_sex_options

label roxxy_locker_hscene_dialog:
    $ random_count = randomizer()
    if animcounter == 0:
        if M_roxxy.get("roxxy locker sex first"):
            player_name "Shhh!!!"
            player_name "You have to be quiet or someone will catch us!"
            rox "I know!"
            rox "It's not exactly easy, you know!"
            player_name "Well then, stop and I'll fuck you later tonight!"

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count > 33 and random_count <= 66:
                rox "Mmm, I love this dick, so fucking much!"
                player_name "Shh!!"
                rox "{b}*Whimper*{/b}"

            elif random_count > 66:
                rox "Aahh!!"

    elif animcounter == 1:
        if M_roxxy.get("roxxy locker sex first"):
            rox "Mmm..."

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count <= 33:
                rox "Mmm, this is so fucking hot!"
                player_name "... Yeah, I know."
                player_name "I'm sweating like crazy."
                rox "Eww! That's not what I meant!"
                player_name "..."
                rox "I mean, like, someone could totally catch us in here fucking!"
                player_name "..."
                rox "Fuck, that's hot!"
                player_name "You are so weird sometimes..."
                rox "Hehehe, shut up and fuck me harder!"

            elif random_count > 66:
                rox "Ooh, fuck me, {b}[firstname]{/b}!"
                player_name "..."
                rox "Fuck me harder!!"
        else:

            rox "{b}[firstname]{/b}!!!"

    elif animcounter == 2:
        if M_roxxy.get("roxxy locker sex first"):
            player_name "{b}Roxxy{/b}!!!"
            rox "Shut up and fuck me!"
            player_name "..."
            player_name "Fine!"
            $ M_roxxy.set("sex speed", .06)
            rox "Fuuuuuck..." with hpunch
            player_name "Be quiet, bitch!"
            rox "{b}*Whimper*{/b}"

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count > 33 and random_count <= 66:
                player_name "Ouch!"
                rox "... What?!"
                player_name "I hit my head on the top of the stupid locker!"
                rox "Hahaha, don't be a baby!"
                player_name "Well, it hurt!"
                rox "Yeah and you pulling my hair hurts too... You don't hear me complaining."
                player_name "... Why didn't you just say something? I would have stopped."
                rox "{b}*Gasp*{/b} Don't you dare stop!"
                rox "Pull it harder!"

            elif random_count > 66:
                player_name "Shh!!! Someone is going to hear you!"
                rox "I don't care!"
                rox "Let them hear me!"
                rox "This is so fucking good!!!"
                player_name "Damnit, {b}Roxxy{/b}!"
                player_name "They'll expel us!"
                rox "{b}*Whimper*{/b}"
                rox "... Fine."
        else:

            rox "Oh god, oh god, OH GOD!!!"

    elif animcounter == 3:
        if M_roxxy.get("roxxy locker sex first"):
            rox "Oh god, oh god, OH GOD!!!"
            player_name "Shut up and cum!!!"

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count > 33 and random_count <= 66:
                player_name "..."
                rox "Mmm! fuuuuuck yessss!!!"
        else:

            if random_count > 50:
                rox "Haaah, I'm getting close."
                player_name "Good, me too!"
    return

label roxxy_locker_sex_cum:
    call expression game.dialog_select("roxxy_locker_sex_cum_pre")
    if M_roxxy.get("roxxy locker sex"):
        call expression game.dialog_select("roxxy_locker_sex_cum_repeat")
    else:

        call expression game.dialog_select("roxxy_locker_sex_cum_first")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Roxxy"]["unlocked"] = True
    $ persistent.cookie_jar["Roxxy"]["gallery"]["05_unlocked"] = True
    $ M_roxxy.trigger(T_roxxy_locker_sex)
    $ player.go_to(L_school_hall)
    $ game.timer.tick()
    $ game.main()

label roxxy_locker_sex_cum_pre:
    scene expression "backgrounds/location_school_locker_inside01.jpg"
    hide roxxys
    show player locker 15_15b
    player_name "Tch!" with flash
    rox "!!!"
    rox "{b}*Gasp*{/b}!!!"
    pause
    show player locker 16 with dissolve
    return

label roxxy_locker_sex_cum_first:
    player_name "You alright?"
    show player locker 17b with dissolve
    rox "Haah... Haah..."
    rox "Yeah, just give me a second..."
    rox "Phew."
    show player locker 17
    player_name "That was crazy."
    show player locker 17b
    rox "Yeah but it felt amazing, didn't it?"
    show player locker 17
    player_name "Heh, yeah..."
    show player locker 17b
    rox "I think we might have to try this again sometime!"
    show player locker 17
    player_name "Huh?! No way!"
    player_name "What if we get caught?!"
    show player locker 17b
    rox "Hehe, we'll just have to be careful..."
    show player locker 17
    player_name "..."
    show player locker 17b
    rox "C'mon, pull your pants up and lets get out of here while the hall is empty!"
    show player locker 17
    player_name "{b}*Sigh*{/b}."
    scene black with fade

    scene school
    show player 14 at left
    show roxxy 1g at right
    with dissolve
    player_name "Seriously, what brought that on?!"
    show player 13
    show roxxy 4
    rox "Hehe, I can't say."
    show roxxy 1g
    show player 14
    player_name "Why not?!"
    show player 13
    show roxxy 1h
    rox "... Because I'm planning a surprise for you!"
    show roxxy 1g
    show player 12
    player_name "Huh?"
    player_name "What kind of surprise?"
    show player 13
    show roxxy 1h
    rox "Hehe, the kind only {b}my man{/b} deserves..."
    show roxxy 1g
    show player 11
    player_name "..."
    show player 13
    show roxxy 1b
    rox "Just remember to {b}show up{/b} for the party this weekend!"
    show roxxy 1g
    show player 14
    player_name "{b}You and the girls doing the beach thing again?{/b}."
    show player 13
    show roxxy 1h
    rox "Always."
    show roxxy 1g
    show player 14
    player_name "So {b}Saturday Evening{/b} at {b}the beach{/b}?"
    show player 13
    show roxxy 1b
    rox "Mmmhmm."
    rox "Don't be late!"
    show roxxy 1
    show player 14
    player_name "Heh, alright."
    show player 13
    show roxxy 1h
    rox "See you later, {b}[firstname]{/b}."
    show roxxy 1g
    show player 14
    player_name "Bye, {b}Roxxy{/b}."
    hide player
    hide roxxy
    with dissolve
    return

label roxxy_locker_sex_cum_repeat:
    player_name "You alright?"
    show player locker 17b with dissolve
    rox "Haah... Haah..."
    rox "Yeah, just give me a second..."
    rox "Phew."
    show player locker 17
    player_name "C'mon, let's get out of here!"
    scene black with fade

    scene school
    show player 10 at left
    show roxxy 1g at right
    with dissolve
    player_name "You know, we really can't keep doing this!"
    show player 5
    show roxxy 1h
    rox "Why not?!"
    show roxxy 1g
    show player 10
    player_name "We're gonna get caught, {b}Roxxy{/b}!"
    show player 5
    show roxxy 2
    rox "Psh, you worry too much!"
    show roxxy 1g
    show player 16
    player_name "..."
    show roxxy 2
    rox "Don't give me that look!"
    show roxxy 48 with dissolve
    rox "C'mon, you know I really get off on this!"
    rox "You aren't gonna take that away from me... Are you?!"
    show roxxy 47
    show player 14
    player_name "{b}*Sigh*{/b} Alright, alright!"
    player_name "Just put your hypnotic boobs away!"
    show player 13
    show roxxy 4 with dissolve
    rox "Hehehe, thank you {b}[firstname]{/b}!"
    hide player
    show roxxy 92 at left
    with dissolve
    pause
    show roxxy 59e with dissolve
    player_name "C'mon, we have to get to class..."
    show roxxy 59d
    rox "Ooh, yes sir..."
    rox "Hehehe!"
    hide roxxy with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
