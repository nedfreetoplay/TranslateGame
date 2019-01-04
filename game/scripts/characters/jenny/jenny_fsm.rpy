label sister_triggers_init:
    python:

        T_jenny_hallway = Trigger("hallway", "Встретиться с Дженни в коридоре")
        T_jenny_panty_raid = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_panty_caught = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_panty_bought = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_somrak_panty_traded = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_peep_cuddle = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_somrak_training_halt = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_panty_sex_toy_traded = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_somrak_panty_traded_tier_2 = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_tricked = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_diary_read = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_webcam_connected = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_watched_stream = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_spied_on_neighbour = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_debbie_mention_breakfast = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_breakfast_done = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_paid_for_titties = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_peep_cuddle_tier_2 = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_hallway_chat = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_couch_fun = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_couch_fun_tier_2 = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_somrak_training_halt_tier_2 = Trigger("panty raid", "Украсть трусики Дженни")
        T_jenny_panty_sex_toy_traded_tier_2 = Trigger("panty raid")
        T_jenny_somrak_panty_traded_tier_3 = Trigger("panty raid")
        T_jenny_watched_stream_tier_2 = Trigger("panty raid")
        T_jenny_spied_on_neighbour_tier_2 = Trigger("panty raid")
        T_jenny_hallway_chat_focus = Trigger("panty raid")
        T_jenny_peep_cuddle_tier_3 = Trigger("panty raid")
        T_jenny_couch_fun_tier_3 = Trigger("panty raid")
        T_jenny_somrak_training_halt_tier_3 = Trigger("panty raid")
        T_jenny_panty_sex_toy_traded_tier_3 = Trigger("panty raid")
        T_jenny_somrak_panty_traded_tier_4 = Trigger("panty raid")
        T_jenny_watched_stream_tier_3 = Trigger("panty raid")
        T_jenny_spied_on_neighbour_tier_3 = Trigger("panty raid")
        T_jenny_peep_cuddle_tier_4 = Trigger("panty raid")
        T_jenny_overhear_stream = Trigger("panty raid")
        T_jenny_stream_idea = Trigger("panty raid")
        T_jenny_stream_ready = Trigger("panty raid")
        T_jenny_peep_cuddle_tier_5 = Trigger("panty raid")
        T_jenny_need_toys = Trigger("panty raid")
        T_jenny_brought_toys = Trigger("panty raid")
    return

