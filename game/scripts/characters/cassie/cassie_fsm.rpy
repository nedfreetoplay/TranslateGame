init python:
    T_cassie_ban_mc = Trigger("ban mc")
    T_cassie_lift_ban = Trigger("lift ban")
    T_cassie_drowning = Trigger("drowning")
    T_cassie_end = Trigger("end")

label cassie_fsm_init:
    python:

        S_cassie_start = State("start")
        S_cassie_ban_from_pool = State("ban from pool", "Вы должны пойти в бассейн ночью...")
        S_cassie_caught_skinny_dipping = State("caught skinny dipping", "Кэсси сняла свой запрет! Сходите поплавать!")
        S_cassie_medic_room = State("medic room", "Веселитесь в комнате медика...")
        S_cassie_end = State("end")


        S_cassie_start.add(T_cassie_ban_mc, S_cassie_ban_from_pool)
        S_cassie_ban_from_pool.add(T_cassie_lift_ban, S_cassie_caught_skinny_dipping)
        S_cassie_caught_skinny_dipping.add(T_cassie_drowning, S_cassie_medic_room)
        S_cassie_medic_room.add(T_cassie_end, S_cassie_end, actions=["exec", A_drowning_in_pussy.unlock])

        M_cassie.add(S_cassie_start, S_cassie_ban_from_pool, 
                     S_cassie_caught_skinny_dipping,
                     S_cassie_medic_room, S_cassie_end)
    return

label cassie_machine_init:
    python:
        M_cassie = Machine("cassie", default_loc=[[L_pool, L_pool, L_pool, L_NULL]],
                         vars={'sex speed': .3,
                               'had sex': False},
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
