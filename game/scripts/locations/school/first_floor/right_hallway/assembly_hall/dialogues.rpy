label assembly_hall_dewitt_graffit_mess:
    scene assembly_hall_cs05
    with fade
    show text "The state of the assembly hall was beyond my wildest imagination..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene assembly_hall_podium_paint
    show eve 1f at Position (xpos=300)
    show kevin 23f at Position (xpos=25)
    show player 22 at left
    show dewitt 11bf at Position (xpos=500)
    with dissolve
    dewitt "This is unbelievable!"
    show dewitt 10bf
    show player 10 with dissolve
    player_name "Holy crap, what a mess..."
    show player 11 with dissolve
    show dewitt 11bf
    dewitt "It's ruined! I just..."
    dewitt "I can't believe it!"
    show dewitt 10bf
    show player 35b
    show kevin 24f
    kev "Who would have done this?"
    show kevin 23f
    show player 11
    show dewitt 14f
    dewitt "{b}Principal Smith{/b} that's who!"
    show dewitt 13f
    show kevin 24f
    kev "You think the principal snuck in here and spray painted a dick on the wall?"
    show kevin 23f
    show dewitt 14f
    dewitt "No."
    dewitt "... But I betcha that bitch is behind it somehow!"
    dewitt "She'll do anything she can to get my show cancelled!"
    show dewitt 13f
    show principal 27 at right with dissolve
    smi "What in the world is going on in here?"
    show principal 26
    show dewitt 14 at Position (xpos=450) with dissolve
    dewitt "Speak of the devil."
    show dewitt 13
    show principal 27
    smi "*Gasp* Who is responsible for this mess?!"
    show principal 26
    show eve 10
    eve "We're not sure, ma'am. We just came in and found it this way."
    show eve 9
    show principal 27
    smi "Tsk, I bet it was {b}Eve's{/b} little band of hooligans again."
    show principal 26
    show eve 2bf
    eve "What?! My friends didn't do this!"
    show eve 1f
    show dewitt 14
    dewitt "Mmmhmm."
    dewitt "You think you're slick but I know you're behind this!"
    show dewitt 13
    show principal 27
    smi "Why {b}Melody{/b}, what an awful thing to say!"
    smi "You think I would vandalize my own school?"
    show principal 26
    show player 16
    show dewitt 14
    dewitt "Hell yeah, I think you would!"
    show dewitt 13
    show principal 27
    smi "Oh, don't be so dramatic..."
    smi "I'll try and organize a cleaning crew."
    smi "Though, I'm afraid I won't be able to get one in time for your show."
    smi "Such a pity..."
    show principal 26
    show dewitt 14
    dewitt "Grrr!!!"
    show dewitt 13
    show principal 27
    smi "Oh well, no use crying over spilled milk..."
    smi "You all have a good day now."
    show principal 38 at Position (xoffset=70) with dissolve
    smi "Hahahahaha!"
    hide principal with dissolve
    dewitt "..."
    show eve 2bf
    eve "I swear, my friends didn't do this, {b}Miss Dewitt{/b}."
    show eve 1f
    show player 5
    show dewitt 11bf at Position (xpos=700) with dissolve
    dewitt "I know, sweetie."
    show dewitt 9ff with dissolve
    pause
    show dewitt 9df with dissolve
    dewitt "I just..."
    dewitt "Excuse me, I need to go collect myself..."
    hide dewitt with dissolve
    show eve 9
    show player 11
    eve "..."
    show kevin 24 at Position (xpos=600) with dissolve
    kev "Aww, I feel so bad for her."
    show kevin 23
    show eve 10
    eve "Yeah, me too."
    show eve 9
    show player 12
    player_name "You guys think {b}Principal Smith{/b} is behind this?"
    show player 5
    show kevin 24
    kev "Probably, but what can we do about it?"
    show kevin 23
    show player 4 with dissolve
    pause
    hide eve with dissolve
    show kevin 20 with dissolve
    pause
    pause
    eve "No way..."
    show player 10 with dissolve
    player_name "What's up {b}Eve{/b}?"
    show player 5
    eve "Come up here!"
    hide player
    hide kevin
    with dissolve

    scene assembly_hall_paint01_c
    show player 5 at left
    show kevin 23f
    show eve 2 at right
    with dissolve
    eve "This is water based paint!"
    show eve 1
    show player 10
    player_name "It is?"
    show player 5
    show kevin 24f
    kev "What does that mean?"
    show kevin 23f
    show eve 2
    eve "It means, we can wash it off!"
    show eve 1
    show kevin 24f
    kev "Whoa, really?"
    show kevin 23f
    show eve 2
    eve "Yeah."
    show eve 1
    show player 10
    player_name "It'll take a lot of scrubbing though..."
    show player 5
    show eve 2
    eve "Which means we'll need help."
    eve "And I've got an idea!"
    eve "{b}[firstname]{/b}, can you meet me at the park this evening?"
    show eve 1
    show player 10
    player_name "Yeah, I guess so but why?"
    show player 5
    show eve 2
    eve "I think I know where we can get some help!"
    eve "Just don't forget, {b}the park at night{/b}."
    show eve 1
    show player 10
    player_name "O-okay, I won't forget."
    show player 5
    show eve 2
    eve "Cool, I'll catch you later then."
    hide eve with dissolve
    show kevin 24 with dissolve
    kev "I wonder what she's up to?"
    show kevin 23
    show player 10
    player_name "No idea..."
    show player 5
    show kevin 19 with dissolve
    kev "Hey, look at this!"
    show kevin 20 at Position (xoffset=95) with dissolve
    show player 10
    player_name "What is it?"
    show player 5
    show kevin 21 at Position (xoffset=95)
    kev "Whoever did this was stupid enough to step in some paint before leaving."
    show kevin 19 with dissolve
    kev "Tch, there's a trail."
    show kevin 20 at Position (xoffset=95)
    show player 14
    player_name "You're right!"
    player_name "Let's follow it and see where it goes!"
    show player 13
    show kevin 22 at Position (xoffset=95) with dissolve
    kev "Right behind you."
    hide player
    hide kevin
    with dissolve
    return

