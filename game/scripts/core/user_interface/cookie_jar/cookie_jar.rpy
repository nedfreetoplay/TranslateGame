init python:
    def fix_cookie_jar_paths(cookie):
        idle = cookie["idle"]
        locked_idle = cookie["locked_idle"]
        idle = idle.split("/")
        locked_idle = locked_idle.split("/")
        gallery_image = cookie["gallery_image"].split("/")
        cookie["idle"] = "cookie_jar/" + idle[1]
        cookie["locked_idle"] = "cookie_jar/" + locked_idle[1]
        cookie["gallery_image"] = "cookie_jar/" + gallery_image[1]
        return

    if persistent.cookie_jar == None:
        persistent.cookie_jar = {}
    else:
        for key, cookie in persistent.cookie_jar.items():
            fix_cookie_jar_paths(cookie)

    if "Debbie" not in persistent.cookie_jar:
        persistent.cookie_jar["Debbie"] = {"idle": "cookie_jar/cookie_jar_01.png",
                                           "locked_idle": "cookie_jar/cookie_jar_01_locked.png",
                                           "unlocked": False,
                                           "order": "01",
                                           "gallery": {},
                                           "gallery_image": "cookie_jar/cookie_jar_box_01_",
        }

    persistent.cookie_jar["Debbie"]["gallery_total"] = 12

    persistent.cookie_jar["Debbie"]["gallery_labels"] = {"01_label": "mom_spy",
                                                         "02_label": "replay_mom_panties",
                                                         "03_label": "mom_night_suck",
                                                         "04_label": "mom_midnight_swim",
                                                         "05_label": "debbie_car_sex",
                                                         "06_label": "mom_night_sex_replay",
                                                         "07_label": "shower_mom_sex_replay",
                                                         "08_label": "mom_couch_sex_replay",
                                                         "09_label": "mom_kitchen_replay",
                                                         "10_label": "mom_mc_sexvisit",
                                                         "11_label": "mom_sex_replay",
                                                         "12_label": "mom_basement_replay",
    }

    if "Jenny" not in persistent.cookie_jar:
        persistent.cookie_jar["Jenny"] = {"idle": "cookie_jar/cookie_jar_02.png",
                                          "locked_idle": "cookie_jar/cookie_jar_02_locked.png",
                                          "unlocked": False,
                                          "order": "02",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_02_",
        }

    persistent.cookie_jar["Jenny"]["gallery_total"] = 17

    persistent.cookie_jar["Jenny"]["gallery_labels"] = {"01_label": "hallway_jenny_hallway_eavesdropping",
                                                        "02_label": "jenny_taking_pictures_replay",
                                                        "03_label": "jenny_computer_video_1",
                                                        "04_label": "jenny_computer_video_2",
                                                        "05_label": "jenny_computer_video_3",
                                                        "06_label": "hallway_jenny_caught_talking_to_camslut",
                                                        "07_label": "button_jenny_start_camshow_handjob",
                                                        "08_label": "entrance_jenny_catch_her_jilling",
                                                        "09_label": "sis_bedroom_jenny_start_camshow_blowjob",
                                                        "10_label": "bedroom_jenny_give_cunni",
                                                        "11_label": "sis_bedroom_jenny_cheerleader_sex",
                                                        "12_label": "jenny_mc_room_sex_on_sleep",
                                                        "13_label": "shower_jenny_blowjob_intro_first",
                                                        "14_label": "jenny_shower_sex_intro_replay",
                                                        "15_label": "button_jenny_fool_around_diningroom_first",
                                                        "16_label": "button_jenny_fool_around_pool_first",
                                                        "17_label": "jenny_bed_night_sex_intro",
    }

    if "Diane" not in persistent.cookie_jar:
        persistent.cookie_jar["Diane"] = {"idle": "cookie_jar/cookie_jar_03.png",
                                          "locked_idle": "cookie_jar/cookie_jar_03_locked.png",
                                          "unlocked": False,
                                          "order": "03",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_03_",
        }

    persistent.cookie_jar["Diane"]["gallery_total"] = 7

    persistent.cookie_jar["Diane"]["gallery_labels"] = {"01_label": "dianes_kitchen_diane_look_in_kitchen",
                                                        "02_label": "dianes_garden_diane_drunk_like_a_sailor",
                                                        "03_label": "kitchen_diane_dinner",
                                                        "04_label": "dianes_dialogue_breastfeed",
                                                        "05_label": "diane_cucumber_start",
                                                        "06_label": "diane_sex_breed_start",
                                                        "07_label": "diane_debbie_sex_start",
    }


    if "Mrs Johnson" not in persistent.cookie_jar:
        persistent.cookie_jar["Mrs Johnson"] = {"idle": "cookie_jar/cookie_jar_04.png",
                                                "locked_idle": "cookie_jar/cookie_jar_04_locked.png",
                                                "unlocked": False,
                                                "order": "04",
                                                "gallery": {},
                                                "gallery_image": "cookie_jar/cookie_jar_box_04_",
        }

    persistent.cookie_jar["Mrs Johnson"]["gallery_total"] = 5

    persistent.cookie_jar["Mrs Johnson"]["gallery_labels"] = {"01_label": "mrsj_afterpoker_fun",
                                                              "02_label": "mrsj_private_yoga_perv_jenny_replay",
                                                              "03_label": "mrsj_erik_cunni_perv_jenny_replay",
                                                              "04_label": "mrsj_3some",
                                                              "05_label": "mrsj_private_yoga",
    }

    if "Mia" not in persistent.cookie_jar:
        persistent.cookie_jar["Mia"] = {"idle": "cookie_jar/cookie_jar_05.png",
                                        "locked_idle": "cookie_jar/cookie_jar_05_locked.png",
                                        "unlocked": False,
                                        "order": "05",
                                        "gallery": {},
                                        "gallery_image": "cookie_jar/cookie_jar_box_05_",
        }

    persistent.cookie_jar["Mia"]["gallery_total"] = 3

    persistent.cookie_jar["Mia"]["gallery_labels"] = {"01_label": "telescope_mia_night_2",
                                                      "02_label": "telescope_mia_sister_spying",
                                                      "03_label": "mia_bedroom_sex",
    }

    if "Helen" not in persistent.cookie_jar:
        persistent.cookie_jar["Helen"] = {"idle": "cookie_jar/cookie_jar_06.png",
                                          "locked_idle": "cookie_jar/cookie_jar_06_locked.png",
                                          "unlocked": False,
                                          "order": "06",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_06_",
        }

    persistent.cookie_jar["Helen"]["gallery_total"] = 2

    persistent.cookie_jar["Helen"]["gallery_labels"] = {"01_label": "helen_baton_replay",
                                                        "02_label": "helen_bedroom_sex",
    }

    if "Angelica" not in persistent.cookie_jar:
        persistent.cookie_jar["Angelica"] = {"idle": "cookie_jar/cookie_jar_07.png",
                                             "locked_idle": "cookie_jar/cookie_jar_07_locked.png",
                                             "unlocked": False,
                                             "order": "07",
                                             "gallery": {},
                                             "gallery_image": "cookie_jar/cookie_jar_box_07_",
        }

    persistent.cookie_jar["Angelica"]["gallery_total"] = 3

    persistent.cookie_jar["Angelica"]["gallery_labels"] = {"01_label": "helen_sacrement_training_part2",
                                                           "02_label": "helen_final_sacrament",
                                                           "03_label": "helen_final_mc",
    }

    if "Ivy" not in persistent.cookie_jar:
        persistent.cookie_jar["Ivy"] = {"idle": "cookie_jar/cookie_jar_08.png",
                                        "locked_idle": "cookie_jar/cookie_jar_08_locked.png",
                                        "unlocked": False,
                                        "order": "08",
                                        "gallery": {},
                                        "gallery_image": "cookie_jar/cookie_jar_box_08_",
        }

    persistent.cookie_jar["Ivy"]["gallery_total"] = 4

    persistent.cookie_jar["Ivy"]["gallery_labels"] = {"01_label": "ivy_paizuri",
                                                      "02_label": "ivy_blowjob",
                                                      "03_label": "ivy_reverse_cowgirl",
                                                      "04_label": "ivy_cowgirl",
    }

    if "June" not in persistent.cookie_jar:
        persistent.cookie_jar["June"] = {"idle": "cookie_jar/cookie_jar_09.png",
                                         "locked_idle": "cookie_jar/cookie_jar_09_locked.png",
                                         "unlocked": False,
                                         "order": "09",
                                         "gallery": {},
                                         "gallery_image": "cookie_jar/cookie_jar_box_09_",
        }

    persistent.cookie_jar["June"]["gallery_total"] = 1

    persistent.cookie_jar["June"]["gallery_labels"] = {"01_label": "june_cosplay_replay",
    }

    if "Cassie" not in persistent.cookie_jar:
        persistent.cookie_jar["Cassie"] = {"idle": "cookie_jar/cookie_jar_10.png",
                                           "locked_idle": "cookie_jar/cookie_jar_10_locked.png",
                                           "unlocked": False,
                                           "order": "10",
                                           "gallery": {},
                                           "gallery_image": "cookie_jar/cookie_jar_box_10_",
        }

    persistent.cookie_jar["Cassie"]["gallery_total"] = 1

    persistent.cookie_jar["Cassie"]["gallery_labels"] = {"01_label": "medic_room_cassie_replay",
    }

    if "Roz" not in persistent.cookie_jar:
        persistent.cookie_jar["Roz"] = {"idle": "cookie_jar/cookie_jar_11.png",
                                        "locked_idle": "cookie_jar/cookie_jar_11_locked.png",
                                        "unlocked": False,
                                        "order": "11",
                                        "gallery": {},
                                        "gallery_image": "cookie_jar/cookie_jar_box_11_",
        }

    persistent.cookie_jar["Roz"]["gallery_total"] = 2

    persistent.cookie_jar["Roz"]["gallery_labels"] = {"01_label": "roz_storage_sex",
                                                      "02_label": "elevator_priya_check_pregnax",
    }

    if "Aqua" not in persistent.cookie_jar:
        persistent.cookie_jar["Aqua"] = {"idle": "cookie_jar/cookie_jar_12.png",
                                         "locked_idle": "cookie_jar/cookie_jar_12_locked.png",
                                         "unlocked": False,
                                         "order": "12",
                                         "gallery": {},
                                         "gallery_image": "cookie_jar/cookie_jar_box_12_",
        }

    persistent.cookie_jar["Aqua"]["gallery_total"] = 2

    persistent.cookie_jar["Aqua"]["gallery_labels"] = {"01_label": "aqua_sex_replay",
                                                       "02_label": "aqua_succ_replay",
    }

    if "Rump" not in persistent.cookie_jar:
        persistent.cookie_jar["Rump"] = {"idle": "cookie_jar/cookie_jar_13.png",
                                         "locked_idle": "cookie_jar/cookie_jar_13_locked.png",
                                         "unlocked": False,
                                         "order": "13",
                                         "gallery": {},
                                         "gallery_image": "cookie_jar/cookie_jar_box_13_",
        }

    persistent.cookie_jar["Rump"]["gallery_total"] = 1

    persistent.cookie_jar["Rump"]["gallery_labels"] = {"01_label": "rump_toilets_stall",
    }

    if "Judith" not in persistent.cookie_jar:
        persistent.cookie_jar["Judith"] = {"idle": "cookie_jar/cookie_jar_14.png",
                                            "locked_idle": "cookie_jar/cookie_jar_14_locked.png",
                                            "unlocked": False,
                                            "order": "14",
                                            "gallery": {},
                                            "gallery_image": "cookie_jar/cookie_jar_box_14_",
        }

    persistent.cookie_jar["Judith"]["gallery_total"] = 2

    persistent.cookie_jar["Judith"]["gallery_labels"] = {"01_label": "boys_lockerroom_judith_changing",
                                                         "02_label": "judith_toilet_replay",
    }

    if "Bissette" not in persistent.cookie_jar:
        persistent.cookie_jar["Bissette"] = {"idle": "cookie_jar/cookie_jar_15.png",
                                             "locked_idle": "cookie_jar/cookie_jar_15_locked.png",
                                             "unlocked": False,
                                             "order": "15",
                                             "gallery": {},
                                             "gallery_image": "cookie_jar/cookie_jar_box_15_",
        }

    persistent.cookie_jar["Bissette"]["gallery_total"] = 2

    persistent.cookie_jar["Bissette"]["gallery_labels"] = {"01_label": "french_classroom_bissette_assignment_replay",
                                                           "02_label": "bissettes_office_night_visit_replay",
    }

    if "Dewitt" not in persistent.cookie_jar:
        persistent.cookie_jar["Dewitt"] = {"idle": "cookie_jar/cookie_jar_16.png",
                                           "locked_idle": "cookie_jar/cookie_jar_16_locked.png",
                                           "unlocked": False,
                                           "order": "16",
                                           "gallery": {},
                                           "gallery_image": "cookie_jar/cookie_jar_box_16_",
        }

    persistent.cookie_jar["Dewitt"]["gallery_total"] = 3

    persistent.cookie_jar["Dewitt"]["gallery_labels"] = {"01_label": "dewitts_office_dewitt_office_reward",
                                                         "02_label": "guitar_hero_minigame_talent_show_pass",
                                                         "03_label": "dewitt_office_dewitt_night_visit",
    }

    if "Ross" not in persistent.cookie_jar:
        persistent.cookie_jar["Ross"] = {"idle": "cookie_jar/cookie_jar_17.png",
                                         "locked_idle": "cookie_jar/cookie_jar_17_locked.png",
                                         "unlocked": False,
                                         "order": "17",
                                         "gallery": {},
                                         "gallery_image": "cookie_jar/cookie_jar_box_17_",
        }

    persistent.cookie_jar["Ross"]["gallery_total"] = 2

    persistent.cookie_jar["Ross"]["gallery_labels"] = {"01_label": "button_ross_found_model",
                                                       "02_label": "ross_hscene_start",
    }

    if "Okita" not in persistent.cookie_jar:
        persistent.cookie_jar["Okita"] = {"idle": "cookie_jar/cookie_jar_18.png",
                                          "locked_idle": "cookie_jar/cookie_jar_18_locked.png",
                                          "unlocked": False,
                                          "order": "18",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_18_",
        }

    persistent.cookie_jar["Okita"]["gallery_total"] = 5

    persistent.cookie_jar["Okita"]["gallery_labels"] = {"01_label": "science_classroom_okita_has_glasses_int_pass",
                                                        "02_label": "okitas_office_okita_xray_perving",
                                                        "03_label": "button_okita_tinkered_belt",
                                                        "04_label": "okitas_office_extract_cum",
                                                        "05_label": "okita_pre_hscene_repeatable",
    }

    if "Anna" not in persistent.cookie_jar:
        persistent.cookie_jar["Anna"] = {"idle": "cookie_jar/cookie_jar_19.png",
                                         "locked_idle": "cookie_jar/cookie_jar_19_locked.png",
                                         "unlocked": False,
                                         "order": "19",
                                         "gallery": {},
                                         "gallery_image": "cookie_jar/cookie_jar_box_19_",
        }

    persistent.cookie_jar["Anna"]["gallery_total"] = 1

    persistent.cookie_jar["Anna"]["gallery_labels"] = {"01_label": "anna_yoga_lesson",
    }

    if "Roxxy" not in persistent.cookie_jar:
        persistent.cookie_jar["Roxxy"] = {"idle": "cookie_jar/cookie_jar_20.png",
                                          "locked_idle": "cookie_jar/cookie_jar_20_locked.png",
                                          "unlocked": False,
                                          "order": "20",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_20_",
        }

    persistent.cookie_jar["Roxxy"]["gallery_total"] = 8

    persistent.cookie_jar["Roxxy"]["gallery_labels"] = {"01_label": "roxxy_shower_replay",
                                                        "02_label": "jennys_bedroom_bissette_roxxy_jenny_spying",
                                                        "03_label": "roxxy_locker_rub_hscene_replay",
                                                        "04_label": "roxxy_massage_hscene_replay",
                                                        "05_label": "roxxy_locker_fuck_hscene_replay",
                                                        "06_label": "roxxy_bedroom_fuck_hscene_replay",
                                                        "07_label": "beach_roxxy_solo_replay",
                                                        "08_label": "beach_mc_4some_roxxy_replay",
    }

    if "Latina Twins" not in persistent.cookie_jar:
        persistent.cookie_jar["Latina Twins"] = {"idle": "cookie_jar/cookie_jar_21.png",
                                                 "locked_idle": "cookie_jar/cookie_jar_21_locked.png",
                                                 "unlocked": False,
                                                 "order": "21",
                                                 "gallery": {},
                                                 "gallery_image": "cookie_jar/cookie_jar_box_21_",
        }

    persistent.cookie_jar["Latina Twins"]["gallery_total"] = 2

    persistent.cookie_jar["Latina Twins"]["gallery_labels"] = {"01_label": "latinas_dialogue_shower",
                                                               "02_label": "latinas_shower_dialogue",
    }

    if "Jane" not in persistent.cookie_jar:
        persistent.cookie_jar["Jane"] = {"idle": "cookie_jar/cookie_jar_22.png",
                                         "locked_idle": "cookie_jar/cookie_jar_22_locked.png",
                                         "unlocked": False,
                                         "order": "22",
                                         "gallery": {},
                                         "gallery_image": "cookie_jar/cookie_jar_box_22_",
        }

    persistent.cookie_jar["Jane"]["gallery_total"] = 1

    persistent.cookie_jar["Jane"]["gallery_labels"] = {"01_label": "backroom_dialogue",
    }

    if "Annie" not in persistent.cookie_jar:
        persistent.cookie_jar["Annie"] = {"idle": "cookie_jar/cookie_jar_23.png",
                                          "locked_idle": "cookie_jar/cookie_jar_23_locked.png",
                                          "unlocked": False,
                                          "order": "23",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_23_",
        }

    persistent.cookie_jar["Annie"]["gallery_total"] = 2

    persistent.cookie_jar["Annie"]["gallery_labels"] = {"01_label": "principals_office_annie_trouble",
                                                        "02_label": "art_minigame_done_dialogue",
    }

    if "Eve" not in persistent.cookie_jar:
        persistent.cookie_jar["Eve"] = {"idle": "cookie_jar/cookie_jar_24.png",
                                          "locked_idle": "cookie_jar/cookie_jar_24_locked.png",
                                          "unlocked": False,
                                          "order": "24",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_24_",
        }

    persistent.cookie_jar["Eve"]["gallery_total"] = 1

    persistent.cookie_jar["Eve"]["gallery_labels"] = {"01_label": "guitar_hero_minigame_karaoke_pass",
    }

    if "Becca & Missy" not in persistent.cookie_jar:
        persistent.cookie_jar["Becca & Missy"] = {"idle": "cookie_jar/cookie_jar_25.png",
                                                  "locked_idle": "cookie_jar/cookie_jar_25_locked.png",
                                                  "unlocked": False,
                                                  "order": "25",
                                                  "gallery": {},
                                                  "gallery_image": "cookie_jar/cookie_jar_box_25_",
        }

    persistent.cookie_jar["Becca & Missy"]["gallery_total"] = 4

    persistent.cookie_jar["Becca & Missy"]["gallery_labels"] = {"01_label": "beach_missy_solo_replay",
                                                                "02_label": "beach_becca_solo_replay",
                                                                "03_label": "beach_mc_4some_missy_replay",
                                                                "04_label": "beach_mc_4some_becca_replay",
    }

    if "Crystal" not in persistent.cookie_jar:
        persistent.cookie_jar["Crystal"] = {"idle": "cookie_jar/cookie_jar_26.png",
                                            "locked_idle": "cookie_jar/cookie_jar_26_locked.png",
                                            "unlocked": False,
                                            "order": "26",
                                            "gallery": {},
                                            "gallery_image": "cookie_jar/cookie_jar_box_26_",
        }

    persistent.cookie_jar["Crystal"]["gallery_total"] = 1

    persistent.cookie_jar["Crystal"]["gallery_labels"] = {"01_label": "crystal_hscene_replay",
    }
    if "Micoe" not in persistent.cookie_jar:
        persistent.cookie_jar["Micoe"] = {"idle": "cookie_jar/cookie_jar_27.png",
                                          "locked_idle": "cookie_jar/cookie_jar_27_locked.png",
                                          "unlocked": False,
                                          "order": "27",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_27_",
        }

    persistent.cookie_jar["Micoe"]["gallery_total"] = 1

    persistent.cookie_jar["Micoe"]["gallery_labels"] = {"01_label": "micoe_bj_scene",
        }

    if "Daisy" not in persistent.cookie_jar:
        persistent.cookie_jar["Daisy"] = {"idle": "cookie_jar/cookie_jar_30.png",
                                          "locked_idle": "cookie_jar/cookie_jar_30_locked.png",
                                          "unlocked": False,
                                          "order": "28",
                                          "gallery": {},
                                          "gallery_image": "cookie_jar/cookie_jar_box_30_",
        }

    persistent.cookie_jar["Daisy"]["gallery_total"] = 1

    persistent.cookie_jar["Daisy"]["gallery_labels"] = {"01_label": "daisy_sex_breed_start",
        }


    for cookie in persistent.cookie_jar:
        cookie_count = 1
        while (cookie_count <= persistent.cookie_jar[cookie]["gallery_total"]):
            cookie_unlock_name = ""
            if cookie_count < 10:
                cookie_unlock_name += "0"
            cookie_unlock_name += str(cookie_count)
            cookie_unlock_name += "_unlocked"
            if cookie_unlock_name not in persistent.cookie_jar[cookie]["gallery"]:
                persistent.cookie_jar[cookie]["gallery"][cookie_unlock_name] = False
            
            cookie_count += 1


