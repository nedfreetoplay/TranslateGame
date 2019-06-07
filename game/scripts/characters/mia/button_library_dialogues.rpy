label mia_library_dialogue_bissette_find_poem_reference_book:
    show player 14 at left
    show mia 7 at right
    with dissolve
    player_name "Hey, {b}Mia{/b}! What are you up to?"
    show player 13
    show mia 10
    mia "Oh, hello, {b}[firstname]{/b}! I was just about to study for the upcoming chemistry test."
    show mia 7
    show player 12
    player_name "I thought your mom didn't allow you to do anything after school?"
    show player 13
    show mia 12
    mia "She usually doesn't but..."
    show mia 10
    mia "I told her that {b}Miss Okita{/b} might write me a college recommendation if I impressed her by doing well on our next test."
    show mia 7
    player_name "Will she really do that?"
    show mia 10
    mia "Probably not but it doesn't hurt to try, right?"
    mia "And I actually get to hang out with {b}Judith{/b} outside of my house too!"
    show mia 7
    show player 14
    player_name "Yeah, I suppose not."
    show player 13
    show mia 10
    mia "What are you doing here?"
    show mia 7
    show player 14
    player_name "{b}Miss Bissette{/b} gave me an assignment. I thought maybe I could get some inspiration here."
    show player 13
    show mia 10
    mia "Oh yeah? What's the assignment?"
    show mia 7
    show player 10
    player_name "Well, it's kinda embarrassing..."
    show player 5
    show mia 9
    mia "Hehe, really?! Well, you have to tell me now!"
    show mia 7
    show player 10
    player_name "*Sigh* I'm supposed to write a romantic poem in French."
    show player 5
    show mia 10
    mia "That's not embarrassing!"
    show mia 7
    show player 12
    player_name "No?"
    show player 5
    show mia 10
    mia "No! We all had to do that!"
    show mia 12
    mia "Well, everyone but {b}Roxxy{/b}... She never does the homework."
    show mia 7
    show player 14
    player_name "I didn't know. What was your poem about?"
    show player 13
    show mia 12
    mia "Oh, I..."
    show mia 56 with dissolve
    mia "...You know, this and that, hehe..."
    show mia 55
    show player 14
    player_name "Aha! See, it is embarrassing!"
    show player 13
    show mia 10 with dissolve
    mia "Yeah, I guess it is a little bit."
    show mia 7
    show player 10
    player_name "I don't even know how to begin writing this thing!"
    player_name "I should probably look around for a book on {b}French Romance{/b}..."
    show player 13
    show mia 10
    mia "You know, {b}Judith{/b} and I found a really informative one."
    show mia 7
    show player 10
    player_name "Oh really?"
    show player 13
    show mia 10
    mia "Yeah, it was pretty graphic though..."
    show mia 7
    show player 12
    player_name "Do you remember what it was called?"
    show player 13
    show mia 12
    mia "Hmm, no, not really."
    show mia 10
    mia "{b}Judith{/b} had it last. She was using it {b}in the back room{/b} there, I think."
    show mia 7
    show player 10
    player_name "Huh, you think she might have left it in there?"
    show player 13
    show mia 10
    mia "Maybe."
    show mia 7
    show player 14
    player_name "I guess I'll go take a look then. Thanks for the help, {b}Mia{/b}!"
    show player 13
    show mia 10
    mia "No problem! Good luck, {b}[firstname]{/b}!"
    show mia 7
    show player 14
    player_name "You too!"
    return

label mia_library_dialogue_bissette_mia_book_feedback:
    show mia 10 at right
    show player 13 at left
    with dissolve
    mia "Any luck finding it?"
    show mia 7
    show player 10
    player_name "Yeah, I found it..."
    show player 14
    player_name "You weren't kidding, it's really graphic!"
    show player 13
    show mia 56 with dissolve
    mia "...Yeah."
    show mia 55
    show player 10
    player_name "I wonder what {b}Judith{/b} was doing with it back there by herself."
    show player 5
    show mia 56
    mia "Heh, y-yeah, I dunno..."
    mia "...I should really get back to studying."
    show mia 55
    show player 14
    player_name "Oh, right! Sorry!"
    player_name "Thanks again, {b}Mia{/b}."
    show player 13
    show mia 56
    mia "No problem, {b}[firstname]{/b}."
    hide mia with dissolve
    show player 14
    player_name "Alright, I had better take this home to {b}my computer{/b} and get to writing on that poem for {b}Miss Bissette{/b}."
    return

label mia_library_dialogue_do_not_disturb:
    show player 10 with dissolve
    player_name "No, I should let her study in peace..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
