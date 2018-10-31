label june_triggers_init:
    python:
        T_june_intro = Trigger("intro", "описание")
        T_june_mc_hang_out = Trigger("ask hang out", "описание")
        T_june_erik_hang_out = Trigger("erik hang out", "описание")
        T_june_completed_ork_bork = Trigger("completed ork bork", "описание")
    return

label june_fsm_init:
    python:

        S_june_start = State("start", "описание")
        S_june_hang_out_path_split = State("hang out path split", "описание")
        S_june_hang_out_mc = State("hang out mc", "описание")
        S_june_hang_out_erik = State("hang out erik", "описание")
        S_june_completed_minigame = State("completed minigame", "описание")


        S_june_start.add(T_erik_find_gf, S_june_hang_out_path_split)
        S_june_hang_out_path_split.add(T_june_mc_hang_out, S_june_hang_out_mc)
        S_june_hang_out_mc.add(T_june_completed_ork_bork, S_june_completed_minigame)
        S_june_hang_out_path_split.add(T_june_erik_hang_out, S_june_hang_out_erik)


        M_june.add(S_june_start, S_june_hang_out_path_split, S_june_hang_out_mc,
                    S_june_hang_out_erik, S_june_completed_minigame)
    return

label june_machine_init:
    python:
        M_june = Machine("june", default_loc = [[L_school_computerlab, L_school_computerlab, L_NULL, L_NULL],
                                                [L_NULL, L_NULL, L_NULL, L_NULL]
                                                ],
                         vars = {'sex speed': .3},
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
