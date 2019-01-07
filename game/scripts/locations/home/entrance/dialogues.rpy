label entrance_diane_gave_birth_dialogue_seen:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 10 at left
    show debbie 1f at Position (xpos=600)
    show diane a_casual_baby b_casual at Position (xpos=625)
    show jenny f_grin at flip
    show jenny at Position (xpos=150)
    with dissolve
    player_name "{b}Diane{/b}?"
    show player 14
    player_name "You guys are finally home?"
    show player 13
    show diane f_normal_talk
    dia "Yup, we're home."
    show diane f_normal
    show debbie 2f
    show diane f_down_front
    if M_diane.pregnancy.baby_gender == "boy":
        deb "Isn't he just the most precious thing ever?!"
        show debbie 1f
        show jenny f_normal_talk
        jen "I dunno, he kinda looks like a potato..."
        show jenny f_normal
        show debbie 2f
        deb "No he doesn't!"
        deb "He's so handsome!"
        show debbie 1f
        pause
        show debbie 2f
        deb "Who's a handsome boy, huh?"
    else:
        deb "Isn't she just the most precious thing ever?!"
        show debbie 1f
        show jenny f_normal_talk
        jen "I dunno, she kinda looks like a potato..."
        show jenny f_normal
        show debbie 2f
        deb "No she doesn't!"
        deb "She's beautiful!"
        show debbie 1f
        pause
        show debbie 2f
        deb "Who's a pretty girl, huh?"
    show debbie 1f
    show diane f_laugh
    dia "Hehe!"
    show diane f_normal
    show debbie 2f
    deb "I can't believe you finally have a child, {b}Diane{/b}."
    deb "I'm so happy for you!"
    show debbie 1f
    show diane f_normal_talk
    dia "I know, I didn't think I'd ever get to be a mommy."
    show diane f_normal
    show debbie 2f
    show diane f_down_front
    if M_diane.pregnancy.baby_gender == "boy":
        deb "He's so adorable..."
        show jenny f_eyeroll
        show debbie 3f
        deb "I could just gobble him up!"
        show debbie 1f
        show jenny f_normal
        pause
        show diane f_normal_talk
        dia "I should really get him down for the night."
        dia "He's had a busy day."
    else:
        deb "She's so adorable..."
        show jenny f_eyeroll
        show debbie 3f
        deb "I could just gobble her up!"
        show debbie 1f
        show jenny f_normal
        pause
        show diane f_normal_talk
        dia "I should really get her down for the night."
        dia "She's had a busy day."
    show diane f_down_front
    show debbie 2f
    deb "Aww, okay..."
    deb "Bye bye, little one."
    show debbie 1f
    pause
    show debbie 1 at right
    show jenny at Position (xpos=200)
    hide diane
    with dissolve
    pause
    show debbie 3
    deb "Oh, I just love babies!"
    show debbie 1
    show jenny f_eyeroll
    jen "Ugh, whatever."
    show jenny f_upset_talk
    jen "If that thing is up all night screaming, I will absolutely lose my shit!"
    show jenny f_upset
    show debbie 13
    deb "{b}*Sigh*{/b}, {b}[jen_name]{/b}..."
    deb "Don't be like that, dear."
    show debbie 14b
    show jenny f_normal_talk
    jen "I'm just saying, I need my eight hours or I get cranky."
    show jenny f_normal
    show player 12
    player_name "You're always cranky..."
    show player 13 with None
    show jenny f_upset_talk at unflip
    show jenny at Position (xpos=-200)
    with dissolve
    jen "What did you say?!"
    show jenny f_gross
    show player 10
    player_name "N-nothing."
    show player 5
    pause
    show jenny f_upset_talk
    jen "Uh huh."
    show jenny f_upset
    pause
    show jenny f_upset_talk
    jen "You better watch your mouth."
    jen "I know where you sleep."
    hide jenny with dissolve
    pause
    show player 12
    player_name "She's such a ray of sunshine..."
    show player 13
    show debbie 3
    deb "Hehehe!"
    show debbie 2
    deb "Oh, don't mind her."
    deb "She likes babies too, she just doesn't want to admit it."
    show debbie 1
    show player 12
    player_name "If you say so."
    hide player
    hide debbie
    hide diane
    with dissolve
    return

label entrance_diane_peeking:
    scene expression "backgrounds/location_home_entrance_night_blur.jpg"
    show player 34 with dissolve
    pause
    show player 35
    player_name "Hmm, it sure is quiet in here tonight..."
    show player 10
    player_name "I wonder what {b}[deb_name]{/b} and {b}Diane{/b} are doing."
    show player 14
    player_name "{b}They're usually in the living room{/b} watching tv and having girl talk."
    player_name "{b}I should check on them.{/b}"
    hide player with dissolve
    return