label sister_fsm_init:
    python:

        S_jenny_start = State("start")
        S_jenny_busy = State("bored", "Жду чего-то")
        S_jenny_panty_steal = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_panty_deal = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_somrak_panty_trade = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_shower_peep_bed_cuddle = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_somrak_more_panty = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_panty_deal_tier_2 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_somrak_panty_trade_tier_2 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_debbie_needs_jenny = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_read_diary = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_connect_webcam = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_watch_stream = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_telescope_spying = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_debbie_breakfast = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_breakfast = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_titty_deal = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_shower_peep_bed_cuddle_tier_2 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_hallway_meetup = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_couch_naughty_time = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_couch_naughty_time_tier_2 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_somrak_more_panty_tier_2 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_panty_deal_tier_3 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_somrak_panty_trade_tier_3 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_watch_stream_tier_2 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_telescope_spying_tier_2 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_hallway_meetup_focus = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_shower_peep_bed_cuddle_tier_3 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_couch_naughty_time_tier_3 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_somrak_more_panty_tier_3 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_panty_deal_tier_4 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_somrak_panty_trade_tier_4 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_watch_stream_tier_3 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_telescope_spying_tier_3 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_shower_peep_bed_cuddle_tier_4 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_hallway_noises = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_overhear_caught = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_cam_show = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_shower_peep_bed_cuddle_tier_5 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_help_stream_tier_4 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_prepare_stream_tier_4 = State("Bedroom1", "В ожидании рейда трусиков")
        S_jenny_end = State("end")


        S_jenny_start.add(T_jenny_hallway, S_jenny_busy)
        S_jenny_busy.add(T_jenny_panty_raid, S_jenny_panty_steal,
                         actions = ["clear", "door locked"]
                         )
        S_jenny_panty_steal.add(T_jenny_panty_caught, S_jenny_panty_deal,
                                actions = ["location", {"place": L_home_sisbedroom},
                                           "force", {"tod": [0,1]},
                                           ]
                                )
        S_jenny_panty_deal.add(T_jenny_panty_bought, S_jenny_somrak_panty_trade,
                               actions = ["unforce", None]
                               )
        S_jenny_somrak_panty_trade.add(T_jenny_somrak_panty_traded, S_jenny_shower_peep_bed_cuddle)
        S_jenny_shower_peep_bed_cuddle.add(T_jenny_peep_cuddle, S_jenny_somrak_more_panty)
        S_jenny_somrak_more_panty.add(T_jenny_somrak_training_halt, S_jenny_panty_deal_tier_2)
        S_jenny_panty_deal_tier_2.add(T_jenny_panty_sex_toy_traded, S_jenny_somrak_panty_trade_tier_2)
        S_jenny_somrak_panty_trade_tier_2.add(T_jenny_somrak_panty_traded_tier_2, S_jenny_debbie_needs_jenny)
        S_jenny_debbie_needs_jenny.add(T_jenny_tricked, S_jenny_read_diary,
                                       actions = ["location", {"place": L_NULL},
                                                  "force", {"tod": [0,1]},
                                                  ]
                                       )
        S_jenny_read_diary.add(T_jenny_diary_read, S_jenny_connect_webcam,
                               actions = ["unforce", None,]
                               )
        S_jenny_connect_webcam.add(T_jenny_webcam_connected, S_jenny_watch_stream)
        S_jenny_watch_stream.add(T_jenny_watched_stream, S_jenny_telescope_spying)
        S_jenny_telescope_spying.add(T_jenny_spied_on_neighbour, S_jenny_debbie_breakfast,
                                     actions = ["location", {"place": L_home_diningroom},
                                                "force", {"tod": 0},
                                                ]
                                     )
        S_jenny_debbie_breakfast.add(T_jenny_debbie_mention_breakfast, S_jenny_breakfast)
        S_jenny_breakfast.add(T_jenny_breakfast_done, S_jenny_titty_deal,
                              actions = ["unforce", None,]
                              )
        S_jenny_titty_deal.add(T_jenny_paid_for_titties, S_jenny_shower_peep_bed_cuddle_tier_2)
        S_jenny_shower_peep_bed_cuddle_tier_2.add(T_jenny_peep_cuddle_tier_2, S_jenny_hallway_meetup)
        S_jenny_hallway_meetup.add(T_jenny_hallway_chat, S_jenny_couch_naughty_time,
                                   actions = ["location", {"place": L_home_livingroom},
                                              "force", {"tod": 2},
                                              ]
                                   )
        S_jenny_couch_naughty_time.add(T_jenny_couch_fun, S_jenny_couch_naughty_time_tier_2,
                                       actions = ["unforce", None,]
                                       )
        S_jenny_couch_naughty_time_tier_2.add(T_jenny_couch_fun_tier_2, S_jenny_somrak_more_panty_tier_2)
        S_jenny_somrak_more_panty_tier_2.add(T_jenny_somrak_training_halt_tier_2, S_jenny_panty_deal_tier_3)
        S_jenny_panty_deal_tier_3.add(T_jenny_panty_sex_toy_traded_tier_2, S_jenny_somrak_panty_trade_tier_3)
        S_jenny_somrak_panty_trade_tier_3.add(T_jenny_somrak_panty_traded_tier_3, S_jenny_watch_stream_tier_2)
        S_jenny_watch_stream_tier_2.add(T_jenny_watched_stream_tier_2, S_jenny_telescope_spying_tier_2)
        S_jenny_telescope_spying_tier_2.add(T_jenny_spied_on_neighbour_tier_2, S_jenny_hallway_meetup_focus)
        S_jenny_hallway_meetup_focus.add(T_jenny_hallway_chat_focus, S_jenny_shower_peep_bed_cuddle_tier_3)
        S_jenny_shower_peep_bed_cuddle_tier_3.add(T_jenny_peep_cuddle_tier_3, S_jenny_couch_naughty_time_tier_3)
        S_jenny_couch_naughty_time_tier_3.add(T_jenny_couch_fun_tier_3, S_jenny_somrak_more_panty_tier_3)
        S_jenny_somrak_more_panty_tier_3.add(T_jenny_somrak_training_halt_tier_3, S_jenny_panty_deal_tier_4)
        S_jenny_panty_deal_tier_4.add(T_jenny_panty_sex_toy_traded_tier_3, S_jenny_somrak_panty_trade_tier_4)
        S_jenny_somrak_panty_trade_tier_4.add(T_jenny_somrak_panty_traded_tier_4, S_jenny_watch_stream_tier_3)
        S_jenny_watch_stream_tier_3.add(T_jenny_watched_stream_tier_3, S_jenny_telescope_spying_tier_3)
        S_jenny_telescope_spying_tier_3.add(T_jenny_spied_on_neighbour_tier_3, S_jenny_shower_peep_bed_cuddle_tier_4)
        S_jenny_shower_peep_bed_cuddle_tier_4.add(T_jenny_peep_cuddle_tier_4, S_jenny_hallway_noises)
        S_jenny_hallway_noises.add(T_jenny_overhear_stream, S_jenny_overhear_caught)
        S_jenny_overhear_caught.add(T_jenny_stream_idea, S_jenny_cam_show)
        S_jenny_cam_show.add(T_jenny_stream_ready, S_jenny_shower_peep_bed_cuddle_tier_5)
        S_jenny_shower_peep_bed_cuddle_tier_5.add(T_jenny_peep_cuddle_tier_5, S_jenny_help_stream_tier_4)
        S_jenny_help_stream_tier_4.add(T_jenny_need_toys, S_jenny_prepare_stream_tier_4)
        S_jenny_prepare_stream_tier_4.add(T_jenny_brought_toys, S_jenny_end)

        M_jenny.add(S_jenny_start, S_jenny_busy, S_jenny_panty_steal,
                    S_jenny_panty_deal, S_jenny_somrak_panty_trade,
                    S_jenny_shower_peep_bed_cuddle, S_jenny_somrak_more_panty,
                    S_jenny_panty_deal_tier_2, S_jenny_somrak_panty_trade_tier_2,
                    S_jenny_debbie_needs_jenny, S_jenny_read_diary,
                    S_jenny_connect_webcam, S_jenny_watch_stream,
                    S_jenny_telescope_spying, S_jenny_debbie_breakfast,
                    S_jenny_breakfast, S_jenny_titty_deal,
                    S_jenny_shower_peep_bed_cuddle_tier_2, S_jenny_hallway_meetup,
                    S_jenny_couch_naughty_time, S_jenny_couch_naughty_time_tier_2,
                    S_jenny_somrak_more_panty_tier_2, S_jenny_panty_deal_tier_3,
                    S_jenny_somrak_panty_trade_tier_3, S_jenny_watch_stream_tier_2,
                    S_jenny_telescope_spying_tier_2, S_jenny_hallway_meetup_focus,
                    S_jenny_shower_peep_bed_cuddle_tier_3, S_jenny_couch_naughty_time_tier_3,
                    S_jenny_somrak_more_panty_tier_3, S_jenny_panty_deal_tier_4,
                    S_jenny_somrak_panty_trade_tier_4, S_jenny_watch_stream_tier_3,
                    S_jenny_telescope_spying_tier_3, S_jenny_shower_peep_bed_cuddle_tier_4,
                    S_jenny_hallway_noises, S_jenny_overhear_caught, S_jenny_cam_show,
                    S_jenny_shower_peep_bed_cuddle_tier_5, S_jenny_help_stream_tier_4,
                    S_jenny_prepare_stream_tier_4,
                    S_jenny_end,
                    )
    return

label jenny_machine_init:
    python:
        M_jenny = Machine("Jenny", default_loc = [[L_home_sisbedroom, L_home_sisbedroom, L_home_sisbedroom, L_home_sisbedroom]],
                          vars = {"door locked": True,
                                  "comp locked": True,
                                  "seen MCs penis": False,
                                  "sex speed": .175,
                                  },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
