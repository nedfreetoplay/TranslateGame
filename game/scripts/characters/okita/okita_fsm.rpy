init python:

    T_okita_intro = Trigger("intro")
    T_okita_get_keycode = Trigger("get keycode")
    T_okita_keycode_acquired = Trigger("keycode acquired")
    T_okita_entered_office = Trigger("entered office")
    T_okita_got_items = Trigger("got items")
    T_okita_foam_misshap = Trigger("foam misshap")
    T_okita_get_bifocal_lenses = Trigger("get bifocal lenses")
    T_okita_take_picture_judith = Trigger("take picture judith")
    T_okita_picture_taken = Trigger("picture taken")
    T_okita_xray_perved_classroom = Trigger("xray perved classroom")
    T_okita_xray_perving_aftermath = Trigger("xray perving aftermath")
    T_okita_requested_faptic_engine = Trigger("requested faptic engine")
    T_okita_faptic_get_controller = Trigger("faptic get controller")
    T_okita_got_master_blaster_info = Trigger("got master blaster info")
    T_okita_belt_assembled = Trigger("belt assembled")
    T_okita_belt_assembled_aftermath = Trigger("belt assembled aftermath")
    T_okita_finished_tinkering_belt = Trigger("finished tinkering belt")
    T_okita_get_ingredients = Trigger("get ingredients")
    T_okita_got_all_ingredients = Trigger("got all ingredients")
    T_okita_extracted_cum = Trigger("extracted cum")
    T_okita_brewed_serum = Trigger("brewed serum")
    T_okita_dosed_smith = Trigger("dosed smith")
    T_okita_smith_effects_seen = Trigger("smith effects seen")
    T_okita_serum_took_effect = Trigger("serum took effect")
    T_okita_had_sex = Trigger("had sex")

