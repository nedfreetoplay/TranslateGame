label trailer_tractor_dialogue:
    $ player.go_to(L_trailer_tractor)
    if M_roxxy.is_state(S_roxxy_beat_clyde):
        call expression game.dialog_select("trailer_tractor_roxxy_beat_clyde")
        $ M_clyde.set("doggo_quest", True)
        jump expression game.dialog_select("shooting_minigame_prepare")

    elif M_roxxy.is_state(S_roxxy_confront_clyde):
        call expression game.dialog_select("trailer_tractor_roxxy_confront_clyde")
        $ M_roxxy.trigger(T_roxxy_confronted_clyde)
        $ player.go_to(L_map)

    elif game.clyde_big_berta and L_trailer_tractor.is_here(M_clyde):
        call expression game.dialog_select("trailer_tractor_big_berta")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
