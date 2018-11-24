label bissette_dialogue_meet_in_office:
    show player 10 at left
    show teacher 1 at right
    with dissolve
    player_name "{b}Miss Bissette{/b}, what did you need me to do?"
    show player 5
    show teacher 12
    bis "Oh, {b}[firstname]{/b}. Not here. {b}Come see me in my office after school{/b}, yes?"
    show teacher 13
    show player 14
    player_name "Okay, I'll meet you there."
    return

label bissette_dialogue_check_dictionary:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "Hey, {b}Miss Bissette{/b}. I found a dictionary at the library but it's missing a few pages."
    show player 239_240 with dissolve
    pause
    show player 503 with dissolve
    pause
    show player 5
    show teacher 22b
    with dissolve
    bis "Oh my!"
    bis "This will make things very difficult, I think."
    bis "The French to English section is intact but you are missing many words..."
    bis "I'm afraid some of them might be crucial to the subjects we are to be studying."
    show teacher 21b
    show player 10
    player_name "Ugh, I was afraid of that.."
    show player 5
    show teacher 21
    bis "Hmm, perhaps all is not lost. I'm sure {b}a classmate of yours{/b} would be willing to let you copy the missing pages from their dictionary."
    bis "You can use the {b}photo copier in the computer lab{/b}."
    show teacher 22
    show player 14
    player_name "That's a good idea!"
    show player 13
    show teacher 2 with dissolve
    bis "Vous etes le bienvenu, {b}[firstname]{/b}."
    bis "Be sure to get English words beginning with the letter 'B' for our next lesson."
    show teacher 1
    show player 14
    player_name "Alright, time to track down another dictionary..."
    show player 13
    show teacher 12
    bis "Working so hard already. I can tell you are desiring the special reward, very much, yes?"
    show teacher 13
    show player 10
    player_name "Any thoughts on whose dictionary I should be asking to borrow?"
    show player 13
    show teacher 11
    bis "Hmm..."
    show teacher 2
    bis "Perhaps {b}Judith{/b}?"
    bis "She shows much talent for the French tongue..."
    show teacher 1
    show player 14
    player_name "Okay, I'll start with {b}Judith{/b} then."
    return

label bissette_dialogue_intro:
    show player 1 at left
    show teacher 2 at right
    with dissolve
    bis "Hi, {b}[firstname]{/b}!"
    show player 17 at left
    show teacher 1 at right
    player_name "Hi, {b}Miss Bissette{/b}!"
    show player 1 at left
    show teacher 2 at right
    bis "Have you been able to catch up on your studies?"
    bis "I really hope you do!"
    bis "Now, is there something you wanted to talk about?"
    show teacher 1
    return

label bissette_dialogue_food_assignment_intro:
    show player 10
    player_name "What my next assignment?"
    show player 5
    show teacher 2
    bis "I want you to {b}write a few paragraphs about your favorite food, en Francais{/b}."
    bis "Then we will go over it together, yes?"
    show teacher 1
    show player 14
    player_name "Oh, yeah!"
    return

label bissette_dialogue_food_assignment_prepare_assignment:
    player_name "I should visit that librarian again. Maybe she could find a book about {b}French food{/b} for me."
    player_name "Then I can type something up at my computer."
    player_name "Thanks, {b}Miss Bissette{/b}!"
    return

label bissette_dialogue_food_assignment_do_assignment:
    player_name "I should type something up at my computer."
    player_name "Thanks, {b}Miss Bissette{/b}!"
    return

label bissette_dialogue_poem_assignment_intro:
    show player 10
    player_name "Remind me, what was the assignment again?"
    show player 5
    show teacher 2
    bis "Le quel? Tu as deja oublie?"
    bis "{b}You are to be writing a romantic poem en Francias{/b}!"
    show teacher 1
    show player 14
    player_name "Oh, right!"
    player_name "Thanks, {b}Miss Bissette{/b}."
    show player 13
    show teacher 2
    bis "Return to me once it's complete."
    bis "Don't keep me waiting, mon bel homme."
    return

label bissette_dialogue_poem_assignment_do_assignment:
    show player 14
    player_name "I should type something up at my computer."
    return

label bissette_dialogue_poem_assignment_print_assignment:
    show player 14
    player_name "I finished the poem, {b}Miss Bissette{/b}."
    show player 13
    show teacher 2
    bis "Great, let me see!"
    show teacher 1
    show player 10
    player_name "Oh, I need to print it out first..."
    show player 5
    show teacher 2
    bis "Well, the printer is in the {b}computer lab{/b}, yes?"
    show teacher 1
    show player 14
    player_name "Yup, be right back!"
    return

