label kim_button_dialogue:
    scene expression L_dealership.background_blur
    call expression game.dialog_select("kim_button_dialogue_intro")
    menu kim_button_menu:
        "Это вы написали на вывеске?":
            call expression game.dialog_select("kim_button_dialogue_sign")
        "Хорошая кнопка.":
            call expression game.dialog_select("kim_button_dialogue_button")
        "Я просто смотрю.":
            call expression game.dialog_select("kim_button_dialogue_browsing")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
