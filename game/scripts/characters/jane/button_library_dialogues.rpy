label jane_library_dialogue_bissette_find_dictionary:
    show jane 1f at Position (xpos=270)
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "I can't seem to find a {b}French dictionary{/b}."
    show player 5f
    show jane 2f
    jan "Hmm, let me see..."
    show jane 1b
    pause
    show jane 2b
    jan "It should be over on there on shelf, next to the back room."
    show jane 1f
    show player 14f
    player_name "Alright, I'll take a look. Thanks."
    return

label jane_library_dialogue_bissette_get_dictionary:
    show jane 1f at Position (xpos=270)
    show xtra 42
    show player 504f at right
    with dissolve
    player_name "Well, I found part of a French dictionary."
    show player 503f
    show jane 4f
    jan "What?"
    show player 5f
    show jane 17bf
    with dissolve
    jan "Oh no!"
    jan "I'll have to order a new one but it'll take awhile to arrive."
    jan "Did you still want to check it out?"
    show jane 18bf
    show player 10f
    player_name "Yeah, I'm pretty desperate. I'll just have to hope I don't need those missing pages..."
    show player 5f
    show jane 17bf
    jan "Okay, well, sorry again!"
    show jane 18f
    jan "You can just keep it. It won't be much use around here..."
    show jane 1f with dissolve
    show player 504f with dissolve
    player_name "Thanks!"
    show player 503f
    show jane 3f
    jan "No problem, have a nice day!"
    hide player
    hide jane
    with dissolve

    scene library
    show player 34 with dissolve
    player_name "( I guess I should take this to {b}Miss Bissette{/b} and see what she thinks... )"
    return

label jane_library_dialogue_bissette_return_overdue_books:
    show jane 1f at Position (xpos=270)
    show xtra 42
    show player 14f at right
    with dissolve
    player_name "I found all the overdue books!"
    show player 239_240f with dissolve
    pause
    show player 507f at Position (xoffset=-9) with dissolve
    show jane 2f
    jan "Really? Let's see..."
    show player 13f
    show jane 22f at Position (xoffset=-18) with dissolve
    jan "You did it! Thanks a lot!"
    jan "I've got something for you too."
    show jane 21f at Position (xoffset=-18)
    show player 10f
    player_name "You do?"
    show jane 20f with dissolve
    jan "Yup, that book you ordered came in."
    show jane 19f with dissolve
    pause
    show player 521f
    show jane 1f
    with dissolve
    player_name "Thanks!"
    player_name "{b}101 Types of Cheese{/b}..."
    show player 5f with dissolve
    show jane 2f
    jan "Will that work?"
    show jane 1f
    show player 10f
    player_name "Err, I'll have to make do."
    show player 14f
    player_name "Thanks again!"
    show player 13f
    show jane 3f
    jan "Come back and see us!"
    return

label jane_library_dialogue_pre:
    show jane 2f at Position (xpos=270)
    show xtra 42
    show player 1f at right
    with dissolve
    jan "Hi! How can I help you?"
    show player 2f
    show jane 1f
    player_name "Hi, I'm looking for a {b}book{/b}."
    show player 1f
    show jane 2f
    jan "Sure thing! Do you know the book's name?"
    show jane 1f
    return

label jane_library_dialogue_production_ask_librarian:
    scene librarydesk
    show jane 1f at Position (xpos=270)
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "You wouldn't happen to have any books on increasing milking, would you?"
    show player 5f
    show jane 4f
    jan "... Umm, that's a weird question."
    show jane 1f
    show player 29f with dissolve
    player_name "Ehh, yeah. I suppose it is."
    player_name "It's for my uhh... Friend."
    show player 3f at Position (xoffset=-8)
    show jane 3f
    jan "Heh, sure it is."
    show jane 7f with dissolve
    jan "Umm, I don't know."
    jan "I'm sure we have stuff on cows but as far as milking goes..."
    show jane 2f
    jan "{b}Try that shelf over there.{/b}"
    show jane 1f
    show player 14f with dissolve
    player_name "Thanks!"
    hide player with dissolve
    pause
    show jane 4f
    jan "What a weirdo..."
    hide jane
    with dissolve
    return

label jane_library_dialogue_french_poetry:
    show player 10f
    player_name "Do you have any French Poetry?"
    show player 5f
    show jane 1b
    jan "Hmm..."
    show jane 2f
    jan "Actually..."
    jan "Some girls were here reading something like that {b}yesterday afternoon{/b}."
    show jane 1f
    show player 10f
    player_name "Really?"
    show player 12f
    player_name "Did they check it out?"
    show player 5f
    show jane 2f
    jan "No."
    show jane 1f
    show player 10f
    player_name "Do you know where it is?"
    show player 5f
    show jane 5f
    jan "..."
    show jane 4f
    jan "No..."
    jan "But, maybe they'll be here again this {b}afternoon{/b}."
    jan "You could ask one of them where they put it."
    show jane 1f
    show player 12f
    player_name "Thanks."
    return

