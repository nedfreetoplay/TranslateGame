init python:

    T_missy_beach_sex = Trigger("beach sex", "MC just had sex with Missy on the beach.")

label missy_fsm_init:
    python:
        M_missy.add_action(T_missy_beach_sex, ["inc", "missy beach sex",])
    return

label missy_machine_init:
    python:
        M_missy = Machine("missy", default_loc = [[L_basketball_court, L_basketball_court, L_NULL, L_NULL]],
                          vars = {"sex speed": .3,
                                  "missy beach sex": 0,
                                  },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
