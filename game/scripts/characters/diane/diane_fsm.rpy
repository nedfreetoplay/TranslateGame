label diane_triggers_init:
    python:

        T_diane_need_shovel = Trigger()
        T_diane_has_shovel = Trigger()


        T_diane_get_delivery_task = Trigger()
        T_diane_make_delivery = Trigger()
        T_diane_place_delivery_goods = Trigger()
        T_diane_delivery_finished = Trigger()


        T_diane_wheelbarrow_strength_pass = Trigger()
        T_diane_wheelbarrow_strength_fail = Trigger()


        T_diane_help_carry_to_bed = Trigger()
        T_diane_find_cold_towel = Trigger()
        T_diane_found_cold_towel = Trigger()
        T_diane_nip_slip_n_dip = Trigger()


        T_diane_fix_infested_garden = Trigger()
        T_diane_cleaned_garden = Trigger()
        T_diane_clean_garden_reported = Trigger()
        T_diane_arrived_at_mall = Trigger()
        T_diane_entered_consumr = Trigger()
        T_diane_find_correct_bug_spray = Trigger()
        T_diane_use_bug_spray_on_garden = Trigger()
        T_diane_inform_diane = Trigger()


        T_diane_check_on_garden = Trigger()
        T_diane_search_kitchen = Trigger()
        T_diane_cucumber_aftermath = Trigger()
        T_diane_worked_on_garden = Trigger()


        T_diane_chat_at_home = Trigger()
        T_diane_find_pump = Trigger()
        T_diane_found_pump = Trigger()
        T_diane_brought_pump = Trigger()


        T_diane_get_delivery_2_task = Trigger()
        T_diane_found_delivery_2_goods = Trigger()
        T_diane_make_delivery_2 = Trigger()
        T_diane_delivery_2_finished = Trigger()


        T_diane_getting_sleep = Trigger()
        T_diane_debbie_request = Trigger()
        T_diane_house_locked = Trigger()
        T_diane_caught_milking = Trigger()


        T_diane_dump_pump = Trigger()
        T_diane_make_drink = Trigger()
        T_diane_drunk = Trigger()
        T_diane_made_drink = Trigger()
        T_diane_gave_drink = Trigger()
        T_diane_drunken_massage = Trigger()


        T_diane_apologizing = Trigger()


        T_diane_help_her = Trigger()
        T_diane_milking_malfunction_help = Trigger()


        T_diane_debbie_overhear_conversation = Trigger()


        T_diane_get_delivery_3_task = Trigger()
        T_diane_found_delivery_3_goods = Trigger()
        T_diane_make_delivery_3 = Trigger()
        T_diane_delivery_3_got_invoice = Trigger()
        T_diane_delivery_3_finished = Trigger()
        T_diane_delivery_3_report_back = Trigger()


        T_diane_dinner_task_acquired = Trigger()
        T_diane_debbie_check_outfit = Trigger()
        T_diane_debbie_ask_fish = Trigger()
        T_diane_debbie_gave_dinner_outfit_advice = Trigger()
        T_diane_got_dinner_fish = Trigger()
        T_diane_dinner_finished = Trigger()


        T_diane_found_carpenter = Trigger()
        T_diane_asked_annie_help = Trigger()
        T_diane_find_tools = Trigger()
        T_diane_helped_annie = Trigger()
        T_diane_carpenter_agreed = Trigger()
        T_diane_informed = Trigger()
        T_diane_moved_in = Trigger()


        T_diane_barn_built = Trigger()
        T_diane_checked_out_barn = Trigger()
        T_diane_research_milk_production = Trigger()
        T_diane_bought_milk_jug = Trigger()
        T_diane_find_production_book = Trigger()
        T_diane_asked_librarian = Trigger()
        T_diane_got_production_book = Trigger()
        T_diane_gave_production_book = Trigger()


        T_diane_gotta_jack_it = Trigger()
        T_diane_learns_your_secret = Trigger()
        T_diane_breeding_partner = Trigger()
        T_diane_go_to_hospital = Trigger()
        T_diane_bathroom_sampling = Trigger()
        T_diane_cup_o_jizz = Trigger()
        T_diane_get_fertility_pills = Trigger()
        T_diane_package_block = Trigger()


        T_diane_get_outfit_package = Trigger()
        T_diane_got_outfit_package = Trigger()
        T_diane_brought_outfit_package = Trigger()


        T_diane_breeding = Trigger()


        T_diane_debbie_caught = Trigger()
        T_diane_debbie_3way = Trigger()
        T_diane_3way_finished = Trigger()
    return

