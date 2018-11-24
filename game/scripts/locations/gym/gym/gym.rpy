label training_dialogue:
    $ player.go_to(L_gym)
    if M_jenny.is_state(S_jenny_busy):
        call expression game.dialog_select("gym_training_dialogue_first")
        $ training_count = 1
        $ training_tier = 1
        $ M_jenny.trigger(T_jenny_panty_raid)

    elif training_count == 1 and training_tier == 2 and M_jenny.is_state(S_jenny_somrak_more_panty):
        call expression game.dialog_select("gym_training_dialogue_second")
        $ training_count = 2
        $ M_jenny.trigger(T_jenny_somrak_training_halt)

    elif training_count == 2 and training_tier == 3 and M_jenny.is_state(S_jenny_somrak_more_panty_tier_2):
        call expression game.dialog_select("gym_training_dialogue_third")
        $ training_count = 3
        $ M_jenny.trigger(T_jenny_somrak_training_halt_tier_2)

    elif training_count == 3 and training_tier == 4 and M_jenny.is_state(S_jenny_somrak_more_panty_tier_3):
        call expression game.dialog_select("gym_training_dialogue_fourth")
        $ training_count = 4
        $ M_jenny.trigger(T_jenny_somrak_training_halt_tier_3)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
