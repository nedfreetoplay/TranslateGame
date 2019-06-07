init python:

    T_jenny_hallway = Trigger()
    T_jenny_spied_shower = Trigger()
    T_jenny_altercation_with_debbie = Trigger()
    T_jenny_breakfast_notice = Trigger()
    T_jenny_had_breakfast = Trigger()
    T_jenny_eavesdropped = Trigger()
    T_jenny_took_pictures = Trigger()
    T_jenny_snoop_in_her_room = Trigger()
    T_jenny_looked_at_diary = Trigger()
    T_jenny_looked_at_nightstand = Trigger()
    T_jenny_caught_snooping = Trigger()
    T_jenny_breakfast_notice_2 = Trigger()
    T_jenny_had_breakfast_2 = Trigger()
    T_jenny_pay_for_favors = Trigger()
    T_jenny_get_a_toy = Trigger()
    T_jenny_got_a_toy = Trigger()
    T_jenny_ivy_jane_leaving = Trigger()
    T_jenny_brought_back_toy = Trigger()
    T_jenny_have_breakfast = Trigger()
    T_jenny_catch_her_in_shower = Trigger()
    T_jenny_wait_a_day = Trigger()
    T_jenny_leave_house = Trigger()
    T_jenny_go_at_pinks = Trigger()
    T_jenny_buy_vibrator = Trigger()
    T_jenny_bought_vibrator = Trigger()
    T_jenny_check_laptop = Trigger()
    T_jenny_return_from_shower = Trigger()
    T_jenny_a_real_penis = Trigger()
    T_jenny_checked_pc_for_new_vids = Trigger()
    T_jenny_get_her_a_new_toy = Trigger()
    T_jenny_bought_bad_monster = Trigger()
    T_jenny_gave_bad_monster = Trigger()
    T_jenny_check_new_vid = Trigger()
    T_jenny_checked_new_vid = Trigger()
    T_jenny_talk_to_cedric = Trigger()
    T_jenny_talked_to_cedric = Trigger()
    T_jenny_cedric_didnt_call = Trigger()
    T_jenny_beaten_up_with_dildo = Trigger()
    T_jenny_spied_on_mia = Trigger()
    T_jenny_get_a_mask = Trigger()
    T_jenny_buy_mask = Trigger()
    T_jenny_bought_mask = Trigger()
    T_jenny_delivered_mask = Trigger()
    T_jenny_gave_handjob = Trigger()
    T_jenny_reconciliation_handjob = Trigger()
    T_jenny_gave_footjob  = Trigger()
    T_jenny_start_camshow_blowjob = Trigger()
    T_jenny_done_camshow_blowjob = Trigger()
    T_jenny_reconciliation_blowjob = Trigger()
    T_jenny_spied_on_tammy = Trigger()
    T_jenny_gave_cunni = Trigger()
    T_jenny_go_breakfast = Trigger()
    T_jenny_get_cheerleader_outfit = Trigger()
    T_jenny_got_cheerleader_outfit = Trigger()
    T_jenny_had_cheerleader_sex = Trigger()
    T_jenny_pool_talk = Trigger()
    T_jenny_stalked = Trigger()
    T_jenny_its_mr_bubbles = Trigger()
    T_jenny_movie_date = Trigger()
    T_jenny_righteous_punch = Trigger()
    T_jenny_didnt_sleep_much = Trigger()
    T_jenny_final_breakfast = Trigger()
    T_jenny_end = Trigger()
    T_jenny_diary_clue = Trigger()
    T_jenny_give_necklace = Trigger()

