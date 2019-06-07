label erik_room_dialogue:
    $ player.go_to(L_erikhouse_erikroom)
    if erik.over(erik_crown_card) and not erik.known(erik_orcette):
        scene expression game.timer.image("erik_house_bedroom{}_b")
        show player 12 with dissolve
        player_name "( Huh, {b}Erik{/b} isn't here. He must be in the basement... )"
        hide player with dissolve

    elif erik.completed(erik_bullying) and not erik.known(erik_bullying_2):
        call expression game.dialog_select("erik_bullying")
        $ erik.add_event(erik_bullying_2)
        $ M_erik.unforce()

    elif erik.completed(erik_bullying_3) and not erik.known(erik_vr):
        call expression game.dialog_select("eriksroom_erik_bullying_3_completed")

    elif erik.over(erik_path_split) and erik.started(erik_sex_ed):
        call expression game.dialog_select("erik_sex_ed")
        $ erik_sex_ed.finish()
        $ M_erik.place(place = L_erikhouse_mrsjroom)

    elif June.started(june_intro):
        call expression game.dialog_select("june_intro")
        $ june_intro.finish()
        jump erik_talk

    elif erik.started(erik_breastfeeding):
        call expression game.dialog_select("eriksroom_erik_breastfeeding_started")
        $ erik_breastfeeding.finish()
        $ M_mrsj.set_default_locations([[L_erikhouse_entrance, L_yoga_room, L_erikhouse_mrsjroom, L_erikhouse_mrsjroom],
                                        [L_erikhouse_entrance, L_yoga_room, L_erikhouse_mrsjroom, L_erikhouse_mrsjroom]])

    if player.location.is_here(M_erik):
        if not erik.started(erik_card_hunt) and not player.location.is_here(M_june):
            $ playSound("<loop 3>audio/ambience_erikroom.ogg")
    $ game.main()

label erik_cards:
    if player.has_item("eriks_cards"):
        show erik 1 at right
        if player.location == L_school_scienceclassroom:
            show erikl 1f at right
        show player 14 at left
        player_name "I found your cards, {b}Erik{/b}!"
        show player 239_240
        pause
        show player 374 with dissolve
        player_name "Here you go..."
        show player 5 with dissolve
        if player.location == L_school_scienceclassroom:
            show erikl 35 at right
        show erik 36 at Position (xpos=1014)
        with dissolve
        eri "Awesome!"
        eri "Here, you have to see this new card I got."
        eri "It practically assures a swift victory in the upcoming tournament!"
        show erik 38
        eri "..."
        eri "Where is it?"
        pause
        show player 11
        eri "NO! It's not in here!"
        show player 12
        player_name "Are you sure?"
        show player 11
        show erik 37
        eri "Yes, I'm sure! I can't believe it! My {b}Cock Crown of Thorns{/b} card is gone!!"
        show erik 2 at right
        if player.location == L_school_scienceclassroom:
            show erikl 2 at right
        with dissolve
        eri "What am I going to do?"
        eri "I'm totally screwed now."
        show erik 3
        if player.location == L_school_scienceclassroom:
            show erikl 1f at right
        with dissolve
        eri "It was my... Precious..."
        show player 34
        player_name "Hmm..."
        show player 33
        player_name "I might be able to help."
        show player 13
        show erik 5
        eri "How so?"
        show erik 3b
        show player 17
        player_name "I could get you another one."
        show player 13
        show erik 5
        eri "How are you going to do that?"
        show erik 3b
        show player 35
        player_name "They sell these cards at {b}Cosmic Cumics{/b} don't they?"
        show player 13
        show erik 5
        eri "Yeah but they're expensive!"
        show erik 5b
        eri "... And I'm broke."
        show erik 3b
        pause
        show player 14
        player_name "No worries, Man. I'm working for {b}[deb_name]'s{/b} friend {b}Diane{/b} now."
        show player 13
        show erik 4
        eri "You'd really buy me a new one? You're the best, dude!"
        show erik 1
        show player 14
        player_name "I'm happy to help!"
        show player 17
        player_name "Besides, I want to see you win that tournament!"
        $ player.remove_item("eriks_cards")
        $ erik_card_hunt.finish()
        $ erik.add_event(erik_crown_card)
    else:
        show erik 1 at right
        show player 10 at left
        player_name "Where did you see your cards last?"
        show player 11
        show erik 5
        eri "Hmm... I think that the last time I took them out was down here."
        eri "I was playing in the basement... But, {b}Mrs. Johnson{/b} must've put them somewhere..."
        show erik 1
        show player 14
        player_name "I'll help you find them."
        show player 13
        show erik 5
        eri "Thanks."
        show erik 3
        eri "I really have to find them before the tournament next weekend..."
    hide erik
    hide erikl
    hide player
    with dissolve
    return

