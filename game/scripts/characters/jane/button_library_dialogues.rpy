label jane_library_dialogue_bissette_find_dictionary:
    show jane f_normal at flip
    show jane at Position (xpos=100)
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "I can't seem to find a {b}French dictionary{/b}."
    show player 5f
    show jane f_normal_talk
    jan "Hmm, let me see..."
    show jane f_normal_down
    pause
    show jane f_normal_talk_down
    jan "It should be over on there on shelf, next to the back room."
    show jane f_normal
    show player 14f
    player_name "Alright, I'll take a look. Thanks."
    return

label jane_library_dialogue_bissette_get_dictionary:
    show jane f_normal at flip
    show jane at Position (xpos=100)
    show xtra 42
    show player 504f at right
    with dissolve
    player_name "Well, I found part of a French dictionary."
    show player 503f
    show jane f_sad_talk
    jan "What?"
    show player 5f
    show jane f_complain_down a_dressed_book1
    with dissolve
    jan "Oh no!"
    jan "I'll have to order a new one but it'll take awhile to arrive."
    show jane f_sad_talk
    jan "Did you still want to check it out?"
    show jane f_sad
    show player 10f
    player_name "Yeah, I'm pretty desperate. I'll just have to hope I don't need those missing pages..."
    show player 5f
    show jane f_sad_talk
    jan "Okay, well, sorry again!"
    show jane f_normal_talk
    jan "You can just keep it. It won't be much use around here..."
    show jane f_normal a_dressed_sides with dissolve
    show player 504f with dissolve
    player_name "Thanks!"
    show player 503f
    show jane f_laugh
    jan "No problem, have a nice day!"
    hide player
    hide jane
    with dissolve

    scene library
    show player 34 with dissolve
    player_name "( I guess I should take this to {b}Miss Bissette{/b} and see what she thinks... )"
    return

label jane_library_dialogue_bissette_return_overdue_books:
    show jane f_normal at flip
    show xtra 42
    show player 14f at right
    with dissolve
    player_name "I found all the overdue books!"
    show player 239_240f with dissolve
    pause
    show player 507f at Position (xoffset=-9) with dissolve
    show jane f_normal_talk
    jan "Really? Let's see..."
    show player 13f
    show jane f_normal_talk a_dressed_book3 with dissolve
    jan "You did it! Thanks a lot!"
    jan "I've got something for you too."
    show jane f_normal
    show player 10f
    player_name "You do?"
    show jane f_normal_talk a_dressed_book2 with dissolve
    jan "Yup, that book you ordered came in."
    show jane f_normal
    pause
    show player 521f
    show jane f_normal a_dressed_sides
    with dissolve
    player_name "Thanks!"
    player_name "{b}101 Types of Cheese{/b}..."
    show player 5f with dissolve
    show jane f_normal_talk
    jan "Will that work?"
    show jane f_normal
    show player 10f
    player_name "Err, I'll have to make do."
    show player 14f
    player_name "Thanks again!"
    show player 13f
    show jane f_laugh
    jan "Come back and see us!"
    return

label jane_library_dialogue_pre:
    show jane f_normal_talk at flip
    show jane at Position (xpos=100)
    show xtra 42
    show player 1f at right
    with dissolve
    jan "Hi! How can I help you?"
    show player 2f
    show jane f_normal
    player_name "Hi, I'm looking for a {b}book{/b}."
    show player 1f
    show jane f_normal_talk
    jan "Sure thing! Do you know the book's name?"
    show jane f_normal
    return

label jane_library_dialogue_production_ask_librarian:
    scene librarydesk
    show jane f_normal at flip
    show jane at Position (xpos=100)
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "You wouldn't happen to have any books on increasing milking, would you?"
    show player 5f
    show jane f_sad_talk
    jan "... Umm, that's a weird question."
    show jane f_normal
    show player 29f with dissolve
    player_name "Ehh, yeah. I suppose it is."
    player_name "It's for my uhh... Friend."
    show player 3f at Position (xoffset=-8)
    show jane f_laugh
    jan "Heh, sure it is."
    show jane f_eyeroll_talk a_dressed_up with dissolve
    jan "Umm, I don't know."
    jan "I'm sure we have stuff on cows but as far as milking goes..."
    show jane f_normal_talk
    jan "{b}Try that shelf over there.{/b}"
    show jane f_normal a_dressed_sides
    show player 14f
    with dissolve
    player_name "Thanks!"
    hide player with dissolve
    pause
    show jane f_sad_talk
    jan "What a weirdo..."
    hide jane
    with dissolve
    return

label jane_library_dialogue_french_poetry:
    show player 10f
    player_name "Do you have any French Poetry?"
    show player 5f
    show jane f_normal_down
    jan "Hmm..."
    show jane f_normal_talk
    jan "Actually..."
    jan "Some girls were here reading something like that {b}yesterday afternoon{/b}."
    show jane f_normal
    show player 10f
    player_name "Really?"
    show player 12f
    player_name "Did they check it out?"
    show player 5f
    show jane f_normal_talk
    jan "No."
    show jane f_normal
    show player 10f
    player_name "Do you know where it is?"
    show player 5f
    show jane f_normal_down
    jan "..."
    show jane f_sad_talk
    jan "No..."
    jan "But, maybe they'll be here again this {b}afternoon{/b}."
    jan "You could ask one of them where they put it."
    show jane f_normal
    show player 12f
    player_name "Thanks."
    return

