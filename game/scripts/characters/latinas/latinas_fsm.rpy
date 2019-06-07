init python:
    T_latinas_showers = Trigger("showers")
    T_latinas_annie_trouble = Trigger("annie trouble")

label latinas_fsm_init:
    python:

        S_latinas_start = State("start")
        S_latinas_caught = State("caught")
        S_latinas_end = State("end")


        S_latinas_start.add(T_latinas_showers, S_latinas_caught)
        S_latinas_caught.add(T_latinas_annie_trouble, S_latinas_end)

        M_latinas.add(S_latinas_start, S_latinas_caught, S_latinas_end)
    return

label latinas_machine_init:
    python:
        M_latinas = Machine("latinas", default_loc=[[None, None, None, None]],
                         vars={'sex speed': .3},
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
