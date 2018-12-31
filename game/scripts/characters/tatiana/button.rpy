label tatiana_dialogue:
    call expression game.dialog_select("tatiana_dialogue_pre")
    menu tatiana_options:
        "Вы кажетесь знакомой.":
            call expression game.dialog_select("tatiana_dialogue_familiar")
            jump expression game.dialog_select("tatiana_options")
        "Есть предложения?":

            call expression game.dialog_select("tatiana_dialogue_suggestions")
            jump expression game.dialog_select("tatiana_options")
        "Я нашел то, что мне нужно.":

            call expression game.dialog_select("tatiana_dialogue_leave")

    hide lilly
    hide player
    hide xtra
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
