label erik_dialogue:
    call expression game.dialog_select("erik_dialogue_intro")
    menu:
        "Линзы." if M_okita.is_state(S_okita_get_bifocal_lenses):
            call expression game.dialog_select("erik_dialogue_okita_get_bifocal_lenses")
        "Ничего":

            call expression game.dialog_select("erik_dialogue_leave")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
