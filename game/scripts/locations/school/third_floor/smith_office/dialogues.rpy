label principals_office_delivery_invoice:
    scene office_clear
    show ronda chair at Position (xoffset=-320,yoffset=-55)
    show principal 22_23f at Position(xpos = 600, ypos = 764)
    player_name "!!!" with hpunch
    player_name "What the f-"
    show principal 25f
    smi "What is the meaning of this?!"
    show principal 24f
    ann "I'm so sorry, ma'am!"
    scene expression game.timer.image("office{}")
    show annie 3f at Position (xpos=375)
    show player 168b at left
    show titty 1f at right
    show principal 26 at Position (xpos=614)
    with dissolve
    ann "I didn't realize-"
    show annie 9f
    show principal 27
    smi "You know better than to interrupt me when I'm disciplining miscreants!"
    show principal 26
    ron "I didn't do anything wrong!"
    show principal 2
    smi "SILENCE!"
    show principal 1
    ann "..."
    show principal 28 at Position (xoffset=-54) with dissolve
    smi "What is that {b}[firstname]'s{/b} carrying?"
    show principal 26 with dissolve
    show annie 1f
    show player 168c
    player_name "{b}*Gulp*{/b} It's uhh, milk... ma'am."
    player_name "For the cafeteria."
    show player 168b
    show annie 9f
    show principal 27
    smi "Oh right, the delivery that I ordered."
    smi "What's it doing in my office?!"
    show principal 26
    show player 168c
    player_name "{b}Annie{/b} said-"
    show player 168b
    show principal 27
    smi "I don't care what {b}Annie{/b} said!"
    show annie 6f
    smi "Take that downstairs to the cafeteria, immediately!"
    show principal 26
    show player 168c
    player_name "{b}*Sigh*{/b} Down the stairs?"
    show player 168b
    show principal 27
    smi "... Problem?"
    show principal 26
    show player 168c
    player_name "I... Sorry, it's just really heavy and I've already carried it all the way up here..."
    show player 168b
    show principal 27
    smi "Ugh..."
    show principal 28 at Position (xoffset=-54) with dissolve
    smi "Just {b}untie Ronda{/b} and she'll help you carry it down."
    show principal 26 with dissolve
    ron "What?! Why do I have to-"
    show principal 27
    smi "It's good enough punishment for her and I'm sick of listening to her mouth!"
    show principal 26
    show player 168c
    player_name "O-okay."
    hide titty
    hide principal
    hide player
    hide annie
    with dissolve
    return

label principals_office_no_entry:
    scene expression game.timer.image("office{}")
    show principal 5 at right with dissolve
    show player 1 at left with dissolve
    smi "What are you doing here?!"
    show player 11 at left
    show principal 3 at right
    player_name "Oh... umm..."
    show player 21 at left
    player_name "I was... looking for the washroom!"
    show player 22 at left
    show principal 4 at right
    smi "Don't play dumb with me, {b}[firstname]{/b}!"
    smi "Didn't I just tell you earlier, to get to class??!"
    show player 10 at left
    show principal 1 at right
    player_name "Well..."
    show player 22 at left
    show principal 2 at right
    smi "Now, get out of my {b}OFFICE{/b}!!!"
    hide player 22 at left with dissolve
    hide principal 2 at right with dissolve
    return

label principals_office_no_entry_night:
    scene expression L_school_floor3.background_blur
    show player 10 with dissolve
    player_name "I can't go in there right now..."
    hide player with dissolve
    return

