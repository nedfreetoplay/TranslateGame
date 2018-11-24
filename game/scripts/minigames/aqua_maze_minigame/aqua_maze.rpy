label maze_pre:
    if game.cheat_mode:
        scene location_lair_ocean with None
        menu:
            "Skip Mini-Game (Cheat)":
                jump maze_pass
            "Play Mini-Game":

                $ pass
    call screen lair_maze

label maze_fail:
    $ M_aqua.trigger(T_aqua_chase_fail)
    $ game.timer.tick()
    $ player.go_to(L_pier)
    scene location_lair_fail_maze
    with fade
    show text "I was completely lost and running out of air." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "There was no choice but to retreat back to the surface." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Hopefully I'll do better next time..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    $ game.main()

label maze_pass:
    $ M_aqua.trigger(T_aqua_maze_conquered)
    scene location_lair_emerge
    with fade
    show text "The cave was a labyrinth of twists and turns." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I pushed forward stubbornly until I felt my lungs about to burst..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "...This can't be the end! This can't be-" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Wait, is that, light!?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    jump lair_dialogue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
