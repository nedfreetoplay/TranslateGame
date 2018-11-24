label june_dialogue_bissette_fix_printer_repeat:
    scene computer_room_printer_c
    show xtra 40
    show june 17 at right
    show player 10 at left
    with dissolve
    player_name "Hey {b}June{/b}! Have you fixed the copy machine yet?"
    show player 5
    show june 19
    june "No, sorry. I haven't had time to mess with it at all."
    show june 17
    player_name "..."
    show player 12
    player_name "Stupid technology!"
    show player 518 with dissolve
    return

label june_dialogue_bissette_fix_printer_first:
    scene computer_room_c
    show player 10 at left
    show june 1 at right
    with dissolve
    player_name "Hey, {b}June{/b}?"
    show player 5
    show june 3
    june "Yes, {b}[firstname]{/b}?"
    show june 2
    show player 12
    player_name "I'm having trouble with the printer. What does PC load letter mean?"
    show player 5
    show june 4
    june "Ugh, is it doing that again?! What a piece of garbage!"
    show june 2
    show player 10
    player_name "I just need to scan a couple pages from this book and print them off."
    player_name "Could you help me?"
    show player 5
    show june 3
    june "Yeah, sure!"
    june "Not to brag or anything but I'm pretty good with electronics."
    show june 2
    show player 14
    player_name "Awesome!"
    show player 13
    scene black with fade

    scene computer_room_printer_c
    show xtra 40
    show player 13 at left
    show june 9f at right
    with dissolve
    june "Oh, sometimes you just need to restart it. Let me just cycle power."
    show june 10f with dissolve
    show player 108f
    player_name "Really?"
    show player 5
    show june 9f with dissolve
    june "Yeah, technology is picky like that."
    june "Just waiting for it to boot up..."
    show player 10
    player_name "Alright."
    show player 5
    pause
    pause
    show june 10f with dissolve
    show player 434
    june "I think it should be work no-"
    show june 9f with dissolve
    show player 5
    june "Grr... PC load error?!"
    show june 15 with dissolve
    show player 110f
    june "You worthless piece of-"
    show june 16 with vpunch
    pause
    show june 15 with dissolve
    june "I guess I'll have to open it up and repair it again."
    show player 10
    player_name "How long will that take?"
    show player 5
    show june 19 with dissolve
    june "It will take awhile, I don't have time to deal with it today."
    show june 17
    show player 10
    player_name "Seriously?"
    show player 5
    show june 19
    june "Yeah, this thing really is a pain in the butt..."
    show june 17
    show player 12
    player_name "Stupid technology!"
    show player 518 with dissolve
    return

label june_dialogue_bissette_fix_printer_fail:
    show player 519 with vpunch
    player_name "..."
    show player 10 with dissolve
    player_name "[str_warn]*Sigh*"
    player_name "[str_warn]I guess I'll check back with you tomorrow then..."
    show player 5
    show june 19
    june "[str_warn]Sorry, {b}[firstname]{/b}."
    hide player
    hide june
    with dissolve
    return

label june_dialogue_bissette_fix_printer_pass:
    show player 519 with vpunch
    pause
    show player 11 with dissolve
    player_name "!!!"
    show june 18
    june "... Hey! It's working!"
    show june 17
    show player 10
    player_name "Really?"
    show player 5
    show june 18
    june "Yeah! You must have the midas touch, {b}[firstname]{/b}!"
    show june 17
    show player 14
    player_name "Hah, Yeah. I guess so..."
    show player 13
    show june 18
    june "Well you can copy your pages now..."
    show june 17
    show player 14
    player_name "Thank goodness! I really need to get this book back to {b}Judith{/b} before she gets upset."
    player_name "Thanks for all your help, {b}June{/b}!"
    show player 13
    show june 18
    june "No problem."
    hide june with dissolve
    show player 518 with dissolve
    player_name "Print!"
    show player 519 with vpunch
    show xtra_paper 39 at Position (xoffset=100) with dissolve
    pause .25
    hide xtra_paper 39 with dissolve
    show player 184 with dissolve
    pause

    show player 510 with dissolve
    player_name "Alright! I finally have a complete French Dictionary."
    player_name "Now I just need to get {b}Judith's{/b} book back to her and I can get started with {b}Miss Bissette{/b}'s private lessons."
    hide player with dissolve
    return

