label terry_triggers_init:
    python:

        T_terry_intro = Trigger("intro", "Meet Terry the fisher")
        T_terry_secret_lure = Trigger("secret lure", "Terry shows you his secret lure")
        T_terry_tigger = Trigger("tigger", "The one that got away with the little piggy")
        T_terry_lure_trade = Trigger("lure trade", "You traded for the golden lure")
        T_terry_retire = Trigger("retire", "You found out how to get Terry to retire")
        T_terry_overjoyed_swim = Trigger("overjoyed swim", "Terry has an overjoyed swim after seeing Tigger dead")
        T_terry_hang_tigger = Trigger("hang tigger", "Terry hangs Tigger as his prized joy")
    return

label terry_fsm_init:
    python:

        S_terry_start = State("start")
        S_terry_secret = State("secret", "The secret behind his fishing")
        S_terry_lure = State("lure", "The lure that made terry famous for his fishing")
        S_terry_nemesis = State("nemesis", "Sara tells you the cause of Terry's drunken state")
        S_terry_drunk = State("drunk", "Terry is out drunk for the day")
        S_terry_trade = State("trade")
        S_terry_bored = State("bored")
        S_terry_retire = State("retire")
        S_terry_tigger_sign = State("tigger sign")
        S_terry_end = State("end")


        S_terry_start.add(T_terry_intro, S_terry_secret)
        S_terry_secret.add(T_terry_secret_lure, S_terry_lure)
        S_terry_lure.add(T_all_sleep, S_terry_nemesis)
        S_terry_nemesis.add(T_terry_tigger, S_terry_drunk,
                            actions = ["location", {"place": L_NULL},
                                       "force", {"flag": True},
                                       ],
                            )
        S_terry_drunk.add(T_all_sleep, S_terry_trade,
                          actions = ["unforce", None],
                          )
        S_terry_trade.add(T_terry_lure_trade, S_terry_bored)
        S_terry_bored.add(T_terry_retire, S_terry_retire)
        S_terry_retire.add(T_terry_overjoyed_swim, S_terry_tigger_sign)
        S_terry_tigger_sign.add(T_terry_hang_tigger, S_terry_end)

        M_terry.add(S_terry_start, S_terry_secret, S_terry_lure, S_terry_nemesis,
                    S_terry_drunk, S_terry_trade, S_terry_bored, S_terry_retire,
                    S_terry_tigger_sign, S_terry_end)
    return

label terry_machine_init:
    python:
        M_terry = Machine("terry", default_loc = [[L_pier, L_pier, L_pier, L_pier]],
                          vars = {"bait talk": False,},
        )
        M_terry.set_priority(1)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
