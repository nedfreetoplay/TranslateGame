label smiths_basement_dialogue:
    $ player.go_to(L_smith_basement)
    if M_roxxy.is_state(S_roxxy_sneak_into_smith) and not player.location.is_visited and game.timer.is_dark():
        $ player.location.visited()
        call expression game.dialog_select("smith_basement_sneaking")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