label okita_fsm_init:
    python:

        S_okita_start = State("start", "I should start focusing on school again")
        S_okita_intro = State("intro", "I wonder if there's anything I can do to fix my grade")
        S_okita_get_keycode = State("get keycode", "Smith usually has coffee in the staff room in the afternon")
        S_okita_enter_office = State("enter office", "With the code, I should be able to get into Okita's office")
        S_okita_get_items_from_office = State("get items from office", "Okita asked me to get three things from her office...")
        S_okita_has_items = State("has items", "I should bring this stuff back to Okita")
        S_okita_foam_misshap = State("foam misshap", "I'll let her get cleaned up")
        S_okita_get_bifocal_lenses = State("get bifocal lenses", "Hmm... Who at school wears glasses?")
        S_okita_take_picture_judith = State("take picture judith", "Judith asked me to meet her at the park this afternoon")
        S_okita_picture_taken = State("picture taken", "Now I can bring Judith's glasses to Okita")
        S_okita_xray_perving = State("xray perving", "Okita asked me to go up to her office. I wonder why")
        S_okita_glasses_completed = State("glasses completed", "That was weird. It's time to head home")
        S_okita_faptic_engine = State("faptic engine", "I wonder if there's anything else I can do to raise my grade")
        S_okita_get_controller_info = State("get controller info", "June usually hangs out in the computer room")
        S_okita_get_controller = State("get controller", "Erik had a Master Blaster controller once!")
        S_okita_belt_assembled = State("belt assembled", "I should meet Okita in her office like she asked")
        S_okita_tinkering_with_belt = State("tinkering with belt", "I'll leave her to work on the belt")
        S_okita_tinkering_with_belt_delay = State("tinkering with belt delay", "I'll leave her to work on the belt")
        S_okita_tinkering_with_belt_delay2 = State("tinkering with belt delay 2", "I'll leave her to work on the belt")
        S_okita_tinkering_with_belt_delay3 = State("tinkering with belt delay 3", "I wonder if she's figured out the issue with the belt")
        S_okita_tired_from_belt = State("tired from belt", "I'll let her rest after that...")
        S_okita_get_ingredients = State("get ingredients", "Where can I find all the stuff she wants?")
        S_okita_extract_cum = State("extract cum", "She asked me to meet her in her office to start")
        S_okita_start_mixing = State("start mixing", "I need to mix the serums together")
        S_okita_dose_smith = State("dose smith", "How can I get Smith to drink her Serum")
        S_okita_wait_for_smith_serum = State("wait for smith serum", "What effect might that Serum have had?")
        S_okita_wait_for_okita_serum = State("wait for okita serum", "What effect might that Serum have had?")
        S_okita_wait_for_okita_serum_delay = State("wait for okita serum delay", "What effect might that Serum have had?")
        S_okita_wait_for_okita_serum_delay2 = State("wait for okita serum delay 2", "What effect might that Serum have had?")
        S_okita_wait_for_okita_serum_delay3 = State("wait for okita serum delay 3", "What effect might that Serum have had?")
        S_okita_is_hypersexual = State("is hypersexual", "I should check to see if her Serum had any major effect")
        S_okita_end = State("end")


        S_okita_start.add(T_okita_intro, S_okita_intro)
        S_okita_intro.add(T_okita_get_keycode, S_okita_get_keycode)
        S_okita_get_keycode.add(T_okita_keycode_acquired, S_okita_enter_office)
        S_okita_enter_office.add(T_okita_entered_office, S_okita_get_items_from_office)
        S_okita_get_items_from_office.add(T_okita_got_items, S_okita_has_items)
        S_okita_has_items.add(T_okita_foam_misshap, S_okita_foam_misshap)
        S_okita_foam_misshap.add(T_okita_get_bifocal_lenses, S_okita_get_bifocal_lenses, actions=["exec", player.increase_grade_science])
        S_okita_get_bifocal_lenses.add(T_okita_take_picture_judith, S_okita_take_picture_judith,
                                       actions = ["location", [M_judith, {"place": L_park}],
                                                  "force", [M_judith, {"tod": 1}],
                                                 ],
                                       )
        S_okita_take_picture_judith.add(T_okita_picture_taken, S_okita_picture_taken,
                                        actions = ["unforce", M_judith],
                                        )
        S_okita_picture_taken.add(T_okita_xray_perved_classroom, S_okita_xray_perving,
                                  actions = ["location", {"place": L_school_okitaoffice},
                                             "force", {"flag": True},
                                            ],
                                  )
        S_okita_xray_perving.add(T_okita_xray_perving_aftermath, S_okita_glasses_completed,
                                 actions = ["unforce", None],
                                 )
        S_okita_glasses_completed.add(T_okita_requested_faptic_engine, S_okita_faptic_engine, actions=["exec", player.increase_grade_science])
        S_okita_faptic_engine.add(T_okita_faptic_get_controller, S_okita_get_controller_info)
        S_okita_get_controller_info.add(T_okita_got_master_blaster_info, S_okita_get_controller)
        S_okita_get_controller.add(T_okita_belt_assembled, S_okita_belt_assembled,
                                   actions = ["location", {"place": L_school_okitaoffice},
                                              "force", {"flag": True},
                                             ],
                                   )
        S_okita_belt_assembled.add(T_okita_belt_assembled_aftermath, S_okita_tinkering_with_belt,
                                   actions = ["unforce", None],
                                   )
        S_okita_tinkering_with_belt.add(T_all_sleep, S_okita_tinkering_with_belt_delay)
        S_okita_tinkering_with_belt_delay.add(T_all_sleep, S_okita_tinkering_with_belt_delay2)
        S_okita_tinkering_with_belt_delay2.add(T_all_sleep, S_okita_tinkering_with_belt_delay3)
        S_okita_tinkering_with_belt_delay3.add(T_okita_finished_tinkering_belt, S_okita_tired_from_belt, actions=["exec", player.increase_grade_science])
        S_okita_tired_from_belt.add(T_okita_get_ingredients, S_okita_get_ingredients,
                                    actions = ["set", "Q3 completed",
                                               "exec", L_forest.unlock,
                                               "location", [M_annie, {"place": L_school_smithoffice,
                                                                      "condition": "not player.has_item('tissue')",
                                                                      }
                                                            ],
                                               "force", [M_annie, {"tod": 1}],
                                              ]
                                    )
        S_okita_get_ingredients.add(T_okita_got_all_ingredients, S_okita_extract_cum,
                                    actions = ["unforce", M_annie]
                                    )
        S_okita_extract_cum.add(T_okita_extracted_cum, S_okita_start_mixing)
        S_okita_start_mixing.add(T_okita_brewed_serum, S_okita_dose_smith)
        S_okita_dose_smith.add(T_okita_dosed_smith, S_okita_wait_for_smith_serum)
        S_okita_wait_for_smith_serum.add(T_okita_smith_effects_seen, S_okita_wait_for_okita_serum)
        S_okita_wait_for_okita_serum.add(T_all_sleep, S_okita_wait_for_okita_serum_delay)
        S_okita_wait_for_okita_serum_delay.add(T_all_sleep, S_okita_wait_for_okita_serum_delay2)
        S_okita_wait_for_okita_serum_delay2.add(T_all_sleep, S_okita_wait_for_okita_serum_delay3)
        S_okita_wait_for_okita_serum_delay3.add(T_okita_serum_took_effect, S_okita_is_hypersexual)
        S_okita_is_hypersexual.add(T_okita_had_sex, S_okita_end, actions=["exec", player.increase_grade_science, "exec", A_science_experiments.unlock])

        M_okita.add(S_okita_start, S_okita_intro, S_okita_get_keycode,
                    S_okita_enter_office, S_okita_get_items_from_office,
                    S_okita_has_items, S_okita_foam_misshap, 
                    S_okita_get_bifocal_lenses, S_okita_take_picture_judith,
                    S_okita_picture_taken, S_okita_xray_perving, S_okita_glasses_completed,
                    S_okita_faptic_engine, S_okita_get_controller_info, S_okita_get_controller,
                    S_okita_belt_assembled, S_okita_tinkering_with_belt, 
                    S_okita_tinkering_with_belt_delay, S_okita_tinkering_with_belt_delay2, 
                    S_okita_tinkering_with_belt_delay3, S_okita_tired_from_belt,
                    S_okita_get_ingredients, S_okita_extract_cum, S_okita_start_mixing,
                    S_okita_dose_smith, S_okita_wait_for_smith_serum,
                    S_okita_wait_for_okita_serum, S_okita_wait_for_okita_serum_delay,
                    S_okita_wait_for_okita_serum_delay2, S_okita_wait_for_okita_serum_delay3,
                    S_okita_is_hypersexual, S_okita_end)
    return

label okita_machine_init:
    python:
        M_okita = Machine("Okita", default_loc = [[L_school_scienceclassroom, L_school_scienceclassroom, L_school_okitaoffice, L_NULL],
                                                  [L_NULL, L_NULL, L_NULL, L_NULL]
                                                  ],
                          vars = {"sex speed":0.175,
                                  "office locked": True,
                                  "glasses assembly fail": False,
                                  "belt assembly fail": False,
                                  "talked with veronica": False,
                                  "talked to annie": False,
                                  "in augmented reality": True,
                                  "repeatable unlocked": False,
                                  "first time repeatable": True,
                                  "Q3 completed":False,
                                },
                        )
        M_okita.set_priority(1)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
