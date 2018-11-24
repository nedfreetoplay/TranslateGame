label helen_triggers_init:
    python:

        T_helen_confessional = Trigger("confessional", "Helen has entered the confessional")
        T_helen_convince_fail = Trigger("convince fail", "You failed to convince Helen to change")
        T_helen_convince_change = Trigger("convince change", "You convinced Helen to try to change")
        T_helen_secret_sacrement = Trigger("secret asacrement", "Ask Helen to join the ancient sacrement")
        T_helen_angelica_ritual = Trigger("convince change", "Helen does the sacrement with Angelica")
        T_helen_caught_masturbating = Trigger("caught masturbating", "You caught Helen masturbating")
        T_helen_sexy_lingerie = Trigger("sexy lingerie", "You gave Helen a sexy red corset lingerie set")
        T_helen_torture = Trigger("torture", "Helen gets tortured by Angelica for her own good")
        T_helen_thanks = Trigger("thanks", "Helen thanks you for your concern and offer")
        T_helen_master_servant = Trigger("master servant", "Helen wants a spanking from her master")
        T_helen_route = Trigger("route", "This sets you permanently onto Helen's route")
        T_helen_master_servant_sex = Trigger("master servant sex", "Helen wants to have more sex with you to stay pure")
    return

label helen_fsm_init:
    python:

        S_helen_start = State("start", "The default state for Helen to start in")
        S_helen_route_split = State("route split", "The split to determine if you go with Mia or Helen")
        S_helen_harold_moved_on = State("route split", "Harold has moved on from Helen and found a new woman")
        S_helen_mia_breakdown = State("route split", "Mia is devastated that her parents have split for good")
        S_helen_master_servant_fun = State("master servant fun", "Helen has some fun with you as her master")
        S_helen_aftersex_mia_suspicious = State("aftersex mia suspicious", "Mia is suspicious about you visiting her mom's room during the day")
        S_helen_end = State("end", "The end of Helen's route")


        S_helen_start.add(T_helen_route, S_helen_route_split)
        S_helen_route_split.add(T_harold_new_girl, S_helen_harold_moved_on)
        S_helen_route_split.add(T_helen_master_servant, S_helen_mia_breakdown)
        S_helen_harold_moved_on.add(T_helen_master_servant, S_helen_master_servant_fun)
        S_helen_mia_breakdown.add(T_harold_new_girl, S_helen_master_servant_fun)
        S_helen_master_servant_fun.add(T_helen_master_servant_sex, S_helen_aftersex_mia_suspicious)
        S_helen_aftersex_mia_suspicious.add(T_mia_stay_alone, S_helen_end, actions=["exec", A_repentance.unlock])

        M_helen.add(S_helen_start, S_helen_route_split, S_helen_mia_breakdown, S_helen_harold_moved_on, S_helen_master_servant_fun, S_helen_aftersex_mia_suspicious, S_helen_end)
    return

label helen_machine_init:
    python:
        M_helen = Machine("helen", default_loc = [[L_miahouse_entrance, L_miahouse_helensbedroom, L_miahouse_entrance, L_miahouse_helensbedroom],
                                                  [L_church, L_miahouse_helensbedroom, L_miahouse_helensbedroom, L_miahouse_helensbedroom],
                                                  ],
                          vars = {"helen route": False,
                                  "sex speed": .175,
                                  "corset lingerie": False,
                                  },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