label jane_library_dialogue_french_food_find_books:
    show player 10f
    player_name "I was wondering if you had any books in French about food?"
    show player 13f
    show jane 3f
    jan "That's an interesting subject..."
    show jane 1f
    show player 14f
    player_name "Yeah, I need it for a school assignment."
    show player 13f
    show jane 2f
    jan "Alright, let me look and see what we have."
    show jane 1b
    jan "..."
    show player 11f
    player_name "..."
    show player 5f
    show jane 2b
    jan "Hmm, we don't appear to have anything like that."
    show jane 1f
    show player 12f
    player_name "Nothing?"
    show player 5f
    show jane 2b
    jan "No... Oh, wait a second!"
    jan "It's saying our sister branch has a French book about cheese."
    show jane 2f
    jan "Would that work?"
    show jane 1f
    show player 14f
    player_name "Sure, I love cheese! Where do I need to pick it up?"
    show player 13f
    show jane 2f
    jan "I can request them to send it here. Should only take a few days..."
    jan "In the meantime, I wonder if you could you help me out with something?"
    show jane 1f
    show player 10f
    player_name "... Sure, I suppose. What is it you need?"
    show player 5f
    show jane 2f
    jan "{b}Some of your classmates have overdue books{/b} I'd like returned."
    jan "I've been sending letters to their homes but that doesn't seem to be working."
    jan "I'd hate to lose the books."
    show jane 1f
    show player 10f
    player_name "Yeah, I could try {b}speaking with them{/b}. What are their names?"
    show player 5f
    show jane 2b
    jan "Hmm, the first is a {b}Miss Martinez{/b}."
    jan "The second is a {b}Mr. Erik J-{/b}."
    show jane 1f
    show player 14f
    player_name "{b}Erik{/b} has a book out?!"
    player_name "Those should be easy."
    show player 13f
    show jane 2b
    jan "...And finally..."
    jan "Huh. It just says {b}Dexter{/b}."
    jan "Ring any bells?"
    show jane 1f
    show player 12f
    player_name "Oh man, not {b}Dexter{/b}... You're sure?"
    show player 11f
    show jane 2f
    jan "That's what the log says..."
    show jane 1f
    show player 12f
    player_name "Crap! Alright, I'll see what I can do."
    show player 5f
    show jane 3f
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
    show jane 2f
    jan "One second..."
    show jane 2b
    jan "Hmm, {b}Miss Martinez{/b}, {b}Mr. Erik{/b}, and a {b}Dexter{/b}."
    show jane 1f
    show player 12f
    player_name "Ugh, I forgot about {b}Dexter{/b}..."
    player_name "Alright, I'm on it."
    return

label jane_library_dialogue_magazines_first:
    show player 2f
    player_name "I'm making a collage for Art class and I need some old magazines."
    player_name "Could you show me where to find some?"
    show player 1f
    show jane 2f
    jan "You're out of luck I'm afraid. We stopped carrying those a few months ago."
    show player 10f
    show jane 1f
    player_name "You don't have any?"
    show player 1f
    show jane 2f
    jan "I'm afraid not. We sent all the ones we had off to be recycled."
    show player 10f
    show jane 1f
    player_name "Oh man..."
    player_name "Thanks anyways."
    show player 11f
    show jane 2f
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
    show jane 2f
    jan "Nope."
    jan "We cancelled the subscriptions and tossed what we had out."
    show jane 1f
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
    show jane 3f
    jan "Great!"
    return

label jane_library_dialogue_return_books_first:
    show jane 2f
    jan "Not many people do."
    show jane 1f
    show player 10f
    player_name "What happens then?"
    show player 5f
    show jane 8f
    jan "I hunt them down and break one of their legs so they don't do it again."
    show jane 12f
    show player 22f
    player_name "!!!"
    show jane 3f
    jan "Just kidding!"
    show jane 1f
    show player 29f with dissolve
    player_name "Oh."
    show player 3f at Position (xoffset=-8)
    return

label jane_library_dialogue_return_books_after:
    show jane 2f
    jan "Just set the books you want to return on the counter and I'll take care of it."
    show jane 3f
    jan "And come back soon!"
    return

label jane_library_dialogue_leave:
    show player 24f
    show jane 4f
    player_name "Sorry. I'll return once I remember the book's name."
    show player 5f
    show jane 2f
    jan "See you then."
    return

label jane_library_dialogue_french_grammar_pre:
    scene librarydesk
    show jane 2f at Position (xpos=270)
    show xtra 42
    show player 1f at right
    with dissolve
    jan "Hi! How can I help you?"
    show player 2f
    show jane 1f
    player_name "Hi, I'm looking for a book."
    show player 1f
    show jane 2f
    jan "Sure thing, do you know its name?"
    show jane 1f
    return

