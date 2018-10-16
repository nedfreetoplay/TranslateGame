label sister_triggers_init:
    python:

        T_jenny_hallway = Trigger("hallway", "Meet Jenny in hallway")
        T_jenny_panty_raid = Trigger("panty raid", "Steal Jenny's panties")
    return

label sister_fsm_init:
    python:

        S_jenny_start = State("start")
        S_jenny_bored = State("bored", "Waiting for something to happen")
        S_jenny_bedroom1 = State("Bedroom1", "Waiting for panty raid")


        S_jenny_start.add(T_jenny_hallway, S_jenny_bored)
        S_jenny_bored.add(T_jenny_panty_raid, S_jenny_bedroom1,
                        actions = ["clear", "door locked",
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
