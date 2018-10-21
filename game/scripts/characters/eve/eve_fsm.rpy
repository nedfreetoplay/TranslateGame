label eve_triggers_init:
    python:

        T_eve_park_hangout = Trigger("park hangout", "Default")
    return

label eve_fsm_init:
    python:

        S_eve_start = State("start")
        S_eve_intro = State("intro", "Ева приветствует возвращение Гг")
        S_eve_end = State("end")


        S_eve_start.add(T_all_school_entrance, S_eve_intro)
        S_eve_intro.add(T_eve_park_hangout, S_eve_end)

        M_eve.add(S_eve_start, S_eve_intro, S_eve_end)
    return

label eve_machine_init:
    python:
        M_eve = Machine("Eve", default_loc = [[L_school_frenchclassroom, L_school_righthallway, L_park, L_park],
                                              [L_NULL, L_NULL, L_park, L_park]
                                              ],
                        vars = {"first park visit": True,
                                "first rap battle": True,
                                },
                        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