label erik_crown_card:
    if player.has_item("card02"):
        show erik 1 at right
        if player.location == L_school_scienceclassroom:
            show erikl 1f at right
        show player 14 at left
        player_name "I got that card you wanted."
        show player 13
        show erik 4
        eri "The {b}Cock Crown of Thorns{/b}!?"
        show erik 1
        show player 2
        player_name "Yup!"
        show player 239_240
        pause
        show player 372 with dissolve
        player_name "Here you go..."
        show player 13 with dissolve
        show erik 40 at Position (xpos=1014)
        if player.location == L_school_scienceclassroom:
            show erikl 40 at right
        with dissolve
        eri "You're awesome! Thank you so much!"
        eri "With this card my victory is assured!"
        eri "I will be unstoppable! Peasants will bow before me..."
        show erik 39
        show player 17
        player_name "Ha ha."
        show player 13
        pause
        show erik 41
        eri "Hold on a second."
        show erik 36
        if player.location == L_school_scienceclassroom:
            show erikl 35 at right
        with dissolve
        eri "I want you to have one of my cards..."
        show erik 30 at Position (xpos=1025)
        if player.location == L_school_scienceclassroom:
            show erikl 30 at right
        with dissolve
        show player 10
        player_name "A card?"
        show player 11
        show erik 31
        eri "It's one of my favorites... But I have a few copies..."
        show erik 1
        if player.location == L_school_scienceclassroom:
            show erikl 1f at right
        with dissolve
        show player 371 with dissolve
        player_name "Huh..."
        hide player
        hide erik
        hide erikl
        with dissolve
        show card_03_c at Position (ypos=650) with dissolve
        pause
        hide card_03_c with dissolve
        show erik 1 at right
        if player.location == L_school_scienceclassroom:
            show erikl 1f at right
        show player 370 at left
        with dissolve
        player_name "...Thanks!"
        show player 13 with dissolve
        show erik 4
        eri "Don't worry about it!"
        eri "It's to thank you for getting me that card."
        eri "Plus, I know you'll take care of her properly."
        show erik 1
        show player 14
        player_name "Well, thanks man!"
        show player 13
        show erik 5
        eri "Just... Make sure you keep it out of the sunlight so it doesn't fade."
        show erik 1
        show player 17
        player_name "Ha ha, I promise..."
        $ player.remove_item("card02")
        show unlock37 at truecenter with dissolve
        $ player.get_item("card03")
        pause
        hide unlock37 with dissolve
        $ erik_crown_card.finish()
        $ M_erik.place(place = L_erikhouse_basement)
        $ M_erik.force()
    else:

        show erik 1 at right
        if player.location == L_school_scienceclassroom:
            show erikl 1f at right
        show player 10 at left
        player_name "Which card is missing again?"
        show player 11
        show erik 5
        eri "Hmm... It's called the {b}Cock Crown of Thorns{/b}."
        eri "You said you might find it at {b}Cosmic Cumics{/b}?"
        show erik 1
        show player 14
        player_name "Oh, right!"
        player_name "I'll see if it's there..."
    hide erik
    hide erikl
    hide player
    with dissolve
    $ game.main()

label erik_package:
    if player.has_item("orcette"):
        show erik 1 at right
        show player 376 at left with dissolve
        player_name "Here's your new toy!"
        show player 378
        show erik 4
        eri "What? You got it already?"
        show erik 1
        show player 376
        player_name "Yup!"
        show player 13 with dissolve
        show erik 43 at Position (xpos=1014)
        if player.location == L_school_scienceclassroom:
            show erikl 42 at right
        with dissolve
        eri "Sweet!"
        eri "This thing looks... Awesome!"
        eri "They even got the colors just right..."
        show player 14
        player_name "You ever used one of these before?"
        show player 13
        show erik 44
        eri "No, but I've always wanted to try it out!"
        eri "{b}Mrs. Johnson{/b} didn't see it did she? I don't want her freaking out..."
        show erik 42
        show player 12
        player_name "Heh, I think she'd be okay with it. She seems really cool!"
        show player 13
        show erik 44
        eri "Maybe..."
        show erik 42
        show player 12
        player_name "Is that thing... easy to clean?"
        show player 13
        show erik 43
        eri "I think it came with instructions, but I should just have to rinse it out."
        show erik 42
        pause
        show erik 43
        pause
        show player 18
        player_name "..."
        show player 17
        player_name "Oh {b}Erik{/b}..."
        show player 18
        show erik 44
        eri "What?!"
        show erik 42
        show player 14
        player_name "Nothing."
        show player 13
        show erik 43
        pause
        show player 33
        player_name "Well, I should probably leave you two alone..."
        show player 13
        show erik 44
        eri "{b}[firstname]{/b}, thanks again."
        show erik 43
        show player 14
        player_name "It's fine..."
        player_name "...Just be sure to lock the door!"
        $ player.remove_item("orcette")
        $ erik_orcette_2.finish()
        $ event_wait_till = game.timer.game_day() + 2
    else:
        show erik 1 at right
        show player 12 at left
        player_name "What item did you want again?"
        show player 13
        show erik 5
        eri "It's like a rubber tube... It's called the {b}Orcette{/b}..."
        eri "You can find it online."
        show erik 1
        show player 14
        player_name "Alright, got it."
        show player 13
        show erik 4
        eri "Thanks, {b}[firstname]{/b}."
    hide erik
    hide erikl
    hide player
    with dissolve
    $ game.main()

