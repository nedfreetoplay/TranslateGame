label eve_classroom_dialogue:
    scene classroom
    call expression game.dialog_select("eve_classroom_dialogue_intro")
    menu eve_dialogue_options:
        "Talent Show." if M_dewitt.is_state([S_dewitt_talent_show_ask, S_dewitt_talent_show_ask_eve]) or M_dewitt.is_set("talent helping kevin"):
            if M_dewitt.is_set("talent helping kevin"):
                call expression game.dialog_select("dewitt_talent_show_helping_kevin")
            else:

                call expression game.dialog_select("eve_classroom_dialogue_talent_show_help")
                $ M_dewitt.trigger(T_dewitt_eves_agreement)

        "Adhesive." if M_dewitt.is_state(S_dewitt_science_adhesive):
            call expression game.dialog_select("eve_classroom_dialogue_adehsive")
        "{b}Miss Bissette's{/b} reward.":

            call expression game.dialog_select("eve_classroom_dialogue_bissettes_reward")
            call expression game.dialog_select("eve_dialogue_options")
        "Hang out.":

            call expression game.dialog_select("eve_classroom_dialogue_hang_out")
            call expression game.dialog_select("eve_dialogue_options")
        "Nothing.":

            call expression game.dialog_select("eve_classroom_dialogue_leave")
    hide evedesk with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
