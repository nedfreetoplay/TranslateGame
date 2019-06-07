label rump_mall_dialogue:
    call expression game.dialog_select("rump_mall_dialogue_pre")
    $ M_rump.set("seen speech mall", True)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
