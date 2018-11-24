label french_classroom_bissette_quiz:
    scene french_class_c
    show teacher 2 with dissolve
    bis "Take your seats, everyone. The test will begin shortly."
    scene black with fade
    pause 1
    bis "Alright, class."
    bis "Match the French word with the corresponding object on your test."
    bis "C'est plutôt facile, non?"
    bis "Let's begin!"
    call screen french_quiz

label french_classroom_bissette_quiz_fail:
    scene french_class_c
    show player 5 at left
    show teacher 5 at right
    with dissolve
    bis "Oh no. {b}[firstname]{/b}, I thought you were prepared for this?"
    show teacher 4
    show player 10
    player_name "You mean I didn't pass?"
    show player 5
    show teacher 5
    bis "I'm afraid not..."
    show teacher 4
    show player 37 with dissolve
    player_name "I'm so sorry, {b}Miss Bissette{/b}!"
    show player 5 with dissolve
    show teacher 5
    bis "You must come back tomorrow and retake it."
    show teacher 4
    show player 12
    player_name "Alright, I can do that!"
    show player 5
    show teacher 5
    bis "I suggest you study harder this time, yes?"
    show teacher 4
    show player 24
    player_name "Yes, Ma'am."
    hide teacher
    hide player
    with dissolve
    $ game.main()

label french_classroom_bissette_quiz_pass:
    scene french_class_cs10
    with fade
    show text "I breezed right through the test, making sure my paper was visible to {b}Roxxy{/b}.\nShe wasn't very subtle about copying me but {b}Miss Bissette{/b} didn't seem to notice.\nI was excited to be done with French and claim my special reward from {b}Miss Bissette{/b}." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    scene black with fade

    scene french_class_c
    show player 5 at left
    show teacher 3 at right
    with dissolve
    bis "Toutes mes félicitations, {b}[firstname]{/b}!"
    show teacher 1
    show player 38 with dissolve
    player_name "I passed?!"
    show player 13 with dissolve
    show teacher 2
    bis "You got a perfect score!"
    show teacher 1
    show player 14
    player_name "Awesome!"
    show player 13
    show teacher 2
    bis "I'd say you earned your A+."
    show teacher 1
    show player 14
    player_name "Thank you so much {b}Miss Bissette{/b}!"
    show player 13
    show teacher 12
    bis "My pleasure, {b}[firstname]{/b}!"
    show teacher 25 with dissolve
    bis "We should celebrate, yes?"
    show teacher 27 with dissolve
    show player 14
    player_name "Sure, what did you have in mind?"
    show player 13
    show teacher 26 with dissolve
    bis "Hmm, why don't you {b}join me in my office this evening{/b}?"
    show teacher 16 with dissolve
    bis "Perhaps we could sample that French wine I told you about?"
    show teacher 17
    show player 26
    player_name "O-okay. I've never had wine before."
    show player 13
    show teacher 26 with dissolve
    bis "Well then you are in for a real treat, jeune homme!"
    show teacher 27 with dissolve
    show player 14
    player_name "I'll see you tonight then."
    show player 13
    show teacher 12 with dissolve
    bis "Au revoir, {b}[firstname]{/b}."
    hide teacher
    hide player
    with dissolve
    $ M_bissette.trigger(T_bissette_quiz_pass)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
