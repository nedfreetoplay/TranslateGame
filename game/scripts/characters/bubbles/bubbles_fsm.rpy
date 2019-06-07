label bubbles_machine_init:
    python:
        M_bubbles = Machine("bubbles", default_loc=[[L_movie_theatre, L_movie_theatre, L_NULL, L_NULL]],
                         vars={'sex speed': .3,
                               'unavailable_movie_first': True},
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
