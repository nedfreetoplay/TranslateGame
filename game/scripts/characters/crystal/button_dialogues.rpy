label button_crystal_preamble:
    show player 5 at left
    show crystal 3 at right
    with dissolve
    crys "It's my little girl's boyfriend again."
    show crystal 1 with dissolve
    show player 10
    player_name "I told you we're not-"
    show player 5
    show crystal 2
    crys "Whatever you say, young man."
    show crystal 4 with dissolve
    crys "*Gulp*"
    show crystal 2 with dissolve
    crys "So what do you want?"
    return

label button_crystal_roxxys_dad:
    show player 10
    player_name "Where's {b}Roxxy's... father{/b}?"
    show player 11
    show crystal 2
    crys "Hah! She don't have no father!"
    crys "I raised her myself."
    show crystal 1
    show player 10
    player_name "I see."
    show player 11
    show crystal 2
    crys "To tell you the truth, I don't remember which one it was..."
    show crystal 4 with dissolve
    crys "*Gulp*"
    show crystal 2 with dissolve
    crys "...So her daddy could be anyone, for all I know."
    show crystal 1
    show player 22
    player_name "!!!"
    show crystal 2
    crys "Anything else you'd like to talk about?"
    show player 5
    show crystal 1
    return

label button_crystal_roxxy:
    show player 10
    player_name "Do you know where I could find {b}Roxxy{/b}?"
    show player 5
    show crystal 3 with dissolve
    crys "Hah! You think I babysit my daughter?"
    show crystal 1 with dissolve
    show player 10
    player_name "Hmm..."
    show player 5
    show crystal 2
    crys "She's always out doing stuff..."
    crys "...But, usually she's at {b}school{/b} or at {b}the beach{/b}."
    show crystal 1
    show player 14
    player_name "Oh. I see. Thanks!"
    show player 13
    show crystal 2
    crys "Anything else?"
    show crystal 1
    return

label button_crystal_nothing:
    show player 10
    player_name "Oh, nothing."
    player_name "I was just passing by..."
    show player 11
    show crystal 2
    crys "Well I got a visitor coming soon, so why don't you move along."
    show crystal 1
    show player 10
    player_name "I'm sorry. I'll get going then."
    player_name "Bye!"
    hide player
    hide crystal
    with dissolve
    return

label button_crystal_roxxy_go_to_picnic:
    scene expression "backgrounds/location_trailer_closeup_night.jpg"
    show player 5 at left
    show player_wet at left
    show crystal 3 at right
    with dissolve
    crys "Mmm, you know I can help you out of them wet clothes if you want?"
    show crystal 1 with dissolve
    show player 10
    player_name "Uhh... I..."
    show player 5
    player_name "..."
    show crystal 2
    crys "Don't be shy now."
    crys "Handsome man, like yourself. You deserve some special attention, don't ya?"
    show crystal 1
    show player 3 with dissolve
    player_name "..."
    rox "{b}Mom{/b}, leave {b}[firstname]{/b} alone!"
    show crystal 2
    crys "Hehehe, I'm just teasin' the boy a bit."
    show crystal 1
    rox "Well, stop!"
    show crystal 4 with dissolve
    rox "{b}[firstname]{/b}, get in here!"
    show crystal 1
    player_name "..."
    hide crystal
    hide player
    hide player_wet
    with dissolve
    return

label button_crystal_rox8_11_evening:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 5 at left
    show crystal 6 at right
    with dissolve
    crys "You lost, handsome?"
    show crystal 5
    show player 10
    player_name "Huh?!"
    show player 5
    show crystal 6
    crys "Oh, yer {b}Roxxy's{/b} new man."
    show crystal 5
    show player 12
    player_name "N-no, I'm-"
    show player 5
    show crystal 6
    crys "She's inside."
    show crystal 5
    return

