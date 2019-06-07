init python:
    T_smith_intro = Trigger("intro", "default")
    T_smith_go_to_locker = Trigger("go to locker")
    T_smith_unlocked_locker = Trigger("unlocked locker")
    T_smith_go_to_athletics = Trigger("go to athletics")
    T_smith_end = Trigger("end")

label smith_fsm_init:
    python:

        S_smith_start = State("start")
        S_smith_intro = State("intro")
        S_smith_go_to_locker = State("go to locker")
        S_smith_unlocked_locker = State("unlocked locker")
        S_smith_go_to_athletics = State("go to athletics")
        S_smith_end = State("end")


        S_smith_start.add(T_smith_intro, S_smith_intro,
                          actions = ["exec", L_basketball_court.unlock,
                                     "location", [M_annie, {"place": L_school_smithoffice}],
                                     "force", [M_annie, {"flag": True}],
                                     ],
                          )
        S_smith_intro.add(T_smith_go_to_locker, S_smith_go_to_locker)
        S_smith_go_to_locker.add(T_smith_unlocked_locker, S_smith_unlocked_locker,
                                 actions = ["unforce", M_annie,],
                                 )
        S_smith_unlocked_locker.add(T_smith_go_to_athletics, S_smith_go_to_athletics)
        S_smith_go_to_athletics.add(T_mc_lockerroom_change, S_smith_end,
                                    actions = ["set", "school intro done", "exec", game.unlock_sleep],
                                    )

        M_smith.add(S_smith_start, S_smith_intro, S_smith_go_to_locker,
                    S_smith_unlocked_locker, S_smith_go_to_athletics, 
                    S_smith_end)
    return

label smith_machine_init:
    python:
        M_smith = Machine("smith", default_loc = [[L_school_smithoffice, L_school_teacherslounge, L_school_smithoffice, L_NULL], 
                                                  [L_NULL, L_NULL, L_NULL, L_NULL]
                                                  ],
                          vars = {"sex speed": .3,
                                  "annie trouble": False,
                                  "school intro done": False,
                                  "left hall cult seen": False,
                                  },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
