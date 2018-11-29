label bissette_triggers_init:
    python:

        T_bissette_improvement_challenge = Trigger("improvement challenge", "Default")
        T_bissette_challenge_thoughts = Trigger("challenge thoughts", "Default")
        T_bissette_require_dictionary = Trigger("require dictionary", "Default")
        T_bissette_check_library = Trigger("check library", "Default")
        T_bissette_check_library_shelf = Trigger("check library shelf", "Default")
        T_bissette_missing_pages = Trigger("missing pages", "Default")
        T_bissette_judith_borrow_dictionary = Trigger("Judith borrow dictionary", "Default")
        T_bissette_broken_printer = Trigger("broken printer", "Default")
        T_bissette_june_scan_pages = Trigger("June scan pages", "Default")
        T_bissette_june_printer_error = Trigger("June printer error", "Default")
        T_bissette_private_study = Trigger("private study", "Default")
        T_bissette_smith_threat = Trigger("Smith threat", "Default")
        T_bissette_ask_dexter = Trigger("ask Dexter", "Default")
        T_bissette_ask_erik = Trigger("ask Erik", "Default")
        T_bissette_ask_martinez = Trigger("ask Martinez", "Default")
        T_bissette_return_books = Trigger("return books", "Default")
        T_bissette_do_assignment = Trigger("do assignment", "Default")
        T_bissette_french_poem = Trigger("French poem", "Default")
        T_bissette_mia_poem_advice = Trigger("Mia poem advice", "Default")
        T_bissette_reference_book_found = Trigger("reference book found", "Default")
        T_bissette_print_assignment = Trigger("print assignment", "Default")
        T_bissette_roxxy_convince = Trigger("Roxxy convince", "Default")
        T_bissette_roxxy_deal = Trigger("Roxxy deal", "Default")
        T_bissette_bridget_pompoms_steal = Trigger("Bridget pompoms steal", "Default")
        T_bissette_jenny_deal = Trigger("jenny deal", "Default")
        T_bissette_jenny_paid = Trigger("jenny paid", "Default")
        T_bissette_roxxy_meet_inform = Trigger("Roxxy meet inform", "Default")
        T_bissette_roxxy_jenny_hangout = Trigger("Roxxy Jenny hangout", "Default")
        T_bissette_roxxy_jenny_spied = Trigger("Roxxy Jenny spied", "Default")
        T_bissette_quiz_warning = Trigger("quiz warning", "Default")
        T_bissette_quiz_pass = Trigger("quiz pass", "Default")
        T_bissette_sexy_time = Trigger("sexy time", "Default")
        T_bissette_smith_pleased = Trigger("Smith pleased", "Default")
    return