label june_dialogue_okita_faptic_engine:
    scene location_school_computer_day_blur
    show player 2 at left
    show june 2 at right
    with dissolve
    player_name "{b}Miss Okita{/b} wants me to get her something called a {b}Faptic Engine{/b}. She told me you could help?"
    show player 1
    show june 4
    june "What the heck does she want with one of those?"
    show player 2
    show june 2
    player_name "She says she needs it for her newest invention."
    show player 1
    show june 4
    june "Hah. What crazy thing has she come up with this time?"
    show player 2
    show june 2
    player_name "It sounds pretty neat actually, It's a-"
    show player 1
    show june 3
    june "No, don't tell me!. I'm sure, I don't wanna know."
    show player 11
    show june 2
    player_name "..."
    show player 10
    player_name "Can you help me or not?"
    show player 11
    show june 4
    june "I doubt it. Does it need to be authentic?"
    show player 10
    show june 2
    player_name "Err, I assume so."
    show player 11
    show june 4
    june "Well that's gonna be hard to come by."
    show player 10
    show june 2
    player_name "What is a {b}Faptic Engine{/b} anyways?"
    show player 11
    show june 3
    june "Oh, you don't know?"
    june "It's a tiny piece of machinery that provides tactile sensations. They just started putting them in the top of the line Smart Phones."
    show player 10
    show june 2
    player_name "Tactile Sensations?"
    show player 11
    show june 4
    june "Sensations you feel with your skin. In this case, vibrations."
    show player 2
    show june 2
    player_name "Oh, I get it now."
    player_name "So why is it so hard to get?"
    show player 1
    show june 3
    june "Well, putting aside the fact that those phones are super expensive..."
    show player 11
    show june 4
    june "They are currently sold out, like everywhere!"
    show player 10
    show june 2
    player_name "How expensive are we talking?"
    show player 11
    show june 4
    june "Around $2000."
    show player 23
    show june 2
    player_name "( !!! )" with hpunch
    show player 10
    player_name "What!? For a phone!?"
    show player 11
    show june 4
    june "I told you they are top of the line."
    show june 3
    june "It really doesn't matter though, didn't you hear me? They are completely sold out."
    show player 10
    show june 2
    player_name "Well shoot! What am I gonna tell Okita?"
    show player 11
    show june 3
    june "It's a shame she wants authentic. There are some pretty good quality knock off versions that you might be able to get your hands on."
    show player 10
    show june 2
    player_name "Hmm, would it work as well as the authentic ones?"
    show player 11
    show june 4
    june "Well no, but pretty close. It would depend on what you're using it for."
    show june 3
    june "In most cases, I'd say the knock off would do the trick."
    show june 2
    player_name "..."
    show player 10
    player_name "Alright, where would I get the knock off version?"
    show player 11
    show june 3
    june "Well, they were putting them into those {b}Master Blaster{/b} controllers a few years ago."
    show player 10
    show june 2
    player_name "{b}Master Blaster{/b}? Like the video game?"
    show player 11
    show june 3b
    june "Yeah! I always wanted one but my parent's couldn't afford it."
    show player 2
    show june 2
    player_name "You know what? My buddy {b}Erik{/b} used to have one of those!"
    show player 1
    show june 6
    june "Does he still have it?"
    show player 2
    show june 5
    player_name "No idea."
    show player 1
    show june 6
    june "Well if you manage to get your hands on one, I could take the {b}Faptic Engine{/b} out for you."
    show player 2
    show june 2
    player_name "Great! I'll go talk to {b}Erik{/b} and see if he still has it."
    player_name "Thanks for the info, {b}June{/b}."
    show player 1
    show june 3
    june "Good luck!"
    return

