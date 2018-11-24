label harold_triggers_init:
    python:

        T_harold_donuts = Trigger("advance", "Give Harold with donuts")
        T_harold_leaves = Trigger("leaves", "Harold decided to leave")
        T_harold_missing = Trigger("missing", "Harold has gone missing")
        T_harold_photo_clue = Trigger("photo clue", "A photo of Harold and Helen suggesting where he is")
        T_harold_found = Trigger("found", "You found Harold")
        T_harold_glasses = Trigger("glasses", "You gave Harold his glasses")
        T_harold_grows_a_pair = Trigger("grows a pair", "Harold grows a pair and rushes to help Yumi")
        T_harold_backup = Trigger("backup", "Harold's backup helped save the day")
        T_harold_find_goods = Trigger("find goods", "Harold needs you to find the stolen goods for him")
        T_harold_found_goods = Trigger("found goods", "You found the stolen goods for Harold")
        T_harold_promotion = Trigger("pomotion", "Harold will now get a promotion for finding the goods")
        T_harold_indecisiveness = Trigger("indecisiveness", "Harold still hasn't decided to stay with or leave Helen")
        T_harold_new_girl = Trigger("new girl", "Harold found found himself a new girl to be with")
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
