label diane_pregnant_announcement_1:
    scene expression player.location.background_blur
    show player 9 with dissolve
    player_name "Hmm?"
    player_name "I've got a text from {b}Diane{/b}!"
    hide player with dissolve
    return

label diane_pregnant_announcement_2:
    if not player.location == L_map:
        scene expression player.location.background_blur
        show player 12 with dissolve
    player_name "I wonder what's going on?"
    player_name "{b}I should swing by {b}Diane's{/b} barn and see what's the matter{/b}."
    hide player with dissolve
    return

label diane_pregnant_labor_1:
    scene expression player.location.background_blur
    show player f_normal_talk with dissolve
    player_name "Looks like I got a text."
    hide player with dissolve
    return

label diane_pregnant_labor_2:
    scene expression player.location.background_blur
    show player 23 with dissolve
    player_name "The baby is coming!"
    player_name "Holy crap!"
    show player 22
    pause
    show player 23
    player_name "I'd better head to {b}the clinic{/b} to check on them!"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
