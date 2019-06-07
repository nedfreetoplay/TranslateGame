label jenny_pregnant_announcement_1:
    scene expression player.location.background_blur with None
    show player f_looking_down a_dressed_phone
    player_name "Hmm?"
    show player f_shock_down
    player_name "I've got a text from {b}[jen_name]{/b}!"
    hide player with dissolve
    return

label jenny_pregnant_announcement_2:
    if not player.location == L_map:
        scene expression player.location.background_blur
        show player f_worried_talk a_dressed_phone
        with fade
    player_name "I wonder what's going on?"
    player_name "{b}I should swing by {b}[jen_name]'s{/b} room and see what's the matter?{/b}."
    hide player with dissolve
    return

label jenny_pregnant_labor_1:
    scene expression player.location.background_blur
    show player f_normal_talk with dissolve
    player_name "Looks like I got a text."
    hide player with dissolve
    return

label jenny_pregnant_labor_2:
    scene expression player.location.background_blur
    show player f_shock
    with fade
    player_name "{b}[jen_name]{/b} had the baby?!"
    player_name "Holy crap!"
    pause
    show player f_worried_talk
    player_name "I'd better head to {b}the clinic{/b} to check on them."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
