label tatiana_dialogue:
    call expression game.dialog_select("tatiana_dialogue_pre")
    menu tatiana_options:
        "You seem familiar.":
            call expression game.dialog_select("tatiana_dialogue_familiar")
            jump expression game.dialog_select("tatiana_options")
        "Any suggestions?":

            call expression game.dialog_select("tatiana_dialogue_suggestions")
            jump expression game.dialog_select("tatiana_options")
        "I found what I need.":

            call expression game.dialog_select("tatiana_dialogue_leave")

    hide tatia
    hide player
    hide xtra
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