label june_dialogue_okita_get_controller_info:
    scene location_school_computer_day_blur
    show player 2 at left
    show june 2 at right
    with dissolve
    player_name "What was the name of that controller again?"
    show player 1
    show june 4
    june "{b}The Master Blaster{/b}."
    show june 3
    june "Didn't you say your buddy {b}Erik{/b} had one?"
    show player 2
    show june 2
    player_name "Yeah, he used to..."
    player_name "I'll go ask him about it."
    player_name "Thanks, {b}June{/b}."
    show player 1
    show june 3
    june "Good luck!"
    return

label june_dialogue_okita_has_controller:
    scene location_school_computer_day_blur
    show player 502 at left
    show june 2 at right
    with dissolve
    player_name "Is this the thing you were talking about?"

    show player 1
    show june 11
    with dissolve
    june "Hey, you actually got one. Awesome!"
    show player 2
    show june 12
    player_name "So you can take the {b}Faptic Engine{/b} out of this?"
    show player 1
    show june 11
    june "Absolutely."
    june "Just give me a few minutes to take it apart."
    show player 2
    show june 12
    player_name "Alright."
    show player 1
    show june 11

    june "This is so cool!"

    pause
    scene location_school_computer_day_blur
    show player 1 at left
    show june 13 at right
    with dissolve
    june "There we go, one knock off {b}Faptic Engine.{/b}"
    show player 2
    show june 14
    player_name "That's it? It's so tiny..."
    show player 505
    show june 18
    with dissolve
    june "Yup, it's a little thing but it packs a punch."
    show player 506
    show june 17
    player_name "Alright, I'd better get this to Okita."
    show player 505
    show june 19
    june "Say, {b}[firstname]{/b}?"
    june "Would you mind if I keep the controller?"
    show player 2 with dissolve
    show june 17
    player_name "No, not at all. Knock yourself out!"
    show player 1
    show june 18
    june "Sweet! Thanks, {b}[firstname]{/b}!"
    return

label june_dialogue_mc_intro:
    show player 14 at left
    show june 5 at right
    player_name "Hey, {b}June{/b}!"
    show player 1
    show june 6
    june "Hi, {b}[firstname]{/b}!"
    june "What's up?"
    show june 5
    return

label june_dialogue_intro:
    if player.location.is_here(M_erik):
        show erik 1b at Position (xpos=700)
    show june 1 at right
    show player 14 at left
    with dissolve
    player_name "Hi!"
    show june 3
    show player 1
    june "Oh, uh, hi?"
    june "What's up?"
    show june 2
    return

label june_dialogue_okita_get_bifocal_lenses:
    show player 2
    player_name "Hey, so uhh..."
    player_name "I'm kinda helping {b}Miss Okita{/b} with a project."
    show player 1
    show june 4
    june "{b}Miss Okita{/b} asked you for help with her designs?"
    show player 10
    show june 2
    player_name "Yes."
    player_name "... And we need some {b}lenses{/b}; Like from a pair of glasses?"
    show player 11
    show june 4
    june "You want my glasses?"
    show player 10
    show june 2
    player_name "Well, I was hoping you might have a spare set?"
    show player 11
    show june 4
    june "Nope, just the one."
    show player 10
    show june 2
    player_name "Maybe I could convince you to give me that pair?"
    show player 11
    show june 4
    june "I doubt it."
    show player 10
    show june 2
    player_name "Hmm, are you farsighted or nearsighted?"
    show player 11
    show june 3
    june "Nearsighted."
    show player 29 with dissolve
    show june 2
    player_name "Oh, nevermind then."
    player_name "I need a pair from someone who is both."
    show player 3
    show june 4
    june "I can't believe {b}Miss Okita{/b} asked {b}YOU{/b} to help with her projects..."
    show player 29
    show june 2
    player_name "Well she's kinda, forcing me..."
    show player 3
    show june 6
    june "Yeah, that sounds more like her."
    show june 3
    june "Well, good luck."
    show player 2 with dissolve
    show june 2
    player_name "Yeah, thanks."
    return

