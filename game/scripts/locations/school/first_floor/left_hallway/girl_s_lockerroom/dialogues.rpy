label girls_lockerroom_judith_in_girls_bathroom:
    scene girl_lockerroom
    show player 106 at left with dissolve
    player_name "Woah! There's a big hole in the ground in here..."
    player_name "( No wonder they had to close this lockeroom! )"
    show player 90
    player_name "..."
    show player 10
    player_name "( I can still hear sobbing. )"
    player_name "( There's definitely {b}someone in here{/b}... )"
    hide player 10 with dissolve
    return

label girls_lockerroom_judith_toilet_first_intro:
    scene expression game.timer.image("backgrounds/location_school_locker_room_broken_stall{}.jpg")
    show judith 11 zorder 1 at Position( xpos = 310, ypos = 768) with dissolve
    window hide
    pause
    show player 106f zorder 0 at Position (xpos = 639, ypos = 768) with dissolve
    player_name "!!!"
    jud "{b}*Sobbing*{/b}"
    show player 108
    player_name "{b}Judith{/b}?!"
    show judith 13
    show player 109
    jud "...Hey, {b}[firstname]{/b}."
    show judith 12
    show player 108
    player_name "Are you okay?"
    show judith 13
    show player 109
    jud "I just wanted to stay away, from everyone."
    show judith 12
    show player 108
    player_name "What do you mean?"
    show judith 13
    show player 109
    jud "No one likes me... And everyone makes fun of my body..."
    jud "...so at least in here I won't be made fun of."
    show judith 12
    show player 108
    player_name "You can't let these people get to you that way!"
    show judith 13
    show player 109
    jud "They're right, though. I am ugly..."
    return

label girls_lockerroom_judith_toilet_first_not_ugly:
    show player 111
    show judith 12
    player_name "I don't think you're ugly at all!!"
    show judith 15
    show player 110
    jud "...Really?"
    show judith 14
    show player 111
    player_name "Yeah!"
    player_name "I think you look good!"
    show judith 15
    show player 110
    jud "That's...the nicest thing anyone has said to me..."
    show judith 14
    show player 111
    player_name "Well, I'm just being honest... And I'm sure I'm not the only one!"
    player_name "You just have to ignore all the negative stuff at school."
    show judith 15
    show player 110
    jud "I guess you're right..."
    show judith 14
    show player 111
    player_name "Anyway, we should get out of here and get back to class."
    show judith 17
    show player 106f
    jud "Wait!!"
    jud "Stay here a little longer... With {b}me{/b}..."
    return

label girls_lockerroom_judith_toilet_first_ok:
    show judith 16
    show player 111
    player_name "Oh... Okay."
    show judith 17
    show player 110
    jud "Do you remember the other day when..."
    jud "...We were both in the lockeroom? In front of {b}Annie{/b}?"
    show judith 16
    show player 111
    player_name "Yeah?"
    show judith 17
    show player 110
    jud "Well I... I liked the way you looked at me."
    show judith 16
    show player 106f
    player_name "!!!"
    show judith 17
    jud "It wasn't just your eyes... Your body was also reacting."
    show judith 16
    player_name "..."
    show judith 17
    jud "Was it my {b}breasts{/b} that made you... So happy? {b}Down there{/b}?"
    show judith 16
    show player 111
    player_name "I... I'm sorry!"
    show judith 17
    show player 106f
    jud "Don't be sorry!!"
    jud "...I really liked it and..."
    jud "...I was wondering If I could, you know, see it again?"
    return

label girls_lockerroom_judith_toilet_first_sure:
    show judith 16
    show player 111
    player_name "I guess so..."
    show judith 17
    show player 106f
    jud "Let me do it."
    hide player
    show judith 18 at Position(xpos = 447, ypos = 768)
    player_name "!!!"
    show judith 19
    window hide
    pause
    show judith 20
    window hide
    pause
    show judith 21
    window hide
    pause
    show judith 22
    window hide
    pause
    show judith 24
    jud "It's so... Nice..."
    jud "...And thick."
    show judith 23
    player_name "{b}*Gasp*{/b}"
    show judith 24
    jud "I just love how it feels in my hand..."
    show judith 25_23
    pause 4
    jud "..."
    show judith 23
    jud "Would you like to touch my breasts?"
    return