label bissette_fsm_init:
    python:

        S_bissette_start = State("start")
        S_bissette_intro = State("intro", "I should inform Miss Bissette about my return to school.")
        S_bissette_challenge = State("challenge", "The private tutoring Miss Bissette talked about seemed very interesting.")
        S_bissette_tutoring_delay = State("tutoring delay", "I should probably talk to Miss Bissette about that private tutoring tomorrow.")
        S_bissette_tutoring = State("tutoring", "I should probably talk to Miss Bissette about that private tutoring.")
        S_bissette_find_dictionary = State("find dictionary", "I need to find a French dictionary for the tutoring lesson Miss Bissette is going to give me.")
        S_bissette_get_dictionary = State("get dictionary", "I need to get the French dictionary from the library shelf.")
        S_bissette_check_dictionary = State("check dictionary", "I need to check about the missing pages in the French dictionary out with Miss Bissette.")
        S_bissette_find_full_dictionary = State("find full dictionary", "I need to find a full French dictionary. Miss Bissette thinks Judith would have one.")
        S_bissette_scan_missing_pages = State("scan missing pages", "I need to scan the missing pages from the full French dictionary. There shoud be one in the Computer Lab.")
        S_bissette_fix_printer = State("fix printer", "I need to fix the printer for the missing pages. Maybe I should try hitting it harder ?")
        S_bissette_study = State("study", "I should return to Miss Bissette to have that tutoring lesson.")
        S_bissette_smith_report = State("smith report", "I should talk to Miss Bissette about my next assignment.")
        S_bissette_find_food_book = State("find food book", "I need to a book to help me with my assignment on food.")
        S_bissette_jane_return_books = State("Jane return books", "The librarian needs my help to return the overdue books from Dexter, Erik and the Martinez twins.")
        S_bissette_got_dexters_book = State("got Dexter's book", "I have Dexter's book. Erik and the Martinez twins left to go.")
        S_bissette_got_dexters_martinez_books = State("got Dexter's & Martinez's book", "I have Dexter's and the Martinez twins' books. Erik is the last one left.")
        S_bissette_got_dexters_eriks_books = State("got Dexter's & Erik's book", "I have Dexter's and Erik's books. The Martinez twins are the last ones left.")
        S_bissette_got_eriks_book = State("got Erik's book", "I have Erik's book. Dexter and the Martinez twins left to go.")
        S_bissette_got_eriks_dexters_books = State("got Erik's & Dexter's book", "I have Erik's and Dexter's books. The Martinez twins are the last ones left.")
        S_bissette_got_eriks_martinez_books = State("got Erik's & Martinez's book", "I have Erik's and the Martinez twins' books. Dexter is the last one left.")
        S_bissette_got_martinez_book = State("got Martinez's book", "I have the Martinez twins' book. Dexter and Erik left to go.")
        S_bissette_got_martinez_dexters_books = State("got Martinez Dexter's book", "I have the Martinez twins' and Dexter's books. Erik is the last one left.")
        S_bissette_got_martinez_eriks_books = State("got Martinez Erik's book", "I have the Martinez twins' and Erik's books. Dexter is the last one left.")
        S_bissette_return_overdue_books = State("return overdue books", "I have all the overdue books. I should return them to the librarian.")
        S_bissette_french_food_assignment = State("French food assignment", "Now that I have the reference book, I should complete the assignment at home.")
        S_bissette_hand_in_assignment = State("hand in assignment", "I should hand in my completed assignment to Miss Bissette.")
        S_bissette_poem_assignment = State("poem assignment", "I should talk to Miss Bissette about my next assignment.")
        S_bissette_find_poem_reference_book = State("find poem reference book", "I need to find a book about romace for my poem assignment.")
        S_bissette_reference_book_search = State("reference book search", "Mia mentioned a book that I could use that Judith was last seen reading in the Library Back Room.")
        S_bissette_do_poem_assignment = State("do poem assignment", "Now that I have the book, I should do the assignment at home.")
        S_bissette_print_poem_assignment = State("print poem assignment", "I need to print out my assignment to hand in.")
        S_bissette_hand_in_poem_assignment = State("hand in poem assignment", "I should hand in my completed assignment to Miss Bissette.")
        S_bissette_office_meetup = State("office meetup", "Miss Bissette asked me to meet her in her office during the evening.")
        S_bissette_roxxy_exam_convince = State("Roxxy exam convince", "I need to try convince Roxxy to attend the French exam.")
        S_bissette_roxxy_pom_poms = State("Roxxy pom poms", "I need to retrieve Roxxy's pom poms from Coach Bridget to convince Roxxy to attend the French exam.")
        S_bissette_roxxy_pom_poms_deal = State("Roxxy pom poms deal", "I need to return the pom poms back to Roxxy for our deal.")
        S_bissette_roxxy_cheerleader_deal = State("Roxxy cheerleader deal", "I need to ask [jen_name] to help Roxxy so she will attend the French exam.")
        S_bissette_jenny_mentoring_payment = State("Jenny mentoring payment", "I need to pay [jen_name] $500 to help mentor Roxxy in cheerleading.")
        S_bissette_roxxy_deal_confirmation = State("Roxxy deal conformation", "I should go tell Roxxy that [jen_name] has agreed to mentor her.")
        S_bissette_roxxy_jenny_mentoring = State("Roxxy Jenny mentoring", "I should head home and make sure [jen_name] doesn't flake on Roxxy.")
        S_bissette_roxxy_jenny_spying = State("Roxxy Jenny spying", "I should go check up on Roxxy and [jen_name] in the Upstairs Bedroom.")
        S_bissette_roxxy_convinced = State("Roxxy Convinced", "I need to inform Miss Bissette that Roxxy will be attending the exam.")
        S_bissette_quiz = State("quiz", "I need to be prepared before the French quiz during class.")
        S_bissette_wine_sampling = State("wine sampling", "Miss Bissette has offered to drink some wine with her during the evening in her office.")
        S_bissette_smith_final_report = State("Smith final report", "I should talk to Miss Bissette about what we did last night.")
        S_bissette_end = State("end")


        S_bissette_start.add(T_bridget_workout, S_bissette_intro, actions=["exec", game.unlock_ui])
        S_bissette_intro.add(T_bissette_improvement_challenge, S_bissette_challenge, actions=["exec", L_library_front.unlock])
        S_bissette_challenge.add(T_bissette_challenge_thoughts, S_bissette_tutoring_delay)
        S_bissette_tutoring_delay.add(T_all_sleep, S_bissette_tutoring)
        S_bissette_tutoring.add(T_bissette_require_dictionary, S_bissette_find_dictionary)
        S_bissette_find_dictionary.add(T_bissette_check_library, S_bissette_get_dictionary)
        S_bissette_get_dictionary.add(T_bissette_check_library_shelf, S_bissette_check_dictionary)
        S_bissette_check_dictionary.add(T_bissette_missing_pages, S_bissette_find_full_dictionary)
        S_bissette_find_full_dictionary.add(T_bissette_judith_borrow_dictionary, S_bissette_scan_missing_pages)
        S_bissette_scan_missing_pages.add(T_bissette_broken_printer, S_bissette_fix_printer)
        S_bissette_fix_printer.add(T_bissette_june_scan_pages, S_bissette_study,
                                   actions = ["clear", "judith return dictionary"]
                                   )
        S_bissette_fix_printer.add(T_bissette_june_printer_error, S_bissette_fix_printer,
                                   actions = ["set", "printer fix fail"]
                                   )
        S_bissette_study.add(T_bissette_private_study, S_bissette_smith_report,
                             actions = ["exec", player.increase_grade_french]
                             )
        S_bissette_smith_report.add(T_bissette_smith_threat, S_bissette_find_food_book)
        S_bissette_find_food_book.add(T_bissette_check_library, S_bissette_jane_return_books)
        S_bissette_jane_return_books.add(T_bissette_ask_dexter, S_bissette_got_dexters_book,
                                         actions = ["clear", "dexters book search"]
                                         )
        S_bissette_got_dexters_book.add(T_bissette_ask_erik, S_bissette_got_dexters_eriks_books,
                                        actions = ["clear", "eriks book search"]
                                        )
        S_bissette_got_dexters_book.add(T_bissette_ask_martinez, S_bissette_got_dexters_martinez_books,
                                        actions = ["clear", "martinez book search"]
                                        )
        S_bissette_got_dexters_martinez_books.add(T_bissette_ask_erik, S_bissette_return_overdue_books,
                                                  actions = ["clear", "eriks book search"]
                                                  )
        S_bissette_got_dexters_eriks_books.add(T_bissette_ask_martinez, S_bissette_return_overdue_books,
                                               actions = ["clear", "martinez book search"]
                                               )
        S_bissette_jane_return_books.add(T_bissette_ask_erik, S_bissette_got_eriks_book,
                                         actions = ["clear", "eriks book search"]
                                         )
        S_bissette_got_eriks_book.add(T_bissette_ask_dexter, S_bissette_got_eriks_dexters_books,
                                      actions = ["clear", "dexters book search"]
                                      )
        S_bissette_got_eriks_book.add(T_bissette_ask_martinez, S_bissette_got_eriks_martinez_books,
                                      actions = ["clear", "martinez book search"]
                                      )
        S_bissette_got_eriks_dexters_books.add(T_bissette_ask_martinez, S_bissette_return_overdue_books,
                                               actions = ["clear", "martinez book search"]
                                               )
        S_bissette_got_eriks_martinez_books.add(T_bissette_ask_dexter, S_bissette_return_overdue_books,
                                                actions = ["clear", "dexters book search"]
                                                )
        S_bissette_jane_return_books.add(T_bissette_ask_martinez, S_bissette_got_martinez_book,
                                         actions = ["clear", "martinez book search"]
                                         )
        S_bissette_got_martinez_book.add(T_bissette_ask_dexter, S_bissette_got_martinez_dexters_books,
                                         actions = ["clear", "dexters book search"]
                                         )
        S_bissette_got_martinez_book.add(T_bissette_ask_erik, S_bissette_got_martinez_eriks_books,
                                         actions = ["clear", "eriks book search"]
                                         )
        S_bissette_got_martinez_dexters_books.add(T_bissette_ask_erik, S_bissette_return_overdue_books,
                                                  actions = ["clear", "eriks book search"]
                                                  )
        S_bissette_got_martinez_eriks_books.add(T_bissette_ask_dexter, S_bissette_return_overdue_books,
                                                actions = ["clear", "dexters book search"]
                                                )
        S_bissette_return_overdue_books.add(T_bissette_return_books, S_bissette_french_food_assignment,
                                            actions = ["clear", "martinez book search",
                                                       "clear", "eriks book search",
                                                       "clear", "dexters book search",
                                                       ]
                                            )
        S_bissette_french_food_assignment.add(T_bissette_do_assignment, S_bissette_hand_in_assignment)
        S_bissette_hand_in_assignment.add(T_bissette_private_study, S_bissette_poem_assignment,
                                          actions = ["exec", player.increase_grade_french]
                                          )
        S_bissette_poem_assignment.add(T_bissette_french_poem, S_bissette_find_poem_reference_book,
                                       actions = ["location", [M_mia ,{"place": L_library}],
                                                  "force", [M_mia, {"tod": 1}],
                                                  ],
                                       )
        S_bissette_find_poem_reference_book.add(T_bissette_mia_poem_advice, S_bissette_reference_book_search)
        S_bissette_reference_book_search.add(T_bissette_reference_book_found, S_bissette_do_poem_assignment,
                                             actions = ["set", "mia book feedback"]
                                             )
        S_bissette_do_poem_assignment.add(T_bissette_do_assignment, S_bissette_print_poem_assignment,
                                          actions = ["unforce", M_mia]
                                          )
        S_bissette_print_poem_assignment.add(T_bissette_print_assignment, S_bissette_hand_in_poem_assignment)
        S_bissette_hand_in_poem_assignment.add(T_bissette_private_study, S_bissette_office_meetup,
                                               actions = ["set", "meet in office",
                                                          "exec", player.increase_grade_french,
                                                         ]
                                               )
        S_bissette_office_meetup.add(T_bissette_roxxy_convince, S_bissette_roxxy_exam_convince)
        S_bissette_roxxy_exam_convince.add(T_bissette_roxxy_deal, S_bissette_roxxy_pom_poms)
        S_bissette_roxxy_pom_poms.add(T_bissette_bridget_pompoms_steal, S_bissette_roxxy_pom_poms_deal)
        S_bissette_roxxy_pom_poms_deal.add(T_bissette_roxxy_deal, S_bissette_roxxy_cheerleader_deal)
        S_bissette_roxxy_cheerleader_deal.add(T_bissette_jenny_deal, S_bissette_jenny_mentoring_payment)
        S_bissette_jenny_mentoring_payment.add(T_bissette_jenny_paid, S_bissette_roxxy_deal_confirmation)
        S_bissette_roxxy_deal_confirmation.add(T_bissette_roxxy_meet_inform, S_bissette_roxxy_jenny_mentoring)
        S_bissette_roxxy_jenny_mentoring.add(T_bissette_roxxy_jenny_hangout, S_bissette_roxxy_jenny_spying)
        S_bissette_roxxy_jenny_spying.add(T_bissette_roxxy_jenny_spied, S_bissette_roxxy_convinced)
        S_bissette_roxxy_convinced.add(T_bissette_quiz_warning, S_bissette_quiz)
        S_bissette_quiz.add(T_bissette_quiz_pass, S_bissette_wine_sampling,
                            actions = ["set", "night visit"],
                            )
        S_bissette_wine_sampling.add(T_bissette_sexy_time, S_bissette_smith_final_report,
                                     actions = ["clear", "meet in office"]
                                     )
        S_bissette_smith_final_report.add(T_bissette_smith_pleased, S_bissette_end,
                                          actions = ["exec", player.increase_grade_french, "exec", A_excellent_francais.unlock],
                                          )

        M_bissette = Machine("Bissette", default_loc = [[L_school_frenchclassroom, L_school_frenchclassroom, L_school_bissetteoffice, L_NULL], 
                                                        [L_NULL, L_NULL, L_NULL, L_NULL]
                                                        ],
                             vars = {"sex speed": .175,
                                     "office first visit": True,
                                     "printer fix fail": False,
                                     "judith return dictionary": True,
                                     "dexters book search": False,
                                     "eriks book search": False,
                                     "martinez book search": False,
                                     "mia book feedback": False,
                                     "meet in office": False,
                                     "night visit": False,
                                     "change angle": False,
                                    },
        )
        M_bissette.set_priority(1)
        M_bissette.add(S_bissette_start, S_bissette_intro, S_bissette_challenge,
                       S_bissette_tutoring_delay, S_bissette_tutoring,
                       S_bissette_find_dictionary, S_bissette_get_dictionary,
                       S_bissette_check_dictionary, S_bissette_find_full_dictionary,
                       S_bissette_scan_missing_pages, S_bissette_fix_printer,
                       S_bissette_study, S_bissette_smith_report,
                       S_bissette_find_food_book, S_bissette_jane_return_books,
                       S_bissette_got_dexters_book, S_bissette_got_dexters_martinez_books,
                       S_bissette_got_dexters_eriks_books, S_bissette_got_eriks_book,
                       S_bissette_got_eriks_dexters_books, S_bissette_got_eriks_martinez_books,
                       S_bissette_got_martinez_book, S_bissette_got_martinez_dexters_books,
                       S_bissette_got_martinez_eriks_books, S_bissette_return_overdue_books,
                       S_bissette_french_food_assignment, S_bissette_hand_in_assignment,
                       S_bissette_poem_assignment, S_bissette_find_poem_reference_book,
                       S_bissette_reference_book_search, S_bissette_do_poem_assignment,
                       S_bissette_print_poem_assignment,
                       S_bissette_hand_in_poem_assignment, S_bissette_office_meetup,
                       S_bissette_roxxy_exam_convince, S_bissette_roxxy_pom_poms,
                       S_bissette_roxxy_pom_poms_deal, S_bissette_roxxy_cheerleader_deal,
                       S_bissette_jenny_mentoring_payment, S_bissette_roxxy_deal_confirmation,
                       S_bissette_roxxy_jenny_mentoring, S_bissette_roxxy_jenny_spying,
                       S_bissette_roxxy_convinced, S_bissette_quiz, S_bissette_wine_sampling,
                       S_bissette_smith_final_report,
                       S_bissette_end
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
