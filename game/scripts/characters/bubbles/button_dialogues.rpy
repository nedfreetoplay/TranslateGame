label bubbles_button_intro:
    scene movie_lobby with None
    show bubbles f_normal_talk o_desk at flip
    show player at flip
    with dissolve
    bub "Welcome to {b}CineSaga Theater{/b}, my name is {b}Bubbles{/b}."
    bub "How can I help you?"
    show bubbles f_normal
    return

label bubbles_movie_select_pre:
    show player f_normal_talk
    player_name "I'd like to see a movie."
    show player f_normal
    show bubbles f_normal_talk
    bub "Sure."
    bub "Tickets are {b}Fifty dollars{/b} and all you have to do is select the one you want to see..."
    show bubbles f_normal
    show player f_normal_talk
    player_name "Cool!"
    show player f_normal
    return

label bubbles_button_nevermind:
    show player f_normal_talk
    player_name "I'm just looking around, thanks."
    show player f_normal
    show bubbles f_normal_talk
    bub "Alright."
    bub "Just let me know if you wanna watch something."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