label button_crystal_rox8_11_day:
    scene trailer_interior_c
    show player 5 at left
    show crystal 2 at right
    with dissolve
    crys "You lost, handsome?"
    show crystal 1
    show player 10
    player_name "Huh?!"
    show player 5
    show crystal 2
    crys "Oh, yer {b}Roxxy's{/b} new man."
    show crystal 1
    show player 10
    player_name "N-no, I'm-"
    show player 5
    show crystal 2
    crys "She ain't here."
    show crystal 4 with dissolve
    return

label button_crystal_final_evening:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 13 at left
    show crystal 6 at right
    with dissolve
    crys "Mmm, now there's a nice capable man!"
    show crystal 5
    show player 14
    player_name "Heh, hi {b}Crystal{/b}..."
    show player 13
    show crystal 6
    crys "Why don't you grab a beer and come sit with me?"
    crys "You can show off that silver tongue some more..."
    show crystal 5
    show player 14
    player_name "Oh, I dunno... {b}Roxxy{/b} wouldn't-"
    show player 5
    show crystal 6
    crys "Yer here to call on {b}Roxxy{/b} then?"
    show crystal 5
    return

label button_crystal_final_day:
    scene trailer_interior_c
    show player 13 at left
    show crystal 2 at right
    with dissolve
    crys "Mmm, now there's a nice capable man!"
    show crystal 1
    show player 14
    player_name "Heh, hi {b}Crystal{/b}..."
    show player 13
    show crystal 2
    crys "Why don't you grab a beer and come sit with me?"
    crys "You can show off that silver tongue some more..."
    show crystal 1
    show player 14
    player_name "Oh, I dunno... {b}Roxxy{/b} wouldn't-"
    show player 5
    show crystal 2
    crys "{b}Roxxy{/b} ain't here."
    show crystal 1
    return

label button_crystal_sorry_to_bother:
    show player 10
    player_name "Sorry to bother you."
    show player 5
    show crystal 6
    crys "Psh, talkin' don't bother me none..."
    crys "In fact, why don't you run on down to the store and buy me a fresh twelve pack?"
    crys "You do that and we can talk 'til yer ears fall off."
    show crystal 5
    show player 17
    player_name "Heh, nah that's okay."
    player_name "I should get inside and see {b}Roxxy{/b}."
    show player 13
    show crystal 6
    crys "Suit yerself."
    hide player
    hide crystal
    with dissolve
    return

label button_crystal_roxxy_rox8_rox11:
    show crystal 1 with dissolve
    show player 10
    player_name "Do you know where she is?"
    show player 5
    show crystal 2
    crys "Psh, ain't got a clue..."
    crys "I can't never keep track of that gal."
    show crystal 1
    show player 10
    player_name "Really?"
    show player 5
    show crystal 2
    crys "Ungrateful brat don't tell me nothin'."
    crys "She needs a whoopin'! What she needs..."
    show crystal 1
    player_name "..."
    return

label button_crystal_roxxy_final:
    show crystal 4 with dissolve
    show player 12
    player_name "Where's she at?"
    show player 5
    show crystal 2 with dissolve
    crys "Heck if I know."
    crys "If she ain't {b}at school{/b}, then I reckon she's probably {b}at the beach.{/b}"
    crys "I swear, that girl is half mermaid!"
    show crystal 1
    show player 17
    player_name "Heh, yeah maybe..."
    show player 13
    return

label button_crystal_roxxys_mom:
    show crystal 1 with dissolve
    show player 10
    player_name "So you're {b}Roxxy's mom{/b}?"
    show player 5
    show crystal 2
    crys "That's right."
    crys "Can't you see the resemblance?"
    show crystal 1
    menu:
        "Yeah, I suppose.":
            show player 12
            player_name "Now that you mention it, you two do look a lot alike."
            show player 5
            show crystal 2
            crys "Yeah, she really lucked out, takin' after me."
            crys "Her father was ugly as sin!"
            show crystal 1
            player_name "..."
            show crystal 2b
            crys "Hahaha!"
            show crystal 1
            jump roxmom_dialogue_repeat
        "You look so young though!":
            show player 12
            player_name "I see the resemblance but you look way too young to be {b}Roxxy's{/b} mom."
            show player 10
            player_name "Are you sure you're not her sister?"
            show player 5
            show crystal 2
            crys "Well now, if you ain't got a silver tongue on you!"
            crys "I reckon that's how you dun got my daughter's attention, huh?"
            show crystal 1
            show player 10
            player_name "Well, I-"
            show player 5
            show crystal 2
            crys "Hate to break it to ya there, slick... But it's gonna take more than fancy talk to keep hold of her."
            crys "I brought her up right, you see?"
            crys "Showed her that the worth of a man is in his actions and not his words!"
            show crystal 1
            player_name "..."
            show crystal 2
            crys "Iffin' you can't take proper care of my girl then you best be movin' on, kiddo."
            show crystal 1
            jump roxmom_dialogue_repeat
    return

