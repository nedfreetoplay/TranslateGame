label daisy_pregnant_announcement_1:
    scene expression player.location.background_blur
    show player 9 with dissolve
    player_name "Hmm?"
    player_name "I've got a text from {b}Diane{/b}!"
    hide player with dissolve
    return

label daisy_pregnant_announcement_2:
    if not player.location == L_map:
        scene expression player.location.background_blur with None
        show player 10 with dissolve
    player_name "I wonder what's going on?"
    player_name "{b}I should swing by {b}Diane's{/b} barn and see what's the matter?{/b}."
    hide player with dissolve
    return

label daisy_pregnant_labor_1:
    scene expression player.location.background_blur
    show player f_normal_talk with dissolve
    player_name "Looks like I got a text."
    hide player with dissolve
    return

label daisy_pregnant_labor_2:
    scene expression player.location.background_blur with None
    show player 14 with dissolve
    player_name "The baby is here!"
    show player 10
    player_name "Holy crap!"
    show player 5
    pause
    show player 14
    player_name "I'd better head to the {b}Barn{/b} to check on them."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
