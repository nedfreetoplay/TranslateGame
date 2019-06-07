label nuke_dialogue_pre:
    if game.timer.is_day():
        scene expression "backgrounds/location_boat_interior_closeup01.jpg"
    else:
        scene expression "backgrounds/location_boat_interior_closeup01_night.jpg"
    show player f_worried_talk_low with dissolve
    player_name "Hmm, what a weird thing to have next to a bed..."
    player_name "I wonder what this button does?"
    show player f_worried_low a_dressed_thinking with dissolve
    return

label nuke_dialogue_push_it:
    show player f_laugh a_dressed_point with dissolve
    player_name "How could anyone resist pushing a big red button?"
    if game.timer.is_day():
        scene expression "backgrounds/location_boat_cutscene01.jpg"
    else:
        scene expression "backgrounds/location_boat_cutscene01_night.jpg"
    with fade
    "Click"
    player_name "!!!" with hpunch
    player_name "What the heck was that?!"
    if game.timer.is_day():
        scene expression "backgrounds/location_boat_cutscene02.jpg"
    else:
        scene expression "backgrounds/location_boat_cutscene02_night.jpg"
    with fade
    player_name "..."
    player_name "Oops..."
    if game.timer.is_day():
        scene expression "backgrounds/location_boat_interior_closeup01.jpg"
    else:
        scene expression "backgrounds/location_boat_interior_closeup01_night.jpg"
    show player f_shock
    pause
    show player f_worried
    player_name "Ehh, I should probably get out of here..."
    show player f_shock
    player_name "Like, right now!"
    hide player with dissolve
    return

label nuke_dialogue_leave_it_be:
    show player f_worried_talk_low a_dressed_pocket with dissolve
    player_name "Hmm, I probably shouldn't be pushing unmarked big red buttons..."
    player_name "Best to just leave it alone."
    show player f_laugh
    player_name "Curiousity killed the cat afterall."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
