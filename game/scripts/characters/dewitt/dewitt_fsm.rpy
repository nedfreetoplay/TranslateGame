label dewitt_triggers_init:
    python:

        T_dewitt_mc_welcome_back = Trigger("MC welcome back", "Описание")
        T_dewitt_mc_overhear = Trigger("MC overhear", "Описание")
        T_dewitt_mc_talent_show_help = Trigger("MC talent show help", "Описание")
        T_dewitt_judith_flute = Trigger("Judith flute", "Описание")
        T_dewitt_get_flute = Trigger("get flute", "Описание")
        T_dewitt_fix_flute = Trigger("fix flute", "Описание")
        T_dewitt_flute_practice = Trigger("flute practice", "Описание")
        T_dewitt_talent_hunt = Trigger("talent hunt", "Описание")
        T_dewitt_annies_refusal = Trigger("Annie's refusal", "Описание")
        T_dewitt_eves_agreement = Trigger("Eve's agreement", "Описание")
        T_dewitt_karaoke_jam = Trigger("karaoke jam", "Описание")
        T_dewitt_find_last_talent = Trigger("find last talent", "Описание")
        T_dewitt_kevins_agreement = Trigger("Kevin's agreement", "Описание")
        T_dewitt_eriks_agreement_shed = Trigger("Erik's agreement shed", "Описание")
        T_dewitt_eriks_agreement_no_shed = Trigger("Erik's agreement no shed", "Описание")
        T_dewitt_no_paint = Trigger("no paint", "Описание")
        T_dewitt_diane_find_paint = Trigger("Diane find paint", "Описание")
        T_dewitt_shed_find_paint = Trigger("shed find paint", "Описание")
        T_dewitt_shed_paint = Trigger("shed paint", "Описание")
        T_dewitt_made_replacement_guitar = Trigger("made replacement guitar", "Описание")
        T_dewitt_get_fender_guitar = Trigger("get fender guitar", "Описание")
        T_dewitt_give_fender_guitar = Trigger("give fender guitar", "Описание")
        T_dewitt_talent_show_excitement = Trigger("talent show excitement", "Описание")
        T_dewitt_auditorium_problem = Trigger("auditorium problem", "Описание")
        T_dewitt_bandit_clue = Trigger("bandit clue", "Описание")
        T_dewitt_clue_dead_end = Trigger("clue dead end", "Описание")
        T_dewitt_crying = Trigger("crying", "Описание")
        T_dewitt_gang_deal = Trigger("gang deal", "Описание")
        T_dewitt_erik_deal = Trigger("Erik deal", "Описание")
        T_dewitt_fixed_auditorium = Trigger("fixed auditorium", "Описание")
        T_dewitt_fetch_dewitt = Trigger("fetch Dewitt", "Описание")
        T_dewitt_talent_show_uncancelled = Trigger("talent show uncancelled", "Описание")
        T_dewitt_twerk_n_derk = Trigger("twerk n derk", "Описание")
        T_dewitt_smith_payback_plan = Trigger("Smith payback plan", "Описание")
        T_dewitt_sticky_tape_get = Trigger("sticky tape get", "Описание")
        T_dewitt_school_sneak_in = Trigger("school sneak in", "Описание")
        T_dewitt_trap_set = Trigger("trap set", "Описание")
        T_dewitt_double_check_trap = Trigger("double check trap", "Описание")
        T_dewitt_trap_check_ok = Trigger("trap check ok", "Описание")
        T_dewitt_talent_show_intro = Trigger("talent show intro", "Описание")
        T_dewitt_talent_show_success = Trigger("talent show success", "Описание")
        T_dewitt_sex_it_up = Trigger("twerk n derk", "Описание")
    return