label principals_office_smith_intro:
    scene expression game.timer.image("office{}")
    show player 10 at left
    show principal 1 zorder 0 at Position(xpos=0.65, ypos=1.0)
    show annie 1 zorder 1 at right
    with dissolve
    player_name "You wanted to see me, {b}Principal Smith{/b}?"
    show player 11
    show principal 27
    smi "Indeed, {b}[firstname]{/b}."
    smi "We need to discuss your grades and whether or not you intend to graduate."
    show player 10
    show principal 1
    player_name "It's really that bad?"
    show player 11
    show principal 4b with dissolve
    smi "Have a look for yourself..."
    show expression ReportCard() zorder 2 with dissolve
    show player 23
    player_name "( !!! )" with hpunch
    pause
    hide expression ReportCard() with dissolve
    show player 10
    show principal 1 with dissolve
    player_name "Oh man, I'm failing everything?!"
    show player 11
    show principal 27
    smi "I told you..."
    show principal 1
    show annie 3
    ann "That's what happens when you skip school for a month!"
    show player 10
    show annie 1
    player_name "I wasn't skipping! My Dad died!"
    show player 11
    show principal 2
    smi "Be silent, {b}Annie{/b}!"
    show principal 1
    show annie 3
    ann "S-sorry, Ma'am."
    show principal 27
    show annie 1
    smi "... Regardless of the circumstances."
    smi "You'll need to {b}find a way to raise these grades{/b} if you don't want to repeat next year."
    smi "I'd suggest you {b}speak to your teachers{/b} about making up the work you've missed."
    smi "Perhaps they can come up with some {b}extra credit{/b} assignments or something?"
    show player 10
    show principal 1
    player_name "Y-yeah, okay."
    show player 11
    show principal 27
    smi "Do whatever it takes!"
    show player 10
    show principal 1
    player_name "Yes, Ma'am."
    show player 11
    show principal 27
    smi "Good, now get to class."
    show player 10
    show principal 1
    player_name "... Actually, Ma'am?"
    show player 11
    show principal 27
    smi "Yes?"
    show player 10
    show principal 1
    player_name "I forgot the combination to my locker. Can you help me get it open?"
    show player 11
    show annie 4
    ann "What do you mean you forgot?!"
    ann "Everyone was told at the beginning of the year to write down their combinations!"
    show player 10
    show annie 1
    player_name "I umm..."
    player_name "I lost it!"
    show player 11
    show annie 5
    ann "Pfft, typical."
    show annie 1
    show principal 27
    smi "That's very disappointing, {b}[firstname]{/b}."
    smi "We'll have to get you a new lock."
    show principal 1
    player_name "..."
    show principal 27
    smi "I'll send {b}Annie{/b} down with her {b}Masterkey{/b} momentarily..."
    smi "I suggest you get everything that you need out now."
    smi "It could be awhile before the new lock arrives."
    show player 10
    show principal 1
    player_name "Yes, Ma'am."
    show player 11
    show principal 27
    smi "Head there now and then get your butt to class after you're finished!"
    $ M_smith.trigger(T_smith_go_to_locker)
    $ game.main()
    return

label principals_office_smith_go_to_locker:
    scene expression game.timer.image("office{}")
    show player 11 at left
    show principal 1 zorder 0 at Position(xpos=0.65, ypos=1.0)
    show annie 4 zorder 1 at right
    with dissolve
    ann "Didn't {b}Principal Smith{/b} tell you to beat it?!"
    show annie 3
    ann "Head down to {b}your locker{/b} and I'll meet you momentarily!"
    $ game.main()
    return

label principals_office_smith_no_desk:
    scene expression game.timer.image("office{}")
    show player 11 at left
    show principal 1 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    smi "What are you doing?"
    show principal 2
    smi "Get the hell out of my office!" with hpunch
    $ game.main()
    return