label sister_fsm_init:
    python:

        S_jenny_start = State("start", "I'm living in the same house as she does...")
        S_jenny_shower_spy = State("shower spy", "[jen_name] is a stuck up bitch. She has a nice body though...")
        S_jenny_debbie_altercation = State("altercation", "[jen_name] is not just busting my balls. She seems to get on the nerves of [deb_name] as well.", delay=1)
        S_jenny_breakfast_notice = State("breakfast", "Something smells good downstairs", delay=2)
        S_jenny_have_breakfast = State("breakfast", "I should have some breakfast downstairs.")
        S_jenny_hallway_eavesdropping = State("eavesdropping", "[jen_name] is up to something... I don't know what though.", delay=2)
        S_jenny_sluttygram_pics = State("sluttygram", "I hear [jen_name] eating in the {b}Dining Room{/b} downstairs.", delay=3)
        S_jenny_pics_afterthought = State("", "I can't believe that just happened!")
        S_jenny_snoop_around = State("", "Mmh. I should look for the photos in her room while she showers.")
        S_jenny_snoop_diary = State("", "Can't hurt to check out her diary while I'm here.")
        S_jenny_snoop_nightstand = State("", "Maybe the she keeps the camera in her nightstand.")
        S_jenny_caught_snooping = State("", "{b}[jen_name]{/b} caught me snooping around. It was costly but worth it.")
        S_jenny_breakfast_notice_2 = State("", "Something smells good {b}downstairs{/b}.", delay=3)
        S_jenny_have_breakfast_2 = State("", "Something smells good {b}downstairs{/b}.")
        S_jenny_go_to_her_room = State("", "{b}[jen_name]{/b} told me to go wait in her room for some kind of deal.")
        S_jenny_get_a_toy = State("", "{b}[jen_name]{/b} has a favor to ask me.", delay=2)
        S_jenny_go_to_pink = State("", "{b}[jen_name]{/b} wants a specific toy. She told me {b}Pink{/b}, at the mall, had it.")
        S_jenny_bring_toy_back = State("", "I should bring this {b}Electroclit Light{/b} to {b}[jen_name]{/b}")
        S_jenny_ivy_jane_leave_pink = State("", "That toy is laying on the counter. It should be enough for {b}[jen_name]{/b}.")
        S_jenny_helping_with_breakfast = State("", "{b}[jen_name]{/b} is downstairs. I bet {b}[deb_name]{/b} is fixing her breakfast again...", delay=2)
        S_jenny_have_breakfast_3 = State("", "At this point, I should grab a bite to eat in the {b}Dining Room{/b}")
        S_jenny_confront_her_hallway = State("", "{b}[jen_name]'s{/b} going to the {b}Shower{/b}, maybe I could catch her and confront her.")
        S_jenny_catch_her_leaving = State("", "{b}[jen_name]{/b} is leaving the house right now. Where is she going?", delay=1)
        S_jenny_go_shopping = State("", "Great, now we're heading to the {b}Mall{/b} for some errands...")
        S_jenny_shop_for_toys = State("", "She left me hanging! She said she was going to {b}Pink{/b}. It's upstairs.")
        S_jenny_buy_vibrator = State("", "I have to buy a vibrator. She mentioned the name : {b}UltraVibrator 2000{/b}")
        S_jenny_snooping_laptop_notice = State("")
        S_jenny_snoop_around_for_laptop = State("", "She's in the shower, I should sneak into her room...")
        S_jenny_check_laptop = State("", "That laptop must have some kind of information on [jen_name]'s whereabouts.")
        S_jenny_figure_out_password = State("", "I have to figure out her password. She mentioned it in her diary... I should go at night though.")
        S_jenny_new_video_notice = State("", "Mmmh, I wonder if [jen_name] has posted a new video yet...", delay=3)
        S_jenny_check_for_new_video = State("", "Mmmh, I wonder if [jen_name] has posted a new video yet...")
        S_jenny_checked_for_new_video = State("", "Mmmh, I wonder if [jen_name] has posted a new video yet...")
        S_jenny_buy_bad_monster = State("", "If I buy her a toy, she'll definitely make a new video! What's her favorite toy again?")
        S_jenny_deliver_bad_monster = State("", "Thank god {b}Ivy{/b} had a Bad Monster in stock! I should give that to [jen_name]")
        S_jenny_video_3_uploaded = State("", "I should check if {b}[jen_name]{/b} has uploaded a new video with that bad monster.", delay=1)
        S_jenny_cedric_upset = State("", "I should get some breakfast in the {b}Dining Room{/b}.", delay=2)
        S_jenny_talk_to_cedric = State("", "{b}[jen_name]{/b} wants me to talk to {b}Cedric{/b} at the {b}Gym{/b}.")
        S_jenny_talked_to_cedric = State("", "I should get back home.")
        S_jenny_caught_talking_to_camslut = State("", "I should check on {b}[jen_name]{/b}...", delay=3)
        S_jenny_spy_on_mia_telescope = State("", "I wonder what's mia doing right now...", delay=1)
        S_jenny_get_a_mask_quest = State("", "I should check on {b}[jen_name]{/b} in the afternoon")
        S_jenny_get_a_mask = State("", "{b}[jen_name]{/b} asked me to buy a mask to make camshows with her.")
        S_jenny_buy_mask = State("", "{b}[jen_name]{/b} asked me to buy a mask to make camshows with her.")
        S_jenny_bought_mask = State("", "I should get this back to {b}[jen_name]{/b}")
        S_jenny_come_back_camshow= State("", "I have to come back to {b}[jen_name]{/b} tomorrow to start the camshows.")
        S_jenny_start_camshow_handjob = State("", "{b}[jen_name]{/b} told me to come to her room to start the camshow.")
        S_jenny_pissed_at_handjob = State("", "She's  pissed at me because of what happened during the camshow. I should try and talk to her.")
        S_jenny_catch_her_jilling = State("", "I should check the living room at night", delay=2)
        S_jenny_morning_visit = State("", "I should get some sleep now...")
        S_jenny_start_camshow_blowjob = State("", "{b}[jen_name]{/b} asked me to come to her room in the afternoon.")
        S_jenny_pissed_at_blowjob = State("", "She's  pissed at me because of what happened during the camshow. I should try and talk to her.")
        S_jenny_perv_on_tammy = State("", "I wonder what's Mrs Johnson's routine is like in the mornings", delay=1)
        S_jenny_give_cunni = State("", "")
        S_jenny_bedroom_intrusion = State("", "", delay=1)
        S_jenny_have_breakfast_4 = State("", "{b}[jen_name]{/b} is waiting downstairs for breakfast")
        S_jenny_get_cheerleader_outfit = State("", "{b}[jen_name]{/b} needs me to pick up her old cheerleader outfit in the attic.")
        S_jenny_cheerleader_sex = State("", "I got the cheerleader outfit, I should bring it to her.")
        S_jenny_want_some_breakfast = State("", "I should check on [jen_name] this weekend.", delay=1)
        S_jenny_pool_talk = State("", "[deb_name] asked me to talk to [jen_name]. She's by the pool on the weekends.")
        S_jenny_find_stalker = State("", "I have to find that creep! I followed him back to the mall.")
        S_jenny_ask_movie_date = State("", "Mr Bubbles has to give out his apology to [jen_name]")
        S_jenny_movie_date = State("", "Mr Bubbles has to give out his apology to [jen_name]")
        S_jenny_night_time_sex = State("", "[jen_name] told me to expect a surprise tonight, I can't wait!")
        S_jenny_weird_relationship = State("", "", delay=1)
        S_jenny_final_breakfast = State("", "{b}[jen_name]{/b} is having breakfast downstairs, I should go talk to her.")
        S_jenny_end = State("end")
        S_jenny_hallway_talk = State("", "I should check on {b}[jen_name]{/b}", delay=3)
        S_jenny_diary_clue = State("", "I really want her to warm up to me, I should check her dairy for ideas.")
        S_jenny_necklace_rebutal = State("", "{b}[jen_name]{/b} refused my gift, but she offered an alternative.")


        S_jenny_start.add(T_jenny_hallway, S_jenny_shower_spy)
        S_jenny_shower_spy.add(T_jenny_spied_shower, S_jenny_debbie_altercation)
        S_jenny_debbie_altercation.add(T_jenny_altercation_with_debbie, S_jenny_breakfast_notice)
        S_jenny_breakfast_notice.add(T_jenny_breakfast_notice, S_jenny_have_breakfast)
        S_jenny_have_breakfast.add(T_jenny_had_breakfast, S_jenny_hallway_eavesdropping)
        S_jenny_hallway_eavesdropping.add(T_jenny_eavesdropped, S_jenny_sluttygram_pics)
        S_jenny_sluttygram_pics.add(T_jenny_took_pictures, S_jenny_pics_afterthought)
        S_jenny_pics_afterthought.add(T_jenny_snoop_in_her_room, S_jenny_snoop_around,
                              actions = ["location", {"place": L_home_shower},
                                         "force", {"tod": 0},
                                         "exec", L_home_sisbedroom.unlock,
                                         "setinshower", M_jenny,
                                         ])
        S_jenny_snoop_around.add(T_jenny_looked_at_diary, S_jenny_snoop_nightstand)
        S_jenny_snoop_around.add(T_jenny_looked_at_nightstand, S_jenny_snoop_diary)
        S_jenny_snoop_nightstand.add(T_jenny_looked_at_nightstand, S_jenny_caught_snooping)
        S_jenny_snoop_diary.add(T_jenny_looked_at_diary, S_jenny_caught_snooping)
        S_jenny_caught_snooping.add(T_jenny_caught_snooping, S_jenny_breakfast_notice_2,
                              actions = ["unforce", None,
                                         "set", [M_player, "jerk jenny"],
                                         'assign', ("diary_index", 6)])
        S_jenny_breakfast_notice_2.add(T_jenny_breakfast_notice_2, S_jenny_have_breakfast_2,
                              actions = ["location", {"place": L_home_diningroom},
                                         "force", {"tod": 0},
                                         ])
        S_jenny_have_breakfast_2.add(T_jenny_had_breakfast_2, S_jenny_go_to_her_room,
                              actions=["unforce", None,
                                       "location", {"place":L_home_sisbedroom},
                                       "force", {"tod": [0, 1, 2, 3]}])
        S_jenny_go_to_her_room.add(T_jenny_pay_for_favors, S_jenny_get_a_toy, actions=["unforce", None])
        S_jenny_get_a_toy.add(T_jenny_get_a_toy, S_jenny_go_to_pink)
        S_jenny_go_to_pink.add(T_jenny_ivy_jane_leaving, S_jenny_ivy_jane_leave_pink,
                              actions = ["location", [M_ivy, {"place": L_NULL}],
                                         "force", [M_ivy, {"flag": True}],
                                        ])
        S_jenny_ivy_jane_leave_pink.add(T_jenny_got_a_toy, S_jenny_bring_toy_back, actions=["unforce", M_ivy])
        S_jenny_bring_toy_back.add(T_jenny_brought_back_toy, S_jenny_helping_with_breakfast)

        S_jenny_helping_with_breakfast.add(T_jenny_have_breakfast, S_jenny_have_breakfast_3)
        S_jenny_helping_with_breakfast.add(T_jenny_catch_her_in_shower, S_jenny_confront_her_hallway)
        S_jenny_have_breakfast_3.add(T_jenny_wait_a_day, S_jenny_catch_her_leaving)
        S_jenny_confront_her_hallway.add(T_jenny_wait_a_day, S_jenny_catch_her_leaving)
        S_jenny_catch_her_leaving.add(T_jenny_leave_house, S_jenny_go_shopping,
                              actions = ["location", {"place": L_NULL},
                                         "force", {"tod": [0,1]},
                                         ])
        S_jenny_go_shopping.add(T_jenny_go_at_pinks, S_jenny_shop_for_toys)
        S_jenny_shop_for_toys.add(T_jenny_buy_vibrator, S_jenny_buy_vibrator, actions=["setcannotleave", L_pink])
        S_jenny_buy_vibrator.add(T_jenny_bought_vibrator, S_jenny_snooping_laptop_notice, actions=["unforce", None, "setcanleave", L_pink, "assign", ("diary_index", 9)])


        S_jenny_snooping_laptop_notice.add(T_player_woke_up, S_jenny_snoop_around_for_laptop, actions=["assign", ("diary_index", 11)])
        S_jenny_snoop_around_for_laptop.add(T_jenny_check_laptop, S_jenny_check_laptop)
        S_jenny_check_laptop.add(T_jenny_return_from_shower, S_jenny_figure_out_password,
                              actions = ["force", {"tod":[2]},
                                         "location", {"place":L_NULL}])
        S_jenny_figure_out_password.add(T_jenny_a_real_penis, S_jenny_new_video_notice,
                              actions = ["unforce", None])

        S_jenny_new_video_notice.add(T_player_woke_up, S_jenny_check_for_new_video)
        S_jenny_check_for_new_video.add(T_jenny_checked_pc_for_new_vids, S_jenny_checked_for_new_video)
        S_jenny_checked_for_new_video.add(T_jenny_get_her_a_new_toy, S_jenny_buy_bad_monster,
            actions=('condition', ('player.has_item("badmonster")',
                                   (('trigger', T_jenny_bought_bad_monster)), ())))
        S_jenny_buy_bad_monster.add(T_jenny_bought_bad_monster, S_jenny_deliver_bad_monster)
        S_jenny_deliver_bad_monster.add(T_jenny_gave_bad_monster, S_jenny_video_3_uploaded)
        S_jenny_video_3_uploaded.add(T_jenny_checked_new_vid, S_jenny_cedric_upset, actions=["assign", ("diary_index", 12)])

        S_jenny_cedric_upset.add(T_jenny_talk_to_cedric, S_jenny_talk_to_cedric)
        S_jenny_talk_to_cedric.add(T_jenny_talked_to_cedric, S_jenny_talked_to_cedric)
        S_jenny_talked_to_cedric.add(T_jenny_cedric_didnt_call, S_jenny_caught_talking_to_camslut, actions=["assign", ("diary_index", 13)])

        S_jenny_caught_talking_to_camslut.add(T_jenny_beaten_up_with_dildo, S_jenny_spy_on_mia_telescope, actions=["assign", ("diary_index", 14)])

        S_jenny_spy_on_mia_telescope.add(T_jenny_spied_on_mia, S_jenny_get_a_mask_quest)
        S_jenny_get_a_mask_quest.add(T_jenny_get_a_mask, S_jenny_get_a_mask,
                              actions = ["location", [M_rump, {"place": L_NULL, "dow":[5, 6]}],
                                         "force", [M_rump, {"tod": [0, 1]}],
                                         ])
        S_jenny_get_a_mask.add(T_jenny_buy_mask, S_jenny_buy_mask,
                              actions = ["unforce", M_rump,
                                         ])
        S_jenny_buy_mask.add(T_jenny_bought_mask, S_jenny_bought_mask)
        S_jenny_bought_mask.add(T_jenny_delivered_mask, S_jenny_come_back_camshow)
        S_jenny_come_back_camshow.add(T_all_sleep, S_jenny_start_camshow_handjob, actions=["assign", ("diary_index", 15)])

        S_jenny_start_camshow_handjob.add(T_jenny_gave_handjob, S_jenny_pissed_at_handjob)
        S_jenny_pissed_at_handjob.add(T_jenny_reconciliation_handjob, S_jenny_catch_her_jilling, actions=["assign", ("diary_index", 16)])

        S_jenny_catch_her_jilling.add(T_jenny_gave_footjob, S_jenny_morning_visit)
        S_jenny_morning_visit.add(T_jenny_start_camshow_blowjob, S_jenny_start_camshow_blowjob)
        S_jenny_start_camshow_blowjob.add(T_jenny_done_camshow_blowjob, S_jenny_pissed_at_blowjob)
        S_jenny_pissed_at_blowjob.add(T_jenny_reconciliation_blowjob, S_jenny_perv_on_tammy)

        S_jenny_perv_on_tammy.add(T_jenny_spied_on_tammy, S_jenny_give_cunni)
        S_jenny_give_cunni.add(T_jenny_gave_cunni, S_jenny_bedroom_intrusion, actions=["assign", ("diary_index", 18)])

        S_jenny_bedroom_intrusion.add(T_jenny_go_breakfast, S_jenny_have_breakfast_4)
        S_jenny_have_breakfast_4.add(T_jenny_get_cheerleader_outfit, S_jenny_get_cheerleader_outfit)
        S_jenny_get_cheerleader_outfit.add(T_jenny_got_cheerleader_outfit, S_jenny_cheerleader_sex)
        S_jenny_cheerleader_sex.add(T_jenny_had_cheerleader_sex, S_jenny_want_some_breakfast)

        S_jenny_want_some_breakfast.add(T_jenny_pool_talk, S_jenny_pool_talk)
        S_jenny_pool_talk.add(T_jenny_stalked, S_jenny_find_stalker)
        S_jenny_find_stalker.add(T_jenny_its_mr_bubbles, S_jenny_ask_movie_date)
        S_jenny_ask_movie_date.add(T_jenny_movie_date, S_jenny_movie_date)
        S_jenny_movie_date.add(T_jenny_righteous_punch, S_jenny_night_time_sex, actions=["assign", ('sneak_in_chance', 100)])
        S_jenny_night_time_sex.add(T_jenny_didnt_sleep_much, S_jenny_weird_relationship,
                                   actions=["assign", ("sneak_in_chance", 5)])

        S_jenny_weird_relationship.add(T_jenny_final_breakfast, S_jenny_final_breakfast)
        S_jenny_final_breakfast.add(T_jenny_end, S_jenny_end,
                                   actions=["exec", A_prolific_camshow.unlock,
                                            "assign", ("diary_index", 27)])

        S_jenny_end.add(T_all_sleep, S_jenny_hallway_talk, actions=["assign", ("diary_index", 28)])
        S_jenny_hallway_talk.add(T_jenny_diary_clue, S_jenny_diary_clue)
        S_jenny_diary_clue.add(T_jenny_give_necklace, S_jenny_necklace_rebutal, actions=["assign", ("diary_index", 29)])

        M_jenny.add(S_jenny_start, S_jenny_shower_spy, S_jenny_debbie_altercation,
                    S_jenny_breakfast_notice, S_jenny_have_breakfast,
                    S_jenny_hallway_eavesdropping,
                    S_jenny_sluttygram_pics,
                    S_jenny_pics_afterthought, S_jenny_snoop_around, S_jenny_snoop_diary, S_jenny_snoop_nightstand, S_jenny_caught_snooping,
                    S_jenny_breakfast_notice_2, S_jenny_have_breakfast_2, S_jenny_go_to_her_room,
                    S_jenny_get_a_toy, S_jenny_go_to_pink, S_jenny_ivy_jane_leave_pink, S_jenny_bring_toy_back,
                    S_jenny_helping_with_breakfast, S_jenny_have_breakfast_3, S_jenny_confront_her_hallway,
                    S_jenny_catch_her_leaving, S_jenny_go_shopping, S_jenny_shop_for_toys, S_jenny_buy_vibrator,
                    S_jenny_snooping_laptop_notice, S_jenny_snoop_around_for_laptop, S_jenny_check_laptop, S_jenny_figure_out_password,
                    S_jenny_new_video_notice, S_jenny_check_for_new_video, S_jenny_checked_for_new_video, S_jenny_buy_bad_monster,
                    S_jenny_deliver_bad_monster, S_jenny_video_3_uploaded,
                    S_jenny_cedric_upset, S_jenny_talk_to_cedric, S_jenny_talked_to_cedric,
                    S_jenny_caught_talking_to_camslut,
                    S_jenny_spy_on_mia_telescope,
                    S_jenny_get_a_mask_quest, S_jenny_get_a_mask, S_jenny_buy_mask, S_jenny_bought_mask, S_jenny_come_back_camshow,
                    S_jenny_start_camshow_handjob, S_jenny_pissed_at_handjob,
                    S_jenny_catch_her_jilling, S_jenny_morning_visit, S_jenny_start_camshow_blowjob, S_jenny_pissed_at_blowjob,
                    S_jenny_perv_on_tammy, S_jenny_give_cunni,
                    S_jenny_bedroom_intrusion, S_jenny_have_breakfast_4, S_jenny_get_cheerleader_outfit, S_jenny_cheerleader_sex,
                    S_jenny_want_some_breakfast, S_jenny_pool_talk, S_jenny_find_stalker,
                    S_jenny_ask_movie_date, S_jenny_movie_date, S_jenny_night_time_sex,
                    S_jenny_weird_relationship, S_jenny_final_breakfast,
                    S_jenny_end,
                    S_jenny_hallway_talk, S_jenny_diary_clue, S_jenny_necklace_rebutal,
                    )
        M_jenny.add_action(T_all_sleep, ["assign", ("forced_sneak_in_chance", 0),
                                         "assign", ("had_couch_sex", False),
                                         "assign", ('force_couch_sex', False),
                                         "assign", ('girlfriend_in_progress', False)])
        M_jenny.pregnancy.add_action("first", 2, ["assign", ("jenny_pregnant_page", "M_jenny.get('diary_index') + 1")])
        M_jenny.pregnancy.add_action("first", 6, ["assign", ("jenny_kid_page", "M_jenny.get('diary_index') + 1")])
    return