label entrance_diane_couch_crashing:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 13 at left
    show diane b_casual a_casual_bag f_laugh zorder 1 at Position (xpos=625)
    with dissolve
    dia "Honey, we're home!"
    dia "Haha!"
    show player 17
    player_name "Haha!"
    show diane f_normal
    show debbie 2f zorder 0 with dissolve
    deb "What in the heck is going-"
    show debbie 3f
    show player 13
    deb "{b}*Gasp*{/b} You're here!"
    show debbie 2f
    show diane f_normal_talk
    dia "I'm here!"
    show diane f_normal_talk a_casual_bag_point with dissolve
    dia "Are we starting with a pajama party?"
    show diane f_normal a_casual_bag
    show debbie 222f
    with dissolve
    deb "Huh?"
    pause
    show debbie 3f with dissolve
    deb "Oh, shuddup."
    show debbie 1f
    show diane f_normal_talk
    dia "I'm serious, I brought my nightgown and everything!"
    show diane f_normal
    show debbie 2f
    deb "Are you hungry?"
    show debbie 1f
    show diane f_normal_talk
    dia "Oh, room service and everything."
    show diane f_smirk_talk
    dia "You didn't tell me it was gonna be so fancy..."
    show diane f_smirk
    show debbie 2f
    deb "Just get in here and I'll help you unpack."
    show debbie 1f
    show diane f_laugh
    dia "Yes, ma'am."
    show diane f_normal_talk
    dia "You wanna join us, {b}[firstname]{/b}?"
    show debbie 1 with dissolve
    show diane f_normal
    show player 55 with dissolve
    player_name "{b}*Yawn*{/b}"
    show player 26 with dissolve
    player_name "... Sure!"
    show player 25
    show debbie 2
    deb "Oh sweetie, you look exhausted!"
    deb "Why don't you just head on to bed and let {b}Diane{/b} and I spend some time together."
    show diane f_wink
    show debbie 1f with dissolve
    pause
    show diane f_smirk_talk
    dia "Mmm, time together, huh?"
    show diane f_smirk
    show debbie 3f
    deb "Oh, hush!"
    show diane f_laugh
    dia "Haha."
    show diane f_normal
    show debbie 1 with dissolve
    show player 26
    player_name "Yeah, okay."
    player_name "I am pretty tired."
    show player 25
    show diane f_smirk_talk
    dia "I guess it's just you and me then, beautiful."
    show diane f_smirk
    show debbie 3f with dissolve
    deb "Hehe, stop it!"
    show debbie 1f
    show diane f_smirk_talk
    dia "Good night, {b}[firstname]{/b}."
    show player 55
    hide debbie
    hide diane
    with dissolve
    pause
    hide player with dissolve
    return

label entrance_diane_debbie_drop_off_request:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 13 at left
    show debbie 221 at right
    with dissolve
    deb "Hold on, {b}[firstname]{/b}."
    show debbie 220
    show player 14
    player_name "Hey, {b}[deb_name]{/b}."
    player_name "What's up?"
    show player 13
    show debbie 221
    deb "Did you do any work for {b}Diane{/b} today?"
    show debbie 220
    show player 14
    player_name "Yeah, I was over there earlier."
    show player 13
    show debbie 221
    deb "Is she doing alright?"
    show debbie 220
    show player 5
    player_name "Hmm?"
    show player 10
    player_name "Yeah, I guess..."
    show player 5
    show debbie 221
    deb "... Cause I just got off the phone with her and she sounds exhausted."
    show debbie 220
    show player 10
    player_name "Well, she is working herself really hard with that new business of hers."
    player_name "I told her to slow down but you know how passionate she is about it."
    show player 5
    show debbie 221
    deb "Yeah, she has a tendency to throw herself into her work and disregard her needs."
    deb "It worries me."
    deb "Would you mind heading back over there?"
    show debbie 220
    show player 10
    player_name "Tonight?"
    show player 5
    show debbie 221
    deb "Yeah, I want you to take her this pie I made today and make sure she eats it!"
    deb "She probably hasn't eaten a thing all day."
    show debbie 220
    show player 14
    player_name "Yeah, I can do that."
    show player 13
    show debbie 221
    deb "I would really appreciate it."
    show debbie 2
    show player 673
    with dissolve
    deb "Tell her she had better get a solid eight hours sleep too or it'll be me visiting her next!"
    show debbie 1
    show player 674
    player_name "Heh, alright."
    hide debbie
    hide player
    with dissolve
    return

label entrance_erik_bullying:
    scene expression L_home_entrance.background
    show mrsj 19c at right with dissolve
    show player 10 at left with dissolve
    player_name "Is everything ok, {b}Mrs. Johnson{/b}?"
    show player 5
    show mrsj 19
    mrsjo "Sorry to disturb you this morning."
    show mrsj 52
    mrsjo "It's just... it's about {b}Erik{/b}."
    mrsjo "Has {b}Erik{/b} been having trouble lately at school?"
    show mrsj 19c
    show player 12
    player_name "Huh?"
    show player 35
    player_name "Not that I know of?"
    show player 10
    player_name "He usually does well at school..."
    show player 5
    show mrsj 20
    mrsjo "No. I'm not talking about grades."
    show mrsj 52
    mrsjo "Have the other kids in school been giving {b}Erik{/b} a hard time?"
    mrsjo "He's been asking to stay home instead of going to class."
    show mrsj 20
    mrsjo "I... I even saw him come home last week with bruises."
    show mrsj 19c
    show player 23
    player_name "!!!" with hpunch
    show player 12
    player_name "{b}Erik{/b} is pretty quiet at school."
    player_name "I've never seen him get involved in any kind of bad stuff."
    show player 5
    show mrsj 19
    mrsjo "Maybe, if a close friend stopped over to him see him, he'd be more willing to talk..."
    show mrsj 19c
    show player 10
    player_name "You want me to ask him?"
    show player 5
    show mrsj 19
    mrsjo "I just want what's best for him, and you're his only friend."
    show mrsj 19c
    show player 12
    player_name "Okay. I'll go see him."
    hide mrsj
    hide player
    with dissolve
    return

