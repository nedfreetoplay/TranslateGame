label richard_button_dialogue:
    scene expression M_richard.where.background_blur
    if game.timer.is_day():
        call expression game.dialog_select("button_richard_intro_day")
    else:
        call expression game.dialog_select("button_richard_intro_night")
    menu richard_button_menu:
        "You should take it easy on {b}Lucy{/b}." if game.timer.is_day():
            call expression game.dialog_select("button_richard_take_it_easy_lucy")
            jump richard_button_menu
        "How's the business going?":

            call expression game.dialog_select("button_richard_hows_the_business")
            jump richard_button_menu
        "Nothing.":

            if game.timer.is_day():
                call expression game.dialog_select("button_richard_nothing_day")
            else:
                call expression game.dialog_select("button_richard_nothing_night")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