label assembly_hall_dewitt_clean_graffit:
    scene assembly_hall_cs06
    with fade
    show text "It seemed that {b}Eve{/b} and her gang had gotten started without me!\nThey had done an amazing job too. The auditorium was spotless!\nI guess that old saying is true, \"you can't judge a book by its cover.\"" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene assembly_hall_paint02_c
    show eve 1 at right
    show tyrone 1 at Position (xpos=700)
    show player 14 at left
    with dissolve
    player_name "Holy crap, you guys already started!"
    show player 13
    show tyrone 2
    tyrone "Dude, look around you. We're already finished!"
    tyrone "You hold up your end of the bargin?"
    show tyrone 1
    show player 14
    player_name "Yeah, I got your beer."
    show player 239_240 with dissolve
    pause
    show player 571 with dissolve
    player_name "Here ya go."
    show player 13 with dissolve
    show tyrone 5 with dissolve
    pause
    show tyrone 7 with dissolve
    tyrone "Niiiice. We were just running out."
    show tyrone 6
    show eve 2
    eve "{b}[firstname]{/b}, you should go and tell {b}Miss Dewitt{/b} to come take a look."
    show eve 1
    show player 14
    player_name "Yeah, that's a good idea."
    player_name "Thanks for doing this guys!"
    hide player
    hide eve
    hide tyrone
    with dissolve
    return

label assembly_hall_dewitt_show_auditorium:
    scene assembly_hall_paint02_c
    show dewitt 9c at left
    show player 13f at Position (xpos=500)
    show eve 6 zorder 1 at right
    with dissolve
    eve "Surprise!"
    show eve 1
    show dewitt 9b
    dewitt "Oh my Lord!"
    dewitt "You guys-"
    dewitt "How did you?!"
    dewitt "It looks good as new in here!"
    show dewitt 1b
    show player 17f
    player_name "Heh, {b}Eve{/b} called in some back-up."
    show player 13f
    show eve 6
    eve "Yeah, but I couldn't have done it without {b}[firstname]{/b}!"
    show eve 1
    show dewitt 6
    hide player
    with dissolve
    dewitt "I just can't believe this!"
    show dewitt 9b
    show player 28f
    with dissolve
    show tyrone 6 at right with dissolve
    dewitt "You kids are just wonderful! All of you!"
    show tyrone 8 with dissolve
    show dewitt 9d
    dewitt "Wait a second, are you all drinking beer!?"
    show tyrone 6 with dissolve
    show player 22f
    dewitt "You can't be having that stuff on school grounds! {b}Principal Smith{/b} will have our hides!"
    show dewitt 9c
    show eve 2b
    eve "Oh, right. Sorry, ma'am."
    eve "Guys, hide that stuff will you!"
    show eve 1 with dissolve
    show tyrone 8 with dissolve
    show dewitt 9b
    dewitt "Why don't you guys take that stuff up to my office and we can celebrate there!"
    show dewitt 1b
    show tyrone 6 with dissolve
    show player 10f
    player_name "Really? You don't mind?"
    show player 13f
    show dewitt 9b
    dewitt "Lord no! I'm so happy right now, I think a little celebration is just what we need!"
    show dewitt 1b
    show eve 6
    eve "You heard her boys, pack it up and let's hit {b}Miss Dewitt's{/b} office!"
    hide tyrone
    hide eve
    with dissolve
    show dewitt 9b
    dewitt "I dunno how you managed this, {b}[firstname]{/b}!"
    show dewitt 1b
    show player 14f
    player_name "It was no big deal. I just didn't like seeing you all upset, {b}Miss Dewitt{/b}."
    show player 13f
    show dewitt 19 with dissolve
    dewitt "Aww, you're quite the little charmer, sugar."
    show dewitt 18
    show principal 3 at right with dissolve
    pause 1
    show principal 3b
    pause
    show player 11
    show principal 5
    with dissolve
    smi "What the..."
    smi "How did this place get fixed up so fast?"
    show principal 3b with dissolve
    show dewitt 19
    dewitt "The students got together and cleaned it because they're excited for the talent show!"
    show dewitt 18
    smi "..."
    show principal 5 with dissolve
    smi "Impossible!"
    show principal 3b with dissolve
    show dewitt 14b
    dewitt "Look, I told you this show is happening and you better just deal with it!"
    dewitt "C'mon, {b}[firstname]{/b} let's head on upstairs."
    hide player
    hide dewitt
    with dissolve
    smi "..."
    show principal 2 at Position (xoffset=-70) with dissolve
    smi "This isn't over!"
    hide principal with dissolve
    return

