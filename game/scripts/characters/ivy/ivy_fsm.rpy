init python:
    T_ivy_intro = Trigger("intro", "default")

label ivy_fsm_init:
    python:

        S_ivy_start = State("start")
        S_ivy_end = State("end")


        S_ivy_start.add(T_ivy_intro, S_ivy_end)

        M_ivy.add(S_ivy_start, S_ivy_end)
    return

label ivy_machine_init:
    python:
        M_ivy = Machine("ivy", default_loc=[[L_pink, L_pink, L_pink, L_NULL]],
                         vars={'sex speed': .8,
                               'first visit': True,
                               },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
