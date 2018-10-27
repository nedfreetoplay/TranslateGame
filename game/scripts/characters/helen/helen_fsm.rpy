label helen_triggers_init:
    python:

        T_helen_confessional = Trigger("confessional", "Хелен вошла в исповедальню")
        T_helen_convince_fail = Trigger("convince fail", "Ты не смог убедить Хелен измениться")
        T_helen_convince_change = Trigger("convince change", "Ты убедил Хелен попытаться измениться")
        T_helen_secret_sacrement = Trigger("secret asacrement", "Попроси Хелен присоединиться к древнему таинству")
        T_helen_angelica_ritual = Trigger("convince change", "Хелен делает таинство с Анжеликой")
        T_helen_caught_masturbating = Trigger("caught masturbating", "Ты поймал Хелен за мастурбирбацией")
        T_helen_sexy_lingerie = Trigger("sexy lingerie", "Ты дал Хелен сексуальный комплект красного корсета нижнего белья")
        T_helen_torture = Trigger("torture", "Хелен подвергается пытками со стороны Анжелики, для её же блага")
        T_helen_thanks = Trigger("thanks", "Хелен благодарит тебя за заботу и предложение")
        T_helen_master_servant = Trigger("master servant", "Хелен хочет порку от своей хозяйки")
        T_helen_route = Trigger("route", "Это ставит тебя постоянный на маршрут Хелен")
        T_helen_master_servant_sex = Trigger("master servant sex", "Хелен хочет иметь больше секса с тобой, чтобы оставаться чистой")
    return

label helen_fsm_init:
    python:

        S_helen_start = State("start", "Состояние по умолчанию для Хелен в начале")
        S_helen_route_split = State("route split", "Раскол, чтобы определить, пойдешь ли ты с Мией или Хелен")
        S_helen_harold_moved_on = State("route split", "Гарольд отошёл от Хелен и нашёл новую женщину")
        S_helen_mia_breakdown = State("route split", "Мия опустошена тем, что её родители расстались навсегда")
        S_helen_master_servant_fun = State("master servant fun", "Хелен имеет некоторое удовольствие с тобой как и с ее хозяйкой")
        S_helen_aftersex_mia_suspicious = State("aftersex mia suspicious", "Мия подозревает, что ты посещаешь комнату её матери в течение дня")
        S_helen_end = State("end", "Конец истории с Хелен")


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
