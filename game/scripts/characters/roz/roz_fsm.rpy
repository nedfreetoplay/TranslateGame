init python:

        T_roz_favour = Trigger("favour", "Роз нуждается в одолжении в обмен на записи некролога")
        T_roz_fuckery = Trigger("fuckery", "Буквально небольшой секс с Роз")

label roz_fsm_init:
    python:

        S_roz_start = State("start")
        S_roz_sexy_time = State("sexy time", "Lets get funky with ol' Rozzy")
        S_roz_end = State("end", "The end of the end but not for Roz")


        S_roz_start.add(T_roz_favour, S_roz_sexy_time)
        S_roz_sexy_time.add(T_roz_fuckery, S_roz_end, actions=["exec", A_oldies_goodies.unlock])

        M_roz.add(S_roz_start, S_roz_sexy_time, S_roz_end)
    return

label roz_machine_init:
    python:
        M_roz = Machine("roz", default_loc = [[L_hospital, L_hospital, L_hospital, L_NULL]],
                        vars = {'fun time': False, 'sex speed': .4},
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
