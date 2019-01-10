label maze_pre:
    if game.cheat_mode:
        scene location_lair_ocean with None
        menu:
            "Пропутить мини-игру (Чит).":
                jump maze_pass
            "Играть в мини-игру.":

                $ pass
    call screen lair_maze

label maze_fail:
    $ M_aqua.trigger(T_aqua_chase_fail)
    $ game.timer.tick()
    $ player.go_to(L_pier)
    scene location_lair_fail_maze
    with fade
    show text "Я полностью был потерян, мне не хватало воздуха." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Мне ничего не оставалось делать, как отступить на поверхность." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Надеюсь, в следующий раз получится лучше..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    $ game.main()

label maze_pass:
    $ M_aqua.trigger(T_aqua_maze_conquered)
    scene location_lair_emerge
    with fade
    show text "Пещера представляла собой лабиринт из множества поворотов. " at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Я упорно двигался вперед, пока не почувствовал, что легкие вот-вот лопнут..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "...Но это не может быть концом! Этого же не может быть." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Погодите-ка, это что, свет!? " at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    jump lair_dialogue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
