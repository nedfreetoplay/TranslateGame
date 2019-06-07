label beth_dialogue:
    call expression game.dialog_select("beth_dialogue_pre")
    menu:
        "I don't know." if not M_mia.is_set("buy donuts"):
            call expression game.dialog_select("beth_dialogue_do_not_know")

        "<>I want donuts! (50$)" if not player.has_money(50) and M_mia.is_set("buy donuts"):
            $ pass

        "I want donuts! (50$)" if player.has_money(50) and M_mia.is_set("buy donuts"):
            call expression game.dialog_select("beth_dialogue_want_donuts")
            call screen donut_minigame
        "No, thanks.":

            call expression game.dialog_select("beth_dialogue_leave")

    hide player
    hide xtra
    hide beth
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
