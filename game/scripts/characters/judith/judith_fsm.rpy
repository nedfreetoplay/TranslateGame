label judith_triggers_init:
    python:
        T_judith_intro = Trigger("intro", "default")
        T_judith_changed = Trigger("changed")
        T_judith_latina_bashed = Trigger("latina bashed")
        T_judith_comfort_her = Trigger("comfort her")
        T_judith_end = Trigger("end")
    return

label judith_fsm_init:
    python:

        S_judith_start = State("start", "описание")
        S_judith_latina_bashing_delay = State("latina bashing delay", "описание")
        S_judith_latina_bashing = State("latina bashing")
        S_judith_in_girls_bathroom = State("in girls bathroom")
        S_judith_end = State("end", "default")


        S_judith_start.add(T_judith_changed, S_judith_latina_bashing_delay)
        S_judith_latina_bashing_delay.add(T_all_sleep, S_judith_latina_bashing)
        S_judith_latina_bashing.add(T_judith_latina_bashed, S_judith_in_girls_bathroom,
                                    actions = ["set", "in bathroom",
                                               "location", {"place": L_school_stall},
                                               "force", {"tod": [0,1]},
                                               "exec", L_school_girlsroom.unlock,
                                               ],
                                    )
        S_judith_in_girls_bathroom.add(T_judith_comfort_her, S_judith_end,
                                       actions = ["set", "can go in bathroom",
                                                  "unforce", None,
                                                  ]
                                       )


        M_judith.add(S_judith_start, S_judith_latina_bashing_delay, S_judith_latina_bashing,
                     S_judith_in_girls_bathroom, S_judith_end)
    return

label judith_machine_init:
    python:
        M_judith = Machine("Judith", default_loc = [[L_school_lefthallway, L_school_lefthallway, L_NULL, L_NULL],
                                                    [L_NULL, L_NULL, L_NULL, L_NULL]
                                                    ],
                           vars = {
                                   "sex speed": .3,
                                   "can go in bathroom": False,
                                   "in bathroom": False,
                                   "sex sequence locked": True,
                           },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