label jane_library_dialogue_french_grammar_volume_1:
    show player 14f at right
    show jane 1f
    player_name "Yeah, I need \"{b}French Grammar - Volume 1{/b}\""
    show player 1f
    show jane 4f
    jan "Did you get me what I asked you for?"
    show jane 1f
    return

label jane_library_dialogue_french_grammar_volume_1_have_webcam:
    show player 12f
    player_name "Yeah... Here's the {b}webcam{/b}."
    show player 239_240f
    pause
    show player 54 at Position(xoffset=-38) with fastdissolve
    pause
    show player 1f with fastdissolve
    show jane 3f
    jan "Thank you!"
    show player 16f
    show jane 1f
    player_name "..."
    show player 12f
    player_name "What about my {b}textbook{/b}?"
    show player 11f
    show jane 3f
    jan "Oh! Right..."
    show player 11f
    jan "It came in earlier today, I put it on the {b}shelf{/b} over there."
    jan "Go ahead and take it."
    show player 1f
    show jane 3f
    jan "See you next time!"
    return

label jane_library_dialogue_french_grammar_volume_1_do_not_have_webcam:
    show player 24f
    player_name "I don't have it yet..."
    show player 5f
    show jane 2f
    jan "I can't get that {b}textbook{/b} order for you then, you know that."
    jan "Come back when you have the {b}webcam{/b}, and we'll talk."
    return

label jane_library_dialogue_french_grammar_volume_2_first:
    show player 14f
    player_name "I need the book: {b}French Grammar - Volume 2{/b}"
    show player 1f
    show jane 2f
    jan "You know how it is..."
    jan "I still can't make any new orders at this moment."
    show player 12f
    show jane 1f
    player_name "Still??"
    show player 5f
    show jane 4f
    jan "I would love to get that for you... But our funds are still low."
    show player 10f
    show jane 1f
    player_name "What do you mean? I thought the new {b}webcam{/b} was helping??"
    show player 5f
    show jane 4f
    jan "Don't get me wrong: It's helping..."
    jan "but people are getting tired of the same stuff!"
    show player 10f
    show jane 1f
    player_name "So... What can we do?"
    show player 5f
    show jane 4f
    jan "Well, our viewers want more variety..."
    show player 11f
    show jane 3f
    jan "...and I maybe you could help with that!"
    show player 12f
    show jane 1f
    player_name "But, how?"
    show player 11f
    show jane 2f
    jan "Don't you go to school?"
    show player 12f
    show jane 1f
    player_name "Yeah?"
    show player 11f
    show jane 3f
    jan "Well, just hide one of my remote controlled {b}webcams{/b} in the school!"
    show jane 1f
    player_name "..."
    show player 12f
    player_name "Are you crazy?!"
    player_name "What if I got caught!"
    show jane 3f
    show player 90f
    jan "Relax! Just go at night, when no one is around."
    show player 37f
    show jane 1f
    player_name "Ugh... I can't believe I have to do this..."
    show jane 2f
    jan "Do you want those books, or not?"
    show player 24f
    show jane 1f
    player_name "I'll see what I can do..."
    return

label jane_library_dialogue_french_grammar_volume_2_repeat_pre:
    show player 14f
    player_name "I need the book: {b}French Grammar - Volume 2{/b}"
    show player 1f
    show jane 4f
    jan "Well? Did you do it?"
    show jane 1f
    return

label jane_library_dialogue_french_grammar_volume_2_repeat_placed_webcam:
    show player 12f
    player_name "Yeah. I placed it in the {b}lockeroom{/b}..."
    player_name "It's in the ceiling {b}air vent{/b}..."
    show player 1f
    show jane 3f
    jan "Thank you!"
    show player 16f
    show jane 1f
    player_name "..."
    show player 12f
    player_name "What about my {b}textbook{/b}?!"
    show player 11f
    show jane 3f
    jan "Oh! Right..."
    show player 11f
    show jane 15
    jan "Here it is!"
    $ player.get_item("textbook2")
    show player 30f
    show jane 1f
    player_name "Thanks!"
    show player 1f
    show jane 3f
    jan "See you next time!"
    return

label jane_library_dialogue_french_grammar_volume_2_repeat_havent_placed_webcam:
    show player 24f
    show jane 4f
    player_name "I didn't do it yet..."
    show player 5f
    show jane 2f
    jan "I can't get that {b}textbook{/b} order for you, then. You know that."
    jan "Come back when you placed the {b}webcam{/b} at school."
    return

label jane_library_dialogue_french_grammar_volume_3:
    show popup_unfinished at truecenter with dissolve
    pause
    hide popup_unfinished with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