label principals_office_annie_trouble:
    scene expression game.timer.image("office{}")
    show principal 6 at right
    show player 11 at left
    with dissolve
    ann "{b}Principal Smith{/b}?"
    show principal 7 at right
    smi "What is it??"
    show principal 6 at right
    ann "Reporting repeated offenders as you ordered!"
    show principal 9 at right
    smi "{b}[firstname]{/b}?"
    show principal 8 at right
    ann "Yes, Ma'am. He was being inappropriate in the locker room!"
    show principal 9 at right
    smi "Don't you have enough problems?"
    smi "What with your failing grades and all..."
    show player 10 at left
    show principal 13
    player_name "Uh, Yes Ma'am!"
    show player 11 at left
    show principal 9
    smi "... And yet, you feel the need to cause problems in the locker room as well?"
    show principal 7 at right
    smi "What happened, exactly, {b}Annie{/b}?"
    show principal 6 at right
    ann "Well, his... he... He's showing inappropriate body parts to the girls in the locker room, Ma'am."
    show principal 9 at right
    smi "Is that so?"
    show player 10 at left
    player_name "Well... I can explain-"
    show player 22 at left
    show principal 10 at right with hpunch
    smi "{b}SILENCE{/b}!!!"
    show principal 9 at right
    show player 5 at left
    smi "...I need to see exactly what happened. Show me what you did, now."
    show principal 6 at right
    ann "Ma'am, it won't work..."
    ann "It only seems to happen when... he sees women in the {b}nude{/b}, Ma'am."
    show principal 7 at right
    smi "Well, what are you waiting for, {b}Annie{/b}?"
    smi "You're going to have to help him with that."
    show principal 11 at right
    show player 11 at left
    ann "{b}What??!{/b}"
    show principal 12 at right
    smi "You're the one who witnessed it and reported the infraction..."
    smi "...It's your {b}duty{/b} to carry out the report!"
    player_name "We really don't have to do this-"
    show principal 10 at right
    show player 22 at left
    smi "No one's leaving until I get a full report! Do it, or you both are in {b}DETENTION{/b}!!!"
    show principal 13 at right
    ann "..."
    show player 8 at left
    show principal 14 at right
    window hide
    pause
    show player 63 at left
    show principal 15 at right
    window hide
    pause
    show principal 16 at right
    show player 64 at left
    smi "Now, look at those {b}firm breasts{/b} of hers..."
    show principal 17 at right
    smi "Don't you want to... suck on them? {b}[firstname]{/b}?"
    show player 65 at left
    player_name "..."
    show player 66 at left
    window hide
    pause
    show player 66 at left with hpunch
    window hide
    pause
    show player 67 at left
    smi "There we are..."
    show principal 18 at right
    smi "That's enough, {b}Annie{/b}. You can leave now..."
    show principal 5 at right with dissolve
    smi "So!..."
    smi "This is what I've been hearing about this whole time."
    hide player 67 at left
    show principal 19 at left
    with dissolve
    smi "You've made quite a reputation around school..."
    smi "I can see why..."
    smi "...this has been a..."
    show principal 20 at left
    window hide
    pause
    show principal 21 at left with hpunch
    window hide
    pause
    smi "...distraction!"
    show player 69 at left
    show principal 1 at right
    with dissolve
    player_name "I'm sorry, Ma'am!"
    player_name "It won't happen again, I promise!"
    show principal 5 at right
    show player 68 at left
    smi "Alright young man: Here's the deal..."
    smi "I won't send you to detention, as long as you keep this... \"problem\" of yours... to yourself."
    smi "My priority is order and discipline in this school, and I plan on keeping it that way!"
    show principal 1 at right
    show player 69 at left
    player_name "Yes, {b}Principal Smith{/b}!"
    show principal 2 at right
    show player 68 at left
    smi "Now, get out of my {b}OFFICE{/b}!!"
    hide player 68 at left with dissolve
    hide principal 2 at right with dissolve
    $ renpy.end_replay()
    return