label replay_INITS(replay_label, replay_cookie):
    python:
        firstname = persistent.firstname or "Anon"
        jen_name = store.jen_name
        jen_char_name = store.jen_char_name
        deb_name = store.deb_name
        deb_char_name = store.deb_char_name
        player = Player(firstname)
        game = Game()
        sister = Event_Queue("sister")
        erik = Event_Queue("erik")
        mrsj = Event_Queue("mrsj")

    call define_events
    call INIT_FSM
    call INIT_INVENTORY_ITEMS

    define player_name = Character('[firstname]', color="#6f96f1")

    python:
        player.location = L_home_bedroom
        player.pregnancy_chance = 0
        erik._events = [erik_intro, erik_favor, erik_favor_2, erik_card_hunt, erik_crown_card, erik_orcette, erik_orcette_2, erik_bullying,
                        erik_bullying_2, erik_bullying_3, erik_vr, erik_breastfeeding, erik_breastfeeding_2, erik_thief, erik_thief_2,
                        erik_father_forgive, erik_father_treasure, erik_path_split, erik_gf, erik_gf_2, erik_gf_stolen, erik_sex_ed, erik_find_gf]
        mrsj._events = [mrsj_intro, mrsj_yoga_intro, mrsj_yoga_help, mrsj_yoga_help_2, mrsj_poker_night, mrsj_poker_night_2, mrsj_sex_ed,
                        mrsj_sex_ed_prep, mrsj_3some, mrsj_private_yoga]
        for event in erik._events:
            event._done = True
            event._completed = True
        properties =  {
            "firstname": firstname,
            "jen_char_name": jen_char_name,
            "jen_name": jen_name,
            "deb_name": deb_name,
            "deb_char_name": deb_char_name,
            "player": player,
            "game": game,
            "player_name": player_name,
            "sister": sister,
            "erik": erik,
            "mrsj": mrsj,
        }
        for iter_str, iter_var in list(locals().iteritems()):
            if "M_" in iter_str or "S_" in iter_str or "T_" in iter_str or "L_" in iter_str or iter_str.startswith("erik_") or iter_str.startswith("mrsj_"):
                new_var = iter_var
                if "M_diane" in iter_str:
                    new_var.outfit.set_default_outfit_schedule([["shirtless", "shirtless", "shirtless", "shirtless"]])
                properties[iter_str] = new_var



    $ renpy.call_replay(Game.dialog_select(replay_label), properties)
    call screen cookie_jar_gallery(replay_cookie)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
