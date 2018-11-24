label backroom_blocked_dialogue:
    scene library
    show player 35 with dissolve
    player_name "Hmm... I'm not sure where the school {b}textbooks{/b} are..."
    player_name "Maybe I should ask the {b}Librarian{/b} at the {b}reception desk{/b} first."
    hide player 35 with dissolve
    $ game.main()

label backroom_dialogue_backroom_count:
    scene backroom01
    show library 1_2 at Position(xpos = 486, ypos = 707) with dissolve
    player_name "( OH SHIT!!! )"
    player_name "..."
    player_name "( People are having sex back here... )"
    pause 4
    player_name "..."
    player_name "( Is that a webcam on the shelf? )"
    player_name "( I think it's filming... Do they even know that it's there? )"
    player_name "( Should I tell the {b}librarian{/b}? )"
    return

label backroom_couple_finish:
    call expression game.dialog_select("backroom_couple_finish_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jane"]["unlocked"] = True
    $ persistent.cookie_jar["Jane"]["gallery"]["01_unlocked"] = True
    if quest06 not in completed_quests:
        $ quest_list.append(quest06)
    $ backroom_count = 2

    $ game.main()

label backroom_couple_finish_dialogue:
    scene backroom01
    show library 1_2 at Position(xpos = 486, ypos = 707)
    pause 4
    hide library 1_2
    pause .2
    show library 3 at Position(xpos = 486, ypos = 707) with dissolve
    window hide
    pause
    show library 4
    window hide
    pause
    player_name "( Oh shit! )"
    player_name "( I hear someone coming!! )"
    show library 5 at Position(xpos = 512, ypos = 707) with hpunch
    window hide
    pause
    hide library with dissolve

    scene backroom01
    show jane 8 at right
    show player 23 at left
    with dissolve
    jan "Oh for crying out loud!"
    show player 11
    jan "NOT AGAIN!!!" with hpunch
    show jane 7 with dissolve
    jan "Ugh..."
    show jane 12 with dissolve
    show player 10
    player_name "Is this common?"
    show player 5
    show jane 5
    jan "..."
    show jane 4
    jan "Unfortunately..."
    jan "People seem to love doing it back here."
    jan "Just keep this to yourself, pretty please?"
    show jane 1
    show player 12
    player_name "Yeah, I won't tell anyone..."
    show player 5
    show jane 2
    jan "Thanks."
    jan "I'm going back to my desk."
    jan "If you need help finding something or you see anyone else doing it in here, let me know!"
    hide jane with dissolve
    show player 17
    player_name "I should visit the library more often!"
    hide player with dissolve
    return

label poem_assignment_book:
    call expression game.dialog_select("poem_assignment_book_dialogue")
    $ M_bissette.trigger(T_bissette_reference_book_found)
    $ player.get_item("french_love")

    $ game.main()

label poem_assignment_book_dialogue:
    scene backroom01
    show book_01 at Position (xpos=376,ypos=426,xanchor=0,yanchor=0)
    player_name "This must be the book-"
    show book_07_c with dissolve
    player_name "!!!" with hpunch
    player_name "Whoa!"
    player_name "{b}Mia{/b} was right. This thing is really graphic!"
    player_name "Hmm, I wonder what {b}Judith{/b} was doing with it back here in this dark room by herself?"
    player_name "..."
    player_name "Alright, I had better take this home to {b}my computer{/b} and get to writing on that poem for {b}Miss Bissette{/b}."
    pause
    hide book_01
    hide book_07_c with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
