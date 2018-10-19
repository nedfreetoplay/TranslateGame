label mom_triggers_init:
    python:

        T_mom_breakfast = Trigger("breakfast", "Описание")
        T_mom_check = Trigger("check", "Описание")
        T_mom_debt_help = Trigger("debt help", "Описание")
        T_mom_help_mow = Trigger("help mow", "Описание")
        T_mom_filled_mower = Trigger("filled mower", "Описание")
        T_mom_mowed_lawn = Trigger("mowed lawn", "Описание")
        T_mom_sis_bitch = Trigger("sis bitch", "Описание")
        T_mom_clean_clothes = Trigger("clean clothes", "Описание")
        T_mom_check_door = Trigger("check door", "Описание")
        T_mom_bad_guys = Trigger("bad guys", "Описание")
        T_mom_mrsj_condolences = Trigger("mrsj condolences", "Описание")
        T_mom_broken_pipe = Trigger("broken pipe", "Описание")
        T_mom_sis_order = Trigger("broken pipe", "Описание")
        T_mom_closed_valve = Trigger("broken pipe", "Описание")
        T_mom_get_wrench = Trigger("get wrench", "Описание")
        T_mom_fixed_broken_pipe = Trigger("fixed broken pipe", "Описание")
        T_mom_sis_nice_boobs = Trigger("sis nice boobs", "Описание")
        T_mom_shower_admire = Trigger("shower admire", "Описание")
        T_mom_bad_guys_watching = Trigger("bad guys watching", "Описание")
        T_mom_vacuumed = Trigger("vacuumed", "Описание")
        T_mom_washed_dishes = Trigger("washed dishes", "Описание")
        T_mom_cleaned_laundry = Trigger("cleaned laundry", "Описание")
        T_mom_lotion_applied = Trigger("lotion applied", "Описание")
        T_mom_steal_panties = Trigger("steal panties", "Описание")
        T_mom_caught_masturbating = Trigger("caught masturbating", "Описание")
        T_mom_movie_invite = Trigger("movie invite", "Описание")
        T_mom_watch_movie = Trigger("watch movie", "Описание")
        T_mom_movie_night_finish = Trigger("watch movie", "Описание")
        T_mom_hang_out_accept = Trigger("hang out accept", "Описание")
        T_mom_hang_out_refuse = Trigger("hang out refuse", "Описание")
        T_mom_mall_arrival = Trigger("mall arrival", "Описание")
        T_mom_cupid_arrival = Trigger("cupid arrival", "Описание")
        T_mom_pick_necklace = Trigger("pick necklace", "Описание")
        T_mom_give_necklace = Trigger("give necklace", "Описание")
        T_mom_dressing_room_check = Trigger("dressing room check", "Описание")
        T_mom_dream = Trigger("dream", "Описание")
        T_mom_caught_spying = Trigger("caugh spying", "Описание")
        T_mom_kiss = Trigger("kiss", "Описание")
        T_mom_shower_ = Trigger("peek", "Описание")
        T_mom_car_help = Trigger("car help", "Описание")
        T_mom_check_engine = Trigger("check engine", "Описание")
        T_mom_deliver_car_news = Trigger("deliver car news", "Описание")
        T_mom_renew_insurance = Trigger("renew insurance", "Описание")
        T_mom_car_fun = Trigger("car fun", "Описание")
        T_mom_midnight_fun = Trigger("midnight fun", "Описание")
        T_mom_bad_guys_beatup = Trigger("bad guys beatup", "Описание")
        T_mom_sleepover_accept = Trigger("sleepover accept", "Описание")
        T_mom_sleepover_morning = Trigger("sleepover morning", "Описание")
        T_mom_diane_chat = Trigger("diane chat", "Описание")
        T_mom_dinner_help = Trigger("dinner help", "Описание")
        T_mom_dinner_outfit_check = Trigger("dinner outfit check", "Описание")
        T_mom_dinner_fish_caught = Trigger("dinner fish caught", "Описание")
        T_mom_diane_dinner_chat = Trigger("diane dinner chat", "Описание")
        T_mom_midnight_wakeup = Trigger("midnight wakeup", "Описание")
        T_mom_midnight_swim = Trigger("midnight swim", "Описание")
        T_mom_gave_towel = Trigger("gave towel", "Описание")
        T_mom_delay = Trigger("delay", "Описание")
        T_mom_read_note = Trigger("read note", "Описание")
        T_mom_got_laundry = Trigger("got laundry", "Описание")
        T_mom_basement_fun = Trigger("basement fun", "Описание")
    return

