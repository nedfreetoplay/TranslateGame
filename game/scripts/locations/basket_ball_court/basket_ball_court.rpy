label basket_court_dialogue:
    $ player.go_to(L_basketball_court)

    if M_roxxy.get("dexter argument got information") and M_roxxy.is_state(S_roxxy_dexter_argument):
        call expression game.dialog_select("basketball_court_roxxy_dexter_argument")
        $ M_roxxy.trigger(T_roxxy_start_gymercise)

    elif M_roxxy.is_state(S_roxxy_dexter_alcohol_fight) and M_roxxy.get("alcohol talked to eve"):
        call expression game.dialog_select("basketball_court_roxxy_dexter_alcohol_fight")
        $ M_roxxy.trigger(T_roxxy_go_to_basketball)

    elif M_roxxy.is_state(S_roxxy_basketball_challenge) and game.timer.is_afternoon() and M_roxxy.get("done basketball"):
        call expression game.dialog_select("basketball_court_roxxy_basketball_challenge")
        jump basketball_minigame_prepare

    if M_bissette.between_states(S_bissette_jane_return_books, [S_bissette_got_eriks_martinez_books, S_bissette_got_martinez_eriks_books]) and not M_bissette.is_set("dexters book search") and player.location.is_here(M_dexter):
        call expression game.dialog_select("basketball_court_bissette_get_books")
        $ M_bissette.set("dexters book search", True)


    if M_dexter.is_state(S_dex_start) and player.location.is_here(M_dexter):
        call expression game.dialog_select("basketball_court_dexter_start")
        $ M_dexter.trigger(T_dex_territory)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
