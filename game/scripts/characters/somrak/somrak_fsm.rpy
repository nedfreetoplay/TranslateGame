init python:

    T_somrak_hungry = Trigger()
    T_somrak_fed = Trigger()
    T_somrak_trained = Trigger()

label somrak_fsm_init:
    python:

        S_somrak_start = State()
        S_somrak_waiting_a = State()
        S_somrak_sated_a = State()
        S_somrak_waiting_b = State()
        S_somrak_sated_b = State()
        S_somrak_waiting_c = State()
        S_somrak_sated_c = State()
        S_somrak_waiting_d = State()
        S_somrak_sated_d = State()



        S_somrak_start.add(T_somrak_hungry, S_somrak_waiting_a)

        S_somrak_waiting_a.add(T_somrak_fed, S_somrak_sated_a)

        S_somrak_sated_a.add(T_somrak_trained, S_somrak_sated_a,
             actions=('condition', ('player.stats.dex() >= 4',
                                    (('trigger', T_somrak_hungry)), ())))
        S_somrak_sated_a.add(T_somrak_hungry, S_somrak_waiting_b)

        S_somrak_waiting_b.add(T_somrak_fed, S_somrak_sated_b)

        S_somrak_sated_b.add(T_somrak_trained, S_somrak_sated_b,
             actions=('condition', ('player.stats.dex() >= 7',
                                    (('trigger', T_somrak_hungry)), ())))
        S_somrak_sated_b.add(T_somrak_hungry, S_somrak_waiting_c)

        S_somrak_waiting_c.add(T_somrak_fed, S_somrak_sated_c)

        S_somrak_sated_c.add(T_somrak_trained, S_somrak_sated_c,
             actions=('condition', ('player.stats.dex() >= 9',
                                    (('trigger', T_somrak_hungry)), ())))
        S_somrak_sated_c.add(T_somrak_hungry, S_somrak_waiting_d)

        S_somrak_waiting_d.add(T_somrak_fed, S_somrak_sated_d)

        S_somrak_sated_d.add(T_somrak_trained, S_somrak_waiting_d)

        M_somrak.add(S_somrak_start,
                     S_somrak_waiting_a, S_somrak_sated_a,
                     S_somrak_waiting_b, S_somrak_sated_b,
                     S_somrak_waiting_c, S_somrak_sated_c,
                     S_somrak_waiting_d, S_somrak_sated_d)
    return

label somrak_machine_init:
    python:
        M_somrak = Machine("somrak", default_loc=[[L_gym, L_gym, L_NULL, L_NULL]],
                           vars={"asked kevin panties": False,
                                 "delivered_panties": None,
                                 "just_delivered_panties": False,
                                 })
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