label girls_lockerroom_judith_toilet_first_yes:
    player_name "Yeah! I'd love to..."
    show judith 33
    player_name "..."
    show judith 34
    player_name "Wow..."
    show judith 35
    jud "Go ahead!"
    jud "Touch them... But be gentle! They're really sensitive..."
    show judith 36_37_38
    pause 4
    show judith 39 with hpunch
    jud "*Moaning*"
    player_name "!!!"
    show judith 33
    jud "It's just too much. My body get's all fuzzy when you touch my nipples..."
    show judith 4f zorder 1 at Position( xpos = 310, ypos = 768)
    show player 112 zorder 0 at Position (xpos = 639, ypos = 768)
    player_name "I didn't mean to hurt you."
    show player 13f
    show judith 5f
    jud "No, it's fine! It felt really good... I'm just sensitive..."
    show judith 4f
    show player 10f
    player_name "Maybe we should stop..."
    show player 13f
    show judith 5f
    jud "Yeah... Thanks for staying with me, I feel much better..."
    show judith 2f
    jud "...And if you want, we could do this again, some time..."
    show judith 4f
    show player 17f
    player_name "I'd like that!"
    show judith 5f
    show player 13f
    jud "I'll see you later then."
    hide player
    hide judith
    with dissolve
    return

label girls_lockerroom_judith_toilet_first_should_stop:
    show judith 24
    player_name "I think we should stop..."
    show judith 6f zorder 1 at Position( xpos = 310, ypos = 768)
    show player 112 zorder 0 at Position (xpos = 639, ypos = 768)
    player_name "We can't be late for class and {b}Annie{/b} could see us in here..."
    show player 13f
    show judith 2f
    jud "I understand. Thanks for staying with me..."
    show judith 3f
    jud "...And if you want, we could do this again, some time..."
    show judith 4f
    show player 17f
    player_name "I'd like that!"
    show player 13f
    show judith 5f
    jud "I'll see you later then."
    return

label girls_lockerroom_judith_toilet_first_cant:
    show judith 16
    show player 108
    player_name "I can't do that right now, {b}Judith{/b}..."
    player_name "Also, we should really go... I don't want to be late and {b}Annie{/b} could see us in here..."
    show judith 13
    show player 109
    jud "Oh..."
    jud "You can go, then. I'll stay here a little bit longer I think..."
    show player 111
    show judith 14
    player_name "Alright, I'll see you later then."
    return

label girls_lockerroom_judith_toilet_should_leave:
    show judith 16
    show player 108
    player_name "We should really go... I don't want to be late and {b}Annie{/b} is already on my case..."
    show judith 13
    show player 109
    jud "Oh..."
    jud "You can go, then. I'll stay here a little bit longer I think..."
    show judith 14
    show player 111
    player_name "Alright, I'll see you later then."
    return

label girls_lockerroom_judith_toilet_first_ugly:
    show judith 12
    show player 108
    player_name "I know, but you have to learn to deal with it!"
    show player 109
    jud "..."
    show judith 11
    jud "{b}*Sobbing*{/b}"
    show player 108
    player_name "I'm sorry..."
    show player 106f
    jud "I just want to be alone right now."
    show player 108
    player_name "I'll see you later, then..."
    return

label girls_lockerroom_judith_toilet_not_here:
    scene expression game.timer.image("backgrounds/location_school_locker_room_broken_stall{}.jpg")
    show player 11 with dissolve
    player_name "..."
    show player 10
    player_name "( {b}Judith{/b} is not here. )"
    player_name "( She must be in the hallway or at home. )"
    show player 108f
    player_name "( I should ask her to come in for {b}some fun{/b}. )"
    hide player 108f
    return

label judith_toilet_replay:
    scene expression game.timer.image("toilet_stall{}")
    show judith 14 zorder 1 at Position( xpos = 310, ypos = 768)
    show player 111 zorder 0 at Position (xpos = 639, ypos = 768) with dissolve
    player_name "Hey!"
    show judith 15
    show player 110
    jud "I was hoping you'd come see me..."
    jud "Did anyone see you come in here?"
    show judith 14
    show player 108
    player_name "I don't think so?"
    show judith 14
    show player 110
    jud "Oh, good..."
    jud "Emm... So? What do you feel like doing?"
    call screen judith_stage01

