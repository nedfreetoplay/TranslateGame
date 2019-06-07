label earl_police_office_dialogue_roxxy_ask_earl_release:
    show earl 1 at right
    show roxxy 1of at Position (xpos=400)
    show player 10 at left
    with dissolve
    player_name "Excuse me, Sir?"
    show player 5
    show earl 2
    ear "Huh?"
    ear "What are you kids doing here?"
    show earl 3 with dissolve
    show player 10
    player_name "We're just trying to get some information about an arrest you guys made earlier today."
    show player 5
    show earl 2 with dissolve
    ear "Hmm, you're {b}Crystal's{/b} daughter, aren't you?"
    show earl 1
    show roxxy 1jf
    rox "..."
    show player 10
    player_name "Yes, she is, sir."
    player_name "Could you tell us what's happening?"
    show player 5
    show earl 2
    ear "I'm afraid I'm not allowed to discuss these matters with anyone other than her family."
    ear "If you want to come with me, miss. I'll fill you in on how this all works."
    show earl 1
    show player 10
    player_name "... Yeah, alright. I'll just wait over-"
    show player 11
    show roxxy 2c at Position (xpos=500) with dissolve
    rox "No!"
    show roxxy 2cf at Position (xpos=434)
    with dissolve
    rox "... I mean."
    show roxxy 33f at Position (xpos=400) with dissolve
    rox "I want him to stay. It's alright."
    show roxxy 32f
    show player 13
    ear "..."
    show earl 2
    ear "You're sure."
    show earl 1
    show roxxy 33f
    rox "Yeah."
    show roxxy 32f
    show earl 2
    ear "Suit yourself."
    ear "We got an anonymous tip this morning regarding a large stash of drugs at your residence."
    ear "So we drove on over to have a look."
    ear "Were you aware that {b}your mother{/b} had over a pound of Crystal Methamphetamine stashed under the couch?"
    show earl 1
    show roxxy 1if
    show player 23
    player_name "A pound?!"
    show player 22
    show roxxy 27f at Position (xoffset=67)
    rox "..."
    show earl 2
    ear "I'm afraid so."
    ear "That's a felony drug charge."
    ear "We're holding {b}your mother{/b} for possession with intention to sell."
    show earl 1
    show roxxy 33bf at Position (xoffset=34) with dissolve
    rox "..."
    show player 10
    player_name "That's not good."
    show player 5
    show roxxy 1jf with dissolve
    show earl 2
    ear "No, son. It certainly isn't."
    ear "... Now, I've known {b}Crystal{/b} for a long time."
    ear "We went to school together back in the day."
    ear "She's always been good at getting herself into trouble..."
    ear "... But after questioning her this morning, I can tell you without a doubt that she doesn't know the first thing about cooking meth."
    ear "Now, she claims she made it all herself and was looking to move it..."
    ear "... But I'd bet good money that she was just holding it for somebody else!"
    show earl 1
    rox "..."
    show earl 2
    ear "Unfortunatly, unless I get proof. She's going to wind up in prison for a very long time."
    show earl 1
    show roxxy 33bf at Position (xoffset=34) with dissolve
    rox "{b}*Sniff*{/b}."
    show player 10
    player_name "Okay, well what about my friend's home?"
    show roxxy 1jf with dissolve
    show player 5
    show earl 2
    ear "Oh, the trailer?"
    ear "... Well, if {b}Crystal{/b} gets convicted, it'll be repossessed by the state and sold off."
    show earl 1
    show player 25
    player_name "Sheesh..."
    show player 12
    player_name "Is there anything we can do to prevent that?"
    show player 5
    show earl 2
    ear "Not unless you can convince {b}Crystal{/b} to give up whoever she's protecting..."
    show earl 1
    rox "..."
    show player 11
    player_name "..."
    show player 5
    show earl 2
    ear "I'm real sorry about how this all went down, Miss."
    show earl 1
    rox "{b}*Sniff*{/b}"
    show earl 2
    ear "You all can {b}go down to the cells and visit her{/b} if you'd like."
    ear "They should be done questioning her by now."
    show earl 1
    show player 14
    player_name "Alright, thanks for the information, Officer."
    show player 13
    hide earl with dissolve
    pause
    show player 5
    show roxxy 33bf
    rox "... {b}*Sniff*{/b} All of this for that inbred idiot..."
    show roxxy 1j with dissolve
    show player 10
    player_name "C'mon, let's go and talk to {b}your mom{/b}."
    hide player
    hide roxxy
    with dissolve
    return