label jenny_machine_init:
    python:
        M_jenny = Machine("jenny", default_loc = [[L_home_diningroom, L_home_sisbedroom, L_home_sisbedroom, L_home_sisbedroom],
                                                  [L_home_backyard, L_home_sisbedroom, L_home_sisbedroom, L_home_sisbedroom]],
                          vars = {"door locked": True,
                                  "comp locked": True,
                                  "seen MCs penis": False,
                                  "sex speed": .175,
                                  "first_shower": True,
                                  'rng': 0,
                                  "diary_index": 5,
                                  "dominance": 0,
                                  "j10_caught_her_leaving":False,
                                  "hacked pc": False,
                                  "watched_video_1": False,
                                  "watched_video_2": False,
                                  "watched_video_3": False,
                                  "cam show mask": True,
                                  'sit': True,
                                  'sneak_in_chance': 0,
                                  'forced_sneak_in_chance': 0,
                                  'first_shower_time': True,
                                  'jenny_debbie_acknowlegement': False,
                                  'jenny_got_first_baby': False,
                                  'seen_in_shower': False,
                                  'seen_in_shower_pregnant': False,
                                  "didnt_see_first_baby_dialogue": True,
                                  "couch_sex_first": True,
                                  "had_couch_sex": False,
                                  'teasin_before_sex': False,
                                  'hack_pc_notice':False,
                                  'went_to_her_room': False,
                                  'first_time_deep_bj': True,
                                  'jenny_bj_deep': True,
                                  'first_sex_dining': True,
                                  'force_couch_sex': False,
                                  'first_sex_pool': True,
                                  'pool_clothes': True,
                                  'jenny_bed_cum_inside': True,
                                  'jenny_girlfriend_first_time': True,
                                  'girlfriend_time': False,
                                  'jenny_pregnant_page': False,
                                  'jenny_kid_page': False,
                                  'bed_sex_first_time': True,
                                  'jenny_bed_cum_inside':False,
                                  'checked_diary_j22': False,
                                  'girlfriend_in_progress': False,
                                  'figure_out_pass_dialogue': False,
                                  },
        )
        M_jenny.set_priority(1)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
