init python:
    T_anna_intro = Trigger("intro")
    T_anna_find_awesomo = Trigger("find awesomo")
    T_anna_found_dog = Trigger("found dog")

label anna_fsm_init:
    python:
        S_anna_start = State("start")
        S_anna_dog_hunt = State("dog hunt")
        S_anna_find_dog = State("find dog")
        S_anna_end = State("end")

        S_anna_start.add(T_anna_intro, S_anna_dog_hunt,
                         actions = ["location", {"place": L_park},
                                    "force", {"tod": [0,1]},
                                    ],
                         )
        S_anna_dog_hunt.add(T_anna_find_awesomo, S_anna_find_dog,
                            actions = ["exec", L_forest.unlock]
                            )
        S_anna_find_dog.add(T_anna_found_dog, S_anna_end,
                            actions = ["unforce", None]
                            )

        M_anna.add(S_anna_start, S_anna_dog_hunt, S_anna_find_dog, S_anna_end)
    return

label anna_machine_init:
    python:
        M_anna = Machine("anna", default_loc = [[L_NULL, L_NULL, L_yoga_room, L_NULL]],
                         vars = {"sex speed": .3,
                                 "awesomo lured": False
                                 },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