label button_crystal_roxxy_busy:
    show player 29 with dissolve
    player_name "Is {b}Roxxy{/b} busy?"
    show player 3
    show crystal 6
    crys "Psh, I doubt it..."
    crys "She's probably just in there yappin' on that damn phone of hers."
    show crystal 5
    show player 12 with dissolve
    player_name "So I can just go in and see her?"
    show player 5
    show crystal 11
    crys "... You expectin' me to stop ya or something?."
    show crystal 10
    show player 10
    player_name "I don't-"
    show player 11
    show crystal 6
    crys "Good grief, kiddo."
    crys "Grow a pair and get in there already!"
    hide crystal
    hide player
    with dissolve
    return

label button_crystal_happy_home:
    show player 10
    player_name "Are you happy to be home?"
    show player 5
    show crystal 2
    crys "Darn tootin' I am!"
    crys "This place might be a shithole but it beats the hell outta that jail cell, I'll tell ya that for free!"
    crys "I reckon, I got you to thank for gettin' me outta there, huh?"
    show crystal 4 with dissolve
    show player 14
    player_name "Oh, no thanks needed. I was just happy to help."
    show player 13
    show crystal 2 with dissolve
    crys "Heh, yeah... Okay."
    crys "If you say so, slick."
    crys "The offer stands iffin' you change yer mind..."
    crys "I can be REAL thankful... Know what I mean?"
    show crystal 1
    show player 5
    player_name "... {b}*Gulp*{/b}"
    show crystal 2
    crys "Hehehe."
    return

label button_crystal_should_go_evening:
    show player 14
    player_name "I should probably get in there..."
    show player 13
    show crystal 6
    crys "Yeah, I reckon yer right about that."
    crys "Take good care of my girl now, ya hear?"
    show crystal 5
    show player 14
    player_name "Yes, ma'am."
    hide player with dissolve
    pause
    show crystal 6
    crys "Hahaha, \"ma'am...\""
    crys "That kills me every time!"
    hide crystal with dissolve
    return

label button_crystal_should_go_day:
    show player 14
    player_name "I should probably go and find {b}Roxxy{/b}."
    show player 13
    show crystal 2
    crys "Well, you don't have to go runnin' off now..."
    crys "I'm more than happy to keep you company 'til she gets home."
    show crystal 1
    show player 14
    player_name "Heh, no that's alright. I'd hate to be a bother."
    show player 13
    show crystal 2
    crys "Psh, ain't no bother."
    crys "I know a few ways we could pass the time..."
    show crystal 1
    show player 3 with dissolve
    player_name "{b}*Gulp*{/b}"
    show player 29
    player_name "I'll uhh... See you later, {b}Crystal{/b}."
    show player 3
    show crystal 2
    crys "Suit yerself."
    hide player
    hide crystal
    with dissolve
    return

label button_crystal_she_here:
    show player 14
    player_name "Yeah, is she here?"
    show player 13
    show crystal 6
    crys "Oh, yeah she's in there..."
    show crystal 11
    crys "Probably yappin' on her phone, as usual."
    crys "If I didn't know better, I'd swear that thing was glued to the side of that girls head..."
    show crystal 5
    show player 17
    player_name "Heh, yeah."
    show player 13
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
