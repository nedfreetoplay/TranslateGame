label annie_button_home_intro:
    show player 10 at left
    show annie 6 at right
    with dissolve
    player_name "Hey, {b}Annie{/b}."
    show player 5
    show annie 5
    ann "{b}[firstname]{/b}?!"
    show annie 4
    ann "What are you doing in my house?"
    show annie 6
    show player 12
    player_name "That's a good question actually..."
    show player 5
    show annie 5
    ann "Don't you have homework you should be doing?!"
    show annie 6
    show player 10
    player_name "I err... Yeah, kinda..."
    show player 5
    pause
    show annie 5
    ann "Well, quit bothering me and go do it!"
    show annie 6
    return

label annie_button_home_menu_alright_sheesh:
    show player 10 at left
    show annie 6 at right
    player_name "Okay, okay!"
    player_name "You really need to get that stick removed."
    show player 5
    show annie 5
    ann "What are you talking about?"
    show annie 6
    show player 14
    player_name "You know, the one in your ass."
    show player 13
    show annie 8
    ann "Do you want detention?!"
    ann "I'll write you up, here and now!"
    show annie 1
    show player 12
    player_name "We aren't even at school, {b}Annie{/b}!"
    show player 5
    show annie 17 with dissolve
    ann "That's it, I'm getting my detention pad-"
    show annie 6 with dissolve
    show player 10
    player_name "Okay, stop!"
    player_name "I'm leaving, sheesh!"
    hide player
    hide annie
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
