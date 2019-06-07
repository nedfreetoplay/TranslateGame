label bissette_dialogue_office_bissette_roxxy_exam_convince:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "What was I supposed to be doing again?"
    show player 5
    show teacher 5
    bis "As-tu oublié?"
    bis "You must convince {b}Roxxy{/b} to show up for the exam."
    bis "Otherwise the grade point average of the entire class will suffer."
    show teacher 4
    show player 14
    player_name "Oh, right!"
    player_name "Don't worry, {b}Miss Bissette{/b}! I'm on it!"
    return

label bissette_dialogue_office_bissette_roxxy_convinced:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "{b}Miss Bissette{/b}?"
    show player 13
    show teacher 5
    bis "Oui?"
    show teacher 4
    show player 14
    player_name "I convinced {b}Roxxy{/b} to show up for the test!"
    show player 13
    show teacher 2
    bis "Truly!?"
    show teacher 1
    show player 17
    player_name "Yup!"
    show teacher 25 zorder 1 with dissolve

    bis "Tu me sauves la vie!"
    show teacher 26 with dissolve
    bis "Whatever would I do without you?!"
    show teacher 27 with dissolve
    show player 29 with dissolve
    player_name "Heh, it's no big deal..."
    show player 13
    show teacher 16
    with dissolve
    bis "Now be sure to study the words we learned over your past assignments, yes?"
    show teacher 17
    show player 14
    player_name "I will! Don't worry!"
    show player 13
    show teacher 16
    bis "Très Bien! Next class we will have the test."
    show teacher 17
    show player 14
    player_name "Alright, {b}Miss Bissette{/b}!"
    return

label bissette_dialogue_office_intro:
    show teacher 3 at right
    show player 13 at left
    with dissolve
    bis "Bonjour, {b}[firstname]{/b}!"
    show teacher 1
    show player 14
    player_name "Hello, {b}Miss Bissette{/b}."
    show player 13
    show teacher 2
    bis "What can I help with?"
    show teacher 1
    return

label bissette_dialogue_office_bissette_wine_sampling:
    player_name "I'm excited to taste that wine, {b}Miss Bissette{/b}."
    show player 13
    show teacher 12
    bis "J'ai hâte également!"
    bis "You will be tasting many things tonight, yes?"
    show teacher 13
    show player 29 with dissolve
    player_name "*Gulp* Y-Yeah..."
    show player 14
    show teacher 3
    bis "Très Bien, I'll be seeing you in my office this evening then."
    show teacher 13
    show player 14 with dissolve
    player_name "See you there!"
    return

label bissette_dialogue_office_leave:
    show player 14
    player_name "I don't think I need anything right now."
    show player 13
    show teacher 2
    bis "Très Bien!"
    show teacher 1
    show player 36 with dissolve
    player_name "Bye!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
