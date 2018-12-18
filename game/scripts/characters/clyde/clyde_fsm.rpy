label clyde_machine_init:
    python:
        M_clyde = Machine("clyde",
                        default_loc=[[L_trailer_shack, L_trailer_tractor, L_trailer, L_trailer_shack_interior]],
                        vars={'sex speed': .3,
                              'cletus': False,
                              'doggo_quest':True},
                        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
