label maria_triggers_init:
    python:
        T_maria_intro = Trigger()
    return

label maria_fsm_init:
    python:

        S_maria_start = State()
        S_maria_end = State()


        S_maria_start.add(T_maria_intro, S_maria_end)

        M_maria.add(S_maria_start, S_maria_end)
    return

label maria_machine_init:
    python:
        M_maria = Machine("maria", default_loc=[[L_pizzeria_interior, L_pizzeria_interior, L_NULL, L_NULL]],
                         vars={'sex speed': .3,
                               'overlay sauce': False,
                               },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
