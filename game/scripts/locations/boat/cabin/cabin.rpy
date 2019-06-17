label boat_cabin_dialogue:
    $ game.main()

label nuke_dialogue:
    hide screen boat_cabin
    call expression game.dialog_select("nuke_dialogue_pre")
    menu:
        "Нажать.":
            call expression game.dialog_select("nuke_dialogue_push_it")
            $ A_world_war_3.unlock()
            $ player.go_to(L_map)
        "Уйти.":
            call expression game.dialog_select("nuke_dialogue_leave_it_be")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