label entrance_erik_bullying_3:
    scene expression L_home_entrance.background
    show mrsj 19c at Position (xpos=700)
    show debbie 13 at right
    with dissolve
    show player 5 at left with dissolve
    deb "Sweetie!! Are you okay?!"
    show debbie 14b
    show player 10
    player_name "I'm fine, {b}[deb_name]{/b}. The nurse said I just had a small concussion."
    show player 11
    show debbie 13
    deb "You had a concussion!"
    show debbie 14b
    show player 10
    player_name "Everything is fine. I'll be okay, {b}[deb_name]{/b}."
    show player 5
    show debbie 13
    deb "Your stupid school didn't even call to let me know you were in the hospital!"
    deb "I had to hear about it from {b}Tammy{/b}!"
    show debbie 14b
    show player 10
    player_name "{b}[deb_name]{/b}, it's alright. I'm really fine! Calm down."
    show player 11
    show debbie 13
    deb "I'm sorry... I was just so worried about you!"
    deb "Your {b}Father{/b} is counting on me to watch over you!"
    show debbie 14b
    show mrsj 19
    mrsjo "I'm so happy to see you're okay, {b}[firstname]{/b}."
    mrsjo "I came over here to fill {b}[deb_name]{/b} in the second {b}Erik{/b} called me."
    mrsjo "You did a good thing standing up for {b}Erik{/b}."
    show mrsj 38
    show debbie 13
    deb "Yes, it was really brave of you to stand up for your friend at school."
    deb "But, be please be careful!"
    show debbie 14b
    show player 24
    player_name "I know {b}[deb_name]{/b}..."
    show player 25
    player_name "I promise I'll try and stay out of trouble."
    show player 24
    show debbie 13
    deb "Come here."
    hide player
    hide debbie
    hide mrsj
    with dissolve
    show mrsj 14 at right
    show debbie 4
    with dissolve
    deb "I'm so glad you're safe."
    deb "{b}Your father{/b} would just throw a fit if he knew I let this happen."
    player_name "It's alright, {b}[deb_name]{/b}."
    hide debbie
    hide mrsj
    with dissolve
    show mrsj 14 at Position (xpos=700)
    show debbie 1 at right
    show player 13 at left
    with dissolve
    show mrsj 17
    mrsjo "Thanks again, {b}[firstname]{/b}."
    mrsjo "You're always welcome to stop over and visit."
    show mrsj 14
    show player 14
    player_name "It's fine. Just helping a friend."
    show player 13
    show mrsj 17
    mrsjo "Thank you."
    show mrsj 14
    show player 36 with dissolve
    player_name "Good night {b}Mrs. Johnson{/b}."
    show player 13 with dissolve
    show mrsj 17
    mrsjo "Good night."
    hide mrsj with dissolve
    show debbie 2
    deb "Now hurry up to bed and get some rest."
    hide player
    hide debbie
    with dissolve
    return

label entrance_mia_angelicas_impatience:
    scene expression L_home_entrance.background
    show debbie 1f at Position (xpos=500)
    show ang 1 at right
    with dissolve
    pause.5
    show player 5 at left
    show debbie 3
    with dissolve
    deb "There he is!"
    show debbie 1
    show player 22
    player_name "!!!" with hpunch
    show debbie 2
    deb "I'm so happy to hear {b}[firstname]{/b} visited our local church lately..."
    deb "... And offered volunteer work with the clergy!"
    show debbie 1
    show player 24
    player_name "Uhh..."
    show debbie 2
    deb "Well! I will leave you two to it, I have things cooking in the kitchen!"
    show debbie 2f with dissolve
    deb "It was great meeting you {b}Sister Angelica{/b}!"
    hide debbie with dissolve
    show player 12
    player_name "Volunteer work?"
    player_name "And why are you here?!"
    show player 11
    show ang 2
    ang "I thought we had an agreement?"
    show ang 1
    show player 24
    player_name "..."
    show ang 2
    ang "Did you think I would just let you slip away from me?!"
    show ang 1
    show player 10
    player_name "No, I just... What do you want from me?"
    show player 11
    show ang 2
    ang "The door of the church will be left unlocked at night."
    ang "Come visit me in my chamber and I will explain what I need from you..."
    ang "...And don't try to hide from me again, or else-"
    show ang 1
    show player 12
    player_name "Okay, okay!"
    player_name "Just don't say anything to my {b}landlady{/b}..."
    show player 11
    show ang 2
    ang "That will be up to you..."
    hide ang with dissolve
    show player 12
    player_name "Now I have to go see her at church? In the middle of the night?!"
    show player 10
    player_name "This is strange..."
    hide player with dissolve
    return

label entrance_mia_angelicas_home_visit:
    scene expression L_home_entrance.background with fade
    show debbie 2f at Position (xpos=500)
    show ang 1 at right
    with dissolve
    pause.5
    show player 5 at left
    show debbie 3f
    with dissolve
    deb "It's always a pleasure to hear that {b}[firstname]{/b} is actively involved with the church."
    deb "You two must be getting to know each other quite well."
    show debbie 1f
    show ang 2
    ang "Yes, {b}[firstname]{/b} has been very helpful bringing in remorsefully wretched sinners."
    ang "{b}God{/b} will surely remember his fruits of love to his neighbors."
    show ang 1
    show debbie 3f
    deb "That's great!"
    deb "I know we all can be naughty at times..."
    show debbie 2f
    deb "Well then, I'd better get going. The laundry isn't going to fold itself."
    hide debbie with dissolve
    show ang 3
    player_name "..."
    show player 30
    player_name "What now?"
    player_name "I brought you {b}Helen{/b}. Isn't that enough?"
    show player 5
    show ang 4
    ang "Oh no my dear child. {b}God{/b} has many things in store for you."
    ang "{b}Helen{/b} is far from being purified. Her stubbornness is most annoying."
    show ang 3
    show player 26
    player_name "Tell me about it."
    show player 5
    show ang 2
    ang "The most penitent Christians require extra care."
    ang "They need to be broken down from their pedestal so that we may build them back up."
    ang "I believe it will take two more rituals for her..."
    ang "That is why I have come to see you."
    ang "I am in need of an essential tool used throughout biblical times."
    show ang 1
    show player 11
    player_name "..."
    show player 12
    player_name "What do you need?"
    show player 5
    show ang 2
    ang "I intend to subvert {b}Helen{/b} through the means of flagellation."
    show ang 1
    show player 12
    player_name "What?"
    show player 5
    show ang 4
    ang "Get me {b}a whip{/b}."
    show ang 3
    show player 23
    player_name "{b}A whip{/b}!?"
    show player 11
    show ang 4
    ang "I'd prefer a cat o' nine tails of which our {b}Savior{/b} was subjected to."
    ang "But I fear that might be more difficult to come by."
    ang "{b}A standard leather whip{/b} will do."
    show ang 2
    ang "Bring it to me in my chambers."
    show ang 1
    show player 10
    player_name "This doesn't seem right at-"
    show player 11
    show ang 2
    ang "Do you forget your place? Don't make me remind you and everyone else of your depraved sins!"
    show ang 1
    show player 15
    player_name "But you want to whip {b}Helen{/b}!"
    show player 16
    show ang 2
    ang "You made a deal with me. Don't question my...the church's methods."
    show ang 1
    show player 12
    player_name "It's just not right."
    show player 5
    show ang 4
    ang "And who are you to judge right from wrong?"
    show ang 3
    show player 24
    player_name "..."
    show player 12
    player_name "Fine. Where am I even supposed to get {b}a whip{/b} though?"
    show player 17
    player_name "Is there a listing of distributors in the back of the bible?"
    show player 5
    show ang 1
    ang "..."
    show ang 2
    ang "I'm sure someone of your age knows of dirty lustful places that sell such things."
    ang "Don't keep me waiting."
    hide ang with dissolve
    show player 37 with dissolve
    player_name "I should never have gone to church."
    pause
    show player 38 with dissolve
    player_name "Where am I going to get {b}a whip{/b}?"
    player_name "Maybe the {b}Pink store at the mall{/b} carries something like that."
    show player 37 with dissolve
    player_name "..."
    hide player with dissolve
    return

