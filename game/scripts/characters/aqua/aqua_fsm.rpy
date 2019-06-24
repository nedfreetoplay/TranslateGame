init python:

    T_aqua_special_lure = Trigger("special lure", "Найдите Золотой компас, чтобы обменять его на специальную приманку")
    T_aqua_obituary_records = Trigger("obituary records", "Получить доступ к записям некролога")
    T_aqua_tomb_engraving = Trigger("tomb engraving", "Откройте для себя гравюру на могиле лодочного кузнеца")
    T_aqua_bell_engraving = Trigger("bell engraving", "Откройте гравюру на церковном колоколе")
    T_aqua_altar_puzzle_solve = Trigger("altar puzzle solve", "Вы решили болезненную головоломку у алтаря")
    T_aqua_treasure_found = Trigger("treasure found", "После такой тяжелой работы вы нашли сокровище")
    T_aqua_treasure_unlocked = Trigger("treasure unlocked", "Вы, наконец, открыли сундук с сокровищами")
    T_aqua_lure_steal = Trigger("lure steal", "Аква украла новую блестящую золотую приманку")
    T_aqua_dive = Trigger("dive", "Вы погружаетесь в океан после Аквы")
    T_aqua_chase_fail = Trigger("chase fail", "Ты не смог догнать Акву")
    T_aqua_squid_defeated = Trigger("squid defeated", "Вы победили кальмара возле входа")
    T_aqua_maze_conquered = Trigger("maze conquered", "Вы смогли пройти через запутанный лабиринт")
    T_aqua_lair_found = Trigger("lair found", "Ты нашёл логово Аквы")
    T_aqua_friended = Trigger("friended", "Ты подружился с Аквой")
    T_aqua_mating_offer = Trigger("mating offer", "Вы предложили спариться с Аквой")
    T_aqua_test_pass = Trigger("test pass", "Вы прошли тест на мужика Аквы")
    T_aqua_mated = Trigger("mated", "Вы спаривались с Аквой")
    T_aqua_seasucc = Trigger("seasucc", "Вы встретили Сосунка")
    T_aqua_seasucc_fuck = Trigger("seasucc fuck", "Вы трахались с Сосунком")

