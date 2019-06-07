label kim_button_dialogue:
    scene expression player.location.background_closeup with None
    call expression game.dialog_select("kim_button_dialogue_intro")
    menu kim_button_menu:
        "Is that you on the sign?":
            call expression game.dialog_select("kim_button_dialogue_sign")
        "Nice button":
            call expression game.dialog_select("kim_button_dialogue_button")
        "I'm just browsing":
            call expression game.dialog_select("kim_button_dialogue_browsing")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
