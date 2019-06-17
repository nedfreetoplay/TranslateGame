label nuke_dialogue_pre:
    if game.timer.is_day():
        scene expression "backgrounds/location_boat_interior_closeup01.jpg"
    else:
        scene expression "backgrounds/location_boat_interior_closeup01_night.jpg"
    show player f_worried_talk_low with dissolve
    player_name "Хм, Что за странная вещь рядом с кроватью..."
    player_name "Интересно, что эта кнопка делает?"
    show player f_worried_low a_dressed_thinking with dissolve
    return

label nuke_dialogue_push_it:
    show player f_laugh a_dressed_point with dissolve
    player_name "Как можно устоять перед желанием нажать большую красную кнопку?"
    if game.timer.is_day():
        scene expression "backgrounds/location_boat_cutscene01.jpg"
    else:
        scene expression "backgrounds/location_boat_cutscene01_night.jpg"
    with fade
    "Click"
    player_name "!!!" with hpunch
    player_name "Что это было?!"
    if game.timer.is_day():
        scene expression "backgrounds/location_boat_cutscene02.jpg"
    else:
        scene expression "backgrounds/location_boat_cutscene02_night.jpg"
    with fade
    player_name "..."
    player_name "Упс..."
    if game.timer.is_day():
        scene expression "backgrounds/location_boat_interior_closeup01.jpg"
    else:
        scene expression "backgrounds/location_boat_interior_closeup01_night.jpg"
    show player f_shock
    pause
    show player f_worried
    player_name "Эхх, мне, наверное, стоит убраться отсюда..."
    show player f_shock
    player_name "И лучше, прямо сейчас!"
    hide player with dissolve
    return

label nuke_dialogue_leave_it_be:
    show player f_worried_talk_low a_dressed_pocket with dissolve
    player_name "Наверное, мне не стоит нажимать большие красные кнопки без надписей..."
    player_name "Лучше просто оставить ее в покое."
    show player f_laugh
    player_name "Люпопытной Варваре нос в дверях оторвали."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
