init python:

    T_aqua_special_lure = Trigger("special lure", "Find the golden compass to trade for the special lure")
    T_aqua_obituary_records = Trigger("obituary records", "Get access to the obituary Records")
    T_aqua_tomb_engraving = Trigger("tomb engraving", "Discover an engraving on the boatsmith's tomb")
    T_aqua_bell_engraving = Trigger("bell engraving", "Discover an engraving on the chuech bell")
    T_aqua_altar_puzzle_solve = Trigger("altar puzzle solve", "You solved the painful puzzle at the altar")
    T_aqua_treasure_found = Trigger("treasure found", "You found the treasure after such hard work")
    T_aqua_treasure_unlocked = Trigger("treasure unlocked", "You have finally unlocked the treasure chest")
    T_aqua_lure_steal = Trigger("lure steal", "Aqua steals your new shiny golden fishing lure")
    T_aqua_dive = Trigger("dive", "You dive into the ocean after Aqua")
    T_aqua_chase_fail = Trigger("chase fail", "You failed to chase after Aqua")
    T_aqua_squid_defeated = Trigger("squid defeated", "You defeated the squid near the entrance")
    T_aqua_maze_conquered = Trigger("maze conquered", "You were able to get through the confusing maze")
    T_aqua_lair_found = Trigger("lair found", "You found Aqua's lair")
    T_aqua_friended = Trigger("friended", "You have befriended Aqua")
    T_aqua_mating_offer = Trigger("mating offer", "You have offered to mate with Aqua")
    T_aqua_test_pass = Trigger("test pass", "You have passed Aqua's mate test")
    T_aqua_mated = Trigger("mated", "You have mated with Aqua")
    T_aqua_seasucc = Trigger("seasucc", "You have met SeaSucc")
    T_aqua_seasucc_fuck = Trigger("seasucc fuck", "You have fucked SeaSucc")

label aqua_fsm_init:
    python:

        S_aqua_start = State("start")
        S_aqua_boatsmith_search = State("boatsmith search", "Search for the holder of the golden compass")
        S_aqua_graveyard_search = State("graveyard search", "Search the graveyard for clues")
        S_aqua_bell_search = State("bell search", "Search the church bell for clues")
        S_aqua_altar_search = State("altar search", "Search the forest altar for clues")
        S_aqua_treasure_search = State("treasure search", "Search the beach for the treasure")
        S_aqua_treasure_unlock = State("treasure unlock", "Now you need to unlock the treasure chest")
        S_aqua_trade = State("trade", "You eed to trade Terry for the golden lure")
        S_aqua_fishing = State("fishing", "You might meet someone while Fishing with the new lure")
        S_aqua_chase = State("chase", "You need to chase after Aqua to get back your lure")
        S_aqua_squid_gaurd = State("squid gaurd", "You need to fight off the squid gaurding the lair")
        S_aqua_maze = State("maze", "You need to traverse the maze to get into the lair")
        S_aqua_lair = State("lair", "You have discovered the secret lair of Aqua")
        S_aqua_found = State("found", "You found Aqua after she stole your lure")
        S_aqua_mating_proposal = State("mating proposal", "You need to try convince Aqua to take you as her mate")
        S_aqua_valor_test = State("valor test", "Aqua has given you a test of valor to become her mate")
        S_aqua_mate = State("mate", "You can now mate with Aqua")
        S_aqua_seasucc_intro = State("seasucc intro", "Aqua's pal and friend, SeaSucc")
        S_aqua_seasucc_mushroom = State("mate", "SeaSucc wants a mushroom before he becomes your friend")
        S_aqua_end = State("end", "The end of Aqua's story")


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