label entrance_mia_angelicas_final_home_visit:
    scene expression L_home_entrance.background with fade
    show player 11 at left
    show ang 2 at right
    with dissolve
    ang "It's about time you came downstairs."
    ang "I have need of you again."
    show ang 1
    show player 5
    player_name "..."
    show player 12
    player_name "I'm not sure I want to continue helping after what you did to {b}Helen{/b}, I-"
    show player 5
    show ang 4
    ang "Oh, don't be so naive!"
    ang "Despite her reluctance, we both know she enjoyed it."
    show ang 3
    show player 11
    player_name "..."
    show ang 2
    ang "I didn't come here to argue with a sinner."
    show ang 39 with dissolve
    ang "If you truly intend to help {b}Helen{/b} you will help me obtain this..."
    show ang 38
    pause
    show ang 3
    show player 459 at Position (xoffset=1)
    with dissolve
    player_name "..."
    hide player
    hide ang
    show note_01_c
    with dissolve
    pause
    hide note_01_c
    show player 1 at left
    show ang 3 at right
    show player 460 at Position (xoffset=1)
    with dissolve
    player_name "What...is it?"
    show player 461 at Position (xoffset=1)
    show ang 4
    ang "It is a crucial element to the final ritual of {b}Helen's{/b} purification..."
    ang "...And your last task."
    show ang 3
    show player 460 at Position (xoffset=1)
    player_name "But how is this going to be used to purify {b}Helen{/b}?"
    show player 11 with dissolve
    show ang 2
    ang "Don't question me!"
    ang "Sinners should just accept the words spoken by {b}God's{/b} chosen."
    ang "Now get me the item in the photograph and meet me in my chambers."
    show ang 1
    show player 5
    player_name "..."
    show player 12
    player_name "Alright..."
    show player 5
    show ang 2
    ang "Good. And be quick about it."
    hide ang with dissolve
    show player 5
    player_name "..."
    show player 10
    player_name "{b}Helen{/b} doesn't even seem to realize {b}Sister Angelica{/b} is transforming her into..."
    player_name "...A sex freak!"
    show player 12
    player_name "I should talk with {b}Harold{/b} before I help out {b}Sister Angelica{/b}."
    player_name "Maybe he can help me figure out what to do."
    show unlock55 at truecenter with dissolve
    $ player.get_item("strapon_drawing")
    pause
    hide unlock55 with dissolve
    hide player with dissolve
    return

label entrance_mom_overheard:
    scene expression game.timer.image("home_entrance{}")
    show player 34 with dissolve
    player_name "...{b}*distant voice*{/b}..."
    show player 35
    player_name "( Is that {b}[deb_name]{/b} on the phone? )"
    show player 12
    player_name "( ...She sounds like she's mad. Is she yelling? )"
    show player 10
    player_name "( I should go see if she's okay. )"
    hide player with dissolve
    return

label entrance_mom_lawn_help:
    scene expression L_home_entrance.background
    show player 1 at left
    show debbie 2 at right
    with dissolve
    if game.timer.is_morning():
        deb "Good morning, sweetie."
    else:
        deb "Hello, sweetie."
    show debbie 1
    show player 2
    if game.timer.is_morning():
        player_name "Morning, {b}[deb_name]{/b}."
    else:
        player_name "Hello, {b}[deb_name]{/b}."
    show player 1
    show debbie 2
    if game.timer.is_morning():
        deb "Ready for school?"
    else:
        deb "Happy to be back at school?"
    show debbie 1
    show player 10
    player_name "Yeah, I guess. I have so much homework to catch up on."
    show player 1
    show debbie 3
    deb "Oh, I'm sure you'll do fine."
    show debbie 2
    deb "It's good to get back into a normal routine."
    show debbie 1
    show player 14
    player_name "I guess."
    player_name "What are you doing today?"
    show player 13
    show debbie 13
    deb "Oh, me?"
    deb "Housework mostly. It keeps me pretty busy."
    deb "It's not easy taking care of this big place by myself you know?"
    show debbie 14b
    show player 5
    pause
    show player 2
    player_name "I could help, you know?"
    show player 1
    show debbie 13
    deb "You want to help with the house work?"
    show debbie 1
    show player 29 with dissolve
    player_name "Sure! I mean, I feel like I should pull my own weight around here..."
    show player 1 with dissolve
    show debbie 2
    deb "That's a great attitude to have, {b}[firstname]{/b}!"
    show debbie 1
    deb "Hmm..."
    show debbie 2
    deb "Well, the lawn hasn't been mowed in weeks."
    deb "You can start there if you want!"
    deb "The {b}lawn mower{/b} should be in the {b}garage{/b}."
    show debbie 1
    show player 14
    player_name "All right. I'll go take a look."
    show player 13
    show debbie 2
    deb "Thanks, {b}[firstname]{/b}."
    deb "Be careful!"
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_clothes_dirty:
    scene expression L_home_entrance.background
    show player 11 zorder 1 at left
    show xtra 15 zorder 2 at Position(xpos=170,ypos=754)
    show jenny 9 at right
    with dissolve
    jen "Eugh, what's that smell?!"
    show player 14
    show jenny 10
    player_name "... Me I think. I was outside mowing the law-"
    show player 11
    show jenny 9
    jen "That's disgusting! You're getting grass everywhere, you slob!"
    show player 12
    show jenny 10
    player_name "I'm sorry. I was just trying to help {b}[deb_name]{/b}."
    show player 11
    show jenny 9
    jen "So what, you're going to start doing chores around here now?"
    jen "You got a thing for {b}[deb_name]{/b} or something?"
    show player 10
    show jenny 10
    player_name "No! I'm just-"
    show player 11
    show jenny 9
    jen "Pfft, don't play dumb! I see what you're up to!"
    hide jenny with dissolve
    pause
    show player 12
    player_name "What's her problem?"
    show player 10
    player_name "Oh well, I should get these clothes {b}downstairs to the wash{/b}."
    hide player with dissolve
    return