label june_dialogue_ross_ask_model:
    show player 2
    player_name "I'm working on a project for {b}Miss Ross{/b} and it requires a live model."
    player_name "Would you be interested?"
    show player 1
    show june 3
    june "Modeling?"
    show june 3b
    june "Do I look like a model to you?"
    show player 10
    show june 5
    player_name "Sure, why not?"
    show player 11
    show june 3b
    june "Pfft, nice try."
    show june 3
    june "I've got other stuff planned anyways..."
    show player 10
    show june 5
    player_name "You do?"
    show june 3
    show player 11
    june "Yeah, the expansion pack for Orcette's Dungeon launched today."
    june "You better believe I'm getting a copy!"
    show player 10
    show june 5
    player_name "Alright, have fun I guess."
    show player 11
    show june 3b
    june "Oh, I will!"
    return

label june_dialogue_hang_out:
    show player 14
    player_name "I was wondering if you wanted to hang out at my place?"
    show player 1
    show june 6
    june "Sure!"
    june "After school?"
    show player 14
    show june 5
    player_name "Yeah."
    show player 1
    show june 6
    june "So, your room it is, then?"
    show player 10
    show june 5
    player_name "My room?"
    show player 11
    show june 6
    june "Yeah! We need a nice quiet place to chill and play games."
    show player 14
    show june 5
    player_name "Heh, okay!"
    show player 1
    show june 6
    june "Awesome!"
    june "I got classes coming up, I should get going."
    june "I'll see ya after school, {b}[firstname]{/b}!"
    return

label june_dialogue_cosplay_no_costume:
    show player 14
    player_name "What cosplay were you trying to make again?"
    show player 1
    show june 3
    june "Oh, it's an orcette costume."
    june "It should have the teeth, necklace and belt!"
    show player 14
    show june 2
    player_name "Ah, right!"
    player_name "I think I know a place in the {b}mall{/b} that has costumes..."
    show player 1
    show june 6
    june "Oh yeah?"
    show player 14
    show june 5
    player_name "I might go by there and check it out!"
    show player 1
    show june 6
    june "Cool! See ya."
    return

label june_dialogue_cosplay_has_costume:
    show player 17
    player_name "I think I found something you might like!"
    show player 1
    show june 3
    june "Huh?"
    show june 6
    june "What is it?"
    show june 5
    show player 423 with fastdissolve
    player_name "It's an orcette costume!!"
    show player 422
    show june 6
    june "For my cosplay?!"
    show player 1
    show june 7
    with fastdissolve
    pause
    show player 13
    show june 8
    june "Oh my gosh!!"
    june "It has all the missing pieces I needed!"
    june "Those even look like real teeth!"
    show player 17
    show june 5 with fastdissolve
    player_name "I'm glad you like it."
    show player 14
    player_name "It's going to look great on you!"
    show player 1
    show june 6
    june "Thank you so much, {b}[firstname]{/b}."
    show player 14
    show june 5
    player_name "I'm just glad you'll have a cool cosplay at the comic con."
    show player 11
    show june 6
    june "I'll probably get a lot of attention from the crowds, I'm sure!"
    show player 10
    show june 5
    player_name "You mean like, guys?"
    show player 11
    show june 6
    june "Well, I guess, yeah..."
    show june 5
    player_name "..."
    show june 6
    june "But you know what?"
    june "I think I should test out the cosplay before I go!"
    june "Maybe put it on... in front of a friend?"
    show june 5
    show player 10
    player_name "Like who?"
    show player 11
    show june 6
    june "You!! Silly..."
    show player 17
    show june 5
    player_name "Oh, ha ha!"
    show player 14
    player_name "Sure, I could emm... give you some feedback!"
    show player 1
    show june 6
    june "Great! How about we meet at your house... Like last time?"
    show player 14
    show june 5
    player_name "Okay, I'll see you after school then!"
    show player 1
    show june 6
    june "See you later!"
    return