label principals_office_dewitt_paint_trail:
    if M_dewitt.is_state(S_dewitt_paint_trail):
        scene smith_office_spying
        show annie spying 1
        show principal spying 2
        with dissolve
        smi "You should have seen their faces!"
        smi "Complete and utter devastation!"
        smi "Hahaha!"
        show principal spying 1
        show annie spying 2
        ann "So did they believe it was {b}Tyrone{/b} and his gang like you planned?"
        show annie spying 1
        show principal spying 2
        smi "Nah, {b}Dewitt{/b} knows I had something to do with it but she can't prove anything."
        show principal spying 1
        show annie spying 3
        ann "I'm sorry, Ma'am. I tried my best to make it look like a bunch of hooligans did it."
        show annie spying 1
        show principal spying 2
        smi "Yes, yes, I'm sure you did."
        smi "I just can't get that image out of my mind!"
        smi "Poor little {b}Dewitt{/b} on the verge of tears."
        smi "Her silly talent show in shambles!"
        show principal spying 3
        smi "Mmm..."
        show principal spying 2
        smi "It's actually getting me kinda worked up."
        smi "Why don't you come over here and help me out."
        show principal spying 1
        show annie spying 3
        ann "Of course, ma'am."
        show annie spying 4
        show principal spying 4
        with dissolve
        pause
        show annie spying 5 with dissolve
        pause
        show principal spying 3
        smi "Ahh, that's it."
        smi "Good girl..."
        smi "Hehehehe, I can't wait to see the look on her face when I tell her the board has pulled her funding!"
        scene black with fade

        scene outside_smith_office
        show kevin 24 at Position (xpos=800)
        show player 107 at Position (xpos=400)
        with dissolve
        kev "Bro, {b}Principal Smith{/b} WAS behind it!"
        show kevin 23
        player_name "..."
        show kevin 24
        kev "What a mega bitch!"
        kev "We have to say something!"
        show kevin 23
        player_name "..."
        show kevin 24
        kev "{b}[firstname]{/b}?"
        kev "{b}[firstname]{/b}?!"
        show kevin 23
        pause 1
        show kevin 25 at Position (xoffset=-82) with hpunch
        kev "Bro!"
        show kevin 23
        show player 12 with dissolve
        player_name "Hey! Chill out, man!"
        show player 5
        show kevin 24
        kev "I'm trying to talk to you!"
        show kevin 23
        show player 12
        player_name "Well, I'm sorry but did you see what they are doing in there right now?!"
        show player 5
        show kevin 24
        kev "Uh, yeah and it's super gross!"
        kev "{b}Principal Smith{/b} is the devil man, I bet her coochie smells like brimstone and sulphur!"
        show kevin 23
        show player 113
        player_name "{b}Annie{/b} doesn't seem to mind..."
        show player 114
        show kevin 24
        kev "C'mon, it's getting late and you're suppose to meet {b}Eve{/b} in the park, remember?!"
        show kevin 23
        show player 113
        player_name "Uh huh, just five more minutes..."
        show player 114
        show kevin 24
        kev "Let's go, before we get caught, ya perv!"
        hide kevin
        hide player
        with dissolve
    else:

        scene smith_office_spying
        show annie spying 5
        show principal spying 3
        with dissolve
        smi "You're getting pretty good at this my little pet."
        smi "Mmm, right there!"
        smi "Ahh!"
        scene black with fade
    return

label principals_office_dewitt_smith_office_trap:
    scene expression game.timer.image("office{}")
    show erik 51 at right
    show player 12 at left
    with dissolve
    player_name "You watch the door while I apply the adhesive, alright?"
    show player 5
    show erik 53
    eri "Yeah, okay."
    eri "Just hurry up, dude. I want to get out of here..."
    show erik 52
    show player 12
    player_name "I will."
    hide player
    hide erik
    with dissolve

    scene smith_office_cs01
    with fade
    show text "I made sure the chairs were glued to the floor before moving onto the cushions.\nThere was no way I would let {b}Principal Smith{/b} and {b}Annie{/b} ruin the {b}Talent Show{/b}.\nNot after all the hard work we had put into it!\nI didn't stop until every last drop of the adhesive had been used." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene smith_office_night_b
    show erik 52 at right
    show player 14 at left
    with dissolve
    player_name "Alright, that should do it."
    show player 17
    player_name "I disconnected her phone from the outlet too so there's no way they can call for help!"
    show player 13
    show erik 54
    eri "Nice thinking!"
    show erik 53
    eri "Now let's get out of here, {b}[firstname]{/b}!"
    show erik 52
    show player 14
    player_name "Yeah, I'm right behind you!"
    hide player
    hide erik
    with dissolve

    scene expression game.timer.image("outside_school{}")
    show player 13 at left
    show erik 53 at right
    with dissolve
    eri "Phew."
    eri "Let's never do that again, okay?"
    show erik 52
    show player 14
    player_name "Heh, yeah."
    player_name "At least we accomplished what we came here to do."
    show player 13
    show erik 54
    eri "Mission successful!"
    show erik 1
    show player 14
    player_name "Thanks for your help, {b}Erik{/b}."
    show player 13
    show erik 4
    eri "Don't mention it, {b}[firstname]{/b}."
    show erik 1
    show player 14
    player_name "I'll see you later!"
    show player 13
    show erik 7 with dissolve
    eri "See ya!"
    hide player
    hide erik
    with dissolve
    return

