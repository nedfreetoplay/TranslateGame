label bissette_book_search_2_books_left:
    show player 12 with dissolve
    player_name "Well, two more books to go."
    hide player with dissolve
    return

label bissette_book_search_1_book_left:
    show player 14 with dissolve
    player_name "Just one book left."
    hide player with dissolve
    return

label bissette_book_search_no_books_left:
    show player 14 with dissolve
    player_name "Great! That's the last book!"
    player_name "Now I just need to return them to the library!"
    hide player with dissolve
    return

label annie_locker_first_visit:
    player_name "Yup. I expected as much."
    player_name "{b}Annie{/b} is such a suck up to {b}Principal Smith{/b}."
    return

label dexter_locker_first_visit:
    player_name "I'd better not let {b}Dexter{/b} see me in here."
    player_name "Typical jock stuff."
    player_name "What a weird basketball air pump."
    return

label dexter_locker_book_search:
    player_name "He was lying! I knew it!"
    return

label dexter_locker_book_found:
    scene dexter_locker
    show book_05_c with dissolve
    player_name "{b}Quick mafs{/b}?"
    player_name "This is a book for little kids..."
    player_name "Hah, I guess it matches his mafs-"
    player_name "Math level!"
    player_name "I need to get out of here!"
    player_name "Something about being next to {b}Dexter{/b} or his stuff is making me dumber!"
    hide book_05_c with dissolve
    show expression game.timer.image("location_school_right_hall_day{}_blur")
    return

label erik_locker_first_visit:
    player_name "{b}Erik{/b} has a lot of {b}Dungeon 'N Orcettes{/b} stuff."
    player_name "There's his lunchbag too."
    player_name "His landlord always packs him some of her homemade fudge."
    player_name "Lucky guy. His landlord sure must like him."
    return

label eve_locker_first_visit:
    player_name "Yikes! I'd better not let anyone else see her locker."
    player_name "Those headphones sure do look comfy though."
    return

label eve_locker_drawing_pick_up:
    $ player.get_item("eve_drawing")
    call expression game.dialog_select("eve_locker_drawing_picked_up")
    $ player.location.call_screen(False)

label eve_locker_drawing_picked_up:
    scene eve_locker
    show closeup_drawing_01
    with dissolve
    player_name "Huh, this IS really good!"
    player_name "... {b}Chad{/b} was right. It's pretty sexy!"
    player_name "I wonder if she actually thinks about wearing something like that?"
    show expression "boxes/popup_item_drawing1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_drawing1.png"
    hide closeup_drawing_01
    with dissolve
    return

label judith_locker_first_visit:
    player_name "Mmm... {b}Mountain Jizz{/b}."
    player_name "That stuff can sure make a mess."
    player_name "Must be all the sugar that makes it so sticky."
    pause
    player_name "She must like cows."
    player_name "I do too-"
    player_name "Hey! How did she get that picture of me?"
    return

label take_judith_glasses:
    scene judith_locker
    player_name "That must be her spare set."
    show expression "boxes/popup_item_glasses1.png" at truecenter with dissolve
    $ player.get_item("judith_glasses")
    pause
    player_name "Now I just need to get these back to Okita."
    pause
    $ game.main()

label take_broken_flute:
    scene judith_locker
    player_name "( That should be the {b}flute{/b} Judith borrowed from Miss Dewitt. )"
    scene lefthall_c with fade
    $ player.get_item("broken_flute")
    call expression game.dialog_select("take_broken_flute_dialogue")
    $ M_dewitt.trigger(T_dewitt_get_flute)
    $ game.main()

label take_broken_flute_dialogue:
    show player 563f at left with dissolve
    player_name "Wow, this thing really got flattened..."
    player_name "It's all bent up!"
    show player 564f with dissolve
    pause
    show player 565f with dissolve
    player_name "Hmm, it smells funny too."
    show player 564f with dissolve
    show erik 5 at right with dissolve
    eri "Uhh, what are you doing there, dude?"
    show erik 52
    show player 22f at Position (xoffset=139) with hpunch
    player_name "!!!"
    show player 29 with dissolve
    player_name "N-nothing! You really scared me!"
    show player 14 with dissolve
    player_name "What are you doing?"
    show player 13
    show erik 5
    eri "Just heading to my next class..."
    show erik 53
    eri "Was that a flute?"
    show player 563
    show erik 3c
    with dissolve
    player_name "Y-yeah. Well, it used to be anyways."
    show player 562
    show erik 53
    eri "It has definitely seen better days..."
    show erik 3c
    show player 563
    player_name "I was gonna play it for {b}Ms. Dewitt's{/b} talent show."
    show player 13 with dissolve
    show erik 5
    eri "Hmm, well maybe you could build your own?"
    show erik 52
    show player 10
    player_name "You think?"
    show player 5
    show erik 54
    eri "Definitely!"
    show erik 4
    eri "I had to build a flute in a video game once."
    eri "All you need is a good piece of wood and a drill to make all the holes."
    show erik 1
    show player 12
    player_name "You built one in a video game?"
    show player 5
    show erik 4
    eri "Totally! I used it to charm all the orc girls in the village!"
    eri "Then we had a giant orgy in the Chief's hut!"
    show erik 1
    show player 10
    player_name "Oh, that's... nice."
    show player 5
    show erik 4
    eri "Heh, dude, it was anything but nice. I can assure you!"
    show player 13
    show erik 54
    eri "Green chicks are crazy in the sack!"
    show erik 1
    show player 14
    player_name "I should probably get busy if I'm going to build a flute from scratch."
    show player 13
    show erik 4
    eri "Oh, right. I hear you."
    show erik 1
    show player 14
    player_name "Thanks, {b}Erik{/b}."
    show player 13
    show erik 4
    eri "My pleasure, dude!"
    hide player
    hide erik
    with dissolve
    return

label kevin_locker_first_visit:
    player_name "Huh?"
    player_name "That looks like my missing jock strap!"
    pause
    player_name "I didn't know we bought the same one."
    return

label mia_locker_first_visit:
    player_name "{b}Mia's{/b} locker smells nice."
    return

label mia_locker_first_visit_early_route:
    player_name "She has such great life."
    return

label mia_locker_first_visit_helping_parents:
    player_name "I should help her parents get back together."
    return

label mia_locker_first_visit_helen_route:
    player_name "I wonder if I should have helped her parents get back together..."
    return

label ronda_locker_first_visit:
    player_name "Is there any sport she isn't good at?"
    player_name "I bet she doesn't even have to pay for college."
    player_name "She probably has a full-ride scholarship."
    return

label roxxy_locker_first_visit:
    player_name "Wow."
    player_name "{b}Roxxy's{/b} locker is nice."
    player_name "Looks like she's popped the seal on a new jar of {b}Cherry Pops{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