label diane_fsm_init:
    python:


        S_diane_start = State("start", "Debbie told me Diane needed some help in the garden.")
        S_diane_need_shovel = State("get shovel", "Diane needs a shovel, there's one in the garage.")


        S_diane_delivery_1_task = State("first delivery task", "Diane needs me at her house.", delay = 3)
        S_diane_delivery_1 = State("first delivery", "I need to head to the Pizzeria for mer delivery.")
        S_diane_delivery_1_place_goods = State("first delivery place goods", "Follow Maria to the back to place the delivery goods.")
        S_diane_delivery_1_done = State("first delivery done", "Maria is indeed quite sexy...")


        S_diane_wheelbarrow = State("wheelbarrow", "Diane needs me to lift a wheelbarrow.", delay = 3)
        S_diane_wheelbarrow_retry = State("wheelbarrow retry", "Take another shot at that wheelbarrow!", delay = 1)


        S_diane_drunken_splur = State("drunken splur", "I should check up Diane and her garden.", delay = 1)
        S_diane_get_cold_towel = State("get cold towel", "Find a cold towel for Diane.")
        S_diane_bring_cold_towel = State("bring cold towel", "Now to return to Diane.")
        S_diane_drunken_splur_aftermath = State("drunken splur aftermath", "I should let her rest")


        S_diane_bug_infested_garden = State("bug infested garden", "I should check up on Diane and her garden.")
        S_diane_clean_garden = State("clean garden", "I need to try to clean up that infestation!")
        S_diane_clean_garden_report = State("clean garden report", "I should tell Diane the job is done.")
        S_diane_go_to_mall = State("go to mall", "Diane and I are going to the mall.")
        S_diane_go_to_consumr = State("go to consumr", "I need to look in Consumr for bug spray.")
        S_diane_get_bug_spray = State("get bug spray", "I need to get bug spray for the garden.")
        S_diane_clear_bug_infested_garden = State("clear bug infested garden", "Use the spray to clear the garden.")
        S_diane_garden_restored = State("garden restored", "Tell diane the garden has been cleared.")


        S_diane_check_up_on_garden = State("check up on garden", "I should check up on Diane and her garden.", delay = 1)
        S_diane_look_in_kitchen = State("look in kitchen", "Diane isn't in her garden, maybe the kitchen ?")
        S_diane_seen_cucumber = State("seen cucumber", "Diane is certainly into some weird sex stuff")
        S_diane_work_on_garden = State("work on garden", "Should probably work on the garden now...")


        S_diane_get_augmentation = State("get augmentation", "I'm tired, I should get some sleep...")
        S_diane_pump_request = State("pump request", "Diane has a small task for me.")
        S_diane_fetch_pump = State("fetch pump", "The pump should be in the kitchen.")
        S_diane_return_pump = State("return pump", "I should bring the pump back to Diane.")


        S_diane_delivery_2_task = State("second delivery task", "Diane needs me at her house.", delay = 3)
        S_diane_delivery_2_fetch_goods = State("second delivery fetch goods", "Fetch the delivery from the shed.")
        S_diane_delivery_2 = State("second delivery", "I need to head to Annie's house for the delivery.")
        S_diane_delivery_2_done = State("second delivery done", "Diane seems to be struggling to meet her delivery demands.")
        S_diane_delivery_2_resting = State("second delivery resting", "Diane is exhausted and needs to rest some more.")


        S_diane_d9_intro = State("d9 intro", "Diane wants to talk to me in her garden", delay = 1)
        S_diane_debbie_drop_off_request = State("debbie drop off request", "Debbie has something to ask of me.")
        S_diane_debbie_drop_off = State("debbie drop off", "Debbie asked me to drop something off at Diane's.")
        S_diane_check_shed_light = State("check shed light", "The shed lights are still on.")


        S_diane_ready_for_day_off = State("ready for day off", "I should see what Diane is doing.", delay = 1)
        S_diane_dump_pump = State("dump pump", "I should dump the content of the pump in the shed into the storage jug.")
        S_diane_daylight_drinking = State("daylight drinking", "I should go see what Diane is doing.")
        S_diane_make_drink = State("make drink", "Head to the kitchen to make another drink for Diane.")
        S_diane_return_drink = State("return drink", "Return to Diane with the drink.")
        S_diane_drunken_garden_work = State("drunken garden work", "Do some gardening while diane drinks the day away.")


        S_diane_drunken_shenanigans_apology = State("drunken shenanigans apology", "I should check up on Diane to see if she is okay.", delay = 1)


        S_diane_gardening_help = State("gardening help", "Time to see if Diane needs anything again.", delay = 2)
        S_diane_milking_help = State("milking help", "Diane seemed in pain. Hurry to the shed.")


        S_diane_debbie_evening_visit = State("debbie evening visit", "I hear something from the kitchen in the evening.", delay = 1)


        S_diane_delivery_3_task = State("delivery 3 task", "Diane has another delivery for me to do.", delay = 1)
        S_diane_delivery_3_fetch_goods = State("delivery 3 fetch goods", "Get the delivery goods from the shed.")
        S_diane_delivery_3 = State("delivery 3", "Deliver the goods to the School Cafeteria.")
        S_diane_delivery_3_fetch_invoice = State("delivery 3 fetch invoice", "Annie requires a delivery invoice from Principal Smith.")
        S_diane_delivery_3_drop_off_goods = State("delivery 3 drop off goods", "Hand the goods over to Annie in the School Cafeteria.")
        S_diane_delivery_3_done = State("delivery 3 done", "Report to Diane about the delivery.")


        S_diane_debbie_dinner = State("debbie dinner", "Debbie needs mer help for dinner with Diane.", delay = 1)
        S_diane_meet_debbie_kitchen = State("meet debbie kitchen", "I should go see [deb_name] in the kitchen")
        S_diane_debbie_dinner_outfit = State("debbie dinner outfit", "Debbie wants mer advice on her dinner outfit.")
        S_diane_debbie_dinner_fish = State("debbie dinner fish", "I need to acquire a fish for the dinner with Diane.")
        S_diane_dinner = State("dinner", "Time for dinner with Diane and the gang.")


        S_diane_find_carpenter = State("find carpenter", "I need to look for a carpenter to help build the barn. Diane may know who to ask.", delay = 1)
        S_diane_ask_help_annie = State("ask help annie", "I need to help Annie's dad to build some tools before he can work on Diane's barn.")
        S_diane_help_annie = State("help annie", "In exchange for carpenting services, me need to help Annie.")
        S_diane_build_toys = State("build toys", "Time to build some toys!")
        S_diane_inform_carpenter = State("inform carpenter", "Inform the carpenter that mer end of the deal is completed.")
        S_diane_couch_crashing = State("couch crashing", "I hear some noises coming from the living room in the evening.")


        S_diane_barn_news = State("barn news", "Diane has news about the barn.", delay = 7)
        S_diane_check_barn_out = State("check barn out", "Let's check the progress on Diane's barn!")
        S_diane_get_milk_jug = State("get milk jug", "I need a milk jug from Consumr.")
        S_diane_buy_milk_jug = State("buy milk jug", "I need a milk jug from Consumr.")
        S_diane_increase_milk_production = State("increase milk production", "Diane needs mer help to find out how to increase milk production.")
        S_diane_production_ask_librarian = State("production ask librarian", "I should ask the librarian if the Library has a book on how to increase production.")
        S_diane_check_bookshelf = State("check bookshelf", "The librarian says the book is on the shelf.")
        S_diane_return_production_book = State("return production book", "Time to return the book to Diane.")


        S_diane_peeking = State("peeking", "NB! Debbie's story needs to be complete for this.", delay = 2)
        S_diane_peeking_masturbate = State("peeking masturbate", "Time to beat the meat!")
        S_diane_breeding_candidate = State("creeding candidate", "Diane has an idea that she wants to run by me.")
        S_diane_barn_checkup = State("barn checkup", "Diane told me to meet her at the Barn")
        S_diane_jizz_checkup = State("jizz checkup", "I should head to the hospital for a checkup.")
        S_diane_jizz_checkup_extra_hand = State("jizz checkup extra hand", "Need to head into the bathroom to get that sample.")
        S_diane_checkup_results = State("checkup results", "Head on back to Diane with the results.")


        S_diane_outfit_package = State("outfit package", "I should check up on Diane at the Barn", delay = 1)
        S_diane_get_outfit_package = State("get outfit package", "I need to collect the package for Diane from the Pink store.")
        S_diane_return_outfit_package = State("return outfit package", "Head on to Diane to hand over the package.")


        S_diane_milk_production_increase = State("milk production increase", "Diane wants to explain how to increase her milk production.")


        S_diane_risky_frisky_kinky = State("milk production increase", "Diane wants to explain how to increase her milk production.")
        S_diane_get_dirty_with_debbie = State("get dirty with debbie", "I can't believe I'm about to ride the tricycle!")
        S_diane_3way_aftermath = State("3 way aftermath", "Smells good! Debbie is probably cooking me breakfast in the kitchen")


        S_diane_end = State("end")




        S_diane_start.add(T_diane_need_shovel, S_diane_need_shovel)
        S_diane_need_shovel.add(T_diane_has_shovel, S_diane_delivery_1_task, actions=["exec", L_bank.unlock])


        S_diane_delivery_1_task.add(T_diane_get_delivery_task, S_diane_delivery_1)
        S_diane_delivery_1.add(T_diane_make_delivery, S_diane_delivery_1_place_goods)
        S_diane_delivery_1_place_goods.add(T_diane_place_delivery_goods, S_diane_delivery_1_done)
        S_diane_delivery_1_done.add(T_diane_delivery_finished, S_diane_wheelbarrow)


        S_diane_wheelbarrow.add(T_diane_wheelbarrow_strength_pass, S_diane_drunken_splur,
                                actions = ["exec", L_diane_kitchen.unlock,
                                           "exec", L_diane_home.unlock
                                           ]
                                )
        S_diane_wheelbarrow.add(T_diane_wheelbarrow_strength_fail, S_diane_wheelbarrow_retry)
        S_diane_wheelbarrow_retry.add(T_diane_wheelbarrow_strength_pass, S_diane_drunken_splur,
                                      actions = ["exec", L_diane_kitchen.unlock,
                                                 "exec", L_diane_home.unlock
                                                 ]
                                      )
        S_diane_wheelbarrow_retry.add(T_diane_wheelbarrow_strength_fail, S_diane_wheelbarrow_retry)


        S_diane_drunken_splur.add(T_diane_help_carry_to_bed, S_diane_get_cold_towel,
                                  actions = ["location", {"place": L_diane_bedroom},
                                             "force", {"tod": [0,1]},
                                             ]
                                  )
        S_diane_get_cold_towel.add(T_diane_found_cold_towel, S_diane_bring_cold_towel)
        S_diane_bring_cold_towel.add(T_diane_nip_slip_n_dip, S_diane_drunken_splur_aftermath)
        S_diane_drunken_splur_aftermath.add(T_all_sleep, S_diane_bug_infested_garden,
                                            actions = ["location", {"place": L_diane_shed},
                                                       "force", {"tod": [0,1]},
                                                       ]
                                            )


        S_diane_bug_infested_garden.add(T_diane_fix_infested_garden, S_diane_clean_garden)
        S_diane_clean_garden.add(T_diane_cleaned_garden, S_diane_clean_garden_report)
        S_diane_clean_garden_report.add(T_diane_clean_garden_reported, S_diane_go_to_mall)
        S_diane_go_to_mall.add(T_diane_arrived_at_mall, S_diane_go_to_consumr)
        S_diane_go_to_consumr.add(T_diane_entered_consumr, S_diane_get_bug_spray)
        S_diane_get_bug_spray.add(T_diane_find_correct_bug_spray, S_diane_clear_bug_infested_garden)
        S_diane_clear_bug_infested_garden.add(T_diane_use_bug_spray_on_garden, S_diane_garden_restored)
        S_diane_garden_restored.add(T_diane_inform_diane, S_diane_check_up_on_garden,
                                    actions = ["location", {"place": L_diane_kitchen},
                                               "force", {"tod": [0,1]},
                                               ]
                                    )


        S_diane_check_up_on_garden.add(T_diane_check_on_garden, S_diane_look_in_kitchen)
        S_diane_look_in_kitchen.add(T_diane_search_kitchen, S_diane_seen_cucumber,
                                    actions = ["action", [M_player, "set", "jerk diane"]
                                               ]
                                    )
        S_diane_seen_cucumber.add(T_diane_cucumber_aftermath, S_diane_work_on_garden)
        S_diane_work_on_garden.add(T_diane_worked_on_garden, S_diane_get_augmentation,
                                    actions = ["unforce", None]
                                    )


        S_diane_get_augmentation.add(T_diane_chat_at_home, S_diane_pump_request)
        S_diane_pump_request.add(T_diane_find_pump, S_diane_fetch_pump)
        S_diane_fetch_pump.add(T_diane_found_pump, S_diane_delivery_2_task,
                               actions = ["setdefaultloc", [[L_diane_shed, L_diane_shed, L_diane_shed, L_diane_bedroom]]]
                               )


        S_diane_delivery_2_task.add(T_diane_get_delivery_2_task, S_diane_delivery_2_fetch_goods, 
                                    actions = ["exec", L_annie_front.unlock, 
                                               "exec", L_diane_shed.unlock, 
                                               "location", {"place": L_diane_bedroom},
                                               "force", {"tod": [0,1]}
                                               ]
                                    )
        S_diane_delivery_2_fetch_goods.add(T_diane_found_delivery_2_goods, S_diane_delivery_2)
        S_diane_delivery_2.add(T_diane_make_delivery_2, S_diane_delivery_2_done,
                               actions = ["location", {"place": L_diane_bedroom},
                                          "force", {"tod": [0,1,2,3]},
                                          ]
                              )
        S_diane_delivery_2_done.add(T_diane_delivery_2_finished, S_diane_delivery_2_resting)
        S_diane_delivery_2_resting.add(T_all_sleep, S_diane_d9_intro,
                                       actions = ["unforce", None]
                                       )


        S_diane_d9_intro.add(T_diane_getting_sleep, S_diane_debbie_drop_off_request)
        S_diane_debbie_drop_off_request.add(T_diane_debbie_request, S_diane_debbie_drop_off)
        S_diane_debbie_drop_off.add(T_diane_house_locked, S_diane_check_shed_light)
        S_diane_check_shed_light.add(T_diane_caught_milking, S_diane_ready_for_day_off)


        S_diane_ready_for_day_off.add(T_diane_dump_pump, S_diane_dump_pump,
                                      actions = ["location", {"place": L_diane_garden},
                                                 "force", {"tod": [0,1]},
                                                  ]
                                      )
        S_diane_dump_pump.add(T_diane_make_drink, S_diane_daylight_drinking)
        S_diane_daylight_drinking.add(T_diane_drunk, S_diane_make_drink)
        S_diane_make_drink.add(T_diane_made_drink, S_diane_return_drink)
        S_diane_return_drink.add(T_diane_gave_drink, S_diane_drunken_garden_work)
        S_diane_drunken_garden_work.add(T_diane_drunken_massage, S_diane_drunken_shenanigans_apology,
                                 actions = ["unforce", None]
                                 )


        S_diane_drunken_shenanigans_apology.add(T_diane_apologizing, S_diane_gardening_help)


        S_diane_gardening_help.add(T_diane_help_her, S_diane_milking_help)
        S_diane_milking_help.add(T_diane_milking_malfunction_help, S_diane_debbie_evening_visit,
                                 actions = ["location", {"place": L_home_kitchen,
                                                         "condition": "not M_diane.is_set('first cucumber')",
                                                         },
                                            "force", {"tod": 2},
                                            ]
                                 )


        S_diane_debbie_evening_visit.add(T_diane_debbie_overhear_conversation, S_diane_delivery_3_task,
                                         actions = ["unforce", None]
                                         )


        S_diane_delivery_3_task.add(T_diane_get_delivery_3_task, S_diane_delivery_3_fetch_goods)
        S_diane_delivery_3_fetch_goods.add(T_diane_found_delivery_3_goods, S_diane_delivery_3)
        S_diane_delivery_3.add(T_diane_make_delivery_3, S_diane_delivery_3_fetch_invoice)
        S_diane_delivery_3_fetch_invoice.add(T_diane_delivery_3_got_invoice, S_diane_delivery_3_drop_off_goods)
        S_diane_delivery_3_drop_off_goods.add(T_diane_delivery_3_finished, S_diane_delivery_3_done)
        S_diane_delivery_3_done.add(T_diane_delivery_3_report_back, S_diane_debbie_dinner)


        S_diane_debbie_dinner.add(T_diane_dinner_task_acquired, S_diane_meet_debbie_kitchen,
                                  actions = ["location", [M_mom, {"place": L_home_kitchen}],
                                             "force", [M_mom, {"tod": [0,1]}],
                                             ]
                                  )
        S_diane_meet_debbie_kitchen.add(T_diane_debbie_check_outfit, S_diane_debbie_dinner_outfit,
                                        actions = ["location", [M_mom, {"place": L_home_mombedroom}],
                                                   "force", [M_mom, {"tod": [0,1]}],
                                                   ]
                                        )
        S_diane_meet_debbie_kitchen.add(T_diane_debbie_ask_fish, S_diane_debbie_dinner_fish,
                                        actions = ["exec", L_pier.unlock,
                                                   "unforce", M_mom,
                                                   ]
                                        )
        S_diane_debbie_dinner_outfit.add(T_diane_debbie_gave_dinner_outfit_advice, S_diane_debbie_dinner_fish,
                                         actions = ["exec", L_pier.unlock,
                                                    "unforce", M_mom,
                                                    ]
                                         )
        S_diane_debbie_dinner_fish.add(T_diane_got_dinner_fish, S_diane_dinner)
        S_diane_dinner.add(T_diane_dinner_finished, S_diane_find_carpenter)


        S_diane_find_carpenter.add(T_diane_found_carpenter, S_diane_ask_help_annie,
                                   actions = ["location", [M_richard, {"place": L_diane_yard}],
                                              "force", [M_richard, {"tod": [0,1]}],
                                              ]
                                   )
        S_diane_ask_help_annie.add(T_diane_asked_annie_help, S_diane_help_annie)
        S_diane_help_annie.add(T_diane_find_tools, S_diane_build_toys)
        S_diane_build_toys.add(T_diane_helped_annie, S_diane_inform_carpenter)
        S_diane_inform_carpenter.add(T_diane_carpenter_agreed, S_diane_couch_crashing,
                                     actions = ["unforce", M_richard])
        S_diane_couch_crashing.add(T_diane_moved_in, S_diane_barn_news,
                                   actions = ["setdefaultloc", [[L_diane_barn_building, L_diane_barn_building, L_home_livingroom, L_home_livingroom]]]
                                   )


        S_diane_barn_news.add(T_diane_barn_built, S_diane_check_barn_out,
                              actions = ["unforce", None,
                                         "setdefaultloc", [[L_diane_barn_interior, L_diane_barn_interior, L_home_livingroom, L_home_livingroom]]
                                         ]
                              )
        S_diane_check_barn_out.add(T_diane_checked_out_barn, S_diane_get_milk_jug)
        S_diane_get_milk_jug.add(T_diane_research_milk_production, S_diane_buy_milk_jug)
        S_diane_buy_milk_jug.add(T_diane_bought_milk_jug, S_diane_increase_milk_production)
        S_diane_increase_milk_production.add(T_diane_find_production_book, S_diane_check_bookshelf)
        S_diane_check_bookshelf.add(T_diane_got_production_book, S_diane_return_production_book)
        S_diane_return_production_book.add(T_diane_gave_production_book, S_diane_peeking)


        S_diane_peeking.add(T_diane_gotta_jack_it, S_diane_peeking_masturbate, actions=["exec", game.lock_sleep])
        S_diane_peeking_masturbate.add(T_diane_learns_your_secret, S_diane_breeding_candidate, actions=["exec", game.unlock_sleep])
        S_diane_breeding_candidate.add(T_diane_breeding_partner, S_diane_barn_checkup)
        S_diane_barn_checkup.add(T_diane_go_to_hospital, S_diane_jizz_checkup,
                                 actions = ["exec", L_hospital.unlock,
                                            "location", {"place": L_hospital_room},
                                            "force", {"tod": [0,1]},
                                            ]
                                 )
        S_diane_jizz_checkup.add(T_diane_bathroom_sampling, S_diane_jizz_checkup_extra_hand,
                                 actions = ["location", [M_micoe, {"place": L_NULL}],
                                            "force", [M_micoe, {"tod": [0,1]}],
                                            ]
                                 )
        S_diane_jizz_checkup_extra_hand.add(T_diane_cup_o_jizz, S_diane_checkup_results,
                                            actions = ["unforce", None,
                                                       "unforce", M_micoe,
                                                       ]
                                            )
        S_diane_checkup_results.add(T_diane_package_block, S_diane_outfit_package, actions=["setpriority", M_priya])


        S_diane_outfit_package.add(T_diane_get_outfit_package, S_diane_get_outfit_package)
        S_diane_get_outfit_package.add(T_diane_got_outfit_package, S_diane_return_outfit_package, 
                                       actions = ["location", [M_ivy, {"place": L_NULL}], 
                                                  "force", [M_ivy, {"tod": [0,1,2,3]}]
                                                  ]
                                       )
        S_diane_return_outfit_package.add(T_diane_brought_outfit_package, S_diane_milk_production_increase,
                                          actions = ["unforce", M_ivy]
                                          )


        S_diane_milk_production_increase.add(T_diane_breeding, S_diane_risky_frisky_kinky)


        S_diane_risky_frisky_kinky.add(T_diane_debbie_caught, S_diane_get_dirty_with_debbie,
                                       actions = ["setdefaultloc", [[L_diane_barn_interior, L_diane_barn_interior, L_home_mombedroom, L_home_livingroom]]]
                                       )
        S_diane_get_dirty_with_debbie.add(T_diane_debbie_3way, S_diane_3way_aftermath)
        S_diane_3way_aftermath.add(T_diane_3way_finished, S_diane_end,
                                   actions = ["exec", A_milky_business.unlock]
                                   )


        M_diane.add(S_diane_start, S_diane_need_shovel, S_diane_delivery_1_task,
                    S_diane_delivery_1, S_diane_delivery_1_place_goods, S_diane_delivery_1_done,
                    S_diane_wheelbarrow, S_diane_wheelbarrow_retry, S_diane_drunken_splur,
                    S_diane_get_cold_towel, S_diane_bring_cold_towel, S_diane_bug_infested_garden,
                    S_diane_clean_garden, S_diane_clean_garden_report, S_diane_go_to_mall,
                    S_diane_go_to_consumr, S_diane_get_bug_spray, S_diane_clear_bug_infested_garden,
                    S_diane_garden_restored, S_diane_check_up_on_garden, S_diane_look_in_kitchen,
                    S_diane_pump_request, S_diane_fetch_pump, S_diane_return_pump,
                    S_diane_delivery_2_task, S_diane_delivery_2_fetch_goods, S_diane_delivery_2,
                    S_diane_delivery_2_done, S_diane_delivery_2_resting, S_diane_debbie_drop_off_request,
                    S_diane_debbie_drop_off, S_diane_check_shed_light, S_diane_daylight_drinking,
                    S_diane_make_drink, S_diane_return_drink, S_diane_drunken_garden_work,
                    S_diane_drunken_shenanigans_apology, S_diane_milking_help, S_diane_gardening_help,
                    S_diane_debbie_evening_visit, S_diane_delivery_3_task, S_diane_delivery_3_fetch_goods,
                    S_diane_delivery_3, S_diane_delivery_3_fetch_invoice, S_diane_delivery_3_drop_off_goods,
                    S_diane_delivery_3_done, S_diane_debbie_dinner, S_diane_debbie_dinner_outfit,
                    S_diane_debbie_dinner_fish, S_diane_dinner, S_diane_find_carpenter,
                    S_diane_help_annie, S_diane_inform_carpenter, S_diane_get_milk_jug, S_diane_buy_milk_jug,
                    S_diane_peeking_masturbate,S_diane_couch_crashing, S_diane_barn_news,
                    S_diane_increase_milk_production, S_diane_production_ask_librarian, S_diane_check_bookshelf,
                    S_diane_return_production_book, S_diane_peeking, S_diane_breeding_candidate,
                    S_diane_jizz_checkup, S_diane_jizz_checkup_extra_hand, S_diane_checkup_results, S_diane_barn_checkup,
                    S_diane_check_barn_out, S_diane_outfit_package, S_diane_return_outfit_package,
                    S_diane_get_outfit_package, S_diane_milk_production_increase, S_diane_risky_frisky_kinky,
                    S_diane_end, S_diane_dump_pump, S_diane_meet_debbie_kitchen,
                    S_diane_seen_cucumber, S_diane_d9_intro, S_diane_ready_for_day_off, S_diane_drunken_splur_aftermath,
                    S_diane_get_augmentation, S_diane_work_on_garden, S_diane_ask_help_annie, S_diane_build_toys,
                    S_diane_get_dirty_with_debbie, S_diane_3way_aftermath,
                    )
    return

label diane_machine_init:
    python:
        M_diane = Machine("diane", default_loc = [[L_diane_garden, L_diane_garden, L_diane_bedroom, L_diane_bedroom]], character = dia,
                          vars = {"sex speed": .4,
                                  "previous outfit": "naked",
                                  "wearing cow outfit": False,
                                  "garden first time": True,
                                  "aunt drink made":False,
                                  "aunt_drink_made": False,
                                  "change angle": False,
                                  "acquired milk": False,
                                  "random drink": "Martini",
                                  "first boobjob": True,
                                  "first cucumber": True,
                                  "change partner": False,
                                  "cum inside": False,
                                  "breed first time": True,
                                  "3way first time":True,
                                  "refused 3way": False,
                                  "seen_shed_locked": False,
                                  "sex_pre_milking": False,
                                  },
        )
        M_diane.add_action(T_all_sleep, ["clear", "refused 3way", 
                                         "assign", ["random drink", "random.choice(['Martini', 'Pina Colada', 'Margarita'])"],
                                         ])
        M_diane.set_priority(1)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