label principals_office_dewitt_trap_check_up:
    scene office_clear
    show annie 19
    with dissolve
    ann "... It's a great plan, ma'am!"
    ann "It'll put a stop to that stupid talent show once and for all."
    show annie 20
    smi "Yes, so long as you don't screw it up again..."
    show annie 19
    ann "But I didn't..."
    ann "... Yes, ma'am."
    show annie 20
    smi "Just go make the preparations!"
    show annie 19
    ann "Right away, ma'am!"
    show annie 20b with dissolve
    ann "..."
    ann "I'm stuck!"
    show annie 20c with dissolve
    smi "What?"
    show annie 20b with dissolve
    ann "I can't get out of my chair!"
    show annie 20c with dissolve
    smi "Stop fooling around, {b}Annie{/b}. We don't have time to waste!"
    show annie 20b with dissolve
    ann "I'm seriously stuck to the chair!"
    show annie 20c with dissolve
    smi "Oh for heavens sake!"
    show annie 21
    smi "( !!! )" with hpunch
    smi "WHAT THE HELL?!"
    smi "I'm stuck too!!!"
    smi "How is this possible?!"
    ann "..."
    smi "{b}Annie{/b} get your butt over here and help me!"
    ann "I can't, I'm stuck too!"
    scene black with fade

    scene outside_smith_office
    show player 107 at Position (xpos=400)
    with dissolve
    pause
    show player 17f at Position (xoffset=100) with dissolve
    player_name "( It worked! )"
    show player 14f at Position (xoffset=100)
    player_name "( There's no way they can interfere with the {b}Talent Show{/b} now! )"
    player_name "( They'll be stuck there arguing until somebody finds them. )"
    player_name "( I'd better get to the {b}auditorium{/b} quickly or I'll miss the introductions. )"
    hide player with dissolve
    return

label principals_office_dewitt_office_night_visit_delay:
    scene expression game.timer.image("office{}")
    show annie 22f at left
    show principal 36 at right
    with dissolve
    ann "Can you get this cushion off me?"
    show annie 23f
    show principal 37
    smi "Not now, idiot!"
    smi "What I want is a full report on who did this!"
    smi "Whoever ruined my chair... and... and my suit!"
    smi "My beautiful suit!"
    show principal 40 with dissolve
    smi "Just look at what they did!"
    smi "FIND THEM!"
    scene black with fade

    scene outside_smith_office
    show player 107 at Position (xpos=400)
    with dissolve
    pause
    show player 17f at Position (xoffset=100) with dissolve
    player_name "( I'd better get out of here before they see me! )"
    hide player with dissolve
    return

label desk03_locked_dialogue:
    scene expression game.timer.image("office{}")
    if player.location.is_here(M_smith):
        show player 30 at left
        player_name "Hmmm... I wonder what's in there?"
        show player 22 at left with hpunch
        show principal 4 at right with dissolve
        smi "What are you doing?"
        show principal 1 at right
        show player 29 at left
        player_name "Oh, I'm sorry... I was just looking!"
        show player 3 at left
        show principal 5 at right
        smi "If I {b}EVER{/b} catch you going through my things..."
        show principal 2 at right
        smi "...you can be sure, you'll be spending the rest of the year in {b}DETENTION{/b}!!!"
    else:
        $ pass
    $ game.main()

label principle_drawer:
    scene principle_drawer
    show expression "objects/object_papers_01.png" at Position(xpos = 378, ypos = 526)
    player_name "..."
    player_name "What's with all those... leather things... in here?"
    player_name "weird..."
    call screen principle_drawer

label principle_drawer_diane_delivery_3_fetch_invoice:
    scene expression game.timer.image("office{}")
    show player 167f at right
    show titty 1 at left
    show principal 28f at Position (xpos = 470)
    with dissolve
    smi "Ah, wonderful."
    smi "Are those the new {b}milk cartons{/b}?"
    show player 168f
    show principal 26f at Position (xpos = 415)
    player_name "Umm... Yeah."
    show principal 27f
    show player 163f
    smi "I sampled the last batch..."
    smi "It was quite... delightful. You're lucky I'm in a good mood."
    smi "Please, tell the milk provider I'm doubling our next order."
    smi "We keep running out. The students absolutely love it!"
    show principal 26f
    show player 164f
    player_name "Will do! Where can I put these cartons?"
    show principal 27f
    show player 163f
    smi "You can give them to {b}Annie{/b}, she'll take care of them."
    show principal 4f at Position (xpos = 470)
    show player 167f
    smi "Now, get out of my office, I have some unfinished business to attend to."
    show principal 26f at Position (xpos = 415)
    show player 168f
    player_name "Yes, {b}Principal Smith{/b}!"
    hide principal
    hide titty
    hide player
    with dissolve
    $ M_diane.trigger(T_diane_delivery_3_got_invoice)
    $ game.main()