label assembly_hall_dewitt_attend_talent_show_dialogue:
    scene assembly_hall_podium_c
    show dewitt 3b at Position (xpos=438)
    show xtra 44
    with dissolve
    dewitt "... We're just so happy you all came out to support us!"
    show dewitt 2b
    dewitt "These kids are so talented and I thank my lucky stars everyday for the opportunity to teach them!"
    dewitt "So without further ado, I'd like to present you with our first act of the show..."
    show dewitt 26 at Position (xpos=290) with dissolve
    dewitt "He's here to lay down a sick beat and spit hot fire... Give it up for {b}MC Tyrone{/b}!"
    hide dewitt with dissolve
    return

label assembly_hall_dewitt_attend_talent_show:
    call expression game.dialog_select("assembly_hall_dewitt_attend_talent_show_dialogue")
    $ M_dewitt.trigger(T_dewitt_talent_show_intro)
    $ game.main()

label assembly_hall_dewitt_talent_show:
    scene assembly_hall_paint02_c
    show kevin 17f at Position (xpos=600)
    show eve 11 zorder 1 at right
    with dissolve
    show player 13 at left with dissolve
    show kevin 18f
    kev "Hey, so were they really stuck?!"
    show kevin 17f
    show player 17
    player_name "Yeah, man. They're gonna be there for a long time..."
    show player 13
    show kevin 18f
    kev "Bro, that's so awesome!"
    show kevin 17f
    show eve 12
    eve "Hahahaha! I wish I could have seen it!"
    show eve 11
    show player 14
    player_name "You guys look great!"
    show player 13
    show kevin 18f
    kev "What, this?!"
    kev "Yeah, it was all {b}Eve's work{/b}."
    show kevin 17f
    show eve 12
    eve "Doesn't {b}Kevin{/b} look dreamy?"
    show eve 11
    show player 10
    player_name "Err... Yeah, I guess?"
    show player 14
    player_name "You look nice too, {b}Eve{/b}!"
    show player 13
    show eve 12
    eve "Aww, thanks {b}[firstname]{/b}!"
    eve "We've gotta do something for you..."
    show eve 11
    show kevin 18f
    kev "You better hurry! {b}Tyrone{/b} is finishing up and we're next!"
    kev "I'm going to check on the sound system one last time."
    show kevin 17f
    show eve 12
    eve "Alright, {b}Kevin{/b}."
    show eve 11
    hide kevin with dissolve
    show player 10
    player_name "You really don't have to do anything, {b}Eve{/b}. I'll be fine without it."
    show player 13
    show eve 12
    eve "Oh, shut up... I'm at least going to do something with your hair."
    show player 551
    show eve 13
    with dissolve
    player_name "..."
    show player 552
    show eve 12 with dissolve
    eve "Bitchin'!"
    show eve 11
    show player 553
    player_name "Yeah, I look cool?"
    show player 552
    show eve 12
    eve "Hahaha! Totally!"
    show eve 11
    show player 555
    player_name "Good, because {b}Miss Dewitt's{/b} about to announce us!"
    scene black with fade

    scene assembly_hall_podium_c
    show dewitt 2b at Position (xpos=438)
    show xtra 44
    with dissolve
    dewitt "Now as a special treat for being such a great crowd!"
    dewitt "We have a little finale planned for you all..."
    dewitt "For the first time ever..."
    dewitt "Allow me to introduce:"
    show dewitt 26 at Position (xpos=290) with dissolve
    dewitt "{b}Angelic Eve and the Cookie Monsters{/b}!!!"
    scene black with fade

    scene assembly_hall_cs01
    with fade
    show text "The show was going great! {b}Tyrone{/b} had gotten the crowd energized.\n... But now the time had come for our big finale! We ascended the stage to the sounds of a roaring crowd!\n{b}Miss Dewitt{/b} had to have been insanely proud of how everything turned out!\nNow we just needed to close it out on a good note!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve
    if game.cheat_mode:
        menu:
            "Play Minigame":
                pass
            "Skip Minigame (Cheat)":

                jump expression game.dialog_select("guitar_hero_minigame_talent_show_pass")
    call screen guitar_hero(0, "guitar_hero_minigame_talent_show_pass", "guitar_hero_minigame_talent_show_fail")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