label aqua_fsm_init:
    python:

        S_aqua_start = State("start")
        S_aqua_boatsmith_search = State("boatsmith search", "Поиск владельца золотого компаса")
        S_aqua_graveyard_search = State("graveyard search", "Поиск улики на кладбище")
        S_aqua_bell_search = State("bell search", "Поиск церковного колокола для подсказки")
        S_aqua_altar_search = State("altar search", "Поиск лесного алтаря для подсказок")
        S_aqua_treasure_search = State("treasure search", "Поиск пляжа с сокровищами")
        S_aqua_treasure_unlock = State("treasure unlock", "Теперь вам нужно открыть сундук с сокровищами")
        S_aqua_trade = State("trade", "Вы должны торговать с Терри за золотую приманку")
        S_aqua_fishing = State("fishing", "Вы можете встретить кого-то во время рыбалки с новой приманкой")
        S_aqua_chase = State("chase", "Вам нужно гоняться за Аквой, чтобы вернуть свою приманку")
        S_aqua_squid_gaurd = State("squid gaurd", "Вам нужно бороться с кальмаром, охраняющим логово")
        S_aqua_maze = State("maze", "Вам нужно пройти лабиринт, чтобы попасть в логово")
        S_aqua_lair = State("lair", "Вы обнаружили секретное логово Аквы")
        S_aqua_found = State("found", "Ты нашел Акву после того, как она украла твою приманку")
        S_aqua_mating_proposal = State("mating proposal", "Вам нужно попробовать убедить Акву взять вас в качестве её партнера")
        S_aqua_valor_test = State("valor test", "Аква дала вам Испытание доблести, чтобы стать её партнером")
        S_aqua_mate = State("mate", "Теперь вы можете спариваться с Аквой")
        S_aqua_seasucc_intro = State("seasucc intro", "Приятель и друг Аквы, Сосунок")
        S_aqua_seasucc_mushroom = State("mate", "Сосунок хочет гриб, прежде чем он станет вашим другом")
        S_aqua_end = State("end", "Конец истории Аквы")


        S_aqua_start.add(T_aqua_special_lure, S_aqua_boatsmith_search)
        S_aqua_boatsmith_search.add(T_aqua_obituary_records, S_aqua_graveyard_search,
                                    actions = ["set", "tomb search"]
                                    )
        S_aqua_graveyard_search.add(T_aqua_tomb_engraving, S_aqua_bell_search,
                                    actions = ["set", "bell search"]
                                    )
        S_aqua_bell_search.add(T_aqua_bell_engraving, S_aqua_altar_search,
                               actions = ["set", "altar search"]
                               )
        S_aqua_altar_search.add(T_aqua_altar_puzzle_solve, S_aqua_treasure_search,
                                actions = ["set", "treasure search",
                                           "set", "altar pass"]
                                )
        S_aqua_treasure_search.add(T_aqua_treasure_found, S_aqua_treasure_unlock)
        S_aqua_treasure_unlock.add(T_aqua_treasure_unlocked, S_aqua_trade, 
                                   actions = ["set", "treasure pass"]
                                   )
        S_aqua_trade.add(T_terry_lure_trade, S_aqua_fishing)
        S_aqua_fishing.add(T_aqua_lure_steal, S_aqua_chase)
        S_aqua_chase.add(T_aqua_dive, S_aqua_squid_gaurd)
        S_aqua_squid_gaurd.add(T_aqua_squid_defeated, S_aqua_maze, 
                               actions = ["set", "squid pass"]
                               )
        S_aqua_squid_gaurd.add(T_aqua_chase_fail, S_aqua_chase)
        S_aqua_maze.add(T_aqua_maze_conquered, S_aqua_lair, 
                        actions = ["set", "maze pass"]
                        )
        S_aqua_maze.add(T_aqua_chase_fail, S_aqua_chase)
        S_aqua_lair.add(T_aqua_lair_found, S_aqua_found, actions = ["exec", L_lair.unlock])
        S_aqua_found.add(T_aqua_friended, S_aqua_mating_proposal)
        S_aqua_mating_proposal.add(T_aqua_mating_offer, S_aqua_valor_test)
        S_aqua_valor_test.add(T_aqua_test_pass, S_aqua_mate)
        S_aqua_mate.add(T_aqua_mated, S_aqua_seasucc_intro,
                        actions = ["set", "seasucc available"]
                        )
        S_aqua_seasucc_intro.add(T_aqua_seasucc, S_aqua_seasucc_mushroom)
        S_aqua_seasucc_mushroom.add(T_aqua_seasucc_fuck, S_aqua_end, actions=["exec", A_mermaid.unlock])

        M_aqua.add(S_aqua_start, S_aqua_boatsmith_search, S_aqua_graveyard_search,
                   S_aqua_bell_search, S_aqua_altar_search, S_aqua_treasure_search,
                   S_aqua_treasure_unlock, S_aqua_trade, S_aqua_fishing, S_aqua_chase,
                   S_aqua_squid_gaurd, S_aqua_maze, S_aqua_lair, S_aqua_found,
                   S_aqua_mating_proposal, S_aqua_valor_test, S_aqua_mate,
                   S_aqua_seasucc_intro, S_aqua_seasucc_mushroom, S_aqua_end)
    return

label aqua_machine_init:
    python:
        M_aqua = Machine("aqua", default_loc=[[L_lair, L_lair, L_lair, L_lair]],
                         vars = {"sex speed": .175,
                                 "tomb search": False,
                                 "bell search": False,
                                 "altar search": False,
                                 "altar pass": False,
                                 "treasure search": False,
                                 "treasure pass": False,
                                 "squid pass": False,
                                 "maze pass": False,
                                 "seasucc available": False,
                                },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