label principals_office_okita_get_keycode_morning:
    scene expression game.timer.image("office{}")
    show player 22 at left
    show principal 26 at right
    player_name "( Oh crap! She's here! )"
    smi "..."
    show principal 27
    smi "... Can I help you with something?"
    show player 10
    show principal 26
    player_name "Oh! I was just-"
    show player 29
    player_name "... Err, I was... just wondering..."
    show principal 2
    show player 3
    smi "Spit it out, {b}[firstname]{/b}?!"
    show principal 26
    pause
    show player 10
    player_name "Uhh, how are you doing, {b}Principal Smith{/b}?"
    show player 11
    smi "..."
    show principal 27
    smi "Busy."
    show principal 2
    smi "Now get out!"
    show player 10
    show principal 26
    player_name "Y-yes, Ma'am!"


    return

label principals_office_okita_get_keycode_afternoon:
    scene expression game.timer.image("office{}")
    show player 1
    with dissolve
    player_name "( She's not here! This is my chance to find that keycode! )"
    player_name "( {b}I should look around.{/b} )"
    return

label masterkey_taken:
    show expression "backgrounds/location_school_office_desk.jpg"
    show expression "boxes/popup_key3.png" at truecenter with dissolve
    $ player.get_item("master_key")
    pause
    hide expression "boxes/popup_key3.png" with dissolve
    $ game.main()

label keycode_note_taken:
    scene expression game.timer.image("office{}")
    show player 544
    with dissolve
    pause
    show player 543
    player_name "Aha! This has gotta be it! {b}6219{/b}."
    show expression "backgrounds/location_school_office_desk.jpg"
    show expression "boxes/popup_item_note2.png" at truecenter with dissolve
    $ player.get_item("keycode_note")
    pause
    hide expression "boxes/popup_item_note2.png" with dissolve
    pause 1
    player_name "Now I just have to go unlock {b}Miss Okita{/b}'s office to grab all those things she wanted."
    $ M_okita.trigger(T_okita_keycode_acquired)
    $ game.main()
    return

label tissue_taken:
    $ player.go_to(L_school_smithoffice)
    scene location_school_office_day_blur
    show player 528
    with dissolve
    pause
    show player 529
    player_name "Ugh, oh man..."

    player_name "Gross!"
    show player 528
    pause
    show player 529
    player_name "I think this will work..."
    player_name "I'd better get outta here before {b}Annie{/b} comes back."
    show expression "boxes/popup_item_tissue1.png" at truecenter with dissolve
    $ player.get_item("tissue")
    pause
    hide expression "boxes/popup_item_tissue1.png" with dissolve
    pause 1

    $ game.main()

label desk_open:
    python:
        for image in renpy.get_showing_tags():
            renpy.hide(image)
    call screen desk_drawer

label principals_office_okita_get_ingredients_morning:
    scene expression game.timer.image("office{}")
    show player 22 at left
    with dissolve
    player_name "( Oh crap! She's here! )"
    show principal 3b at Position(xpos=0.85, ypos=1.0) with dissolve
    smi "..."
    show principal 27 at right with dissolve
    smi "... Can I help you with something?"
    show player 29 with dissolve
    show principal 26
    player_name "Oh! I was just-"
    player_name "... Err, I was... just wondering..."
    show player 3
    show principal 27 with dissolve
    smi "Spit it out, {b}[firstname]{/b}!"
    show player 29
    show principal 26
    player_name "Uhh, how are you doing, {b}Principal Smith{/b}?"
    show player 3
    smi "..."
    show principal 27
    smi "Busy."
    show player 22
    show principal 2
    with dissolve
    smi "Now get out!" with hpunch
    show principal 1
    show player 10
    player_name "Y-yes, Ma'am!"

    return

label principal_trash:
    if M_okita.is_state(S_okita_get_ingredients) and not player.has_picked_up_item("tissue"):
        call screen principle_garbage
    else:
        scene location_school_office_day_blur
        show player 10
        player_name "I don't want to look through Principal Smith's garbage."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