label earl_police_office_dialogue_first_visit:
    show earl 2 at right
    show player 11 at left
    with dissolve
    ear "What'chu doing in here?!"
    show earl 3
    ear "Is it another one of those \"Bring your kids to work\" days?"
    show earl 1
    show player 14
    player_name "Oh, no, I'm just passing by, Sir."
    player_name "I wanted to speak with {b}Harold{/b}."
    show earl 2
    show player 1
    ear "Wait a minute... Don't you go to school with my daughter?"
    show earl 3
    show player 14
    player_name "Oh, right! You're {b}Ronda's dad{/b}!"
    show earl 2
    show player 1
    ear "Shiiiiiiiiiiieeeeeet!"
    show player 11
    ear "You better watch yourself around my baby girl, or I'll have to put surveillance on {b}you{/b}."
    show earl 4
    ear "Got it?!"
    show earl 1
    show player 29
    player_name "Uhh... of course, Sir!"
    player_name "I would never-"
    show earl 2
    show player 13 at left
    ear "Relax, I'm just messing with ya! Move along now."
    return

label earl_police_office_dialogue_pre:
    show earl 2 at right
    show player 1 at left
    with dissolve
    ear "Hey, what's up?"
    show earl 3
    return

label earl_police_office_dialogue_donuts:
    show earl 1
    show player 14
    player_name "This might seem like a silly question, but what kind of donuts does {b}Harold{/b} like?"
    show player 1
    show earl 2
    ear "Hah!"
    ear "{b}Harold{/b} only eats them if they're {b}[harold_glaze]{/b}..."
    show earl 3
    ear "... But I ain't sure what else he puts on them."
    show player 14
    show earl 1
    player_name "I see."
    show player 11
    show earl 2
    ear "Why do you ask?"
    show player 17
    show earl 1
    player_name "Oh, no reason."
    show player 11
    show earl 4
    ear "Wait, shouldn't you be at school? What are you doing here-"
    show player 14
    show earl 3
    player_name "Errr..."
    show player 17
    player_name "Thanks, bye!"
    return

label earl_police_office_dialogue_harold:
    show player 10
    player_name "Do you know where {b}Harold{/b} could be?"
    player_name "I need to err...return something to him!"
    show player 11
    show earl 2
    ear "I'm not sure where he went, but I saw him yesterday in the office..."
    ear "...He looked in a bad shape, that's for sure!"
    ear "For a second I thought he was quitting..."
    ear "...So I told him to take some time off."
    show earl 1
    show player 12
    player_name "Did he mention where he would be while off duty?"
    show player 5
    show earl 2
    ear "I didn't want to ask too many questions, you know?"
    ear "Sometimes guys just need some alone time..."
    show earl 1
    show player 14
    player_name "Alright, thanks."
    return

label earl_police_office_dialogue_roxxys_mom:
    show earl 1
    show player 12
    player_name "Where can we speak with my {b}friend's mom{/b} again?"
    show player 5
    show earl 2
    ear "She's {b}downstairs in a cell{/b}."
    ear "Officer {b}Yumi{/b} is down there but she'll give you all some privacy to talk."
    show earl 1
    show player 14
    player_name "Alright, thanks."
    return

label earl_police_office_dialogue_leave:
    show player 14
    player_name "Just passing by, Sir."
    show earl 2
    show player 1
    ear "Alright then."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