label jane_library_dialogue_french_food_find_books:
    show player 10f
    player_name "I was wondering if you had any books in French about food?"
    show player 13f
    show jane f_laugh
    jan "That's an interesting subject..."
    show jane f_normal
    show player 14f
    player_name "Yeah, I need it for a school assignment."
    show player 13f
    show jane f_normal_talk
    jan "Alright, let me look and see what we have."
    show jane f_normal_down
    jan "..."
    show player 11f
    player_name "..."
    show player 5f
    show jane f_normal_talk_down
    jan "Hmm, we don't appear to have anything like that."
    show jane f_normal
    show player 12f
    player_name "Nothing?"
    show player 5f
    show jane f_normal_talk_down
    jan "No... Oh, wait a second!"
    jan "It's saying our sister branch has a French book about cheese."
    show jane f_normal_talk
    jan "Would that work?"
    show jane f_normal
    show player 14f
    player_name "Sure, I love cheese! Where do I need to pick it up?"
    show player 13f
    show jane f_normal_talk
    jan "I can request them to send it here. Should only take a few days..."
    jan "In the meantime, I wonder if you could you help me out with something?"
    show jane f_normal
    show player 10f
    player_name "... Sure, I suppose. What is it you need?"
    show player 5f
    show jane f_normal_talk
    jan "{b}Some of your classmates have overdue books{/b} I'd like returned."
    jan "I've been sending letters to their homes but that doesn't seem to be working."
    jan "I'd hate to lose the books."
    show jane f_normal
    show player 10f
    player_name "Yeah, I could try {b}speaking with them{/b}. What are their names?"
    show player 5f
    show jane f_normal_talk_down
    jan "Hmm, the first is a {b}Miss Martinez{/b}."
    jan "The second is a {b}Mr. Erik J-{/b}."
    show jane f_normal
    show player 14f
    player_name "{b}Erik{/b} has a book out?!"
    player_name "Those should be easy."
    show player 13f
    show jane f_normal_talk_down
    jan "...And finally..."
    jan "Huh. It just says {b}Dexter{/b}."
    jan "Ring any bells?"
    show jane f_normal
    show player 12f
    player_name "Oh man, not {b}Dexter{/b}... You're sure?"
    show player 11f
    show jane f_normal_talk
    jan "That's what the log says..."
    show jane f_normal
    show player 12f
    player_name "Crap! Alright, I'll see what I can do."
    show player 5f
    show jane f_laugh
    jan "Thanks, I really appreciate this!"
    hide jane with dissolve
    show player 12 at center with dissolve
    player_name "Ugh, why did it have to be {b}Dexter{/b}?"
    return

label jane_library_dialogue_french_food_book_holders:
    show player 10f
    player_name "What were the students names again?"
    player_name "You know, the ones with the overdue books."
    show player 5f
    show jane f_normal_talk
    jan "One second..."
    show jane f_normal_talk_down
    jan "Hmm, {b}Miss Martinez{/b}, {b}Mr. Erik{/b}, and a {b}Dexter{/b}."
    show jane f_normal
    show player 12f
    player_name "Ugh, I forgot about {b}Dexter{/b}..."
    player_name "Alright, I'm on it."
    return

label jane_library_dialogue_magazines_first:
    show player 2f
    player_name "I'm making a collage for Art class and I need some old magazines."
    player_name "Could you show me where to find some?"
    show player 1f
    show jane f_normal_talk
    jan "You're out of luck I'm afraid. We stopped carrying those a few months ago."
    show player 10f
    show jane f_normal
    player_name "You don't have any?"
    show player 1f
    show jane f_normal_talk
    jan "I'm afraid not. We sent all the ones we had off to be recycled."
    show player 10f
    show jane f_normal
    player_name "Oh man..."
    player_name "Thanks anyways."
    show player 11f
    show jane f_normal_talk
    jan "Sorry."

    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "What am I gonna do now?"
    show player 11
    player_name "..."
    show player 10
    player_name "I guess {b}I'll head back to school and look around{/b}."
    player_name "There's gotta be some magazines somewhere."
    return

label jane_library_dialogue_magazines_repeat:
    show player 10f
    player_name "So don't have a single magazine around here?"
    show player 11f
    show jane f_normal_talk
    jan "Nope."
    jan "We cancelled the subscriptions and tossed what we had out."
    show jane f_normal
    show player 10f
    player_name "Okay, thanks anyways."
    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "{b}*Sigh*{/b}"
    player_name "I guess I should {b}head back to school and look around there.{/b}"
    player_name "... Maybe I'll get lucky?"
    return

label jane_library_dialogue_return_books_pre:
    show player 14f
    player_name "I'd like to return a book."
    show player 13f
    show jane f_laugh
    jan "Great!"
    return

label jane_library_dialogue_return_books_first:
    show jane f_normal_talk
    jan "Not many people do."
    show jane f_normal
    show player 10f
    player_name "What happens then?"
    show player 5f
    show jane f_mad_talk
    jan "I hunt them down and break one of their legs so they don't do it again."
    show jane f_mad
    show player 22f
    player_name "!!!"
    show jane f_laugh
    jan "Just kidding!"
    show jane f_normal
    show player 29f with dissolve
    player_name "Oh."
    show player 3f at Position (xoffset=-8)
    return

label jane_library_dialogue_return_books_after:
    show jane f_normal_talk
    jan "Just set the books you want to return on the counter and I'll take care of it."
    show jane f_laugh
    jan "And come back soon!"
    return

label jane_library_dialogue_leave:
    show player 24f
    show jane f_sad_talk
    player_name "Sorry. I'll return once I remember the book's name."
    show player 5f
    show jane f_normal_talk
    jan "See you then."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
