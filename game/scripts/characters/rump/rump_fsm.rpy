label rump_machine_init:
    python:
        M_rump = Machine("rump", 
                         default_loc=[[L_rump_front, L_rump_front, L_rump_front, L_rump_front],
                                      [L_mall, L_mall, L_rump_front, L_rump_front]],
                         vars={'sex speed': .3,
                               'seen speech mall': False,
                               'rump_n_cunt': False,
                               'can see speech mall': True,
                               },
        )

        M_rump.add_action(T_all_sleep, ["assign", ["rump_n_cunt", "random.randint(1,8)==1 and not game.timer.is_weekend()"]])
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
