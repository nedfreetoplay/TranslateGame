label movie_theatre_movie_select_after(movie="foxxy_roxxy"):
    if player.has_money(50):
        if movie == 'bitch_perfect':
            $ player.spend_money(50)
            $ game.timer.tick()
        call expression game.dialog_select("movie_theatre_watch_movie_{}".format(movie))
    else:
        call expression game.dialog_select("movie_theatre_watch_movie_no_money")
    if game.timer.is_dark():
        $ player.go_to(L_map)
    else:
        $ player.go_to(L_movie_theatre)
    $ game.main()

label movie_theatre_movie_select_after_dialogue:
    scene movie_lobby
    show bubbles f_normal_talk o_desk at flip
    show player f_normal at flip
    with dissolve
    bub "Good pick!"
    show bubbles a_tickets with dissolve
    bub "Here's your ticket."
    show bubbles f_normal a_sides with dissolve
    show player f_normal_talk
    player_name "Thanks."
    show player f_normal
    show bubbles f_worried_talk
    bub "Just don't make a mess on the seats."
    show bubbles f_normal_talk
    bub "I hate cleaning that stuff off!"
    show bubbles f_normal
    show player f_surprised_teeth
    player_name "..."
    show bubbles f_normal_talk
    bub "Enjoy!"
    return

label movie_theatre_watch_movie_foxxy_roxxy:
label movie_theatre_watch_movie_dirty_harold:
label movie_theatre_watch_movie_its_a_trap:
    scene movie_lobby
    if M_bubbles.get("unavailable_movie_first"):
        $ M_bubbles.set("unavailable_movie_first", False)
        show bubbles o_desk at flip
        show player f_normal_talk at flip
        with None
        player_name "What's this movie? I haven't even heard of it."
        show player f_normal
        show bubbles f_worried_talk
        bub "Oh, that one? That movie is actually sold out at the moment."
        show bubbles f_worried
        show player f_worried_talk
        player_name "When's the next available showing?"
        show player f_worried
        show bubbles f_normal_talk
        bub "Let me see..."
        show bubbles f_normal
        bub "...{w}...{w}..."
        show bubbles f_normal_talk
        bub "It appears it's sold out out all day today."
        show bubbles f_normal
        show player f_surprised
        player_name "!!!"
        show player f_skeptical_talk
        player_name "Really?"
        show player f_thinking a_dressed_thinking with dissolve
        player_name "( He didnt even look... )"
        show player f_skeptical_talk a_dressed_pocket with dissolve
        player_name "Alright, I guess I'll pick a different movie then."
        show player f_skeptical
    else:
        show bubbles o_desk at flip
        show player f_worried_talk at flip
        with None
        player_name "Is that movie still sold out?"
        show player f_worried
        show bubbles f_normal_talk
        bub "I'm afraid so."
        show bubbles f_normal
        show player f_skeptical_talk
        player_name "Alright, I guess I'll pick a different movie then."
        show player f_skeptical
    return

label movie_theatre_watch_movie_bitch_perfect:
    show player f_normal_talk
    player_name "How about... {b}Bitch Perfect{/b}."
    show player f_normal
    show bubbles f_worried_talk
    bub "Ehh, are you sure you wanna see that one?"
    show bubbles f_worried
    show player f_worried
    player_name "Hmm?"
    show bubbles f_normal_talk
    bub "Heh, nevermind..."
    show bubbles f_normal
    show player f_normal
    player_name "..."
    show bubbles f_normal_talk a_tickets with dissolve
    bub "Here you go, enjoy the movie!"
    show bubbles f_normal a_sides
    show player f_normal_talk a_dressed_ticket
    with dissolve
    player_name "Thanks."
    scene black with fade
    pause
    scene expression "backgrounds/location_mall_movie_cutscene03.jpg" with fade
    "... And remember to check out our snack bar."
    "We've got everything a moviegoer could want!"
    "Popcorn, nachos, hotdogs, candy... Even delicious Slurpees!"
    scene expression "backgrounds/location_mall_movie_cutscene02.jpg" with fade
    "Thank you for choosing {b}CineSaga Theater{/b}!"
    "Please remember to be courteous. The feature is on the BIG SCREEN."
    "Don't talk, don't text, don't ruin the movie!"
    scene expression "backgrounds/location_mall_movie_cutscene_bitch01.jpg" with fade
    pause
    scene expression "backgrounds/location_mall_movie_cutscene_bitch02.jpg" with fade
    pause
    scene expression "backgrounds/location_mall_movie_cutscene_bitch03.jpg" with fade
    pause
    scene black with fade
    return

label movie_theatre_watch_movie_no_money:
    show player f_worried_talk
    player_name "Hmm, I guess I don't have enough money..."
    show player f_worried
    show bubbles f_worried_talk
    bub "Oh, ehh..."
    bub "Sorry, I can't people in for free."
    show bubbles f_worried
    show player f_tired_talk
    player_name "Yeah, I understand."
    show player f_tired
    show bubbles f_normal_talk
    bub "Don't worry though."
    bub "We don't cycle our movies out that often..."
    show bubbles f_worried_talk
    bub "... Or ever, really, heh..."
    show bubbles f_normal
    show player f_worried
    player_name "..."
    show bubbles f_normal_talk
    bub "You can always come back and see it another time."
    show bubbles f_normal
    show player f_worried_talk
    player_name "Thanks, will do."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
