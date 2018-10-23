label player_triggers_init:
    python:

        T_mc_homework = Trigger("homework", "Завершите домашнее задание по французскому языку")
        T_mc_nun_thoughts = Trigger("nun thoughts", "Вы преодолеваете затруднительное положение, которое монахиня положила на вас")
        T_mc_mowed_lawn = Trigger("mowed lawn", "Ты подстриг свой газон")
        T_mc_lockerroom_change = Trigger("locker room changed", "Вы переоделись в свой Джерси в раздевалке")
        T_mc_beach_sex = Trigger("beach sex", "Вам просто повезло с четверкой на пляже.")
    return

label player_fsm_init:
    python:

        S_player_start = State("start")
        S_player_end = State("end")


        S_player_start.add(T_all_school_entrance, S_player_end)

        M_player.add(S_player_start, S_player_end)
        M_player.add_action(T_mc_beach_sex, ["inc", "mc beach sex",])
        M_player.add_action(T_all_sleep, ["clear", "masturbated tv",
                                          "set", "just wokeup",
                                          ]
                            )
    return

label player_machine_init:
    python:
        M_player = Machine("player", default_loc=[[L_NULL, L_NULL, L_NULL, L_NULL]],
                           vars = {"just wokeup": True,
                                   "sex speed": .4,
                                   "jerk mom": False,
                                   "jerk mia": False,
                                   "jerk roxxy": False,
                                   "telescope active": True,
                                   "telescope selection": None,
                                   "found cat": False,
                                   "pet cat": False,
                                   "first swim": True,
                                   "library subscription": False,
                                   "wearing swimsuit": False,
                                   "fixed computer": False,
                                   "library subscription": False,
                                   "drank milk": False,
                                   "masturbated tv": False,
                                   "mc beach sex": 0,
                                   "beach bottle spins": 0,
                                   "left of 4some": None,
                                  },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
