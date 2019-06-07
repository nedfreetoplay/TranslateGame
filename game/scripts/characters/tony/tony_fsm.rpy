init python:
    T_tony_intro = Trigger("intro", "default")

label tony_fsm_init:
    python:

        S_tony_start = State("start")
        S_tony_end = State("end")


        S_tony_start.add(T_tony_intro, S_tony_end)

        M_tony.add(S_tony_start, S_tony_end)
    return

label tony_machine_init:
    python:
        M_tony = Machine("tony", default_loc=[[None, None, None, None]],
                         vars={'sex speed': .3,
                               'deliver': False},
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
