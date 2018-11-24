label micoe_triggers_init:
    python:
        T_micoe_intro = Trigger()
    return

label micoe_fsm_init:
    python:

        S_micoe_start = State()
        S_micoe_end = State()


        S_micoe_start.add(T_micoe_intro, S_micoe_end)

        M_micoe.add(S_micoe_start, S_micoe_end)
    return

label micoe_machine_init:
    python:
        M_micoe = Machine("micoe", default_loc=[[L_hospital_room, L_hospital_room, L_NULL, L_NULL]],
                         vars={'sex speed': .3,
                               },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
