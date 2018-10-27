label sister_triggers_init:
    python:

        T_jenny_hallway = Trigger("hallway", "Встретиться с Дженни в коридоре")
        T_jenny_panty_raid = Trigger("panty raid", "Украсть трусики Дженни")
    return

label sister_fsm_init:
    python:

        S_jenny_start = State("start")
        S_jenny_bored = State("bored", "Ждать того, что что-то случится")
        S_jenny_bedroom1 = State("Bedroom1", "В ожидании рейда трусиков")


        S_jenny_start.add(T_jenny_hallway, S_jenny_bored)
        S_jenny_bored.add(T_jenny_panty_raid, S_jenny_bedroom1,
                        actions = ["clear", "дверь заперта",
                                   "assign", ["default location", "bedroom"],
                        ])


        M_jenny.add(S_jenny_start, S_jenny_bored, S_jenny_bedroom1)
    return

label jenny_machine_init:
    python:
        M_jenny = Machine("Jenny", default_loc = [[L_home_sisbedroom, L_home_sisbedroom, L_home_sisbedroom, L_home_sisbedroom]],
                          vars = {"door locked": True,
                                  "default location": "bedroom",
                                  "seen MCs penis": False,
                                  "sex speed": .175,
                                  },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
