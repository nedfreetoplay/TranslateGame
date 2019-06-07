init python:

    T_jane_library_pass = Trigger("library pass", "Default")

label jane_fsm_init:
    python:

        S_jane_start = State("start")
        S_jane_intro = State("intro", "Default")
        S_jane_end = State("end")


        S_jane_start.add(T_all_school_entrance, S_jane_intro)
        S_jane_intro.add(T_jane_library_pass, S_jane_end)

        M_jane.add(S_jane_start, S_jane_intro, S_jane_end)
    return

label jane_machine_init:
    python:
        M_jane = Machine("Jane", default_loc=[[L_library, L_library, L_NULL, L_NULL]],
                        vars={"first book returned": True})
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