label june_dialogue_ask_about_class:
    show player 14
    player_name "Hey, what class are you in?"
    player_name "I don't see you around school often."
    show player 1
    show june 3
    june "Oh, I don't do sports."
    june "I prefer hanging around here..."
    show player 14
    show june 2
    player_name "What do you do in the computer room?"
    show player 1
    show june 3
    june "You know, just stuff... like browsing the internet..."
    june "... going on message boards, watching streams and playing games."
    show june 2
    show player 14
    player_name "Games, huh?"
    show player 1
    show june 3
    june "Yeah."
    show june 1
    show player 14
    player_name "Like the one you're holding?"
    show player 1
    show june 3
    june "Oh, this thing? It's just a silly game..."
    show player 14
    show june 2
    player_name "What's it called?"
    show player 1
    show june 3
    june "It's called Orc Bork."
    show player 14
    show june 2
    player_name "A game about orcs?"
    show player 1
    show june 3
    june "Yeah."
    show june 4
    june "It's pretty hard."
    show player 11
    june "I've been trying to beat it for months..."
    show player 14
    show june 2
    player_name "Is it really that difficult?"
    show player 1
    show june 3
    june "Well, it's easier when you play with two players."
    show june 4
    june "I just haven't found anyone who plays these kind of games at school..."
    show june 3
    june "Unless, maybe you know someone?"
    show june 1
    return

label june_dialogue_erik_help:
    show player 14
    player_name "Actually, I do!"
    player_name "My good friend {b}Erik{/b} LOVES games with orcs in them!"
    player_name "Especially... the orcettes."
    player_name "I think you two should totally play together!"
    show player 1
    show june 3
    june "{b}Erik{/b}?"
    show player 11
    june "I don't think I know him..."
    show player 10
    show june 1
    player_name "He said you borrowed one of his pencils once."
    show player 1
    show june 4
    june "Huh..."
    show player 14
    show june 5
    player_name "Well, he spends a lot of time in his room... playing games..."
    show player 1
    show june 6
    june "Seriously?"
    show player 14
    show june 5
    player_name "I think he could help you beat that game."
    show player 1
    show june 6
    june "That would be awesome."
    june "Let me know if he's up for it!"
    show player 17
    show june 5
    player_name "Sweet!!"
    show player 14
    player_name "I'll definitely let him know."
    return

label june_dialogue_mc_help:
    show player 14
    player_name "I'm not really good at those games... But I'll try!"
    show player 1
    show june 4
    june "You... want to play with me?"
    june "Are you sure you would like that?"
    show player 14
    show june 2
    player_name "Sure, why not?"
    show player 11
    show june 3
    june "Well, it's just that no one has ever asked before..."
    show player 17
    show june 2
    player_name "I'd gladly be your first!"
    show player 21
    show june 5
    player_name "Err... I mean... Not like-"
    show player 11
    show june 6
    june "Ha ha, you're funny."
    show june 5
    player_name "..."
    show player 14
    player_name "So... You want to play now?"
    show player 11
    show june 6
    june "Umm... How about we play somewhere else?"
    june "I'm a bit tired of spending all my time in this computer room..."
    show player 14
    show june 5
    player_name "Okay, where then?"
    show player 10
    player_name "If we play in the hallway, {b}Annie{/b} will give us detention..."
    show player 11
    show june 6
    june "Hmm... How about we play at your house?"
    show player 12
    show june 5
    player_name "My... My house?!"
    show player 11
    show june 6
    june "Yeah!"
    june "After school?"
    show player 10
    show june 5
    player_name "Uhh... I guess we could?"
    show player 11
    show june 6
    june "Awesome!"
    june "Thanks for wanting to play with me..."
    show player 13
    june "It's... really nice of you!"
    show player 14
    show june 5
    player_name "Oh, ha ha. It's nothing..."
    show player 1
    show june 6
    june "Just come ask me when you're ready to hang out!"
    june "I'll be waiting in here."
    show player 17
    show june 5
    player_name "Sure!"
    return

label june_dialogue_leave:
    show june 2 at right
    show player 14
    player_name "Oh, nothing!"
    player_name "Just saying hi."
    show player 1
    show june 4
    june "Oh, okay then..."
    show june 1
    show player 29 at Position(xoffset=8)
    player_name "Err... I'll see you later!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