label bissette_dialogue_private_tutoring:
    show player 10
    player_name "Do you think we could meet in your office tonight?"
    show player 26
    player_name "You know, for some... Tutoring?"
    show player 13
    show teacher 12
    bis "Oh, tutoring. Oui!"
    bis "I'll see you tonight for some one on one time, yes?"
    show teacher 13
    show player 33
    player_name "Oui!"
    show player 13
    show teacher 12
    bis "Très Bien, mon bel homme!"
    return

label bissette_dialogue_tutoring:
    show player 10
    player_name "I was wondering if you were still offering private tutoring?"
    show player 5
    show teacher 3
    bis "Oh, oui!"
    show teacher 1
    show player 14
    player_name "Awesome! When would you be availa-"
    show player 11
    show teacher 2
    bis "Impressionnant! You're the first student to inquire about the tutoring!"
    show teacher 1
    show player 12
    player_name "Really? That's weird..."
    show player 5
    show teacher 5
    bis "I was beginning to think nobody was interested in the special reward."
    show teacher 1
    show player 12
    player_name "Oh yeah, I forgot about the special reward..."
    show player 5
    show teacher 5
    bis "Quoi!? You are not desiring the reward either?!"
    show teacher 4
    show player 29 with dissolve
    player_name "Err... No, I mean... A-a special reward sounds wonderful, {b}Miss Bissette{/b}."
    show player 3
    show teacher 3
    bis "Ah superbe!"
    show teacher 2
    bis "Then we will meet after school for some one on one lessons, yes?"
    show teacher 1
    show player 10 with dissolve
    player_name "Ummm... Yeah, I think that will-"
    show player 11
    show teacher 2
    bis "Tres bien!"
    bis "Just be sure to bring your {b}French dictionary{/b} along."
    show teacher 1
    show player 24
    player_name "Ah, crap. About that... {b}Miss Bissette{/b}, I can't seem to find my {b}French Dictionary{/b}."
    show player 25
    player_name "It's not in my backpack, my house, or my locker..."
    show player 5
    show teacher 5
    bis "Oh non, this is not good!"
    bis "Perhaps you should {b}stop by the library{/b} and see if they have one?"
    show teacher 2
    bis "I would loan you mine, but I'm afraid I've recently spilt wine upon it."
    show teacher 1
    show player 14
    player_name "Oh yeah, I forgot about the library!"
    show player 13
    show teacher 2
    bis "Oui, I go there quite often myself."
    show teacher 12
    bis "I love the feel of a good book in my hands."
    bis "Cuddled up by the warm fire with some strong wine..."
    bis "C'est le paradis."
    show teacher 13
    show player 11
    player_name "..."
    show teacher 2
    bis "Oh, silly me, babbling on and on. Just let me know when you have the dictionary, yes?"
    show teacher 1
    show player 14
    player_name "Sure thing, {b}Miss Bissette{/b}."
    return

label bissette_dialogue_get_dictionary:
    show player 12
    player_name "Remind me what I need to get before we can study together?"
    show player 5
    show teacher 2
    bis "You will need a French to English dictionary."
    bis "{b}Check the library{/b}, yes?"
    show teacher 1
    show player 14
    player_name "Oh, that's right!"
    player_name "Thanks!"
    return

label bissette_dialogue_replace_missing_pages:
    show player 12
    player_name "What was I supposed to do again?"
    show player 5
    show teacher 2
    bis "Copy the pages you are missing from a classmates Dictionary."
    show teacher 1
    show player 14
    player_name "Oh, that's right!"
    show player 13
    show teacher 2
    bis "Check with {b}Judith{/b}. She is a very good with her French."
    show teacher 1
    show player 14
    player_name "And then {b}the computer lab has the copy machine{/b}..."
    player_name "Got it, thanks again!"
    return

label bissette_dialogue_chat:
    show player 29 at left
    show teacher 1 at right
    player_name "{b}Miss Bissette{/b}, I just wanted to say that I really appreciate the help with catching up on my school work!"
    show player 13 at left
    show teacher 3 at right
    bis "It's my pleasure! All I want is to make sure that you are motivated to perform..."
    show teacher 12 at right
    bis "...And I love rewarding hard working students!"
    show teacher 13 at right
    show player 10 at left
    player_name "I'll do my best. I really want to get into a good college..."
    show teacher 2 at right
    show player 13 at left
    bis "That's what I like to hear!"
    bis "I can review your {b}homework{/b} with you when you hand it in, if you want!"
    show teacher 1 at right
    show player 17 at left
    player_name "That sounds good, {b}Miss Bissette{/b}! Thank you!"
    return

label bissette_dialogue_leave:
    show player 14
    player_name "No. I just wanted to say hello."
    show teacher 2
    show player 13
    bis "Well, take a seat. Class will be starting soon!"
    show teacher 3
    bis "I've got an exciting lesson planned for today!"
    show teacher 1
    show player 2
    player_name "Sounds good, {b}Miss Bissette{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
