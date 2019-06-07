label kevin_machine_init:
    python:
        M_kevin = Machine("kevin", default_loc = [[L_school_cafeteria, L_school_cafeteria, L_NULL, L_NULL]],
                          vars = {"sex speed": .3,
                                  "asked_shift_cover": False},
        )
        M_kevin.outfit.set_default_outfit_schedule([["apron", "apron", "apron", "apron"]])

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
