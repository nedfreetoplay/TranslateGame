label dexter_triggers_init:
    python:

        T_dex_territory = Trigger("territory", "Декстер утверждает, что это его территория")
        T_dex_challenge = Trigger("challenge", "Попробуйте бросить вызов Декстеру")
    return

label dexter_fsm_init:
    python:

        S_dex_start = State("start")
        S_dex_flirting = State("flirting", "Декстер занят флиртом на баскетбольном корте")
        S_dex_end = State("end")


        S_dex_start.add(T_dex_territory, S_dex_flirting)
        S_dex_flirting.add(T_dex_challenge, S_dex_end)

        M_dexter.add(S_dex_start, S_dex_flirting, S_dex_end)
    return

label dexter_machine_init:
    python:
        M_dexter = Machine("Dexter", default_loc = [[L_school_track, L_basketball_court, L_NULL, L_NULL], 
                                                    [L_NULL, L_basketball_court, L_NULL, L_NULL]
                                                    ]
                           )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