label entrance_mom_debt_collectors:
    scene henchman_cs1 2 with fade
    show text "I was expecting to see {b}Erik{/b}, instead I saw a strange man...\nHe was wearing an all black suit coupled with a stern look that would put coach Bridget's to shame." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    scene henchman_cs1 1
    show player 2 at left
    show henchman2 1 at right
    with dissolve
    player_name "Hi?"
    show henchman2 2
    show player 1
    henchman2 "Where's the owner of this residence?"
    show henchman2 1
    show player 11
    player_name "..."
    show player 12
    player_name "Who's asking?"
    show player 11
    show henchman2 3
    henchman2 "It's personal matters, Kid."
    show henchman2 1
    show player 12
    player_name "Well, she's kind of busy at the moment, so why don't you come another time."
    show henchman2 2
    show player 11
    henchman2 "No need. Just give her this message."
    show henchman2 3
    henchman2 "She's running out of time. She better pay up or else!"
    henchman2 "My boss ain't the patient type."
    show henchman2 1
    show player 11
    player_name "..."
    show player 12
    player_name "Or else, what?"
    show player 11
    show henchman2 3
    henchman2 "Just give her the message, Kid."
    henchman2 "We'll be back soon..."
    show henchman2 1
    player_name "..."
    $ playMusic()
    hide henchman2
    with dissolve
    scene expression L_home_entrance.background
    show player 10 at left
    with fade
    player_name "( What was {b}that{/b} all about... )"
    show player 5
    show debbie 62 at right with dissolve
    deb "Was someone at the door, sweetie?"
    show player 10
    show debbie 61
    player_name "Yeah, some strange guy in a black suit came by..."
    show player 5
    show debbie 59
    deb "!!!"
    show player 11
    show debbie 60
    deb "...What did he want?"
    show debbie 59
    show player 10
    player_name "He said you need to pay up and that he'll be back soon, but refused to say why."
    show player 11
    show debbie 60
    deb "It must be about..."
    deb "But I already paid off all the-"
    show debbie 59
    deb "..."
    show player 10
    player_name "What is it?"
    show player 11
    show debbie 60
    deb "It's nothing, sweetie."
    show player 1
    show debbie 62
    deb "They must've gotten the wrong address, that's all."
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_pipe_help:
    scene expression L_home_entrance.background
    show player 11 at left
    show debbie 13 at right
    with dissolve
    deb "Sweetie! Thank God you're here!"
    show debbie 14b
    show player 10
    player_name "{b}[deb_name]{/b}?"
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} and I need your help."
    show debbie 14b
    show player 12
    player_name "Huh?"
    show player 5
    show debbie 13
    deb "There's a broken pipe upstairs and water everywhere!"
    deb "She's up there messing with it now."
    deb "Could you go and help her?"
    show debbie 14b
    show player 10
    player_name "Me? I err..."
    show player 5
    show debbie 13
    deb "I can't afford to call a repairman right now. Not with everything that's happened recently..."
    show debbie 14b
    show player 10
    player_name "Oh, right..."
    show player 14
    player_name "I'll go take a look."
    show player 13
    show debbie 2
    deb "Thanks, sweetie! Let me know if there's anything I can do to help."
    show debbie 1
    show player 14
    player_name "Alright."
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_movie_night:
    scene location_home_entrance_night_blur
    show player 1 at left
    show debbie 62 at right
    deb "Oh, hey, sweetie!"
    deb "Heading to bed?"
    show player 2
    show debbie 61
    player_name "Nah, just looking around for something to do..."
    show player 14
    player_name "Why, what are you up to?"
    show player 1
    show debbie 62
    deb "I was just thinking about starting a movie."
    show player 2
    show debbie 61
    player_name "Cool."
    show player 1
    deb "..."
    show debbie 63
    deb "Why don't you come join me?"
    show player 10
    show debbie 61
    player_name "Really?"
    show player 11
    show debbie 62
    deb "Sure, why not? It's still early and I would love the company!"
    show player 2
    show debbie 61
    player_name "Y-yeah, okay. That sounds nice, {b}[deb_name]{/b}."
    show player 1
    show debbie 62
    deb "Great!"
    deb "I'll go get situated and you just come join me when you're ready, alright?"
    show player 2
    show debbie 61
    player_name "Sounds good!"
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_hang_out:
    scene location_home_entrance_day_blur
    show player 1 at left with dissolve
    show debbie 165 at right with dissolve
    deb "Hey there, Sweetheart!"
    show player 2
    show debbie 164
    player_name "Hey {b}[deb_name]{/b}!"
    player_name "You look nice! Going somewhere?"
    show player 1
    show debbie 165
    deb "Oh, I just need to run to the {b}Mall{/b} and pick up a few things."
    show debbie 164
    deb "..."
    show debbie 165
    deb "Would you like to join me?"
    show player 11
    show debbie 164
    player_name "Hmm?"
    show player 10
    player_name "Oh I dunno, I was gonna-"
    show player 11
    show debbie 165
    deb "Aww, c'mon! It'll do you good to get some fresh air."
    show debbie 164
    player_name "..."
    show debbie 165
    deb "... And besides, I don't want to go all by myself..."
    deb "Won't you come and keep me company?"
    show debbie 164
    return

