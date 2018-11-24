label beachhouse_not_bought:
    scene expression player.location.background_blur
    show player 3 at left
    player_name "Man, I don't have the key..."
    show player 4 at left
    player_name "Hmm... There's a sale sign on the lawn..."
    show player 1 at left with dissolve
    player_name "I guess I could save up some of that money {b}Diane{/b} gives me..."
    with dissolve
    return

label beach_house_first_time:
    scene expression player.location.background_blur
    show player 14
    with dissolve
    player_name "Whoa, this is awesome!"
    player_name "There's so much space!"
    show player 1
    pause
    show player 14
    player_name "I can't believe it's really mine!"
    show player 1
    pause
    show player 14
    player_name "I guess, I should start looking into buying some {b}furnishings{/b}."
    player_name "... Really fix this place up nice!"
    return

label beachhouse_weekday_just_wokeup:
    scene expression L_beachhouse_bedroom.background_blur
    show player 7 with dissolve
    player_name "{b}*Yawn*{/b}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( I should get ready for school... )"
    hide player with dissolve
    return

label beachhouse_weekend_just_wokeup:
    scene expression L_beachhouse_bedroom.background_blur
    show player 7 with dissolve
    player_name "{b}*Yawn*{/b}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( What should I do this weekend... )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
