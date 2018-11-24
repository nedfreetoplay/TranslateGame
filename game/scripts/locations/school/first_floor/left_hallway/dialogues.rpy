label left_hallway_judith_changing:
    scene lefthall_c
    show player 2 at left with dissolve
    show judith 6 at right with dissolve
    player_name "Hey, {b}Judith{/b}..."
    show player 11 at left
    player_name "..."
    show player 10 at left
    player_name "Is everything all right?"
    show player 5 at left
    show judith 3 at right
    jud "Oh, hey, {b}[firstname]{/b}..."
    jud "I'm just not feeling too well; I might just go home."
    show player 10 at left
    show judith 1 at right
    player_name "You're not coming to the Athletics class?"
    show player 5 at left
    show judith 2 at right
    jud "Well..."
    jud "...I just..."
    show judith 3 at right
    jud "... I can't go in the guy's Locker Room."
    show player 10 at left
    show judith 1 at right
    player_name "... The guy's Locker Room?"
    player_name "Why would you need to go in the guy's Locker Room?"
    show player 5 at left
    show judith 3 at right
    jud "You mean nobody told you?"
    show judith 1 at right
    show player 10 at left
    player_name "... No?"
    show player 5 at left
    show judith 3 at right
    jud "A pipe burst in the girls locker and it's closed for repairs..."
    show judith 2 at right
    jud "We're sharing the boys Locker Room now."
    show judith 1 at right
    show player 10 at left
    player_name "For real?!"
    show player 5 at left
    show judith 3 at right
    jud "I don't really feel comfortable about it, like the other girls."
    show judith 6 at right
    show player 35 at left
    player_name "Well..."
    show player 10 at left
    show judith 1 at right
    player_name "The class is starting soon, so there's probably not that many people left in there anyway?"
    show player 1 at left
    show judith 5 at right
    jud "Yeah, I guess you're right..."
    show player 2 at left
    show judith 4 at right
    player_name "I can go in with you, to make sure you're okay..."
    show player 33 at left
    player_name "...And I won't look!"
    show player 13 at left
    show judith 5 at right
    jud "Okay... I'll follow you, then."
    hide player 13 at left with dissolve
    hide judith 5 at left with dissolve
    return

label left_hallway_latinos_bashing:
    scene lefthall_c
    show judith 10 at left
    show martinez 20 at Position (xpos=625)
    show latinas 19 at right
    with dissolve
    lopez "Just look at those nasty-ass saggy tits!"
    show latinas 18 at right
    show judith 7 at left
    jud "..."
    show judith 8 at left
    show martinez 21
    martinez "She's probably too poor to afford a bra..."
    show martinez 20
    show latinas 18 at right
    show judith 7 at left
    jud "It's not like that!!"
    show judith 10 at left
    show latinas 19
    lopez "You think you're gonna get the boys attention showing your tits around like that?"
    show latinas 18 at right
    show judith 7 at left
    jud "My breasts are sensitive!! It hurts when I wear a bra..."
    jud "I'm just more comfortable like this!!"
    show judith 10 at left
    show latinas 19
    lopez "Haha!"
    show latinas 18
    show judith 9 at left
    show martinez 21
    martinez "Yo, you better not hang around here no more..."
    show martinez 22 with dissolve
    martinez "PUTA! Did you just hear? This is our turf, so get out!"
    show martinez 20 with dissolve
    show latinas 18 at right
    show player 12 at Position( xpos = 290, ypos = 768)
    hide judith 9
    show judith 9 at left
    with dissolve
    player_name "What's going on here?!"
    show player 114
    jud "{b}*Sobbing*{/b}"
    hide combo 7 at left
    show player 90 at Position( xpos = 290, ypos = 768)
    show judith 9 at left
    show martinez 21
    martinez "You defending this ugly bitch now??"
    show martinez 20
    show latinas 19 at right
    lopez "Keep walking white boy!"
    show latinas 18 at right
    show player 113
    player_name "Are you okay {b}Judith{/b}?"
    hide judith
    show player 90 at left
    with dissolve
    show martinez 21
    martinez "What's the matter, white boy, you not gonna run after your bitch?"
    show martinez 20
    show latinas 18 at right
    show player 12 at left
    player_name "You didn't have to do this..."
    show martinez 22 with dissolve
    martinez "We'll do whatever the fuck we want!"
    show martinez 20 with dissolve
    show latinas 19
    lopez "Haha! See ya!"
    hide player
    hide latinas
    hide martinez
    with dissolve
    return

label left_hallway_judith_missing:
    scene expression game.timer.image("lefthall{}")
    show player 11 with dissolve
    player_name "..."
    show player 10
    player_name "...Where's {b}Judith{/b}?"
    player_name "( She usually hangs out in this hallway. )"
    show player 34
    player_name "Hmm..."
    show player 35
    player_name "( I can {b}hear{/b} something... )"
    show player 10
    player_name "( Is that someone... Sobbing? )"
    show player 12
    player_name "( It's like a crying voice coming from the {b}girls locker room{/b}... )"
    hide player 12 with dissolve
    return