label mom_fsm_init:
    python:

        S_mom_start = State("start")
        S_mom_relaxing = State("relaxing", "Описание")
        S_mom_overheard = State("overheard", "Описание")
        S_mom_debt_call = State("debt call", "Описание")
        S_mom_lawn_delay = State("lawn delay", "Описание")
        S_mom_lawn_help = State("lawn help", "Описание")
        S_mom_fill_mower = State("fill mower", "Описание")
        S_mom_mow_lawn = State("mow lawn", "Описание")
        S_mom_clothes_dirty = State("clothes dirty", "Описание")
        S_mom_wash_clothes = State("wash clothes", "Описание")
        S_mom_sleeping = State("sleeping", "Описание")
        S_mom_doorbell = State("doorbell", "Описание")
        S_mom_debt_collectors = State("debt collectors", "Описание")
        S_mom_mrsj_visit_delay = State("mrsj visit delay", "Описание")
        S_mom_mrsj_visit = State("mrsj visit", "Описание")
        S_mom_pipe_delay = State("pipe delay", "Описание")
        S_mom_pipe_help = State("pipe help", "Описание")
        S_mom_sis_check = State("sis check", "Описание")
        S_mom_close_valve = State("close valve", "Описание")
        S_mom_pipe_check = State("pipe check", "Описание")
        S_mom_fix_pipe = State("fix pipe", "Описание")
        S_mom_sis_boobs_afterthoughts = State("sis boobs afterthoughts", "Описание")
        S_mom_shower_delay = State("shower delay", "Описание")
        S_mom_shower_peek = State("shower peek", "Описание")
        S_mom_shower_peek_after = State("shower peek after", "Описание")
        S_mom_bad_guys_driveby = State("bad guys driveby", "Описание")
        S_mom_chores_delay = State("chores delay", "Описание")
        S_mom_vacuum_help = State("vacuum help", "Описание")
        S_mom_dishes_help = State("dishes help", "Описание")
        S_mom_laundry_help = State("laundry help", "Описание")
        S_mom_lotion_adventure = State("lotion adventure", "Описание")
        S_mom_search_panties = State("search panties", "Описание")
        S_mom_panties_masturbation = State("panties masturbation", "Описание")
        S_mom_movie_night = State("movie night", "Описание")
        S_mom_romance_movie = State("romance movie", "Описание")
        S_mom_movie_afterthoughts = State("romance movie", "Описание")
        S_mom_hang_out = State("hang out", "Описание")
        S_mom_hang_out_return = State("hang out return", "Описание")
        S_mom_mall_outing = State("mall outing", "Описание")
        S_mom_cupid_store = State("cupid store", "Описание")
        S_mom_choose_gift = State("choose gift", "Описание")
        S_mom_show_necklace = State("show necklace", "Описание")
        S_mom_dressing_room = State("dressing room", "Описание")
        S_mom_smith_dream = State("smith dream", "Описание")
        S_mom_spy = State("spy", "Описание")
        S_mom_solo_dream = State("solo dream", "Описание")
        S_mom_kissing_practice = State("kissing practice", "Описание")
        S_mom_shower_walk_in = State("shower walk in", "Описание")
        S_mom_car_broken = State("car broken", "Описание")
        S_mom_check_car = State("check car", "Описание")
        S_mom_car_condition = State("car condition", "Описание")
        S_mom_fix_car = State("fix car", "Описание")
        S_mom_car_fixed = State("car fixed", "Описание")
        S_mom_panties_masturbation_again = State("panties masturbation again", "Описание")
        S_mom_night_visit = State("night visit", "Описание")
        S_mom_bad_guys_revisit = State("bad guys revisit", "Описание")
        S_mom_story_delay = State("story delay", "Описание")
        S_mom_sleepover_offer = State("sleepover offer", "Описание")
        S_mom_sleepover = State("sleepover", "Описание")
        S_mom_sleepover_wakeup = State("sleepover wakeup", "Описание")
        S_mom_diane_visit = State("diane visit", "Описание")
        S_mom_dinner = State("dinner", "Описание")
        S_mom_dinner_outfit = State("dinner outfit", "Описание")
        S_mom_dinner_fish = State("dinner fish", "Описание")
        S_mom_diane_dinner = State("diane dinner", "Описание")
        S_mom_movie_night_two = State("movie night two", "Описание")
        S_mom_romance_movie_two = State("romance movie two", "Описание")
        S_mom_movie_afterthoughts_two = State("movie afterthoughts two", "Описание")
        S_mom_night_visit_two = State("night visit two", "Описание")
        S_mom_midnight_noises = State("midnight noises", "Описание")
        S_mom_midnight_search = State("midnight search", "Описание")
        S_mom_fetch_towel = State("fetch towel", "Описание")
        S_mom_midnight_swim_after = State("midnight swim after", "Описание")
        S_mom_night_visit_three = State("night visit three", "Описание")
        S_mom_note_delay = State("note delay", "Описание")
        S_mom_note = State("note", "Описание")
        S_mom_fetch_laundry = State("fetch laundry", "Описание")
        S_mom_give_laundry = State("give laundry", "Описание")
        S_mom_end = State("end")


        S_mom_start.add(T_mom_breakfast, S_mom_relaxing, actions = ["exec", L_map.unlock, "exec", L_erikhouse.unlock])
        S_mom_relaxing.add(T_all_school_entrance, S_mom_overheard,
                           actions = ["set", "dad question"],
                           )
        S_mom_overheard.add(T_mom_check, S_mom_debt_call,
                            actions = ["location", {"place": L_home_kitchen},
                                       "force", {"flag": True},
                                       ],
                            )
        S_mom_debt_call.add(T_mom_debt_help, S_mom_lawn_delay,
                            actions = ["set", "money question",
                                       "unforce", None,
                                       ],
                            )
        S_mom_lawn_delay.add(T_all_sleep, S_mom_lawn_help)
        S_mom_lawn_help.add(T_mom_help_mow, S_mom_fill_mower)
        S_mom_fill_mower.add(T_mom_filled_mower, S_mom_mow_lawn)
        S_mom_mow_lawn.add(T_mom_mowed_lawn, S_mom_clothes_dirty)
        S_mom_clothes_dirty.add(T_mom_sis_bitch, S_mom_wash_clothes,
                                actions = ["location", {"place": L_home_basement},
                                           "force", {"flag": True},
                                           ],
                                )
        S_mom_wash_clothes.add(T_mom_clean_clothes, S_mom_sleeping,
                               actions = ["unforce", None,],
                               )
        S_mom_sleeping.add(T_all_sleep, S_mom_doorbell)
        S_mom_doorbell.add(T_mom_check_door, S_mom_debt_collectors,
                           actions = ["location", {"place": L_home_entrance},
                                      "force", {"flag": True},
                                      ],
                           )
        S_mom_debt_collectors.add(T_mom_bad_guys, S_mom_mrsj_visit_delay,
                                  actions = ["set", "bad guys question",
                                             "unforce", None,
                                             ],
                                  )
        S_mom_mrsj_visit_delay.add(T_all_sleep, S_mom_mrsj_visit,
                                   actions = ["location", {"place": L_home},
                                              "force", {"flag": True},
                                              ],
                                   )
        S_mom_mrsj_visit.add(T_mom_mrsj_condolences, S_mom_pipe_delay,
                             actions = ["unforce", None,],
                             )
        S_mom_pipe_delay.add(T_all_sleep, S_mom_pipe_help)
        S_mom_pipe_help.add(T_mom_broken_pipe, S_mom_sis_check,
                            actions = ["location", [M_jenny, {"place": L_NULL}],
                                       "force", [M_jenny, {"flag": True}],
                                       ],
                            )
        S_mom_sis_check.add(T_mom_sis_order, S_mom_close_valve)
        S_mom_close_valve.add(T_mom_closed_valve, S_mom_pipe_check)
        S_mom_pipe_check.add(T_mom_get_wrench, S_mom_fix_pipe,
                             actions = ["force", [M_jenny, {"tod": [0,1]}]],
                             )
        S_mom_fix_pipe.add(T_mom_fixed_broken_pipe, S_mom_sis_boobs_afterthoughts,
                           actions = ["unforce", M_jenny],
                           )
        S_mom_sis_boobs_afterthoughts.add(T_mom_sis_nice_boobs, S_mom_shower_delay)
        S_mom_shower_delay.add(T_all_sleep, S_mom_shower_peek)
        S_mom_shower_peek.add(T_mom_shower_admire, S_mom_shower_peek_after)
        S_mom_shower_peek_after.add(T_all_sleep, S_mom_bad_guys_driveby)
        S_mom_bad_guys_driveby.add(T_mom_bad_guys_watching, S_mom_chores_delay)
        S_mom_chores_delay.add(T_all_sleep, S_mom_vacuum_help,
                               actions = ["set", "chores",
                                          "location", {"place": L_home_entrance},
                                          "force", {"tod":[0,1]},
                                          ],
                               )
        S_mom_vacuum_help.add(T_all_sleep, S_mom_vacuum_help,
                              actions = ["set", "chores"],
                              )
        S_mom_vacuum_help.add(T_mom_vacuumed, S_mom_dishes_help,
                              actions = ["unforce", None,],
                              )
        S_mom_dishes_help.add(T_all_sleep, S_mom_dishes_help,
                              actions = ["set", "chores"],
                              )
        S_mom_dishes_help.add(T_mom_washed_dishes, S_mom_laundry_help,
                               actions = ["location", {"place": L_home_basement},
                                          "force", {"tod":[0,1]},
                                          ],
                               )
        S_mom_laundry_help.add(T_all_sleep, S_mom_laundry_help,
                               actions = ["set", "chores"],
                               )
        S_mom_laundry_help.add(T_mom_cleaned_laundry, S_mom_lotion_adventure,
                               actions = ["clear", "bedroom locked",
                                          "set", "fetch lotion",
                                          ],
                               )
        S_mom_lotion_adventure.add(T_mom_lotion_applied, S_mom_search_panties,
                               actions = ["clear", "fetch lotion",
                                          "clear", "retrieved lotion",
                                          "set", "panties available",
                                          "unforce", None,
                                          ],
                               )
        S_mom_search_panties.add(T_mom_steal_panties, S_mom_panties_masturbation,
                                 actions = ["clear", "bed locked"],
                                 )
        S_mom_panties_masturbation.add(T_mom_caught_masturbating, S_mom_movie_night,
                                       actions = ["clear", "panties available",
                                                  "location", {"place": L_home_entrance},
                                                  "force", {"tod": 2},
                                                  ],
                                       )
        S_mom_movie_night.add(T_mom_movie_invite, S_mom_romance_movie,
                              actions = ["clear", "panties available",
                                         "location", {"place": L_home_livingroom},
                                         "force", {"flag": True},
                                         ],
                              )
        S_mom_romance_movie.add(T_mom_watch_movie, S_mom_movie_afterthoughts,
                                actions = ["unforce", None,],
                                )
        S_mom_movie_afterthoughts.add(T_mom_movie_night_finish, S_mom_hang_out)
        S_mom_hang_out.add(T_mom_hang_out_accept, S_mom_mall_outing)
        S_mom_hang_out.add(T_mom_hang_out_refuse, S_mom_hang_out_return)
        S_mom_hang_out_return.add(T_mom_hang_out_accept, S_mom_mall_outing)
        S_mom_mall_outing.add(T_mom_mall_arrival, S_mom_cupid_store)
        S_mom_cupid_store.add(T_mom_cupid_arrival, S_mom_choose_gift,
                              actions = ["location", {"place": L_cupid},
                                         "force", {"flag": True},
                                         ],
                              )
        S_mom_choose_gift.add(T_mom_pick_necklace, S_mom_show_necklace)
        S_mom_show_necklace.add(T_mom_give_necklace, S_mom_dressing_room,
                                actions = ["location", {"place": L_cupid_dressroom},],
                                )
        S_mom_dressing_room.add(T_mom_dressing_room_check, S_mom_smith_dream,
                                actions = ["set", "jerk available",
                                           "unforce", None,
                                           ],
                                )
        S_mom_smith_dream.add(T_mom_dream, S_mom_spy,
                              actions = ["location", {"place": L_home_mombedroom},
                                         "force", {"flag": True},
                                         ],
                              )
        S_mom_spy.add(T_mom_caught_spying, S_mom_solo_dream,
                      actions = ["set", "caught spying",
                                 "unforce", None,
                                 ],
                      )
        S_mom_solo_dream.add(T_mom_dream, S_mom_kissing_practice)
        S_mom_kissing_practice.add(T_mom_kiss, S_mom_shower_walk_in,
                                   actions = ["set", "practice kissing"],
                                   )
        S_mom_shower_walk_in.add(T_mom_shower_admire, S_mom_car_broken)
        S_mom_car_broken.add(T_mom_car_help, S_mom_check_car)
        S_mom_check_car.add(T_mom_check_engine, S_mom_car_condition)
        S_mom_car_condition.add(T_mom_deliver_car_news, S_mom_fix_car, actions = ["exec", L_dealership_front.unlock])
        S_mom_fix_car.add(T_mom_renew_insurance, S_mom_car_fixed)
        S_mom_car_fixed.add(T_mom_car_fun, S_mom_panties_masturbation_again,
                            actions = ["set", "panties available"],
                            )
        S_mom_panties_masturbation_again.add(T_mom_caught_masturbating, S_mom_night_visit,
                                             actions = ["clear", "panties available"],
                                             )
        S_mom_night_visit.add(T_mom_midnight_fun, S_mom_bad_guys_revisit)
        S_mom_bad_guys_revisit.add(T_mom_bad_guys_beatup, S_mom_story_delay,
                                   actions = ["set", "shower random",
                                              "set", "shower sex available",
                                              ],
                                   )
        S_mom_story_delay.add(T_all_sleep, S_mom_sleepover_offer)
        S_mom_sleepover_offer.add(T_mom_sleepover_accept, S_mom_sleepover,
                                  actions = ["set", "sleep together"],
                                  )
        S_mom_sleepover.add(T_all_sleep, S_mom_sleepover_wakeup)
        S_mom_sleepover_wakeup.add(T_mom_sleepover_morning, S_mom_diane_visit)
        S_mom_diane_visit.add(T_mom_diane_chat, S_mom_dinner)
        S_mom_dinner.add(T_mom_dinner_help, S_mom_dinner_outfit, actions=["exec", L_pier.unlock])
        S_mom_dinner_outfit.add(T_mom_dinner_outfit_check, S_mom_dinner_fish)
        S_mom_dinner_fish.add(T_mom_dinner_fish_caught, S_mom_diane_dinner)
        S_mom_diane_dinner.add(T_mom_diane_dinner_chat, S_mom_movie_night_two)
        S_mom_movie_night_two.add(T_mom_movie_invite, S_mom_romance_movie_two)
        S_mom_romance_movie_two.add(T_mom_watch_movie, S_mom_movie_afterthoughts_two)
        S_mom_movie_afterthoughts_two.add(T_mom_movie_night_finish, S_mom_night_visit_two)
        S_mom_night_visit_two.add(T_mom_midnight_fun, S_mom_midnight_noises)
        S_mom_midnight_noises.add(T_mom_midnight_wakeup, S_mom_midnight_search)
        S_mom_midnight_search.add(T_mom_midnight_swim, S_mom_fetch_towel,
                                  actions = ["location", {"place": L_home_backyard},
                                             "force", {"flag": True},
                                             ],
                                  )
        S_mom_fetch_towel.add(T_mom_gave_towel, S_mom_night_visit_three,
                              actions = ["unforce", None,],
                              )
        S_mom_midnight_swim_after.add(T_all_sleep, S_mom_night_visit_three)
        S_mom_night_visit_three.add(T_mom_midnight_fun, S_mom_note_delay,
                                    actions = ["assign", ("delay", 2),
                                               "set", "sex available",
                                               "location", {"place": L_home_mombedroom,
                                                            "condition": "M_mom.get('sex available') and M_mom.get('location random') == 'bedroom' and M_mom.get('time random')()",
                                                            },
                                               "force", {"tod": [0,1]},
                                               ],
                                    )
        S_mom_note_delay.add(T_all_sleep, S_mom_note_delay,
                             actions = ["triggerOnZero", ("delay", T_mom_delay)]
                             )
        S_mom_note_delay.add(T_mom_delay, S_mom_note)
        S_mom_note.add(T_mom_read_note, S_mom_fetch_laundry,
                       actions = ["location", {"place": L_home_basement},
                                  "force", {"flag": True},
                                  ],
                       )
        S_mom_fetch_laundry.add(T_mom_got_laundry, S_mom_give_laundry)
        S_mom_give_laundry.add(T_mom_basement_fun, S_mom_end,
                               actions = ["set", "basement sex",
                                          "location", {"place": L_home_mombedroom,
                                                       "condition": "M_mom.get('sex available') and M_mom.get('location random') == 'bedroom' and M_mom.get('time random')()",
                                                       },
                                          "force", {"tod": [0,1]},
                                          "exec", A_end_of_chores.unlock,
                                          ],
                               )

        M_mom.add(S_mom_start, S_mom_relaxing, S_mom_overheard, S_mom_debt_call, S_mom_lawn_delay,
                  S_mom_lawn_help, S_mom_fill_mower, S_mom_mow_lawn, S_mom_clothes_dirty,
                  S_mom_wash_clothes, S_mom_sleeping, S_mom_doorbell, S_mom_debt_collectors,
                  S_mom_mrsj_visit, S_mom_mrsj_visit_delay, S_mom_pipe_delay, S_mom_pipe_help,
                  S_mom_sis_check, S_mom_close_valve, S_mom_pipe_check, S_mom_fix_pipe,
                  S_mom_sis_boobs_afterthoughts, S_mom_shower_delay, S_mom_shower_peek,
                  S_mom_shower_peek_after, S_mom_bad_guys_driveby, S_mom_chores_delay, S_mom_vacuum_help,
                  S_mom_dishes_help, S_mom_laundry_help, S_mom_lotion_adventure, S_mom_search_panties,
                  S_mom_panties_masturbation, S_mom_movie_night, S_mom_romance_movie,
                  S_mom_movie_afterthoughts, S_mom_hang_out, S_mom_hang_out_return,
                  S_mom_mall_outing, S_mom_cupid_store, S_mom_choose_gift,
                  S_mom_show_necklace, S_mom_dressing_room, S_mom_smith_dream,
                  S_mom_spy, S_mom_solo_dream, S_mom_kissing_practice,
                  S_mom_shower_walk_in, S_mom_car_broken, S_mom_check_car,
                  S_mom_car_condition, S_mom_fix_car, S_mom_car_fixed,
                  S_mom_panties_masturbation_again, S_mom_night_visit,
                  S_mom_bad_guys_revisit, S_mom_story_delay, S_mom_sleepover_offer,
                  S_mom_sleepover, S_mom_sleepover_wakeup, S_mom_diane_visit,
                  S_mom_dinner, S_mom_dinner_outfit, S_mom_dinner_fish,
                  S_mom_diane_dinner, S_mom_movie_night_two, S_mom_romance_movie_two,
                  S_mom_movie_afterthoughts_two, S_mom_night_visit_two, S_mom_midnight_noises,
                  S_mom_midnight_search, S_mom_fetch_towel, S_mom_midnight_swim_after,
                  S_mom_night_visit_three, S_mom_note_delay, S_mom_note, S_mom_fetch_laundry,
                  S_mom_give_laundry, S_mom_end
        )
        M_mom.add_action(T_all_sleep, ["clear", "room sneak",
                                       "clear", "movie night",
                                       "assign", ["location random", "random.choice(('bedroom', 'kitchen', 'basement'))"],
                                       "assign", ["time random", "random.choice((game.timer.is_morning, game.timer.is_afternoon))"],
                                       ])
    return

label mom_machine_init:
    python:
        M_mom = Machine("mom", default_loc = [[L_home_kitchen, L_home_basement, L_home_mombedroom, L_home_mombedroom]],
                        vars = {"sex speed": .4,
                                "mom concerned": 100,
                                "dad question": False,
                                "money question": False,
                                "bad guys question": False,
                                "bedroom locked": True,
                                "shower random": False,
                                "chores": False,
                                "lotion fun": False,
                                "fetch lotion": False,
                                "retrieved lotion": False,
                                "bed locked": True,
                                "panties available": False,
                                "panties taken": False,
                                "no panties": False,
                                "jerk available": False,
                                "caught spying": False,
                                "practice kissing": False,
                                "jerk count": 0,
                                "sleep together": False,
                                "revealing": False,
                                "shower fingered": False,
                                "sex flip": True,
                                "robe on": False,
                                "sex available": False,
                                "change angle": False,
                                "location random": "",
                                "time random": game.timer.is_dark,
                                "room sneak": False,
                                "movie night": False,
                                "car jerk": False,
                                "car sex": False,
                                "basement sex": False,
                                "shower sex available": False,
                               },
        )
        M_mom.set_priority(1)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
