init python:

    T_bridget_workout = Trigger("workout", "Default")

label bridget_fsm_init:
    python:

        S_bridget_start = State("start")
        S_bridget_intro = State("intro", "MC informs Mrs. Bridget of his return")
        S_bridget_end = State("end")


        S_bridget_start.add(T_mc_lockerroom_change, S_bridget_intro,
                            actions = ["location", [M_judith, {"place": L_NULL}],
                                       "force", [M_judith, {"tod": [0,1]}],
                                       ],
                            )
        S_bridget_intro.add(T_bridget_workout, S_bridget_end,
                            actions = ["exec", L_gym_front.unlock,
                                       "exec", L_pool.unlock,
                                       "unforce", M_judith,
                                       ],
                            )

        M_bridget.add(S_bridget_start, S_bridget_intro, S_bridget_end)
    return

label bridget_machine_init:
    python:
        M_bridget = Machine("Bridget", default_loc = [[L_school_track, L_school_bridgetoffice, L_NULL, L_NULL],
                                                      [L_NULL, L_NULL, L_NULL, L_NULL]
                                                      ],
                            )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
