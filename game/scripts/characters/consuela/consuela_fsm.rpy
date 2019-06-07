init python:
    T_consuela_intro = Trigger()

label consuela_fsm_init:
    python:

        S_consuela_start = State("start")
        S_consuela_met_consuela = State("met consuela")
        S_consuela_end = State("end")


        S_consuela_start.add(T_consuela_intro, S_consuela_met_consuela)
        S_consuela_met_consuela.add(T_all_sleep, S_consuela_end)

        M_consuela.add(S_consuela_start, S_consuela_met_consuela, S_consuela_end)
    return

label consuela_machine_init:
    python:
        M_consuela = Machine("consuela", default_loc=[[L_NULL, L_NULL, L_NULL, L_NULL],
                                                      [L_NULL, L_NULL, L_NULL, L_NULL],
                                                      [L_NULL, L_NULL, L_NULL, L_NULL],
                                                      [L_NULL, L_beachhouse_entrance, L_NULL, L_NULL],
                                                      [L_NULL, L_NULL, L_NULL, L_NULL],
                                                      [L_NULL, L_NULL, L_NULL, L_NULL],
                                                      [L_NULL, L_NULL, L_NULL, L_NULL]],
                         vars={'sex speed': .3},
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
