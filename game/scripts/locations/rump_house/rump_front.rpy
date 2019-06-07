label mayor_rumps_frontyard_dialogue:
    $ game.main()

label mayor_rumps_house_locked:
    scene expression player.location.background_closeup with None
    show player f_worried
    show rump_guard 1 at right
    with dissolve
    guard "..."
    show player f_worried_talk
    player_name "Umm, hi?"
    show player f_worried
    show rump_guard 2
    guard "What do you want, kid?"
    show rump_guard 1
    show player f_worried_talk
    player_name "This is {b}Mayor Rump's{/b} house, right?"
    show player f_worried
    show rump_guard 2
    guard "That's correct."
    guard "Do you have an appointment?"
    show rump_guard 1
    show player f_worried_talk
    player_name "N-no..."
    show player f_worried
    show rump_guard 2
    guard "Then move it along, please. This is no place for loitering."
    show rump_guard 1
    show player f_worried_talk
    player_name "Can't I just-"
    show player f_worried
    show rump_guard 2
    guard "Move along!"
    show rump_guard 1
    show player f_surprised_teeth
    player_name "!!!"
    hide rump_guard
    show player 4 at center
    with dissolve
    player_name "( How in the heck am I supposed to {b}get an appointment{/b} with the {b}Mayor{/b}? )"
    show popup_unfinished at truecenter
    pause
    $ player.go_to(L_map)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