label entrance_mom_hang_out_yes:
    show player 2
    player_name "Heh, sheesh {b}[deb_name]{/b}! Alright, I'll go."
    show player 1
    show debbie 166
    deb "Great!"
    show debbie 165
    deb "I'll meet you in the car then, sweetie!"
    return

label entrance_mom_hang_out_no:
    show player 10
    player_name "Sorry {b}[deb_name]{/b}, I have something else planned for today..."
    show player 11
    show debbie 168
    deb "Oh."
    show debbie 169
    deb "..."
    show debbie 168
    deb "Okay, sweetie, well... Just stay safe and be home for dinner."
    show player 2
    show debbie 169
    player_name "Sure thing."
    return

label entrance_mom_spy:
    scene expression L_home_entrance.background
    show player 10 with dissolve
    player_name "Huh?"
    player_name "What was that noise?"
    show player 11
    pause
    show player 10
    player_name "Maybe the TV is on in the living room."
    hide player with dissolve
    return

label entrance_mom_kissing_practice:
    scene expression L_home_entrance.background
    show player 4 with dissolve
    player_name "I wonder if {b}[deb_name]{/b} would let me kiss her again if I asked?"
    player_name "I should {b}talk to her{/b} about it..."
    hide player with dissolve
    return

label entrance_mom_car_broken:
    scene expression L_home_entrance.background
    show debbie 3 at right
    show player 1 at left
    with dissolve
    deb "Good morning, sweetie."
    show debbie 1
    show player 14
    player_name "Morning, {b}[deb_name]{/b}."
    show player 13
    show debbie 2
    deb "Did you sleep well last night?"
    show debbie 1
    show player 10
    player_name "...Yeah... sorta."
    player_name "I've been having a lot of weird dreams lately."
    show player 11
    show debbie 2
    deb "Is that so? What kind of weird dreams?"
    show debbie 1
    show player 10
    player_name "Oh, umm..."
    player_name "Well, it's kinda embarrassing."
    show player 11
    show debbie 2
    deb "... Naughty dreams?"
    show debbie 1
    show player 10
    player_name "Err... Yeah."
    show player 11
    show debbie 2
    deb "Well that's nothing to be embarrassed about, Sweetheart!"
    show debbie 3
    deb "You're at that age after all."
    show debbie 1
    pause
    show debbie 2
    deb "So who's the lucky girl?"
    show player 10
    show debbie 1
    player_name "The girl?"
    player_name "Umm, I don't really wanna talk about it..."
    show player 11
    show debbie 3
    deb "Hehe, Oh? I wonder if it's somebody I would know?"
    show player 11
    player_name "..."
    show debbie 3
    deb "Oh, fine. Keep your secrets!"
    show debbie 2
    deb "While you're here, I need your help with something. Got a minute?"
    show debbie 14
    show player 10
    player_name "Uh... Yeah. What is it?"
    show player 1
    show debbie 13
    deb "Can you look at the car and see why it's not starting?"
    show debbie 1
    show player 10
    player_name "Didn't we just take it out the other day?"
    show player 1
    show debbie 13
    deb "Yeah but for some reason I can't get it started now!"
    show debbie 1
    show player 2
    player_name "You didn't leave the lights on and kill the battery again, did you?"
    show debbie 2
    show player 1
    deb "Hah, no... I mean, well... I don't think I did. Would you mind checking?"
    show debbie 1
    show player 14
    player_name "Not at all!"
    hide player
    hide debbie
    with dissolve
    return

label entrance_mom_panties_masturbation_again:
    scene expression L_home_entrance.background
    show player 1
    player_name "( I can't believe {b}[deb_name]{/b} actually rubbed my Cock! )"
    player_name "( ... a couple more seconds and I would have popped. )"
    player_name "( Arrgh, I want her so bad! This is torture! )"
    show player 11
    player_name "( .... )"
    player_name "( Hmm, I know I promised not to jerk off in her room but... )"
    show player 13
    player_name "( It just felt so good last time! )"
    player_name "( ... )"
    player_name "( Maybe if I do it quickly and quietly, I can snag a pair of her panties and bust a nut without her noticing. )"
    player_name "( She seems to be {b}busy in the [temp]{/b} which should allow me to sneak into her room and rub one out in her bed. )"
    player_name "( I think it's worth a shot... I need the release... To clear my head! )"
    hide player with dissolve
    return

label entrance_mom_diane_visit:
    scene expression L_home_entrance.background
    show player 34 with dissolve
    player_name "...{b}*distant voice*{/b}..."
    show player 35
    player_name "( Hmm, sounds like {b}[deb_name]{/b} is talking to someone in the kitchen... )"
    show player 12
    player_name "( I wonder who's here? )"
    show player 10
    player_name "( I should go take a look... )"
    hide player with dissolve
    return

label entrance_mom_vacuum:
    scene location_home_entrance_fight
    show debbie 94 at right with dissolve
    pause
    show debbie 95
    pause
    show debbie 94
    pause
    show debbie 95
    pause
    show debbie 94
    show player 1 at left with dissolve
    pause
    show debbie 95
    pause
    show debbie 97 with dissolve
    deb "Oh!!"
    deb "You startled me..."
    show debbie 98
    show player 17
    player_name "Sorry, {b}[deb_name]{/b}."
    show player 14
    player_name "I didn't mean to!"
    show debbie 97
    show player 1
    deb "Sorry about the noise."
    deb "I should be done with the vacuum soon."
    deb "... Ugh, this is killing my back!"
    show debbie 98
    return