label dewitt_fsm_init:
    python:

        S_dewitt_start = State("start")
        S_dewitt_intro = State("intro", "Описание")
        S_dewitt_smith_berating = State("Smith berating", "Описание")
        S_dewitt_talent_show_help = State("talent show help", "Описание")
        S_dewitt_find_flute = State("find flute", "Описание")
        S_dewitt_judith_locker_search = State("Judith locker search", "Описание")
        S_dewitt_make_new_flute = State("make new flute", "Описание")
        S_dewitt_return_flute = State("return flute", "Описание")
        S_dewitt_talent_show_progress = State("talent show progress", "Описание")
        S_dewitt_talent_show_ask_annie = State("talent show ask Annie", "Описание")
        S_dewitt_talent_show_ask = State("talent show ask", "Описание")
        S_dewitt_talent_show_ask_eve = State("talent show ask Eve", "Описание")
        S_dewitt_eve_karaoke = State("Eve karaoke", "Описание")
        S_dewitt_talent_show_ask_kevin = State("talent show ask Kevin", "Описание")
        S_dewitt_erik_borrow_guitar = State("Erik borrow guitar", "Описание")
        S_dewitt_garage_find_paint = State("garage find paint", "Описание")
        S_dewitt_ask_deb_paint = State("ask Deb paint", "Описание")
        S_dewitt_ask_diane_paint = State("ask Diane paint", "Описание")
        S_dewitt_shed_get_paint = State("shed get paint", "Описание")
        S_dewitt_make_replacement_guitar = State("make replacement guitar", "Описание")
        S_dewitt_replace_guitar = State("replace guitar", "Описание")
        S_dewitt_kevin_give_guitar = State("Kevin give guitar", "Описание")
        S_dewitt_talent_get = State("talent get", "Описание")
        S_dewitt_music_sheets_delay = State("music sheets delay", "Описание")
        S_dewitt_music_sheets = State("music sheets", "Описание")
        S_dewitt_graffiti_mess = State("graffiti mess", "Описание")
        S_dewitt_paint_trail = State("paint trail", "Описание")
        S_dewitt_check_up = State("check up", "Описание")
        S_dewitt_eve_meet_up = State("Eve meet up", "Описание")
        S_dewitt_erik_get_beer = State("Erik get beer", "Описание")
        S_dewitt_clean_graffiti = State("clean graffiti", "Описание")
        S_dewitt_find_dewitt = State("find Dewitt", "Описание")
        S_dewitt_show_auditorium = State("show auditorium", "Описание")
        S_dewitt_office_reward = State("office reward", "Описание")
        S_dewitt_talent_show_practice = State("talent show practice", "Описание")
        S_dewitt_talent_show_practice_delay = State("talent show practice delay", "Описание")
        S_dewitt_science_adhesive = State("science adhesive", "Описание")
        S_dewitt_school_sneak_mission_help = State("school sneak mission help", "Описание")
        S_dewitt_school_sneak_mission = State("school sneak mission", "Описание")
        S_dewitt_smith_office_trap = State("Smith office trap", "Описание")
        S_dewitt_pre_talent_show_chat = State("pre talent show", "Описание")
        S_dewitt_trap_check_up = State("trap check up", "Описание")
        S_dewitt_attend_talent_show = State("attend talent show", "Описание")
        S_dewitt_talent_show = State("talent show", "Описание")
        S_dewitt_office_night_visit_delay = State("office night visit delay", "Описание")
        S_dewitt_office_night_visit = State("office night visit", "Описание")
        S_dewitt_end = State("end")


        S_dewitt_start.add(T_bridget_workout, S_dewitt_intro)
        S_dewitt_intro.add(T_dewitt_mc_welcome_back, S_dewitt_smith_berating)
        S_dewitt_smith_berating.add(T_dewitt_mc_overhear, S_dewitt_talent_show_help)
        S_dewitt_talent_show_help.add(T_dewitt_mc_talent_show_help, S_dewitt_find_flute)
        S_dewitt_find_flute.add(T_dewitt_judith_flute, S_dewitt_judith_locker_search)
        S_dewitt_judith_locker_search.add(T_dewitt_get_flute, S_dewitt_make_new_flute)
        S_dewitt_make_new_flute.add(T_dewitt_fix_flute, S_dewitt_return_flute)
        S_dewitt_return_flute.add(T_dewitt_flute_practice, S_dewitt_talent_show_progress,
                                  actions = ["exec", player.increase_grade_music]
                                  )
        S_dewitt_talent_show_progress.add(T_dewitt_talent_hunt, S_dewitt_talent_show_ask_annie)
        S_dewitt_talent_show_ask_annie.add(T_dewitt_annies_refusal, S_dewitt_talent_show_ask,
                                           actions = ["set", "talent ask erik",
                                                      "set", "talent ask eve",
                                                      "set", "talent ask dexter",
                                                      "set", "talent ask judith",
                                                      "set", "talent ask kevin",
                                                      "set", "talent ask mia",
                                                      "set", "talent ask ronda",
                                                      "set", "talent ask roxxy",
                                                     ]
                                           )
        S_dewitt_talent_show_ask.add(T_dewitt_eves_agreement, S_dewitt_eve_karaoke,
                                     actions = ["clear", "talent ask eve",
                                                "set", "talent helping eve",
                                               ]
                                     )
        S_dewitt_talent_show_ask.add(T_dewitt_kevins_agreement, S_dewitt_erik_borrow_guitar,
                                     actions = ["clear", "talent ask kevin",
                                                "set", "talent helping kevin",
                                               ]
                                     )
        S_dewitt_talent_show_ask_eve.add(T_dewitt_eves_agreement, S_dewitt_eve_karaoke)
        S_dewitt_eve_karaoke.add(T_dewitt_find_last_talent, S_dewitt_talent_show_ask_kevin,
                                 actions = ["clear", "talent helping eve"]
                                 )
        S_dewitt_eve_karaoke.add(T_dewitt_karaoke_jam, S_dewitt_talent_get,
                                 actions = ["clear", "talent helping eve"]
                                 )
        S_dewitt_talent_show_ask_kevin.add(T_dewitt_kevins_agreement, S_dewitt_erik_borrow_guitar)
        S_dewitt_erik_borrow_guitar.add(T_dewitt_eriks_agreement_shed, S_dewitt_shed_get_paint)
        S_dewitt_erik_borrow_guitar.add(T_dewitt_eriks_agreement_no_shed, S_dewitt_garage_find_paint)
        S_dewitt_garage_find_paint.add(T_dewitt_no_paint, S_dewitt_ask_deb_paint)
        S_dewitt_ask_deb_paint.add(T_dewitt_diane_find_paint, S_dewitt_ask_diane_paint)
        S_dewitt_ask_diane_paint.add(T_dewitt_shed_paint, S_dewitt_shed_get_paint)
        S_dewitt_shed_get_paint.add(T_dewitt_shed_find_paint, S_dewitt_make_replacement_guitar)
        S_dewitt_make_replacement_guitar.add(T_dewitt_made_replacement_guitar, S_dewitt_replace_guitar)
        S_dewitt_replace_guitar.add(T_dewitt_get_fender_guitar, S_dewitt_kevin_give_guitar)
        S_dewitt_kevin_give_guitar.add(T_dewitt_find_last_talent, S_dewitt_talent_show_ask_eve,
                                       actions = ["clear", "talent helping kevin"]
                                       )
        S_dewitt_kevin_give_guitar.add(T_dewitt_give_fender_guitar, S_dewitt_talent_get,
                                       actions = ["clear", "talent helping kevin"]
                                       )
        S_dewitt_talent_get.add(T_dewitt_talent_show_excitement, S_dewitt_music_sheets_delay,
                                actions = ["clear", "talent ask erik",
                                           "clear", "talent ask eve",
                                           "clear", "talent ask dexter",
                                           "clear", "talent ask judith",
                                           "clear", "talent ask kevin",
                                           "clear", "talent ask mia",
                                           "clear", "talent ask ronda",
                                           "clear", "talent ask roxxy",
                                           "exec", player.increase_grade_music,
                                          ]
                                )
        S_dewitt_music_sheets_delay.add(T_all_sleep, S_dewitt_music_sheets)
        S_dewitt_music_sheets.add(T_dewitt_auditorium_problem, S_dewitt_graffiti_mess,
                                  actions = ["location", {"place": L_school_assemblyhall},
                                             "force", {"flag": True},
                                             ],
                                  )
        S_dewitt_graffiti_mess.add(T_dewitt_bandit_clue, S_dewitt_paint_trail,
                                   actions = ["unforce", None,
                                              "location", [M_annie, {"place": L_school_smithoffice}],
                                              "force", [M_annie, {"flag": True}],
                                              "location", [M_smith, {"place": L_school_smithoffice}],
                                              "force", [M_smith, {"flag": True}],
                                              ],
                                   )
        S_dewitt_paint_trail.add(T_dewitt_clue_dead_end, S_dewitt_check_up,
                                 actions = ["unforce", M_annie,
                                            "unforce", M_smith,
                                            ],
                                 )
        S_dewitt_check_up.add(T_dewitt_crying, S_dewitt_eve_meet_up)
        S_dewitt_eve_meet_up.add(T_dewitt_gang_deal, S_dewitt_erik_get_beer)
        S_dewitt_erik_get_beer.add(T_dewitt_erik_deal, S_dewitt_clean_graffiti)
        S_dewitt_clean_graffiti.add(T_dewitt_fixed_auditorium, S_dewitt_find_dewitt,
                                    actions = ["location", {"place": L_school_musicclassroom},
                                               "force", {"flag": True},
                                               ],
                                    )
        S_dewitt_find_dewitt.add(T_dewitt_fetch_dewitt, S_dewitt_show_auditorium,
                                 actions = ["location", {"place": L_school_assemblyhall}],
                                 )
        S_dewitt_show_auditorium.add(T_dewitt_talent_show_uncancelled, S_dewitt_office_reward,
                                     actions = ["location", {"place": L_school_dewittoffice}],
                                     )
        S_dewitt_office_reward.add(T_dewitt_twerk_n_derk, S_dewitt_talent_show_practice_delay,
                                   actions = ["exec", player.increase_grade_music,
                                              "unforce", None,
                                              ],
                                   )
        S_dewitt_talent_show_practice_delay.add(T_all_sleep, S_dewitt_talent_show_practice)
        S_dewitt_talent_show_practice.add(T_dewitt_smith_payback_plan, S_dewitt_science_adhesive)
        S_dewitt_science_adhesive.add(T_dewitt_sticky_tape_get, S_dewitt_school_sneak_mission_help)
        S_dewitt_school_sneak_mission_help.add(T_dewitt_erik_deal, S_dewitt_school_sneak_mission)
        S_dewitt_school_sneak_mission.add(T_dewitt_school_sneak_in, S_dewitt_smith_office_trap)
        S_dewitt_smith_office_trap.add(T_dewitt_trap_set, S_dewitt_pre_talent_show_chat)
        S_dewitt_pre_talent_show_chat.add(T_dewitt_double_check_trap, S_dewitt_trap_check_up,
                                          actions = ["location", [M_annie, {"place": L_school_smithoffice}],
                                                     "force", [M_annie, {"flag": True}],
                                                     "location", [M_smith, {"place": L_school_smithoffice}],
                                                     "force", [M_smith, {"flag": True}],
                                                     ],
                                          )
        S_dewitt_trap_check_up.add(T_dewitt_trap_check_ok, S_dewitt_attend_talent_show)
        S_dewitt_attend_talent_show.add(T_dewitt_talent_show_intro, S_dewitt_talent_show)
        S_dewitt_talent_show.add(T_dewitt_talent_show_success, S_dewitt_office_night_visit_delay)
        S_dewitt_office_night_visit_delay.add(T_all_sleep, S_dewitt_office_night_visit,
                                              actions = ["unforce", M_annie,
                                                         "unforce", M_smith,
                                                         ],
                                              )
        S_dewitt_office_night_visit.add(T_dewitt_sex_it_up, S_dewitt_end,
                                        actions = ["exec", player.increase_grade_music, "exec", A_music_taste.unlock]
                                        )

        M_dewitt.add(S_dewitt_start, S_dewitt_intro, S_dewitt_smith_berating,
                     S_dewitt_talent_show_help, S_dewitt_find_flute,
                     S_dewitt_judith_locker_search, S_dewitt_make_new_flute,
                     S_dewitt_return_flute, S_dewitt_talent_show_progress,
                     S_dewitt_talent_show_ask_annie, S_dewitt_talent_show_ask,
                     S_dewitt_talent_show_ask_eve, S_dewitt_eve_karaoke,
                     S_dewitt_talent_show_ask_kevin, S_dewitt_erik_borrow_guitar,
                     S_dewitt_garage_find_paint, S_dewitt_ask_deb_paint,
                     S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint, S_dewitt_make_replacement_guitar,
                     S_dewitt_replace_guitar, S_dewitt_kevin_give_guitar,
                     S_dewitt_talent_get, S_dewitt_music_sheets_delay,
                     S_dewitt_music_sheets, S_dewitt_graffiti_mess,
                     S_dewitt_paint_trail, S_dewitt_check_up,
                     S_dewitt_eve_meet_up, S_dewitt_erik_get_beer,
                     S_dewitt_clean_graffiti, S_dewitt_find_dewitt,
                     S_dewitt_show_auditorium, S_dewitt_office_reward,
                     S_dewitt_talent_show_practice, S_dewitt_talent_show_practice_delay,
                     S_dewitt_science_adhesive, S_dewitt_school_sneak_mission_help,
                     S_dewitt_school_sneak_mission, S_dewitt_smith_office_trap,
                     S_dewitt_pre_talent_show_chat, S_dewitt_trap_check_up,
                     S_dewitt_attend_talent_show, S_dewitt_talent_show,
                     S_dewitt_office_night_visit_delay, S_dewitt_office_night_visit,
                     S_dewitt_end)
    return

label dewitt_machine_init:
    python:
        M_dewitt = Machine("Dewitt", default_loc = [[L_school_musicclassroom, L_school_musicclassroom, L_school_dewittoffice, L_NULL],
                                                    [L_NULL, L_NULL, L_NULL, L_NULL]
                                                    ],
                           vars = {"sex speed": .175,
                                   "talent ask erik": False,
                                   "talent ask eve": False,
                                   "talent ask dexter": False,
                                   "talent ask judith": False,
                                   "talent ask kevin": False,
                                   "talent ask mia": False,
                                   "talent ask ronda": False,
                                   "talent ask roxxy": False,
                                   "talent helping eve": False,
                                   "talent helping kevin": False,
                                   "failcount": 0,
                                  },
        )
        M_dewitt.set_priority(1)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