label judith_kiss:
    show player 108
    show judith 14
    player_name "Hmm... Have you ever kissed someone?"
    show judith 15
    show player 110
    jud "You mean, like a... Kiss, kiss?"
    show judith 14
    show player 17f
    player_name "Well, yeah!"
    show judith 13
    show player 110
    jud "Not really..."
    show judith 14
    show player 17f
    player_name "Let's try it!"
    show judith 4f
    show player 110
    jud "..."
    hide player
    show judith 31_32 at Position ( xpos = 380, ypos = 768)
    with dissolve
    pause 4
    show judith 5f zorder 1 at Position( xpos = 320, ypos = 768)
    show player 13f zorder 0 at Position (xpos = 640, ypos = 768)
    with dissolve
    jud "That... Was good..."
    show judith 4f
    show player 17f
    player_name "Feels a bit strange I guess. Ha ha."
    show judith 5f
    show player 11f
    jud "Let's do something else!"
    show judith 4f
    show player 14f
    player_name "Okay..."
    call screen judith_stage02

label judith_handjob:
    show player 111
    show judith 16
    player_name "We could do like last time, I guess?"
    show judith 17
    show player 106f
    jud "Let me do it."
    hide player
    show judith 18 at Position(xpos = 465, ypos = 768)
    player_name "!!!"
    show judith 19
    window hide
    pause
    show judith 20
    window hide
    pause
    show judith 21
    window hide
    pause
    show judith 22
    window hide
    pause
    show judith 24
    jud "It's so... Nice..."
    jud "...And thick."
    show judith 23
    player_name "{b}*Gasp*{/b}"
    show judith 24
    jud "I just love how it feels in my hand..."
    show judith 25_23
    pause 4
    player_name "That feels sooo... good!"
    show judith 24
    jud "You want me to stop?"
    call screen judith_stage03

label judith_keepgoing:
    show judith 25_23
    pause 4
    player_name "That feels sooo... good!"
    show judith 24
    jud "You want me to stop?"
    call screen judith_stage03

label judith_playwithtits:
    show judith 33
    jud "..."
    show judith 35
    jud "You like feeling them?"
    show judith 34
    player_name "Yeah..."
    show judith 36
    player_name "Your breasts are so nice and soft..."
    show judith 36_37_38
    pause 4
    show judith 39 with hpunch
    jud "{b}*Moaning*{/b}"
    player_name "!!!"
    show judith 35
    jud "You want to try something else?"
    call screen judith_stage03

