label lucy_button_dialogue:
    scene expression player.location.background_blur with None
    if game.timer.is_day():
        call expression game.dialog_select("lucy_button_intro_day")
    else:
        call expression game.dialog_select("lucy_button_intro_night")
    menu button_lucy_menu:
        "How are you?":
            call expression game.dialog_select("button_lucy_how_are_you")
            jump button_lucy_menu
        "That milk working out for you?":
            call expression game.dialog_select("button_lucy_hows_the_milk")
            jump button_lucy_menu
        "Annie around?":
            if game.timer.is_day():
                call expression game.dialog_select("button_lucy_annie_around_day")
            else:
                call expression game.dialog_select("button_lucy_annie_around_night")
            jump button_lucy_menu

        "How's my rugrat doing?" if PregnancyManager.total_babies() == 1:
            call expression game.dialog_select("button_lucy_baby_dialogue")
            jump button_lucy_menu

        "How are my rugrats doing?" if PregnancyManager.total_babies() > 1:
            call expression game.dialog_select("button_lucy_baby_dialogue_multiple")
            jump button_lucy_menu

        "How are the little ones?" if PregnancyManager.total_babies() > 1:
            call expression game.dialog_select("button_lucy_how_are_the_little_ones")
            jump button_lucy_menu
        "I should go.":

            call expression game.dialog_select("button_lucy_leave")
            $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