label erik_vr_game:
    if player.has_item("game02") and player.has_item("virtualsaga"):
        show erik 1 at right with dissolve
        show player 14 at left with dissolve
        player_name "I got it!"
        show player 239_240
        pause
        show player 400
        player_name "I got the headset!"
        show player 399
        show erik 4
        eri "Oh yeah?!"
        show player 13 with dissolve
        show erik 46
        if player.location == L_school_scienceclassroom:
            show erikl 45 at right
        with dissolve
        eri "Wow... That must of been expensive..."
        show erik 47
        eri "How much was it?!"
        show erik 45
        show player 17
        player_name "Ehh, don't worry about it."
        show player 14
        player_name "I've been saving up some money."
        show player 13
        show erik 46
        eri "That's... Awesome."
        show erik 45
        show player 12
        player_name "Oh, here's the game, too!"
        show player 13
        show erik 47
        eri "Thanks, {b}[firstname]{/b}."
        eri "I've mentioned having people over to the basement to {b}Mrs. Johnson{/b}."
        eri "She didn't seem to mind us using it."
        eri "She always bugs me about never having friends over..."
        show erik 45
        show player 14
        player_name "Great!"
        show player 33
        player_name "Hmm... I'll have to think about who we could invite over."
        show player 13
        show erik 47
        eri "I don't really know anyone, but I'll go with whoever you find!"
        show erik 45
        show player 14
        player_name "Ok!"
        show player 13
        show erik 46
        eri "Thanks again for the headset! I can't wait to try it out!"
        show erik 49
        if player.location == L_school_scienceclassroom:
            show erikl 48 at right
        with dissolve
        show player 14
        player_name "You're welcome."
        eri "Awesome..."
        show erik 49
        pause
        player_name "See you later, {b}Erik{/b}."
        $ player.remove_item("game02")
        $ player.remove_item("virtualsaga")
        $ erik_vr.finish()
        $ M_mrsj.place(place = L_erikhouse_entrance)
        $ M_mrsj.force()
    else:

        show erik 1 at right
        show player 10 at left
        with dissolve
        player_name "What did you want in exchange for using the basement?"
        show player 5
        show erik 5
        eri "Hmm... The VR headset {b}Virtual Saga X{/b}..."
        show erik 4
        eri "...And that new game, called {b}World of Orcette{/b}..."
        show erik 1
        show player 10
        player_name "Where did you say they sold it?"
        show player 5
        show erik 5
        eri "At {b}Cosmic Cumics{/b}."
        show erik 1
        show player 14
        player_name "Ok. I'll see if I can find it there.."
        show player 13
        show erik 4
        eri "Thanks, {b}[firstname]{/b}!"
    hide player
    hide erik
    hide erikl
    with dissolve
    $ game.main()

label sock_pile_book_search:
    scene expression game.timer.image("eriks_room{}_c")
    show player 517 with dissolve
    player_name "Hmm, what's with these socks?"
    player_name "They're stiff as a board!"
    show player 516
    player_name "..."
    show player 517
    player_name "Gross..."
    player_name "I'm not even going to bother digging for the book in there..."
    hide player with dissolve
    $ game.main()

label dresser_book_search:
    scene expression game.timer.image("backgrounds/location_erik_house_bedroom_dresser_day{}.jpg")
    player_name "!!!"
    player_name "Are those stained?"
    pause
    player_name "His dresser is such a mess like his room!"
    $ game.main()

label under_bed_book_search:
    scene expression game.timer.image("under_eriks_bed{}")
    show book_03 at Position (xpos=431,ypos=425,xanchor=0,yanchor=0)
    player_name "Just a bunch of dust bunnies..."
    player_name "...Wait a minute! There's a book under here!"
    call screen under_eriks_bed

    player_name "Sweet, this is it!"
    hide book_03
    show book_04_c with dissolve
    player_name "{b}Oedipuss{/b}?"
    player_name "Doin' it the Ancient Way..."
    player_name "Why in the world would {b}Erik{/b} want this?"
    hide book_04_c with dissolve

    scene expression game.timer.image("eriks_room{}_c")
    if M_bissette.get_state() == S_bissette_jane_return_books:
        show player 12 with dissolve
        player_name "Well, two more books to go."

    elif M_bissette.get_state() in [S_bissette_got_dexters_book, S_bissette_got_eriks_book, S_bissette_got_martinez_book]:
        show player 14 with dissolve
        player_name "Just one book left."
    else:

        show player 14 with dissolve
        player_name "Great! That's the last book!"
        player_name "Now I just need to return them to the library!"
    hide player with dissolve
    $ M_bissette.trigger(T_bissette_ask_erik)
    $ player.get_item("oedipuss")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
