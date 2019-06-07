label bubbles_button_dialogue:
    call expression game.dialog_select("bubbles_button_intro")
    menu bubbles_menu_options:
        "See a movie.":
            call expression game.dialog_select("bubbles_movie_select_pre")
            call screen movie_options
        "Nevermind.":

            call expression game.dialog_select("bubbles_button_nevermind")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
