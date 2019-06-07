init python:
    T_crystal_intro = Trigger("intro")

label crystal_fsm_init:
    python:
        S_crystal_start = State("start")
        S_crystal_end = State("end")

        S_crystal_start.add(T_crystal_intro, S_crystal_end)
        M_crystal.add(S_crystal_start, S_crystal_end)
    return

label crystal_machine_init:
    python:
        M_crystal = Machine("crystal", default_loc = [[L_trailer_interior, L_trailer_interior, L_trailer, L_NULL]],
                            vars = {"sex speed": .3,
                                    "crystal sex offer": False,
                                    "crystal sex offer denied": False,
                                    "crystal anal": False,
                                    },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
