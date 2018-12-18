label beth_dialogue:
    call expression game.dialog_select("beth_dialogue_pre")
    menu:
        "Я не знаю." if not M_mia.is_set("buy donuts"):
            call expression game.dialog_select("beth_dialogue_do_not_know")

        "<>Я хочу пончики! (50$)" if not player.has_money(50) and M_mia.is_set("buy donuts"):
            $ pass

        "Я хочу пончики! (50$)" if player.has_money(50) and M_mia.is_set("buy donuts"):
            call expression game.dialog_select("beth_dialogue_want_donuts")
            call screen donut_minigame
        "Нет, спасибо.":

            call expression game.dialog_select("beth_dialogue_leave")

    hide player
    hide xtra
    hide beth
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