label entrance_mom_vacuum_yes:
    show debbie 98 at right
    show player 14 at left
    player_name "Here, {b}[deb_name]{/b}, pass me the vacuum."
    show player 1
    show debbie 96
    deb "..."
    show debbie 97
    deb "You want the vacuum?"
    show debbie 96
    show player 14
    player_name "Yeah, I'll take over from here."
    player_name "You should rest your back for a bit..."
    show player 10
    player_name "No sense in working yourself so hard when I'm here to help."
    show debbie 97
    show player 11
    deb "No, it's okay, sweetie. You don't have-"
    show debbie 98
    show player 10
    player_name "I know I don't have to help, {b}[deb_name]{/b}."
    player_name "I want to do it."
    show debbie 97
    show player 1
    deb "Well, if you insist..."
    show player 257
    show debbie 100
    with dissolve
    deb "This is very sweet of you."
    show player 259
    show debbie 99
    player_name "Not a problem!"
    hide player
    hide debbie
    with dissolve
    scene expression "backgrounds/location_home_cutscene02.jpg"
    show expression FilteredText("I felt bad {b}[deb_name]{/b} was having a hard time with her back pain. \nThe least I could do was help her out, even if it took me forever to finish. \nThe stairs were the worst part! No wonder her back is hurting her... \nAt least {b}[deb_name]{/b} kept me company while I worked.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    return

label entrance_mom_vacuum_no:
    show debbie 96 at right
    show player 10 at left
    player_name "Can you please finish cleaning another time?"
    player_name "I'm trying to study upstairs and all this noise is distracting."
    show debbie 97
    show player 11
    deb "I'm sorry, sweetie!"
    deb "I had no idea you were upstairs studying."
    show debbie 96
    show player 14
    player_name "It's okay, {b}[deb_name]{/b}."
    show debbie 97
    show player 1
    deb "It'll be good to rest my back for a bit anyways..."
    show debbie 96
    show player 17
    player_name "Thanks!"
    hide player
    hide debbie
    with dissolve
    return

label entrance_sis_couch_1:
    scene expression L_home_entrance.background
    show player 11 with dissolve
    player_name "( What's that sound? )"
    player_name "( It sounds like the TV is on. )"
    show player 4 at Position(xpos=518)
    player_name "( Who could be watching TV this late? )"
    hide player with dissolve
    return

label entrance_sis_couch_2:
    scene expression L_home_entrance.background
    show player 26 with dissolve
    player_name "( That porno {b}[jen_name]{/b} was watching was hot! I kind of feel like watching it, too... )"
    show player 33
    player_name "Hmm... Maybe {b}another night{/b}."
    hide player with dissolve
    return

label entrance_sis_couch_3:
    scene expression L_home_entrance.background
    show player 11 with dissolve
    player_name "( What was that sound? )"
    hide player with dissolve
    return

label entrance_bissette_roxxy_jenny_mentoring:
    scene expression L_home_entrance.background
    show player 13 at Position (xpos=300)
    show debbie 2 at right
    with dissolve
    deb "Sweetie, somebody is at the door! Can you get it?"
    show debbie 1
    show player 14
    player_name "Sure thing, {b}[deb_name]{/b}!"
    show player 10
    show roxxy 1 at Position (xpos=600) with dissolve
    player_name "Hey {b}Roxxy{/b}! You here for your session with {b}[jen_name]{/b}?"
    show player 5
    show roxxy 2
    rox "Duh. What do you think I'm here to see you or something?!"
    show roxxy 1
    show player 21
    player_name "... No."
    show player 5
    show roxxy 2
    rox "Good, cause there is no fucking way-"
    show roxxy 1
    show jenny 9f at left with dissolve
    jen "*Ahem*"
    jen "Is this that girl you wanted me to help?"
    show jenny 12f
    jen "You know, the one you're trying to bang?"
    show jenny 11f
    hide xtra
    show player 11
    with dissolve
    show debbie 14
    player_name "!!!" with hpunch
    show roxxy 3
    rox "EXCUSE ME!?"
    show roxxy 14
    show player 113
    player_name "N-no!!"
    show player 10
    player_name "{b}Roxxy{/b}, I swear I never said-"
    show player 11
    show roxxy 2
    rox "As if you even have a shot... Not even in your dreams, Twerp!"
    show roxxy 1
    show player 37 at Position (xoffset=41) with dissolve
    show jenny 12f
    jen "Aww, too bad little pervert."
    jen "I guess you're stuck with your hand and a bottle of lotion."
    show jenny 11f
    show roxxy 4
    rox "Hah! Yeah, and I feel sorry for the lotion..."
    show roxxy 1
    show jenny 12f
    jen "Hahaha! Oh, I like you! {b}Roxxy{/b} was it?"
    show jenny 11f
    show roxxy 1b
    rox "Yeah, and you're {b}[jen_name]{/b}?"
    show roxxy 1
    show jenny 12f
    jen "That's right."
    jen "C'mon, {b}Roxxy{/b}. We can ditch the dweeb and get started in my room."
    show jenny 11f
    show roxxy 1b
    rox "Gladly."
    show roxxy 2
    rox "See ya, dweeb!"
    hide roxxy
    hide jenny
    show player 25
    with dissolve
    player_name "..."
    show player 24
    player_name "I have a bad feeling about this."
    hide player
    hide debbie
    with dissolve

    scene location_home_entrance_cutscene04
    with fade
    show text "Those two had formed a connection almost instantly...\nI guess {b}[jen_name]{/b} and {b}Roxxy{/b} did have a lot in common." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    show text "They were both Captains of the cheer squad, popular, beautiful,\nand both of them had mastered the art of being a bitch..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    show text "I really hope I don't end up regretting this..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    with dissolve

    scene expression L_home_entrance.background
    show player 24 at Position (xpos=300)
    show debbie 13 at right
    with dissolve
    deb "Who was that?"
    show debbie 14
    show player 10
    player_name "Just a girl from my school. {b}[jen_name]{/b} agreed to help her with some cheer-leading stuff."
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} is helping somebody?"
    show debbie 3
    deb "That's a new one."
    show debbie 1
    show player 12
    player_name "Yeah, because I paid her..."
    show player 90
    show debbie 13
    deb "Ah."
    deb "Sweetie, you really shouldn't let {b}[jen_name]{/b} take advantage of you like that..."
    show debbie 14
    show player 12
    player_name "Yeah, I know."
    show player 90
    player_name "..."
    show debbie 13
    deb "Something else on your mind?"
    show debbie 14
    show player 12
    player_name "I've just never seen {b}[jen_name]{/b} hit it off with someone like that..."
    show player 10
    player_name "Kinda freaks me out, to be honest."
    show player 5
    show debbie 2
    deb "Well, I think it's a good thing she's made a new friend."
    deb "I worry about her sitting upstairs by herself all day..."
    show debbie 13
    deb "I'm sure she gets lonely."
    show debbie 14
    show player 10
    player_name "I doubt it."
    show player 5
    player_name "..."
    show player 11
    jen "Hahahaha!!"
    show player 10
    player_name "...{b}Maybe I should go check on them{/b}?"
    show player 5
    show debbie 2
    deb "Maybe."
    show debbie 13
    deb "...Just be careful, sweetie."
    hide player
    hide debbie
    with dissolve
    return

