init python:
    T_priya_start = Trigger()
    T_priya_talked_to_roz = Trigger()
    T_priya_helped_roz_with_camera = Trigger()
    T_priya_start_testing = Trigger()

label priya_fsm_init:
    python:

        S_priya_start = State("start", "У Микое может быть, есть информация о том, как повысить рождаемость.")
        S_priya_talk_to_roz = State("talk to roz", "Я должен поговорить с Роз, чтобы получить доступ на третий этаж.")
        S_priya_roz_camera_check = State("roz camera check", "Роз сказала мне, что ей нужна камера, установленная в лифте.")
        S_priya_look_in_lab = State("look in lab", "Наконец-то! Возможно, я никогда не оправлюсь от этого, но теперь я могу шпионить.")
        S_priya_end = State("end", "Сюжетная линия Прии заканчивается здесь.")


        S_priya_start.add(T_priya_start, S_priya_talk_to_roz)
        S_priya_talk_to_roz.add(T_priya_talked_to_roz, S_priya_roz_camera_check,
                                actions = ["location", [M_roz, {"place": L_hospital_elevator}],
                                           "force", [M_roz, {"tod": [0,1,2,3]}]
                                           ]
                                )
        S_priya_roz_camera_check.add(T_priya_helped_roz_with_camera, S_priya_look_in_lab,
                                     actions = ["exec", L_hospital_floor3.unlock,
                                                "location", {"place": L_NULL},
                                                "force", {"tod": [0,1,2,3]},
                                                "unforce", M_roz
                                                ]
                                     )
        S_priya_look_in_lab.add(T_priya_start_testing, S_priya_end,
                                actions = ["unforce", None]
                                )

        M_priya.add(S_priya_start, S_priya_roz_camera_check, S_priya_look_in_lab, 
                    S_priya_talk_to_roz, S_priya_end)
    return

label priya_machine_init:
    python:
        M_priya = Machine("priya", default_loc=[[L_hospital_lab, L_hospital_lab, L_NULL, L_NULL]],
                         vars={'sex speed': .3,
                               },
        )
        M_priya.set_priority(0)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