label judith_cum:
    show judith 25_23
    pause 4
    show judith 26
    pause .3
    show judith 27
    jud "..."
    show judith 28
    jud "Wow, that's a lot of cum!"
    show judith 29
    player_name "Sorry! I didn't mean to make a mess..."
    show judith 28
    jud "It's fine..."
    jud "I always wanted to know how that feels!"
    show judith 30
    player_name "Oh. Ha ha!"
    show judith 5f zorder 1 at Position( xpos = 300, ypos = 768)
    show player 13f zorder 0 at Position (xpos = 623, ypos = 768)
    jud "We could do this again..."
    show player 17f
    show judith 4f
    player_name "I'd like that!"
    show player 13f
    show judith 5f
    jud "Me too..."
    show player 2f
    show judith 4f
    player_name "We should get out of here..."
    show player 1f
    show judith 5f
    jud "Okay!"
    $ renpy.end_replay()
    $ M_judith.set("in bathroom", False)
    $ M_judith.unforce()
    $ persistent.cookie_jar["Judith"]["unlocked"] = True
    $ persistent.cookie_jar["Judith"]["gallery"]["02_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_school_lefthallway)
    $ game.main()

label judith_pullpants:
    show judith 24
    jud "I'm not... Ready for that yet."
    show judith 23
    player_name "Oh... It's okay! We don't have to."
    show judith 24
    jud "Maybe another time..."
    jud "...When I feel a bit more comfortable."
    show judith 23
    player_name "I'm ok with that."
    show judith 24
    jud "Can we do something else?"
    call screen judith_stage03

label girls_lockerroom_roxxy_lockerroom_event:
    scene expression game.timer.image("location_school_locker_room_broken{}_blur")
    show missy 1 at Position (xpos=400)
    show becca 1 at left
    show roxxy 3 at right
    with dissolve
    rox "It's total bullshit!"
    show roxxy 3d
    show becca 2
    becca "I can't believe {b}Coach Bridget{/b} really suspended you from the team!"
    show becca 1
    show missy 2
    missy "Yeah, doesn't she realize that the team is going to suck hardcore with you?"
    show missy 1
    show becca 6
    becca "Well, we aren't THAT bad."
    show becca 1
    show missy 1bf with dissolve
    missy "... Please. You can't even do a proper toe touch!"
    show missy 2bf
    show becca 2
    becca "Hey, I can too!"
    show becca 6
    becca "I just don't like to do them cause it makes my tits sore!"
    show becca 8
    becca "You'd understand if you weren't such a stick!"
    show becca 7
    show missy 4f
    missy "Screw you, Skank! {b}Roxxy{/b} does them just fine and she's got bigger tits than you do!"
    show missy 4bf
    show becca 8
    becca "Pfft, yeah well... EVERYONE has bigger tits than you!"
    show becca 7
    show missy 4f
    missy "Oh, that's it! I'm gonna-"
    show roxxy 31
    rox "Would you two cut it out?"
    show missy 3 with dissolve
    show roxxy 3
    rox "Focus on me and my problems!"
    show roxxy 3d
    show missy 1b
    missy "Sorry, {b}Roxxy{/b}."
    show missy 1
    show becca 2
    becca "I just don't know what to tell you..."
    show becca 1
    show roxxy 3
    rox "Well, I can't steal homework from that four-eyed cow anymore."
    rox "If I get caught again, they're going to expel me."
    show roxxy 3d
    show missy 3
    missy "..."
    show becca 2
    becca "What about {b}Dexter{/b}?"
    show becca 1
    show missy 1
    rox "..."
    show roxxy 2
    rox "What about him?"
    show roxxy 1
    show becca 2
    becca "He's your boyfriend, isn't he?"
    show becca 1
    show roxxy 3c
    rox "... Yeah, so?"
    rox "He's too stupid to help me with my homework if that's where you're going with this..."
    rox "... He can barely read."
    show roxxy 3d
    show missy 6
    missy "Hahaha!"
    show roxxy 31
    rox "Shut up, {b}Missy{/b}!"
    show roxxy 3b
    show missy 1b
    missy "... Sorry."
    show missy 1
    show becca 2
    becca "You don't need him to help you do the homework. Just have him steal someone elses homework for you!"
    show becca 1
    show roxxy 29
    rox "... Hmm."
    show roxxy 30
    rox "That's not bad."
    rox "I can continue on the same way but without any of the risk."
    show roxxy 29
    show missy 2
    missy "... So {b}Dexter{/b} really can't read?"
    show missy 1
    show roxxy 3
    rox "... {b}Missy{/b} drop it."
    show roxxy 3d
    show missy 1b
    missy "Hehe, I'm sorry it's just kind of funny is all."
    show missy 1
    show becca 2
    becca "Who cares if he can read?"
    becca "He's the most popular guy in school AND he has a car!"
    show becca 1
    show roxxy 2
    rox "Yeah."
    rox "... And he's old enough to buy us alcohol!"
    show roxxy 1
    show missy 8
    missy "You're right, that's definitely a perk!"
    show missy 7
    show becca 2
    becca "So you're all set then?"
    show becca 1
    show missy 1
    show roxxy 1b
    rox "Not quite."
    rox "{b}Dexter{/b} can steal work for the {b}French Bitch{/b} and {b}Miss Ross{/b} is easy enough to please."
    rox "I just need to tell her she's pretty and pretend I'm interested in her stupid art."
    show roxxy 3c
    rox "... But what am I going to do for {b}Miss Dewitt's class{/b}?"
    show roxxy 1
    becca "..."
    show missy 1b
    missy "Just pick up the flute like {b}Becca{/b} and I did."
    show missy 1
    show roxxy 3c
    rox "Ugh, seriously?"
    show roxxy 1
    show missy 1b
    missy "Yeah, it's not that hard."
    missy "... And it's good practice, you know..."
    show missy 8
    missy "... For blowjobs!"
    show missy 7
    show roxxy 2
    rox "Pfft, yeah right!"
    show roxxy 1
    show missy 2
    missy "I'm serious!"
    show missy 5
    missy "... Or well, that's what {b}my sister{/b} says..."
    show missy 1
    show roxxy 2
    rox "Playing a musical instrument and sucking dick are two completely different things, you dumb slut."
    show roxxy 1
    show missy 3
    missy "..."
    show becca 2
    becca "Yeah and didn't your sister get fired from her job at {b}Consum-R{/b} because she couldn't count the register properly?"
    show becca 1
    show missy 2f with dissolve
    missy "Huh?"
    show missy 4f
    missy "... No!"
    show missy 2f
    missy "I mean..."
    show missy 4f
    missy "... Shut up, {b}Becca{/b}!"
    show missy 2bf
    show becca 4
    becca "Pffftt!!!"
    show becca 8
    becca "\"My sister says...\""
    show becca 4
    becca "Hahaha!"
    show missy 2 with dissolve
    missy "Look, I'm just saying go with the flute and we can help you practice."
    show missy 1
    becca "Hahaha!"
    show becca 1
    show missy 4f with dissolve
    missy "I said shut up, {b}Becca{/b}!!"
    show missy 2bf
    show roxxy 2
    rox "Ugh, both of you shut up..."
    show missy 1 with dissolve
    show roxxy 1b
    rox "C'mon, we better get going or the {b}French Bitch{/b} is gonna lecture us with her mush mouth again."
    show roxxy 1
    show becca 4
    becca "Haha!"
    hide becca
    hide missy
    hide roxxy
    with dissolve

    scene expression game.timer.image("lefthall{}")
    show player 23 at left with dissolve
    player_name "( Oh crap! They're coming this way! )"
    show player 22
    show roxxy 1 at Position (xpos=500)
    show missy 1f at Position (xpos=700)
    show becca 2f at right
    with dissolve
    becca "Hey, were you spying on us?!"
    show becca 1f
    show roxxy 3c
    rox "What the hell you perv!"
    show roxxy 3b
    show missy 8f
    missy "Hi, {b}[firstname]{/b}."
    show missy 7f
    show roxxy 3cf at Position (xoffset=-50) with dissolve
    becca "..."
    show missy 3f
    rox "..."
    show missy 2f
    missy "I mean... Yeah, what the fuck, nerd?!"
    show roxxy 3c with dissolve
    show missy 1f
    show player 12
    player_name "I wasn't-"
    show player 22
    show roxxy 3
    rox "Don't lie!"
    show roxxy 3d
    show becca 2f
    becca "Yeah, it's obvious you were listening!"
    show becca 1f
    show player 24
    player_name "... Fine."
    show player 12
    player_name "I was listening, you happy?"
    show player 24
    show roxxy 3
    rox "Eugh, you're such a loser..."
    show roxxy 3d
    show player 12
    player_name "You know, having {b}Dexter{/b} steal people's homework isn't going to work..."
    player_name "The teachers are going to know you didn't write it."
    show player 16
    show becca 8f
    becca "Pfft, what do you know?!"
    show becca 7f
    show roxxy 3c
    rox "... And why do you care?"
    show roxxy 3d
    show player 12
    player_name "I don't care!"
    player_name "Flunk out and prove everybody right about you."
    player_name "It won't bother me one bit..."
    hide player with dissolve
    show roxxy 29
    rox "..."
    show missy 8f
    missy "Bye, {b}[firstname]{/b}!"
    show missy 7f
    show roxxy 3cf at Position (xoffset=-50) with dissolve
    show becca 2f
    becca "What the hell, {b}Missy{/b}?"
    show becca 1f
    show missy 2 with dissolve
    missy "... What?"
    scene black
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
