label harold_triggers_init:
    python:

        T_harold_donuts = Trigger("advance", "Дай Гарольду пончики")
        T_harold_leaves = Trigger("leaves", "Гарольд решил уйти")
        T_harold_missing = Trigger("missing", "Гарольд пропал без вести")
        T_harold_photo_clue = Trigger("photo clue", "Фото Гарольда и Елены, указывают, где он")
        T_harold_found = Trigger("found", "Ты нашел Гарольда")
        T_harold_glasses = Trigger("glasses", "Ты дал Гарольду его очки")
        T_harold_grows_a_pair = Trigger("grows a pair", "Гарольд набрался смелости и спешит на помощь Юми")
        T_harold_backup = Trigger("backup", "Подмога Гарольда, помогла спасти положение")
        T_harold_find_goods = Trigger("find goods", "Гарольд должен, найти украденные вещи")
        T_harold_found_goods = Trigger("found goods", "Ты нашел украденные вещи для Гарольда")
        T_harold_promotion = Trigger("pomotion", "Теперь Гарольд получит повышение за нахождение вещей")
        T_harold_indecisiveness = Trigger("indecisiveness", "Гарольд все еще не решил остаться или уйти от Елены")
        T_harold_new_girl = Trigger("new girl", "Гарольд нашел себе новую девушку, чтобы быть с")
    return

label harold_fsm_init:
    python:

        S_harold_start = State("start")
        S_harold_end = State("end")


        S_harold_start.add(T_harold_donuts, S_harold_end)

        M_harold.add(S_harold_start, S_harold_end)
    return

label harold_machine_init:
    python:
        M_harold = Machine("harold", default_loc = [[L_police_office, L_police_office, L_miahouse_entrance, L_miahouse_entrance],
                                                    [L_church, L_police_office, L_miahouse_entrance, L_miahouse_entrance]
                                                    ],
                           vars = {"sex speed": .3,
                                   "topping": renpy.random.choice(["chocolate chips", "sprinkles", "vanilla drizzle", "maple drizzle"]),
                                   "glaze": renpy.random.choice(["chocolate glazed", "strawberry glazed", "blueberry glazed", "vanilla glazed"]),
                                   },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
