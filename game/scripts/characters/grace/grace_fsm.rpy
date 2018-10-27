label grace_triggers_init:
    python:
        T_grace_intro = Trigger("intro", "Описание")
    return

label grace_fsm_init:
    python:

        S_grace_start = State("start")
        S_grace_end = State("end")


        S_grace_start.add(T_grace_intro, S_grace_end)


        M_grace.add(S_grace_start, S_grace_end)
    return

label grace_machine_init:
    python:
        M_grace = Machine("grace", default_loc=[[L_tattooparlor_interior, L_tattooparlor_interior, L_NULL, L_NULL]],
                         vars={'sex speed': .3},
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