label left_hallway_martinez_book_search:
    scene lefthall_c
    show martinez 20b at Position (xpos=625)
    show lopez 18 at right
    show player 10 at left
    with dissolve
    player_name "Hey, {b}Martinez{/b}?"
    show player 5
    show martinez 22b
    martinez "...What do you want, Culo?"
    show martinez 20b
    show lopez 19
    lopez "Yeah! What do you want?"
    show lopez 18
    show player 10
    player_name "Uhh, I heard you had a book that's overdue from the library."
    show player 5
    show martinez 21b
    martinez "What, are you stalking me or something, White boy?"
    show martinez 20b
    show player 10
    player_name "Huh? No, the librarian sent me!"
    show player 5
    show lopez 19
    lopez "So, you're just the librarians little bitch?"
    show lopez 18
    show martinez 21b
    martinez "Haha!"
    show martinez 20b
    show player 12
    player_name "What? No, she ordered a book for me and asked if I could talk to you guys in return."
    show player 5
    show martinez 22b
    martinez "Whatever, bitch! We ain't got time for this..."
    show martinez 21b
    martinez "C'mon, {b}Lopez{/b}. We gotta get ready for gym class."
    show martinez 20b
    show lopez 19
    lopez "Sure thing, {b}Martinez{/b}. Later, Culo!"
    lopez "Hahaha!"
    hide lopez
    show martinez 23
    with dissolve
    show player 428
    pause
    show martinez 23 at right with dissolve
    show player 11
    player_name "!!!"
    hide martinez with dissolve
    show player 12
    player_name "I bet that's it in her backpack!"
    show player 30
    player_name "I should try and {b}grab it while they are showering{/b}. They probably wouldn't even realize it's gone."
    show player 33
    player_name "I just have to be sneaky..."
    hide player with dissolve
    return

label left_hallway_cult_discovery:
    scene cult_event 5
    with dissolve
    window hide
    $ renpy.pause()
    scene cult_event 6
    with Dissolve(0.3)
    $ renpy.pause()
    scene expression "backgrounds/location_school_lefthall_night.jpg"
    with Dissolve(0.3)
    scene expression game.timer.image("lefthall{}")
    show player 11 at left with dissolve
    show erik 1 at right with dissolve
    player_name "..."
    show player 12
    player_name "They went in the utility closet?"
    show player 90
    show erik 5
    eri "Why would they go in there?"
    show player 35
    show erik 1
    player_name "The better question is: How could they all fit in there?"
    player_name "It must lead somewhere else..."
    show player 34
    show erik 5
    eri "Can we leave now?"
    show player 12
    show erik 1
    player_name "Let's just stick to our original plan, and look around."
    show player 1
    show erik 3
    eri "Okay..."
    hide player 1 with dissolve
    hide erik 3 with dissolve
    return

label left_hallway_school_sneak_mission:
    scene cult_event 5
    with dissolve
    window hide
    pause
    scene cult_event 6
    with Dissolve(0.3)
    pause
    scene expression game.timer.image("lefthall{}")
    show player 11 at left with dissolve
    show erik 51 at right with dissolve
    player_name "..."
    show player 12
    player_name "They went into the utility closet?"
    show player 90
    show erik 53
    eri "Why would they go in there?"
    show erik 52
    show player 35
    player_name "It doesn't make sense."
    player_name "They couldn't all fit in there!"
    show player 34
    show erik 53
    eri "You think maybe there's a secret tunnel or something?"
    show erik 52
    show player 10
    player_name "Hmm, I dunno. Maybe?"
    show player 5
    show erik 53
    eri "This is really creeping me out."
    eri "Can we leave now?"
    show erik 52
    show player 12
    player_name "Hold on. We still have a mission to complete."
    show player 5
    show erik 50
    eri "..."
    show player 12
    player_name "C'mon, let's head up to {b}Principal Smith's office{/b} on the {b}third floor{/b}."
    hide player
    hide erik
    with dissolve
    return

label door14_locked_dialogue:
    scene expression game.timer.image("lefthall{}")
    show player 35 at left
    player_name "( The utility closet is locked. )"
    $ game.main()

label left_hallway_roxxy_lockerroom_event:
    scene expression game.timer.image("lefthall{}")
    show player 34 with dissolve
    player_name "Hmm?"
    player_name "( There are voices coming from the {b}girls locker room{/b}! )"
    player_name "( It's supposed to be off limits... )"
    show player 4 at Position (xoffset=6) with dissolve
    player_name "( ... I wonder what's going on? )"
    hide player with dissolve
    return

label left_hallway_roxxy_shower_event:
    scene expression game.timer.image("lefthall{}")
    show erik 62 at right
    show jersey 10 at left
    with dissolve
    player_name "{b}Erik{/b}?"
    show erik 61
    player_name "Where are all your clothes?"
    show jersey 5
    show erik 63
    eri "Hey, {b}[firstname]{/b}..."
    eri "I was just in the {b}locker room{/b} changing, when {b}Roxxy{/b} and her friends came in..."
    show erik 62
    eri "... They kicked me out."
    show erik 61
    show jersey 10
    player_name "So your clothes are still in there?"
    show jersey 5
    show erik 62
    eri "... Yeah."
    show erik 61
    show jersey 12
    player_name "C'mon man, I'll go with you."
    player_name "We'll grab your clothes and then I need to hit the shower."
    show jersey 5
    show erik 62
    eri "O-okay..."
    hide player
    hide erik
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
