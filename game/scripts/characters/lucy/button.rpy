label lucy_button_dialogue:
    scene expression player.location.background_blur with None
    if game.timer.is_day():
        call expression game.dialog_select("lucy_button_intro_day")
    else:
        call expression game.dialog_select("lucy_button_intro_night")
    menu button_lucy_menu:
        "Как поживаешь?":
            call expression game.dialog_select("button_lucy_how_are_you")
            jump button_lucy_menu
        "Это молоко подходит тебе?":
            call expression game.dialog_select("button_lucy_hows_the_milk")
            jump button_lucy_menu
        "Энни здесь?":
            if game.timer.is_day():
                call expression game.dialog_select("button_lucy_annie_around_day")
            else:
                call expression game.dialog_select("button_lucy_annie_around_night")
            jump button_lucy_menu

        "Как поживает мой малыш?" if PregnancyManager.total_babies() == 1:
            call expression game.dialog_select("button_lucy_baby_dialogue")
            jump button_lucy_menu

        "Как поживают мои малыши?" if PregnancyManager.total_babies() > 1:
            call expression game.dialog_select("button_lucy_baby_dialogue_multiple")
            jump button_lucy_menu

        "Как поживают малыши?" if PregnancyManager.total_babies() > 1:
            call expression game.dialog_select("button_lucy_how_are_the_little_ones")
            jump button_lucy_menu
        "Мне пора идти.":

            call expression game.dialog_select("button_lucy_leave")
            $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