label entrance_bissette_roxxy_jenny_mentoring_sex:
    scene expression L_home_entrance.background
    show player 13 at Position (xpos=300)
    show debbie 2 at right
    with dissolve
    deb "Sweetie, somebody is at the door! Can you get it?"
    show debbie 1
    show player 14
    player_name "Sure thing, {b}[deb_name]{/b}!"
    show player 10
    show roxxy 1 at Position (xpos=600) with dissolve
    player_name "Hey {b}Roxxy{/b}! You here for your session with {b}[jen_name]{/b}?"
    show player 5
    show roxxy 2
    rox "Yup. It's still on, right?"
    show roxxy 1
    show player 21
    player_name "Absolutely."
    show player 5
    show roxxy 2
    rox "Awesome! I'm so excited to-"
    show roxxy 1
    show jenny 9f at left with dissolve
    jen "*Ahem*"
    jen "Is this that girl you wanted me to help?"
    show jenny 12f
    jen "You know, the one you're trying to bang?"
    show jenny 11f
    hide xtra
    show player 11
    with dissolve
    show debbie 14
    player_name "!!!" with hpunch
    show roxxy 4
    rox "... Hahaha!"
    show roxxy 14
    show player 113
    player_name "I didn't-"
    show player 10
    player_name "{b}Roxxy{/b}, I swear I never said-"
    show player 11
    show roxxy 1h
    rox "What exactly have you been telling them, {b}[firstname]{/b}?"
    show roxxy 1
    show player 37 at Position (xoffset=41) with dissolve
    show jenny 12f
    jen "Wait a second..."
    jen "You mean, you... A-and him?!"
    show jenny 11f
    show roxxy 4
    rox "Uhh yeah?!"
    rox "So long as he keep taking good care of me..."
    rox "... And doesn't get fat or lose his hair, yuck!"
    show roxxy 1
    show jenny 12f
    jen "Hahaha! Oh, I like you! {b}Roxxy{/b} was it?"
    show jenny 11f
    show roxxy 1b
    rox "Yeah, and you're {b}[jen_name]{/b}?"
    show roxxy 1
    show jenny 12f
    jen "That's right."
    jen "C'mon, {b}Roxxy{/b}. We'll do this in my room."
    show jenny 11f
    show roxxy 1b
    rox "Alright."
    show roxxy 2
    rox "Thanks again, {b}[firstname]{/b}."
    hide roxxy
    hide jenny
    show player 25
    with dissolve
    player_name "..."
    show player 24
    player_name "I have a bad feeling about this."
    hide player
    hide debbie
    with dissolve
    scene expression L_home_entrance.background
    show player 24 at Position (xpos=300)
    show debbie 13 at right
    with dissolve
    deb "So you two are dating now?"
    show debbie 14
    show player 10
    player_name "Heh, yeah. {b}[jen_name]{/b} agreed to help her with some cheer-leading stuff."
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} is helping somebody?"
    show debbie 3
    deb "That's a new one."
    show debbie 1
    show player 12
    player_name "Yeah, because I paid her..."
    show player 90
    show debbie 13
    deb "Ah."
    deb "Sweetie, you really shouldn't let {b}[jen_name]{/b} take advantage of you like that..."
    show debbie 14
    show player 12
    player_name "Yeah, I know."
    show player 90
    player_name "..."
    show debbie 13
    deb "Something else on your mind?"
    show debbie 14
    show player 12
    player_name "I've just never seen {b}[jen_name]{/b} hit it off with someone like that..."
    show player 10
    player_name "Kinda freaks me out, to be honest."
    show player 5
    show debbie 2
    deb "Well, I think it's a good thing she's made a new friend."
    deb "I worry about her sitting upstairs by herself all day..."
    show debbie 13
    deb "I'm sure she gets lonely."
    show debbie 14
    show player 10
    player_name "I doubt it."
    show player 5
    player_name "..."
    show player 11
    jen "Hahahaha!!"
    show player 10
    player_name "...{b}Maybe I should go check on them{/b}?"
    show player 5
    show debbie 2
    deb "Maybe."
    show debbie 13
    deb "...Just be careful, sweetie."
    hide player
    hide debbie
    with dissolve
    return

label entrance_bissette_roxxy_jenny_spying:
    scene expression L_home_entrance.background
    show player 10 with dissolve
    player_name "I should go check on {b}Roxxy{/b} and {b}[jen_name]{/b}..."
    hide player with dissolve
    return

label entrance_diane_debbie_evening_visit_overhear:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 34 with dissolve
    player_name "( Hmm? )"
    player_name "( Is that {b}Diane{/b}? )"
    player_name "( {b}[deb_name]{/b} must have invited her over. )"
    player_name "( {b}I wonder what they're talking about?{/b} )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
