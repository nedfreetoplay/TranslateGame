label library_diane_production_ask_librarian:
    scene expression "backgrounds/location_library_day_blur.jpg"
    show player 13 with dissolve
    player_name "( I should ask the librarian about those milking books {b}Veronica{/b} mentioned. )"
    hide player with dissolve
    return

label library_jane_intro:
    call expression game.dialog_select("library_jane_intro_pre")
    menu:
        "Sure." if player.has_money(20):
            call expression game.dialog_select("library_jane_intro_sure")
            $ player.spend_money(20)
            $ M_player.set("library subscription", True)
            $ M_jane.trigger(T_jane_library_pass)
        "I'll pass.":

            call expression game.dialog_select("library_jane_intro_not_yet")
            $ player.go_to(L_map)
            $ game.main()

    hide player
    hide jane
    with dissolve
    return

label library_jane_intro_pre:
    scene library
    show player 1 at left
    show jane 2 at right
    with dissolve
    jan "Hi!"
    show player 14
    show jane 1
    player_name "Oh, hi!"
    player_name "I'm looking for some school {b}textbooks{/b}."
    show player 1
    show jane 2
    jan "Do you have a membership subscription?"
    show jane 1
    show player 10
    player_name "Umm... I don't think I have one."
    show player 13
    show jane 3
    jan "Oh. That's okay!"
    show jane 2
    jan "Would you like to get one?"
    show jane 3
    show player 11
    jan "Membership subscriptions are {b}$20{/b}, and you get access to all of our selections!"
    show jane 1
    show player 2
    player_name "Uhh... I guess I have no choice. Haha."
    show jane 3
    show player 13
    jan "Knowledge is priceless, right?"
    show jane 2
    jan "Would you like to subscribe right now?"
    show jane 1
    return

label library_jane_intro_sure:
    show player 4
    player_name "Hmm..."
    show player 174b at Position(xoffset=38) with fastdissolve
    player_name "All right. Here's {b}$20.{/b}"
    show player 1 with fastdissolve
    show jane 3
    jan "Thank you!"
    show jane 2
    jan "If you're looking for a specific {b}book{/b}, just come to the front desk."
    jan "I'll look them up and find 'em for ya!."
    show jane 1
    show player 2
    player_name "That sounds great! Thanks!"
    return

label library_jane_intro_not_yet:
    show player 4
    player_name "Hmm..."
    show player 35
    player_name "Actually, I think I'll pass..."
    show jane 2
    show player 1
    jan "Oh... alright then."
    show jane 1
    show player 2
    player_name "I might come by another time!"
    show jane 2
    show player 1
    jan "Okay, have a good day!"
    return

label library_bissette_find_poem_reference_book:
    scene library
    show player 14f with dissolve
    player_name "Now, to find something on French romance."
    show player 12f
    player_name "This isn't going to be easy-"
    show player 32f at Position(xoffset=-69) with dissolve
    player_name "Is that {b}Mia{/b}?"
    show player 14f with dissolve
    player_name "I wonder what she's doing here?"
    player_name "I should go and say Hi!"
    hide player with dissolve
    return

label library_ross_find_magazines:
    scene library
    show player 2
    with dissolve
    player_name "Hmm, I should {b}ask the Librarian{/b} where she keeps the magazines."
    return

label check_out_lock:
    scene library
    show player 5 with dissolve
    player_name "( I need to check out this book first. )"
    player_name "( I should {b}talk to the librarian again{/b}. )"
    hide player with dissolve
    $ game.main()

label poem_assignment_lock:
    if M_bissette.is_state(S_bissette_find_poem_reference_book) and player.location.is_here(M_mia):
        call expression game.dialog_select("poem_assignment_lock_bissette_find_poem_reference_book")
    else:

        call expression game.dialog_select("poem_assignment_lock_bissette_reference_book_search")
    $ game.main()

label poem_assignment_lock_bissette_find_poem_reference_book:
    scene library
    show player 14f with dissolve
    player_name "I should go say hello to {b}Mia{/b}."
    hide player with dissolve
    return

label poem_assignment_lock_bissette_reference_book_search:
    scene library
    show player 14 with dissolve
    player_name "I should check {b}the back room{/b} for that book {b}Mia{/b} was talking about."
    hide player with dissolve
    return

label kamasutra:
    $ player.get_item("kamasutra")
    call expression game.dialog_select("kamasutra_dialogue")
    $ player.location.call_screen(ui = False)

label kamasutra_dialogue:
    scene libraryshelf with None
    show book_02_c at truecenter with dissolve
    player_name "Woa..."
    player_name "This book has all sorts of sex...positions?"
    player_name "It must be what she asked for..."
    hide book_02_c with dissolve
    return

label french_dictionary:
    $ player.get_item("french_dictionary")
    call expression game.dialog_select("french_dictionary_dialogue")

    $ player.location.call_screen(ui = False)

label french_dictionary_dialogue:
    scene libraryshelf with None
    player_name "Aha! French to English dictionary!"
    player_name "Great! Now I can-"
    show book_03_c at truecenter with dissolve
    player_name "Wait a second..."
    player_name "Some of the pages are missing!"
    player_name "Now what do I do?"
    pause
    player_name "Hopefully nothing important is gone."
    hide book_03_c with dissolve
    return

label library_old_book:
    $ player.get_item("old_book")
    call expression game.dialog_select("library_old_book_dialogue")
    $ player.location.call_screen(ui = False)

label library_old_book_dialogue:
    scene libraryshelf with None
    show closeup_book_09 at truecenter with dissolve
    player_name "This book looks like it would be useful decoding something."
    player_name "..."
    if not player.has_item("weird_coin"):
        player_name "Heh. Maybe some {b}hidden pirate treasure{/b} someone tossed aside carelessly."
        player_name "But that's just {b}wishful thinking{/b}."
    else:

        player_name "I think that {b}pirate coin{/b} had a four digit number on it."
        player_name "I should look at it again."
    show popup_item_book6 at truecenter with dissolve
    pause
    hide popup_item_book6 with dissolve
    hide closeup_book_09 with dissolve
    return

label breeding_guide:
    call expression game.dialog_select("breeding_guide_dialogue")
    $ player.get_item("breeding_guide")
    $ M_diane.trigger(T_diane_got_production_book)
    hide book_01_c with dissolve
    $ player.location.call_screen()

label breeding_guide_dialogue:
    scene libraryshelf
    player_name "( Hmm, Breeder's Guide? )"
    player_name "( This might have what I'm looking for... )"
    show book_01_c at truecenter with dissolve
    player_name "( Here we go, \"Increasing milk yield.\""
    pause
    player_name "!!!" with hpunch
    player_name "( Holy crap! )"
    player_name "( {b}Veronica{/b} was right! )"

    scene expression "backgrounds/location_library_day_blur.jpg"
    show player 369b
    with dissolve
    player_name "( It seems like, if {b}Diane{/b} get's pregnant, it will increase her milk production significantly. )"
    pause
    player_name "( *Gulp* )"
    player_name "( I know we've been having a bit of fun together but would {b}Diane{/b} really want to... )"
    player_name "( ... With me?! )"
    player_name "( ... )"
    player_name "( This is going to be a really awkward conversation. )"
    player_name "( ... But I promised I'd help her in any way I could! )"
    player_name "( {b}I have to show her this book!{/b} )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
